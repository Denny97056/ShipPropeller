"""一次執行 code/ 裡所有模組的驗證，最後列出結果"""
import subprocess
import sys
from pathlib import Path

CODE = Path(__file__).resolve().parents[1] / "code"
MODULES = ["prop_geometry", "prop_momentum"]

results = []
for m in MODULES:
    r = subprocess.run([sys.executable, f"{m}.py"], cwd=CODE, capture_output=True, text=True)
    out = r.stdout + r.stderr
    ok = r.returncode == 0 and "FAILED" not in out
    results.append((m, ok))
    print(out)
    print(f"{'PASS' if ok else 'FAIL'}  {m}")
print(f"\n{sum(ok for _, ok in results)}/{len(results)} modules passed")
sys.exit(0 if all(ok for _, ok in results) else 1)
