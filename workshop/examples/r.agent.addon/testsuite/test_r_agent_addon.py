import numpy as np

from grass.tools import Tools


def test_output_exists(session):
    """Test that r.agent.addon creates the output depth raster"""
    tools = Tools(session=session, consistent_return_value=False)
    # Create a simple elevation raster for testing
    tools.r_mapcalc(expression="elevation = row() + col()")

    # Run the addon
    output = tools.r_agent_addon(
        elevation="elevation", rainfall_rate=40, niterations=30, depth=np.array
    )

    # Check that output was created and contains data
    assert output is not None
    assert output.size > 0
