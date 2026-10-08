---
title: 'Perplexity AI Releases pplx-embed-v2-late: A 0.6B Edge Model and a 9B Model
  Scoring 92.4% on MADQA'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/07/perplexity-ai-releases-pplx-embed-v2-late-a-0-6b-edge-model-and-a-9b-model-scoring-92-4-on-madqa/
model: claude-code/sonnet
generated_at: '2026-10-08T22:21:21.251410'
score: 92
---

📌 128 維逐 token 嵌入：Perplexity 開源多模態檢索模型

TL;DR：Perplexity 開源 ColBERT 式多模態嵌入模型，9B 版本 MADQA 拿下 92.4%。

多數嵌入模型把一整份文件壓成一個向量，查詢時難免丟掉細節。Perplexity 這次反過來，為每個 token 都保留一個向量，而且文字、圖片、PDF 頁面全部共用同一個嵌入空間。

🤔 **一個模型吃下文字、圖片與 PDF**

Perplexity 釋出 pplx-embed-v2-late，是一對 ColBERT 風格的多模態嵌入模型，提供兩種尺寸：0.6B 版本主打快速、低成本查詢，9B 版本主打最高品質。兩者都能檢索文字、圖片以及渲染後的 PDF 頁面，並共用同一個嵌入空間，意味著可以用小模型查詢、大模型建立的索引，或反過來混搭使用。

🧩 **用 MaxSim 取代單一向量壓縮**

一般 dense 嵌入模型會把整份文件壓縮成 1 個向量，pplx-embed-v2-late 則是為每個 token 保留一個 128 維向量，比對時用 MaxSim 計分：每個查詢 token 找出文件中最相似的那個 token，再把所有最大值加總。頁面是以圖片形式編碼，因此不需要額外的 OCR 步驟。兩個模型都是從一個 18B 的教師模型蒸餾而來，採用 LEAF 風格的 token 層級訓練，正是這套訓練方式讓文字與影像共用同一個嵌入空間成為可能。

📊 **9B 模型在 MADQA 拿下 92.4%**

依照 Perplexity 官方公告的數據：
- 最強成績：9B 模型在 MADQA 拿下 92.4%。
- 最大領先幅度：在 BrowseComp+ 上領先最佳 dense 模型 8.7 個百分點。
- 最弱成績：0.6B 模型在 ViDoRe v3 Markdown 上為 61.2%，但在該項目中仍是第二好的分數。
- 影像檢索是明顯弱項：Gemini Embedding 2 在 MIRACL-Vision 上勝過 9B 模型，在 PPLX-Q2I 上也領先 2 個百分點。
- 混搭尺寸反而更有效率：用 9B 建索引、0.6B 查詢，在 ViDoRe v3 影像檢索上拿到 63.5%，比起 0.6B 建索引、0.6B 查詢的 62.3% 還高，但查詢成本維持在小模型等級。

💡 **部署門檻與環境需求**

兩個模型都已上架 Hugging Face，採 MIT 授權，代表可以自行下載部署；官方雖有計畫推出託管 API 端點，但目前尚未上線。模型卡顯示兩者都需要 CUDA GPU，並依賴 sentence-transformers 6.0.0 以上版本與 transformers 5.4.0 以上版本。公開的 checkpoint 以 F32 格式儲存，下載體積會是半精度的兩倍；若只看權重本身，以每參數 2 bytes 估算記憶體用量（此為估算值，非官方數字），0.6B 版本適合邊緣裝置或低延遲查詢場景。

⚠️ **影像檢索仍有落差**

雖然在文字問答與跨模態檢索的多項測試中表現亮眼，pplx-embed-v2-late 在純影像檢索（MIRACL-Vision、PPLX-Q2I）上仍落後 Gemini Embedding 2，說明這套方案的強項目前集中在文字為主、圖文混合檢索的場景，而非純視覺比對。

🎯 **實務啟示**

對於需要同時檢索文字、圖片與 PDF 的 RAG 系統，pplx-embed-v2-late 提供了一個可自行部署、MIT 授權的選項，而且 9B 大索引配 0.6B 小模型查詢的混搭模式值得注意，能在不犧牲太多準確率的前提下壓低查詢端的運算成本。若場景以純影像比對為主，仍建議評估 Gemini Embedding 2 等競品。

🔗 **來源**
- 標題：Perplexity AI Releases pplx-embed-v2-late: A 0.6B Edge Model and a 9B Model Scoring 92.4% on MADQA
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/10/07/perplexity-ai-releases-pplx-embed-v2-late-a-0-6b-edge-model-and-a-9b-model-scoring-92-4-on-madqa/

#Perplexity #EmbeddingModel #MultimodalAI #ColBERT #RAG #OpenSource #HuggingFace #InformationRetrieval #VectorSearch #EdgeAI
