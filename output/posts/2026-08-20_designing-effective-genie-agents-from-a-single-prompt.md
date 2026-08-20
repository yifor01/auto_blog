---
title: Designing effective Genie Agents from a single prompt
source: Databricks
url: https://www.databricks.com/blog/designing-effective-genie-agents-single-prompt
model: claude-code/sonnet
generated_at: '2026-08-20T06:37:27.979351'
score: 80
---

📌 Genie Agents：一句 Prompt 生出企業專屬 AI Agent，關鍵不在提示詞

TL;DR：Databricks Genie Agents 用單一 prompt 建立領域專屬 agent，真正決定品質的是 Unity Catalog 裡治理過的資料脈絡。

問一個泛用型 agent「營收多少」，它很可能抓到的是它找到的第一張營收表，而不是財務部門真正在維護的那一張。多數人的第一反應是去改 prompt，但 Databricks 這篇文章說：問題通常根本不在提示詞。

🤔 答錯的不是 prompt，是缺的商業脈絡

弱或不一致的 agent 回答，大多數情況下的根源是缺乏商業脈絡（business context），而非 prompt 寫得不好。過去建立 Genie Agent 需要手動設定，現在可以用一句 prompt 完成。

🧩 一句 Prompt，啟動一個治理過的 Agent

透過 Genie One 或 Genie Code，只需一句 prompt，就能結合 Unity Catalog 中的脈絡與使用者對話內容，快速生出一個 agent。文章給的範例很簡單：「使用我們的 incident runbooks 與 service-health 資料，建立一個協助 support engineers 調查生產環境事故的 agent。」這句話已經足夠讓 Genie 辨識出問題領域，並指向該用哪些資料來源。

Genie Agents 能推理的脈絡分兩類：結構化資料，包括已治理的資料表、指標定義（metric definitions）、儀表板、資料品質規則與內部文件；以及非結構化資料，例如儲存在 Unity Catalog volumes 中的 PDF、Word 文件、簡報與圖片。使用者提問時，agent 會擷取最相關的檔案內容，與治理過的資料表一起推理後產生答案，並全程套用提問者本人的權限。文章舉了幾個例子：Sales Opportunity Data agent 可從治理過的 CRM 資料表中找出 pipeline 風險；Logistics Management agent 能在供應鏈資料中追蹤貨運並標示延遲；Product Line Lookup agent 能從內部產品目錄回答詳細的產品問題；Incident Investigation agent 則能直接引用真實的 runbook PDF 來調查事故。

Genie Agents 也內建 benchmark 機制：可以定義一組附帶預期答案的測試問題，跑出一個準確率分數。文章建議先拿幾個「已知根因」的歷史事故做測試，不只看 agent 是否得出正確結論，也要檢查它引用的 runbook 與 service-health 資料是否正確；如果 agent 引用了過時的 runbook 或錯誤的服務，代表需要補齊的是治理脈絡，而不是重寫 prompt。每次調整後重新跑一次 benchmark，能把「感覺變好了」轉成可追蹤的具體數字，monitor 分頁還會呈現使用者實際提出的問題與回饋，可以回頭補進 benchmark。

💡 先窄後寬：把 context engineering 變成可驗證的治理流程

文章反覆強調一個順序：先聚焦在單一、可辨識的具體任務，例如回答某個產品 FAQ、調查某一類常見的生產事故，把資料來源、測試與 benchmark 做扎實，再逐步擴充知識、工具與跨部門工作流程。這個「先窄後寬」的路徑，本質上是把 curated Unity Catalog 語義（metric views、domain、certification 等）當成 agent 品質的地基，單一 prompt 只是啟動流程的入口，並不能取代文件治理與領域知識本身。換句話說，Genie Agents 把 context engineering 的工作，從一次性的手動設定，變成可以反覆疊代、可被 benchmark 驗證的治理流程。

🎯 實務啟示

下次遇到 agent 回答不準確的狀況，與其直接鑽進 prompt 反覆調整措辭，不如先檢查它引用的資料來源是不是對的一份、是不是最新的一份。從一個範圍夠窄、有明確驗收標準的用例切入，搭配內建 benchmark 反覆驗證，會比一開始就想做出一個什麼都能答的萬用 agent 更容易落地。

🔗 來源
- 標題：Designing effective Genie Agents from a single prompt
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/designing-effective-genie-agents-single-prompt

#Databricks #GenieAgents #UnityCatalog #AIAgents #RAG #EnterpriseAI #DataGovernance #LLM #PromptEngineering #DataPlatform
