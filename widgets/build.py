"""
把共用核心（widgets/src/core/*.js）、共用樣式（widget.css）和每個元件的程式、版面組成單一、自給自足的 ESM 檔，
放到 widgets/dist/，供 MyST 的 {anywidget} 指令載入。

MyST 會把 {anywidget} 指到的檔案複製進網站，但不會解析其中的 import，
所以每個元件都要先在這裡打包成一個檔案。
用法：python widgets/build.py
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC, DIST = HERE / "src", HERE / "dist"

# 元件名稱 → 需要的核心模組（依序串接）
WIDGETS = {}  # 目前只有 proto-embed；之後的自製元件加在這裡
# 不需要打包、直接複製的獨立元件（widgets/src/名稱.mjs）
STANDALONE = ["proto-embed"]


def _read(path):
    return path.read_text(encoding="utf-8")


def build(name, cores, dist=DIST, read=_read):
    """read(path) 讀原始檔；英文版由 tools/build_en.py 傳入翻譯過的讀檔函式"""
    core = "\n".join(read(SRC / "core" / c) for c in cores)
    markup = read(SRC / f"{name}.html")
    body = read(SRC / f"{name}.js")
    body = "\n".join("  " + line for line in body.splitlines())
    css = (SRC / "widget.css").read_text(encoding="utf-8")
    out = f"""// 由 widgets/build.py 產生，請勿直接編輯；原始碼在 widgets/src/
{core}

const MARKUP = {json.dumps(markup, ensure_ascii=False)};
const CSS = {json.dumps(css, ensure_ascii=False)};

function render({{ model, el }}) {{
  // 樣式直接內嵌：不依賴 :css: 選項，元件放在任何頁面都長一樣
  el.innerHTML = `<style>${{CSS}}</style><div class="wroot">${{MARKUP}}</div>`;
  const root = el;
  const $ = s => root.querySelector(s);
{body}
}}

export default {{ render }};
"""
    (dist / f"{name}.mjs").write_text(out, encoding="utf-8")
    print("built", dist / f"{name}.mjs", f"({len(out)/1024:.1f} kB)")


if __name__ == "__main__":
    DIST.mkdir(exist_ok=True)
    for name, cores in WIDGETS.items():
        build(name, cores)
    for name in STANDALONE:
        (DIST / f"{name}.mjs").write_bytes((SRC / f"{name}.mjs").read_bytes())
        print("copied", DIST / f"{name}.mjs")
