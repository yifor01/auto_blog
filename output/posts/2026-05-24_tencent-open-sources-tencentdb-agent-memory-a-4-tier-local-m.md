---
title: "Tencent Open-Sources TencentDB Agent Memory: A 4-Tier Local Memory Pipeline for AI Agents"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/23/tencent-open-sources-tencentdb-agent-memory-a-4-tier-local-memory-pipeline-for-ai-agents/
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-05-24T19:31:06.173489
---

📌 【Tencent 開源】TencentDB Agent Memory：四層本地記憶管線解決 AI Agent 長上下文問題  

長期運行的 AI Agent 常被「上下文脹大」與「記憶召回失效」困擾——把所有對話、工具日誌直接丟進平面向量資料庫，搜尋時只能依賴盲目的相似度匹配，缺乏宏觀結構的指引。  

🤔 **記憶碎片化導致召回效率下降**  
當 Agent 需要處理多輪對話、長工具鏈或複雜任務時，傳統記憶堆疊會把資料切碎後平鋪在向量庫中。此種做法雖簡單，但無法保留層次資訊，導致在需要細節時必須掃描大量無關片段，實際召回品質受限。  

🧪 **四層象徵式＋分層記憶架構**  
TencentDB Agent Memory 以兩個支柱設計：記憶層次化與象徵式記憶。長期個人化採用四層金字塔結構，從下至上依序為：  

- **L0 Conversation**：原始對話紀錄  
- **L1 Atom**：抽取出的事實單元  
- **L2 Scenario**：場景塊，將多個 Atom 編織成可重用的情境  
- **L3 Persona**：使用者的日常偏好與個人檔案，優先被查詢  

上層保存結構與概覽，下層保留完整證據。當 Agent 僅需要高層概況時，直接從 L3 或 L2 讀取；若需細節，則向下鑽取至 L1 或甚至原始 L0 對話。  

💡 **符號記憶與內容外送**  
為減少上下文視窗的 token 消耗，系統將完整工具日誌外送至 `refs/*.md` 檔案，狀態轉換則以 Mermaid 語法編碼在輕量任務畫布中。Agent 在其視窗內僅推論符號圖（node_id），真正需要原文時，透過 node_id 進行本機 grep 檢索。  

🔗 **存儲與後端**  
預設後端為本地 SQLite，搭配 `sqlite-vec` 擴充實現向量搜尋，無需外部 API。事實、日誌與追蹤資料保存在資料庫以支援全文檢索；Personas、場景與畫布則以可讀的 Markdown 檔案儲存於 `~/.openclaw/memory-tdai/` 目錄下。  

🔌 **插件與適配器**  
該專案以 MIT 授權開源，可作為 OpenClaw 的外掛，亦透過 Gateway 適配器與 Hermes Agent 整合。工程師可直接拉取原始碼，在本地環境中啟用四層記憶管線。  

⚠️ **目前已知限制**  
- 為早期開源版本，尚未公開大規模基準測試結果。  
- 預設依賴 SQLite + sqlite-vec，效能在極高寫入吞吐場景尚待社群驗證。  
- 記憶層的劃分策略（何時將資料提升至較高層）目前依賴預設規則，未來可透過微調適應不同使用場景。  

🎯 **對工程師的實務啟示**  
若你正在構建需要長時間記憶與精準召回的 AI Agent（如個人助理、任務自動化或多輪對話系統），TencentDB Agent Memory 提供了一種無需外部服務、可即插即用的記憶層次方案。透過象徵式節點與外送日誌，可在保持低 token 佔用的同時，仍能於需要時快速定位至原始證據。  

🔗 **論文／專案連結**  
📝 TencentDB Agent Memory：A 4‑Tier Local Memory Pipeline for AI Agents  
👤 Michal Sutter（Tencent）  
🔗 https://www.marktechpost.com/2026/05/23/tencent-opensources-tencentdb-agent-memory-a-4-tier-local-memory-pipeline-for-ai-agents/  
💾 原始碼（MIT 授權）：https://github.com/Tencent/TencentDB-Agent-Memory  

你有在專案中嘗試過分層記憶或符號快取嗎？歡迎在留言區分享經驗與改進想法 👇  

#AI #AgentMemory #Tencent #OpenSource #SQLiteVec #OpenClaw #Hermes #LLM #機器學習 #軟體工程
