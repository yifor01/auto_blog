---
title: 'Meet Alibaba’s Page Agent: A JavaScript In-Page GUI Agent That Controls Web
  Interfaces With Natural Language Through the DOM'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/02/meet-alibabas-page-agent-a-javascript-in-page-gui-agent-that-controls-web-interfaces-with-natural-language-through-the-dom/
score: 92
model: google/gemma-4-31b-it:free
generated_at: '2026-07-03T19:54:37.726531'
---

📌 【Alibaba 開源】Page Agent：將 LLM 代理內嵌於頁面，直接透過 DOM 操控 Web 介面

TL;DR：一個以 TypeScript 實作的客戶端函式庫，讓 AI 代理以純 JavaScript 形式執行在頁面內，直接操作 DOM 並繼承使用者 session。

大多數的瀏覽器自動化工具（如 Playwright, Puppeteer, Selenium 或 browser-use）都是從「外部」驅動瀏覽器，透過截圖或 Chrome DevTools Protocol 來讀取頁面。但阿里巴巴推出的 Page Agent 採取了完全相反的路徑：它直接住在網頁裡面。

🤔 **擺脫外部驅動，讓 AI 成為「真正的使用者」**

Page Agent 是一個基於 TypeScript 的開源專案（MIT 授權），它將 AI 代理定義為一個客戶端函式庫。開發者將其內嵌到 Web App 中後，使用者即可透過自然語言下達指令。

由於代理直接執行在瀏覽器會話（Browser Session）中，它具備一個關鍵優勢：直接繼承使用者的 cookies、session 與身份驗證狀態。這意味著開發者不需要額外撰寫後端邏輯，且原有的 UI 驗證與安全規則依然有效。

🧩 **核心技術：透過 DOM Dehydration 降低模型成本**

現代網頁包含數千個節點，若將原始 HTML 全部傳送給 LLM 會導致速度緩慢且成本極高。Page Agent 採用了名為「DOM Dehydration」的技術來解決此問題：

1. **掃描與識別**：當指令到達時，代理會掃描 DOM 並識別所有互動元素（如按鈕、連結、輸入框）。
2. **標記與簡化**：為每個元素分配索引（Index）、角色（Role）與標籤（Label）。
3. **轉換為 FlatDomTree**：將活生生的 DOM 轉換為一個精簡的文本對映表（FlatDomTree），剔除冗餘的標記。

最終，模型讀取的是這份精簡的文本表示法而非畫素，因此不需要多模態模型（Multi-modal model），只要強大的純文字模型即可運作。

💡 **模型無關設計與模組化架構**

Page Agent 的設計並不綁定特定模型，工程師可以透過任何相容於 OpenAI 的端點（Endpoint）接入自選的 LLM。

在實作架構上，該專案採用 monorepo 管理，將職責拆分為小型套件。其中 `@page-agent/core` 負責核心邏輯，並透過一個 `PageController` 來委派具體操作。此外，其 DOM 處理流程與 Prompt 設計是基於 browser-use 衍生而來。

🎯 **實務啟示**

對於想要為 Web App 增加 AI 操控能力的工程師來說，Page Agent 提供了一種低門檻的整合方式。由於它不需要 headless browser 或複雜的截圖分析流程，只要能將其內嵌至前端並對接 LLM API，就能實現讓 AI 幫使用者點選按鈕或填寫表單的功能，且無需處理繁瑣的身份驗證同步問題。

🔗 **來源**
- 標題：Meet Alibaba’s Page Agent: A JavaScript In-Page GUI Agent That Controls Web Interfaces With Natural Language Through the DOM
- 作者／機構：Asif Razzaq
- 連結：https://www.marktechpost.com/2026/07/02/meet-alibabas-page-agent-a-javascript-in-page-gui-agent-that-controls-web-interfaces-with-natural-language-through-the-dom/

#AI #LLM #TypeScript #DOM #BrowserAutomation #OpenSource #Alibaba #WebDevelopment #JavaScript #Agent
