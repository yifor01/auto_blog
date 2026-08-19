---
title: Multi-Vector (Late Interaction) Embedding Models with Sentence Transformers
source: HuggingFace Blog
url: https://huggingface.co/blog/multi-vector-encoder
model: claude-code/sonnet
generated_at: '2026-08-19T06:43:22.393918'
score: 76
---

📌 一個文件不再只有一個向量：Sentence Transformers v6.0 收編 ColBERT 式多向量檢索

TL;DR：Sentence Transformers v6.0 新增 MultiVectorEncoder，用同一套 API 直接跑 ColBERT／PyLate／ColPali 系列的 late interaction 模型。

一句「green sofa with wooden legs and rounded cushions」丟給一般的 dense embedding 模型，四個條件全部要擠進同一組向量裡，結果往往是「腳型不對的綠色沙發」反而排到很前面。這不是模型不夠好，而是單一向量本身就有壓縮上限。

🤔 背景：單一向量必須把所有資訊擠在一起

一般的 dense embedding 模型讀完一段文字後，只回傳一個固定大小的向量，384、768 或 1024 維，文字裡的一切都得塞進這幾百個數字裡，相似度比對也只是兩個向量之間的一次內積。這在多數情境下表現不錯，但壓縮方式是有代價的：一個罕見實體、一個精確代號，或一段長文中某個關鍵子句，都得跟同一向量裡的其他資訊搶位置。當一個查詢同時帶有多個條件時，同樣的問題會再發生一次。

🧩 方法：把 token 級的資訊留到最後一刻才比對

多向量模型（也稱 late-interaction 或 ColBERT 式模型，得名自 ColBERT 論文）不做這種壓縮。它一樣跑同一個 transformer，但不把 token embedding 池化成一個向量，而是把每個 token embedding 投影到較小的維度（經典設定是 128 維）並全部保留下來。一段 9 個 token 的文件，會變成一個 9x128 的矩陣，而不是一個 1x128 的向量。查詢與文件之間的互動被延後到評分那一刻才發生，這也是「late interaction」這個名字的由來。

文中把三種架構放在一起比較：cross-encoder 讓兩段文字一起進模型互動，準確但沒有任何東西能事先算好，每來一個新查詢都要重新編碼所有文件；bi-encoder（也就是一般的 dense embedding 模型）幾乎不互動，只在兩個已經算好的摘要向量間做一次內積，這也是它能先把整個文件庫編碼好、之後快速查詢的原因；late interaction 介於兩者之間，文件依然可以獨立編碼、離線建索引，但評分時是每一個查詢 token 都去跟每一個文件 token 比對，互動空間比 bi-encoder 大得多。

評分用的是 MaxSim 運算子：對查詢裡的每一個 token，找出它與文件裡所有 token 相似度的最大值，再把這些最大值加總成最終分數。由於 token 向量都經過 L2 正規化，每個比對值其實就是一個介於負一到正一之間的餘弦相似度，整體分數會落在「負的查詢 token 數」到「正的查詢 token 數」這個區間內。可以把它理解成一種軟性對齊：每個查詢 token 都指向最能解釋它的文件 token，最終分數代表文件整體上有多支持這個查詢。這個對齊不必是字面上的比對，因為 token embedding 本身帶有上下文——文中舉例，用 lightonai/mLateOn 對「Where do penguins live?」和「Penguins inhabit Antarctica.」編碼後，查詢裡的 live 會在文件裡找到 inhabit 當作最佳匹配，相似度高達 0.94，儘管兩個詞完全沒有共用字母。這正是傳統詞彙檢索（如 BM25）做不到的事：它們需要字詞本身出現，同義詞或改寫的說法會直接被漏掉。

📊 代價：索引大小暴增，但可以用量化壓縮救回來

文中用 4,874 筆 Natural Questions 段落做示範，多向量模型 lightonai/LateOn 編碼後產生 608,414 個 token 向量，平均每段落 124.8 個向量。

| 表示方式 | 向量數 | 維度 | float32 大小 |
|---|---|---|---|
| Dense, all-MiniLM-L6-v2 | 4,874 | 384 | 7.5 MB |
| Dense, gte-modernbert-base | 4,874 | 768 | 15.0 MB |
| Multi-vector, LateOn | 608,414 | 128 | 311.5 MB |

這大約是 MiniLM 索引的 42 倍，換算下來每段落要多花 62 KiB。不過索引通常會經過壓縮，同樣的 608,414 個向量做成 fast-plaid 索引後只要 92 MB，因為 PLAID 儲存的是每個向量的 centroid id 加上量化後的殘差，而不是完整向量本身。做個對照，像 Qwen3-Embedding-8B 這種 4096 維的 dense 模型，處理同樣 4,874 筆段落大約需要 80 MB，換算下來壓縮後的多向量索引，其實跟目前大家已經在用的 dense 索引處於同一個量級。文中也提到，Token Pooling 可以在建索引前先縮減向量數量，而 Retrieve and Rerank 這種用法則完全不用建索引。

🧩 怎麼用：一行 pip install，四種模型統一 API

安裝方式很單純，`pip install -U sentence-transformers` 即可。升級到 v6.0 後，函式庫多了第四種模型型別 MultiVectorEncoder，任何 PyLate checkpoint、Stanford-NLP 的 ColBERT checkpoint 都能直接載入使用，處理視覺文件檢索的 colpali-engine 模型也可以透過同一套 API 使用，跟原本用來操作 dense、sparse、reranker 模型的介面一致。

背景補充：Sentence Transformers 原本只涵蓋 dense 與 sparse 模型，沒有 late interaction 的支援，因此 LightOn 在它之上另外開發了 PyLate，補齊訓練、推論與檢索所需的元件，包含後面會用到的 late-interaction 索引工具 fast-plaid。v6.0 之後，這些能力直接收進了 Sentence Transformers 本體。

⚠️ 限制：索引成本是硬約束

多向量模型的優勢集中在特定情境：查詢裡某個具體片段才是關鍵的檢索、像沙發例子那種多條件查詢（每個條件都能找到自己的證據）、以及訓練分佈之外的域外資料（dense 模型的壓縮方式是從訓練查詢學來的，可能剛好丟掉正式查詢真正在意的東西）。這個效果會隨文件長度拉長而放大，因為要塞進同一個固定向量裡的文字更多了。但代價很直接：每個 token 存一個向量而不是每份文件存一個向量，向量數量暴增，只有靠更小的維度部分抵銷，實務上必須搭配量化壓縮或 Token Pooling 才划算。

🎯 實務啟示

如果檢索場景裡查詢常常帶多個獨立條件，或需要匹配精確代號、人名、函式名這類「不能被平均掉」的詞，多向量模型值得一試；由於現在直接掛在 Sentence Transformers 裡，遷移成本主要就是評估索引壓縮方案（例如 fast-plaid）能不能把儲存空間壓到跟現有 dense 索引同一量級，而不是重寫整套檢索管線。

🔗 來源
- 標題：Multi-Vector (Late Interaction) Embedding Models with Sentence Transformers
- 作者／機構：Tom Aarsen（Hugging Face）、Antoine Chaffin、Raphael Sourty（LightOn）
- 連結：https://huggingface.co/blog/multi-vector-encoder

#SentenceTransformers #ColBERT #LateInteraction #InformationRetrieval #Embeddings #RAG #SemanticSearch #NLP #HuggingFace #VectorSearch
