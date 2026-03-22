---
title: "What's New in Mellea 0.4.0 + Granite Libraries Release"
source: HuggingFace Blog
url: https://huggingface.co/blog/ibm-granite/granite-libraries
score: 33
model: gpt-4o-free
generated_at: 2026-03-22T18:49:22.654114
---

📌 **Mellea 0.4.0 + Granite Libraries 發布**  🤔 **AI 工作流難以維護與除錯**  
當開發者使用大型語言模型時，常面臨輸出難以預測、除錯成本高以及缺乏結構化驗證的問題。這些挑戰限制了 LLM 在生產環境中的可靠性與維護性。  🧪 **以受限解碼與修復迴圈為核心的新架構**  
Mellea 0.4.0 是一個開源 Python 庫，設計用來取代傳統的概率式提示行為。它透過以下機制讓 LLM 程式變得更可維護與可預測：  - **受限解碼（constrained decoding）** 確保產出符合預先定義的結構或 schema。  
- **結構化修復迴圈（structured repair loops）** 透過取樣拒絕（rejection sampling）實作 instruct‑validate‑reward 模式，自動偵測並修正不符合規範的輸出。  
- **可組合的管線（composable pipelines）** 讓不同的工作流步驟可以像函式一樣被串聯與重複使用。  

🆕 **Mellea 0.4.0 原生支援三種 Granite 庫，提供結構化、可驗證的工作流**  
此次發布隨附三個專用模型適配器：  
- **granitelib-rag-r1.0** – 優化查詢改寫與檢索增強生成。  
- **granitelib-core-r1.0** – 提供核心語言理解與生成功能。  
- **granitelib-guardian-r1.0** – 負責幻覺偵測與政策合規檢查。  

透過這些適配器，Mellea 能在不依賴通用提示的情況下，對輸入鏈或對話的特定片段進行精準操作，並使用受限解碼保證輸出符合期望的格式。  

💡 **透過專用模型適配器實現查詢改寫、幻覺偵測與政策合規檢查**  
每個 Granite Library 都是經過微調的模型，專門針對單一任務進行優化：  
- 查詢改寫適配器可將使用者的原始問題轉換為更適合檢索的形式。  
- 幻覺偵測適配器會檢查生成內容是否與事實相符，降低虛構資訊的風險。  
- 政策合規檢查適配器則能即時判斷輸出是否違反預先設定的使用規範。  

這種「專任模型 + 受限解碼」的組合，讓開發者可以在程式層面明確定義每一步的預期行為，除錯時也能追溯到具體的適配器或管線階段。  

⚠️ **目前僅支援 IBM Granite 模型，生態系統尚在早期階段**  
- 現階段的適配器與 API 專為 IBM Granite 模型系列設計，其他模型尚未提供官方支援。  
- 由於庫才剛發布，社區範例與第三方擴充仍在積累中，實務上可能需要自行適配某些邊界情況。  

🎯 **開發者可透過標準化 API 建構可觀測、可維護的 LLM 應用**  
- 透過 Mellea 的觀測鉤子（observability hooks），開發者可以在工作流的每個事件點插入回調函式，以監控執行時間、錯誤率或schema 違反情況。  
- 結合 Granite Libraries 的專任適配器，團隊可以將複雜的 LLM 任務拆解為可測試、可版本控制的微服務，提升整體系統的可靠度與開發效率。  

🔗 **原始發布連結**  
🌐 https://huggingface.co/blog/ibm-granite/granite-libraries  

你是否已經在專案中嘗試過結構化 LLM 工作流？歡迎在留言區分享你的經驗或問題 👇  #IBM #Granite #Mellea #LLM #AI工程 #開源 #機器學習 #HuggingFace
