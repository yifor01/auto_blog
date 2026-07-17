---
title: browseros-ai/BrowserOS
source: GitHub Trending
url: https://github.com/browseros-ai/BrowserOS
score: 97
model: tencent/hy3:free
generated_at: '2026-07-17T08:09:36.961346'
---

📌 【開源專案】BrowserOS：讓 AI 代理操作你已登入的瀏覽器帳號

TL;DR：BrowserOS 推出開源 Chromium 分支，供 AI 代理驅動已登入帳號並即時觀看重播。

你的 AI 再聰明，遇到登入畫面也只能停下來——它沒辦法幫你按按鈕、過驗證。BrowserOS 想用一個開源瀏覽器把這道牆打掉。

🤔 **AI 卡在登入畫面，是自動化的斷點**

README 指出，現今 AI 助手能規劃任務，但「book a flight、download an invoice、reply to an email」等操作都會停在登入關卡。BrowserClaw 的設計目標就是補上這個缺口：讓 AI 代理用你既有的帳號身分去實際執行網頁操作。

🧩 **兩款瀏覽器，同一套程式碼基底**

BrowserOS 專案包含兩個面向，但共用一個 codebase：
- BrowserOS：給人類用的 AI 瀏覽器，內建 AI agent，標榜為 ChatGPT Atlas、Perplexity Comet、Dia 的隱私優先開源替代方案。
- BrowserClaw：給 AI 代理用的瀏覽器，讓 Claude Code、Codex、Cursor 或任何 MCP 客戶端驅動你已登入的帳號。

專案採 AGPL-3.0 授權，強調免費、開源、local-only，並支援自帶 AI keys（bring your own AI keys）。

🧩 **BrowserClaw 怎麼串接你的 AI**

README 描述的最小流程如下：
1. 安裝 BrowserClaw，像一般瀏覽器一樣登入你常用的網站；每個登入的帳號都變成 AI 可使用的身分。
2. 一鍵連線 AI：Claude Code、Codex、Cursor、VS Code、Zed、OpenCode、Antigravity 支援單鍵安裝；其他任何支援 MCP 的客戶端用一個 URL 即可連線。
3. 下達真實任務：例如在 AI 聊天中說「Find a good time next week for a 30-minute team meeting and send the invite」，隨後在專屬分頁中即時觀看代理操作，也能像看影片一樣重播任何 session。

⚠️ **限制與適用邊界**

素材僅說明 BrowserClaw 為 local-only 且需自帶 AI 金鑰，未提及支援的作業系統範圍、具體效能表現或與商業方案的功能差異細節。隱私聲稱（privacy-first）來自專案自我定位，實際資安模型未在摘要中展開。

🎯 **實務啟示**

對工程師而言，若你已在用 Claude Code 或 Cursor 等 MCP 客戶端，BrowserClaw 提供了一個不需另建登入流程的本地沙盒：把日常網站帳號交給代理執行繁瑣操作，同時保留即時監看與重播能力。在評估 ChatGPT Atlas 等閉源 AI 瀏覽器時，這是個可自架、可審計的開源選項。

🔗 **來源**
- 標題：browseros-ai/BrowserOS
- 作者／機構：browseros-ai
- 連結：https://github.com/browseros-ai/BrowserOS

#BrowserOS #BrowserClaw #OpenSource #Chromium #AIAgent #MCP #LocalOnly #PrivacyFirst #AGPL #BrowserAutomation
