---
title: topoteretes/cognee
source: GitHub Trending
url: https://github.com/topoteretes/cognee
score: 107
model: tencent/hy3:free
generated_at: '2026-07-20T08:48:18.576952'
---

📌 【topoteretes 開源】Cognee：讓 AI 代理擁有跨會話的長期記憶

TL;DR：Cognee 是開源 AI 記憶體平臺，用知識圖譜為代理提供自託管持久記憶。

你家的 AI 代理每次新對話就失憶，上下文全得重喂？Cognee 想把這件事解決：讓代理在不同 session 之間記得住、連得起、還能行動。

🤔 **代理缺少跨會話的持久記憶**

README 指出，Cognee 是開源 AI memory platform，目標是給 AI agents 提供 persistent long-term memory across sessions。也就是說，代理不再每次從零開始，而是能延續過往累積的知識與脈絡。

🧩 **向量、圖推理與本體生成三合一**

Cognee 的設計理念結合了三項技術：
- vector embeddings：讓檔案能按語意搜尋
- graph reasoning：用關係連線資料，且會隨知識演進
- cognitive-science-grounded ontology generation：基於認知科學的本體生成

使用者能以任意格式 ingest 資料，平臺會持續建置一個 self-hosted knowledge graph，使檔案同時可被語意檢索、也被關係串聯。

🔌 **多種客戶端與外掛整合方式**

README 提到 Cognee 提供多種接入形式，方便不同環境的開發者使用：
- OpenClaw 外掛：cognee-openclaw
- Claude Code 外掛：claude-code-plugin
- Rust 客戶端：cognee-rs
- TypeScript 客戶端：@cognee/cognee-ts

此外，官方也提及可用來「Easily Build Company Brain」，統一來自多處的資料（摘要於此截斷，細節未提供）。

🎯 **實務啟示**

若你正在開發需要長期脈絡的 agent 系統，Cognee 提供了一個自託管、開源的記憶體層選項，不必從頭刻知識圖譜與向量檢索。先從官方檔案與其中一個客戶端（如 TypeScript 或 Rust）試接，評估是否能取代現有的上下文重喂流程。

🔗 **來源**
- 標題：topoteretes/cognee
- 作者／機構：topoteretes
- 連結：https://github.com/topoteretes/cognee

#AI #Agents #Memory #KnowledgeGraph #OpenSource #Cognee #VectorEmbeddings #GraphReasoning #Ontology #SelfHosted
