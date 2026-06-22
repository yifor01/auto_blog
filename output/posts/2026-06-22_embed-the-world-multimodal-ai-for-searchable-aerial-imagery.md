---
title: 'Embed the world: Multimodal AI for searchable aerial imagery at scale'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/embed-the-world-multimodal-ai-for-searchable-aerial-imagery-at-scale/
score: 91
model: google/gemma-4-31b-it:free
generated_at: '2026-06-22T21:05:08.653567'
---

📌 【AWS 技術分享】用多模態 AI 將航空影像轉化為可搜尋的知識庫

TL;DR：結合多模態嵌入與向量搜尋，讓大規模航空影像可透過自然語言直接檢索，取代繁瑣的手動檢查。

當你需要從數十億畫素的航空影像中找出某個郊區的所有游泳池、開發區的道路網路或城市的太陽能板數量時，傳統做法只有兩種：要麼由人工一張張切片檢查，要麼為每個新問題訓練一個專屬的電腦視覺模型。這種效率低下的過程，正是地理空間資料應用者面臨的共同痛點。

🤔 **從「逐片檢查」到「自然語言查詢」**

對於保險、房地產、政府、基礎建設與農業等依賴地理空間資料的產業來說，將海量影像轉化為可搜尋的知識庫至關重要。AWS 與航空影像提供商 Vexcel 合作，針對其涵蓋 45 個以上國家與地區的高解析度資料（包含正射影像、多角度斜拍影像及高程模型），探索如何透過「一次索引，多次查詢」的機制，讓使用者能用自然語言直接獲取答案。

🧩 **基於 Amazon Bedrock 與 OpenSearch 的系統架構**

為了實現大規模的地理空間語義搜尋，該方案採取了以下技術路徑：
1. **多模態嵌入 (Multimodal Embeddings)**：將影像與文字對映到相同的向量空間。
2. **LLM 標記 (LLM Captioning)**：利用大語言模型為影像生成描述。
3. **向量搜尋 (Vector Search)**：利用 Amazon OpenSearch Serverless 進行高效的相似度檢索。

作者在文中詳細討論了針對多視角航空影像的嵌入模型選擇、融合策略、標記整合以及搜尋方法的評估。

📊 **實驗結果：Amazon Nova 表現最優**

為了驗證設計選擇對語義搜尋的影響，團隊基於 OpenStreetMap 的地面真值 (Ground Truth) 建立了評估方法，並進行了四組實驗。實驗結果顯示，Amazon Nova Multimodal Embeddings 在兩組基準查詢中均交付了最高的 F1 分數。

這套技術實作最終演進為 Vexcel Intelligence 產品，將原本需要人工逐片檢查的繁瑣流程，轉化為高效的自動化搜尋體驗。

🎯 **實務啟示**

對於需要處理大規模影像檢索的工程師，此案例證明瞭「多模態嵌入 + 向量資料庫」的組合能有效降低對專屬 CV 模型的依賴。在建構類似系統時，選擇正確的嵌入模型（如 Nova）以及設計合理的融合策略，是提升檢索精準度（F1 分數）的關鍵。

🔗 **來源**
- 標題：Embed the world: Multimodal AI for searchable aerial imagery at scale
- 作者／機構：Gilbert V Lepadatu @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/embed-the-world-multimodal-ai-for-searchable-aerial-imagery-at-scale/

#MultimodalAI #GeospatialData #VectorSearch #AmazonBedrock #AmazonOpenSearch #AerialImagery #AmazonNova #SemanticSearch #AWS #MachineLearning
