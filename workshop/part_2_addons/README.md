# Part 2 - From GRASS scripts to GRASS addons

- Setting up the development environment
  - [grass-addons](https://github.com/OSGeo/grass-addons)
- Addon structure and best practices
  - [grass-addon-cookiecutter](https://github.com/OSGeo/grass-addon-cookiecutter)
  - [GRASS Programming Style Guide](https://grass.osgeo.org/grass85/manuals/style_guide.html)
- Standardized options and flags
  - [Standard Parser Options][parser] standard option structure
- Local testing and debugging
  - [GRASS Testing Framework](https://grass.osgeo.org/grass85/manuals/libpython/gunittest_testing.html#)


## Fork GRASS addons

We can follow the contributing documentation from the [grass-addons](https://github.com/OSGeo/grass-addons/blob/grass8/CONTRIBUTING.md) GitHub repository.

## Create a new addon

[Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) is set up to help generate the required boiler plate structure of an addon.

> Cookiecutter is already install in this codespace, but you will need to install it on your own machine using the following documentation for local use ([cookiecutter install docs](https://cookiecutter.readthedocs.io/en/stable/installation.html#install-cookiecutter)).

```bash
cookiecutter gh:OSGeo/grass-addon-cookiecutter
```
