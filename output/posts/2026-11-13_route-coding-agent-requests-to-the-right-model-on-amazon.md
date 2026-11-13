---
title: Route coding agent requests to the right model on Amazon Bedrock with NVIDIA
  NeMo Switchyard
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/route-coding-agent-requests-to-the-right-model-on-amazon-bedrock-with-nvidia-nemo-switchyard/
model: claude-code/sonnet
generated_at: '2026-11-13T22:51:17.369877'
score: 88
---

📌 用 NeMo Switchyard 依任務成本路由 Coding Agent

TL;DR：AWS 示範如何用 NVIDIA NeMo Switchyard 在 Bedrock 上路由 coding agent 請求，並改用「每個成功任務的成本」取代單純的 token 單價來評估路由策略。

一個 coding agent 任務可能只呼叫模型一次，也可能呼叫幾十次——開發者真正付的錢是整個任務跑完的總花費，不是某一次 API 呼叫的單價。

🤔 **token 單價算不出任務真正的成本**

像 Claude Code、OpenAI Codex CLI 這類 coding agent 的工作方式是：接到一個修改需求後，讀檔、改程式碼、跑測試，反覆直到完成。每個任務需要多少輪模型呼叫、每輪要重播多少歷史紀錄、任務失敗要重試幾次甚至永遠跑不完，都會影響總花費——而這些都不是單純的 token 價格能反映出來的。因此文章主張：路由策略應該用 cost per solved task 來評估，也就是所有跑的總花費除以測試通過的次數。

🧩 **Switchyard 的兩種路由策略**

NVIDIA NeMo Switchyard 是一個開源函式庫，用來幫 agent 決定每個請求交給哪個模型處理，使用者需定義可用模型與路由策略。它的 LiteLLM 整合支援兩種策略：

- **Stage routing**：讀取最近的工具呼叫活動與請求歷史中的結果，從兩個候選模型中挑一個。
- **Random routing**：依設定的權重在多個模型間隨機分配，適合做流量分配與 A/B 測試。

LiteLLM 本身近期也內建了一個以 Switchyard stage router 為基礎的 auto-router 策略可供參考。而 Classifier-backed 的策略（如 Task routing、Composite routing）需要額外的中間模型呼叫，目前這套 LiteLLM 整合並不支援。

🧩 **部署架構**

本文用 AWS CDK 把 LiteLLM（開源 LLM gateway）搭配 Switchyard 路由外掛，部署在私有子網路中的 Amazon ECS on Fargate 容器裡，並由 LiteLLM 呼叫 Amazon Bedrock 上的模型。具體設計包括：LiteLLM 在容器內監聽 4000 埠，作為負載平衡器的目標，任務的安全群組只允許負載平衡器存取；Amazon ECR 存放 gateway 映像檔；AWS Secrets Manager 產生 gateway key；設定檔透過 `LITELLM_CONFIG_TEXT` 與 `SWITCHYARD_CONFIG_TEXT` 兩個環境變數傳入，啟動腳本會寫進 `/tmp` 後再啟動 LiteLLM；日誌集中送往一個 CloudWatch log group（保留 30 天），並搭配 Container Insights 收集指標；VPC 跨兩個可用區，由一個 NAT gateway 提供對外存取。

設定上，Stage 路由需要恰好兩個候選模型，且要先列出能力較強的模型、再列效率較高的模型，因為 Stage 會依宣告順序讀取角色；範例設定了 `claude-opus-5-5` 與 `nemotron-super-3-120b` 兩個單模型 baseline 群組，方便和路由後的群組做成本與通過率的對照。所有模型都透過 `bedrock/converse/<id>` 路由呼叫 Amazon Bedrock Converse API。

⚠️ **這仍是實驗性範例**

官方特別強調：範例所用的 `switchyard-server 0.3.0` 在 NVIDIA 文件中被標示為 demo／evaluation 用途，設定與 API 可能隨版本改變；這套 LiteLLM 整合本身也是實驗性質。文章建議在非生產環境帳號中部署測試，並與資安與法遵團隊確認是否符合組織規範。另外，若使用 global 前綴的跨區域推論設定檔，Bedrock 可能在全球任一受支援的商用 AWS 區域處理請求，若處理地點有合規考量，應改用地理性設定檔或指定區域內的模型 ID。

🎯 **實務啟示**

對已經在用 coding agent 卻苦於 token 帳單難以預測的團隊，這套方法提供了一個具體可量化的評估框架（cost per solved task），以及一份可直接部署、能做 A/B 對照的 CDK 範例，適合用來驗證「把部分請求路由到效率模型」是否真的划算。但部署前務必先檢視由設定檔推導出的 IAM 權限範圍，並在非生產帳號中完整測試。

🔗 **來源**
- 標題：Route coding agent requests to the right model on Amazon Bedrock with NVIDIA NeMo Switchyard
- 作者／機構：Aswath Ram A Srinivasan（AWS）
- 連結：https://aws.amazon.com/blogs/machine-learning/route-coding-agent-requests-to-the-right-model-on-amazon-bedrock-with-nvidia-nemo-switchyard/

#CodingAgents #NVIDIA #AmazonBedrock #LiteLLM #LLMRouting #AWS #ClaudeCode #AIInfrastructure #CostOptimization #MachineLearning
