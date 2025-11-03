#!/usr/bin/env python

##############################################################################
# MODULE:    r.simwe.scenario
#
# AUTHOR(S): Corey T. White <smortopahri@gmail.com>
#
# PURPOSE:   Run overland flow scenarios with the SIMWE model.
#
# COPYRIGHT: (C) 2025 by Corey T. White and the GRASS Development Team
#
#            This program is free software under the GNU General Public
#            License (>=v2). Read the file COPYING that comes with GRASS
#            for details.
##############################################################################

"""Run overland flow scenarios with the SIMWE model."""

# %module
# % description: Run overland flow scenarios with the SIMWE model.
# % keyword: raster
# % keyword: hydrology
# % keyword: water
# %end
# %option G_OPT_R_ELEV
# %required: yes
# %end
# %option G_OPT_R_OUTPUT
# % description: Name for output depth raster [m]
# % required: yes
# %end
# %option
# % key: rainfall_rate
# % type: double
# % description: Rainfall rate (mm/hr)
# % answer: 10
# %end
# %option
# % key: min_depth
# % type: double
# % description: Minimum depth to retain in output raster (m) if -d flag is set
# % answer: 0.01
# %end
# %option G_OPT_M_NPROCS
# %end
# %option G_OPT_M_SEED
# %end
# %flag
# % key: d
# % description: Limit output to depths above 0.01 m
# %end

import sys
import atexit
from gettext import gettext as _
import grass.script as gs
from grass.tools import Tools


def clean(names: list, tools=None):
    tools.g_remove(type="raster", name=names, flags="f", superquiet=True)


def run_simwe(elevation, dx, dy, rainfall_rate, depth_output, procs, seed, tools=None):
    """Run SIMWE overland flow model."""
    tools.r_slope_aspect(elevation=elevation, dx=dx, dy=dy)
    tools.r_sim_water(
        elevation=elevation,
        dx=dx,
        dy=dy,
        rain_value=rainfall_rate,
        depth=depth_output,
        random_seed=seed,
        nprocs=procs,
    )


def limit_depths(output_raster, depth_raster, min_depth, tools=None):
    """Limit depth raster to values above a minimum depth."""
    tools.r_mapcalc(
        expression=f"{output_raster} = if({depth_raster} >= {min_depth}, {depth_raster}, null())",
        overwrite=True,
    )

    # Set color table for output raster back to that of the original depth raster
    tools.r_colors(map=output_raster, raster=depth_raster)


def main():
    # initalize tools
    tools = Tools(overwrite=True)

    # get input options
    options, flags = gs.parser()
    elevation = options["elevation"]
    output_raster = options["output"]
    rainfall_rate = float(options["rainfall_rate"])
    min_depth = float(options["min_depth"])
    procs = options["nprocs"]
    seed = options["seed"]

    # crete a temporary raster that will be removed upon exit
    temporary_raster_dx = gs.append_node_pid("dx")
    temporary_raster_dy = gs.append_node_pid("dy")
    output_depth_raster = gs.append_node_pid("depth") if flags["d"] else output_raster
    temp_files = [temporary_raster_dx, temporary_raster_dy]
    atexit.register(clean, temp_files, tools=tools)

    gs.debug(
        _("Running r.simwe.scenario with %s processes and seed %s") % (procs, seed)
    )
    gs.message(_("Running scenario..."))
    # run analysis
    run_simwe(
        elevation=elevation,
        dx=temporary_raster_dx,
        dy=temporary_raster_dy,
        rainfall_rate=rainfall_rate,
        depth_output=output_depth_raster,
        procs=procs,
        seed=seed,
        tools=tools,
    )

    # flags
    if flags["d"]:
        gs.message(_("Filtering depth..."))
        limit_depths(
            output_raster=output_raster,
            depth_raster=output_depth_raster,
            min_depth=min_depth,
            tools=tools
        )

    # save history into the output raster
    gs.raster_history(output_raster, overwrite=True)


if __name__ == "__main__":
    sys.exit(main())
