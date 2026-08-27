---
title: 'Z.ai Releases GLM-5.3-Flash: A 320B-A18B Natively Multimodal MoE With a 1M-Token
  Context'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/26/z-ai-releases-glm-5-3-flash-a-320b-a18b-natively-multimodal-moe-with-a-1m-token-context/
model: claude-code/sonnet
generated_at: '2026-08-27T17:24:09.188750'
score: 106
---

📌 Z.ai 發布 GLM-5.3-Flash：3200 億參數多模態 MoE，價格僅十分之一

TL;DR：GLM-5 系列首款原生多模態模型，用十分之一價格逼近 Claude Opus 4.8 的程式碼能力。

一款模型悄悄以「Ox Alpha」的匿名身分在 OpenCode 與 OpenRouter 上跑了一週，直到 Z.ai 正式公布身分，外界才知道背後其實是全新的 GLM-5.3-Flash。

🤔 這款模型想解決什麼問題

Z.ai 表示，GLM-5.3-Flash 是 GLM-5 系列中第一款原生多模態模型，同時也是該實驗室推出過最便宜、卻仍具備實用能力的程式碼模型。目標很直接：在維持高階編碼能力的同時，大幅壓低推論成本，讓開發者能以更低門檻部署多模態、長上下文的 agent 應用。

🧩 架構與訓練規模

GLM-5.3-Flash 是一個 mixture-of-experts（MoE）模型，總參數 320B，每個 token 僅啟用 18B 參數；支援高達 1,048,576 token（約百萬級）的上下文視窗，並可接受影像與影片輸入。模型從一個全新訓練的基礎模型出發，使用 30T token 規模的多模態語料庫進行預訓練。權重以 MIT 授權釋出於 Hugging Face，同時也有已上線計價的託管 API。

Z.ai 指出，整個 Ox Alpha 預覽版完全在自製的中國國產 AI 晶片上運行，搭配自研、以 SGLang 為基礎的推論引擎，將 encoding、prefill、decoding 三個階段解耦（disaggregate）處理，官方宣稱在數萬顆加速器規模下取得端到端 3 倍的服務效能提升。

📊 官方基準與獨立評測的落差

根據 Z.ai 的說法，GLM-5.3-Flash 在各項基準測試與實際工作負載上全面超越前代 GLM-5.2，價格卻僅約十分之一；在其內部程式碼基準上，成績與 Claude Opus 4.8 相差不到半分。文章也提醒，這些數字多為 Z.ai 自行公布，各測試所用的執行環境（harness）不盡相同，模型卡的註腳會分別標註溫度、上下文長度限制與評審模型，因此跨模型比較須留意設定差異。

獨立測評機構 Artificial Analysis 給出 Intelligence Index 57 分，在 Z.ai 的 API 上實測輸出速度為 48.7 tokens/秒、首字延遲（TTFT）1.52 秒，顯示「智慧與價格比」不錯，但輸出速度偏慢、內容也偏冗長。視覺能力則是相對弱項，在 BabyVision 與 MVBench 上落後於 Gemini 3.7 Flash。

💡 定價與使用管道

標準 API 定價為輸入 0.15 美元／百萬 token、快取輸入 0.03 美元／百萬 token、輸出 0.50 美元／百萬 token。Z.ai 表示在折扣層級下，於 Artificial Analysis Intelligence Index v4.1.1 測試中平均每個任務成本約 0.045 美元。GLM Coding Plan 各方案（Lite 每月 18 美元、Pro 80 美元、Max 168 美元）皆已可使用該模型，配額為 GLM-5.3 的三倍，多模態能力也已整合進 ZCode 的 Browser Use 與 Computer Use 功能。本地部署則支援 SGLang、vLLM、TokenSpeed 與 KTransformers。

🎯 給工程師的實務啟示

如果你已經在用 GLM 系列做 agentic coding，GLM-5.3-Flash 的百萬 token 上下文與多模態輸入，讓長文件、長對話，以及需要讀圖讀影片的工作流程更容易一次處理完。MIT 授權加上多個本地推論框架的支援，也降低了自架的門檻。但視覺能力仍有落差，且輸出速度偏慢，實際導入前建議先用自己的工作負載跑一輪基準，而非只看官方數字。

🔗 來源
- 標題：Z.ai Releases GLM-5.3-Flash: A 320B-A18B Natively Multimodal MoE With a 1M-Token Context
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/26/z-ai-releases-glm-5-3-flash-a-320b-a18b-natively-multimodal-moe-with-a-1m-token-context/

#GLM #ZAI #MoE #LLM #OpenSource #MultimodalAI #LongContext #AICoding #HuggingFace #AIInfrastructure
