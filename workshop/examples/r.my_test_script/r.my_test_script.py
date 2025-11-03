#!/usr/bin/env python
##############################################################################
# MODULE:    r.my_test_script
#
# AUTHOR(S): Generated from user's script
#
# PURPOSE:   Run simple slope/aspect and a small rainfall-runoff sim (r.sim.water)
#
# COPYRIGHT: (C) 2025 by Workshop contributor and the GRASS Development Team
#
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.
##############################################################################

"""Run slope/aspect and a quick surface-water simulation.

This is a small wrapper that calls r.slope.aspect and r.sim.water using
the `Tools` helper. It intentionally keeps behaviour minimal and relies on
GRASS session/region management provided by the environment.
"""

# %module
# % description: Compute slope/aspect and run a simple rainfall-runoff sim (r.sim.water wrapper).
# % keyword: raster
# % keyword: hydrology
# % keyword: simulation
# %end
# %option G_OPT_R_INPUT
# % key: elevation
# % description: Name of elevation raster to use
# %end
# %option
# % key: rainfall
# % type: double
# % description: Rainfall rate (units depend on r.sim.water configuration)
# % answer: 10
# %end
# %option G_OPT_R_OUTPUT
# % key: depth
# % description: Name for depth output raster
# %end

import sys
from gettext import gettext as _

import grass.script as gs
from grass.tools import Tools


def run_simwe(elevation, rainfall_rate=10, depth_output="depth", tools=None):
    """Helper that runs r.slope.aspect and r.sim.water using Tools.

    Parameters
    - elevation: name of elevation raster
    - rainfall_rate: numeric rainfall input
    - depth_output: name for output depth raster
    - tools: optional Tools instance (if None, a new Tools() will be created)
    """
    if tools is None:
        tools = Tools()

    # compute slope/aspect names (conservative names)
    # r.slope.aspect will create rasters named 'dx' and 'dy' here by default
    tools.r_slope_aspect(elevation=elevation, dx="dx", dy="dy")

    # run the simulation
    tools.r_sim_water(
        elevation=elevation,
        dx="dx",
        dy="dy",
        rain_value=rainfall_rate,
        depth=depth_output,
    )


def main():
    options, flags = gs.parser()

    elevation = options.get("elevation")
    rainfall = float(options.get("rainfall"))
    depth = options.get("depth")

    tools = Tools()

    # If user wants to change region it can be done externally. Keep this tool
    # simple and non-invasive.

    run_simwe(elevation=elevation, rainfall_rate=rainfall, depth_output=depth, tools=tools)

    # Save history to output raster
    try:
        gs.raster_history(depth, overwrite=True)
    except Exception:
        gs.verbose(_("Could not write raster history for <{depth}>.").format(depth=depth))


if __name__ == "__main__":
    sys.exit(main())
