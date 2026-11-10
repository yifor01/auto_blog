---
title: TPU 8tx and TPU 8i Max
source: Hacker News
url: https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/
model: claude-code/sonnet
generated_at: '2026-11-10T01:01:31.979450'
score: 87
---

📌 Google 一年內推出四款 TPU：8tx 主攻機密推理，8i Max 衝刺超長 Context

TL;DR：Google 擴充第八代 TPU 陣容，新增 TPU 8tx 與 TPU 8i Max，分別解決機密運算與記憶體頻寬瓶頸，瞄準正在興起的 agentic 工作負載。

當 AI agent 開始連續執行數十個步驟，同時碰觸企業最敏感的資料，或是處理數小時長的影片內容時，基礎設施的瓶頸已經不只是算力，而是「安全」與「記憶體」。Google 這次一口氣交出兩款新系統來回應這個現實。

🤔 **一年四款系統，背後是 agent 時代的新需求**

Google 今年四月已推出 TPU 8t（訓練）與 TPU 8i（推理），這次新增的 8tx 與 8i Max 是同一年內的第四、第五款系統配置。Google 表示目前 TPU 業務已有近 100 家客戶，涵蓋 frontier labs、trading firms、零售商與大學等，而隨著運算從「人類尺度」走向「agent 尺度」，企業開始要求能跨越模型巨大 context window 進行推理的加速器，以及能滿足特定加密需求的合規方案，這正是兩款新系統的設計起點。

🧩 **重點不是新晶片，是重新組裝系統**

Google 特別強調「新晶片」與「新系統」的差異：設計一顆新晶片是數年等級、受物理與製程限制的工程；而「系統」指的是如何把運算、網路與儲存組合在晶片周邊。TPU 8tx 沿用與 TPU 8t 相同的晶片，搭配第五代 AMD EPYC CPU 主機，並採用原本為 TPU 8i 打造的低延遲 Boardfly 網路，把加密能力直接內建在硬體層，讓資料與模型權重即使在運算中「使用時」也能保持加密隔離。TPU 8i Max 則是把兩顆低延遲的 TPU 8i 晶片封裝進同一個模組，直接針對「記憶體牆」問題，讓運算與記憶體同步擴充。

📊 **官方揭露的效能提升幅度**

- TPU 8t／8i（今年四月基準）：相較前一代 TPU，訓練效能提升最多 2.7 倍，推理性價比提升 80%。
- TPU 8i：把晶片間通訊延遲縮短最多一半。
- TPU 8tx：相較 TPU 8t，延遲降低最多 2 倍，且幾乎沒有效能損失。
- TPU 8i Max：相較 TPU 8i，運算力、SRAM 與 HBM 頻寬皆倍增，同樣機架空間可塞入兩倍矽晶圓面積。

💡 **十年前的一個賭注：模組化比晶片更快演進**

Google 表示，第一代 TPU 設計時就判斷軟體演進速度會遠快於晶片製造週期，因此把 TPU 當作 AI Hypercomputer 的建構區塊，讓封裝、高速記憶體、光纖網路與安全機制都能快速調整組合。這個哲學讓 Google 能用數月而非數年交付新規格的超級電腦，這也解釋了為何同一代矽晶圓能在一年內衍生出四種系統。配合近期的 PyTorch 支援與開源工具，Google 的目標是讓更多開發者能直接用熟悉的工具鏈上手 TPU。

🎯 **給工程團隊的選型提示**

面對四款系統，選型邏輯其實相對清晰：大規模訓練用 TPU 8t；低延遲即時推理用 TPU 8i；需要在同一叢集內對敏感資料做 fine-tune、distill 或強化學習而不想搬移資料，選 TPU 8tx；面對多 agent 協作或跨整個程式碼庫的超長 context 需求，則看 TPU 8i Max。對正在規劃 agentic 系統基礎設施的團隊，這種「依工作負載分流硬體」的思路值得參考。

🔗 **來源**
- 標題：TPU 8tx and TPU 8i Max
- 作者／機構：Amin Vahdat（SVP and Chief Technologist, AI and Infrastructure, Google）
- 連結：https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/

#GoogleCloud #TPU #AIInfrastructure #AgenticAI #ConfidentialComputing #AIHardware #CloudComputing #MachineLearning #LLMInference #DataCenter
