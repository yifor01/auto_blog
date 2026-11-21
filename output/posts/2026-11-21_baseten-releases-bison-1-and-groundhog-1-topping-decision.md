---
title: Baseten Releases Bison-1 and Groundhog-1, Topping Decision Model Index
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/20/baseten-bison-1-groundhog-1-gemma-4-decision-models/
model: claude-code/sonnet
generated_at: '2026-11-21T22:20:11.975105'
score: 97
---

📌 Baseten 決策模型 bison-1 奪冠,Gemma 4 底座、不生文字只吐機率

TL;DR:Baseten 新推出的 bison-1、groundhog-1 不寫文章,只回校準機率,登上決策模型榜首。

當大家還在比拼誰的模型寫作更流暢時,有一類模型從頭到尾不產生一個輸出 token,它的任務只有一個:在 yes/no、選項、分數之間,給出一個可信賴的機率數字。這次 Baseten 把這類「決策模型」的分數刷到了業界第一。

🤔 決策模型在解什麼問題

決策模型不寫文字,它回答的是是非題、選擇題與評分題,輸出的是校準過的機率,例如 P(yes),或帶有機率欄位的選項結果。Baseten 列出的目標場景包括工單分流、垂直郵件偵測、jailbreak guardrail,以及 LLM 路由判斷,這些場景共同的需求是:在一次呼叫裡,把完整的政策文件與對話歷史餵進去,換回一個能直接用來做決策的數字,而不是一段需要再解析的文字。

🧩 架構:Gemma 4 底座,bison-1 與 groundhog-1 的分工

bison-1 是 31B 參數的決策模型,基於 Google Gemma 4 31B 進行後訓練(post-train)。groundhog-1 則是較便宜的版本,微調自 Gemma 4 26B-A4B,這是一個每個 token 約啟用 4B 參數的混合專家(MoE)模型。這兩款是 Baseten 既有產品線 mammoth-1(27B)、elephant-1(9B)、joey-1(2B)之外的新成員,前三者都建立在 Qwen 骨幹上,而 bison-1 與 groundhog-1 是 Baseten 首次採用 Gemma 這個骨幹模型的產品。

請求格式上,一次呼叫帶入一個 state(文字,可選擇附帶圖片)和任意數量的 question。每個問題有三種類型:noul(是非題)、choice(具名選項)、score(有序等級)。模型在單一 prefill pass 中回答所有問題,不產生輸出 token。兩款模型都把上下文視窗從 16k 拉高到 128k,並支援圖片輸入,這讓完整政策文件與歷史記錄能一次塞進一次呼叫。

Baseten 將效能提升歸功於兩點:Gemma 這個底座本身,以及訓練資料中加入更多「soft label」。soft label 用機率目標取代單一正確答案,讓模型學會回報與實際命中率相符的不確定性,而不是死板地二選一。

📊 數據:Decision Index 與長上下文成績

在 Artificial Analysis Decision Index v2.1 上,bison-1 拿下 76 分,排名 19 個模型中的第一:

| 模型 | AA Decision Index v2.1 | Brier Score |
|---|---|---|
| bison-1 | 76 | 0.14 |
| d1.2-ultra(Liquid AI) | 75 | 0.15 |
| mammoth-1 | 71 | 未提供 |

Brier score 越低越好,bison-1 的 0.14 是榜上最低。這個指數由 6 項評測組成,權重最高的是 AA-Paperclip,佔 30%。bison-1 的模型卡顯示它在 6 個子項中拿下 4 項第一,知識密集型決策是相對弱項。

長上下文方面,Baseten 回報的 LongMemEval 成績如下:

| 模型 | LongMemEval M(128k) | LongMemEval S |
|---|---|---|
| bison-1 | 84.8 | 87.1 |
| groundhog-1 | 77.4 | 79.3 |

groundhog-1 目前還沒有官方的 Decision Index 分數,Baseten 預期它會接近 mammoth-1 的水準。

⚠️ 用之前要注意的限制

超過訓練長度上限的請求會被直接拒絕,而不是靜默截斷,原本假設 API 會自動截斷的管線,需要額外加上長度檢查。知識密集型決策是 bison-1 相對較弱的一塊,而 groundhog-1 的正式榜上成績目前仍是空白。Baseten 目前只提供 Hugging Face 上的開放 BF16 權重,沒有列出推論用 GPU 建議或量化版本。

🎯 實務啟示

兩款新模型沿用與舊款決策模型相同的 API,ID 分別是 decision-models/baseten-bison-latest 與 decision-models/baseten-groundhog-latest,從舊模型切換過去只需要改一個模型名稱。計價上 bison-1 每百萬 token 0.10 美元,與 mammoth-1 同價;groundhog-1 每百萬 token 0.035 美元,與 elephant-1 同價,且因為不產生輸出 token,這個價格就是全部成本。對於已經在用 Baseten 決策模型做路由、分流或守門邏輯的團隊,這次升級幾乎是零成本的效能提升。

🔗 來源
- 標題:Baseten Releases Bison-1 and Groundhog-1, Topping Decision Model Index
- 作者/機構:Asif Razzaq,MarkTechPost
- 連結:https://www.marktechpost.com/2026/11/20/baseten-bison-1-groundhog-1-gemma-4-decision-models/

#Baseten #Gemma4 #DecisionModels #LLMRouting #AIGuardrails #OpenWeights #MachineLearning #ModelBenchmark #AIInfra #CalibratedProbabilities
