---
title: "opendatalab/MinerU"
source: GitHub Trending
url: https://github.com/opendatalab/MinerU
score: 116
model: tencent/hy3-preview:free
generated_at: 2026-05-29T20:55:42.172061
---

📌 【opendatalab】MinerU：多格式文件解析工具，一鍵轉 Markdown/JSON  

想把 PDF、Office、圖片直接喂給 LLM 用？一鍵解析，零安裝就能用。  

🤔 **文件準備成為 LLM/RAG/Agent 的瓶頸**  
在大語言模型、檢索增強生成或智慧代理的工作流程中，原始文件常常是 PDF、DOCX、PPTX、XLSX 或掃描圖片。手動轉成結構化文字費時且易出錯，亟需一個能即時輸出 Markdown/JSON 的解析引擎。  

🧪 **零安裝網頁版＋完整桌面客戶端＋即時 API**  
MinerU 提供三種使用方式：直接在 mineru.net 線上使用、下載跨平台桌面客戶端，或透過 REST API、Python/Go/TypeScript SDK、CLI 與 Docker 映像整合到自有系統。所有版本皆內建 VLM+OCR 雙引擎，支援 109 語言的文字識別。  

 **高精度多格式解析，版面與閱讀順序保持一致**  
原生支援 DOCX、PPTX、XLSX 的結構化解析；公式自動轉 LaTeX、表格轉 HTML；可處理掃描文件、手寫文字、多欄排版以及跨頁表格合併。輸出內容遵循人類閱讀順序，並自動移除頁首頁尾。  

🔌 **與主流 AI 框架原生整合**  
內建 MCP Server，可直接被 Cursor、Claude Desktop、Windsurf 等 AI 編程工具調用。同時提供 LangChain、LlamaIndex、RAGFlow、RAG-Anything、Flowise、Dify、FastGPT 的原生適配，使開發者在構建 RAG 或 Agent 時免除額外的資料前處理步驟。  

⚠️ **依賴社群維護與硬體適配度仍需觀察**  
目前文件顯示支援國產 AI 晶片（Ascend、Cambricon、Enfla），但實際效能與穩定度尚未在大規模生產環境中長期驗證；此外，作為工具類專案，其核心技術屬於現有 VLM/OCR 與文件解析庫的整合，而非基礎算法突破。  

🎯 **適合需要快速將非結構化文件納入 LLM 流程的團隊**  
- 若您正在構建內部知識庫、客服機器人或代理系統，可直接呼叫 MinerU API 取得結構化輸出。  
- 對於希望在本地或完全離線環境運作的團隊，桌面客戶端與 Docker 映像提供免安裝、免佈署的選項。  
- 開發者可透過 MCP Server 與主流 AI 編程工具無縫串接，減少「資料準備」的重複勞動。  

🔗 **專案連結**  
📂 opendatalab/MinerU  
🔗 https://github.com/opendatalab/MinerU  

你有試過用 MinerU 把 PDF 轉成 LLM 可直接 ingest 的格式嗎？歡迎在留言區分享你的使用經驗 👇  

#MinerU #文件解析 #LLM #RAG #Agent #opendatalab #AI工具 #開源專案
