---
title: Google DeepMind Releases EmbeddingGemma 2, a 740M Open Multimodal Embedding
  Model Built on Gemma 4
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/06/google-deepmind-releases-embeddinggemma-2-a-740m-open-multimodal-embedding-model-built-on-gemma-4/
model: claude-code/sonnet
generated_at: '2026-10-06T21:53:51.611655'
score: 103
---

📌 740M 參數打通五種模態，Google DeepMind 開源可離線跑的嵌入模型

TL;DR：EmbeddingGemma 2 用單一向量空間統一文字、程式碼、圖片、影片與音訊，Apache 2.0 授權，手機上就能跑 RAG。

一支手機能同時「看懂」文字、照片、影片和語音備忘錄嗎？Google DeepMind 剛發布的 EmbeddingGemma 2，把這五種模態全部塞進同一個 768 維向量空間，而且模型只有 740M 參數，今天就能下載部署。

🤔 **為什麼需要跨模態 embedding**

Embedding 模型把內容轉成一組數字向量，用來捕捉語意，意思相近的內容在向量空間裡會彼此靠近，方便搜尋與比對。在 RAG（Retrieval-Augmented Generation）流程中，這些向量讓 LLM 能檢索自己訓練時沒見過的最新資訊。把 embedding 生成放在裝置本地執行，資料不出裝置、延遲更低，也能離線運作，這正是 EmbeddingGemma 2 瞄準的場景：裝置端搜尋、分類與重視隱私的 RAG。

🧩 **建立在 Gemma 4 架構上的模組化設計**

EmbeddingGemma 2 以 Gemma 4 架構為基礎，支援文字查詢檢索圖片、語音備忘錄檢索影片，甚至把文字、圖片、示範影片交錯混合的商品列表，編碼成單一向量。模型設計是模組化的，分成三個部分，開發者可依需求只載入需要的版本：270M（純文字）、440M（文字＋視覺）、570M（文字＋音訊），或 740M（全模態）。所有版本共享同一個向量空間，也就是說用純文字版本編碼的查詢，依然能比對出全模態版本編碼的文件。

此外，context window 來到 8,192 tokens，是上一版的 4 倍，足以容納約 29 張圖片、58 個影片畫格，或 5.5 分鐘音訊。

📊 **跑分與資源消耗**

Google 研究團隊表示，在 sub-1B 參數規模的多模態 embedding 模型中，EmbeddingGemma 2 在 MTEB Code 與 MAEB 上拿下領先成績；在 768 維、全精度下，程式碼檢索（code retrieval）提升 9.92 分，約 14%，多語言文字品質則維持穩定。不過體量更大的模型在部分排行榜仍領先，例如 Qwen3-VL-Embedding-2B 在自家 MMEB-V2 跑分報 73.2，參數量約為 EmbeddingGemma 2 的 2.7 倍，且不支援音訊。

在資源消耗方面，於 Pixel 11 Pro 上搭配量化，純文字權重的 active RAM 約 191MB，全模態模型約 567MB；量化感知訓練（quantization-aware training）把權重壓縮到 INT4／INT8。Google AI Edge 團隊在 MacBook M5 Pro GPU 上測得每張圖片 37.3 ms（70-token 視覺預算）。

透過 Matryoshka Representation Learning（MRL），開發者可以把向量截斷到 512、256 或 128 維：從 768 維降到 128 維，儲存空間最多省 6 倍。截到 256 維時，MTEB 多語言分數從 61.36 僅略降到 60.41；但到 128 維，MMEB 分數會掉到 45.65，因此 Google 建議 128 維主要用於純文字場景。

💡 **部署生態已經鋪好**

EmbeddingGemma 2 目前可在 sentence-transformers v6.1.0+、Transformers、vLLM、SGLang、MLX、llama.cpp、Ollama、LM Studio、LiteRT 與 MediaPipe 上運作；向量儲存可搭配 Qdrant，微調可用 Unsloth。針對 Android 的 ML Kit 整合（含 NPU 加速）也將在數週內推出。權重已上架 Hugging Face 與 Kaggle，想快速試用的話，執行 `ollama pull embeddinggemma-2` 即可，tag 從 270m（378MB）到 740m（1.3GB）都有，Demo 可在 Google AI Edge Gallery 體驗。

🎯 **實務啟示**

對要做隱私優先 RAG 或裝置端多模態搜尋的工程師，EmbeddingGemma 2 的模組化設計值得關注：可以先用 270M 純文字版上線，之後再無縫升級到全模態版本而不必重建索引，因為所有子模型共享同一個向量空間。128 維截斷特別適合純文字的大規模向量資料庫，能大幅壓低儲存成本。

🔗 **來源**
- 標題：Google DeepMind Releases EmbeddingGemma 2, a 740M Open Multimodal Embedding Model Built on Gemma 4
- 作者／機構：Asif Razzaq
- 連結：https://www.marktechpost.com/2026/10/06/google-deepmind-releases-embeddinggemma-2-a-740m-open-multimodal-embedding-model-built-on-gemma-4/

#EmbeddingGemma #GoogleDeepMind #Gemma4 #MultimodalAI #RAG #OnDeviceAI #OpenSource #VectorEmbeddings #MachineLearning #AIEngineering
