---
title: 'Meet LEANN: An Open-Source Vector Index that Shrinks a 60M-Chunk RAG Index
  from 201 GB to 6 GB'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/27/leann-vector-index-mlsys-2026/
model: claude-code/sonnet
generated_at: '2026-10-28T21:50:36.952768'
score: 110
---

📌 LEANN：RAG 索引從 201GB 砍到 6GB 的開源向量索引

TL;DR：查詢時才重算 embedding，UC Berkeley 的 LEANN 讓 6000 萬筆 Wikipedia 索引從 201GB 縮到 6GB。

向量索引通常比原始資料還肥：一個 76GB 的語料庫，光是 embedding 就要 173GB，再加上 HNSW 圖結構的 15GB，等於索引比資料本身還大一倍以上。UC Berkeley Sky Computing Lab 做了一件反直覺的事，讓索引幾乎不存 embedding。

🤔 **向量索引為何總是「比資料還大」**

LEANN（Low-storage approximate nearest neighbor index）是建構在 FAISS 之上的低儲存空間 ANN 索引，目標是解決一個具體問題：向量索引往往比它索引的資料本身還大。這篇研究論文獲得了 MLSys 2026 的 Best Research Paper 獎，程式碼採 MIT 授權。

🧩 **查詢時才重算，不存完整向量**

Graph-based 索引（如 HNSW）每次查詢只會走訪一小部分節點，LEANN 利用了這個特性：只保留經過剪枝（pruned）的圖結構，加上一張精簡的 product quantization（PQ）表，完全不存完整向量，查詢時只針對搜尋路徑上走到的節點重新計算 embedding。研究團隊用了多種技術讓這個做法實際可用，其中 ablation 顯示 two-level search 平均帶來 1.4 倍加速，加上 batching 後提升到 1.8 倍；即便如此，embedding 重算仍佔查詢延遲的約 76%。

📊 **儲存省 95%，但查詢時間變長**

研究團隊在 NQ、TriviaQA、GPQA、HotpotQA 上，對一個 6000 萬段落的 RPJ-Wiki 資料庫做測試，延遲以 90% Recall@3 為基準。以下數據均為論文自報：

| 方法 | NQ 下游準確率 | 儲存空間 |
|---|---|---|
| LEANN | 25.5% | 4 GB |
| HNSW | 25.5% | 188 GB |
| BM25 | 18.3% | － |
| PQ 壓縮 | 17.9% | － |

在 RTX 4090 上搭配 Qwen3-4B，LEANN 與 HNSW 的下游準確率打平在 25.5%，儲存空間卻從 188GB 降到 4GB。代價是搜尋時間：LEANN 在 NQ 上的檢索要 2.48 秒，HNSW 只要 0.05 秒；生成約需 20 秒，因此端到端延遲從 20.95 秒增加到 23.34 秒。跨資料集測試中，LEANN 檢索時間從 1.12 秒（GPQA）到 7.12 秒（HotpotQA）不等。作為對照，受 EdgeRAG 啟發的 IVF-based 重算基準最高慢了 200 倍。相較 BM25，LEANN 的精確匹配（exact match）最高提升 11.8%。在個人資料場景，GitHub repo 報告 40 萬則聊天訊息從 1.8GB 縮到 64MB，3.8 萬筆瀏覽紀錄從 130MB 縮到 6.4MB。在 ContextBench 的 30 個 SWE-Bench Pro 任務上，LEANN 的初始相關程式碼 recall 為 24.2%，對比 BM25 的 11.4%，agent 使用的 token 數還減少 8.4%。

🧩 **怎麼用**

LEANN 可用 `uv pip install leann` 安裝。Repo 內建文件、Apple Mail、Chrome 瀏覽紀錄、WeChat、iMessage，以及 ChatGPT 或 Claude 匯出紀錄的現成應用，MCP reader 還能拉取 Slack 與 Twitter 書籤的即時資料；LEANN 也能作為 Claude Code 的語意搜尋 MCP 伺服器運作。預設後端是 HNSW，也支援 DiskANN 做更快速的搜尋；生成端則相容 Ollama、Hugging Face、Anthropic，或任何 OpenAI 相容 API。

⚠️ **限制**

LEANN 的核心取捨是用查詢延遲換儲存空間，以 NQ 為例，端到端延遲從約 21 秒增加到約 23 秒。平臺支援涵蓋 Ubuntu、Arch、WSL、macOS 與 Windows，但部分應用（如 Apple Mail 搜尋）僅支援 macOS。

🎯 **實務啟示**

如果你要在筆電或儲存空間有限的環境中，對個人資料（信件、聊天記錄、瀏覽歷史）做語意搜尋或 RAG，LEANN 提供了一個「用時間換空間」的實際方案，而且已有現成的應用整合與 MCP 伺服器，可直接接上 Claude Code 之類的 agent 工作流。

🔗 **來源**
- 標題：Meet LEANN: An Open-Source Vector Index that Shrinks a 60M-Chunk RAG Index from 201 GB to 6 GB
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/27/leann-vector-index-mlsys-2026/

#RAG #VectorSearch #LEANN #OpenSource #FAISS #SemanticSearch #MLSys2026 #UCBerkeley #LLM #EmbeddingCompression
