---
title: "Gemini API File Search is now multimodal"
source: Hacker News
url: https://blog.google/innovation-and-ai/technology/developers-tools/expanded-gemini-api-file-search-multimodal-rag/
score: 100
model: tencent/hy3-preview:free
generated_at: 2026-05-10T19:23:49.012419
---

📌 【Google DeepMind】Gemini API File Search 現在支援多模態搜尋  

🎣 你曾經為了在海量圖片與文件中找出特定視覺資產而費力？現在 Gemini API 能直接「看圖」並給出精準位置。  

🤔 **多模態檔案搜尋讓 RAG 不再只看文字**  
Gemini API 的 File Search 已經支援純文字檢索，現在新增圖像與文字的聯合處理，使開發者能在同一個索引中同時搜尋圖片與文字內容。  

🧪 **由 Gemini Embedding 2 模型驅動的原生圖像理解**  
這項多模態能力來自 Gemini Embedding 2 模型，該模型能直接編碼圖像特徵，無需額外的 OCR 或外掛模型，從而在檢索階段就具備圖像語意理解。  

📊 **自訂中資料與頁層引用提升可驗證性**  
除了多模態，更新還加入了自訂中資料（custom metadata）功能，讓開發者可以附加自己的欄位（如作者、日期、標籤）進行過濾；並提供頁層引用（page‑level citations），使生成的答案能直接指向具體的頁碼或圖片位置，提升答案的可追溯與可信度。  

💡 **適合原型與生產環境的易用 API**  
Google 強調該工具無論是週末專案還是服務數千用戶的生產系統，都能以簡單的 API 呼叫完成多模態檢索與中資料過濾，降低建構驗證型 RAG 系統的門檻。  

⚠️ **僅針對 Gemini API File Search 提供，其他模型需自行適配**  
目前的多模態支援僅限於 Gemini API 的 File Search 工具；若使用其他嵌入模型或自建向量資料庫，需自行實作圖像編碼與中資料索引。  

🎯 **開發者可先利用多模態搜尋建構可驗證的知識庫**  
建議在設計 RAG 時，先把文字與圖片一起送入 Gemini Embedding 2 生成向量，利用自訂中資料過濾無關內容，並依賴頁層引用讓 LLM 的回答可直接追溯至原始檔案的具體位置，提升系統的準確度與可信度。  

🔗 **論文連結**  
📝 Gemini API File Search is now multimodal  
👤 gmays (Hacker News) – 原文來自 Google 部落格  
🔗 連結：https://blog.google/innovation-and-ai/technology/developers-tools/expanded-gemini-api-file-search-multimodal-rag/  

你有試過在圖書館裡用文字搜尋找圖片嗎？多模態檢索可能改變你的做法，歡迎在留言區分享你的使用經驗 👇  

#Gemini #GoogleDeepMind #多模態 #RAG #AI開發 #FileSearch
