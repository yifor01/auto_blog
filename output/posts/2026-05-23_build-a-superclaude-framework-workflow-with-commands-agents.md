---
title: "Build a SuperClaude Framework Workflow with Commands, Agents, Modes, and Session Memory"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/23/build-a-superclaude-framework-workflow-with-commands-agents-modes-and-session-memory/
score: 63
model: tencent/hy3-preview:free
generated_at: 2026-05-23T19:53:02.456287
---

📌 **Build a SuperClaude Framework Workflow – A Step‑by‑Step Tutorial for Structured Claude Prompting**

你有試過讓 Claude 依照特定角色或任務模式自動切換提示詞嗎？這篇 MarkTechPost 教學示範如何把現有的 SuperClaude Framework 包裹成一個 Python 橋接層，讓每次模型呼叫前都能動態載入對應的 Markdown 行為檔案，從而在腦力激盪、前端實作、安全審查、商業策略等不同場景中保持提示詞的一致性與角色意識。

🤔 **從零開始構建可重複使用的 Claude 工作流程**

當開發者想讓 AI 在不同任務間保持固定的行為指引時，常需要手動複製貼上長段系統提示詞，這不僅易出錯，也難以管理。SuperClaude Framework 透過將命令（Commands）、代理人（Agents）與模式（Modes）以 Markdown 檔案的形式組織起來，提供了一種結構化的方式來描述期望的 AI 行為。本教學的目標是展示如何用 Python 將這些資產連結到 Anthropic API，使其在實際開發流程中可重複使用、易於維護。

🧪 **教學實作步驟概覽**

1. **環境準備** – 安裝所需的 Python 套件（包括 `rich` 用於美化 Colab 輸出），設定 Anthropic API 金鑰並選擇使用的 Claude 模型。  
2. **取得框架** – 使用 `git clone` 取得 SuperClaude Framework 儲存庫，確保本地端擁有所有 Markdown‑based 的 commands、agents 與 modes。  
3. **資產掃描與分類** – 遍歷儲存庫，將發現的命令、代理人與模式分別放入不同的「儲存桶」（bucket），以便在運行時依需求動態載入。  
4. **定義 SuperClaude 類別** – 建立一個 Python 類別，負責：  
   - 讀取基礎系統指令（base instruction）  
   - 根據使用者選擇的命令、代理人與模式，載入對應的 Markdown 內容  
   - 將這些內容組合成最終的系統提示詞  
   - 提供 `run`、`save` 與 `load` 方法，以執行引導式工作流程並保存/載入 session 歷史。  
5. **實作範例工作流程** – 透過以下情境示範橋接層的使用方式：  
   - **腦力激盪**：使用特定命令與模式引導 Claude 產發點子。  
   - **前端實作**：選擇前端開發相關的代理人與模式，獲得結構化的程式碼建議。  
   - **安全分析**：載入安全審查的行為檔案，讓 Claude 提出潛在風險與修復建議。  
   - **商業策略**：切換至策略規劃模式，獲取市場分析與決策框架。  
   - **深度研究規劃**：啟用深度研究模式，產出可追蹤的研究步驟。  
   - **Token‑efficient 回應**：測試不同模式對輸出長度與資訊密度的影響。  
   - **鏈式多步驟開發工作流程**：結合前面的步驟，示範如何在一次 session 中完成需求分析 → 程式碼生成 → 安全檢查 → 文件撰寫，並利用 `save/load` 功能在中途暫停與繼續。  

 **核心發現：框架如何提升 Prompt 一致性與角色感**

透過將行為指令外部化為 Markdown 檔案並動態注入系統提示詞，教學展示了兩個具體優勢：  
- **一致性**：相同的命令/代理人/模式組合會產生相似的系統提示詞，減少因手動編輯導致的變異。  
- **角色感**：模型在每次呼叫前都會收到明確的角色定義（例如「前端工程師」或「安全分析師」），使其輸出更貼近預期的專業視角。  

此外，`save` 與 `load` 方法讓開發者能够在長時間的多步驟任務中保留中間思考軌跡，避免每次重新說明背景資訊。

💡 **深入分析：為何這種結構化層實用？**

SuperClaude Framework 的設計將「什麼該做」行為描述與「如何呼叫模型」的技術細節分離。這意味著：  
- **可重用性**：同一套命令/代理人/模式可在不同專案或不同團隊成員間共享，只需調用橋接類別即可。  
- **易於維護**：更新某個角色的行為指標時，只需編輯對應的 Markdown 檔案，無需改動 Python 程式碼。  
- **透明度**：所有行為規則都以純文字形式存在，團隊成員可以直接閱讀審核，降低黑箱操作的風險。  

教學同時指出，橋接層本身並未改變 Claude 的基礎模型能力，而是提供了一種更有條件的方式來引導其輸出。

⚠️ **目前可見的限制（僅基於教學說明）**

- 教學聚焦於如何將現有框架連結至 Anthropic API，未涉及框架本身的演算法創新或模型訓練改進。  
- 所有示範均基於作者提供的範例命令、代理人與模式；實際應用時，開發者仍需自行編寫或調整對應的 Markdown 行為檔案以符合特定需求。  
- 教學未進行大規模效能基準測試（例如 token 使用量或延遲的系統級比較），因此無法量化橋接層在大規模生產環境中的開銷。  

🎯 **實務啟示：如何在你的開發流程中採用此方法**

- 若你的團隊經常需要 Claude 在不同角色間切換（例如從程式編寫轉為安全審查），考慮把常用的行為指令寫成 Markdown 檔案，並使用類似教學中的 `SuperClaude` 類別作為橋接層。  
- 利用 `save/load` 功能可以在長期研究或多迭代專案中保留對話歷史，減少重複說明背景資訊的成本。  
- 先從單一情境（如腦力激盪）開始測試，確認橋接層能正確載入並產生預期的提示詞，之後再逐步擴充至更複雜的鏈式工作流程。  

🔗 **參考資源**  
📝 **文章標題**：Build a SuperClaude Framework Workflow with Commands, Agents, Modes, and Session Memory  
👤 **作者**：Sana Hassan（MarkTechPost）  
🔗 **連結**：https://www.marktechpost.com/2026/05/23/build-a-superclaude-framework-workflow-with-commands-agents-modes-and-session-memory/  

你有試過用類似的方式結構化 AI 提示詞嗎？歡迎在留言區分享你的經驗或詢問實作細節 👇  

#AI #Claude #Anthropic #PromptEngineering #SuperClaude #Python #開發工具 #MarkTechPost
