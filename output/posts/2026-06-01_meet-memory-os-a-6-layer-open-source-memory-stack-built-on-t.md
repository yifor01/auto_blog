---
title: "Meet Memory OS: A 6-Layer Open-Source Memory Stack Built on Top of Hermes Agent"
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/01/meet-memory-os-a-6-layer-open-source-memory-stack-built-on-top-of-hermes-agent/
score: 89
model: tencent/hy3-preview:free
generated_at: 2026-06-01T22:26:36.348922
---

📌 **Meet Memory OS：一個基於 Hermes Agent 的六層開源記憶堆疊**  

你以為 Hermes Agent 的記憶已經夠好了？一個新專案主張，它只是記憶系統的冰山一角。  

🤔 **記憶淺層限制了代理的長期任務表現**  
Hermes Agent 本身提供跨會話的工作區檔案與會話資料庫，但社群開發者 ClaudioDrews 認為這種內建記憶過於簡單，無法支撐需要長期知識累積與結構化檢索的複雜任務。  

🧪 **六層記憶堆疊架構與本地 Docker 部署**  
Memory OS 不是 Hermes 的外掛開關，而是一個位於 Hermes 記憶之上的分層系統。它保留 Hermes 原有的工作區檔案與會話資料庫（第 1‑2 層），然後向上疊加四層：結構化事實庫、向量資料庫（Qdrant）、自動維護的知識維基（Fabric）以及快取層（Redis)。整個堆疊可透過 Docker 在本機啟動，需 Python 3.11+，並支援 Hermes 所支援的任意 LLM 提供者，包括 OpenRouter、OpenAI、Anthropic 與 Ollama。  

🔑 **核心發現：向量資料庫、結構化事實與自動維護的知識維基**  
在每次 LLM 呼叫之前（pre_llm_call），Memory OS 會執行它所稱的「手術式回憶」（surgical recall），同時從四個來源讀取：Fabric、Qdrant、會話資料庫與事實庫。每個來源都會經過相關性閾值過濾，若低於門檻則不會傳遞給模型。會話內部會進行去重複，避免相同內容重複出現；社群過濾器會跳過類似「thanks」這樣的無意義訊息。  

在呼叫結束（post_llm_call）或會話結束（on_session_end）時，系統會自動抽取並儲存新學習的事實，以維持知識庫的更新。  

💡 **手術式回憶與四級備援檢索保證在向量庫失效時仍能運作**  
第五層的檢索採用四級後備機制：先嘗試混合搜尋，若失敗或無結果則依序使用密集向量、字面匹配以及 SQLite 查詢。這種設計使得即使向量資料庫暫時不可用，記憶仍能透過其他方式被存取。此外，Memory OS 還會執行每週一次的衰弱掃描（weekly decay scanner），將過時的條目逐步淘汰。  

⚠️ **尚未見大規模社群採用，效能基準僅限於作者自測**  
該專案剛釋出，尚未在廣泛的開發者社群中獲得顯著星號或使用回報。現有說明多基於作者的自行測試與 README 描述，缺乏獨立的基準測試或長期穩定性數據。  

🎯 **開發者可直接透過 MIT 授權庫在本機擴充 Hermes 的記憶能力**  
如果你正在使用 Hermes Agent 並需要超越簡單會話記憶的功能（例如長期知識庫、結構化事實查詢或自動維護的維基），Memory OS 提供了一個可直接啟動的 Docker‑based 解決方案。其 MIT 授權允許自由修改與整合，適合希望在本地環境中實驗多層記憶架構的團隊。  

🔗 **專案連結**  
📝 Meet Memory OS: A 6-Layer Open-Source Memory Stack Built on Top of Hermes Agent  
👤 作者：Michal Sutter（MarkTechPost 報導）  
🔗 文章：https://www.marktechpost.com/2026/06/01/meet-memory-os-a-6-layer-open-source-memory-stack-built-on-top-of-hermes-agent/  
🐙 程式碼（MIT 授權）：https://github.com/ClaudioDrews/memory-os  

你有試過將多層記憶堆疊應用於代理開發嗎？歡迎在留言區分享你的經驗與想法 👇  

#AI #HermesAgent #MemoryOS #LLM #OpenSource #VectorDB #Docker #NousResearch #TechBlog
