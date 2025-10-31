#!/usr/bin/env python3

import subprocess
import sys


def run_simwe(elevation, rainfall_rate=10, depth_output="depth", tools=None):
    tools.r_slope_aspect(elevation=elevation, dx="dx", dy="dy")
    tools.r_sim_water(
        elevation=elevation,
        dx="dx",
        dy="dy",
        rain_value=rainfall_rate,
        depth=depth_output,
    )


def main():
    # Append GRASS to the python system path
    sys.path.append(
        subprocess.check_output(["grass", "--config", "python_path"], text=True).strip()
    )

    import grass.script as gs
    from grass.tools import Tools

    # Initialize the GRASS session
    with gs.setup.init("/root/nc_basic_spm_grass7") as session:
        tools = Tools(session=session)
        tools.g_region(
            raster="elevation", res=40
        )  # notice res downsampling so this script runs quickly!
        run_simwe(elevation="elevation", rainfall_rate=60, tools=tools)


if __name__ == "__main__":
    main()
