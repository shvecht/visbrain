"""Qt icon resource helpers."""
from __future__ import annotations

import sys
from importlib import import_module
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

__all__ = ["load_icon"]


def _load_impl():
    module_name = f"{__name__}._impl"
    module = sys.modules.get(module_name)
    if module is not None:
        return module

    try:
        return import_module(module_name)
    except ModuleNotFoundError:
        icons_py = Path(__file__).resolve().parent.parent / "icons.py"
        spec = spec_from_file_location(module_name, icons_py)
        if spec is None or spec.loader is None:
            raise ModuleNotFoundError(
                f"Unable to load icon helpers from {icons_py!s}"
            )
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules[module_name] = module
        return module


load_icon = _load_impl().load_icon
