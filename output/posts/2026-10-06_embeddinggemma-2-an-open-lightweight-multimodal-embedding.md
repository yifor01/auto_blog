---
title: 'EmbeddingGemma 2: an open, lightweight multimodal embedding model'
source: Google DeepMind
url: https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/
model: claude-code/sonnet
generated_at: '2026-10-06T21:48:48.965904'
pinned: true
---

📌 Google DeepMind 推出 EmbeddingGemma 2：7.4 億參數塞進手機的多模態 embedding 模型

TL;DR：EmbeddingGemma 2 讓文字、圖片、音訊、影片共用一個向量空間，完全跑在裝置端。

去年 EmbeddingGemma 上線時，Google DeepMind 可能沒料到下載量會衝破 2000 萬次。開發者用它在手機上跑語意搜尋、打造隱私優先的 RAG（retrieval augmented generation）pipeline。這次升級不是單純擴大模型，而是把文字以外的模態——程式碼、圖片、影片、音訊——全部塞進同一個向量空間，而且依然是能在消費級硬體上跑的輕量模型。

🤔 **從「文字 embedding」到「任意模態 embedding」**

第一代 EmbeddingGemma 解決的是裝置端文字 embedding 的品質與體積問題，讓 app 不需要把資料送上雲端就能做搜尋與比對。但現實世界的資料本來就是多模態的：一段語音備忘錄裡可能提到某個影片片段、使用者可能想用一張圖片去找相似的媒體檔案。EmbeddingGemma 2 的目標就是讓這些跨模態查詢，由「同一個模型」在裝置端原生處理，不需要分別呼叫文字模型、圖片模型再手動對齊向量空間。

🧩 **建立在 Gemma 4 之上的模組化設計**

EmbeddingGemma 2 以 Gemma 4 架構為基礎，採用 Apache 2.0 授權開放下載，總參數量 7.4 億，官方定位為「最適合裝置端推論」的規模。其設計重點是模組化：

- 純文字工作負載最少只需要 2.7 億參數
- 需要視覺理解時加掛 1.7 億參數的視覺編碼器
- 需要音訊理解時加掛 3 億參數的音訊編碼器

換句話說，開發者可以依照應用場景只載入需要的模組，而不是永遠扛著完整的多模態權重。

輸出向量維度為 768，並透過 Matryoshka Representation Learning（MRL）技術，可依需求動態截斷到 512、256 甚至 128 維，官方表示這能為本地向量資料庫帶來最高 6 倍的儲存空間節省。上下文長度也從第一代的規格擴大 4 倍，來到 8K tokens，足以處理最長 5.5 分鐘的音訊、29 張圖片、58 個影格，或是這些模態交錯組合的輸入。

由於與 Gemma 4 共用文字 tokenizer 與音訊編碼器，兩個模型可以組成單一 pipeline 一起跑，整體記憶體佔用會比各自獨立部署更低。

📊 **程式碼理解大幅進步，裝置端記憶體也壓得很低**

官方公布的量化數據中，最明顯的進步落在程式碼語意理解：

| 項目 | EmbeddingGemma 1 | EmbeddingGemma 2 |
|---|---|---|
| MTEB Code 分數 | 68.76 | 78.68（+9.92） |

官方稱這讓模型適合用於本地程式碼庫索引、語意程式碼搜尋，以及 coding agent 的檢索需求。在圖片、影片、文件、音訊等任務上，官方表示 EmbeddingGemma 2 在「sub-1B 參數」級別中建立了新的品質／參數比標準，甚至在部分任務上超越參數量兩倍以上的專用模型。

實機記憶體表現方面，在 Google Pixel 11 Pro 上經過量化後，純文字權重大約只需 191MB 執行期 RAM，完整多模態模型（含視覺與音訊編碼器）約需 567MB。

💡 **為什麼這對裝置端 AI 開發是個關鍵拼圖**

把 embedding 運算留在裝置端，直接解決了三個長期痛點：資料隱私（原始內容不需要離開裝置）、pipeline 延遲（省去網路往返），以及離線可用性。官方也同步釋出了幾個示範應用，說明這個模型的實際用法：在 Google AI Edge Gallery 的 Instant Media Search 中用文字或圖片做語意比對找出媒體庫中的相符內容；在 Video Moments Finder 中用文字或音訊查詢定位影片中的特定片刻；在 Google AI Edge Foresight app 中，將 EmbeddingGemma 2 負責的本地檔案檢索與 Gemma 4 的語境推理組合成完整的裝置端 RAG 系統。此外還能透過 MediaPipe Decision Task API，把多模態 embedding 用於即時分類、路由與預測決策引擎。

生態系整合也做得相當完整：模型權重可在 Hugging Face 與 Kaggle 下載，LiteRT Community 提供裝置端最佳化版本；部署面支援 Google AI Edge MediaPipe、LiteRT，瀏覽器端可用 transformers.js 或 WebGPU；推論框架涵蓋 transformers、sentence-transformers、MLX、vLLM、llama.cpp、SGLang、Ollama、LMStudio；向量儲存可搭配 Qdrant；微調則有 Unsloth 提供的指南。

🎯 **實務啟示**

如果你的團隊正在做裝置端搜尋或隱私優先的 RAG，EmbeddingGemma 2 的模組化參數設計（270M 文字 / +170M 視覺 / +300M 音訊）值得拿來評估：不必為了多模態能力一次扛下整包權重，可以依場景漸進式加掛模組。MRL 的動態維度截斷也是個值得注意的細節——如果儲存空間是瓶頸，先用低維度向量跑原型，確認檢索品質可接受後再視需求升級維度，是個低成本的最佳化路徑。對已經在用 Gemma 4 做生成任務的團隊，共用 tokenizer 與音訊編碼器這點意味著整合 embedding 與生成模型的邊際成本會更低。

🔗 **來源**
- 標題：EmbeddingGemma 2: an open, lightweight multimodal embedding model
- 作者／機構：Google DeepMind
- 連結：https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/

#EmbeddingGemma #GoogleDeepMind #Gemma4 #OnDeviceAI #MultimodalEmbedding #RAG #SemanticSearch #EdgeAI #OpenSourceAI #LiteRT
