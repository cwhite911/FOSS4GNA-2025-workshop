import subprocess
import sys


def main():
    # Append GRASS to the python system path
    sys.path.append(
        subprocess.check_output(["grass", "--config", "python_path"], text=True).strip()
    )

    import grass.script as gs
    from grass.tools import Tools

    # Create a new project
    gs.create_project(path="path/to/my_project", epsg="3358")

    # Initialize the GRASS session
    with gs.setup.init("path/to/my_project") as session:
        # Run GRASS tools
        tools = Tools(session=session)
        tools.r_import_(input="/path/to/elevation.tif", output="elevation")
        tools.g_region(raster="elevation")
        tools.r_slope_aspect(elevation="elevation", slope="slope")
        print("GRASS GIS project created and tools executed successfully.")


if __name__ == "__main__":
    main()
