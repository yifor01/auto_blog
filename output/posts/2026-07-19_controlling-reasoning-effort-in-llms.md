---
title: Controlling Reasoning Effort in LLMs
source: Sebastian Raschka
url: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
score: 97
model: tencent/hy3:free
generated_at: '2026-07-19T08:03:39.428829'
---

📌 【Sebastian Raschka 專欄】如何打造有多檔推理力度的 LLM

TL;DR：Raschka 新文聚焦開發具多種 reasoning-effort 模式的推理模型，補足過往教學缺口。

推理模型問世將滿兩年，從 OpenAI o1 到 DeepSeek-R1，再到上週釋出的 GPT-5.6 提供三種尺寸、各約五到六種推理力度設定——但「怎麼讓模型本身支援多檔推理模式」的實作細節，過去卻較少被獨立拆解。

🤔 **推理模型已成標準配備，但「力度控制」是新課題**

OpenAI 在約兩年前釋出 o1，帶動 LLM-based reasoning 模型風潮；約四個月後 DeepSeek-R1 跟進，並公開以 reinforcement learning with verifiable rewards（RLVR，可驗證獎勵的強化學習）訓練推理模型的做法。上週 OpenAI 釋出 GPT-5.6 系列，包含三種尺寸，每種皆有約五到六個 reasoning-effort 設定。作者指出，推理模型已成為現代模型釋出的標準部分。

🧩 **從「轉換模型」走向「多模式推理模型」的開發**

Raschka 過去資源（如《Understanding Reasoning LLMs》、兩篇 RL 推理狀態專文，以及 440 頁新書《Build A Reasoning Model (From Scratch)》）多聚焦如何把常規 LLM 轉為推理模型。本文則標榜為獨立可讀的專文，目標是解釋如何開發具多種 effort modes 的推理模型，類比於文首示意圖所示。作者提醒，不應將「推理模型」字面解讀為像人類般思考；在 LLM 研究中，它指會輸出 intermediate reasoning trace（中間推理軌跡，逐步處理任務的回應）的模型。

🎯 **實務啟示**

對從事推理模型訓練或部署的工程師，本文切入點從「單一推理能力」擴充套件到「可調力度模式」，呼應 GPT-5.6 等實際產品的多檔設定需求。若你已讀過 Raschka 先前的推理模型資源，這篇可作為補完「推理力度控制」實作視角的續作；若沒讀過，作者表示本文也能獨立閱讀。

🔗 **來源**
- 標題：Controlling Reasoning Effort in LLMs
- 作者／機構：Sebastian Raschka
- 連結：https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms

#LLM #ReasoningModel #ReasoningEffort #RLVR #OpenAI #DeepSeek #GPT56 #SebastianRaschka #MachineLearning #AI
