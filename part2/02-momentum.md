# 第 2 章　致動盤、葉素理論與敞水曲線

## 2.1 致動盤：推力就是動量的增加

先把螺旋槳想成一片很薄、會讓水壓突然升高的圓盤，不管葉片的形狀。穿過圓盤的水被加速，流管往下游收縮。對流管用動量守恆，再對盤前、盤後各用一次白努利方程，可以得到圓盤處的速度增量正好是遠方尾流增量的一半：

$$
V_{disk} = V_A(1 + a), \qquad V_{wake} = V_A(1 + 2a), \qquad
C_T = \frac{T}{\tfrac12 \rho A V_A^2} = 4a(1 + a)
$$

有用功率是 $T V_A$，槳交給水的功率是 $T V_A(1 + a)$，所以理想效率

$$
\eta_i = \frac{1}{1 + a} = \frac{2}{1 + \sqrt{1 + C_T}}
$$

這是任何推進器都超越不了的上限，損失的部分是留在尾流裡的動能。負載越重（$C_T$ 越大），要把水加速得越多，效率越低。要降低 $C_T$，最直接的辦法是加大直徑：同樣的推力分給更多的水。

```{anywidget} ../widgets/dist/proto-embed.mjs
{"file": "momentum.html", "section": "s1"}
```

:::{note}
致動盤假設流體無黏、推力均勻分布在盤面上、尾流不旋轉。流管的形狀用均勻負載圓盤的中心線速度 $V_A[1 + a(1 + x/\sqrt{x^2 + R^2})]$ 配連續方程近似，只是示意。下一節的葉素理論會把旋轉和黏性損失加回來。
:::

## 2.2 速度三角形：一個剖面看到什麼

回到葉片本身。在半徑 $r$ 的剖面上，水從前方以 $V_A$ 流來，剖面本身以 $\omega r$ 轉動。兩者合成的角度叫進角 $\beta$：

$$
\tan\beta = \frac{V_A}{\omega r} = \frac{J}{\pi\, r/R}
$$

槳在推水，水也反過來被槳帶動：軸向多了 $aV_A$，切向被帶著轉了 $a'\omega r$。剖面真正看到的相對速度 $W$ 的方向是誘導進角 $\beta_i$，攻角是螺距角減去它：

