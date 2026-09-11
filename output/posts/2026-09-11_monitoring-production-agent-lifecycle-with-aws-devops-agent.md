---
title: Monitoring production agent lifecycle with AWS DevOps Agent and AgentCore Evaluations
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/monitoring-production-agent-lifecycle-with-aws-devops-agent-and-agentcore-evaluations/
model: claude-code/sonnet
generated_at: '2026-09-11T19:52:03.894600'
score: 95
---

📌 【AWS 技術分享】CloudWatch 全綠，Agent 卻在亂轉單？監控多代理系統的兩層解法

TL;DR：AWS 用 AgentCore Evaluations + DevOps Agent 打造雙層監控，補上基礎設施指標抓不到的代理品質盲點。

想像一下：儀表板上所有指標都是綠色，模型呼叫成功、工具執行無誤、也回傳了結果，但使用者的需求其實完全沒被理解。這正是多代理系統上線後最棘手的狀況：系統「跑得動」不代表「做得對」。

🤔 **基礎設施正常，代理照樣失效**

文章舉出幾種典型場景：代理的執行角色少了一個 IAM 權限，導致無法呼叫 foundation model，卻不會拋出 500 錯誤，只是回傳空白內容；一個 prompt 沒設計好的 supervisor agent，開始把 20% 的請求誤導到錯誤的專家代理，但錯誤率毫無變化。更麻煩的是，基礎設施問題往往不會直接報錯，而是表現為「代理行為變差」——例如訂票代理不再完成訂位，但日誌顯示工具執行全部成功，因為問題發生在呼叫鏈第三層,沒有拋出例外。在多代理系統中，一個使用者請求可能觸發 supervisor agent 把工作分派給多個專家，彼此有各自的工具與模型呼叫，沒有固定的執行圖可供監測，失敗點可能出現在任何一次交接，傳播路徑也不可預測。

🧩 **兩層監控：品質看 AgentCore Evaluations，基礎設施看 DevOps Agent**

Amazon Bedrock AgentCore Evaluations 負責持續為線上互動評分，涵蓋 helpfulness、correctness、goal completion 三個面向，會依可設定比例抽樣正式環境請求，在背景進行評估，每個分數都附帶理由,說明是根據對話脈絡、使用的工具、任務需求得出的判斷。當品質指標下滑，系統會對近期低分的 session 做模式分析,找出代理是否持續選錯工具，或是答案內容正確但格式不友善，並產出具體建議，例如修改 prompt、調整工具選擇邏輯,或改進 orchestration 流程。

另一層是 AWS DevOps Agent,負責跨指標、日誌、錯誤模式監控系統健康度。一旦出狀況,它會自動拉取相關的 CloudWatch 日誌,建立受影響資源的拓撲圖,跨服務（IAM、Amazon Bedrock、agent runtime）關聯錯誤,追出失敗路徑並給出具體修復建議——不只是丟一個帶連結的警報,而是真的做調查,能把「空白回應」連回「缺少的 IAM 權限」,或把「timeout 暴增」連回「特定 Region 的 Bedrock 限流」。

🔍 **案例：四個代理組成的航空訂位 Swarm**

團隊用這套架構打造了一個真實的航空訂位系統,包含 Supervisor Agent（入口，用 think tool 規劃子任務並分派）、Flight Agent（搜尋航班與轉機）、User Agent（取得會員等級、票券、個人資料）、Reservation Agent（建立、修改、取消訂位並在異動前驗證）,採用 Swarm 模式運作。與傳統的中央路由不同,Swarm 中的代理共享工作記憶,並依自己查到的結果動態決定交接對象,而不是照著預先定義的執行計畫走。例如 Flight Agent 若找不到直飛航班,會自行執行轉機搜尋,找到選項後再交給 Reservation Agent 訂位。這種彈性能應付難以預測的請求結構,但也代表沒有固定的呼叫圖可供監測,每次執行路徑都可能不同,品質問題與基礎設施問題從外部看起來幾乎一模一樣,卻需要完全不同的應對方式。

🎯 **實務啟示**

對正在把多代理系統推上生產環境的工程團隊來說，光靠傳統的錯誤率、延遲等基礎設施指標不夠，需要另外一層專門評估「代理是否真的幫使用者達成目標」的機制，並搭配自動化的根因調查,才能形成監控、分析、改進、部署的持續回饋迴圈。

🔗 **來源**
- 標題：Monitoring production agent lifecycle with AWS DevOps Agent and AgentCore Evaluations
- 作者／機構：Meghana Ashok（AWS ML Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/monitoring-production-agent-lifecycle-with-aws-devops-agent-and-agentcore-evaluations/

#AWS #AgentObservability #MultiAgentSystems #AmazonBedrock #AgentCore #LLMOps #AIAgents #CloudWatch #ProductionAI #DevOps
