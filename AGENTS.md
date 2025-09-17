# Agent Instructions

## Scope
These guidelines apply to the entire repository unless a subdirectory adds its own `AGENTS.md` with more specific directions.

## Environment Setup
- Use Python 3.9+.
- Install tooling with `python -m pip install -r requirements/dev.txt` before running tests or linters.

## Required Checks
When you modify any files:
1. Run `make flake` for linting.
2. Run `pytest` (or `make test`) for automated tests.
3. Run additional commands mentioned in the relevant documentation if your changes affect packaging (e.g., `python -m build`).
Document all executed commands and their outcomes in the final response.

## Coding Conventions
- Prefer modern Python features compatible with the supported versions (3.9+).
- Avoid introducing new runtime downloads; package assets via the build system instead.
- Keep Makefile targets compatible with POSIX sh.

## Documentation
- Update the modernization roadmap under `docs/modernization/` when you make significant plan adjustments.
- Keep README instructions aligned with the current tooling workflow.

## Testing Notes
- GUI smoke tests may require a display; prefer headless-friendly flags such as `--visbrain-show=False` when adding or updating examples.

## Pull Requests
- Provide concise summaries highlighting the impact and include the commands run for validation.
- Ensure the working tree is clean before completion.
