---
title: 'Gemini Decisions API: Fast, calibrated multimodal decisions'
source: Google AI Blog
url: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/
model: claude-code/sonnet
generated_at: '2026-11-11T23:33:54.783463'
pinned: true
---

📌 Gemini Decisions API：單次推論回答上千個是非題

TL;DR：Google 推出 Gemini Decisions API，單次請求可對多模態輸入評估上千個問題，端到端延遲僅150-250毫秒。

如果系統只需要「是」或「否」、「選 A 還是選 B」，為什麼要讓 LLM 逐字生成一整段回答？

🤔 背景或問題

許多實際的 AI 應用場景，核心需求並非生成長文字，而是做決策：要不要呼叫這個工具？這張圖片有沒有問題？這段內容該打幾分？Google DeepMind 的 Min Choi 與 Felix Yu 在部落格中指出，這類「封閉集合」（closed-set）決策，像是工具選擇、政策檢查、模型路由、情境評分，過去往往被迫套用一般的生成式 API，導致延遲與成本都偏高。Gemini Decisions API 就是為了這類場景打造的新端點。

🧩 架構與三種題型

Gemini Decisions API 由新模型 Gemini Decision 1（API 名稱 gemini-decision-1）驅動，透過 Google AI Studio 的 Gemini API 存取。與一般生成式模型逐 token 解碼不同，Gemini Decision 1 對候選選項做單次前向傳遞（single forward pass）評分，直接回傳機率與信心分數。

一次請求可放入單一多模態輸入（文字、圖片、音訊、影片、PDF 混用，最多256K tokens），再搭配最多1,000道獨立問題，三種題型可混用：
- noul（是非題）：評估一個是非條件成立的機率，可附加成立與不成立的判斷準則。
- choice（選擇題）：從2到255個選項中選出結果，回傳每個候選項目的標準化機率。
- score（評分題）：依一套從0開始的順序 rubric 打分，回傳連續加權分數與每個等級的機率。

每個答案都附帶0到1的信心分數，方便程式依信心高低，把模糊案例轉交給備援邏輯或人工審核。官方給出的 Python 範例，示範了如何對同一張搃檯照片與一段文字備註，同時跑完 noul、choice、score 三種題型的判斷。

📊 延遲、成本與基準測試表現

官方公布的基準測試涵蓋 agent 路由、推理、排序與多模態理解，Gemini Decision 1 在整組基準測試中表現領先，且校準誤差（calibration error）最低。因為不需要逐字解碼，模型運算延遲中位數僅50-100毫秒（端到端150-250毫秒），在最多16K tokens 的多模態情境下，即使問題數從1題增加到100題，延遲幾乎維持平坦。

計價方式也與一般生成式 API 不同：每1M input tokens 收費0.10美元，輸出 tokens 完全不計費。共用的輸入內容在同一請求中只計費一次，之後每多加一道問題，只依該問題的 instruction 與 criteria 文字計算 tokens，沒有額外的音訊轉錄或 OCR 費用。官方表示，在共用的基準測試集上，Gemini Decision 1 搭配 Decisions API 的成本比 Gemini 3.5 Flash-Lite 搭配 Interactions API 便宜近5倍。

💡 Google 內部團隊怎麼用

部落格列出幾個已經在使用 Decisions API 的內部案例：
- Gemini Notebook：用 Decisions API 做即時路由，毫秒級判斷查詢意圖，把一般查詢導向較低延遲的模型層級，複雜任務才交給深度推理模型，一般查詢延遲最多降低40%。
- Stitch 的 Rapid Canvas 實驗：用 Decisions API 在數秒內生成產品流程的可互動線框稿，並即時套用語音或點擊編輯。
- Google Labs 的 CC：從超過200個候選表情符號中，在極短時間內選出適合的反應，避免額外運算拖慢互動速度。
- Google Search：把 Decisions API 當作 MCP 工具的安全層，用來偵測對抗性（adversarial）行為與內容。

🎯 實務啟示

對正在設計 agent 系統或內容審核流程的工程師而言，Gemini Decisions API 提供的是介於「寫死規則」與「完整生成式呼叫」之間的第三條路：不用自己訓練分類器，也不用為了一個路由判斷付出完整生成的延遲與成本。文件支援 Python、JavaScript、REST，Google AI Studio 提供免費額度可先行原型驗證，生態系整合也已在 OpenRouter、LangChain、Vercel、LiteLLM、Pydantic AI、Pipecat、LiveKit、OpenCode 等工具鏈中展開，Gemini in Google Cloud 的支援也在規劃中。如果你的系統裡有「選擇題」而非「作文題」的判斷邏輯，這個 API 值得評估能否取代現有的路由或審核機制。

🔗 來源
- 標題：Gemini Decisions API: Fast, calibrated multimodal decisions
- 作者／機構：Google — Min Choi, Felix Yu（Google DeepMind）
- 連結：https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/

#Gemini #GeminiDecisionsAPI #GoogleDeepMind #LLM #AIAgents #ModelRouting #MultimodalAI #AIInfrastructure #DeveloperTools #GenerativeAI
