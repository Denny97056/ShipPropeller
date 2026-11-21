# 船用螺旋槳：從幾何到面元法（互動式教材）

以 [Jupyter Book 2](https://jupyterbook.org)（MyST）建置的互動式電子書，網站：<https://denny97056.github.io/MarinePropeller/>（英文版在 `/en/`）。
架構與 [ShipStructure](https://github.com/Denny97056/ShipStructure) 相同。

## 本機建置

```bash
pip install -r requirements.txt     # 需要 Node.js 18 以上
python tools/run_validations.py     # 先跑所有 Python 模組的驗證
python tools/add_embed_mode.py      # 替原型頁加上嵌入模式（可重複執行）
python widgets/build.py             # 打包互動元件到 widgets/dist/
jupyter book build --html           # 輸出靜態網站到 _build/html/
```

## 發布

推到 GitHub 的 `main` 分支後，`.github/workflows/deploy.yml` 會自動驗證、打包元件、建置並發布到
GitHub Pages（需在儲存庫的 Settings → Pages 把來源設為 GitHub Actions）。

## 資料夾

| 路徑 | 內容 |
|---|---|
| `myst.yml` | 書的設定與目錄 |
| `index.md`、`part1/`、`appendix/` | 各章內容（MyST Markdown） |
| `code/` | Python 模組，每個都附驗證 |
| `prototypes/` | 互動頁（單一 HTML），各章以 iframe 嵌入其中一節（`?embed=s1`） |
| `widgets/src/proto-embed.mjs` | 把原型頁的一節嵌進書頁的 anywidget 元件 |
| `tools/` | 嵌入模式、英文版產生、一次執行全部驗證 |

## 英文版（/en/）

英文章節文字在 `en/`，自己有一份 `en/myst.yml`。互動頁不另外維護：`tools/build_en.py` 讀
`prototypes/` 與 `widgets/src/`，用 `tools/i18n_en.py` 的對照表把中文換成英文，產生 `en/prototypes/`
與 `en/widgets/dist/`。改了中文原型頁之後重跑即可；沒翻到的文字會列出並讓建置失敗。

```bash
python tools/build_en.py
cd en && jupyter book build --html
```
