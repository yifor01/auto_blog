---
title: "mksglu/context-mode"
source: GitHub Trending
url: https://github.com/mksglu/context-mode
score: 113
model: tencent/hy3-preview:free
generated_at: 2026-06-02T21:31:44.682963
---

📌 **【mksglu/context-mode】讓 LLM Agent 不再被工具回傳的原始數據淹沒**

你有沒有發現，才用了幾十分鐘，LLM Agent 的對話視窗就被 Playwright 快照、GitHub issue、access log 等工具回傳的原始數據塞滿？隨著對話壓縮，關鍵的檔案編輯狀態、進行中的任務甚至你最後的請求都可能被遺失，而 Agent 仍在浪費 token 對客套話和冗長解釋進行輸出。

🧪 **沙盒工具 + 持久化 SQLite/FTS5 日誌 + 思考即編碼**

Context Mode 是一個 MCP 伺服器，它從四個方向同時攻擊上下文浪費問題：  
- **Context Saving** – 工具執行被放入沙盒，原始二進位資料不再佔用 LLM 的 context window；實測顯示 315 KB 的原始數據僅佔 5.4 KB（約 98% 減少）。  
- **Session Continuity** – 每一次檔案編輯、git 操作、任務狀態、錯誤與使用者決策都被記錄到 SQLite 中，並建立 FTS5 全文索引。對話壓縮時，僅透過 BM25 檢索取回與當前任務相關的事件，避免「忘記正在編輯的檔案」或「上次的請求」。若不使用 `--continue`，上一階段的資料會被立即刪除，保證每次會話從乾淨狀態開始。  
- **Think‑in‑Code** – 讓 LLM 透過編寫腳本來完成分析，而不是直接將大量檔案讀入 context。例如，計算函式數量不需要把 50 個檔案塞進視窗，只要寫一段腳本執行並 `console.log()` 結果，一腳本可取代十次工具調用，節省約 100 倍的 context。

📈 **原始數據佔比劇降，任務連續性顯著提升**

根據專案頁面的實測數據：  
- 在未使用 Context Mode 的情況下，30 分鐘後約有 40% 的 context window 已被工具回傳的原始數據佔用。  
- 啟用 Context Mode 後，同樣的工作負荷僅需 5.4 KB，意味著可用空間從原本的 60% 提升至近乎 98%。  
- 因為所有會話事件皆被索儲，Agent 壓縮對話後仍能精準定位到「上次編輯的檔案」、「尚未完成的任務」以及「使用者最後的請求」，避免重複說明或重新查找資訊。

💡 **上下文管理的根本轉移：從「讀取」到「計算」**

傳統做法是把工具產出的原始資料直接丟進 LLM，導致 token 被低價值的填充內容消耗。Context Mode 透過三個機制改變這個流程：  
1. **隔離**：原始二進位資料永不進入 context window，僅保留元資料或索引。  
2. **持續性**：透過 SQLite/FTS5 保存會話狀態，使得即使經過多次壓縮，仍能基於關鍵詞快速定位相關事件。  
3. **計算導向**：鼓勵 Agent 以腳本形式執行分析，只把最終結果帶回對話，從根本上降低每輪對話所需的 token 數。

⚠️ **專案尚處早期階段，長期效果與邊界案例待驗證**

- 目前的數據基於專案頁面提供的基準測試，尚未見大規模、長時間的生產環境基準。  
- 實作依賴 MCP 伺服器與特定工具的沙盒配置，對於尚未支援 MCP 的工具可能需要額外適配。  
- 雖然設計上保證「不續續則清除」，但實際使用中是否會因誤觸 `--continue` 而導致資料洩漏，仍需社群進一步測試與最佳實踐的分享。

🎯 **工程師可立即評估的切入點**

- 若你正在構建長時間運行的 LLM Agent（如程式輔助、自動化測試或資料探索），可先在本地部署 mksglu/context-mode 作為 MCP 伺服器，觀察 token 使用量的下降。  
- 將工具呼叫封裝在沙盒中，讓 Agent 專注於產出腳本或簡潔的回覆，而非處理大量二進位快照。  
- 利用內建的 SQLite/FTS5 會話索引，實作「斷點續傳」功能，讓 Agent 在對話被壓縮後仍能無縫繼續先前的工作流程。  
- 關注專案的 Issue 與 Pull Request，社群正在積討論如何擴充支援更多工具類型以及如何在不同 LLM 框架中無縫掛載。

🔗 **專案連結**  
📂 mksglu/context-mode  
🔗 https://github.com/mksglu/context-mode  

你的 Agent 是否也在為上下文窗口的「雙向流失」而苦惱？歡迎在留言區分享你的體驗或改進想法 👇

#AI #LLM #Agent #MCP #ContextManagement #GitHubTrending #開源工具 #mksglu #contextmode
