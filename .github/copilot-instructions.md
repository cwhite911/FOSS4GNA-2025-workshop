# Copilot instructions for FOSS4GNA-2025-workshop

This repo is a hands-on workshop for building GRASS GIS addons in Python (with a small C example). Agents should follow these conventions and workflows to be productive.

## Architecture and key locations

- Workshop content lives under `workshop/`
  - `part_1_grass/`: intro notebooks and a simple Python script (`my_grass_script.py`) using `grass.tools.Tools` inside a GRASS session.
  - `part_2_addons/`: curriculum and guidance (`README.md`).
  - `examples/`:
    - `r.myaddon/`: canonical Python addon example (`Makefile`, `r.myaddon.py`, `testsuite/`).
    - `r.caddon.example/`: minimal C addon example (`main.c`, `Makefile`).
- Repo-wide contribution instructions for style and docs are under `.github/instructions/`:
  - `general.instructions.md` (GRASS best practices),
  - `docs.instructions.md` (docs style and module man page format),
  - `c.instructions.md` (C style and includes).

## GRASS Python development patterns

- Use `grass.tools.Tools` within a managed GRASS session for calling modules. Typical pattern:
  - Append GRASS Python path with: `subprocess.check_output(["grass", "--config", "python_path"], text=True).strip()`.
  - Create a project with `gs.create_project(path=..., epsg=...)`.
  - Initialize a session with `with gs.setup.init(path) as session:` then construct `Tools(session=session)`.
- Respect computational region and mask policies from `general.instructions.md`. Prefer temporary region/mask via context managers: `RegionManager` and `MaskManager`.
- For addons, follow the cookiecutter-style header and GRASS parser comments (see `workshop/examples/r.myaddon/r.myaddon.py`). Define `%module`, `%keyword`, and options like `%option G_OPT_R_INPUT`.

## Building and installing addons

- Python addon: `workshop/examples/r.myaddon/Makefile` uses GRASS build rules. Set `PGM=r.myaddon` and include `$(MODULE_TOPDIR)/include/Make/Script.make`. Default target `script` builds the Python module.
- C addon: `workshop/examples/r.caddon.example/Makefile` includes `Make/Module.make` with `PGM = r.caddon.example`, and links `$(RASTERLIB) $(GISLIB) $(DATETIMELIB)`.
- `MODULE_TOPDIR = ../..` assumes building from within the workshop tree under a GRASS source-like layout during exercises.

## Tests and how they run

- Tests live in `workshop/examples/r.myaddon/testsuite/` and use `pytest` with GRASS fixtures:
  - `conftest.py` creates a temporary GRASS project and a `TemporaryMapsetSession` per test, sets region to 20x20, and seeds a raster `data = 1`.
  - `test_r_myaddon.py` demonstrates calling `Tools(session=session)` and invoking the addon via `tools.r_myaddon(...)`.
- When writing new code, mirror these fixtures for isolation. Expect functions to accept a `session` or run within `with gs.setup.init(...):`.

## Linting, formatting, and hooks

- Pre-commit is configured in `.pre-commit-config.yaml` and runs:
  - Ruff (lint + format) for Python, Flake8, Markdownlint, Yamllint.
  - Biome for web/JSON-like files.
  - Clang-Format 18 for C/C++.
  - UV hooks to keep Python lock/export in sync.
- On commit, hooks may modify files; re-add and commit again. For manual runs:
  - `pre-commit run --all-files`
  - To apply formatters only: `pre-commit run ruff-format --all-files` or `pre-commit run clang-format --all-files`.

## Dev environment

- Devcontainer (`.devcontainer/devcontainer.json`) installs extensions and runs `uv sync --locked`. GRASS presence is expected; scripts detect its Python path via `grass --config python_path`.
- Python requires `>=3.13` (see `pyproject.toml`). Dependencies: `ipyleaflet`; dev: `cookiecutter`, `ipykernel`, `pre-commit`, `ruff`.

## Project-specific conventions

- Do not change the global computational region or MASK; use temporary contexts and document any deviations.
- Output maps must be written to the current mapset; accept inputs from any mapset name.
- Use GRASS messaging style for user-facing strings and include histories (e.g., `gs.raster_history`).
- Module naming: `PGM` controls names across source, docs, and installed binaries. Keep names consistent (e.g., `r.myaddon`, `r.myaddon.py`, `r.myaddon.html`).

## Useful references in-repo

- Example addon: `workshop/examples/r.myaddon/r.myaddon.py`
- Testing fixtures: `workshop/examples/r.myaddon/testsuite/conftest.py`
- C example: `workshop/examples/r.caddon.example/main.c`
- GRASS guidance: `.github/instructions/*.md`

If anything here is unclear (e.g., how you expect addons to be built in this workshop context or how tests are invoked in CI), reply with specifics and we’ll refine these instructions.
