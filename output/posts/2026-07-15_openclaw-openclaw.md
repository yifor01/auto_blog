---
title: openclaw/openclaw
source: GitHub Trending
url: https://github.com/openclaw/openclaw
score: 87
model: tencent/hy3:free
generated_at: '2026-07-15T08:29:53.729102'
---

📌 OpenClaw：本地優先的個人 AI 助手

TL;DR：OpenClaw 讓你在自有裝置跑個人 AI 助手，串接常用聊天頻道，重視隱私與永遠線上。

🎣 開場鉤子
當多數 AI 助手爭相把資料送上雲端，OpenClaw 選擇反向操作：把控制平面與產品都放在你的裝置上，在你的頻道裡就地待命。

🤔 想要本地、單使用者、永遠線上的助手
README 指出，OpenClaw 定位為 personal AI assistant，強調在自有裝置（own devices）上執行。目標使用者是想要一個感覺本地、快速、always-on 的單使用者助手的人，而非團隊或企業多租戶方案。它直接在你已經在用的通道上回答，減少切換成本。

🧩 Gateway 只是控制平面，產品是助手本身
架構設計上，作者明確表示 Gateway 只是控制平面，產品是助手本身。這意味核心價值來自助手本體，而非排程或路由層。助手能在 macOS/iOS/Android 上語音輸入與輸出（speak and listen），並可渲染一個你能控制的 live Canvas。支援的通道極廣，包含 WhatsApp、Telegram、Slack、Discord、LINE、WeChat、QQ、Matrix 等諸多頻道（README 列出完整清單）。

🧩 一條 onboard 指令完成跨平臺初始化
對於新安裝，README 推薦在終端機執行 `openclaw onboard`，它會逐步引導設定 gateway、workspace、channels 與 skills，且適用 macOS、Linux、Windows。Windows 桌面使用者可額外使用原生 Windows Hub 伴隨應用程式，提供設定、托盤狀態、聊天、node mode 與本地 MCP mode。執行環境方面，推薦 Node 24.15+，並可透過 npm、pnpm 或 bun 管理。模型提供商部分，雖支援多家，但檔案建議優先選用你信任且已在使用的提供商之當前旗艦模型；OAuth 訂閱明確提到 OpenAI (ChatGPT/Codex)。

🎯 重視隱私的開發者可從 onboard 起步
若你評估本地優先的 AI 助手符合需求，最直接的行動是克隆專案後執行 `openclaw onboard`，在熟悉的作業系統上完成頻道串接。選擇模型時，依據官方建議採用信任提供商的旗艦模型，可兼顧品質與既有帳務整合。

🔗 來源
- 標題：openclaw/openclaw
- 作者／機構：openclaw
- 連結：https://github.com/openclaw/openclaw

#OpenClaw #AIAssistant #LocalFirst #Privacy #Messaging #Channels #Onboarding #NodeJS #LLM #PersonalAI
