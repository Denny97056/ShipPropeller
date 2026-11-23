"""Reference numbers for 第二篇 動量與葉素理論 (propeller handout).

Same formulas as the page's JS core (prototypes/momentum.html):
  - actuator disk: C_T = T / (0.5 rho A V_A^2), eta_i = 2 / (1 + sqrt(1 + C_T))
  - Wageningen B-series open water polynomials (Oosterveld & van Oossanen 1975, Re = 2e6),
    39 K_T terms and 47 K_Q terms
  - blade-element momentum theory (BEMT) for DTMB 4119 with the Prandtl tip factor,
    2D section lift  C_L = 2 pi (alpha - alpha_0),  alpha_0 from thin-airfoil theory
    of the a = 0.8 mean line, constant section drag C_D
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

import prop_geometry as G

# ------------------------------------------------------------------ actuator disk
def eta_ideal(CT):
    """Ideal (Froude) efficiency of an actuator disk at thrust loading C_T."""
    return 2.0 / (1.0 + np.sqrt(1.0 + CT))


def disk_a(CT):
    """Axial induction factor at the disk: u_disk = a V_A, far wake 2 a V_A."""
    return 0.5 * (np.sqrt(1.0 + CT) - 1.0)


# ------------------------------------------------------------------ B-series
# columns: C, s (J), t (P/D), u (AE/A0), v (Z)
KT_TAB = np.array([
    [0.00880496, 0, 0, 0, 0], [-0.204554, 1, 0, 0, 0], [0.166351, 0, 1, 0, 0], [0.158114, 0, 2, 0, 0],
    [-0.147581, 2, 0, 1, 0], [-0.481497, 1, 1, 1, 0], [0.415437, 0, 2, 1, 0], [0.0144043, 0, 0, 0, 1],
    [-0.0530054, 2, 0, 0, 1], [0.0143481, 0, 1, 0, 1], [0.0606826, 1, 1, 0, 1], [-0.0125894, 0, 0, 1, 1],
    [0.0109689, 1, 0, 1, 1], [-0.133698, 0, 3, 0, 0], [0.00638407, 0, 6, 0, 0], [-0.00132718, 2, 6, 0, 0],
    [0.168496, 3, 0, 1, 0], [-0.0507214, 0, 0, 2, 0], [0.0854559, 2, 0, 2, 0], [-0.0504475, 3, 0, 2, 0],
    [0.010465, 1, 6, 2, 0], [-0.00648272, 2, 6, 2, 0], [-0.00841728, 0, 3, 0, 1], [0.0168424, 1, 3, 0, 1],
    [-0.00102296, 3, 3, 0, 1], [-0.0317791, 0, 3, 1, 1], [0.018604, 1, 0, 2, 1], [-0.00410798, 0, 2, 2, 1],
    [-0.000606848, 0, 0, 0, 2], [-0.0049819, 1, 0, 0, 2], [0.0025983, 2, 0, 0, 2], [-0.000560528, 3, 0, 0, 2],
    [-0.00163652, 1, 2, 0, 2], [-0.000328787, 1, 6, 0, 2], [0.000116502, 2, 6, 0, 2], [0.000690904, 0, 0, 1, 2],
    [0.00421749, 0, 3, 1, 2], [0.0000565229, 3, 6, 1, 2], [-0.00146564, 0, 3, 2, 2]])
KQ_TAB = np.array([
    [0.00379368, 0, 0, 0, 0], [0.00886523, 2, 0, 0, 0], [-0.032241, 1, 1, 0, 0], [0.00344778, 0, 2, 0, 0],
    [-0.0408811, 0, 1, 1, 0], [-0.108009, 1, 1, 1, 0], [-0.0885381, 2, 1, 1, 0], [0.188561, 0, 2, 1, 0],
    [-0.00370871, 1, 0, 0, 1], [0.00513696, 0, 1, 0, 1], [0.0209449, 1, 1, 0, 1], [0.00474319, 2, 1, 0, 1],
    [-0.00723408, 2, 0, 1, 1], [0.00438388, 1, 1, 1, 1], [-0.0269403, 0, 2, 1, 1], [0.0558082, 3, 0, 1, 0],
    [0.0161886, 0, 3, 1, 0], [0.00318086, 1, 3, 1, 0], [0.015896, 0, 0, 2, 0], [0.0471729, 1, 0, 2, 0],
    [0.0196283, 3, 0, 2, 0], [-0.0502782, 0, 1, 2, 0], [-0.030055, 3, 1, 2, 0], [0.0417122, 2, 2, 2, 0],
    [-0.0397722, 0, 3, 2, 0], [-0.00350024, 0, 6, 2, 0], [-0.0106854, 3, 0, 0, 1], [0.00110903, 3, 3, 0, 1],
    [-0.000313912, 0, 6, 0, 1], [0.0035985, 3, 0, 1, 1], [-0.00142121, 0, 6, 1, 1], [-0.00383637, 1, 0, 2, 1],
    [0.0126803, 0, 2, 2, 1], [-0.00318278, 2, 3, 2, 1], [0.00334268, 0, 6, 2, 1], [-0.00183491, 1, 1, 0, 2],
    [0.000112451, 3, 2, 0, 2], [-0.0000297228, 3, 6, 0, 2], [0.000269551, 1, 0, 1, 2], [0.00083265, 2, 0, 1, 2],
    [0.00155334, 0, 2, 1, 2], [0.000302683, 0, 6, 1, 2], [-0.0001843, 0, 0, 2, 2], [-0.000425399, 0, 3, 2, 2],
    [0.0000869243, 3, 3, 2, 2], [-0.0004659, 0, 6, 2, 2], [0.0000554194, 1, 6, 2, 2]])


def _poly(T, J, pd, ear, z):
    return float(np.sum(T[:, 0] * J ** T[:, 1] * pd ** T[:, 2] * ear ** T[:, 3] * z ** T[:, 4]))


def bseries(J, pd, ear, z):
    """(K_T, K_Q, eta_0) of a Wageningen B-series propeller."""
    kt, kq = _poly(KT_TAB, J, pd, ear, z), _poly(KQ_TAB, J, pd, ear, z)
    return kt, kq, J * kt / (2 * np.pi * kq)


# ------------------------------------------------------------------ BEMT
Z = 3
YMAX = 0.06794                     # max camber of the a = 0.8 mean line at C_Li = 1


def _dz(x, h=1e-6):
    return (G.mean_a(x + h) - G.mean_a(x - h)) / (2 * h)


_th = lambda t: (1 - np.cos(t)) / 2
# thin-airfoil theory for the a = 0.8 mean line at C_Li = 1 (alpha from the nose-tail line)
ALPHA0 = float(-1 / np.pi * quad(lambda t: _dz(_th(t)) * (np.cos(t) - 1), 1e-6, np.pi - 1e-6, limit=200)[0])
ALPHAI = float(1 / np.pi * quad(lambda t: _dz(_th(t)), 1e-6, np.pi - 1e-6, limit=200)[0])
ALPHA0_ROUND = -0.13228            # value hard-coded in the JS (rad); checked below

NEL, NIT, RELAX = 40, 300, 0.3


def element(x, J, cd=0.008, tip=True):
    """Solve one blade element of DTMB 4119 at radius x = r/R and advance ratio J.
    Units: R = 1, n = 1 rev/s, so V_A = 2J and omega r = 2 pi x.
    Returns dict with induction factors, angles and dK_T/dx, dK_Q/dx."""
    c = 2 * float(G.cD(x))
    phi = np.arctan(float(G.pD(x)) / (np.pi * x))
    al0 = ALPHA0_ROUND * float(G.fC(x)) / YMAX
    Va, wr = 2 * J, 2 * np.pi * x
    a, ap = 0.1, 0.01
    for _ in range(NIT):
        ua, ut = Va * (1 + a), wr * (1 - ap)
        bi = np.arctan2(ua, ut)
        W2 = ua * ua + ut * ut
        CL = 2 * np.pi * (phi - bi - al0)
        F = max(2 / np.pi * np.arccos(np.exp(-Z * (1 - x) / (2 * x * np.sin(bi)))), 1e-3) if tip else 1.0
        dT = 0.5 * W2 * Z * c * (CL * np.cos(bi) - cd * np.sin(bi))          # dT/dr per rho
        dQ = 0.5 * W2 * Z * c * (CL * np.sin(bi) + cd * np.cos(bi)) * x      # dQ/dr per rho
        an = (-1 + np.sqrt(max(1 + dT / (np.pi * x * Va * Va * F), 0.01))) / 2
        apn = dQ / (4 * np.pi * x ** 3 * Va * (1 + an) * 2 * np.pi * F)
        a, ap = (1 - RELAX) * a + RELAX * an, (1 - RELAX) * ap + RELAX * apn
    return dict(a=a, ap=ap, phi=phi, bi=bi, beta=np.arctan(J / (np.pi * x)), alpha=phi - bi, CL=CL, F=F,
                dKT=dT / 16, dKQ=dQ / 32, W2=W2,
                resid=dT - 4 * np.pi * x * Va * Va * (1 + a) * a * F)


def bemt(J, cd=0.008, tip=True):
    """Integrate the elements (midpoint rule on 0.2..1) -> K_T, K_Q, eta_0."""
    xs = 0.2 + 0.8 * (np.arange(NEL) + 0.5) / NEL
    els = [element(x, J, cd, tip) for x in xs]
    KT = sum(e["dKT"] for e in els) * 0.8 / NEL
    KQ = sum(e["dKQ"] for e in els) * 0.8 / NEL
    return KT, KQ, J * KT / (2 * np.pi * KQ), xs, els


# measured design point of DTMB 4119 (Jessup 1989; ITTC 1998 workshop)
J_DES, KT_EXP, KQ_EXP = 0.833, 0.146, 0.0280


if __name__ == "__main__":
    print(f"a=0.8 mean line, C_Li=1: ideal angle {np.degrees(ALPHAI):.3f} deg, zero-lift angle {np.degrees(ALPHA0):.3f} deg")
    for CT in (0.5, 1, 2, 5, 10):
        print(f"C_T={CT:5.1f}: a={disk_a(CT):.4f}  eta_i={eta_ideal(CT):.4f}  wake radius ratio={np.sqrt((1+disk_a(CT))/(1+2*disk_a(CT))):.4f}")

    print("\nB-series check (MIT 2.611 notes, B5-75):")
    res = {}
    for n, c in ((2, 0.544), (4, 0.544)):
        best = None
        for pd in (0.6, 0.8, 1.0, 1.2, 1.4):
            J = brentq(lambda J: bseries(J, pd, .75, 5)[0] - c * J ** n, 0.05, pd * 1.1)
            e = bseries(J, pd, .75, 5)[2]
            print(f"  K_T/J^{n} = {c}: P/D={pd:.1f}  J={J:.3f}  eta0={e:.3f}")
            if best is None or e > best[2]:
                best = (pd, J, e)
        res[n] = best
    for J in (0, .2, .4, .6, .8, 1.0):
        kt, kq, e = bseries(J, 1.0, .70, 4)
        print(f"  B4-70 P/D=1.0  J={J:.1f}: K_T={kt:.4f} 10K_Q={10*kq:.4f} eta0={e if J else 0:.3f}")

    print("\nBEMT, DTMB 4119:")
    for J in (0.5, 0.7, 0.833, 0.9, 1.0, 1.1):
        r1, r0 = bemt(J), bemt(J, tip=False)
        print(f"  J={J:.3f}: tip loss K_T={r1[0]:.4f} 10K_Q={10*r1[1]:.4f} eta={r1[2]:.3f} |"
              f" no tip loss K_T={r0[0]:.4f} 10K_Q={10*r0[1]:.4f} eta={r0[2]:.3f}")
    KT, KQ, ETA, xs, els = bemt(J_DES)
    eta_exp = J_DES * KT_EXP / (2 * np.pi * KQ_EXP)
    e7 = element(0.7, J_DES)
    print(f"  0.7R at J=0.833: a={e7['a']:.4f} a'={e7['ap']:.4f} alpha={np.degrees(e7['alpha']):.3f} deg CL={e7['CL']:.4f} F={e7['F']:.4f}")
    print(f"  design point: BEMT K_T={KT:.4f} (exp {KT_EXP}, ratio {KT/KT_EXP:.2f}),"
          f" 10K_Q={10*KQ:.4f} (exp {10*KQ_EXP:.3f}), eta={ETA:.3f} (exp {eta_exp:.3f})")
    CT = KT / J_DES ** 2 * 8 / np.pi
    print(f"  thrust loading C_T={CT:.3f}, actuator-disk eta_i={eta_ideal(CT):.3f}")
    els0 = bemt(J_DES, cd=0.0)[4]
    eta_nodrag = bemt(J_DES, cd=0.0)[2]

    # ---- validation (run_validations.py looks for FAILED) ----
    def check(name, ok):
        print(f"{'PASS' if ok else 'FAILED'}  {name}")
        return ok
    CTs = np.linspace(0.1, 10, 50)
    a = disk_a(CTs)
    oks = [
        check("actuator disk: eta_i = 1/(1+a) and C_T = 4a(1+a)", np.allclose(eta_ideal(CTs), 1 / (1 + a))
              and np.allclose(4 * a * (1 + a), CTs)),
        check("a=0.8 mean line: ideal angle 1.54 deg (Abbott & von Doenhoff) within 0.05 deg",
              abs(np.degrees(ALPHAI) - 1.54) < 0.05),
        check("thin airfoil: C_L at the ideal angle = 1 (2 pi (alpha_i - alpha_0))", abs(2 * np.pi * (ALPHAI - ALPHA0) - 1) < 0.01),
        check("JS constant alpha_0 matches the integral", abs(ALPHA0 - ALPHA0_ROUND) < 2e-5),
        check("B-series: B5-75, K_T/J^2=0.544 -> best P/D 1.0, J 0.64, eta 0.61 (MIT 2.611)",
              res[2][0] == 1.0 and abs(res[2][1] - 0.64) < 0.01 and abs(res[2][2] - 0.61) < 0.01),
        check("B-series: B5-75, K_T/J^4=0.544 -> best P/D 1.0, J 0.74, eta 0.67 (MIT 2.611)",
              res[4][0] == 1.0 and abs(res[4][1] - 0.74) < 0.01 and abs(res[4][2] - 0.67) < 0.01),
        check("BEMT converged: momentum residual < 1e-6 on every element", max(abs(e["resid"]) for e in els) < 1e-6),
        check("BEMT without drag stays below the actuator-disk ideal efficiency", eta_nodrag < eta_ideal(CT)),
        check("BEMT efficiency at the design point within 0.02 of the measured 0.69", abs(ETA - eta_exp) < 0.02),
        check("BEMT over-predicts K_T by 30-60% (no lifting-surface correction; see Part 3)", 1.3 < KT / KT_EXP < 1.6),
    ]
    raise SystemExit(0 if all(oks) else 1)
