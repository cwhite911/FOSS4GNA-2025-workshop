import grass.script as gs

from grass.tools import Tools


def test_creates_depth_raster(session):
    tools = Tools(session=session, consistent_return_value=False)
    # run the addon, expect it to create raster named 'depth_test'
    out_name = "depth_test"
    tools.r_my_test_script(elevation="data", rainfall=1.0, depth=out_name)

    info = gs.find_file(out_name, element="raster")
    assert info["file"]
