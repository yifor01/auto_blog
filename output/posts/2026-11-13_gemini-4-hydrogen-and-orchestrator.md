---
title: Gemini 4 Hydrogen and Orchestrator
source: Hacker News
url: https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity/
model: claude-code/sonnet
generated_at: '2026-11-13T22:44:52.288457'
score: 101
---

📌 【Google DeepMind】不用猜模型該多聰明：Orchestrator 讓 Carbon 與 Hydrogen 邊做邊換手

TL;DR：Antigravity 新增 Orchestrator，在單一任務中動態切換 Gemini 4 Carbon 與 Hydrogen。

多數人對「模型路由」的想像，是看一眼你的第一句 prompt，猜你的任務有多難，然後把整個任務丟給夠用的最便宜模型。Google Antigravity 團隊認為這種做法在任務拉長後會失靈，於是推出了 Orchestrator。

🤔 **靜態路由器為什麼會「開始的時候猜對，後面就垮掉」**

素材指出，常見的業界做法是用一個靜態「model router」，根據你的第一個 prompt 猜任務難度，然後把整個任務路由給一個「夠用的最便宜模型」。問題是，隨著 agent 執行時間變長，任務在不同階段需要的能力等級會不一樣,而這往往是任務跑到一半才會暴露出來的,靜態路由器無法應對這種「中途變難」的情況。

🧩 **Carbon 探路、Hydrogen 動手，卡住了再換回來**

Orchestrator 的做法是在同一條任務軌跡（trajectory）裡,讓 Carbon 和 Hydrogen 做雙向動態切換：

- Carbon 先進入只讀階段，探索相依關係、解決模糊之處，並建立一份附帶明確「重新規劃觸發點」的具體計畫。
- Hydrogen 接手執行寫入類工作：修改程式碼、更新套件、跑測試。
- 如果 Hydrogen 執行中遇到阻礙，就把控制權交還給 Carbon,讓它檢查現狀、修復計畫後再把任務交回來繼續執行。

這週早些時候，Google 先發布了 Gemini 4 Carbon 與 /swarm 功能，用於處理需要多個 worktree、平行 agent 團隊的大型工程任務；素材提到短短幾天內 Antigravity 上已經啟動了數萬次 swarm。Orchestrator 則是針對「日常功能開發與除錯」這類單一 session 場景,因為對每一步都動用前沿推理模型加多個平行 agent,會拖慢迴圈速度並消耗前沿模型的配額。

除了在模型選單直接選 Orchestrator，開發者也可以透過 Antigravity SDK 自行寫出明確的多模型 pipeline。素材展示的範例是一套開源議題分級（issue triage）系統：Hydrogen agent 負責分級與編碼,處理進來的議題量、搜尋程式碼庫、提出澄清問題，並根據 PR 留言快速迭代 UI；Carbon agent 則被指派處理較大型的重構、新功能與安全檢查。

📊 **Terminal-Bench 4.1：接近 Carbon 的成功率,配額省 24%、速度快 19%**

在 Terminal-Bench 4.1 上，Orchestrator 達到接近 Carbon 單獨執行的任務成功率，同時平均少消耗 24% 配額、完成速度快 19%。

單獨使用 Hydrogen 時，它在 Artificial Analysis Intelligence Index 拿下 51 分（最高設定下可到 54），超過 Argon 的 50 分；在 Terminal-Bench 4.1 拿下 57%，是 Gemini 3.8 Flash 的 18.2% 的三倍以上。使用 Hydrogen 時可調整四個思考深度等級：low、medium、high（預設）,以及新增的 xhigh。

🎯 **實務啟示**

如果你的 agent 任務是「短 session、多步驟但任務難度會中途變化」,Orchestrator 這種「單一 prompt 背後動態換模型」的設計，比起自己手刻一個難度分類器再路由，可能是更省事的起點；若你需要完全掌控哪個角色該用哪個模型，Antigravity SDK 開的明確 pipeline 介面也值得評估。

🔗 **來源**
- 標題：Gemini 4 Hydrogen and Orchestrator
- 作者／機構：jonbaer（Hacker News，原文為 The Antigravity Team）
- 連結：https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity/

#Gemini #GoogleDeepMind #AIAgents #Antigravity #LLM #MultiAgent #Coding #DeveloperTools #AIOrchestration #MachineLearning
