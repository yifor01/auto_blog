---
title: opendatalab/MinerU
source: GitHub Trending
url: https://github.com/opendatalab/MinerU
score: 99
model: google/gemma-4-31b-it:free
generated_at: '2026-06-25T20:22:01.733979'
---

📌 【opendatalab】MinerU：支援 109 國語言，將多格式檔案精準轉為 Markdown 的解析引擎

TL;DR：高精度的檔案解析引擎，透過 VLM+OCR 雙引擎將 PDF 等多種格式轉為結構化 Markdown/JSON，強化 RAG 與 Agent 流程。

處理 LLM 或 RAG 應用時，最痛苦的往往不是模型能力，而是如何將雜亂的 PDF、PPTX 或掃描檔，在不丟失格式的情況下轉成機器可讀的結構化資料。

🧩 **VLM 與 OCR 雙引擎實現高精度解析**

MinerU 旨在解決複雜檔案的解析問題，將 PDF、DOCX、PPTX、XLSX、影像及網頁內容，統一轉換為結構化的 Markdown 或 JSON 格式。其核心技術亮點在於：

- **雙引擎驅動**：結合 VLM（視覺語言模型）與 OCR，支援 109 種語言的識別。
- **精準佈局重建**：能處理掃描檔案、手寫文字、多欄位佈局，並支援跨頁表格合併。
- **結構化輸出**：公式轉換為 LaTeX，表格轉為 HTML，且輸出順序遵循人類閱讀邏輯，並會自動去除頁首與頁尾。

🔌 **從 MCP Server 到 RAG 框架的全面整合**

MinerU 不僅提供解析能力，更將整合路徑延伸至開發者的工具鏈中：

- **AI 程式設計工具**：透過 MCP Server 整合至 Cursor、Claude Desktop 及 Windsurf。
- **RAG 框架**：原生支援 LangChain、LlamaIndex、RAGFlow、RAG-Anything、Flowise、Dify 與 FastGPT。
- **開發介面**：提供 Python、Go 與 TypeScript SDK，以及 CLI、REST API 與 Docker 部署選項。
- **低門檻使用**：提供 mineru.net 線上版、Gradio WebUI 及桌面客戶端。

🖥️ **彈性的部署模式與硬體支援**

根據不同的效能需求，MinerU 提供三種推理後端選擇：

- **pipeline**：速度快且穩定，無幻覺問題，支援 CPU 或 GPU 執行。
- **vlm-engine**：追求高精度，支援 vLLM、LMDeploy 及 mlx 生態系。
- **hybrid-engine**：結合原生文字提取與高精度識別，降低幻覺。

此外，該專案在硬體相容性上相當廣泛，支援 Ascend、Cambricon、Enfla 等多款 AI 晶片。

🎯 **實務啟示**

對於建構 RAG 系統的工程師而言，MinerU 的價值在於將「非結構化檔案 $\rightarrow$ 結構化 Markdown」這一環節標準化。特別是其對 MCP Server 的支援，讓開發者能直接在 Cursor 等 AI 編輯器中處理檔案解析，大幅縮短了資料前處理的工程時間。

🔗 **來源**
- 標題：opendatalab/MinerU
- 作者／機構：opendatalab
- 連結：https://github.com/opendatalab/MinerU

#AI #RAG #OCR #VLM #Markdown #DocumentParsing #LLM #LangChain #MCP #OpenSource
