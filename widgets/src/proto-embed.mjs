// 把 prototypes/ 裡的原型互動頁的某一節，以 iframe 嵌進書頁（不依賴任何外部服務）
// 用法：
//   ```{anywidget} ../widgets/dist/proto-embed.mjs
//   {"file": "longitudinal.html", "section": "s1"}
//   ```
// section 可以是節的 id（s1、ch4…）或 "hero"（篇首的總覽圖）。
// prototypes/ 會在建置後複製到網站根目錄（見 .github/workflows/deploy.yml），
// 而 MyST 把這個 .mjs 放在 <網站根目錄>/build/，所以用 ../prototypes/ 找得到。

function render({ model, el }) {
  const file = model.get("file");
  const section = model.get("section") || "hero";
  const root = document.documentElement;
  const theme = () => (root.classList.contains("dark") ? "dark" : "light");

  const page = new URL(`../prototypes/${file}`, import.meta.url);
  const src = new URL(page);
  src.searchParams.set("embed", section);
  src.searchParams.set("theme", theme());
  const full = new URL(page);
  if (section !== "hero") full.hash = section;

  el.innerHTML = `
    <div style="margin:1rem 0">
      <iframe src="${src}" title="互動圖" loading="lazy"
        style="display:block;width:100%;height:640px;border:1px solid #C9D2D5;border-radius:6px;background:transparent"></iframe>
      <div style="text-align:right;font-size:.85rem;margin-top:.3rem">
        <a href="${full}" target="_blank" rel="noopener">在新分頁開啟完整互動頁 ↗</a>
      </div>
    </div>`;
  const frame = el.querySelector("iframe");

  // 原型頁在嵌入模式會回報自己的高度，讓 iframe 不出現捲軸
  const onMessage = (e) => {
    if (e.source === frame.contentWindow && e.data && e.data.type === "ship-proto-height") {
      frame.style.height = `${e.data.height}px`;
    }
  };
  window.addEventListener("message", onMessage);

  // 書的深淺色切換時，同步給原型頁（同源，可直接設定）
  const observer = new MutationObserver(() => {
    try { frame.contentDocument.documentElement.dataset.theme = theme(); } catch (_) { /* 尚未載入 */ }
  });
  observer.observe(root, { attributes: true, attributeFilter: ["class"] });

  return () => {
    window.removeEventListener("message", onMessage);
    observer.disconnect();
  };
}

export default { render };
