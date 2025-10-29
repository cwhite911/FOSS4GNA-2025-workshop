# FOSS4GNA-2025-workshop

Workshop Participant Level: Advanced

![GRASS Logo](https://grass.osgeo.org/images/logos/grass-gradient-horizontal.svg)

Learn to develop [GRASS addons](https://github.com/OSGeo/grass-addons) with
Python! Together, we will develop a parallelized custom addon with Python,
command line, and graphical user interfaces. [GRASS](https://grass.osgeo.org/)
works as a powerful geospatial processing engine that works on a small laptop to
a huge supercomputer. GRASS also makes it easy to move from using a
[graphical user interface (GUI)](https://grass.osgeo.org/grass85/manuals/helptext.html)
to command line interface or
[Python API](https://grass.osgeo.org/grass85/manuals/python_intro.html).
During this workshop we will develop a GRASS addon exploring the various
[GRASS Python modules](https://grass.osgeo.org/grass-devel/manuals/libpython/index.html),
tooling, and best practice required to produce high quality open source software.
The bonus material for this workshop will also cover tools written in C.

## Prerequisites

To get the most out of this workshop, basic Python and GIS experience is
recommended. The workshop will use an online environment, so no software
installation on laptops is required from participants.

## Learning Objectives

By the end of this workshop, participants will be able to:

- Understand the structure of a GRASS addon
- Understand community best practices for GRASS addon development
- Use GRASS Python modules to develop geospatial processing tools
- Develop command line and graphical user interfaces for GRASS addons
- Be ready to contribute GRASS addons to the community repository :green_heart:

## Workshop Structure

[![Open in Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?template=true)

- GRASS Fundamentals
  - Intro to GRASS
  - GRASS scripting with Python
  - Write your first GRASS script
- From GRASS scripts to GRASS addons
  - Setting up the development environment
  - Addon structure
  - Standardized options and flags
  - Local testing and debugging
  - best practices for coding and documentation
- Project
  - Build a parallelized GRASS addon with CLI and GUI
  - Testing and packaging
  - Submitting to grass-addons
- Wrap-up
- Bonus: C Addon Overview
- Bonus: AI-assisted coding for GRASS addon development the good, the bad, and
the ugly.

## Resources

- [GRASS Website](https://grass.osgeo.org/)
- [GRASS Python Documentation](https://grass.osgeo.org/grass-devel/manuals/libpython/index.html)

### GitHub Repositories

- [grass](https://github.com/OSGeo/grass)
- [grass-addons](https://github.com/OSGeo/grass-addons)
- [grass-addon-cookiecutter](https://github.com/OSGeo/grass-addon-cookiecutter)

### Developer Docs

- [GRASS Python Introduction](https://grass.osgeo.org/grass-devel/manuals/python_intro.html)

  - [grass.tools](https://grass.osgeo.org/grass-devel/manuals/libpython/grass.tools.html)
provides a Python interface to GRASS tools,
  - [grass.script](https://grass.osgeo.org/grass-devel/manuals/libpython/script_intro.html)
handles GRASS projects and sessions in Python,
  - [grass.pygrass](https://grass.osgeo.org/grass-devel/manuals/libpython/pygrass_index.html)
  enables a fine-grained access to the GRASS data structures.
- [GRASS 8 Programmer's Manual](https://grass.osgeo.org/programming8/)
- [Standard Parser Options][parser] standard option structure
- [GRASS Programming Style Guide](https://grass.osgeo.org/grass85/manuals/style_guide.html)

[parser]: https://grass.osgeo.org/grass85/manuals/parser_standard_options.html

## Instructors

- [Corey White](https://github.com/cwhite911)
- [Caitlin Haedrich](https://github.com/chaedri)

## Funding

USDA NRCS
