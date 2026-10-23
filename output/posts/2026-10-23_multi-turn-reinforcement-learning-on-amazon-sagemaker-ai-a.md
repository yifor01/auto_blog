---
title: 'Multi-Turn Reinforcement Learning on Amazon SageMaker AI: A hands-on guide'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/multi-turn-reinforcement-learning-on-amazon-sagemaker-ai-a-hands-on-guide/
model: claude-code/sonnet
generated_at: '2026-10-23T20:42:18.297845'
score: 92
---

📌 Wordle 教會 gpt-oss-20b 的事：多輪 RL 實戰拆解

TL;DR：AWS 用 Wordle 示範 SageMaker AI 的多輪 RL 流程，把 gpt-oss-20b 解題率從 61% 練到 84%，訓練只花約 339 美元。

一個會填報帳表單或分流客服工單的 agent，根本沒有「標準答案序列」可以模仿，唯一可靠的訊號是整個任務最後有沒有成功。監督式微調拿不到這種標籤，單輪強化學習也沒辦法把三步之後才出現的獎勵，正確地歸因到當下的決策。這正是 Amazon SageMaker AI 的 Multi-Turn Reinforcement Learning（MTRL）要解決的問題。

🤔 **用 Wordle 當教學範例，因為規則少、回饋即時**

Wordle 是六次機會猜五字母單字的遊戲，每次猜測後每個字母會標示綠（位置正確）、黃（字對位錯）或灰（不在字中）。它很適合用來示範 MTRL：規則簡單、每次猜測都依賴上一次的回饋、結果又能被客觀評分。作者強調 Wordle 只是教學範例，前沿模型本來就玩得不錯；實務上 MTRL 真正的用途，是把一個小型、低成本的模型，練到擅長某個企業內部特有的多步驟工作流程，而這條 pipeline 可以直接套用到那類場景。

🧩 **系統分兩半：SageMaker 管訓練，AgentCore 管執行**

整個系統由兩部分組成：SageMaker AI 擁有訓練任務與正在訓練的 policy model；Amazon Bedrock AgentCore 則負責架設 agent、Wordle 環境與獎勵函式。每一次 rollout，MTRL 服務會呼叫 AgentCore runtime 並傳入一筆訓練資料（一個秘密單字）。runtime 裡的 Strands agent 透過 SageMaker Job Runtime 提供的 OpenAI 相容端點呼叫 policy model，模型用唯一的 guess_word 工具最多猜六次，每次猜測後環境回傳逐字母回饋與已知資訊摘要；遊戲結束時，agent 回傳單一個獎勵值。Group Relative Policy Optimization（GRPO）接著利用同一個單字多次 rollout 之間的獎勵差異，去更新套在 policy model 上的 LoRA adapter。

MTRL 本身是 serverless 的：你只需要選定 base model，服務會自動佈建訓練與取樣所需的基礎設施，不用自己挑 instance 或規劃叢集。作者選擇 GPT-OSS-20B，原因是它在可選的幾個 base model 中每 token 價格最低，而且 reasoning effort 可以逐次請求調整。計費依照 prefill、sample、train 三個維度，各自以 token 數量計價，其中 train 維度的佔比最高，且會隨對話軌跡長度增加而放大，代表較短的遊戲與較精簡的推理過程能直接省錢。

📊 **100 步訓練，339 美元換來 23 個百分點的提升**

這次 100 步的訓練共消耗 4.916 億個 prefill token、1.597 億個 sample token、6.433 億個 train token，橫跨 105,486 次 rollout，耗時 12 小時 40 分鐘。以 us-east-1 當時的 GPT-OSS-20B 牌價計算，總成本約 339 美元；另外 AgentCore runtime 依 vCPU 與記憶體使用量另計，依 CloudWatch 用量指標約 79 美元。最終效果是：在預設 reasoning effort 下，held-out 單字的解題率從 61% 提升到 84%；而在訓練時使用的低 reasoning effort 下，解題率更是從 15% 大幅拉高到 69%。作者也指出，將 REASONING_EFFORT 設為 low，比起 medium 可減少 63% 到 83% 的 sample token 用量，是壓低訓練成本的重要手段。

💡 **部署時容易踩的雷：IAM 信任主體寫錯**

文章特別點出兩個需要手動建立的 IAM 角色與一個常見錯誤：Agent runtime role 由 agentcore deploy 自動建立，信任 bedrock-agentcore.amazonaws.com 並需要 AmazonSageMakerJobRuntimeAccess；Training job role 則要自己建立，必須信任 job.sagemaker.amazonaws.com（而非一般文件常見的 sagemaker.amazonaws.com）並同時允許 sts:AssumeRole 與 sts:TagSession，否則 CreateJob 會先報「Could not assume role」，且要重試幾次後才會顯示正確的信任主體名稱。另外，agent 進入點必須用 BedrockAgentCoreApp 搭配 @app.entrypoint 包住 sagemaker_rft_handler，且 entrypoint decorator 要放在最外層，否則每次呼叫都會在 30 秒後逾時。作者建議在真正花費 GPU 資源前，先用倉庫附帶的 payload.json 送一個假的 job ARN，若能在 CloudWatch 日誌中看到 agent 完成 parsing、驗證並收到「Could not find job」的 400 錯誤，就代表整條鏈路是通的。

🎯 **實務啟示**

MTRL 的價值不在於讓模型打敗 Wordle，而是提供了一條「只要能打分、不需要標準答案」的訓練路徑。對於有明確業務流程、但缺乏標註資料的多步驟任務（如內部工單分流、審批流程），這類 pipeline 可以直接拿既有的 reward function 套用；而部署時的 IAM 信任主體與逾時陷阱，值得在正式投產前先用最小 payload 驗證過一輪。

🔗 **來源**
- 標題：Multi-Turn Reinforcement Learning on Amazon SageMaker AI: A hands-on guide
- 作者／機構：Daniel Quang, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/multi-turn-reinforcement-learning-on-amazon-sagemaker-ai-a-hands-on-guide/

#ReinforcementLearning #AmazonSageMaker #AgentCore #MultiTurnRL #GRPO #LoRA #AWS #AIAgents #Wordle #MachineLearning
