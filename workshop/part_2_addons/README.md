[grass-addons]: https://github.com/OSGeo/grass-addons
[gunittest_testing]: https://grass.osgeo.org/grass85/manuals/libpython/gunittest_testing.html#
[grass_parser]: https://grass.osgeo.org/grass85/manuals/parser_standard_options.html
[grass_style_guide]: https://grass.osgeo.org/grass85/manuals/style_guide.html
[contributing]: https://github.com/OSGeo/grass-addons/blob/grass8/CONTRIBUTING.md
[cookiecutter]: https://cookiecutter.readthedocs.io/en/stable/
[cookiecutter_install]: https://cookiecutter.readthedocs.io/en/stable/installation.html#install-cookiecutter
[grass-addon-cookiecutter]: https://github.com/OSGeo/grass-addon-cookiecutter

# Part 2 - From GRASS scripts to GRASS addons

## Learning Objectives

By the end of this part, you will be able to:

1. Define what a GRASS addon is :green_heart: and when to create one :green_heart:
2. Describe the structure of a GRASS addon and community best practices for development
3. Develop command line and graphical user interfaces for GRASS addons
4. Be ready to contribute GRASS addons to the community repository :green_heart:

## Getting Started

### What is a GRASS addon?

A [GRASS addon][grass-addons] is a standalone module that extends the
functionality of GRASS software.

### When should you create an addon?

- [ ] You have a script that could be useful to others
- [ ] You want to share your code with the GRASS community
- [ ] You want to contribute to the GRASS ecosystem
- [ ] You want to maintain your code independently
from the core GRASS development cycle
- [ ] You want to publish your research methods as GRASS modules

## Addon Development Environment

### Setting up the development environment

- [grass-addons][grass-addons] repository
- [grass-addon-cookiecutter][grass-addon-cookiecutter]

### Addon structure

Example code structure for a generated addon:

```text
r.myaddon
├── Makefile
├── r.myaddon.html
├── r.myaddon.ipynb (optional)
├── r.myaddon.py
└── testsuite
    └── test_r_myaddon.py

```

#### Standardized options and flags

- [Standard Parser Options][grass_parser] standard option structure

### Community Best Practices

- [GRASS Programming Style Guide][grass_style_guide]

### Testing and debugging

[GRASS Testing Framework][gunittest_testing]

## Addon Development Steps

### 1. Fork GRASS addons

We can follow the contributing documentation from the [grass-addons][contributing]
GitHub repository.

### 2. Create a new addon using Cookiecutter

[Cookiecutter][cookiecutter] is set up to help generate the required boiler
plate structure of an addon.

> Cookiecutter is already install in this codespace, but you will need to
install it on your own machine using the following documentation for local
use ([cookiecutter install docs][cookiecutter_install]).

```bash
cookiecutter gh:OSGeo/grass-addon-cookiecutter

cookiecutter https://github.com/cwhite911/grass-addon-cookiecutter --checkout grass-tools
```
