---
title: 'Google DeepMind Releases Gemini 3.8 Flash and Gemini 3.8 Flash Cyber: One
  Core Model, Two Access Envelopes'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/02/google-deepmind-releases-gemini-3-8-flash-and-gemini-3-8-flash-cyber-one-core-model-two-access-envelopes/
model: claude-code/sonnet
generated_at: '2026-09-03T20:21:01.641856'
score: 89
---

📌 Gemini 3.8 Flash雙版本齊發：同一顆模型，兩道存取閘門

TL;DR：Google DeepMind同時發布Gemini 3.8 Flash與限量開放的Cyber版，靠存取權限而非架構區分一般與資安用途。

六週內第三次發布Flash系列模型，Google DeepMind這次玩的不是「更大更強」的老套路，而是同一顆核心模型，切出兩種截然不同的使用門檻。

🤔 **三週一版的Flash節奏，多了一道「資安限定」入口**

Google DeepMind宣布推出Gemini 3.8 Flash與Gemini 3.8 Flash Cyber，距離上一版Gemini 3.7 Flash僅三週，也是六週內第三個Flash發布。兩個版本使用相同的基礎模型，透過長時間執行的agentic迴圈遞迴評估精煉而成。真正的差異不在架構，而在安全防護層級與誰能使用。Gemini 3.8 Flash已透過Gemini API、Google AI Studio、Antigravity、Android Studio與Gemini Enterprise全面開放，可直接導入正式環境，但權重仍為封閉，沒有自架或地端部署的選項。Gemini 3.8 Flash Cyber則完全不對外開放，僅透過新設的Fairwind Program逐案審核授權。

🧩 **規格未變，但「更努力思考」是重點**

研究團隊說明，3.8 Flash是以3.7 Flash為基礎打造。規格維持不變：1,048,576 token的context window、65,536 token的最大輸出、支援文字、圖片、音訊與影片輸入及文字輸出，思考等級維持LOW、MEDIUM、HIGH三檔，MEDIUM為預設值。有一個會影響遷移的重大改動：3.8 Flash不再支援MINIMAL等級，設定該值會直接觸發API驗證錯誤。

行為面的改變才是重點：Google直言3.8 Flash「更努力工作」，面對複雜任務會執行額外的推理步驟並反覆呼叫工具，在較高的思考等級下可能消耗更多token。Google的開發者指南也坦承，這種做法用更高的token消耗換取更好的準確度，並建議在compute效率是硬限制的情境下，繼續使用3.7 Flash——這是罕見地直接承認新模型並非所有場景的最佳預設。

📊 **基準測試表現**

Google公布的部分數據如下：

| 基準測試 | 結果 |
|---|---|
| HLE-Verified | 54.9% |
| DeepSWE v1.1（長週期軟體工程基準） | 以更低成本超越多數更大型的前沿模型（未附絕對分數） |
| Vals Finance Agent V2、Harvey Legal Agent Benchmark | 相對於3.7 Flash與其他前沿模型有所提升（未附絕對分數） |
| CyberGym（漏洞發現，以C/C++為主） | 超越3.5 Flash Cyber及規模更大的前沿模型，達前沿水準（未附絕對分數） |
| 內部20種程式語言漏洞發現基準 | 發現成功率高於70% |
| CWE-Bench（Collinear執行，修補pass@1） | Flash Cyber 47.2%，對比某領先前沿模型47.8% |
| Chrome Security內部評測 | 正確修補數為最佳大型商用模型的2.6倍 |
| Wiz滲透測試內部基準 | recall高出7.5至9.7個百分點，成本降低2.3至5.2倍 |

Google Cloud Vulnerability Research團隊也提到，用Flash Cyber在兩小時內找到一個關鍵的基礎性漏洞，這類工作通常需要數月時間。

💡 **不是要拿第一，而是要站上Pareto frontier**

在CWE-Bench的修補任務上，Flash Cyber以47.2% pass@1逼近某領先前沿模型的47.8%，Google將此定調為「以顯著更低成本逼近頂尖表現」，而非「登頂」，並明確表示自身定位是站上Pareto frontier而非刷新排行榜第一名。Google也明確表示，開發Flash Cyber時優先處理漏洞修補，而非攻擊性的漏洞利用能力。也正因為Flash Cyber附帶更寬鬆的資安防護限制集合，才需要透過Fairwind Program把使用者限制在政府單位、關鍵基礎設施營運商與軟體維護者等可信賴的防守方。

⚠️ **部分數據仍是相對敘述**

DeepSWE v1.1、Vals Finance Agent V2、Harvey Legal Agent Benchmark以及CyberGym等測試，Google的公告中僅提供相對比較結果（「優於」「超越」），並未公開絕對分數，評估其實際能力時需留意這層限制。

🎯 **實務啟示**

如果你的工作負載對compute成本敏感，Google自己都建議先留在3.7 Flash，把3.8 Flash留給真正需要多步推理、反覆呼叫工具的複雜任務。而如果你屬於政府機關、關鍵基礎設施或開源軟體維護方，Fairwind Program是目前唯一能接觸Flash Cyber這類「進攻/防守雙面刃」能力的合法途徑，值得留意申請管道與審核條件。

🔗 **來源**
- 標題：Google DeepMind Releases Gemini 3.8 Flash and Gemini 3.8 Flash Cyber: One Core Model, Two Access Envelopes
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/02/google-deepmind-releases-gemini-3-8-flash-and-gemini-3-8-flash-cyber-one-core-model-two-access-envelopes/

#GeminiFlash #GoogleDeepMind #LLM #AICybersecurity #VulnerabilityResearch #AgenticAI #AIBenchmark #CyberGym #ResponsibleAI #AIModel
