---
title: 'Perplexity Releases pplx-embed-v2-context-9b-preview: A Contextual Embedding
  Model That Retrieves Answers and Their Supporting Evidence'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/30/perplexity-releases-pplx-embed-v2-context-9b-preview-a-contextual-embedding-model-that-retrieves-answers-and-their-supporting-evidence/
model: claude-code/sonnet
generated_at: '2026-10-01T22:02:28.280253'
score: 95
---

📌 Perplexity 新 embedding 模型：檢索答案的同時，連「證據」一起找出來

TL;DR：pplx-embed-v2-context-9b-preview 訓練時連答案的佐證段落一起學，解決 RAG 單一金標段落的盲點。

RAG 系統最尷尬的場景之一：三份租約文件裡都寫著「每月租金為…」，但只有一份屬於你要找的那間房子。傳統的 chunk 檢索常常只盯著「哪一段最像答案」，卻漏掉了「哪一段能證明這個答案是對的」。Perplexity Research 與 turbopuffer 聯手釋出的 pplx-embed-v2-context-9b-preview，想解決的正是這個落差。

🤔 **問題：金標段落之外的證據，全被當成負樣本**

RAG 系統會把長文件切成多個 chunk，但一個 chunk 的意義經常依賴文件別處提到的實體、標題或定義。近期的 contextual embedding 模型多半採用 late chunking 來處理：先把整份文件編碼一次，再針對每個 chunk 做 pooling。問題在於訓練階段通常只標記「一個」金標 chunk，其餘全部當作負樣本，連能幫忙驗證答案的佐證句子也不例外。Perplexity 另外點出三個延伸問題：二元標籤給出的訓練訊號太粗糙；用 LLM 標註資料的成本會隨資料量線性增加；而且標籤往往綁死在單一種切分策略上。

🧩 **方法：用「教師模型」打分，取代單一金標籤**

pplx-embed-v2-context-9b-preview 的核心改動在訓練訊號：模型學習的目標是同時檢索出答案「以及」驗證這個答案所需要的上下文，而不是單一金標段落。負責打分的教師模型是 Perplexity 自家的 query-aware context compression 模型，它會同時讀入 query 與文件，為每個 token 評分。每個訓練批次會隨機抽樣一種切分策略，chunk 之間以一個學習到的 `<|chunk_sep|>` token 分隔並做 mean pooling。由於教師模型只在訓練階段運作，推論時不會增加延遲或儲存成本。

模型本身是從 Perplexity 內部的 9B ColBERT 檢索模型出發，接上線性投影輸出 2048 維向量，並透過 Matryoshka 訓練同時支援 1024 維；再搭配 quantization-aware training，讓模型原生支援 int8 embedding。這次釋出的版本是多個 checkpoint 的 model soup，訓練資料涵蓋約 430 個資料集、超過 50 種語言，且不含 ConTEB 資料。

📊 **資料與評測：context-bench 上的表現**

Perplexity 以自建的 context-bench 進行評測（2,099 筆查詢、38,894 份文件、2,458,072 個句子層級 chunk，採取窮舉式排序）。在 K=10 的設定下，Perplexity 報告其模型與 voyage-context-4 相比分別領先 14.4 分與 5.0 分（文中 Voyage 數值是以 Perplexity 公布的差距反推所得）。在成本面，Perplexity 指出以 1024 維 int8（每筆 1 KB）儲存，在其 chunk 檢索測試集上的表現，還略微超越 2048 維 float32（每筆 8 KB）的 voyage-context-4；而跨 74 項 MTEB 任務的平均 nDCG@10（敏感度指標）也在報告中一併公布。

🧩 **怎麼用：已開源，但還沒進 API**

這個模型現在就可以自行部署：權重已上架 Hugging Face，採用 MIT 授權，載入時需要 `transformers>=5.4.0` 並開啟 `trust_remote_code=True`。目前尚未整合進 Perplexity 自家 API，官方在模型卡上也特別註明，這是 preview 版本，權重與介面之後可能會有不向下相容的變動。

⚠️ **限制**

模型卡明確標註這是 preview 版本，介面與權重可能隨時改動；目前也只能自行架設推論服務，無法透過 Perplexity API 直接呼叫。

🎯 **實務啟示**

如果你的 RAG 系統常常遇到「答案對了，但驗證不了」的狀況，這種把驗證證據也納入訓練目標的做法值得關注。由於權重已經開源且支援低維度 int8 embedding，對儲存成本敏感的團隊可以優先評估用 1024 維版本取代既有的高維浮點數 embedding，在縮小儲存體積的同時不犧牲太多檢索品質。

🔗 **來源**
- 標題：Perplexity Releases pplx-embed-v2-context-9b-preview: A Contextual Embedding Model That Retrieves Answers and Their Supporting Evidence
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/30/perplexity-releases-pplx-embed-v2-context-9b-preview-a-contextual-embedding-model-that-retrieves-answers-and-their-supporting-evidence/

#Perplexity #RAG #EmbeddingModel #ContextualRetrieval #InformationRetrieval #OpenSource #HuggingFace #VectorSearch #MachineLearning #NLP
