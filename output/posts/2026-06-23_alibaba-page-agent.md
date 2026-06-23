---
title: alibaba/page-agent
source: GitHub Trending
url: https://github.com/alibaba/page-agent
score: 116
model: google/gemma-4-31b-it:free
generated_at: '2026-06-23T20:23:59.336893'
---

📌 【Alibaba 開源】Page Agent：無需瀏覽器擴充功能，用 JavaScript 直接在頁面內實現 GUI 自動化

TL;DR：一個僅需匯入 JS 即可讓網頁支援自然語言控制的 GUI Agent，無需 Headless Browser 或多模態模型。

大多數的 Web Agent 為了操作網頁，通常需要部署複雜的 Headless Browser（如 Playwright/Puppeteer）或安裝瀏覽器擴充功能，這不僅增加了開發成本，還面臨許可權與部署的挑戰。Alibaba 開源的 Page Agent 則採取了完全不同的路徑：將 Agent 直接「住」在網頁裡。

🧩 **純 JavaScript 實作，擺脫後端環境依賴**

Page Agent 的核心設計理念是簡化整合流程，讓 AI 控制介面的過程直接發生在前端頁面中：
- **無環境依賴**：不需要 Python、不需要瀏覽器擴充功能，也不需要 Headless Browser。
- **純文字 DOM 操作**：不依賴螢幕截圖或多模態 LLM (Multi-modal LLMs)，而是透過文字形式的 DOM 操作來控制介面，因此不需要特殊許可權。
- **靈活的模型選擇**：支援 Bring your own LLMs，開發者可以根據需求接接不同的語言模型。

🚀 **從單頁操作到跨分頁控制**

Page Agent 根據應用場景提供了兩種操作模式：
- **單頁面模式**：直接在頁面內執行，適合快速整合 AI Copilot 或自動化表單填寫。
- **跨頁面模式**：提供選配的 Chrome 擴充功能，讓 Agent 的能力延伸至不同的瀏覽器分頁。
- **外部控制**：提供 Beta 版本的 MCP Server，允許外部 Agent 客戶端控制瀏覽器。

💡 **三大實務應用場景**

- **SaaS AI Copilot**：無需重寫後端，僅用幾行程式碼即可在產品中內建 AI 助手。
- **智慧表單填寫**：將 ERP、CRM 或管理系統中繁瑣的 20 次點選流程，簡化為一句自然語言指令。
- **提升無障礙體驗 (Accessibility)**：透過自然語言、語音指令或螢幕閱讀器，降低使用網頁應用的門檻。

🎯 **實務啟示：低門檻的 GUI 自動化方案**

對於工程師而言，Page Agent 的最大價值在於「極低的整合成本」。如果你的目標是為現有 SaaS 產品增加 AI 操控能力，而不想為了部署 Playwright 等工具而重新設計後端架構，這種純前端的實作方式提供了一個快速驗證（PoC）的方案。

🔗 **來源**
- 標題：page-agent
- 作者／機構：Alibaba
- 連結：https://github.com/alibaba/page-agent

#AI #GUIAgent #OpenSource #JavaScript #Alibaba #WebAutomation #LLM #SaaS #Accessibility #MCP
