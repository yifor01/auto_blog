---
title: HKUDS/CLI-Anything
source: GitHub Trending
url: https://github.com/HKUDS/CLI-Anything
score: 88
model: google/gemma-4-31b-it:free
generated_at: '2026-06-29T20:32:23.298154'
---

📌 【HKUDS 開源】CLI-Anything：將所有軟體轉化為 AI Agent 原生介面

TL;DR：透過建立 CLI 橋接層與 Hub 管理機制，讓 AI Agent 能直接操作各種軟體並產出實體成果。

目前的軟體設計邏輯是「服務人類」，但未來的使用者將是 AI Agent。然而，Agent 如何精準地操作複雜的專業軟體？這正是 CLI-Anything 試圖解決的斷層。

🧩 **將軟體「Agent 化」的橋接方案**

CLI-Anything 的核心理念是將各種軟體封裝成 Agent 易於理解與呼叫的命令列介面 (CLI)。透過這種方式，無論是 Pi、OpenClaw、nanobot、Cursor 或 Claude Code 等不同的 AI Agent，都能透過統一的命令列操作，直接驅動底層軟體。

🛠️ **透過 CLI-Hub 快速擴充能力**

專案提供了一個名為 CLI-Hub 的管理機制，讓社群能共同建構並分享軟體介面：
- **安裝與管理**：使用者可透過 `pip install cli-anything-hub` 安裝，隨後使用 `cli-hub install <name>` 即可瀏覽並安裝社群開發的 CLI。
- **社群貢獻**：開發者可以透過提交 Pull Request (PR) 將自己開發的 CLI 加入 Hub，更新後會立即生效。
- **擴充套件路徑**：若有特定軟體需求，使用者可提交 wishlist 請求，或申請成為貢獻者來建構新的 CLI harness。

📊 **從 CAD 到地圖：實作的產出成果**

根據專案展示，AI Agent 在使用這些生成的 CLI 後，能配合預覽、即時預覽與軌跡迴圈 (trajectory loops) 來產出實際的成品，包括：
- CAD 建模、3D 場景、圖表、遊戲玩法、字幕等。
- 近期更新中，社群已提出 ArcGIS Pro 的支援（Windows/ArcPy CLI），可用於製圖、地理處理、要素編輯以及 live-Pro MCP 工作流。

🎯 **實務啟示**

對於 AI 工程師而言，這個專案提供了一種將「傳統軟體」轉化為「Agent 工具」的標準化路徑。與其為每個 Agent 撰寫複雜的 API 整合，不如將軟體能力封裝成標準的 CLI 介面，讓 Agent 透過指令直接操作，能大幅降低 AI 與專業工具之間的整合成本。

🔗 **來源**
- 標題：CLI-Anything: Making ALL Software Agent-Native
- 作者／機構：HKUDS
- 連結：https://github.com/HKUDS/CLI-Anything

#AI #AIAgent #CLI #OpenSource #SoftwareEngineering #HKUDS #Automation #DeveloperTools #LLM #Interoperability
