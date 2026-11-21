"""Reference numbers for 第一篇 幾何 (propeller handout).

Same formulas as the page's JS core:
  - DTMB 4119 radial tables (Jessup 1989 / ITTC 1998 workshop)
  - chord and thickness interpolated as g(x)*sqrt(1-x) so the tip closes round
  - NACA a=0.8 mean line, NACA 66 (mod) thickness
  - EAR = Z/(pi R^2) * int c dr,  PAR = Z/(pi R^2) * int c cos(phi) dr
"""
import numpy as np
from scipy.interpolate import PchipInterpolator
from scipy.integrate import quad

X  = np.array([.2, .3, .4, .5, .6, .7, .8, .9, .95, 1.0])
CD = np.array([.3200, .3625, .4048, .4392, .4610, .4622, .4347, .3613, .2775, 0.0])
PD = np.array([1.1050, 1.1022, 1.0983, 1.0932, 1.0879, 1.0839, 1.0811, 1.0785, 1.0770, 1.0761])
TD = np.array([.0658, .0563, .0478, .0396, .0321, .0250, .0185, .0120, .0086, 0.0])
FC = np.array([.01429, .02318, .02303, .02182, .02072, .02003, .01967, .01817, .01631, .01175])


def tipround(v):
    g = v[:-1] / np.sqrt(1 - X[:-1])
    g1 = g[-1] + (g[-1] - g[-2]) / (X[-2] - X[-3]) * (1 - X[-2])
    p = PchipInterpolator(X, np.append(g, g1))
    return lambda x: p(x) * np.sqrt(np.maximum(0.0, 1 - x))


cD, tD = tipround(CD), tipround(TD)
pD, fC = PchipInterpolator(X, PD), PchipInterpolator(X, FC)


def mean_a(x, a=0.8):
    """NACA a-series mean line for CLi = 1 (Abbott & von Doenhoff eq. 4.26)."""
    x = np.asarray(x, float)
    L = lambda u: np.where(np.abs(u) < 1e-14, 0.0, u * u * np.log(np.abs(u) + 1e-300))
    g = -1 / (1 - a) * (a * a * (0.5 * np.log(a) - 0.25) + 0.25)
    h = 1 / (1 - a) * (0.5 * (1 - a) ** 2 * np.log(1 - a) - 0.25 * (1 - a) ** 2) + g
    xl = np.where(x > 0, x * np.log(np.maximum(x, 1e-300)), 0.0)
    return 1 / (2 * np.pi * (a + 1)) * (
        1 / (1 - a) * (0.5 * L(a - x) - 0.5 * L(1 - x) + 0.25 * (1 - x) ** 2 - 0.25 * (a - x) ** 2)
        - xl + g - h * x)


if __name__ == "__main__":
    xs = np.linspace(0, 1, 20001)
    y = mean_a(xs)
    print(f"a=0.8 mean line, CLi=1: max y/c = {y.max():.5f} at x/c = {xs[y.argmax()]:.3f}")

    for Z in (3, 4, 5):
        ear = Z / np.pi * 2 * quad(lambda x: cD(x), .2, 1, limit=200)[0]
        par = Z / np.pi * 2 * quad(lambda x: cD(x) * np.cos(np.arctan(pD(x) / (np.pi * x))), .2, 1, limit=200)[0]
        print(f"Z={Z}: EAR = {ear:.4f}, PAR = {par:.4f}, PAR/EAR = {par/ear:.3f}")

    for x in (.2, .3, .5, .7, .9, 1.0):
        phi = np.degrees(np.arctan(pD(x) / (np.pi * x)))
        print(f"r/R={x:.2f}: P/D={float(pD(x)):.4f} phi={phi:6.2f} deg  c/D={float(cD(x)):.4f}  t/c={float(tD(x)/max(cD(x),1e-9)):.4f}")
    # pitch at 0.7R is the usual 'nominal' value
    print("nominal P/D(0.7) =", float(pD(.7)))

    # ---- validation (run_validations.py looks for FAILED) ----
    def check(name, ok):
        print(f"{'PASS' if ok else 'FAILED'}  {name}")
        return ok
    ear3 = 3 / np.pi * 2 * quad(lambda x: cD(x), .2, 1, limit=200)[0]
    oks = [
        check("a=0.8 mean line: max camber 0.0679 at C_Li = 1 (Abbott & von Doenhoff)", abs(y.max() - 0.0679) < 2e-4),
        check("interpolation reproduces the DTMB 4119 table", all(abs(float(cD(x)) - c) < 1e-9 for x, c in zip(X, CD))
              and all(abs(float(pD(x)) - p) < 1e-12 for x, p in zip(X, PD))),
        check("DTMB 4119 EAR within 2% of nominal 0.60", abs(ear3 - 0.60) / 0.60 < 0.02),
        check("chord and thickness close to zero at the tip", float(cD(1.0)) == 0.0 and float(tD(1.0)) == 0.0),
        check("PAR < EAR for positive pitch", all(
            quad(lambda x: cD(x) * np.cos(np.arctan(pD(x) / (np.pi * x))), .2, 1)[0] < quad(lambda x: cD(x), .2, 1)[0] for _ in [0])),
    ]
    raise SystemExit(0 if all(oks) else 1)
