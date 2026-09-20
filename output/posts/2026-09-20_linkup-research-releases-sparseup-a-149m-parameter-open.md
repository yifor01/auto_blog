---
title: 'Linkup Research Releases SPARSEUP: A 149M-Parameter Open-Source Sparse Embedding
  Model'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/19/linkup-research-releases-sparseup/
model: claude-code/sonnet
generated_at: '2026-09-20T19:32:12.422789'
score: 91
---

📌 149M參數稀疏嵌入模型SPARSEUP，補上開源檢索三缺一

TL;DR：Linkup 發布149M參數的開源稀疏嵌入模型SPARSEUP，BEIR-13平均nDCG@10達56.4，權重與訓練細節全公開。

多數開源檢索模型都是稠密向量：一段文字對應一個向量。Linkup 這次補的，是業界最近一次開源浪潮裡缺的那一塊。

🤔 **LightOn留下的空缺：稀疏編碼器**

觸發這次發布的是 LightOn 稍早的 DenseOn 與 LateOn 專案，該專案公開了訓練資料、訓練流程、一個稠密模型與一個 late-interaction 模型。Linkup research 團隊發布的 SPARSEUP，補上了其中缺少的稀疏（sparse）編碼器，並沿用同一個骨幹模型家族與微調資料，讓三種檢索風格可以直接放在一起比較。稀疏模型輸出的是對整個詞彙表的權重分布，而非單一向量：每個維度對應一個真實的 token，因此向量能直接放進 inverted index，人類也能直接讀懂內容，且通常對罕見詞的匹配效果較好。

🧩 **從LateOn-unsupervised出發，接回MLM head**

SPARSEUP 建立在一個149M參數的 ModernBERT 骨幹之上，以 Apache 2.0 授權開源，可透過 Transformers 或 Sentence Transformers 載入，並需要開啟 trust_remote_code=True。訓練起點是 LateOn-unsupervised 檢查點，但該檢查點原本沒有 MLM head，Linkup 團隊把 ModernBERT 原生的 MLM head 重新接回去。微調階段使用 LightOn 的微調資料組合，僅採用對比學習（contrastive learning），沒有經過 cross-encoder 蒸餾；每個查詢會從50個候選中取樣7個困難負例（hard negatives），再搭配 batch 內負例，整個訓練過程可在單張 H100 上完成。

團隊也提到，直接在這個骨幹上訓練標準的 SPLADE 會產生塞滿停用詞（stopwords）的龐大向量，因此做了調整：查詢與文件分別加上 [Q]、[D] 前綴，並改用內積（dot product）計算分數；評估時查詢最大長度設為128個 token，文件為512個 token。

📊 **BEIR-13平均56.4分，控制變因後仍略遜同源模型**

在 BEIR-13（不含 MS MARCO）的評測中，Linkup 團隊表示 SPARSEUP 是他們所知150M參數以下、基於詞彙表的稀疏編碼器中表現最好的一個，平均 nDCG@10 為56.4分。但在骨幹與資料都固定的控制比較下，數字沒有那麼漂亮：LateOn 得58.9分、DenseOn 得57.9分，SPARSEUP 為56.4分——且 SPARSEUP 使用近似的 Seismic 搜尋，LightOn 報告的則是精確搜尋結果。細看子項目，SPARSEUP 在 ArguAna 與 Touché 上勝出，也在 HotpotQA 上贏過 DenseOn，但在語意性較強的資料集上落後，其中 FiQA 差距最大，DBPedia 也是弱項。若改看去污染（decontaminated）後的 BEIR，與 DenseOn 的差距縮小到0.17分，不過團隊也提醒，去污染後的 NQ 與 MS MARCO 分別只剩21與46筆查詢，結果雜訊較大，不宜過度解讀。

在 MS MARCO 上，SPARSEUP 平均每個查詢產生47個非零詞項、每份文件190個，相較之下 SPLADE-v3 分別是25與170個。搭配 Seismic 反向索引，SPARSEUP 在單執行緒、平均每次查詢約380微秒的條件下，能達到超過97%相對於精確搜尋的召回率。

⚠️ **刻意維持稀疏，犧牲一點分數**

Linkup 表示，如果放大向量維度，理論上可以再拉高1到2個 BEIR 分數，但團隊選擇維持稀疏設計，以保留稀疏模型在索引效率與可解釋性上的優勢。

🎯 **實務啟示**

對於已經在用 inverted index 做檢索、又想要引入語意能力的團隊，SPARSEUP 提供了一個權重、資料組合與訓練細節都公開的可複現基準；搭配 Seismic 這類近似索引，能在維持毫秒級查詢延遲的同時取得不錯的召回率，是評估「要不要導入稀疏檢索」時值得放進候選清單的選項。

🔗 **來源**
- 標題：Linkup Research Releases SPARSEUP: A 149M-Parameter Open-Source Sparse Embedding Model
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/19/linkup-research-releases-sparseup/

#SPARSEUP #SparseEmbedding #InformationRetrieval #OpenSourceAI #ModernBERT #BEIR #SemanticSearch #Apache2 #EmbeddingModel #NeuralIR
