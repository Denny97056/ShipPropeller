# Code and validation

Every module can be run directly (`python code/<module>.py`) and prints its validation cases and results. To run them all:

```bash
python tools/run_validations.py
```

| Part | Module | Contents | Main checks |
|---|---|---|---|
| 1 | `prop_geometry.py` | Interpolation of the DTMB 4119 radial distributions, the *a* = 0.8 mean line, expanded and projected area ratios | Maximum camber 0.0679 at $C_{Li} = 1$; interpolation passes through the table; EAR within 2% of the nominal 0.60; PAR < EAR |

The JavaScript in the interactive figures (`prototypes/`) uses the same formulas and interpolation as these modules, and the numbers agree (for example EAR = 0.607 and PAR = 0.500 for three blades).
