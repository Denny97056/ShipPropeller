# Where the thrust comes from, and where the efficiency goes

A propeller pushes a body of water aft, and the thrust equals the momentum that water gains. This part first uses the crudest model, the actuator disc, to find the upper limit on efficiency. It then returns to the blade sections, splits thrust and torque over the radius with the velocity triangle, and finally integrates them into the open-water curves that designers look up every day.

The examples are the Wageningen B-series regression polynomials and DTMB 4119 from Part 1. Start with the most direct quantity: how far the propeller actually advances per revolution. Drag the advance ratio $J$ and watch the gap between the pitch line and the actual advance (the slip), and how the thrust, torque and efficiency of a B4-70 follow.

```{anywidget} ../widgets/dist/proto-embed.mjs
{"file": "momentum.html", "section": "hero"}
```
