---
title: What is Decision 3.0? vLLM Semantic Router’s New Open Decision Models
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/11/what-is-decision-3-0-vllm-semantic-routers-new-open-decision-models/
model: claude-code/sonnet
generated_at: '2026-10-12T23:50:37.200172'
score: 97
---

📌 vLLM Semantic Router推Decision 3.0：用機率取代文字輸出的決策模型

TL;DR：5個尺寸、Apache-2.0授權的多模態決策模型,讓你免解析LLM輸出就能做分類、路由與guardrail。

如果你的系統需要判斷「這段內容該不該放行」「這張圖是不是違規」,過去多半得丟給LLM生成文字再寫一堆regex去解析。vLLM Semantic Router團隊發布的Decision 3.0,想解決的就是這個麻煩。

🤔 **為誰而做:路由器與guardrail不需要生成文字**

Decision 3.0是一組開源決策模型,輸入可以是文字或JSON狀態,再加上可選的圖片,搭配一組具名問題,模型會對每個問題直接回傳機率,而不是一段話。問題類型分三種:Choice(選項)、Yes/No、或是Score(分數量尺)。團隊把這稱為路由器與guardrail的「system one」模式:不用再prompt一個LLM然後解析它的輸出,而是直接拿到可以設閾值的校準分數。

🧩 **架構:Qwen底模+視覺編碼器,5個尺寸全開源**

共有5個尺寸,從0.8B到27B,全部採用Apache-2.0授權。每個模型都是Qwen底模的fine-tune:27B的d3建在Qwen3.8-27B上,其餘4個較小尺寸(0.8B、2B、4B、9B)建在Qwen3.5 checkpoint上。每個尺寸都搭載視覺編碼器:d3-lite是0.10B,d3-nano與d3-mini是0.33B,d3-flash與d3是0.46B。輸入端可接受多張PNG、JPEG或WebP圖片,每張最高讀取1.6百萬像素,每個問題都會看到所有圖片,且每個問題各自跑一次forward pass。

🧩 **怎麼用**

安裝需要transformers==5.17.0,若安裝選用的flash-linear-attention套件,可以加速linear-attention層的運算;載入模型時需要設定trust_remote_code=True。

📊 **跑分:中等尺寸就打贏前代大尺寸**

團隊在自家的Jev Decision Index 0.3.1(對TypeSafe的Jev決策系統的開放復現排行榜)上公布內部評測:文字任務上d3拿下64.1分,領先Perplexity Decider v1.1的62.8分與Jev本身的60.1分;但在公開測試集上,Torchcast Decision 27B反而拿到更高的65.1分(對比d3的64.9分)。視覺任務上,d3拿71.6分,高於Perplexity Decider v1.1的70.6分。

最值得注意的是尺寸效率:9B的d3-flash拿下59.0分,反超上一代Decision 2.0的27B版本(55.9分);在公開測試集上,相對Decision 2.0的進步幅度從+8.0分(27B)到+15.1分(0.8B)都有。不過表現並非全面領先:在公開視覺任務上,d3在InfographicVQA拿97.3分、Mind2Web拿89.9分(皆為近似復現版本),但在MMMU-Pro視覺題只拿46.2分,Hateful Memes內容審核更只有44.6分。所有模型都在AMD Instinct MI325X GPU上訓練完成。

⚠️ **限制**

跑分顯示Decision 3.0在某些公開評測項目上不是絕對第一(如文字公開測試集輸給Torchcast、視覺上在MMMU-Pro與內容審核任務偏弱),而且目前公開的跑分主要來自團隊內部評測與Jev Decision Index,尚待更多第三方驗證。

🎯 **實務啟示**

如果你的系統裡有「分類」「路由」「內容把關」這類需要明確機率而非自由文字的環節,Decision 3.0提供了一條現成路:選一個符合延遲/成本預算的尺寸(從0.8B到27B),用named questions一次問完多個判斷,直接拿機率做閾值判斷,省掉prompt engineering與輸出解析的工程負擔。

🔗 **來源**
- 標題：What is Decision 3.0? vLLM Semantic Router's New Open Decision Models
- 作者／機構：Michal Sutter，MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/11/what-is-decision-3-0-vllm-semantic-routers-new-open-decision-models/

#VLLM #SemanticRouter #OpenSource #Qwen #MultimodalAI #AIGuardrails #ModelRouting #ApacheLicense #DecisionModels #LLMOps
