---
title: 'Cohere Releases Embed 5: How It Compares to Voyage 4 Large, Gemini Embedding
  2, and OpenAI'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/01/cohere-releases-embed-5/
model: claude-code/sonnet
generated_at: '2026-10-01T22:05:33.088324'
score: 90
---

📌 Cohere Embed 5上線：Pro/Fast共享向量空間，對比Voyage、Gemini、OpenAI

TL;DR：Cohere新一代嵌入模型分Pro/Fast雙層，可混搭索引與查詢，ViDoRe V3上Pro拿下85.8分略勝同業。

多數嵌入模型升級只推出單一版本，Cohere Embed 5卻讓你用高品質的Pro模型建索引、用便宜快速的Fast模型查詢，而且分數幾乎不打折。

🤔 背景：agentic檢索需要不同層級的嵌入

在RAG與agentic retrieval場景下，一個agent可能在單一任務裡發出數十次搜尋，查詢延遲會隨之疊加放大。企業端需要的是「建索引時追求品質、查詢時追求速度」的靈活性，而不是單一尺寸的嵌入模型。

🧩 架構：Pro與Fast共享同一個嵌入空間

Embed 5分兩個tier：Embed 5 Pro主打最高檢索品質，Embed 5 Fast主打查詢路徑的延遲與成本。兩者都接受文字、圖片，以及文字加圖片的融合輸入，涵蓋100多種語言，最長可讀128K tokens。關鍵設計是Pro與Fast共用同一個embedding space，代表可以用其中一個模型建索引、另一個模型查詢，只要兩邊輸出維度一致即可。模型可輸出2048、1536、1024、768、512或256維，預設為2048維，並支援float、int8、binary三種精度格式。

Cohere在40個開發資料集上，測試過每一種corpus與query的配對組合：以Pro加Pro為100分的基準，Pro索引搭配Fast查詢拿下98.4分，全Fast配置拿下96.6分。官方建議的模式是「用Pro建索引、用Fast查詢」。API模型ID為embed-v5.0-pro與embed-v5.0-fast，兩者都已在Cohere API、Model Vault、Microsoft Foundry、Amazon SageMaker上線，也可透過vLLM在私有VPC或on-prem環境部署。

📊 數據：跟Voyage 4 Large、Gemini Embedding 2、OpenAI的對比

在ViDoRe V3上的平均分數：

| 模型 | 分數 |
|---|---|
| Embed 5 Pro | 85.8 |
| Embed 5 Fast | 84.5 |
| Voyage 4 Large | 83.7 |
| Gemini Embedding 2 | 83.2 |
| OpenAI text-embedding-3-large | 75.5 |

Embed 5 Pro相較前代Embed 4提升8.8分。在Cohere自家的parsed-PDF測試集上，Pro以84.8分領先Voyage 4 Large的83.6分。金融領域是Embed 5最突出的場景：Pro在FinanceBench拿80.1分、FinQA拿90.0分、ViDoRe V3 Finance拿85.0分，全部排名第一，Fast則都排名第二。

多語言表現則較為分散：Pro在歐洲語言平均分以77領先，但在Cohere自己公布的結果表中，Gemini Embedding 2在日文、阿拉伯文、印地文、泰盧固文等10種語言裡有9種贏過Pro。

吞吐量方面，Fast每秒處理377.3份文件，Pro則是159.7份。定價為Pro每百萬text token 0.12美元、Fast 0.08美元，圖片輸入兩者都是每百萬token 0.40美元。透過Matryoshka representation learning加上低精度輸出，一億個chunk的原始儲存空間可以從約819 GB壓縮到3.2 GB（1024維int8設定）。Cohere建議以1024維int8作為預設選擇，稱其品質接近滿精度。

⚠️ 限制

文中多數分數採用Cohere自創的RCP-nDCG@10指標，這個指標是在固定候選集合上重新排序，衡量的其實更接近reranking品質，而非第一階段的檢索召回率。Cohere已公開評測程式碼，但素材指出獨立複現的結果尚未出現，這些數字目前仍屬廠商自報，需謹慎看待。

🎯 實務啟示

如果你的RAG pipeline已經在用Cohere嵌入模型，Pro建索引、Fast查詢這種混搭模式值得評估，尤其是agentic workload每次任務要發多次查詢的場景，延遲與成本的節省會直接疊加。但在下決定前，建議針對自己的語料跑一次基準測試，而不是只看供應商公布的RCP-nDCG@10分數。

🔗 來源
- 標題：Cohere Releases Embed 5: How It Compares to Voyage 4 Large, Gemini Embedding 2, and OpenAI
- 作者／機構：Sana Hassan，MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/01/cohere-releases-embed-5/

#Cohere #Embed5 #EmbeddingModel #RAG #VectorSearch #AgenticAI #Multimodal #SemanticSearch #LLM #MachineLearning
