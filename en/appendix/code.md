# Code and validation

Every module can be run directly (`python code/<module>.py`) and prints its validation cases and results. To run them all:

```bash
python tools/run_validations.py
```

| Part | Module | Contents | Main checks |
|---|---|---|---|
| 1 | `prop_geometry.py` | Interpolation of the DTMB 4119 radial distributions, the *a* = 0.8 mean line, expanded and projected area ratios | Maximum camber 0.0679 at $C_{Li} = 1$; interpolation passes through the table; EAR within 2% of the nominal 0.60; PAR < EAR |
| 2 | `prop_momentum.py` | Actuator-disc ideal efficiency, Wageningen B-series polynomials (39 + 47 terms), blade-element momentum theory for DTMB 4119 with the Prandtl tip factor | Actuator-disc identities; ideal angle 1.54° for the *a* = 0.8 mean line; B-series reproduces both MIT 2.611 examples (B5-75 best $P/D$ = 1.0, $J$ = 0.64 / 0.74, $\eta_0$ = 0.61 / 0.67); BEMT converges, design-point efficiency within 0.02 of the measured 0.69, $K_T$ over-predicted by 30–60% (no lifting-surface correction; see Part 3) |

The JavaScript in the interactive figures (`prototypes/`) uses the same formulas and interpolation as these modules, and the numbers agree (for example EAR = 0.607 and PAR = 0.500 for three blades; $K_T$ = 0.215 and $\eta_0$ = 0.700 for DTMB 4119 at $J$ = 0.833).
