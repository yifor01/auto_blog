---
title: Tencent launches Hy4
source: Hacker News
url: https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/
model: claude-code/sonnet
generated_at: '2026-11-06T22:19:57.780835'
score: 92
---

📌 騰訊 Hy4 開源旗艦模型登場：補上視覺理解與 Computer-Use 兩塊拼圖

TL;DR：騰訊新一代開源模型 Hy4 首度支援視覺理解與電腦操作，並在金融、遊戲開發場景做了深度最佳化。

當多數開源模型還在比拼純文字推理分數時，騰訊 Hy 團隊選擇把戰場拉到「能不能真正幹活」。Hy4 這次補齊的,不是另一個 benchmark 分數,而是視覺理解和操作電腦這兩項過去開源模型相對缺席的能力。

🤔 **從純文字模型到能看、能動手的 Agent**

Hy4 是騰訊 Hy 系列最新一代大型語言模型，官方宣稱其效能已躋身全球領先開源 AI 模型之列。模型權重與 system card 將於近期釋出。相較前代，Hy4 首次加入視覺理解能力，同時在指令遵循、長文本理解（long-context）與長程 agentic 任務上都有明顯提升。

🧩 **視覺理解 + Computer-Use + 專業軟體訓練**

Hy4 透過進階的視覺理解、推理與工具呼叫（tool-calling）能力，支援細粒度影像處理、複雜圖表分析與數學視覺推理等任務。更值得注意的是，Hy4 首度導入 computer-use 能力，可透過命令列介面（CLI）與圖形使用者介面（GUI）互動並執行日常工作任務。官方特別提到，模型針對 Blender、CAD 等專業軟體做了專門訓練，以強化長程、複雜任務的規劃與執行能力。

在產品整合面，Hy4 深度結合騰訊 WorkBuddy，透過 WeCom 串接聊天、郵件、文件、日曆與會議等日常工作流資料，能自動追蹤多專案進度、標記待辦事項與即將到來的會議，協助使用者排定優先順序。

📊 **金融與遊戲開發場景的實測數據**

Hy4 在金融分析上做了針對性訓練，依據基金研究、證券分析與量化投資的真實工作流資料微調。騰訊 Hy 團隊與騰訊金融科技合作，邀請 213 位金融專業人士（其中 153 位來自外部機構、約 70% 具五年以上業界經驗）進行盲測，針對 579 個真實金融任務評分：

| 模型 | 評分 |
|---|---|
| Hy4 | 3.04 |
| DeepSeek-V4.1-Flash-1017 | 2.97 |
| Kimi K3.1 Pro | 2.68 |
| GLM-5.3 | 2.68 |

Hy4 在這項評測中拿下開源模型最高分，且相較 Hy4 Preview，在財金公司 Rabyte 的內部投資研究 Agent 基準（iRaB）上提升了 12.03 個百分點。幻覺率也從 12.95% 降至 7.2%，因無根據假設導致的錯誤率從 23.1% 降至 5.6%。

在前後端與遊戲開發方面，Hy4 針對複雜商業邏輯、狀態管理與前後端協調做了最佳化，並與騰訊互動娛樂集團（IEG）的專業開發者合作，深度整合 Unreal Engine、Unity 與 Godot，支援複雜遊戲邏輯與多人連線實作。相較 Hy4 Preview，在 GameDev 基準上提升 19.1%，GameLogic 基準提升 9.8%。

⚠️ **安全性：防禦性資料訓練，攻擊性能力評估「未見顯著風險」**

網路安全方面，Hy4 的訓練資料以防禦性安全資料為主，優先涵蓋概念驗證（PoC）開發與漏洞修復，並納入逆向工程與滲透測試作為分析用途，但明確排除與漏洞利用相關的攻擊性材料。騰訊玄武實驗室與 Keen Security Lab 針對密碼學逆向、二進位去混淆、漏洞利用等領域進行安全評估,結論是未發現 Hy4 在這些受評領域存在顯著的攻擊性網路安全風險。生物安全方面，內部專家評審認為 Hy4 具備扎實的生物學基礎知識，但在開放式實驗設計能力上仍不及前沿模型。

🎯 **實務啟示**

對工程師而言，Hy4 值得關注的不只是分數，而是「視覺理解＋computer-use＋垂直場景訓練」這個組合——它代表開源模型正從純文字助理走向能操作實際軟體環境的 agent。若你的團隊在評估開源 agent 框架，Hy4 已在 Tencent Cloud TokenHub 上線，API 也將透過 OpenRouter 等第三方平臺提供，可留意後續釋出的權重與 system card，實測其 computer-use 能力是否真的能落地到現有工作流。

🔗 **來源**
- 標題：Tencent launches Hy4
- 作者／機構：Tencent（經 Hacker News 使用者 gmays 分享）
- 連結：https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/

#Tencent #Hy4 #OpenSourceAI #LLM #ComputerUse #AIAgent #VisionLanguageModel #AIProductivity #Cybersecurity #OpenSourceLLM
