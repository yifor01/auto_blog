---
title: 'Cloudflare Introduces Kitesurf: An Agent-First Web Browser That Runs Entirely
  in V8 Isolates on Cloudflare Workers'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/06/cloudflare-introduces-kitesurf-an-agent-first-web-browser-that-runs-entirely-in-v8-isolates-on-cloudflare-workers/
model: tencent/hy3:free
generated_at: '2026-08-07T07:27:30.533902'
score: 112
---

📌 【Cloudflare 新技術】拋棄 Chromium！專為 AI Agent 設計的 Kitesurf 瀏覽器正式登場

TL;DR：Kitesurf 是運行於 Cloudflare Workers V8 Isolates 的無狀態瀏覽器，大幅降低 AI 代理執行任務的成本與資源消耗。

當前主流的瀏覽器引擎（如 Chromium）主要是為了人類設計，其龐大的記憶體與運算開銷，使得「一個 AI 代理配一個瀏覽器」的模式變得極度昂貴。對於 AI 代理而言，它們不需要標籤頁、擴充功能，也不需要 60-fps 的流暢渲染，它們真正需要的是機器可讀的內容、低 Token 開銷、高擴展性，以及防止 Prompt Injection（提示詞注入）的隔離機制。

🧩 **捨棄視覺渲染，專注機器可讀內容**

Cloudflare 推出的 Kitesurf 採取了完全不同的設計理念：直接捨棄人類介面，保留模型真正需要的組件。

- **架構設計**：將瀏覽器拆分為多個隔離的 Workers 組件。
- **無狀態設計**：除了 Engine（引擎）是唯一的公開介面（透過 WebSocket 傳輸 CDP 協定與 HTTP REST）並儲存 Session 狀態外，其餘組件皆為無狀態且可隨時丟棄。
- **PageScript 隔離機制**：每個頁面或跨進程的 iframe 都擁有獨立的長效 Isolate，並具備乾淨的 `globalThis` 與 DOM。
- **核心引擎技術**：
    - HTML/CSS 解析：使用 Rust 編寫的 Blitz 模組化渲染引擎與 Stylo (Firefox 的 CSS 解析器)。
    - JS 執行：由於 Workers 不支援原生 `eval`，透過 Boa JS (Rust 編寫的 ECMAScript 引擎) 來執行。
    - 渲染與圖形：使用 blitz-paint 與 Parley 進行圖像渲染與文字塑形。
- **安全性隔離**：專門的 `SandboxOutbound` worker 負責處理所有網路請求，負責執行 CORS、注入瀏覽器標頭、維護 Cookie 罐，並對違規請求回傳 403。

📊 **效能表現：CPU 與記憶體消耗大幅下降**

根據 Cloudflare 在 14 個 URL 測試集上的數據顯示，Kitesurf 在處理 AI 代理常見的爆發式工作負載時，具備極高的成本效益：

| 任務類型 | 評估指標 | Kitesurf | Chromium | 效能提升 |
| :--- | :--- | :--- | :--- | :--- |
| 截圖 (Screenshot) | CPU 消耗 | 380 ms | 1,173 ms | **3.1× 較低** |
| 截圖 (Screenshot) | 記憶體消耗 | 57.8 MiB | 271.0 MiB | **4.7× 較低** |
| HTML 提取 | CPU 消耗 | 229 ms | 877 ms | **3.8× 較低** |
| HTML 提取 | 記憶體消耗 | 39.4 MiB | 273.7 MiB | **7.0× 較低** |

*註：雖然 Kitesuf 在牆鐘時間 (Wall time) 上因渲染與編碼原因比 Chromium 慢約 1.7~1.8 倍，但由於 CPU 與記憶體是驅動雲端帳單的核心指標，對於代理工作負載而言，Kitesurf 具備顯著優勢。*

⚙️ **開發者整合成本極低**

對於工程師來說，切換到 Kitesurf 幾乎不需要修改現有的程式碼邏輯。

- **無縫整合**：現有的 Puppeteer、Playwright、chrome-remote-interface 與 MCP 用戶，只需在 Browser Run 的 CDP 端點或 Quick Actions API 中加入 `browser=kitesurf` 參數即可使用。
- **測試與相容性**：目前已通過超過 215,000 項 Web Platform Tests (WPT)，並能成功渲染 TodoMVC (包含 React, Vue, Angular 等框架)、Wikipedia 與 Hacker News。
- **混合模式**：對於複雜頁面，建議將 Chromium 作為 fallback（備援）方案；對於相容網站與單次任務，Kitesurf 表現強勁。

🎯 **實務啟示**

如果你正在開發需要大規模、高頻率與網頁互動的 AI Agent，Kitesurf 提供了一個「生產環境就緒 (Production-adjacent)」的選擇。它透過 V8 Isolates 解決了傳統瀏覽器在雲端運算上的資源浪費問題，讓工程師能以更低的成本實現大規模的自動化網頁任務。

🔗 **來源**
- 標題：Cloudflare Introduces Kitesurf: An Agent-First Web Browser That Runs Entirely in V8 Isolates on Cloudflare Workers
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/06/cloudflare-introduces-kitesurf-an-agent-first-web-browser-that-runs-entirely-in-v8-isolates-on-cloudflare-workers/

#AI #Cloudflare #Kitesurf #AIAgent #WebBrowser #V8Isolates #CloudWorkers #Puppeteer #Playwright #MachineLearning
