[grass-addons-repo]: https://github.com/OSGeo/grass-addons
[grass-addons]: https://grass.osgeo.org/grass-devel/manuals/addons/
[gunittest_testing]: https://grass.osgeo.org/grass85/manuals/libpython/gunittest_testing.html#
[grass_style_guide]: https://grass.osgeo.org/grass85/manuals/style_guide.html
[grass_tools]: https://grass.osgeo.org/grass-devel/manuals/libpython/grass.tools.html
[grass-addon-cookiecutter]: https://github.com/OSGeo/grass-addon-cookiecutter

# From GRASS scripts to GRASS addons

**_Corey White and Caitlin Haedrich_**

## Learning Objectives

By the end of this part, you will be able to:

1. Define what a GRASS addon is :green_heart: and when to create one :green_heart:
2. Describe the structure of a GRASS addon and community best practices for development
3. Be ready to contribute GRASS addons to the community repository :green_heart:

## 1. What is a GRASS addon?

A [GRASS addon][grass-addons] is a standalone module that extends the
functionality of GRASS software.

### Why create an addon?

- [ ] Allow others to run your useful script or workflow, with long term maintanence
- [ ] Contribute to the GRASS ecosystem
- [ ] Easy to maintain your code independently
from the core GRASS development cycle
- [ ] Publish your research methods with open science best practices

## 2. The Addon Development Environment

### Setting up the development environment

- [grass-addons][grass-addons-repo] repository
- [grass-addon-cookiecutter][grass-addon-cookiecutter]

### Addon Structure

- [Addon Structure Tutorial](./Addon_Structure.md)

### Community Best Practices

- [GRASS Programming Style Guide][grass_style_guide]

### Testing and debugging

New addons should include unit tests to ensure code quality and reliability.
Testing is done using Pytest and the [grass.tools][grass_tools] library.

- [GRASS Testing Framework][gunittest_testing]
- [GRASS Unit Testing with Python](https://github.com/OSGeo/grass-addons/blob/grass8/doc/development/submitting/UNIT_TESTS.md)

## 3. Step-by-Step: How to Contribute an Addon

- [Steps for Developing an Addon](./Developing_an_addon.md)
