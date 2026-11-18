---
title: New LoRA Adapter Lifts Qwen3.8 Coding Success From 39% to 65%
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/18/hugging-face-qwen3-8-27b-pi-adapted-lora/
model: claude-code/sonnet
generated_at: '2026-11-18T23:40:16.752890'
score: 97
---

📌 一片 LoRA,把 Qwen3.8-27B 在 coding agent 裡的勝率從 39% 推到 65%

TL;DR:Hugging Face 針對 pi coding agent 訓練出專用 LoRA 轄接器,用強化學習把開源模型調校成「某個 harness 的專家」。

通用對話模型硬套進 coding agent,常常卡在工具呼叫的細節上。Hugging Face 的 harness-hub 團隊給出另一條路:不調整整個模型,只為特定的 agent harness 訓練一片小小的 LoRA 轄接器。

🤔 **一個模型配一個 harness 的轄接器**

Qwen3.8-27B-pi-adapted 是一個 PEFT LoRA 轄接器,套用在開源模型 Qwen3.8-27B 上,目標是讓它在 pi(一套 MIT 授權的 agent 工具組,內含 coding agent CLI)裡表現更好。轄接器本身以 Apache-2.0 授權釋出,作用於 q、k、v、o、gate、up、down 等投影層。它只支援 Qwen3.8-27B 這個基礎模型,而這個基礎模型本身是一個密集混合架構,在 64 層中交替使用 Gated DeltaNet 線性注意力區塊與 Gated Attention 區塊。

這套方法延續 Hugging Face 11 月 6 日發布的 harness adapters 方法論:一個模型配一個 harness,訓練一片轄接器,而且訓練過程直接在未經修改的 harness 裡進行,任務全部是可驗證的。

🧩 **用規則型代理攔截 reward hacking**

訓練時,每一次工具呼叫都會經過 `safeagents`,一個規則型的代理(proxy),會擋下例如「直接去 Hub 上抓 benchmark 答案」這類作弊行為。被擋下的 rollout 直接計 0 分,強化學習因此被推離 reward hacking 的方向。

📊 **解題數上升,輪數大幅下降**

以下數字皆為自行公布,測試皆使用 pi harness、每個任務只跑一次:

- SWE-bench Pro:新解出 15 題,反而失手 2 題。
- Terminal-Bench 2.1:新解出 16 題,失手 2 題。
- 在兩個模型都解得出的任務上,SWE-bench Pro 的中位數對話輪數從 59 降到 23,Terminal-Bench 2.1 從 18 降到 8。
- 轄接器生成的 token 數量,比開啟 thinking 模式的基礎模型少了約 4.5 倍。

值得注意的是,開啟 thinking 模式的基礎模型本身已經有 64.7%(SWE-bench Pro)與 54.2%(Terminal-Bench 2.1)的分數;而這片轄接器在開啟 thinking 後進一步達到 66.7% 與 56.6%——也就是說,它用遠少於長推理鏈的 token 成本,達到甚至超過 thinking 模式的準確率。(文章另有引用的 OpenCode 轄接器數字,使用不同 harness 測得,不能直接拿來比較。)

💡 **轄接器可以共用同一個底座模型伺服**

模型卡提供了 4 種使用路徑,但更值得留意的設計意義是:因為所有 harness 專用轄接器共享同一個基礎模型,一臺伺服器就能同時掛載 pi 與 OpenCode 的轄接器,依請求來源切換,不需要為每個 harness 各跑一份完整模型。

⚠️ **限制**

轄接器僅對 Qwen3.8-27B 生效,換一個基礎模型就需要重新訓練;而且它是針對 pi harness 最佳化的,跨 harness 的數字並不直接可比。

🎯 **對工程師的意義**

如果你在本機跑開源模型做 coding agent,這個案例提供了一個具體方向:與其等通用模型進化,不如針對自己實際用的 harness,用強化學習訓練一片小轄接器——保留開源底座模型,只替換少量參數,就能換來明顯的效率與解題率提升。

🔗 **來源**
- 標題:New LoRA Adapter Lifts Qwen3.8 Coding Success From 39% to 65%
- 作者/機構:Asif Razzaq, MarkTechPost
- 連結:https://www.marktechpost.com/2026/11/18/hugging-face-qwen3-8-27b-pi-adapted-lora/

#LoRA #CodingAgent #ReinforcementLearning #OpenSource #Qwen #HuggingFace #SWEBench #PEFT #LLM #AIAgents
