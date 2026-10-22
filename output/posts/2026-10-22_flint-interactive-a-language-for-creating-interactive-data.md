---
title: 'Flint-interactive: A language for creating interactive data visualizations'
source: Microsoft Research
url: https://www.microsoft.com/en-us/research/blog/flint-interactive-a-language-for-creating-interactive-data-visualizations/
model: claude-code/sonnet
generated_at: '2026-10-22T20:44:10.928775'
score: 105
---

📌 Microsoft Research 的 Flint-interactive：讓 AI agent 寫出能「玩」的圖表

TL;DR：Flint-interactive 是一套讓 AI agent 用高階語法就能生成互動式資料視覺化的語言。

AI agent 現在已經很會畫圖表，但畫出來的東西往往只能看，不能摸。放大細節、跨圖表比對、點一下圖就連動反白文件中的相關文字，這些探索式體驗，光靠現成的視覺化函式庫內建互動，往往不夠表達力，也難以客製。

🤔 **問題出在缺一套「描述互動」的語言**

Microsoft Research 團隊（Chenglong Wang、Yuwei Xiao、Alper Sarikaya、Michel Galley、Chris Quirk、Jianfeng Gao）指出，即便是能力強大的前沿模型，要穩定產出高品質互動視覺化仍有明顯的現實落差。根本原因是缺少一套既有表達力又夠高階的語言，來描述「使用者選取了什麼、該觸發什麼視覺反應」這類互動邏輯。

🧩 **編譯器把互動翻譯成語意事件**

Flint-interactive 建立在既有的 Flint 之上，核心是 Flint 的編譯器：它會把使用者（或 agent）的互動行為，翻譯成帶有語意的事件（semantic event），再用高階運算子（operator）去更新視覺呈現，而不是直接操作渲染器底層的圖形元件（mark）。

這個設計把「視覺邏輯」與「互動邏輯」分開：視覺邏輯交給編譯器處理複雜的依賴關係，使用者或 agent 只需要在語意層描述想要的互動，不必自己逆向工程渲染邏輯。因為事件產生與視覺更新都是可組合的，同一套模型也能把圖表和表格、文字、其他圖表、widget 串連起來，建構出互動式資料故事或儀表板。負責追蹤使用者操作並管理渲染狀態的核心元件，是一個稱為 Flint Canvas 的狀態機。

🧩 **三種使用方式**

- 在聊天或 canvas 環境中，透過 Flint-MCP 與 MCP Apps 直接呼叫：告訴 agent 要畫什麼圖、要哪種互動，agent 便能生成 interaction_spec 與 Flint 圖表規格，在對話中直接渲染出互動圖表。
- 用 Flint Interactive Canvas 打造儀表板或資料故事類應用：應用程式透過 event handler 處理 Flint Canvas 送出的語意事件（例如篩選表格、更新另一張圖），也能反向送出 update operator 來控制圖表更新。
- 若要做超出內建預設的「客製互動」，可用 programming API 定義 trigger 與自訂 handler function，把語意事件映射到客製化的圖表更新序列，例如點擊某國家時同時反白並標上名稱，組合 set-style 與 set-annotation，而不需碰觸渲染器專屬的底層標記。

🎯 **實務啟示**

對想做資料視覺化的工程師，Flint-interactive 的價值在於把互動邏輯從「渲染器細節」提升到「語意事件」這個抽象層級，使得無論是人工開發者還是 AI agent，都能更容易描述、維護複雜互動，而不必每次重新發明狀態管理。團隊也開放在 GitHub 提出新的互動 preset，等於邀請社群一起擴充 Flint 的「互動詞彙庫」。

🔗 **來源**
- 標題：Flint-interactive: A language for creating interactive data visualizations
- 作者／機構：Microsoft — Chenglong Wang, Yuwei Xiao, Alper Sarikaya, Michel Galley, Chris Quirk, Jianfeng Gao
- 連結：https://www.microsoft.com/en-us/research/blog/flint-interactive-a-language-for-creating-interactive-data-visualizations/

#MicrosoftResearch #DataVisualization #AIAgent #MCP #InteractiveDashboard #DataJournalism #Compiler #DomainSpecificLanguage #HCI #DataStorytelling
