---
title: How Natera designed an agentic AI system for lab ops with Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-natera-designed-an-agentic-ai-system-for-lab-ops-with-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-11-12T23:04:19.020761'
score: 84
---

📌 【真實案例】實驗室工單回應從 17.4 小時縮到分鐘級,Natera 怎麼做到的

TL;DR:cfDNA 檢測公司 Natera 用 Amazon Bedrock AgentCore 打造 SWARM,首次回應速度快了約 130 倍,96.2% 工單自動覆蓋。

一位資深技術員離職,他多年累積對某個儀器家族的診斷經驗也跟著一起消失,沒有任何系統留得住。這是 Natera 實驗室工程團隊(由 Ariel Jirau 帶領)遇到的真實困境,也是他們和 AWS 合作打造 SWARM(Systematic Workflow Analytics and Resolutions Manager)的起點。

🤔 **每天 65 張工單,平均要等 17.4 小時才有人回**

Natera 是做 cell-free DNA(cfDNA)檢測的公司,實驗室設備一旦停機就會打斷樣本處理流程。但他們的服務工程團隊是靠個人經驗深度運作,而不是標準化的作業手冊,每天要處理超過 65 張分散在三個 Jira 隊列的工單,平均首次回應時間要 17.4 小時。設備停機會拖延樣本處理與病患報告的時程,而單靠多招人根本追不上工單量的成長速度。

🧩 **兩套 Runtime 共用一個技能庫**

Natera 選擇在 Amazon Bedrock AgentCore 上建構 SWARM,Jirau 提到團隊看重的是「一個受管的 runtime,讓工程資源能專注在診斷準確度而不是基礎設施,AgentCore 同時提供內建的身分管理,以及不用重寫 agent 邏輯就能替換模型的彈性」。

SWARM 的架構分成四層,核心是兩套互補的 runtime 共用同一個技能庫:swarm-agent 會在工程師還沒打開工單之前,就自動生成結構化的診斷報告;swarm-hive 則讓工程師即時互動,可以上傳圖片、探索其他排錯路徑。Jirau 強調「這個系統不是取代工程師,而是讓他們在工單一出現時,就能取得完整深度的機構知識」。

架構上第一個決定是把 agent 跑在哪裡。團隊選用 AgentCore runtime,因為它能用一個安全、受管的環境同時承載 swarm-agent 與 swarm-hive,內建身分管理與監控,不必自建一整套 agent 執行層。

因為 SWARM 跑在臨床環境中,憑證外流是不能接受的風險,團隊採用無金鑰(keyless)的部署模式:用 OpenID Connect(OIDC)搭配 AWS STS 產生依部署範圍限定的臨時憑證,管線裡不存放長期有效的存取金鑰;IAM 在元件層級強制最小權限;Amazon VPC 配合私有子網路與 VPC endpoint,讓流量不經過公開網際網路;AWS Secrets Manager 以 30 天週期自動輪替少數仍存在的憑證。GitLab CI runner 透過向帳號內設定的 IAM identity provider 出示 OIDC token 來向 AWS 驗證身分,再由 AWS STS 換取限定部署角色範圍的短期憑證。

這套基礎設施層的控管搭配資料治理政策,共同構成在受管制臨床環境運作 AI 系統所需的合規姿態:SWARM 跑在 HIPAA-eligible 的 AWS 服務上,並受 Business Associate Agreement(BAA)約束;每一次 agent 呼叫都會留下稽核紀錄;病患可識別資訊不會進入向量索引或語言模型,工單裡只保留設備與工作流程的metadata。

📊 **準確度先是資料品質問題,不是模型問題**

早期用一般用途的檢索、沒有針對設備的 metadata 時,結果並不穩定,於是團隊自建了一套針對技術設備文件的客製文件處理管線。Amazon Titan Text Embeddings 負責產生語意檢索用的向量表示,Amazon Bedrock Knowledge Bases 提供全託管的 RAG,把文件轉成向量後以 100 筆為一批寫入,這個批次大小是為了在索引吞吐量與 API 速率限制之間取得平衡。對於包含表格與圖表等高度結構化的原始文件,團隊投入自建的解析管線,而不是用預設的 chunking,文章指出這類投資能讓準確度提升「複利式」地延伸到每一次診斷。切分文字區塊時,團隊用 tiktoken 搭配 cl100k_base 編碼來量測邊界。

Jirau 分享了一個具體例子:「準確度本質上先是資料品質問題」,光是為表現最差的那個儀器家族補齊缺漏的廠商手冊,準確度就從 71% 提升到 75%,而且沒有動任何模型。這也形塑了團隊的改善流程:當準確度停滯時,先檢查資料覆蓋率,再考慮模型調整,因為廠商文件的缺口是漏診最常見的原因。

技能邏輯的設計上,團隊面臨「直接寫進 agent prompt」或「建立獨立、有版本控制的技能庫」的選擇,最終選擇技能庫,因為這樣系統才可稽核、可改善。Jirau 說:「診斷錯誤時,我們需要能指向具體的某個技能,而不是從頭debug整個系統,這就是為什麼我們從一開始就建立了有版本控制的技能庫」。目前技能庫包含 33 個技能:24 個針對特定儀器、覆蓋 Natera 支援的全部設備家族,加上 9 個適用於各類工單的跨領域工作流程技能。

📊 **成效:130 倍回應速度,96.2% 自動覆蓋**

SWARM 上線後帶來約 130 倍更快的首次回應時間,以及 96.2% 的工單自動覆蓋率,讓工程師在工單一出現時就能立即取得機構知識,而不用等人工排查。

🎯 **實務啟示**

這個案例給其他想做 agentic 運維系統的團隊幾個可直接套用的教訓:準確度瓶頸出現時先檢查資料覆蓋率而不是急著換模型或調參;把 agent 邏輯放進有版本控制的技能庫,而不是全部塞進 prompt,才能在出錯時精準定位問題;在受管制環境中,無金鑰部署與逐元件最小權限應該是架構設計的起點,而不是事後補的安全措施。

🔗 **來源**
- 標題:How Natera designed an agentic AI system for lab ops with Amazon Bedrock AgentCore
- 作者／機構:Ariel Jirau(Natera)
- 連結:https://aws.amazon.com/blogs/machine-learning/how-natera-designed-an-agentic-ai-system-for-lab-ops-with-amazon-bedrock-agentcore/

#AmazonBedrock #AgentCore #AgenticAI #Natera #RAG #HealthcareAI #LabOps #AWS #KnowledgeBase #AIOps
