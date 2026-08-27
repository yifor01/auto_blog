---
title: Training and Finetuning Multi-Vector Embedding Models with Sentence Transformers
source: HuggingFace Blog
url: https://huggingface.co/blog/train-multi-vector-encoder
model: claude-code/sonnet
generated_at: '2026-08-27T17:26:01.911433'
score: 94
---

📌 用單張 RTX 3090 訓練，Multi-Vector 檢索模型贏過所有通用模型

TL;DR：Sentence Transformers v6.0 新增 MultiVectorEncoder，讓你在消費級 GPU 上微調出打敗通用檢索模型的 ColBERT 式模型。

一份平均長度 941 tokens 的醫療文件，丟給多數通用檢索模型會發生什麼事？答案是：模型在你不知情的狀況下，默默丟掉了文件的大半內容。這正是 Sentence Transformers 這篇文章想解決的問題。

🤔 **通用模型的隱藏地雷：截斷**

Sentence Transformers 是一個用於訓練與使用 embedding、reranker 模型的 Python 函式庫，應用場景涵蓋 RAG、語意搜尋、語意文本相似度等。v6.0 更新新增第四種模型型別 MultiVectorEncoder，用於 ColBERT 式的 late interaction 檢索，並附上完整的訓練方法。

文章指出，多數釋出的檢索模型是為短段落設計的：經典 ColBERT checkpoint 把文件截斷在 180 或 300 tokens，許多熱門 dense 模型也只到 256 或 512 tokens，原因是它們的 MS MARCO 式訓練資料本來就很少超過這個長度。作者在自己的醫療檢索評測（平均段落長度 941 tokens）中測得，這種截斷造成的損失最多達到 0.24 NDCG@10，比不同模型架構之間的差異還要大得多。

🧩 **什麼是 Multi-Vector 模型：不壓縮，逐 token 比對**

Dense embedding 模型會把整段文字壓縮成單一向量，相似度計算就是兩個向量的一次內積。Multi-vector（也稱 late-interaction 或 ColBERT 式）模型則跳過這個壓縮步驟：每個 token 保留一個小向量，查詢與文件之間用 MaxSim 運算子計分，也就是查詢的每個 token 都去找文件中最匹配的 token，再把分數加總。這種 token 級別的比對保留了單一向量必須平均掉的細粒度訊號，通常能帶來更強的檢索效果，代價是索引會變大。

🛠️ **兩種起點：續練既有模型，或從零打造**

如果要在既有的 multi-vector 模型上繼續微調，架構完全不用煩惱：

```python
from sentence_transformers import MultiVectorEncoder
model = MultiVectorEncoder(
    "lightonai/mLateOn-unsupervised",
    model_kwargs={"torch_dtype": "float32"},
    processor_kwargs={"model_max_length": 8192},
)
```

checkpoint 會自帶查詢／文件標記 token、投影頭、計分 skiplist 等完整配方。作者特別提醒要檢查長度設定，許多釋出的 checkpoint 把文件長度上限設在 180 到 512 tokens，而他的醫療段落長達 1,400 tokens；mLateOn 系列已經能用滿 backbone 的 8192 token context，但如果起始 checkpoint 帶有長度上限，可以直接解除：

```python
model[0].query_length = None
model[0].document_length = None
```

作者也加上了標點符號 skiplist，讓文件端計分與儲存時排除標點 token。在「不排除／排除標點／排除停用詞／兩者都排除」的四向消融實驗中，這個設定在品質上小幅勝出，同時讓這份資料的文件索引縮小了 9.6%：

```python
import string
model[2].skiplist_words = list(string.punctuation)
model[2].resolve_with_tokenizer(model.tokenizer)
```

若想從零開始，直接指向任意 base transformer 即可，函式庫會自動附加一個隨機初始化的 token 級投影層：

```python
from sentence_transformers import MultiVectorEncoder
model = MultiVectorEncoder("answerdotai/ModernBERT-base", model_kwargs={"torch_dtype": "float32"})
```

📊 **14.5 小時、單張 RTX 3090，打敗所有通用檢索模型**

作者用這套方法訓練出的 multi-vector-encoder/mLateOn-medical 模型，在單張 RTX 3090 上訓練 14.5 小時，在他自己的醫療檢索評測中，全面超越了他能找到的所有通用檢索模型，涵蓋 dense、sparse、lexical、multi-vector 各種類型。

⚠️ **仍要留意索引成本**

Token 級別比對雖然保留了更細粒度的訊號，但代價是索引體積比單向量模型大，這是 multi-vector 架構本身的取捨，作者用 punctuation skiplist 之類的技巧來部分緩解，但無法完全消除。

🎯 **實務啟示**

如果你的檢索場景屬於垂直領域（醫療、法律、金融，或公司內部文件），而且文件長度偏長，這篇文章給出的訊息很直接：官方不會為你的領域出模型，但你可以自己在一張消費級 GPU 上、幾小時內訓練出來。動手前務必先確認起始 checkpoint 的長度上限設定，這往往比選擇哪個模型架構更影響最終效果。

🔗 **來源**
- 標題：Training and Finetuning Multi-Vector Embedding Models with Sentence Transformers
- 作者／機構：Tom Aarsen, Hugging Face
- 連結：https://huggingface.co/blog/train-multi-vector-encoder

#SentenceTransformers #ColBERT #MultiVectorEmbedding #RetrievalAugmentedGeneration #SemanticSearch #EmbeddingModels #HuggingFace #NLP #InformationRetrieval #Finetuning
