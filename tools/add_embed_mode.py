"""
替 prototypes/*.html 加上「嵌入模式」，並把頁尾連到 claude.ai 的連結改成站內相對連結。
可重複執行（已加過就略過）。

嵌入模式：網址加 ?embed=<節 id>（或 ?embed=hero）時，只顯示那一節的控制項與圖，
說明文字隱藏（書頁本身已有），並把頁面高度用 postMessage 回報給外層的 iframe。
?theme=dark|light 可指定深淺色。
用法：python tools/add_embed_mode.py   （在書的根目錄執行）
"""
from pathlib import Path

PROTO = Path(__file__).resolve().parents[1] / "prototypes"
MARK = "embed-mode"

ARTIFACTS = {  # claude.ai 上的原型網址 → 站內檔名
    "https://claude.ai/artifact/KzC9geXmFzDmyhAK2s1tU8": "geometry.html",
}

HEAD = """<!-- embed-mode: 指定深淺色（要在繪圖前設定） -->
<script>
(function(){
  var t = new URLSearchParams(location.search).get("theme");
  if (t === "dark" || t === "light") document.documentElement.dataset.theme = t;
})();
</script>
"""

BODY = """<!-- embed-mode: ?embed=<節 id> 時只顯示那一節，供書頁以 iframe 嵌入 -->
<style>
html.embed body{ background:var(--paper); }
html.embed body > :not(.embed-target):not(script):not(style){ display:none !important; }
html.embed .embed-target{ display:block; max-width:none; margin:0; padding:.9rem 1rem 1rem; border-top:0; }
html.embed .embed-target .text{ position:static; }
html.embed .embed-target .text > :is(h2,p,.eq,.eqs){ display:none; }
html.embed header.embed-target > div:first-child > :is(h1,p){ display:none; }
html.embed .embed-target .controls{ margin:0 0 1rem; grid-template-columns:repeat(auto-fill,minmax(15rem,1fr)); column-gap:1.5rem; }
html.embed .embed-target .stage{ margin-top:.5rem; }
</style>
<script>
(function(){
  var id = new URLSearchParams(location.search).get("embed");
  if (!id) return;
  var target = id === "hero" ? document.querySelector("header.hero") : document.getElementById(id);
  if (!target) return;
  target.classList.add("embed-target");
  document.documentElement.classList.add("embed");
  function send(){
    parent.postMessage({ type: "ship-proto-height", id: id,
      height: Math.ceil(target.getBoundingClientRect().height) + 2 }, "*");
  }
  if (window.ResizeObserver) new ResizeObserver(send).observe(target);
  window.addEventListener("load", send);
  send();
})();
</script>
"""

for f in sorted(PROTO.glob("*.html")):
    s = f.read_text(encoding="utf-8")
    for url, name in ARTIFACTS.items():
        s = s.replace(url, name)
    if MARK not in s:
        s = s.replace("</head>", HEAD + "</head>", 1)
        i = s.rfind("</body>")
        s = s[:i] + BODY + s[i:]
    f.write_text(s, encoding="utf-8")
    print("ok", f.name)
