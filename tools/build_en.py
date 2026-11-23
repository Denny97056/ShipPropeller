"""產生英文版的互動資源：
  prototypes/*.html          → en/prototypes/*.html
  widgets/src/proto-embed.mjs → en/widgets/dist/proto-embed.mjs
用 tools/i18n_en.py 的對照表逐段替換；沒找到的對照或殘留的中文會列出並失敗。
用法：python tools/build_en.py   （先跑 tools/add_embed_mode.py）"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import i18n_en  # noqa: E402

CJK = re.compile(r"[　-〿一-鿿＀-￯]")
JOBS = [  # (來源, 輸出, 對照表)
    (ROOT / "prototypes/geometry.html", ROOT / "en/prototypes/geometry.html", i18n_en.GEOMETRY),
    (ROOT / "prototypes/momentum.html", ROOT / "en/prototypes/momentum.html", i18n_en.MOMENTUM),
    (ROOT / "widgets/src/proto-embed.mjs", ROOT / "en/widgets/dist/proto-embed.mjs", i18n_en.PROTO_EMBED),
]


def strip_cjk_comments(s):
    s = re.sub(r"/\*(?:(?!\*/).)*?[一-鿿](?:(?!\*/).)*?\*/", "/* */", s, flags=re.S)
    return re.sub(r"//[^\n]*[一-鿿][^\n]*", "", s)


bad = 0
for src, dst, table in JOBS:
    s = src.read_text(encoding="utf-8")
    for zh, en in table:
        if zh not in s:
            print(f"NOT FOUND in {src.name}: {zh[:60]}")
            bad += 1
        s = s.replace(zh, en)
    s = strip_cjk_comments(s)
    left = [ln.strip()[:100] for ln in s.splitlines() if CJK.search(ln)]
    for ln in left:
        print(f"UNTRANSLATED in {src.name}: {ln}")
    bad += len(left)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(s, encoding="utf-8")
    print("wrote", dst.relative_to(ROOT))
sys.exit(1 if bad else 0)
