---
title: 'NVIDIA AI Releases Nemotron 3 Embed: An Open Embedding Collection Whose 8B
  Checkpoint Ranks #1 on RTEB'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/17/nvidia-ai-releases-nemotron-3-embed-an-open-embedding-collection-whose-8b-checkpoint-ranks-1-on-rteb/
score: 90
model: tencent/hy3:free
generated_at: '2026-07-18T07:36:03.942572'
---

📌 【NVIDIA 釋出 Nemotron 3 Embed】8B 嵌入模型登頂 RTEB 檢索榜

TL;DR：NVIDIA 開源三款嵌入模型，8B  checkpoint 在 RTEB 檢索基準拿下整體第一。

當 agent 要決定「該看哪段文字」時，背後靠的就是 embedding model。NVIDIA 這回直接把這一層做成開源集合，宣稱在生產級檢索場景能打。

🤔 **鎖定 agent 檢索與記憶層的嵌入需求**

NVIDIA 釋出 Nemotron 3 Embed 模型系列，目標應用包含生產規模 RAG、agentic retrieval、code retrieval 與 agent memory。這系列不是單一模型，而是三個開放權重 checkpoint 的集合。

🧩 **三個 checkpoint 與統一架構設計**

模型集合包含三個開放 checkpoint：
- Nemotron-3-Embed-8B-BF16：以準確度為優先的選項。
- Nemotron-3-Embed-1B-BF16：沿用相同設計但體積更小。
- Nemotron-3-Embed-1B-NVFP4：針對 Blackwell 最佳化的 4-bit 路徑。

三者的技術基底如下：
- 皆為 transformer encoders，採用 bidirectional attention masking 訓練。
- 最終 embedding 由 token 級表示做 average pooling 得出。
- 每個 checkpoint 最大序列長度皆為 32,768 tokens。
- 模型在 34 種語言上進行評估。
- 授權皆為 OpenMDW License Agreement 1.1 (OpenMDW-1.1)。
- 基底來自 Mistral 模型：8B 基於 Ministral-3-8B-Instruct-2512；兩個 1B 變體皆使用 Ministral-3-3B-Instruct-2512。

📊 **8B 拿下 RTEB 整體第一，1B 壓縮僅微幅掉點**

Nemotron-3-Embed-8B-BF16 在 RTEB（Retrieval Embedding Benchmark）整體排名 #1（截至 2026 年 7 月 17 日），評估涵蓋其 16 個公開任務。以下資料皆為模型序列長度 4096 下的平均 NDCG@10：

- 1B 版本相較前代基線 llama-nemotron-embed-vl-1b-v2，RTEB 提升 10.4 分。
- NVFP4 相較其 BF16 父模型僅損失 0.38 RTEB 分，保留率達 99.5%。

🧩 **1B 模型來自剪枝與蒸餾，非從頭小訓練**

README 指出，1B 分數來自壓縮流程而非較小的訓練回合。父模型為 nemotron-3-embed-3b，經兩輪迭代剪枝與蒸餾：
1. 3B 父模型用 NVIDIA ModelOpt mcore_minitron Neural Architecture Search (NAS) 剪枝至 2B；搜尋範圍含 hidden width、FFN size、attention heads 與 depth，並從 top-10 Pareto front 選最佳候選，以 50k in-domain calibration corpus 評分。
2. 2B 模型從微調後的 8B embedding teacher 蒸餾，損失函式結合 cosine distance loss (COS) 與 mean squared error (MSE) loss。

🎯 **實務啟示**

對建置 RAG 或 agent 檢索系統的團隊，NVIDIA 這組開放權重提供了從 8B 準確度優先到 1B NVFP4 省記憶體的選項，且皆支援 32k 上下文與多語言；若部署在 Blackwell 架構，NVFP4 版本幾乎不損效能卻顯著瘦身，值得納入評估。

🔗 **來源**
- 標題：NVIDIA AI Releases Nemotron 3 Embed: An Open Embedding Collection Whose 8B Checkpoint Ranks #1 on RTEB
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/17/nvidia-ai-releases-nemotron-3-embed-an-open-embedding-collection-whose-8b-checkpoint-ranks-1-on-rteb/

#NVIDIA #Nemotron3Embed #EmbeddingModel #RAG #RTEB #AgenticRetrieval #ModelCompression #NVFP4 #OpenSource #TransformerEncoder
