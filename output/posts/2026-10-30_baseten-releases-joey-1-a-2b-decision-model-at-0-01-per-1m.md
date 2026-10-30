---
title: Baseten Releases joey-1, a 2B Decision Model at $0.01 per 1M Tokens
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/29/baseten-joey-1-2b-decision-model/
model: claude-code/sonnet
generated_at: '2026-10-30T21:42:17.442836'
score: 88
---

📌 Baseten joey-1：2B 決策模型，每百萬 token 只要 $0.01

TL;DR：joey-1 用單次 forward pass 回傳校準過的機率而非生成文字，鎖定高流量路由與護欄檢查，開源權重加超低定價。

如果你的應用其實只需要回答「是不是」或「選哪一個」，卻讓 LLM 跑一次完整的文字生成，再自己寫程式碼解析輸出，這中間浪費掉的延遲與 token 成本，正是 Baseten 旗下研究團隊 Base Labs 想解決的問題。

🤔 **為高流量路由與護欄檢查而生**

joey-1 是一個 2B 參數的「決策模型」，目標情境是高流量的路由、分類與護欄（guardrail）檢查。使用方式是送入一個狀態（文字或影像）加上一個或多個問題，模型針對每個問題的每個選項回傳一個機率，不輸出需要你自己解析的自由文字。這是 Baseten 決策模型家族的第三個成員，前面已經推出 27B 的 mammoth-1 與 9B 的 elephant-1，三者共用訓練資料與 /v1/systemone API，切換模型只需改一行程式碼。

🧩 **共享前綴一次回答多個問題**

Base Labs 以 Qwen3.5-2B 為基礎進行語言模型的全參數微調，視覺編碼器則維持凍結。架構上，full-attention 層使用 block-bidirectional mask，所有問題都從同一個共享前綴（shared-prefix）的 prefill 回答，因此追加問題帶來的成本增量很小。模型支援設定信心門檻（confidence threshold），遇到不確定的答案可以往上升級給 elephant-1、mammoth-1，或直接交給人工處理。

📊 **延遲與定價的取捨**

| 指標 | joey-1 | elephant-1 | mammoth-1 |
|---|---|---|---|
| 參數規模 | 2B | 9B | 27B |
| 輸入定價（每百萬 token） | $0.01 | $0.035 | $0.10 |
| P50 端到端延遲（2,000 token 請求） | 20 ms | 49 ms | — |

Baseten 官方舉例：每月 1,000 萬張支援單、每張約 500 token，總量 50 億 token，用 joey-1 約花費 50 美元，換成 mammoth-1 則要約 500 美元。延遲方面，joey-1 的 P50 約比 elephant-1 快 2.5 倍，部落格另宣稱比「同類決策模型」快 5 倍，但未具名比較對象。

在 Jev Decision Index 0.4 公開測試集上，joey-1 得分 63.30，在 230 個模型中排名第 37，也是 4B 以下模型中的最高分；同集測試中 Cloudflare 27B 的 Clef 得分 61.71，Jev 1.14 得分 60.70。joey-1 在五個子領域中有四個領域贏過 Jev 1.14（包括語言、工具與檢索），但在每個領域都落後自家的 elephant-1。在 Baseten 複製的 Artificial Analysis Decision Index 上，joey-1 得分 62.9，mammoth-1 為 65.9。以上分數均為 Baseten 在其 model card 上自評。

⚠️ **小尺寸仍有代價，數字需要保留懷疑**

joey-1 在每個測試領域都輸給自家更大的 elephant-1，說明把規模壓到 2B 並非沒有效能犧牲；而所有基準分數都是 Baseten 自行公布，延遲數字也不能直接拿來跟 Cloudflare 自家測得的 Decision Index 0.2.1 結果比較，因為測試平臺不同。

🎯 **實務啟示**

joey-1 的權重在 Hugging Face 上以 MIT 授權開放，也已上架 OpenRouter，並可透過 Baseten Training Jobs 的 fine-tuning cookbook 進行客製微調。對需要高吞吐路由、分類或 guardrail 的團隊來說，這類決策模型提供了一個便宜且可自行微調的前置篩選層，搭配信心門檻把不確定的案例升級給更大模型，是一種務實的 cascade 架構思路。

🔗 **來源**
- 標題：Baseten Releases joey-1, a 2B Decision Model at $0.01 per 1M Tokens
- 作者／機構：Asif Razzaq
- 連結：https://www.marktechpost.com/2026/10/29/baseten-joey-1-2b-decision-model/

#Baseten #DecisionModel #LLMRouting #OpenWeights #Qwen #MachineLearning #Guardrails #ModelServing #AIInfrastructure #CostEfficientAI
