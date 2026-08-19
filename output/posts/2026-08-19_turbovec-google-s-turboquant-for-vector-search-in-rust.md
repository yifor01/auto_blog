---
title: Turbovec – Google's TurboQuant for vector search in Rust
source: Hacker News
url: https://github.com/RyanCodrai/turbovec
model: claude-code/sonnet
generated_at: '2026-08-19T06:37:04.511425'
score: 87
---

📌 Turbovec：4GB 記憶體裝下千萬筆向量，速度還贏 FAISS

TL;DR：Rust 實作 Google TurboQuant 演算法的向量索引，記憶體省下八成、搜尋速度勝過 FAISS。

一千萬筆文件的向量語料庫，用 float32 儲存要吃掉 31GB 記憶體。Turbovec 把它壓進 4GB，而且搜尋還比 FAISS 快。

🤔 向量索引的老問題：記憶體、訓練、重建

RAG 系統的向量索引常見痛點是記憶體佔用大，而傳統 PQ（product quantization）量化通常需要獨立的訓練階段與參數調整，語料庫成長時還得面對重建成本。Turbovec 是一個帶 Python bindings 的 Rust 向量索引，支援 online ingest：向量加進去就直接被索引，不需要 train 步驟、不用調參數、語料庫成長也不用重建。

🧩 基於 TurboQuant 的 data-oblivious 量化器

Turbovec 底層採用 Google Research 的 TurboQuant 演算法，是一種 data-oblivious 的量化器，號稱有接近最佳的失真表現，且不需要獨立的訓練階段。搜尋效能靠手寫的 SIMD kernel：ARM 上用 NEON SDOT/SMMLA，x86 上用 AVX-512 VNNI 與 vpermb，並提供 AVX2 與 scalar 版本作為 fallback。持久化採用 incremental save：sync() 只寫入自上次同步後變動的部分，每次呼叫只需一次 fsync，任何位元組寫入中斷都能保持索引可用；write/load 則用於整檔快照。搜尋時可傳入 id allowlist 或 slot bitmask 做過濾，過濾邏輯直接在 SIMD kernel 內以 32 個向量為一個 block 的粒度執行，沒有允許項目的 block 會被直接跳過，因此篩選條件越嚴格，反而越省運算。整個系統純本機執行，資料不會離開本機或 VPC。

📊 實測：recall 打平甚至贏過 FAISS，速度快 3 倍以上

在 100K 向量、k=64 的測試中，校正後的 TurboQuant（TQ+）在 OpenAI d=1536 與 d=3072 的四組設定裡，有三組在 R@1 指標上贏過 FAISS IndexPQ（LUT256, nbits=8），領先幅度 0.9 到 2.9 分，僅 d=1536 的 4-bit 落後 0.7 分；兩者在 k=8 時都能到達 1.0 的 recall。低維度的 GloVe（d=200）情境較吃力，TQ+ 在 R@1 仍領先 FAISS（4-bit 領先 1.9 分、2-bit 領先 0.8 分），但 FAISS 在 2-bit、k≈8 之後保有些微優勢。

搜尋速度方面，在 ARM（GCP c4a-standard-8, Google Axion, 8 vCPUs）上，Turbovec 在每個測試設定都贏過 FAISS FastScan，4-bit 平均快 3.5 倍，2-bit 平均快 26%；在 x86（Intel Xeon Platinum 8481C, 8 vCPUs）上，4-bit 平均快 3.4 倍，2-bit 平均快 20%。插入延遲測試中，單筆 add() 耗時 6.3 到 19.7 微秒（比 FAISS 快 7.6 到 13.9 倍），以 100 筆為一批插入則攤提到每筆 4.6 到 16.3 微秒（比 FAISS 快 4.6 到 15.1 倍）。

🧩 怎麼用

安裝與最小範例：

pip install turbovec

from turbovec import TurboQuantIndex
index = TurboQuantIndex(dim=1536, bit_width=4)
index.add(vectors)
scores, indices = index.search(query, k=10)
index.write("my_index.tv")

若需要在刪除後仍保持穩定的外部 id，可改用 IdMapIndex，支援 add_with_ids、以 O(1) 複雜度用 id 移除向量。Turbovec 也提供 LangChain、LlamaIndex、Haystack、Agno 的框架整合套件，可以直接替換這些框架內建的 in-memory 向量／文件儲存，介面與持久化語意維持一致，換個 import 就能接上既有 pipeline。

⚠️ 限制

在低維度 embedding（如 d=200 的 GloVe）情境下，TurboQuant 演算法所依賴的 asymptotic Beta 假設較不成立，2-bit 量化時 FAISS 在較深的 k 值仍保有些微優勢；這代表演算法特性在超低維度場景下的優勢不如高維度明顯。

🎯 實務啟示

如果正在為 RAG 系統挑向量索引，特別在意記憶體成本、不想忍受訓練與重建流程、又需要資料留在本機或 VPC 內，Turbovec 提供了一個可以直接替換 LangChain、LlamaIndex 或 Haystack 內建 in-memory store 的選項，值得納入評估清單。

🔗 來源
- 標題：Turbovec – Google's TurboQuant for vector search in Rust
- 作者／機構：fittingopposite (Hacker News) / RyanCodrai (GitHub)
- 連結：https://github.com/RyanCodrai/turbovec

#Rust #VectorSearch #TurboQuant #RAG #FAISS #Quantization #SIMD #OpenSource #Embeddings #MachineLearning
