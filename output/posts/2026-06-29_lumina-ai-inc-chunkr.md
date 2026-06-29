---
title: lumina-ai-inc/chunkr
source: GitHub Trending
url: https://github.com/lumina-ai-inc/chunkr
score: 95
model: google/gemma-4-31b-it:free
generated_at: '2026-06-29T20:27:35.059127'
---

📌 【開源專案】Chunkr：將複雜檔案轉化為 RAG 可用片段的生產級 API 服務

TL;DR：整合版面分析、OCR 與語意切分，將 PDF、PPT 與 Word 轉為 LLM 可用的結構化片段。

在構建 RAG（檢索增強生成）系統時，最痛苦的往往不是 LLM 的選擇，而是如何將雜亂的 PDF 或 PPT 轉化為高品質、不失義的資料片段。如果切分位置錯誤，模型將失去上下文，導致回答出錯。

🧩 **整合版面分析與 OCR 的檔案處理流程**

Chunkr 提供了一個生產級的服務，旨在將非結構化檔案轉換為 LLM 可讀的格式。其核心能力包含：
- **版面分析與 OCR**：識別檔案結構並提供 Bounding Boxes（邊界框）。
- **格式轉換**：將 PDF、PPT、Word 與圖片轉換為結構化的 HTML 與 Markdown。
- **語意切分 (Semantic Chunking)**：利用 Vision-Language Model (VLM) 處理，將內容切分為適合 RAG 的片段。

🚀 **快速部署與配置方式**

專案提供了靈活的部署與模型配置選項，讓工程師能快速將其整合進工作流：
- **部署方式**：支援使用 Docker Compose 快速啟動。
- **LLM 配置**：可透過 `models.yaml` 進行推薦配置，或使用環境變數進行基礎設定。
- **供應商支援**：支援多種常見的 LLM API 提供者。

⚠️ **開源版與雲端版的關鍵差異**

開發者在選擇版本時需注意，開源版（AGPL 授權）與其雲端 API 服務在底層模型上有顯著區別：
- **模型能力**：開源版使用社群/開源模型；雲端版則執行原廠開發的專有模型，在準確度、速度與企業級可靠性上表現更佳。
- **功能支援**：開源版目前不支援 Excel 格式，而雲端版與企業版則提供原生解析支援。
- **基礎設施**：開源版需自行託管 (Self-hosted)，雲端版則為完全託管服務。

🎯 **實務啟示**

對於正在建構 RAG 管道的工程師來說，Chunkr 的價值在於它將「版面分析 $\to$ OCR $\to$ 結構化 $\to$ 切分」這一連串複雜的預處理步驟封裝成一個 API 服務。如果你需要處理大量含有複雜版面的檔案，且不希望從零開始組合多個開源工具，這是一個值得嘗試的整合方案。

🔗 **來源**
- 標題：chunkr
- 作者／機構：lumina-ai-inc
- 連結：https://github.com/lumina-ai-inc/chunkr

#RAG #OCR #DocumentIntelligence #OpenSource #LLM #SemanticChunking #LayoutAnalysis #VLM #PDFParsing #MachineLearning
