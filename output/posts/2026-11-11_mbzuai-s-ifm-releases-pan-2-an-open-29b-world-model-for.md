---
title: MBZUAI’s IFM Releases PAN 2, an Open 29B World Model for Physical AI
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/10/ifm-pan-2-open-world-model/
model: claude-code/sonnet
generated_at: '2026-11-11T23:41:23.937027'
score: 106
---

📌 MBZUAI開源PAN2：29B世界模型模擬物理動作結果

TL;DR：IFM開源29B世界模型PAN 2，用文字動作模擬場景變化，助agent先模擬再行動。

如果機器人在真正動手之前，能先在腦中「跑一遍」會發生什麼事，會怎樣？這正是MBZUAI旗下Institute of Foundation Models（IFM）在PAN 2想做的事。

🤔 背景：為物理智慧打造的世界模型

IFM於2026年11月10日在X上公布PAN 2，是一個通用世界模型，輸入一個場景與一段文字描述的動作，模擬動作發生後場景會如何改變，輸出為影片。這是繼2025年11月發布的PAN之後的後續版本，權重、訓練程式碼與推論程式碼皆以Apache 2.0授權發布。對機器人與agent開發者而言，賣點很直接：在真正行動前，先在模擬中測試計畫。

🧩 架構：Generative Latent Prediction，模擬拆成兩種推理

PAN 2沿用IFM在其《Critique of World Models》論文中提出的Generative Latent Prediction（GLP）架構。整體目標是「simulative reasoning」：agent先提出多個計畫，PAN 2逐一模擬，agent再依模擬結果挑出最好的那個去執行。素材指出PAN 2將模擬拆成兩種推理，但兩者具體內容原始素材未進一步展開，故本文不做臆測。

📊 消融實驗：拿掉LLM推理，完成率直接歸零

IFM的消融實驗顯示，conceptual reasoning（概念推理）這一環對結果影響甚大：

| 設定 | 完整計畫完成率 | 單步完成率 |
|---|---|---|
| 完整模型 | 34.0% | 75.1% |
| 無conceptual reasoning | 0.0% | 8.7% |
| 僅格式重寫（無推理） | 27.8% | — |

IFM也提到，在早期訓練階段之後拿掉遊戲、動畫與模擬素材的影片資料，一個9B的測試模型在未使用這些資料訓練的情況下，贏得了58%的盲測投票。

IFM用自家測試套件評估PAN 2，涵蓋6項能力、300個單一動作案例，再加上100個多步驟任務，所有分數皆為IFM自行回報。

💡 使用方式與安全防護

PAN 2支援text-to-video與image-to-video，可透過Hugging Face Diffusers、vLLM、FastVideo或repo內的generate.py執行。預設取樣設定為50步、flow shift 9、guidance 2.5，一個clip預設241個frame（約10秒）；每個GPU worker需以BF16載入完整29B模型，IFM未公布VRAM用量或生成時間。

Prompt建議寫成結構化caption，IFM也為Claude Code與Codex提供一個Conceptual Reasoner skill，可將自由文字改寫成結構化caption，caption有1,536 token的硬上限。IFM強烈建議搭配獨立的pan2-guardrail模組：在IFM的測試中，它把有害T2V請求的不安全輸出比例從33.9%降到1.5%，但也擋掉了11.5%的正常（benign）T2V請求。

⚠️ 限制

消融與benchmark分數皆為IFM自行回報、自行執行，未經第三方獨立驗證；guardrail在降低不安全輸出的同時，也有一定比例誤擋正常請求。

🎯 實務啟示

對做機器人或agent規劃的團隊，PAN 2提供了一個可自行部署、附訓練程式碼的世界模型，可用於「先模擬、再行動」的pipeline驗證計畫可行性；消融實驗也提醒，若要自行微調或裁剪模型，拿掉conceptual reasoning環節的代價相當高。

🔗 來源
- 標題：MBZUAI's IFM Releases PAN 2, an Open 29B World Model for Physical AI
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/10/ifm-pan-2-open-world-model/

#WorldModel #PAN2 #MBZUAI #PhysicalAI #OpenSource #Robotics #GenerativeAI #VideoGeneration #ApacheLicense #AIAgents
