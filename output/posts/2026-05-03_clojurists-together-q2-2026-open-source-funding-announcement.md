---
title: "Clojurists Together – Q2 2026 Open Source Funding Announcement"
source: Hacker News
url: https://www.clojuriststogether.org/news/q2-2026-funding-announcement/
score: 52
model: tencent/hy3-preview:free
generated_at: 2026-05-03T19:48:29.884230
---

📌 Clojurists Together Q2 開源資助出爐

Clojurists Together 公布 2026 年 Q2 開源資助名單，總額 3.1 萬美金，5 個獲選專案包含 Clojure 生態 LLM 工具與熱門驗證庫 Malli。
不過這則公告對多數 AI 工程師來說，參考價值可能相當有限。
以下為整理後的重點資訊與分析：

🤔 **Clojure 社群常態化資助開源，本季總額 3.1 萬美金**
Clojurists Together 是專門資助 Clojure 生態開源專案的社群組織，於 2026 年 5 月 2 日由 Kathy Davis 公布 Q2 資助名單。本次共選出 5 個專案，其中 3 個為常規專案各獲 9000 美金資助，2 個為短期或實驗性專案各獲 2000 美金資助，總額 3.1 萬美金，資金來自社群成員會費。本次新增 Transduce 級成員 Metabase，專門支持 Ambrose Bonnaire-Sergeant 的 Malli 專案開發，Malli 在 Metabase 內部大量使用，也獲得許多其他社群成員採用。

🧪 **5 個獲資助專案涵蓋資料驗證、LLM、科學運算**
本次獲資助的專案與負責人資訊如下：
【9000 美金檔】
1. Ambrose Bonnaire-Sergeant：Malli 資料驗證庫
2. Dragan Djuric：Uncomplicate AI: Clojure LLM（Clojure 生態大型語言模型工具）
3. Cvetomir Dimov：SciCloj Documentation and Plotting Libraries（科學運算文件與繪圖庫）
【2000 美金檔】
1. Ingy döt Net：Gloat
2. Shantanu Kumar：PluMCP

🔍 **Malli 過往改進遞迴驗證，仍存在記憶體占用問題**
Ambrose Bonnaire-Sergeant 公開了 Malli 專案的後續規劃背景：過往在 Clojurists Together 的資助下，他改進了 Malli 遞迴引用驗證的效能，透過主動展開遞迴 schema 直到發現遞迴點，取代原本惰性實作、快取無限制遞迴層級的邏輯，避免驗證大深度輸入時發生記憶體洩漏，提升長期運作系統的可靠性。但此改動的缺點是會占用更多記憶體（公告原文此處截斷，未披露後續完整開發計畫）。

💡 **僅屬行政公告，無可落地技術細節**
本則消息為純資金分配通知，未包含任何專案的技術架構、實作細節或開源成果釋出。其中提及的 Clojure LLM 工具、Malli 驗證庫雖在對應領域有一定能見度，但公告本身無可延伸的技術分析內容，也不涉及新的 AI 架構或工程方法創新。

⚠️ **對 GenAI 工程師參考價值低**
根據現有資訊，本則公告無新技術或架構創新，對專注生成式 AI 架構與工程實踐的讀者來說，話題相關性較低，難以延伸出有吸引力的技術分析內容。若你並非 Clojure 
