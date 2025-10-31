## DESCRIPTION

The purpose of *r.agent.addon* is to run SIMWE (SIMulated Water Erosion) simulation
with a custom rainfall rate. This module computes slope aspect derivatives and then
runs the r.sim.water simulation to model water flow and depth across the landscape.

Parameter **elevation** is the input elevation raster map used for the simulation.

Parameter **rainfall_rate** is the rainfall intensity value in mm/hr (default: 40).

Parameter **niterations** is the number of simulation iterations (default: 30).

Parameter **depth** is the output water depth raster map.

## NOTES

This module is a wrapper around r.sim.water that simplifies running SIMWE simulations
with custom rainfall parameters. It automatically computes the required slope derivatives
(dx, dy) from the elevation model and cleans up temporary maps after execution.

The simulation uses the kinematic wave approach to model overland water flow. Higher
rainfall rates will produce greater water depths, while the number of iterations affects
the temporal resolution of the simulation.

## EXAMPLE

```sh
# Set the computational region
g.region raster=elevation

# Run SIMWE simulation with default rainfall rate (40 mm/hr)
r.agent.addon elevation=elevation depth=water_depth

# Run with custom rainfall rate and iterations
r.agent.addon elevation=elevation rainfall_rate=60 niterations=50 depth=water_depth
```

## REFERENCES

Mitas, L., & Mitasova, H. (1998). Distributed soil erosion simulation for effective
erosion prevention. Water Resources Research, 34(3), 505-516.

## SEE ALSO

*[r.sim.water](https://grass.osgeo.org/grass-stable/manuals/r.sim.water.html),
*[r.slope.aspect](https://grass.osgeo.org/grass-stable/manuals/r.slope.aspect.html),
*[g.region](https://grass.osgeo.org/grass-stable/manuals/g.region.html)*

## AUTHORS

Corey T. White
