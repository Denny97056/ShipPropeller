# Chapter 1　The Helicoid, Blade Sections, Skew and Area Ratio

## 1.1 The helicoid: where a section lies

Cut the blade with a cylinder of radius $r$, coaxial with the shaft. The cut is the blade section at that radius. Slit the cylinder along a generator and unroll it: the chord of the section lies on a straight sloping line, which advances one pitch $P$ along the axis per revolution.

$$
\tan\varphi = \frac{P}{2\pi r}
$$

$\varphi$ is the pitch angle. The same $P$ gives a different angle at every radius: sections near the hub stand steep, sections at the tip lie almost flat. That is why a blade looks twisted even when its pitch is constant.

By convention the pitch at $0.7R$ stands for the whole propeller, written as the pitch ratio $P/D$. DTMB 4119 has 1.084 at $0.7R$, falling only from 1.105 at the hub to 1.076 at the tip: very nearly constant pitch.

```{anywidget} ../widgets/dist/proto-embed.mjs
{"file": "geometry.html", "section": "s1"}
```

:::{note}
Here $P$ is defined on the nose–tail line (leading edge to trailing edge). Older drawings often use face pitch instead, which differs slightly for cambered sections. The propeller actually advances less than $P$ per revolution; the difference is slip, covered in Part 2.
:::

## 1.2 Blade sections: thickness and camber each have one job

Unrolled, a section is a two-dimensional foil described by three numbers: chord $c$, maximum thickness $t$ and maximum camber $f$. Thickness is there mainly for strength, camber mainly for lift.

The most common combination on marine propellers is the NACA 66 (mod) thickness form with the NACA $a = 0.8$ mean line. $a = 0.8$ means the pressure difference between back and face stays constant from the leading edge to 80% chord, then falls linearly to zero. Camber is proportional to the design lift coefficient:

$$
C_{Li} = \frac{f/c}{0.0679}, \qquad \Delta C_p = \frac{C_{Li}}{0.9} \quad (x/c \le 0.8)
$$

A flat pressure difference has no peak, and the flatter the minimum pressure on the back, the later cavitation starts. The 66 series puts maximum thickness at 45% chord for the same reason, unlike the NACA four-digit sections common in aeronautics (maximum thickness at 30%).

Drag $t/c$ and $f/c$, or load DTMB 4119 sections from different radii: the root is thick and short for strength, the tip is very thin, and the section near $0.7R$ looks most like an ordinary foil.

```{anywidget} ../widgets/dist/proto-embed.mjs
{"file": "geometry.html", "section": "s2"}
```

:::{note}
This is the thin-foil loading at the ideal angle of attack. Away from it a suction peak appears at the leading edge; the cavitation chapter treats this with the bucket diagram.
:::

## 1.3 Skew and rake: sliding sections over the helicoid

Once a section's shape is fixed, we still have to decide where it goes. The mid-chord points of all sections form the mid-chord line. The straight line drawn out from the shaft centre, normal to the axis, is the generator line: the reference for drawing and manufacture.

**Skew**: slide each section back along its own helix (against the rotation) by an angle $\theta_s$, and the blade becomes scimitar-shaped. Sections at different radii then do not enter the high-wake region behind the hull at the same moment, so vibration and hull pressure pulses drop.

**Rake**: shift each section downstream along the axis by $x_R$. The blade leans aft, which increases the clearance to the hull.

Because skew moves along the helix, it also carries an axial shift with it, called skew-induced rake:

$$
x_m = x_R + r\,\theta_s \tan\varphi
$$

The side view shows it best: add skew without rake and the mid-chord line still leans aft. Highly skewed propellers are often given some negative rake to bring the tip back. Set skew to 45° and find the rake angle that puts the tip back on the generator line.

```{anywidget} ../widgets/dist/proto-embed.mjs
{"file": "geometry.html", "section": "s3"}
```

:::{note}
Skew is distributed quadratically, $\theta_s = \theta_{tip}\,\big((r - r_h)/(R - r_h)\big)^2$, and rake linearly; chord and pitch are DTMB 4119. Real propellers tailor both distributions to the design.
:::

## 1.4 Area ratio: how much of the disc the blades cover

Blade area divided by disc area $\pi R^2$ is one of the most quoted propeller parameters. Expanded area uses only the chord, as if every section were laid flat side by side; projected area is what the blades cover on the disc seen from astern:

$$
\mathrm{EAR} = \frac{Z}{\pi R^2}\int_{r_h}^{R} c\,dr, \qquad
\mathrm{PAR} = \frac{Z}{\pi R^2}\int_{r_h}^{R} c\cos\varphi\,dr
$$

Sections sit at an angle on the helicoid, so seen from astern only a width $c\cos\varphi$ remains. PAR is therefore always smaller than EAR, and the gap grows with pitch. DTMB 4119 comes out at EAR = 0.607 (0.60 nominal), with PAR about 80% of that.

Area ratio is set mainly by cavitation. For a given thrust, less area means higher loading per unit area, lower pressure on the back and earlier cavitation; more area means more friction and lower efficiency. Blade number relates to vibration frequency and hub space: at the same area ratio, more blades means narrower blades.

```{anywidget} ../widgets/dist/proto-embed.mjs
{"file": "geometry.html", "section": "s4"}
```

:::{note}
Strictly, developed area (measured on the helicoid) and expanded area differ slightly; in practice they are usually treated as equal. Projected area here ignores camber and thickness.
:::

## References

1. DTMB 4119 geometry: Jessup (1989) model tests, and the ITTC 1998 Propulsion Committee comparative calculation workshop.
2. NACA $a$-series mean lines and four-digit thickness: Abbott & von Doenhoff, *Theory of Wing Sections*.
3. NACA 66 (mod) thickness: Brockett (1966), DTMB Report 1780. Table values in the interactive figures are approximate and for teaching only.
4. Definitions of skew, rake and area ratio: Carlton, *Marine Propellers and Propulsion*; Kerwin & Hadler, *Propulsion* (SNAME PNA series).
