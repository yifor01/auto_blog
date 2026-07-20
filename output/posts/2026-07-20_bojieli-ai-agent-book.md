---
title: bojieli/ai-agent-book
source: GitHub Trending
url: https://github.com/bojieli/ai-agent-book
score: 114
model: tencent/hy3:free
generated_at: '2026-07-20T08:47:56.595576'
---

📌 【開源專案】一本全開源的 AI Agent 實戰書：從公式到程式碼

TL;DR：bojieli 開源《深入理解 AI Agent》全書正文與範例程式碼，含多語言版本。

當大多數 AI Agent 教學停留在概念圖與 Demo 時，有一個 GitHub 倉庫把整本書的正文、配圖與實驗程式碼全部攤開在你眼前——而且還能自己編譯 PDF。

🤔 **這是什麼：一本徹底開源的 Agent 技術書**

bojieli 在 GitHub 上維護的 `ai-agent-book` 倉庫，是《深入理解 AI Agent：設計原理與工程實踐》一書的開源主倉庫。README 指出，全書正文、配圖與配套實驗程式碼全部開源，歡迎讀者把實驗親手跑一遍、提 issue 和 PR。

🧩 **核心架構：Agent = LLM + 上下文 + 工具**

全書圍繞核心公式 `Agent = LLM + 上下文 + 工具` 展開，共十章。README 列出前七章重點如下：

- 第 1 章 · Agent 基礎知識：從「模型即 Agent」的新範式出發，建立核心公式，並引入 Harness 工程（模型之外的一切工程能力）。
- 第 2 章 · 上下文工程：上下文決定 Agent 能力上限，涵蓋大模型 API 上下文結構、KV Cache 友好設計、提示工程、動態提示詞與 Agent Skills、狀態列元資訊、上下文壓縮策略。
- 第 3 章 · 使用者記憶和知識庫：跨會話記住使用者並接入外部知識，含使用者記憶系統、RAG 基礎管道、結構化索引與知識圖譜等。
- 第 4 章 · 工具：工具分類與通用設計原則、MCP 協議、感知／執行／協作三類工具、事件驅動的非同步 Agent。
- 第 5 章 · Coding Agent 與程式碼生成：以生產級 Coding Agent 為例展示完整實現。
- 第 6 章 · Agent 的評估：評估環境、資料集設計、指標體系、統計顯著性、可觀測性、評估驅動選型、生產級內部評估與模擬環境。
- 第 7 章 · 模型後訓練：預訓練、SFT、RL 三階段全景（README 摘要至此截斷，第 8–10 章細節未提供）。

💡 **多語言與自行編譯：社群驅動的開放性**

倉庫提供中文 PDF（原版）、英文、泰米爾語、越南語 PDF，後三者為社群貢獻翻譯，內容可能滯後於中文原版。正文原始碼為 `book/introduction.md`、`book/chapter1.md` 至 `book/chapter10.md` 與 `book/afterword.md`。

若要自行編譯，README 指出需安裝 pandoc、xelatex、ElegantBook 檔案類與相關字型，執行 `cd book && bash build_pdf.sh`；圖表由 `book/gen_*_figs.py` 生成，排版細節見 `book/preamble.tex` 與 `book/*.lua`。

🎯 **實務啟示**

對 AI/ML 工程師來說，這個倉庫把「設計原理」與「工程實踐」繫結在同一份開源內容裡：想動手的人可以直接跑配套程式碼，想深入的人能從 Markdown 正文讀起，甚至自己編譯最新 PDF。若你正在搭建 Agent 系統，第 2 章上下文工程與第 6 章評估方法特別值得優先翻。

🔗 **來源**
- 標題：bojieli/ai-agent-book
- 作者／機構：bojieli
- 連結：https://github.com/bojieli/ai-agent-book

#AI #Agent #LLM #OpenSource #ContextEngineering #RAG #MCP #CodingAgent #Evaluation #Book
