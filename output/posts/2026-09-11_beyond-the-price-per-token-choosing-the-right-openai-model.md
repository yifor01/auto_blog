---
title: 'Beyond the price per token: Choosing the right OpenAI model on Amazon Bedrock
  for your workload'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/beyond-the-price-per-token-choosing-the-right-openai-model-on-amazon-bedrock-for-your-workload/
model: claude-code/sonnet
generated_at: '2026-09-11T19:49:49.472685'
score: 95
---

📌 別只看每百萬 token 多少錢：Bedrock 上 OpenAI 模型的真實成本比較

TL;DR：AWS 開源基準工具實測顯示，多輪 agent 任務中「輪數」比單價更能決定真實成本，Bedrock 上的新模型未必比 mini/nano 貴。

一個模型每百萬 token 的報價比另一個便宜，但如果它要多繞三輪才能把任務做完，那省下的單價很可能連零頭都補不回來。AWS 用一套開源基準工具實測了這個問題，答案沒那麼直覺。

🤔 **生產工作負載買的是結果，不是 token**

企業比較模型時最常看的是每百萬 token 的價格，但實際的生產工作負載買的是「解決的工單」「寫完的研究簡報」「正確的財務摘要」這些結果。從報價單到結果之間，還隔著報價頁面完全看不到的乘數：模型答對的機率、答對要花多少 token，以及在 agentic 工作負載中要繞幾輪才能完成，因為每一輪都要重新送出不斷增長的對話內容。

🧩 **同一套 Responses API，五個模型一起測**

這次基準測試比較了 Amazon Bedrock 上的三個 OpenAI 模型（gpt-5.6-luna、gpt-5.6-terra、gpt-5.6-sol）與 OpenAI API 上兩個常見的成本優化基準模型（gpt-5.4-mini、gpt-5.4-nano）。開源工具 openai-on-aws/benchmarks-openai 讓所有五個模型都走同一套 Responses API client、同一套評測邏輯，只切換後端與模型 ID。需要留意的是，Bedrock 上的模型測試時關閉了 reasoning，OpenAI API 上的基準模型則使用預設設定，所以這是「實務部署設定」之間的比較，而非模型本身能力的受控比較。

評測涵蓋三個面向：AIME 競賽數學、GPQA Diamond 研究生等級科學題、MMLU-Pro 的單次呼叫準確度與成本；DeepSearchQA 多步驟網路研究任務的多輪 agent 軌跡；以及 GDPval 的真實職業交付物，依評分規則（rubric）評分。評分結合確定性檢查與 LLM 裁判（使用 gpt-5.5，非受測模型之一），評分提示詞的 hash 都記錄在每份結果檔案中。樣本數介於 48 到 198 之間，作者提醒小幅差距應視為方向性訊號，實際決策前建議在自己的工作負載上重跑一次評測。

📊 **輪數才是隱藏的帳單**

DeepSearchQA 用 50 題分層抽樣的多步驟研究問題，搭配真實的 `web_search` 與 `fetch_page` 工具跑完整的 agent 迴圈，答對標準是 F1 ≥ 0.7：

| 模型 | 平均輪數 | 累積 input token | 每個通過答案的成本 | 平均 F1 |
|---|---|---|---|---|
| gpt-5.4-mini | 7.6（多為重複搜尋） | 約 114k token | $0.40 | 0.39 |
| gpt-5.6-terra | 較少 | 約 50k token | $0.31 | 0.50 |
| gpt-5.6-luna | 少於 mini | — | $0.05 | — |
| gpt-5.4-nano | — | — | $0.07（18% 通過率） | — |

mini 每一輪都重新送出累積的搜尋結果，導致最終 input token 量達到 terra 的 2.3 倍；terra 雖然單價較高，但靠更少輪數與更高品質把每個通過答案的成本壓到 mini 的近八成，luna 則同時做到比 mini 更少的輪數與更低的成本。

在 48 題的 GDPval 職業交付物任務上（由平均 14 年經驗的專業人士撰寫評分規則，通過門檻為加權評分達 70% 以上）：

| 模型 | 每個通過交付物的成本 | 通過率 |
|---|---|---|
| gpt-5.6-luna | $0.010 | 56%（27/48） |
| gpt-5.4-mini | $0.030 | 42%（20/48） |
| gpt-5.4-nano | $0.012 | 35% |

三個 gpt-5.6 系列模型的評分規則得分都高於關閉 reasoning 的 mini 與 nano，差距在法律、護理、財務建議這類要求特定但書與完整結構的任務中最明顯。這是單次呼叫、沒有多輪效應的任務，重新計價前 mini、nano 每個通過交付物的成本確實較低，重新計價後 luna 反而拿到本次樣本中最低的觀察成本。需要留意的是輸出被限制在 8,192 token，導致 luna、terra、sol 分別有 6、9、7 份交付物被截斷，mini 為 0 份、nano 為 1 份，這是在此輸出上限下的真實結果，提高上限可能改善品質但也可能推升成本，作者建議兩者一併測試。

延遲方面，2026 年 7 月於 us-west-2 的單區域快照測試顯示，Bedrock 上 luna 的中位數 TTFT 平均低 21%，terra 平均低 5%（涵蓋 12 組對應設定）；輸出達 500 token 以上時，luna 在 Bedrock 上的吞吐量平均高 43%（terra 高 4%）；觀察到的最差情況 TTFT 對中位數比值，Bedrock 為 2.1–2.5 倍，OpenAI API 為 4.6–6.6 倍，代表尾端延遲波動較小，但這不是 p99 延遲的估計值，且共享服務的表現會隨負載變動，應視為一次性快照並自行重新量測。

🎯 **實務啟示**

如果你現在跑的是 mini 或 nano，遷移與否取決於工作負載的形狀：單次呼叫、輸出短的任務，價格差距接近報價單上的數字；但只要工作負載涉及串接工具呼叫的多輪 agent（研究、多跳查詢、迭代檢索），務必把「軌跡成本」而非單次呼叫成本納入基準測試，報價頁面永遠看不到輪數這個變數。

🔗 **來源**
- 標題：Beyond the price per token: Choosing the right OpenAI model on Amazon Bedrock for your workload
- 作者／機構：Nick McCarthy
- 連結：https://aws.amazon.com/blogs/machine-learning/beyond-the-price-per-token-choosing-the-right-openai-model-on-amazon-bedrock-for-your-workload/

#AmazonBedrock #OpenAI #LLMBenchmark #AIAgents #CostOptimization #MLOps #GDPval #AIME #ModelSelection #GenerativeAI
