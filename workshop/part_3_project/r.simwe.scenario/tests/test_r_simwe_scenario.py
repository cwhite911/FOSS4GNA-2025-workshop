# import numpy as np

from grass.tools import Tools
import grass.script as gs

def test_output_exists(xy_dataset_session):
    tools = Tools(session=xy_dataset_session, consistent_return_value=True)
    tools.r_simwe_scenario(elevation="rows_raster", output="output_raster", rain_value=10.0)
    # check that output raster exists
    assert gs.find_file("output_raster", element="raster")["name"] == "output_raster"

# Write your tests here