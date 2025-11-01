# Copilot instructions for FOSS4GNA-2025-workshop

This repo is a hands-on workshop for building GRASS GIS addons in Python (plus one C example). Use this guide to be productive quickly in this codebase.

## Layout you’ll use

- `workshop/part_1_grass/`: intro notebooks and Python scripts (`my_grass_script.py`, `grass_tools.py`).
- `workshop/examples/`:
  - `r.myaddon/`: canonical Python addon (Makefile, `r.myaddon.py`, `testsuite/`).
  - `r.caddon.example/`: minimal C addon (Makefile, `main.c`).
- `workshop/part_2_addons/`: curriculum and guidance (`Intro.md`, `Addon_Structure.md`, `Developing_an_addon.md`).
- Repo rules: `.github/instructions/` (read `general.instructions.md`, `docs.instructions.md`, `python.instructions.md`, `c.instructions.md`).

## Python patterns that matter

- Always run GRASS tools via a managed session and `grass.tools.Tools`:
  - Append GRASS’s Python path: `grass --config python_path`.
  - Create/init: `gs.create_project(path=..., epsg=...)`; `with gs.setup.init(path) as session: tools = Tools(session=session)`.
- Respect region/mask: use `gs.RegionManager()` and `gs.MaskManager()` (don’t change global region or MASK). See `python.instructions.md` and the example in `r.myaddon.py`.
- GRASS parser comments define CLI/UI: `%module`, `%keyword`, `%option G_OPT_R_INPUT`, `%option G_OPT_R_OUTPUT` (see `r.myaddon.py`).

## Build, run, test

- Python addon build: `workshop/examples/r.myaddon/Makefile` (uses `$(MODULE_TOPDIR)/include/Make/Script.make)`, `PGM=r.myaddon`, default target `script`.
- C addon build: `workshop/examples/r.caddon.example/Makefile` (uses `Make/Module.make)`, `PGM=r.caddon.example`, links `$(RASTERLIB) $(GISLIB) $(DATETIMELIB)`.
- Assumption: `MODULE_TOPDIR=../..` (build within this workshop tree).
- Tests: `workshop/examples/r.myaddon/testsuite/` uses `pytest` and GRASS fixtures. `conftest.py` seeds a small project and `TemporaryMapsetSession`; tests call the addon via `Tools(session=...).r_myaddon(...)`.

## Dev environment and tooling

- Python: `>=3.13` (see `pyproject.toml`). Runtime dep: `ipyleaflet`; dev deps: `cookiecutter`, `ipykernel`, `pre-commit`, `ruff`.
- Devcontainer runs `uv sync --locked` and validates GRASS; VS Code settings point to the workspace venv.
- Pre-commit (`.pre-commit-config.yaml`): Ruff (lint+format), Flake8, Markdownlint, Yamllint, Biome, Clang-Format 18, and uv hooks.
  - Useful commands: `pre-commit run --all-files` • `pre-commit run ruff-format --all-files` • `pre-commit run clang-format --all-files`.

## Conventions that differ from “typical”

- Don’t modify global computational region/MASK; use temporary contexts. Outputs go to the current mapset; inputs may include mapset qualifiers.
- Prefer GRASS messaging (`gs.message`, `gs.warning`, `gs.fatal`) and add raster history (`gs.raster_history`).
- Keep names consistent via `PGM` (source, docs, binary: e.g., `r.myaddon`, `r.myaddon.py`, `r.myaddon.html`).

## Pointers and examples

- Example addon: `workshop/examples/r.myaddon/r.myaddon.py` (shows parser header, temporary map cleanup, region/mask guidance).
- Tests and fixtures: `workshop/examples/r.myaddon/testsuite/`.
- C example: `workshop/examples/r.caddon.example/main.c`.
- Policy/docs: `.github/instructions/*.md`.

Questions or gaps (e.g., CI expectations or non-standard build flows)? Ask and we’ll refine this file.
