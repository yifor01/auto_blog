---
title: 'PROOF-Gen: From Optimized Data to Better Distillation'
source: Apple ML
url: https://machinelearning.apple.com/research/proof-gen-optimized-distillation
model: claude-code/sonnet
generated_at: '2026-08-27T17:18:44.249795'
score: 109
---

📌 【Apple ML・EMNLP 2026】57% 教師軌跡失敗,PROOF-Gen 讓失敗也能變教材

TL;DR：PROOF-Gen 用逐案例反思優化,把教師模型失敗的工具呼叫軌跡救回為乾淨訓練資料。

在工具呼叫（tool-calling）代理人的蒸餾流程裡，多數團隊只做一件事：讓教師模型跑過場景，通過的留下、失敗的丟掉。但如果失敗率本身就很高，而且失敗的理由又高度相似呢？Apple ML 團隊在 τ2-bench 上觀察到，教師模型有 57% 的試驗會失敗，其中三分之二屬於「差一步就成功」的 near-miss：大部分工具呼叫都對，卻被一個決定性的錯誤搞砸。這代表每一輪蒸餾都在原地打轉，同樣困難的場景被一次又一次地跳過。

🤔 **generate-and-filter 的死角**

標準做法是對教師生成的軌跡做監督式微調（SFT），作為蒸餾工具呼叫能力的第一階段。上線的代理人系統通常每天或每週重跑這個階段，每次都要付出呼叫前沿教師模型的成本。問題在於機制本身是 generate-and-filter：留下通過的軌跡、丟棄失敗的，而失敗的案例完全沒有提供訓練訊號。久而久之，同一批「教師也做不好」的困難場景就持續留在資料集之外。

🧩 **PROOF-Gen：讓反思器替教師寫「提示補丁」**

PROOF-Gen（Per-scenario Reflective Optimization to Overcome Failed Generation）針對每一個失敗任務，讓一個反思器（reflector）分析執行軌跡與評估回饋，寫出針對該場景的修正指引，引導教師模型重新產生一次能通過的軌跡。關鍵設計是：這段修正指引只用來引導生成，訓練前會被剝離，讓學生模型看到的仍是乾淨的示範軌跡，沒有任何針對特定任務的鷹架（scaffold）殘留。換句話說，教師是被逐案例最佳化過的提示詞說服去做對，而不是靠人工寫死的修正規則。

📊 **93% 失敗場景被救回，Pass^1 從 0.132 衝到 0.529**

在 τ2-bench 上，逐案例的提示優化把 93% 原本失敗的場景救回為通過的軌跡。把這些救回的資料和原本通過的資料合併後進行微調，Qwen3-4B-Instruct-2507 的 Pass^1 從 0.132 提升到 0.529；Gemma 4 E4B-it 則在 BFCL v4 多輪測試上取得 +7.2pp 的提升。在一個實際上線的蒸餾管線中，這個方法讓軌跡品質提升 +6.3pp 的目標完成率，並且成功遷移到一個已部署的裝置端模型：目標完成率提升 +1.5pp，多項回覆品質指標提升 +1.7 至 +5.0pp，且在每一個語系都出現正向遷移（非英語平均 +1.48pp）。

🎯 **實務啟示**

如果你的團隊也在跑「教師生成、過濾、微調」的每週蒸餾循環，PROOF-Gen 提醒了一件容易被忽略的事：失敗率高的場景往往不是雜訊，而是資料集裡最值得投資的部分。與其把失敗直接丟掉，不如把它們當成需要逐案例提示優化的候選集，用一個反思器把教師拉回正軌，再把提示鷹架剝除後留下乾淨的示範。這種做法特別適合需要頻繁重跑蒸餾、且教師模型呼叫成本高昂的生產環境。

🔗 **來源**
- 標題：PROOF-Gen: From Optimized Data to Better Distillation
- 作者／機構：Anh Ta, Junjie Zhu, Shahin Shayandeh（Apple ML）
- 連結：https://machinelearning.apple.com/research/proof-gen-optimized-distillation

#PROOFGen #Distillation #ToolCalling #AppleML #LLM #AgenticAI #FineTuning #EMNLP2026 #SyntheticData #ModelTraining
