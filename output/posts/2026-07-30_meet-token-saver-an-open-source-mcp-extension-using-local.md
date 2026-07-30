---
title: 'Meet Token Saver: An Open-Source MCP Extension Using Local Hybrid RAG to Cut
  Claude PDF Token Costs 90-99%'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/30/token-saver-an-open-source-mcp-extension-using-local-hybrid-rag/
model: tencent/hy3:free
generated_at: '2026-07-30T08:18:23.997575'
score: 105
---

📌 【開源專案】Token Saver：利用本地 Hybrid RAG，讓 Claude 分析 PDF 的 Token 成本降低 90-99%

TL;DR：這款開源 MCP 擴充功能透過本地 RAG 技術，讓 Claude 無須讀取整份文件即可回答問題，大幅節省 Token 消耗並保護隱私。

🎣 **每一次對話，都在重複支付昂貴的「上下文成本」**

當你在 Claude 中貼上一個 200 頁的 PDF 時，這並非一次性的費用。由於對話歷史會在每一輪對話中重新傳送給模型，這份龐大的文件會隨著你的每一個後續問題，反覆消耗大量的 Token 費用。此外，Claude 預設會將每一頁轉換為圖片以保留圖表與版面，單是文字部分，每頁就可能消耗 1,500 到 3,000 個 Token。

🧩 **Token Saver：讓 PDF 留在你的硬碟裡**

Token Saver 是一個針對 Claude Desktop 開發的開源 MCP (Model Context Protocol) 擴充功能 (v1.0, MIT 授權)，其核心設計理念是將檢索工作從雲端移回本地端。

- **本地 Hybrid RAG 架構**：透過在使用者電腦上運行的本地混合檢索技術 (Local Hybrid RAG)，Claude 僅會檢索與問題相關的片段，而非將整份文件傳送給模型。
- **MCP Server 運作模式**：它作為一個輕量級的背景程式，讓 Claude 能將其視為一個「工具 (tool)」來呼叫，從而實現「不需上傳檔案」即可進行問答。
- **零環境配置**：使用者不需要安裝 Python 環境或進行複雜的終端機 (terminal) 設定。

📊 **大幅降低成本並解決幻覺問題**

- **節省 Token 成本**：根據開發者測試，Token 消耗量可降低 92% 到 99%。
- **提升精準度**：若強迫 LLM 在 1,000 頁的教科書中自行搜尋，不僅效率低下且容易產生幻覺 (hallucination)；使用 Token Saver 則能精準定位相關段落。
- **隱私保障**：由於 PDF 檔案從未離開過使用者的硬碟，資料安全性得到保障。

🎯 **實務啟示**

對於需要頻繁處理長篇技術文件或法律文件的開發者與研究人員來說，這是一個極具價值的工具。它不僅解決了 Context Window 帶來的經濟壓力，更透過將檢索重心轉移至本地，在效能與隱私之間取得了平衡。

🔗 **來源**
- 標題：Meet Token Saver: An Open-Source MCP Extension Using Local Hybrid RAG to Cut Claude PDF Token Costs 90-99%
- 作者／機構：Arnav Rai, Jean-marc Mommessin and Asif Razzaq @ Marktechpost AI Media Inc
- 連結：https://www.marktechpost.com/2026/07/30/token-saver-an-open-source-mcp-extension-using-local-hybrid-rag/

#AI #MCP #Claude #RAG #OpenSource #LLM #Productivity #TokenOptimization #Privacy #MachineLearning
