#!/usr/bin/env python3

import subprocess
import sys


def run_simwe(elevation, rainfall_rate=40, tools=None):
    tools.r_slope_aspect(elevation=elevation, dx="dx", dy="dy")
    tools.r_sim_water(
        elevation=elevation,
        dx="dx",
        dy="dy",
        rain=rainfall_rate,
        depth="depth",
        flags="t",
        niterations=30,
    )


def main():
    # Append GRASS to the python system path
    sys.path.append(
        subprocess.check_output(["grass", "--config", "python_path"], text=True).strip()
    )

    import grass.script as gs
    from grass.tools import Tools

    # Initialize the GRASS session
    with gs.setup.init("path/to/my_project") as session:
        tools = Tools(session=session)
        tools.g_region(raster="elevation")
        run_simwe(elevation="elevation", rainfall_rate=60, tools=tools)


if __name__ == "__main__":
    main()
