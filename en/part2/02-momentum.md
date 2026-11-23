# Chapter 2　Actuator Disc, Blade-Element Theory and Open-Water Curves

## 2.1 The actuator disc: thrust is added momentum

First think of the propeller as a very thin disc that raises the water pressure abruptly, and forget the blade shape. Water passing through the disc is accelerated and the stream tube contracts downstream. Momentum conservation over the stream tube, plus Bernoulli's equation applied once ahead of and once behind the disc, shows that the velocity increase at the disc is exactly half the increase in the far wake:

$$
V_{disk} = V_A(1 + a), \qquad V_{wake} = V_A(1 + 2a), \qquad
C_T = \frac{T}{\tfrac12 \rho A V_A^2} = 4a(1 + a)
$$

The useful power is $T V_A$ and the power delivered to the water is $T V_A(1 + a)$, so the ideal efficiency is

$$
\eta_i = \frac{1}{1 + a} = \frac{2}{1 + \sqrt{1 + C_T}}
$$

No propulsor can beat this limit; what is lost is the kinetic energy left in the wake. The heavier the loading (the larger $C_T$), the more the water must be accelerated and the lower the efficiency. The most direct way to reduce $C_T$ is a larger diameter: the same thrust shared by more water.

```{anywidget} ../widgets/dist/proto-embed.mjs
{"file": "momentum.html", "section": "s1"}
```

:::{note}
The actuator disc assumes inviscid flow, thrust spread uniformly over the disc and no wake rotation. The stream-tube shape is approximated from the centreline velocity of a uniformly loaded disc, $V_A[1 + a(1 + x/\sqrt{x^2 + R^2})]$, with continuity; it is only illustrative. Blade-element theory in the next section adds back the rotational and viscous losses.
:::

## 2.2 The velocity triangle: what a section sees

Back to the blade itself. At the section of radius $r$, water arrives from ahead at $V_A$ while the section moves at $\omega r$. The angle of the combined velocity is the advance angle $\beta$:

$$
\tan\beta = \frac{V_A}{\omega r} = \frac{J}{\pi\, r/R}
$$

The propeller pushes the water, and the water is dragged along in return: an extra $aV_A$ axially and a swirl $a'\omega r$ tangentially. The relative velocity $W$ that the section actually sees points along the hydrodynamic pitch angle $\beta_i$, and the angle of attack is the pitch angle minus it:

