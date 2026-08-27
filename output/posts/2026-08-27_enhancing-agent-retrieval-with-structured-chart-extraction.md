---
title: Enhancing Agent Retrieval with Structured Chart Extraction
source: Databricks
url: https://www.databricks.com/blog/enhancing-agent-retrieval-structured-chart-extraction
model: claude-code/sonnet
generated_at: '2026-08-27T17:28:20.763679'
score: 90
---

📌 Databricks 用結構化 JSON 讓 Agent 真正「讀懂」圖表

TL;DR：把圖表轉成結構化 JSON 索引後，Agent 在圖表問答上超越多模態嵌入模型，且索引成本更低。

問一個前沿 agent「這張圖有幾個局部最大值」，它想了 50 秒，答案是 17，錯了。同一個問題丟給接上結構化圖表擷取的 Databricks Genie，答對了：18。

🤔 **文字檢索抓不到圖表裡的數字**

Databricks 觀察到,越來越多企業要求 agent 處理內部文件並回答其中內容,但關鍵資訊往往藏在圖表裡。許多客戶反映 agent 難以正確讀取並計數圖表中的數值,這個問題在 Databricks 自家的 OfficeQA Pro 基準測試中也有印證：模型在圖表相關與多模態問題上的表現,明顯不如不需要理解圖表的問題。

傳統的文字檢索系統只能在文字空間搜尋，常見做法是為圖表生成一段文字描述（caption），但這種做法可能漏掉回答細粒度數字問題所需的資料，導致系統檢索到錯誤的頁面，或檢索到正確頁面卻沒有足夠資訊來回答問題。

🧩 **管線設計：ai_parse_document 把圖表轉成 JSON,再交給輕量嵌入模型索引**

Databricks 用自家的 AI functions 建構了一條端到端的圖表感知檢索管線：先用 ai_parse_document 擷取文件內容，圖表以結構化 JSON 呈現；再用 ai_prep_search 把內容轉換成可檢索的區塊，用一個輕量的 3 億參數文字嵌入模型（BGE）建立索引；最後用 ai_search 建立索引並連接到 Genie 進行檢索與回答。實驗比較了兩種索引，兩者來自相同的來源 PDF，差異只在圖表的表示方式。

📊 **兩個資料集，結構化 JSON 都同時提升檢索與回答品質**

團隊在 ViDoRe V3 基準測試中挑出 310 個圖表與資訊圖表密集的問題進行評估，涵蓋就業、能源、製藥、物理、金融、電腦科學、工業文件七個領域，對整個 1.6 萬頁的英文語料庫進行解析、切塊並生成所有查詢的答案。由於部分圖表相關問題仍可透過周邊文字回答，團隊另外建立了一個純圖表問答的合成資料集 Chart-RAG：從 BIS 季度報告、IMF 世界經濟展望、摩根大通長期資本市場假設這三份圖表密集報告（共 378 頁）中撰寫了 114 個視覺基礎（visually grounded）問題。

評分方式是用 LLM 裁判（gemini-3-flash）依照黃金答案，將每個回答評為正確、部分正確或錯誤；檢索指標則採用 Hit Rate@10 與 nDCG@10。結果顯示，結構化圖表 JSON 在兩個資料集上都同時提升了回答品質與檢索表現。團隊也測試在回答時額外提供檢索到的前三個文字區塊所對應的圖片：在檢索結果不變的情況下,圖片讓 Chart-RAG 的回答正確率提升 4 個百分點,ViDoRe V3 子集提升 2.6 個百分點。

💡 **輕量方案打贏大型多模態嵌入模型**

Databricks 將自家方案與四種多模態嵌入模型比較：採用多向量後期互動評分的 ColQwen2.5-3B、單向量的 Qwen3-VL-Embedding-2B，以及更輕量的 Jina CLIP v2（9 億參數）和 CLIP ViT-L/14（4.28 億參數）。這些模型為每一頁生成嵌入，查詢時用 MaxSim（ColQwen2.5-3B）或餘弦相似度（單向量模型）排序，並將最高分的五頁交給回答用的視覺語言模型。

結果顯示，搭配前三張圖片的圖表 JSON 方案在 ViDoRe V3 上達到 75.9% 的正確率，在 Chart-RAG 上達到 75.1%，兩者都超過了四個多模態嵌入基準模型，卻只需要傳入三張圖片。這個結果來自比 ColQwen2.5-3B 的多向量後期互動架構簡單約十倍的方案。

⚠️ **仍待探索的部分**

Databricks 表示，未來還可以進一步探索不同的結構化擷取表示格式，對檢索與回答準確度的影響。目前 ai_parse_document 的圖表 JSON 強化功能即將推出，屆時任何解析過的文件都會自動包含結構化的圖表數值,不需要更動函式介面。

🎯 **實務啟示**

如果你的 RAG 系統要處理財務報告、季度回顧一類的圖表密集文件，光靠圖表 caption 很可能不足以支撐細粒度數字問答；把圖表擷取為結構化資料再索引，可能比直接上大型多模態嵌入模型更划算。

🔗 **來源**
- 標題：Enhancing Agent Retrieval with Structured Chart Extraction
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/enhancing-agent-retrieval-structured-chart-extraction

#RAG #Databricks #ChartExtraction #AIAgents #EnterpriseAI #DocumentAI #MultimodalAI #InformationRetrieval #LLM #Genie
