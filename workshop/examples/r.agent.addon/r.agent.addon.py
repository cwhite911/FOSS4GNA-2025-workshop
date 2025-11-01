#!/usr/bin/env python

##############################################################################
# MODULE:    r.agent.addon
#
# AUTHOR(S): Corey T. White <smortopahri@gmail.com>
#
# PURPOSE:   Run SIMWE simulation with custom rainfall rate
#
# COPYRIGHT: (C) 2025 by Corey T. White and the GRASS Development Team
#
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.
##############################################################################

"""Run SIMWE simulation with custom rainfall rate"""

# %module
# % description: Run SIMWE simulation with custom rainfall rate
# % keyword: raster
# % keyword: hydrology
# % keyword: simulation
# %end
# %option G_OPT_R_INPUT
# % key: elevation
# % description: Name of input elevation raster map
# %end
# %option
# % key: rainfall_rate
# % type: double
# % required: no
# % answer: 40
# % description: Rainfall intensity value (mm/hr)
# %end
# %option
# % key: niterations
# % type: integer
# % required: no
# % answer: 30
# % description: Number of iterations
# %end
# %option G_OPT_R_OUTPUT
# % key: depth
# % description: Name of output water depth raster map
# %end

import sys
import atexit
import grass.script as gs
from grass.tools import Tools
from gettext import gettext as _


def clean(*names):
    """Remove temporary rasters"""
    for name in names:
        gs.run_command("g.remove", type="raster", name=name, flags="f", superquiet=True)


def run_simwe(elevation, rainfall_rate, niterations, depth, tools):
    """Run SIMWE simulation

    :param elevation: Input elevation raster
    :param rainfall_rate: Rainfall intensity value (mm/hr)
    :param niterations: Number of iterations
    :param depth: Output water depth raster
    :param tools: GRASS Tools instance
    """
    # Create temporary rasters for dx and dy
    dx = gs.append_node_pid("dx")
    dy = gs.append_node_pid("dy")
    atexit.register(clean, dx, dy)

    gs.verbose(_("Computing slope aspect derivatives..."))
    tools.r_slope_aspect(elevation=elevation, dx=dx, dy=dy)

    gs.verbose(
        _("Running SIMWE with rainfall rate {rate} mm/hr...").format(
            rate=rainfall_rate
        )
    )
    tools.r_sim_water(
        elevation=elevation,
        dx=dx,
        dy=dy,
        rain=rainfall_rate,
        depth=depth,
        flags="t",
        niterations=niterations,
    )


def main():
    # Initialize tools
    tools = Tools()

    # Get input options
    options, flags = gs.parser()
    elevation = options["elevation"]
    rainfall_rate = float(options["rainfall_rate"])
    niterations = int(options["niterations"])
    depth = options["depth"]

    # Run SIMWE simulation
    run_simwe(
        elevation=elevation,
        rainfall_rate=rainfall_rate,
        niterations=niterations,
        depth=depth,
        tools=tools,
    )

    # Save history into the output raster
    gs.raster_history(depth, overwrite=True)

    gs.message(_("SIMWE simulation complete. Output saved to <{}>").format(depth))


if __name__ == "__main__":
    sys.exit(main())