$$
\tan\beta_i = \frac{V_A(1 + a)}{\omega r(1 - a')}, \qquad \alpha = \varphi - \beta_i
$$

Lift $dL$ is normal to $W$ and drag $dD$ lies along $W$; projected onto the axial and tangential directions they give thrust and torque:

$$
dT = dL\cos\beta_i - dD\sin\beta_i, \qquad dQ = r\,(dL\sin\beta_i + dD\cos\beta_i)
$$

Rearranging the section efficiency $dT\,V_A / (dQ\,\omega)$ splits it neatly into three factors:

$$
\eta_{section} = \underbrace{\frac{1}{1 + a}}_{\text{axial}}\;\underbrace{(1 - a')}_{\text{rotational}}\;\underbrace{\frac{\tan\beta_i}{\tan(\beta_i + \gamma)}}_{\text{viscous}}, \qquad \tan\gamma = \frac{C_D}{C_L}
$$

The first factor is the actuator-disc term; the second is the energy carried away by wake swirl; the third is section drag. Drag $J$ and you will see the axial loss dominate at heavy loading (small $J$), while at light loading the lift drops and the viscous share grows.

```{anywidget} ../widgets/dist/proto-embed.mjs
{"file": "momentum.html", "section": "s2"}
```

:::{note}
The $a$ and $a'$ in the interactive figure are those of DTMB 4119, solved with the blade-element momentum theory of the next section.
:::

## 2.3 Blade-element momentum theory: integrating the whole propeller

How are $a$ and $a'$ found? Cut the disc into annuli. Each annulus must satisfy two things at once: the force from the blade sections (2.2) must equal the momentum change through that annulus (the actuator disc of 2.1, applied to a ring):

$$
dT = 4\pi r\,\rho V_A^2 (1 + a)\, a F\, dr, \qquad
dQ = 4\pi r^3 \rho V_A\, \omega (1 + a)\, a' F\, dr
$$

Both sets of equations contain $a$ and $a'$; substitute back and forth until they converge. $F$ is the Prandtl tip factor:

$$
F = \frac{2}{\pi}\arccos\left[\exp\left(-\frac{Z}{2}\,\frac{1 - r/R}{(r/R)\sin\beta_i}\right)\right]
$$

With a finite number of blades, water leaks round the tips, so momentum theory overestimates more and more towards the tip; $F$ corrects it downwards. After integration the results are expressed as non-dimensional coefficients:

$$
K_T = \frac{T}{\rho n^2 D^4}, \qquad K_Q = \frac{Q}{\rho n^2 D^5}, \qquad \eta_0 = \frac{J}{2\pi}\frac{K_T}{K_Q}
$$

Compared with the DTMB 4119 tests at the design point $J = 0.833$, the efficiency comes out very close (0.700 against 0.691), but $K_T$ and $K_Q$ are both over-predicted by more than 40% ($K_T$ 0.215 against 0.146). The cause is the use of two-dimensional section lift: on wide blades the streamlines are curved, so the effective camber and angle of attack are smaller. Part 3, with lifting-line and lifting-surface corrections, deals with this.

```{anywidget} ../widgets/dist/proto-embed.mjs
{"file": "momentum.html", "section": "s3"}
```

:::{note}
Section lift uses thin-airfoil theory, $C_L = 2\pi(\alpha - \alpha_0)$. The zero-lift angle $\alpha_0$ is integrated from the $a = 0.8$ mean line, $-7.58°$ at $C_{Li} = 1$, then scaled by the local $C_{Li}$; the same integral gives an ideal angle of 1.52°, in line with the 1.54° of Abbott & von Doenhoff. The drag coefficient is constant over the radius (0.008 by default).
:::

## 2.4 Open-water curves and the B-series: choosing a propeller from charts

The open-water curves are a propeller's identity card in uniform inflow: $J$ on the horizontal axis, $K_T$, $10K_Q$ and $\eta_0$ on the vertical. Small $J$ means heavy loading (high thrust, low efficiency); as $J$ approaches $P/D$ the thrust falls towards zero.

The Wageningen B-series is a systematic set of more than a hundred model propellers tested at MARIN in the Netherlands. Oosterveld and van Oossanen (1975) fitted the results with regression polynomials, 39 terms for $K_T$ and 47 for $K_Q$:

$$
K_T = \sum_{k=1}^{39} C_k\, J^{s_k} (P/D)^{t_k} (A_E/A_0)^{u_k} Z^{v_k}
$$

A typical selection problem: given the speed of advance $V_A$ (ship speed less wake), the required thrust $T$ (resistance plus thrust deduction) and the diameter $D$, find the rate of revolution and the pitch. Eliminating $n$,

$$
\frac{K_T}{J^2} = \frac{T}{\rho D^2 V_A^2}
$$

The right-hand side is a known constant, so the design point must lie on the parabola $K_T = cJ^2$. Each $P/D$ crosses the parabola once; pick the crossing with the highest efficiency, then get the revolutions from $n = V_A/(JD)$. If the revolutions are given and the diameter is wanted, use $K_T/J^4 = Tn^2/(\rho V_A^4)$ instead; the procedure is the same.

```{anywidget} ../widgets/dist/proto-embed.mjs
{"file": "momentum.html", "section": "s4"}
```

:::{note}
The regression is valid for $Z$ = 2–7, $A_E/A_0$ = 0.30–1.05 and $P/D$ = 0.5–1.4 at a Reynolds number of $2\times10^6$; the area ratios actually tested for each blade number are narrower, and the figure warns when it extrapolates. The defaults reproduce the worked example in the MIT 2.611 notes: B5-75 with $K_T/J^2 = 0.544$ gives the best $P/D = 1.0$ at $J = 0.64$, $\eta_0 = 0.61$.
:::

## References

1. Actuator disc and blade-element theory: Carlton, *Marine Propellers and Propulsion*; Kerwin & Hadler, *Propulsion* (SNAME PNA series).
2. B-series polynomials: Oosterveld & van Oossanen (1975), "Further computer-analyzed data of the Wageningen B-screw series", *International Shipbuilding Progress* 22.
3. Selection example and check values: MIT OpenCourseWare 2.611 *Marine Power and Propulsion* (2006), "Using KT and KQ for design".
4. DTMB 4119 test values: Jessup (1989); ITTC 1998 Propulsion Committee comparative calculation workshop.
5. Ideal angle of the $a = 0.8$ mean line: Abbott & von Doenhoff, *Theory of Wing Sections*.
