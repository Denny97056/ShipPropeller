# 程式與驗證

每個模組都可以直接執行（`python code/模組名稱.py`），會印出它的驗證案例與結果。一次執行全部：

```bash
python tools/run_validations.py
```

| 篇 | 模組 | 內容 | 主要驗證 |
|---|---|---|---|
| 一 | `prop_geometry.py` | DTMB 4119 徑向分布的內插、*a* = 0.8 平均線、展開與投影面積比 | 平均線最大拱度 0.0679（*C*{sub}`Li` = 1）、內插通過原始表格、EAR 與標稱 0.60 相差 2% 內、PAR < EAR |

互動圖（`prototypes/`）裡的 JavaScript 用和這些模組相同的公式與內插方法，數值一致（例如三葉 EAR = 0.607、PAR = 0.500）。
