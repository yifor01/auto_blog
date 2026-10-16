---
title: Elorian’s first AI model wants to reason with images, not just about them
source: TechCrunch AI
url: https://techcrunch.com/2026/10/16/elorians-first-ai-model-wants-to-reason-with-images-not-just-about-them/
model: claude-code/sonnet
generated_at: '2026-10-16T20:12:47.807499'
score: 93
---

📌 Elorian 的第一個模型：讓 AI 邊看邊想，而不是看一眼就靠記憶推理

TL;DR：新創 Elorian 發布研究預覽模型 Glimpse，讓模型在推理過程中能主動回去「重新看」圖片與影片。

你有沒有想過，為什麼人類可以靠著 IKEA 說明書上幾個簡筆圖就把家具組裝起來，但前沿多模態模型看一張桌遊照片卻說不出誰在贏？這正是 Palo Alto 新創 Elorian 想解決的問題。

🤔 **多模態模型「看一次，就靠記憶推理」**

Elorian CEO、前 Google DeepMind 研究員 Andrew Dai 的團隊觀察到，目前多數多模態模型的運作方式是把圖片轉成 token 之後，就完全在文字空間裡推理，類似「憑記憶描述一張照片」。Dai 分享了一個親身經歷：他拍下一局剛結束的桌遊照片，問前沿模型誰贏了，模型答不出來。他認為原因在於每種桌遊都有自己的視覺語言、圖示與符號系統，「對成年人來說用很少的文字就能看懂發生了什麼事，但這些模型無法直覺理解符號的意思」。

🧩 **「視覺暫存空間」：推理中途可以回頭再看一次**

Elorian 於週五發布的第一個模型 Glimpse，核心機制被稱為「visual scratch space」（視覺暫存空間）：模型在推理過程中可以主動裁切放大圖片的某個區域、從影片中抽取特定幀，或是執行程式碼來測量、比對它正在看的內容，就像用手指在手機照片上放大確認細節。摘要指出，這個做法本身並非全新，OpenAI 在 2025 年已為 o 系列模型加入推理中裁切放大的能力；Elorian 的主張在於它從頭把整個模型設計圍繞這個機制打造，而且訓練成本低廉：一個小團隊用數百張 GPU 完成訓練，模型規模也遠小於它被拿來比較的前沿系統。

📊 **評測表現與定價**

根據 Elorian 自己的評測，Glimpse 在科學圖表推理與短影片字幕生成任務上超越 GPT-6 Astra，在其他視覺推理任務上則表現具競爭力（摘要未提供具體分數）。計費方式為每百萬 token 輸入 0.60 美元、輸出 3 美元，比 Sonnet、Sol 等中階模型便宜，但比 Haiku、Luna 等輕量模型貴。

⚠️ **目前僅研究預覽，無法獨立驗證**

Glimpse 目前以研究預覽形式發布，提供 API 存取，聊天介面則需候補名單。這意味著外部開發者還無法大規模實測或複現摘要中提到的評測結果，目前能看到的主要是 Elorian 自身給出的結果敘述與定位論述。

🎯 **為何工程師該留意**

Elorian 六個月前以 3 億美元估值完成 5500 萬美元種子輪（由 Striker Venture Partners、Menlo Ventures、Altimeter Capital 共同領投，Nvidia 與 Google 首席科學家 Jeff Dean 參與），目前瞄準坐擁大量影片資料的客群：機器人公司、科學實驗室、媒體與創意產業。長期目標是從「看懂」走向「行動」，建立場景模型以支援決策，甚至直接控制機器人；Dai 表示明年目標是打造「世界最強的視覺推理模型」。對處理圖表、影片、空間推理任務的工程團隊來說，這是一個值得追蹤但尚待驗證的技術方向。

🔗 **來源**
- 標題：Elorian's first AI model wants to reason with images, not just about them
- 作者／機構：Aditya Mehta, TechCrunch AI
- 連結：https://techcrunch.com/2026/10/16/elorians-first-ai-model-wants-to-reason-with-images-not-just-about-them/

#MultimodalAI #VisionLanguageModel #AIStartup #VisualReasoning #Elorian #ComputerVision #AIResearch #RoboticsAI #ModelRelease #SeedRound
