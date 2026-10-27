---
title: 'vLLM Semantic Router Releases d3-ultra: A 27B Open Multimodal Decision Model'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/26/vllm-semantic-router-d3-ultra-27b-multimodal-decision-model/
model: claude-code/sonnet
generated_at: '2026-10-27T21:34:15.808539'
score: 92
---

📌 d3-ultra:27B開源模型,一次讀取回答所有問題

TL;DR:vLLM Semantic Router開源27B多模態決策模型d3-ultra,單次推論就能回傳一組問題的機率答案。

大多數開源模型發布都在比誰寫得更流暢,d3-ultra反其道而行——它根本不生成文字,只回傳機率。

🤔 **它解決的不是生成,是「分類與判斷」**

d3-ultra是vLLM Semantic Router team推出的System One決策模型,專門用來回答「typed questions」並給出機率,而不是寫一段回答。對開發者而言,這代表routing(路由決策)、classification(分類)、視覺定位(visual grounding)與影片檢查,都能靠一次open-weight呼叫完成。它是Decision 3.0家族的最新成員,這個家族涵蓋從0.6B到27B的模型規模,並以Apache-2.0授權釋出。

🧩 **核心設計:state once,一次讀取、多題作答**

d3-ultra的核心概念是「state once」——模型針對每個請求只讀取一次輸入(文字或JSON,加上圖片或影片),然後針對同一份輸入提出的一整組問題逐一作答。問題本身可以帶有型別,圖片甚至可以直接出現在問題或選項裡,例如一題測驗先秀出一張照片,再提供4張蝕刻畫作為選項讓模型選。

其中Box類型的答案設計得很明確:永遠只回傳1個方框加上一個信心值,信心值接近0就代表目標根本不在圖片裡。輸入長度若超過131,072 tokens,系統會直接回傳max_length_exceeded錯誤,而不是悄悄把內容截斷。

架構上,模型卡顯示d3-ultra採用Qwen3.5架構骨幹,共64層,其中48層是linear-attention層、16層是full-attention層。模型卡並未指明d3-ultra自己的base checkpoint,但vLLM的訓練說明指出同系列的d3是從Qwen3.8-27B訓練而來。

📊 **跟誰比、比出什麼結果**

研究團隊在兩組自建測試上,將d3-ultra與GLiDE V1.2、d1-ultra、d3-turbo、d3以及Jev 1.14做比較,分數經過chance-corrected校正(0代表純猜測,100代表滿分)。

SR-Text測試包含10,411筆文字請求、共73,495道問題,多數題目改寫自34個公開benchmark,另有4,896道題目來自43個全新任務類型(例如SQL檢查、工單路由)。結果顯示d3-ultra在幾乎所有領域都領先,唯獨在「藝術與人類品味」這個項目上,d1-ultra以90.8分對89.6分略勝一籌,但差距在誤差範圍內。

SR-Box測試則包含5,678道Box類型問題,涵蓋10個領域、4,984張圖片,以IoU 0.5作為正確判定門檻。d3-ultra在10個領域與9個領域分別拿下58.2%與54.6%,而d3-turbo拿下60.0%與59.6%,Jev 1.14則是45.7%與46.9%。團隊指出,d3-turbo在自然影像上表現更強,d3-ultra則在圖表類影像上領先。

延遲方面,在單張AMD Instinct MI325X顯卡上用AutoModel測試,針對一張照片提出一個問題需要304毫秒;若一次問255個問題,總共只需2.16秒,平均每多一題只增加約7.3毫秒。

⚠️ **不是全面最強,挑對場景才划算**

從數據看,d3-ultra並非在所有面向都是最佳解:自然影像的框選定位上輸給同系列的d3-turbo,藝術品味判斷上也被d1-ultra小幅超車。選型時應對照自己的任務類型(文字分類 vs. 自然影像框選 vs. 圖表理解)挑選對應的家族成員,而不是預設最大模型就是最優解。

🎯 **適合拿來做什麼**

對需要在agent pipeline前端加一層「判斷層」的團隊而言,d3-ultra這類System One決策模型提供了一個現成選項:把路由、分類、視覺定位這些原本要靠多次生成式呼叫拼湊的工作,收斂成一次推論、多個機率輸出。Apache-2.0授權加上公開的模型卡、GitHub repo與Hugging Face Space,也讓評估與落地的門檻相對低。

🔗 **來源**
- 標題:vLLM Semantic Router Releases d3-ultra: A 27B Open Multimodal Decision Model
- 作者/機構:Asif Razzaq, MarkTechPost
- 連結:https://www.marktechpost.com/2026/10/26/vllm-semantic-router-d3-ultra-27b-multimodal-decision-model/

#OpenSource #MultimodalAI #DecisionModel #vLLM #LLMRouting #Qwen #ApacheLicense #AIInfrastructure #MachineLearning #ModelBenchmark
