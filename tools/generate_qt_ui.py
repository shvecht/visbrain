#!/usr/bin/env python3
"""Regenerate Qt Designer artifacts used by Visbrain's interfaces.

This helper locates all ``.ui`` and ``.qrc`` files under the GUI interface
packages and feeds them to the PySide6 code generators. It can either update
in place or simply check whether the committed Python artifacts are stale.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Callable, Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent
GUI_ROOT = REPO_ROOT / "visbrain" / "gui"
INTERFACE_TOKEN = "interface"
VISUALS_ROOT = REPO_ROOT / "visbrain" / "visuals"

# Additional Qt Designer search roots.  Each entry provides a directory and an
# optional predicate used to filter rglob results.
QT_SEARCH_SCOPES: tuple[tuple[Path, Callable[[Path], bool]], ...] = (
    (GUI_ROOT, lambda path: INTERFACE_TOKEN in path.parts),
    (VISUALS_ROOT, lambda _path: True),
)


class GeneratorError(RuntimeError):
    """Raised when a Qt code generation step fails."""


def _require_tool(name: str) -> str:
    """Return the path to *name* or abort with a clear error message."""

    path = shutil.which(name)
    if path is None:
        raise SystemExit(
            f"Unable to locate '{name}'. Ensure PySide6 is installed in the active "
            "environment."
        )
    return path


def _iter_interface_files(pattern: str) -> Iterable[Path]:
    """Yield interface files matching *pattern* relative to the repo root."""

    seen: set[Path] = set()
    for root, predicate in QT_SEARCH_SCOPES:
        for path in sorted(root.rglob(pattern)):
            resolved = path.resolve()
            if not predicate(resolved):
                continue
            if resolved in seen:
                continue
            seen.add(resolved)
            yield resolved


def _normalize_ui_imports(content: str) -> str:
    """Replace direct PySide imports with :mod:`visbrain.qt` wrappers."""

    header_marker = content.find(
        "WARNING! All changes made in this file will be lost when recompiling UI file!"
    )
    if header_marker == -1:
        raise GeneratorError("Unable to locate Qt UIC header in generated output")
    header_end = content.find("\n\n", header_marker)
    if header_end == -1:
        header_end = content.find("\r\n\r\n", header_marker)
    if header_end == -1:
        raise GeneratorError("Unable to determine end of Qt UIC header")
    header_end += 2
    header = content[:header_end]
    body = content[header_end:]

    pattern = re.compile(r"from PySide6\.(Qt\w+) import \((.*?)\)\n", re.DOTALL)
    modules: dict[str, list[str]] = {}

    def _capture(match: re.Match[str]) -> str:
        module = match.group(1)
        names = match.group(2).replace("\n", " ").replace(",", " ").split()
        modules[module] = [name for name in names if name]
        return ""

    body = pattern.sub(_capture, body)

    supported = {"QtCore", "QtGui", "QtWidgets"}
    if not set(modules).issubset(supported):
        unsupported = ", ".join(sorted(set(modules) - supported))
        raise GeneratorError(
            "Generated UI references unsupported Qt modules: " f"{unsupported}"
        )

    for module, names in modules.items():
        for name in sorted(set(names), key=len, reverse=True):
            replacement = f"{module}.{name}" if name != "Qt" else f"{module}.Qt"
            body = re.sub(rf"\b{name}\b", replacement, body)

    return header + "from visbrain.qt import QtCore, QtGui, QtWidgets\n\n" + body


def _should_normalize(ui_file: Path) -> bool:
    """Return ``True`` when *ui_file* should use :mod:`visbrain.qt` imports."""

    try:
        ui_file.relative_to(VISUALS_ROOT)
    except ValueError:
        return False
    return True


def _run_generator(command: list[str]) -> str:
    """Execute *command* and return the generated file contents."""

    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = Path(tmpdir) / "generated.py"
        result = subprocess.run(
            [*command, "-o", str(output_path)],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.stderr:
            # Propagate warnings from Qt's generators to the caller.
            print(result.stderr.rstrip(), file=sys.stderr)
        if result.returncode != 0:
            raise GeneratorError(
                f"Command {' '.join(command)} failed with exit code {result.returncode}"
            )
        return output_path.read_text(encoding="utf-8")


def _generate_ui(uic_exe: str, ui_file: Path) -> str:
    """Return the Python code generated from *ui_file* using PySide's UIC."""

    command = [uic_exe, "-g", "python", str(ui_file)]
    content = _run_generator(command)
    if _should_normalize(ui_file):
        content = _normalize_ui_imports(content)
    return content


def _generate_qrc(rcc_exe: str, qrc_file: Path) -> str:
    """Return the Python resources module generated from *qrc_file*."""

    command = [rcc_exe, str(qrc_file)]
    return _run_generator(command)


def _write_or_check(path: Path, content: str, check_only: bool) -> bool:
    """Write *content* to *path* or compare it during check mode.

    Returns ``True`` when a difference is detected.
    """

    path = path.resolve()
    existing = path.read_text(encoding="utf-8") if path.exists() else None
    if check_only:
        if existing != content:
            rel = path.relative_to(REPO_ROOT)
            print(f"Stale generated file: {rel}", file=sys.stderr)
            return True
        return False

    if existing == content:
        return False

    path.write_text(content, encoding="utf-8")
    rel = path.relative_to(REPO_ROOT)
    print(f"Updated {rel}")
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify that generated files match the Qt Designer sources.",
    )
    args = parser.parse_args(argv)

    uic_exe = _require_tool("pyside6-uic")
    qrc_exe = shutil.which("pyside6-rcc")

    had_differences = False

    for ui_file in _iter_interface_files("*.ui"):
        target = ui_file.with_suffix(".py")
        content = _generate_ui(uic_exe, ui_file)
        if _write_or_check(target, content, args.check):
            had_differences = True

    qrc_files = list(_iter_interface_files("*.qrc"))
    if qrc_files and qrc_exe is None:
        raise SystemExit(
            "Resource files found but 'pyside6-rcc' is unavailable. Install PySide6 "
            "or adjust your PATH."
        )

    if qrc_exe is not None:
        for qrc_file in qrc_files:
            target = qrc_file.with_name(f"{qrc_file.stem}_rc.py")
            content = _generate_qrc(qrc_exe, qrc_file)
            if _write_or_check(target, content, args.check):
                had_differences = True

    if args.check and had_differences:
        print("Qt Designer artifacts are out of date.", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
