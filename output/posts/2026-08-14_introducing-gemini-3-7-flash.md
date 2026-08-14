---
title: Introducing Gemini 3.7 Flash
source: Google DeepMind
url: https://deepmind.google/blog/introducing-gemini-3-7-flash/
model: claude-code/sonnet
generated_at: '2026-08-14T07:20:18.091654'
pinned: true
---

📌 【Google DeepMind】Gemini 3.7 Flash 上線，價格砍半、程式碼能力全面提升

TL;DR：距上一代僅三週，Gemini 3.7 Flash 用一半價格帶來更強的 coding 與 agent 表現。

一款主打「workhorse」的模型，距離上一代發布只隔了三週就再度更新，這在模型迭代節奏上並不常見。Google DeepMind 表示，Gemini 3.7 Flash 是「開發者反饋加上演算法創新」的直接成果，並將以先前一半的每百萬 token 價格作為引進期定價推出。

🤔 **Flash 系列的定位：coding 與 agent 的工作馬**

Google DeepMind 產品管理資深總監 Tulsee Doshi 在文章中指出，3.7 Flash 延續 Flash 系列一貫的定位，鎖定軟體工程、知識工作與網頁開發等工作流程，目標是成為目前最聰明的一款「工作馬」模型。

📊 **跨領域基準測試全面優於前代**

依官方公布的數據：

| Benchmark | 測試內容 | 3.7 Flash | 3.6 Flash |
|---|---|---|---|
| FrontierCode 1.1 Main | 程式碼生成 | 43.6% | 34.4% |
| DeepSWE v1.1 | 軟體工程任務 | 65.3% | 49.0% |
| WebDev Arena（Elo） | 網頁開發對戰 | 1588 | 1538 |
| GDP.pdf | 複雜文件處理 | 34.0% | 22.0% |
| AutomationBench | 真實商業工作流程 | 30.4% | 17.0% |

Google DeepMind 說明，3.7 Flash 在除錯與 issue 解決等 coding 任務上有明顯進步，首次生成的程式碼準確度更高，產出的程式碼也更接近可直接上線的品質；在網頁開發上，模型能用更少的 prompt 生成功能更完整的版面與應用程式，並在依據截圖、圖片或完整設計系統還原介面時展現高度的設計一致性；在金融、法律、生醫等知識密集領域，模型的推理與準確度也有提升。

🧩 **更懂得配合開發者，而不只是更聰明**

文章特別提到，3.7 Flash 在開發者體驗上的進步同樣值得關注：它更能應對卡關情境、在需要時主動釐清使用者意圖、更精確地遵循指令，並在多步驟規劃與工具呼叫上投入更多「思考」，帶來更少的人工介入與重試次數。這款模型也將從今天起套用到 Gemini Spark——面向 Google AI Pro 與 Ultra 訂閱者、於超過 160 個國家提供的 24 小時個人 agent，帶來更佳的 Google Workspace 工具使用準確度，能更有效率地整理檔案、草擬郵件、更新狀態文件等多技能工作流程。

⚠️ **同步更新的安全防護**

Google DeepMind 表示，3.7 Flash 上線時同步強化了針對化學、生物、放射性與核能（CBRN）以及網路攻擊濫用情境的安全防護措施，同時仍致力於保留正向用途的可用性，詳細內容可參考官方發布的模型卡。

🎯 **實務啟示**

對正在評估 coding 與 agent 場景成本效益的工程團隊來說，3.7 Flash 以「一半價格＋多項 benchmark 提升」的組合定位為高性價比選項：開發者可透過 Google Antigravity、Gemini API（Google AI Studio、Android Studio）直接試用，企業則可透過 Gemini Enterprise Agent Platform 與 Gemini Enterprise app 存取，適合用來評估是否能以更低成本規模化生產環境中的 agent 工作流程。

🔗 **來源**
- 標題：Introducing Gemini 3.7 Flash
- 作者／機構：Tulsee Doshi／Google DeepMind
- 連結：https://deepmind.google/blog/introducing-gemini-3-7-flash/

#GoogleDeepMind #Gemini #GeminiFlash #AICoding #LLM #AgenticAI #WebDevelopment #AIPricing #GeminiSpark #ModelRelease
