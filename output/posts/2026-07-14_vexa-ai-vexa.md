---
title: Vexa-ai/vexa
source: GitHub Trending
url: https://github.com/Vexa-ai/vexa
score: 91
model: tencent/hy3:free
generated_at: '2026-07-14T08:02:02.467759'
---

這是一個開源專案（GitHub），我將依照開源專案的骨架進行撰寫。

📌 【Vexa-ai】開源自託管會議機器人：將會議轉錄與 Agent 工作流整合為「知識即程式碼」

TL;DR：自託管會議機器人，能加入 Meet/Teams/Zoom 並將轉錄內容轉為 Markdown 知識庫。

🤔 **為什麼我們需要 Vexa？**

目前的會議 AI 工具大多採取「雲端租賃」模式：你將對話傳送到對方的雲端，再由對方租回存取權。這種做法讓企業面臨隱私風險。Vexa 採取完全相反的邏輯：透過自託管（Self-hosted）架構，讓開發者能將整套技術棧跑在自己的環境中，並對會議產出的資料擁有完全的所有權。

🧩 **核心架構：從即時轉錄到 Agent 驅動的知識庫**

Vexa 的設計理念是將「會議」轉化為「可管理的程式碼」，其工作流程如下：

1.  **機器人加入會議**：一個真實的機器人會加入 Google Meet、Microsoft Teams 或 Zoom。
2.  **即時轉錄 API**：機器人會將帶有說話者標記（speaker-attributed）的逐字稿，透過你自行架設的 API 進行即時串流。
3.  **知識庫轉化**：會議內容會被整理成 Markdown 格式，並儲存在 Git 儲存庫中。這使得知識變得「可移植、可進行 diff 比較、可使用 grep 搜尋」，實現了「知識即程式碼」（Knowledge as code）的理念。
4.  **沙盒化 Agent 運作**：專用的 Agent 可以在隔離的容器（如 Docker 或 Kubernetes）中執行，像開發者一樣讀取並寫入該 Git 儲存庫。這些 Agent 執行在臨時容器內，且具備無出口（no egress）的特性，確保安全性。

🛠️ **靈活的開發者選項**

- **獨立轉錄 API**：如果你只需要轉錄功能，可以將其視為一個獨立產品，直接傳送機器人並讀取串流，完全跳過 Agent 流程。
- **部署彈性**：支援在 Docker 或 Kubernetes 上部署，並具備支援離線環境（air-gap-ready）的能力。

🎯 **實務啟示**

對於對隱私極度敏感、且希望將會議記錄與現有開發工作流（如 Git）深度整合的團隊來說，Vexa 提供了一種全新的思維：不再只是「與檔案對話」，而是將會議直接轉化為結構化的、可由 Agent 安全操作的程式碼資產。

🔗 **來源**
- 標題：Vexa-ai/vexa
- 連結：https://github.com/Vexa-ai/vexa

#Vexa #OpenSource #SelfHosted #MeetingAI #Transcription #LLM #AgenticWorkflow #Markdown #DeveloperTools #PrivacyPreserving
