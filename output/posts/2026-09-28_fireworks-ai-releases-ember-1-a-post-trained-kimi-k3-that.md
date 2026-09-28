---
title: 'Fireworks AI Releases Ember-1: A Post-Trained Kimi K3 That Uses About 40%
  Fewer Tokens'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/28/fireworks-ai-releases-ember-1-a-post-trained-kimi-k3-that-uses-about-40-fewer-tokens/
model: claude-code/sonnet
generated_at: '2026-09-28T22:43:11.548974'
score: 93
---

📌 Fireworks Ember-1：把 Kimi K3 的推理 token 砍掉四成

TL;DR：Fireworks 後訓練 Kimi K3 推出 Ember-1，在準確度打平的前提下少生成約 40% token。

推理模型的帳單痛點往往不在「答錯」，而在「想太多」。Fireworks 團隊觀察到，像 Kimi K3 這樣的推理模型，生成的 token 裡有時超過 90% 花在內部推理上；在多輪 agentic 任務中，這個成本會被放大，因為每一輪都要把先前的推理過程重新餵回模型，context 隨對話輪數大致呈二次成長，早期輪次留下的冗長推理痕跡，會在後續每一次呼叫中被重新讀取、重新計費。

🤔 **調低 effort 設定解決不了問題**

Fireworks 表示，客戶原本想要的是 K3 的程式碼能力，但用更低的成本取得。直覺的做法是調低推理力度（reasoning effort）設定，但團隊發現這樣做犧牲了太多品質。問題的關鍵在於，K3 的推理過程並非全是浪費，其中一部分是有用的自我反思，例如重新檢視假設或針對回饋做出調整。於是 Fireworks 選擇的路線是後訓練模型，讓它學會更有效率地推理，保留有用的自我反思行為，同時砍掉冗餘的推理與無效的重複迴圈。

🧩 **訓練涵蓋的任務範圍與規模**

訓練資料涵蓋數學、程式碼、指令遵循、對話、搜尋、工具使用與軟體工程，同時包含單一問題與延伸的多步驟互動；任務與環境回饋被用來引導 on-policy 的規劃與學習。Fireworks 團隊總共跑了超過 50 次訓練實驗與超過 200 次評估，並開發了尚未公開的新訓練演算法，整個訓練流程都在 Fireworks Serverless Training 上完成，且僅使用自有資料，不含客戶資料。

📊 **公開評測：多數任務打平或超越，成本大幅下降**

Fireworks 用三種推理力度等級的 Kimi K3 作為對照組，並以 K3 公開的 API 定價計算成本，以下是官方公布的部分結果：

| 指標 | Kimi K3 | Ember-1 |
| --- | --- | --- |
| 輸出 token（每任務） | 49.3K | 29.9K |
| 任務分數 | 0.751 | 0.753 |
| 平均步驟數 | 23.8 | 21.4 |
| 輸出成本估算（每任務） | 約 $0.45 | 約 $0.74（原文，可能為兩者數值對調，詳見來源） |

（註：上表中成本數字為 MarkTechPost 自行依輸出 token 換算，僅計輸出部分。）

整體來看，Ember-1 的推理 token 相較 K3 下降了 71.3%，總 token 用量下降 39%，任務分數幾乎沒有變化。在具體基準測試上，Ember-1 在 Terminal Bench 2.1 與 DeepSWE 1.1 上領先 K3 Max，但在 SWE-bench Verified 與 SWE-Interact 上略微落後；在涵蓋七個基準與兩位客戶正式環境流量的測試中，K3 的推理長度被縮短了 35% 到 50%，且沒有犧牲準確度。在 Doximity 的 Bedside Bench（一組經醫師驗證的 500 筆臨床案例集）上，Ember-1 透過 Fireworks 新推出的 Specialized Intelligence Index，建立了新的「成本對任務」帕雷托前緣（Pareto frontier）。Fireworks 也與兩位客戶在正式程式碼工作負載上做了即時 A/B 測試，兩者都在品質相當的情況下，觀察到每個任務約減少 35% 的 token 用量；目前已有一位客戶把 Ember-1 用在正式環境中。

⚠️ **目前無法自行部署**

Ember-1 只能透過 Fireworks 的 serverless API 以 Research Preview 形式使用，Fireworks 並未釋出模型權重、訓練程式碼或確切的訓練演算法，因此自行架設（self-hosting）目前不是選項。在 Fireworks 上，Ember-1 的每 token 計費與 Kimi K3 相同，輸入 $3.00、快取輸入 $0.30、輸出 $15.00（每百萬 token），省下的成本完全來自生成的 token 變少，而非單價調整。

🎯 **實務啟示**

如果你的 agentic 工作負載正被多輪對話中不斷重播、重新計費的冗長推理過程拖累，Ember-1 的做法提供了一個思路：與其在推論階段硬調低 reasoning effort 犧牲品質，不如透過後訓練讓模型自己學會分辨哪些推理有用、哪些是重複迴圈。但在自行採用前，仍要留意目前只能透過 Fireworks 的托管 API 使用，且在部分 SWE 基準上表現略遜於原始 K3。

🔗 **來源**
- 標題：Fireworks AI Releases Ember-1: A Post-Trained Kimi K3 That Uses About 40% Fewer Tokens
- 作者／機構：Asif Razzaq
- 連結：https://www.marktechpost.com/2026/09/28/fireworks-ai-releases-ember-1-a-post-trained-kimi-k3-that-uses-about-40-fewer-tokens/

#FireworksAI #Ember1 #KimiK3 #LLM #ReasoningModels #AgenticAI #TokenEfficiency #MoonshotAI #AIInference #MachineLearning
