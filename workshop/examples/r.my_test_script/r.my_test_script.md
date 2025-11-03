## DESCRIPTION

Wrapper that computes slope/aspect and runs a small rainfall-runoff simulation
using `r.sim.water`. The tool calls `r.slope.aspect` and `r.sim.water` and
saves the resulting depth raster.

## EXAMPLES

```
r.my_test_script elevation=elevation rainfall=60 depth=depth_sim
```

## SEE ALSO

*[r.slope.aspect](r.slope.aspect.md), [r.sim.water](r.sim.water.md)

## AUTHORS

Workshop contributor.