$$
\tan\beta_i = \frac{V_A(1 + a)}{\omega r(1 - a')}, \qquad \alpha = \varphi - \beta_i
$$

升力 $dL$ 垂直於 $W$，阻力 $dD$ 沿著 $W$，投影到軸向和切向就是推力與扭矩：

$$
dT = dL\cos\beta_i - dD\sin\beta_i, \qquad dQ = r\,(dL\sin\beta_i + dD\cos\beta_i)
$$

把這個剖面的效率 $dT\,V_A / (dQ\,\omega)$ 整理一下，正好拆成三個因子：

$$
\eta_{section} = \underbrace{\frac{1}{1 + a}}_{\text{軸向}}\;\underbrace{(1 - a')}_{\text{旋轉}}\;\underbrace{\frac{\tan\beta_i}{\tan(\beta_i + \gamma)}}_{\text{黏性}}, \qquad \tan\gamma = \frac{C_D}{C_L}
$$

第一項就是致動盤的那一項；第二項是尾流旋轉帶走的能量；第三項是剖面阻力。拉動 $J$ 會看到：重負載（$J$ 小）時軸向損失主導，輕負載時升力變小，黏性損失的比例變大。

```{anywidget} ../widgets/dist/proto-embed.mjs
{"file": "momentum.html", "section": "s2"}
```

:::{note}
互動圖裡的 $a$、$a'$ 是 DTMB 4119 用下一節的葉素–動量理論解出來的值。
:::

## 2.3 葉素–動量理論：把整支槳積分起來

前一節的 $a$ 和 $a'$ 要怎麼求？把槳盤切成一圈一圈的環，每個環同時滿足兩件事：葉剖面算出來的力（2.2），要等於這個環的動量變化（2.1 的致動盤，只是換成一個環）：

$$
dT = 4\pi r\,\rho V_A^2 (1 + a)\, a F\, dr, \qquad
dQ = 4\pi r^3 \rho V_A\, \omega (1 + a)\, a' F\, dr
$$

兩組式子各自有 $a$、$a'$，反覆代入直到收斂。$F$ 是 Prandtl 葉尖修正：

$$
F = \frac{2}{\pi}\arccos\left[\exp\left(-\frac{Z}{2}\,\frac{1 - r/R}{(r/R)\sin\beta_i}\right)\right]
$$

葉數有限，水會從葉尖繞過去，越靠近葉尖，動量理論高估得越多，$F$ 就把它往下修。積分後用無因次係數表示：

$$
K_T = \frac{T}{\rho n^2 D^4}, \qquad K_Q = \frac{Q}{\rho n^2 D^5}, \qquad \eta_0 = \frac{J}{2\pi}\frac{K_T}{K_Q}
$$

和 DTMB 4119 的試驗比較：在設計點 $J = 0.833$，效率算得很準（0.700 對 0.691），但 $K_T$ 和 $K_Q$ 都高估了四成多（$K_T$ 0.215 對 0.146）。原因是剖面用了二維翼型的升力：寬葉片上的流線是彎的，實際的有效拱度和攻角都比較小。第三篇的升力線與升力面修正會處理這件事。

```{anywidget} ../widgets/dist/proto-embed.mjs
{"file": "momentum.html", "section": "s3"}
```

:::{note}
剖面升力用薄翼理論 $C_L = 2\pi(\alpha - \alpha_0)$。零升力角 $\alpha_0$ 由 $a = 0.8$ 平均線積分而得，$C_{Li} = 1$ 時為 $-7.58°$，再乘上各半徑的 $C_{Li}$；同一個積分給出的理想攻角是 1.52°，與 Abbott & von Doenhoff 的 1.54° 相符。阻力係數沿半徑取定值（預設 0.008）。
:::

## 2.4 敞水曲線與 B 系列：用圖表選槳

敞水曲線是槳在均勻來流中的「身分證」：橫軸 $J$，縱軸 $K_T$、$10K_Q$ 和 $\eta_0$。$J$ 小代表重負載（推力大、效率低），$J$ 接近 $P/D$ 時推力趨近於零。

Wageningen B 系列是荷蘭 MARIN 系統化試驗的一百多支模型槳。Oosterveld 與 van Oossanen（1975）把結果迴歸成多項式，$K_T$ 有 39 項、$K_Q$ 有 47 項：

$$
K_T = \sum_{k=1}^{39} C_k\, J^{s_k} (P/D)^{t_k} (A_E/A_0)^{u_k} Z^{v_k}
$$

典型的選槳問題：已知進速 $V_A$（船速扣掉伴流）、需要的推力 $T$（阻力加上推力減額）和直徑 $D$，求轉速和螺距。把 $n$ 消掉，

$$
\frac{K_T}{J^2} = \frac{T}{\rho D^2 V_A^2}
$$

右邊是已知的常數，所以設計點一定落在拋物線 $K_T = cJ^2$ 上。每個 $P/D$ 和拋物線各有一個交點，挑效率最高的那個，再由 $n = V_A/(JD)$ 求轉速。如果給的是轉速、要求直徑，則改用 $K_T/J^4 = Tn^2/(\rho V_A^4)$，做法相同。

```{anywidget} ../widgets/dist/proto-embed.mjs
{"file": "momentum.html", "section": "s4"}
```

:::{note}
迴歸式的適用範圍是 $Z$ = 2–7、$A_E/A_0$ = 0.30–1.05、$P/D$ = 0.5–1.4，雷諾數 $2\times10^6$；各葉數實際試驗過的面積比範圍更窄，互動圖會在外插時提醒。預設值重現 MIT 2.611 講義的例題：B5-75、$K_T/J^2 = 0.544$，最佳 $P/D = 1.0$、$J = 0.64$、$\eta_0 = 0.61$。
:::

## 參考資料

1. 致動盤與葉素理論：Carlton, *Marine Propellers and Propulsion*；Kerwin & Hadler, *Propulsion*（SNAME PNA 系列）。
2. B 系列迴歸式：Oosterveld & van Oossanen (1975), "Further computer-analyzed data of the Wageningen B-screw series", *International Shipbuilding Progress* 22。
3. 選槳例題與檢核值：MIT OpenCourseWare 2.611 *Marine Power and Propulsion*（2006），"Using KT and KQ for design"。
4. DTMB 4119 試驗值：Jessup (1989)；ITTC 1998 推進委員會的計算比對工作坊。
5. $a = 0.8$ 平均線的理想攻角：Abbott & von Doenhoff, *Theory of Wing Sections*。
