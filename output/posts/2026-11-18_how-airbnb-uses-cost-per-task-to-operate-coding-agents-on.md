---
title: How Airbnb uses cost per task to operate coding agents on Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-airbnb-uses-cost-per-task-to-operate-coding-agents-on-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-11-18T23:45:22.509039'
score: 91
---

📌 Airbnb 怎麼用「每個任務的成本」管理 coding agent

TL;DR：Airbnb 用自建 eval 系統算出每個模型的 cost per task，再搭配 Amazon Bedrock 的監控數據決定要不要換模型。

五週內冒出八款新模型，到十月中旬，Airbnb 工程師透過 coding agent 發出的請求有三分之二已經轉向這些新模型。發布會上的 benchmark 圖表好看,但那不是你工程師真正在做的工作——Airbnb 選擇自己量出答案。

🤔 **問題：發布會的 benchmark 不等於你的工作**

Airbnb 內部有個叫 AirChat 的工具，供上千名工程師與相關角色每週執行 coding agent。這些 agent 的模型請求會經過 Airbnb 自建的 LLM gateway，再送進 Amazon Bedrock，由 AWS 在其環境內處理程式碼、prompt 與模型回應。

每次新模型上線，output token 用量、成本、延遲與容量可能同時改變，但官方公布的 benchmark 無法告訴 Airbnb，這個模型面對自己工程師的實際任務時表現如何。

🧩 **兩套系統並行：上線前 eval，上線後觀測**

Airbnb 的做法是雙軌並行。上線前，用自己的任務集跑 eval，量出每個模型（以及每個允許的 reasoning effort 設定）的分數與 cost per task。Cost per task 定義為：agent 完成一個任務所用掉的所有 token，依公開牌價換算出的成本。Bedrock 針對每個請求回報四種 token：未快取輸入、cache 讀取、cache 寫入與輸出，Airbnb 在一次 eval 跑裡把這四種全部計入單個任務的總成本中,並以該次跑所使用的當時公開牌價計算,平均成本也會納入表現不佳的嘗試。

這些分數與成本,被用來設定每個模型的「預設」(agent 工具預設使用的模型與 reasoning effort)和「effort ceiling」(該模型允許的最高 reasoning effort)。

上線後，則比對 CloudWatch 在 AWS/Bedrock namespace 底下的執行期訊號（token 數量、延遲、錯誤、throttle)與 gateway 的使用紀錄（依模型、客戶端、團隊、使用者紀錄，但僅用於彙總的成本與容量規劃)，看生產環境的實際表現是否與 eval 結果吻合；若不吻合,就要找出原因。

📊 **Reasoning effort 多花 2.5 倍成本，只換到 0.8 分**

Airbnb 測試過的一個模型顯示：把 reasoning effort 從低調到高，分數只提升 0.8 分，但 cost per task 卻變成 2.5 倍——這類數字直接決定了 effort ceiling 該設在哪裡。

另一個案例：延遲上升了 40%，但 TimeToFirstToken 和 OTPS（output tokens per second，Bedrock 沒有原生指標,需透過 metric math 自行推算)都維持平穩。追查後發現是系統 prompt 被改成要求「更詳盡的回答」，導致每次請求的 output token 數量上升了 50%——模型生成速度沒變，只是答案變長了。Airbnb 的結論是：把 prompt 修改和模型升級都當成一次「部署」，標註在監控儀表板上。

新模型上線當天，一個請求就能啟動一整輪 eval campaign，讓新模型跑過全部七個任務套件(suite)。數百個任務分散在各套件與多個雲端工作區執行，結果在 grader 評分完成的當下就會出現，幾個小時內就有第一批結果，隔天早上每個 suite 都有了分數與 cost per task，足以做出整個組織的部署決策。

每個任務是一個資料夾，裝著單次執行所需的一切；grader 會從凍結的資料重新算出正確答案，只有每項檢查都通過,agent 才能拿到 1 分的 reward。長任務會跑好幾輪，中間還有模擬審查者的回饋施壓，由一個模型 grader 依八個加權維度評分，每個維度 0 到 3 分。Airbnb 使用開源框架 Harbor 來在沙箱中執行這些 agent eval。

⚠️ **分數相近，不代表成本也相近**

文中提到的「model A」在 Airbnb 的 coding 任務上比先前最佳模型高出三分多分,且用的是同一個 grader 評分,但 cost per task 大致相同——這提醒我們,eval 分數的提升必須配合成本一起看，單看分數容易做出錯誤的部署決策。

🎯 **實務啟示**

要做到這種速度，前提是任務集早就寫好、可重複執行；若要複製這套做法，第一步是啟用帶 cost allocation tag 的 IAM role（而且要在開始收集資料「前」就啟用，因為啟用不會回溯補齊之前的成本數據），再搭配隔離的執行環境、Amazon Bedrock Guardrails 過濾有害或敏感內容,並把這些防護機制的延遲與成本也一併納入你的量測範圍。

🔗 **來源**
- 標題：How Airbnb uses cost per task to operate coding agents on Amazon Bedrock
- 作者／機構：Alan Yao（AWS Machine Learning Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/how-airbnb-uses-cost-per-task-to-operate-coding-agents-on-amazon-bedrock/

#AmazonBedrock #CodingAgents #Airbnb #LLMOps #CostPerTask #AWS #AgentEvaluation #Observability #CloudWatch #AIInfrastructure
