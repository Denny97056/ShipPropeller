# Marine Propellers: From Geometry to Panel Methods

This is an interactive textbook for undergraduate naval architecture students who have taken fluid mechanics. Every chapter follows the same order: **geometric or flow intuition → formula → interactive check → the matching Python module and its validation**.

The book uses public textbook examples throughout, chiefly the classic DTMB 4119 three-bladed propeller and the Wageningen B-series:

- **Part 1　Geometry**: the helicoid and pitch, blade sections (NACA 66 (mod) with the *a* = 0.8 mean line), skew and rake, area ratios
- **Part 2　Momentum and blade-element theory**: actuator disc and ideal efficiency, velocity triangles, blade-element momentum theory, $K_T$, $K_Q$, $J$ and the B-series open-water curves
- **Part 3　Lifting line and optimum circulation** (in preparation): induced velocities, tip corrections, the Betz condition
- **Part 4　Panel methods, cavitation and strength** (in preparation)

:::{warning} For teaching
The calculations in this book are teaching codes written to explain the principles. They are checked against published values, but they are not certified design tools.
:::

All Python modules are in the `code/` folder; see [Appendix: Code and validation](appendix/code.md).
