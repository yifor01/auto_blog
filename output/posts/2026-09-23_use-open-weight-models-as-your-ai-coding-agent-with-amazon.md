---
title: Use open weight models as your AI coding agent with Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/use-open-weight-models-as-your-ai-coding-agent-with-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-09-23T20:38:46.607849'
score: 87
---

📌 開權重模型也能當 Coding Agent：OpenCode 搭配 Amazon Bedrock 實測

TL;DR：OpenCode 串接 Bedrock 上的開權重模型，資料留在自家 AWS 帳戶、按用量計費。

多數 AI coding agent 有一個共同的前提：你的程式碼要送到第三方 API。這對有資料留存（data residency）要求、成本敏感，或不想被單一模型供應商綁死的團隊來說，是實打實的摩擦。AWS 這篇文章示範了另一條路：把開權重模型部署在 Amazon Bedrock 上，搭配開源的終端機原生 coding agent OpenCode，讓推論全程留在自己的 AWS 帳戶內，不用自建 GPU 基礎設施，也不用綁死單一模型。

🤔 **為什麼開權重模型正在成為選項**

文章引用 McKinsey 的 2025 年報告《Open-source technology in the age of AI》指出，76% 的組織預期會增加開源 AI 的使用，而領先的 AI 採用者採用開權重模型的可能性高出 40%。文章列出五個驅動因素：效能可以打平甚至超越專有模型（CrowdStrike 微調過的 NVIDIA Nemotron 在有效查詢準確率上達到 96%，優於 GPT-4o 的 61% 與 Claude Sonnet 4.5 的 94%）；成本效率（Gartner 2026 年分析指出，agentic 工作流會把 token 消耗放大 5 到 30 倍，讓每 token 成本變得至關重要，在每月數百萬次對話的規模下，換用 Bedrock 上的開權重模型能降低年化成本）；客製化與控制（開權重模型支援微調、蒸餾與領域調整，讓較小模型可以取代昂貴的通用模型）；模型彈性（換模型只是 Bedrock API 的一個參數變更）；以及透明度（可檢視的模型架構有利於受監管產業的 AI 治理需求）。

🧩 **架構：OpenCode 在本地跑，推論在你的 AWS 帳戶內完成**

OpenCode 是用 Go 寫成的開源終端機原生 coding agent，能讀寫檔案、執行 shell 指令，並透過 Language Server Protocol（LSP）診斷理解專案結構，目前串接超過 75 個 LLM 供應商，其中包含 Amazon Bedrock。整體架構分兩部分：OpenCode 以 TUI（terminal user interface）在你本機執行，透過 Amazon Bedrock Converse API 發送推論請求；Bedrock 則以全代管、無伺服器端點的形式承載模型。每一次請求都由 AWS IAM 驗證，AWS CloudTrail 記錄 API 活動，開權重模型與專有模型共用同一套 IAM 政策、CloudTrail 日誌、AWS PrivateLink 連線與加密控制，不需要另外建一套安全機制。Bedrock 提供三種計價層級：Priority 給延遲敏感的正式環境、Standard 是依 token 用量計費的隨選推論、Flex 則以低 50% 的成本服務可容忍延遲變動的工作負載；預設額度是每分鐘 1 億 tokens、每分鐘 1 萬次請求。在資料留存方面，透過 global 跨區域推論設定檔（如 `global.moonshotai.kimi-k3`）可將請求路由到任一受支援的商用 AWS 區域，成本比地理區域專屬設定檔（如 `us.moonshotai.kimi-k3`）約低 10%；若有明確的地理限制需求，則可改用地理專屬設定檔把處理範圍鎖在特定地理區域內。

OpenCode 的 agent 系統支援把不同模型指派給不同角色，例如用一個推理能力強的模型做規劃、另一個較快的模型做程式碼生成，在同一個 session 裡形成多模型工作流。文章示範的設定方式，是在專案根目錄的 `opencode.json` 中，把規劃與架構任務（需要較深推理）指定給 Kimi K3，把程式碼生成與實作任務指定給 Nemotron 3 Super 120B 以取得較好的輸出吞吐量，再把最上層的預設模型設為 GPT-OSS 120B 處理其餘情境；啟動 OpenCode 後輸入 `/models` 就能瀏覽 Bedrock 上所有可用模型。

📊 **三個模型，三種角色**

文章實際示範的三個模型各有分工：Moonshot AI 的 Kimi K3 負責規劃與架構這類需要深度推理的任務；NVIDIA Nemotron 3 Super 120B 負責追求最佳化吞吐量的程式碼生成；OpenAI 的 GPT-OSS 120B 是一個 1,200 億參數的開權重模型，結合強推理與程式碼生成能力，適合橫跨多檔案、架構較複雜的實作任務，被設為預設模型。文中也提到 Ethara.AI 在生產環境中採用這套架構，搭配多 agent 協作來支撐 AI 工程與研究工作流，不過素材未提供更多細節。

⚠️ **選模型前先做評測，別只看單一數字**

CrowdStrike 的 96% 準確率是在針對自家資料微調 Nemotron 之後量出來的結果，並不代表任何開權重模型開箱即用就能打平專有模型。文章建議兩條評測路徑：一是用 Artificial Analysis Coding Index，這是橫跨 SWE-Bench、Terminal-Bench、SWE-Atlas 等真實軟體工程任務的綜合基準，可以比較模型效能、每任務成本與延遲；二是用 Amazon Bedrock Evaluations，針對自己的 prompt 與資料做並排比較，搭配自動評分、LLM-as-a-judge 或人工審查。

🎯 **實務啟示**

如果你的團隊有資料留存或合規上的顧慮（Bedrock 涵蓋 HIPAA、SOC 2、ISO 27001、FedRAMP、GDPR 等常見合規範疇），又想避免被單一模型供應商綁住，OpenCode 加 Bedrock 開權重模型是一條值得評估的路徑。正式環境建議用 IAM Identity Center 或 IAM 角色取代長期有效的存取金鑰，並依任務型態（規劃 vs. 程式碼生成）把不同模型指派到 OpenCode 的不同角色，而非用單一模型硬扛所有工作。

🔗 **來源**
- 標題：Use open weight models as your AI coding agent with Amazon Bedrock
- 作者／機構：Aris Tsakpinis／AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/use-open-weight-models-as-your-ai-coding-agent-with-amazon-bedrock/

#AmazonBedrock #OpenCode #OpenWeightModels #AICoding #AWS #KimiK3 #GPTOSS #NVIDIANemotron #CodingAgent #LLMOps
