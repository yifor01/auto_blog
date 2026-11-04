---
title: Use decision models with Amazon Bedrock AgentCore Evaluations
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/use-decision-models-with-amazon-bedrock-agentcore-evaluations/
model: claude-code/sonnet
generated_at: '2026-11-04T23:00:21.186374'
score: 74
---

📌 AgentCore Evaluations 新增決策模型：用機率取代「感覺對不對」

TL;DR：AWS 讓 Bedrock AgentCore Evaluations 可接入決策模型，把部分評估問題變成可設定閾值的機率分數。

評估一個 agent 的回應時，很多問題其實不需要長篇解釋，只需要一個「是/否」或「幾分」的答案，而且這個答案最好每次都穩定一致。這正是 Amazon Bedrock AgentCore Evaluations 這次新增「決策模型（decision model）」支援要解決的問題。

🤔 **LLM 評審的分數會飄，但有些問題其實很窄**

AgentCore Evaluations 會在 agent 的整個生命週期中評分：開發階段的即時評估、針對已儲存 session 的批次任務，以及對生產環境流量的線上評估。目前內建 15 種評估器，也支援自訂評估器，分為 LLM-as-a-judge（用 Bedrock 上的模型依你的指示與評分量表打分）與 code-based evaluator（在 AWS Lambda 裡執行你自己的邏輯，可呼叫任何外部系統、模型或 API）。

問題在於：像「這個回應有沒有偏離政策？」「這個工具呼叫能不能批准？」這類問題,如果每次都丟給通用 LLM 自由生成文字再解讀信心程度，結果會隨 run 不同而有落差。

🧩 **決策模型：固定選項 + 校準過的機率**

決策模型是一種專門訓練來「從固定選項中選一個」的小型模型，回傳的是一個機率分布，而不是帶理由的自由文字分數。這讓分數可以被直接閾值化、聚合、自動化處理。文章介紹了兩種決策模型後端：TypeSafe 的託管模型 Jev，以及 Strands Agents 團隊開源的 20 億參數模型 Strands Decider 2B。兩者都支援三種題型：

- **noul 問題**：是/否題，回傳 0（不是）到 1（是）之間的機率。
- **choice 問題**：最多 255 個選項中選一個,回傳最可能的選項、完整分布與信心值。
- **score 問題**：2 到 10 個有序等級中選一個,回傳機率加權分數、各等級分布與信心值。

像「這個回應裡的每一項事實是否都有工具結果支持？」就是一個 noul 問題,而「依四級量表評估這個回應的有用程度」就是一個 score 問題。

📊 **用 HR Assistant 示範三種評估器並行運作**

文章以一個用 Strands Agents 建構、部署在 AgentCore runtime 上的 HR Assistant agent 作示範。這個 agent 透過五個工具回答員工關於 PTO 餘額、PTO 申請、HR 政策、福利與薪資單的問題（皆為固定 mock 資料,方便驗證評估器行為)。執行 evaluate.py 預設會跑出確定性檢查（code-based checks）加上 LLM-as-a-judge 評分的管線;決策模型評估器是「選用」的,加上 `--with-jev --jev-secret-arn <ARN>` 即可部署 jev-evaluator,並註冊 JevGroundedness、JevHelpfulness、JevGoalCompletion 三個評估器;加上 `--with-decider`（可搭配 `--decider-ec2` 自動佈建 EC2、安全群組、IAM 角色與 Lambda VPC 設定）則會用 Strands Decider 2B 跑同樣三種評估。

每個決策模型後端都是透過 code-based evaluator 的框架,在 Lambda 中呼叫模型,再把機率結果轉回 AgentCore 的評估結果。Lambda 收到的是 agent 的 OpenTelemetry spans,由 spans.py 模組統一格式後送入決策模型;trace 層級評估只送目標回合與簡短前情,session 層級評估則送入完整對話。

💡 **決策模型不是取代 LLM 評審,而是篩選層**

文中明確定位:決策模型不是要取代內建的 LLM-as-a-judge 評估器。當評估需要連結證據、找出缺漏資訊或深入推理時,LLM 評審的解釋能力仍不可替代。但因為決策模型可以在同一次請求中針對同一個狀態回答多個問題,它更適合當作篩選層,先用 pass/fail 訊號跑過所有指標,挑出真正值得讓 LLM 評審深入檢視的回合。

🎯 **實務啟示**

如果你的評估 pipeline 裡有大量重複、窄範圍的判斷題（例如「這次工具呼叫安全嗎」「回答有沒有跑題」），值得先用自己的流量驗證一個決策模型的判斷是否可信，驗證通過後就能把它接成篩選層,省下讓 LLM 評審處理每一筆資料的成本,把深度分析留給真正有疑慮的樣本。

🔗 **來源**
- 標題：Use decision models with Amazon Bedrock AgentCore Evaluations
- 作者／機構：Sungyeon Kim, AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/use-decision-models-with-amazon-bedrock-agentcore-evaluations/

#AWS #BedrockAgentCore #AIEvaluation #AgenticAI #LLMasJudge #DecisionModels #MLOps #StrandsAgents #AIObservability #MachineLearning
