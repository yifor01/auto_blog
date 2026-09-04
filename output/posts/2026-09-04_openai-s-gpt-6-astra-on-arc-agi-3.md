---
title: OpenAI's GPT-6 Astra on ARC-AGI-3
source: Hacker News
url: https://arcprize.org/blog/astra
model: claude-code/sonnet
generated_at: '2026-09-04T19:49:09.202365'
score: 91
---

📌 【OpenAI】GPT-6 Astra 在 ARC-AGI-3 拿下 99.9%，靠的是自創的符號筆記法

TL;DR：GPT-6 Astra 在 ARC-AGI-3 創下 SOTA，行動效率首度全面超越人類基準。

一個測驗要求 AI 在完全沒有說明書的陌生遊戲環境裡，自己摸索規則、設定目標、規劃行動。GPT-6 Astra 不只答對了，用的步數還比一半以上的人類受試者更少，而且是在 96% 的關卡上都做到這件事。

🤔 ARC-AGI-3 到底在測什麼

ARC-AGI-3 是 ARC-AGI 系列基準的第三代，專門用來研究 agentic intelligence：agent 必須在全新、抽象、回合制的環境中主動探索、推斷目標,並建立內部模型以規劃行動，而不是依賴明確指令。人類受試者可以解出 100% 的環境。ARC-AGI-3 具體測試四種能力：探索（主動與環境互動以取得資訊）、建模（把觀察轉成能預測未來狀態的通用模型）、目標設定（在稀疏獎勵下辨識目標狀態）、規劃與執行（規劃出從當前狀態到目標的路徑，並依新資訊隨時修正）。

📊 換一種 harness，分數從 62.7% 跳到 99.9%

Astra 在兩種測試 harness 下都拿下 SOTA。在 Standard harness（模型可自行選擇要在整個環境中攜帶哪些筆記）下，Astra（max）在 ARC-AGI-3 Semi-Private 拿下 62.7%，花費約 2.6 萬美元；在 Provider Adapter harness（保留不透明的推理狀態並用 compaction 處理長對話，讓模型能重複利用先前的推理成果）下，Astra（high）拿下 99.9%，花費約 1.9 萬美元。

| 推理強度 | Standard harness | Provider Adapter harness |
|---|---|---|
| max | 62.7%，$26,098 | 98.6%，$17,332 |
| xhigh | 59.3%，$37,317 | 98.4%，$18,147 |
| high | 54.8%，$40,705 | 99.9%，$18,817 |
| medium | 38.6%，$48,090 | 98.4%，$19,285 |
| low | 17.5%，$38,166 | 98.0%，$21,298 |
| none | 35.2%，$49,791 | 96.7%，$23,457 |

值得注意的是，在 max 推理強度下，Astra 因為能用更少行動解出遊戲，總體 model call 與 token 數反而下降，成本也隨之降低。作為對照，ARC Prize 團隊在人類測試中支付每場 90 分鐘 115 美元、每完成一款遊戲再加 5 美元，受試者平均每場約嘗試九款遊戲，換算下來每次嘗試約 12.78 美元；若只計算大腦運作消耗的電力成本，則每場約 0.6 美分，每次嘗試約 0.067 美分。

💡 它把陌生的遊戲機制，寫成了自己發明的代數式筆記

除了分數之外，Astra 的行為紀錄（replay）更值得玩味。在 Standard harness 下，Astra 可以自行選擇要保留哪些策略筆記，它會追蹤物件、座標、規則與未完成的計畫，並使用一套自己生成的、類似 domain-specific language 的簡寫記法。作者指出，類似行為在其他模型上也出現過，但 Astra 的筆記在精確度與資訊密度上格外突出。舉例來說，它會用「L8: hub q2 (8↓). Lengths: 14=1…」記錄關卡、局部旋轉索引與機制長度；用「extend8 to3; retract10 to2; shorten8 to1」記錄一組對特定機制的多步驟操作序列；用「9−=(39,4), rotate=(49,18), 14+=(59,11)」把操作對應到執行該操作的控制項座標；用「Turn 5: P=(24,20), empty, facing west」把回合數、玩家位置、攜帶狀態與朝向壓縮成一行。這是一種即興產生的代數式簡寫，而非完整的程式語言。

🎯 行動效率首次全面追平甚至超越人類

ARC Prize 團隊在推出 ARC-AGI-3 之前，找了約 500 名一般大眾（未特別篩選解謎能力）建立人類行動效率基準，以完成該關卡玩家的行動次數中位數作為對照。結果顯示，在 Provider Adapter harness 下，Astra（max）在 96.0% 的關卡上使用的行動次數少於人類基準，平均每關少用 51.7% 的行動。作者原本假設，即使 AI 能解出關卡，探索所需的行動次數仍會明顯多於人類，這在暴力搜尋式的方法上依然成立；但前沿模型呈現出更接近二元的模式，一旦「理解」了遊戲機制，執行時的行動次數就會落在人類效率的範圍內。

🎯 對正在打理 agent 的工程師：筆記本身就是一種世界模型

Astra 的自創代數式筆記法，本質上是把非結構化的環境觀察，即時壓縮成結構化、可重複使用的符號表示。對於正在設計長時任務 agent 的工程師來說，這提示了一個值得驗證的方向：與其只依賴 context window 塞入原始觀察紀錄，讓模型自主決定要保留、壓縮成什麼樣的中介表示，可能是應對複雜、多步驟任務時更節省 token 也更穩健的做法。

🔗 來源
- 標題：OpenAI's GPT-6 Astra on ARC-AGI-3
- 作者／機構：Greg Kamradt, ARC Prize
- 連結：https://arcprize.org/blog/astra

#ARCAGI #OpenAI #GPT6Astra #AGI #AIBenchmark #AgenticAI #LLMReasoning #AIResearch #WorldModels #FrontierAI
