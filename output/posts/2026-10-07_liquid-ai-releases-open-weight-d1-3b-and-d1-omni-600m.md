---
title: 'Liquid AI Releases Open-Weight d1-3B and d1-omni-600M: Multimodal Decision
  Models With Zero Output Tokens'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/07/liquid-ai-releases-open-weight-d1-3b-and-d1-omni-600m-multimodal-decision-models-with-zero-output-tokens/
model: claude-code/sonnet
generated_at: '2026-10-07T22:14:29.853834'
score: 105
---

📌 Liquid AI 開源 d1-3B / d1-omni-600M:一次 forward pass,零輸出 token 的決策模型

TL;DR:不寫文字、只吐機率的多模態決策模型,開源權重、支援 llama.cpp,主打 NVIDIA 全端即時推論。

一般的 LLM 要給你一個答案,得一個 token、一個 token 地把它寫出來,你的程式再負責解析。Liquid AI 的 d1 系列反過來做:讀一次輸入,直接回傳每個允許答案的機率,輸出 token 數是零。

🤔 **決策不需要生成文字,只需要校準過的機率**

Liquid AI 這次開源兩個模型:d1-3B 讀文字與圖片,d1-omni-600M 讀文字搭配圖片、或文字搭配音訊。兩者都不寫文字,而是針對一組「state」與一批「named questions」,讀一次就回傳每個允許答案的機率。一次呼叫裡可以讓多個問題共用同一個 state,每次回應都會標示 output_tokens: 0。Liquid AI 把這類模型定義為三種問題類型,並建議用於路由、內容審核、意圖分類、reranking、LLM-as-a-judge 評分、agent guardrail 與視覺檢測等場景,強調這不是聊天模型。

🧩 **從既有 LFM2.5 模型權重平均與多次微調合併而來**

d1-3B 共 3.12B 參數,起點是 decoder-only 的 vision-language 模型 LFM2.5-VL-3B。Liquid AI 先將 LFM2.5-2.6B 與該模型的文字骨幹做權重平均,再用不同 seed 與資料組合微調出多個 checkpoint,最後再合併一次。視覺端採用 400M 參數的 SigLIP2 NaFlex encoder,context 長度 32,768 token。README 特別提到,長輸入、打亂答案選項順序、修正資料捷徑(data shortcuts),比起用更進階的技巧更關鍵。

d1-omni-600M 共 587M 參數,起點是雙向編碼器 LFM2.5-Encoder-350M,由 381M 的共享主幹與決策頭、94M 視覺編碼器、112M 音訊編碼器組成,音訊編碼器是 17 層的 FastConformer。context 長度 16,384 token,音訊片段上限 30 秒,且一次請求只能帶圖片或音訊、不能同時帶兩者;音訊訓練資料僅涵蓋英語的 speaker-to-assistant 場景。

**怎麼用**:兩個 checkpoint 都在 Hugging Face 上,透過 Transformers 載入,並有第一天的 llama.cpp 支援。授權是 LFM Open License v1.0,年營收低於 1,000 萬美元可免費商用。d1-3B 需要 transformers>=5.14 並開啟 trust_remote_code=True,d1-omni-600M 需要 transformers>=5.15。兩者都提供 system_one(state, questions) 處理單一 state,以及 system_one_batch 處理打包請求的介面。README 建議 d1-omni-600M 在 GPU 上使用 float16,因為 bfloat16 會改變部分最高機率的答案。

📊 **Decision Index 上,d1-3B 擠進所有 10B 以下模型之首**

在 Decision Index v0.2.1 上,d1-3B 拿到 48.57 分,打敗所有 10B 以下的模型,也小幅領先 Decider 35B-A3B 的 47.11 分,只有 Winnow-12B 以 50.02 分更高。d1-3B 在 Tools 類別拿下 74.5 分、Arts 類別 36.3 分,但在 Knowledge 類別只有 23.8 分,相對弱勢。Liquid AI 說明這些分數是自行跑官方 scorer 所得,並非正式排行榜提交。

在七個公開文字 benchmark 上,d1-3B 平均 82.9 分,高於 Decider 4B 的 81.1 分;d1-omni-600M 平均 78.4 分,其中 Civil Comments 拿下 95.8 分、PAWS-X 拿下 79.5 分,均為該批比較中的最高分。在 11 個影像 benchmark 上,d1-3B 平均 74.1 分,比起其底層模型的 73.9 分略有提升。音訊方面,Liquid AI 直接稱決策類音訊 benchmark 仍是一個尚待解決的問題。

延遲方面,一個問題在 RTX 4090 上耗時 8 ms(使用 model.compile(mode="reduce-overhead"),未開啟則為 16 ms),在 AMD MI325X 上 9 ms。Jetson 系列中,AGX Thor 為 16 ms、AGX Orin 為 26 ms、Orin Nano 為 50 ms;在 AGX Thor 上,對同一個 state 問三個問題只需 20 ms,相較單一問題的 16 ms 幾乎沒有額外負擔。

⚠️ **仍有明確的邊界**

d1-omni-600M 目前沒有公開延遲數據,屬於較早期的研究性釋出;音訊訓練資料侵限於英語的 speaker-to-assistant 情境;一次請求無法同時帶圖片與音訊;GPU 上若用 bfloat16 而非 float16,部分答案的機率排序會改變。這些都代表它離「通用多模態決策引擎」還有一段距離,目前更適合定義明確、答案空間有限的任務。

🎯 **對工程師的意義**

如果你的系統裡本來就有「分類」「打分」「路由」這類只需要一個機率分佈、不需要生成文字的子任務,用傳統 LLM 加上 prompt 解析往往是殺雞用牛刀,還多了 token 生成的延遲與不穩定性。d1 這種零輸出 token、一次 forward pass 回傳校準機率的設計,如果延遲與分數數字能在自己的場景裡重現,對 guardrail、審核、agent 路由這類高頻、低延遲需求的子系統會是值得評估的選項。

🔗 **來源**
- 標題:Liquid AI Releases Open-Weight d1-3B and d1-omni-600M: Multimodal Decision Models With Zero Output Tokens
- 作者／機構:Asif Razzaq(MarkTechPost)
- 連結:https://www.marktechpost.com/2026/10/07/liquid-ai-releases-open-weight-d1-3b-and-d1-omni-600m-multimodal-decision-models-with-zero-output-tokens/

#LiquidAI #DecisionModels #OpenWeight #MultimodalAI #EdgeAI #NVIDIAJetson #LLMAlternatives #AIGuardrails #ModelRouting #MachineLearning
