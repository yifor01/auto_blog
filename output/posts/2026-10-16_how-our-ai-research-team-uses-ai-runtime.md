---
title: How our AI Research team uses AI Runtime
source: Databricks
url: https://www.databricks.com/blog/how-our-ai-research-team-uses-ai-runtime
model: claude-code/sonnet
generated_at: '2026-10-16T20:19:04.376289'
score: 61
---

📌 Databricks 研究團隊怎麼靠自家 AI Runtime 撐住近兆參數訓練

TL;DR:Databricks AI 研究團隊用 AI Runtime 管理 GPU 健康、實驗追蹤與 agent 驅動研究,訓練任務量成長 8 倍。

當研究流程從「人類手動啟動每個實驗」變成「agent 自己決定下一步要跑什麼」,基礎設施要承受的就不再是人類的手速,而是機器一次喊出上百個任務的衝擊。Databricks 的 AI 研究團隊,正好把自家平臺當成應對這個轉變的工具。

🤔 **從數十億到近一兆參數,研究規模早已超出手動管理的範圍**

Databricks 的研究團隊負責開發支撐 Genie、Smart Routing、AI Functions(例如 ai_parse_document、ai_extract)背後的模型。要達到文章提到的「業界領先的文件解析品質」,團隊需要在不同架構、資料集、訓練技巧與超參數之間反覆試驗,橫跨數萬次訓練與評估執行;模型規模從數十億參數到接近一兆參數都有,訓練時依工作負載使用 NVIDIA H100 或 B300 GPU,其中最大型的訓練任務可能需要數百張 GPU 跑上好幾天到好幾週,並仰賴高頻寬網路維持訓練效率。

🧩 **AI Runtime 扮演的角色:健康檢查、實驗追蹤與治理化資料存取**

團隊從 AI Runtime(AIR)產品推出之初就是第一個使用者。AIR 會在訓練開始前對分配到的 GPU 節點做 preflight 健康檢查,訓練過程中持續監控 NCCL 通訊失敗、過熱或電力節流、GPU 驅動問題等狀況;一旦節點出狀況導致任務失敗,AIR 會偵測並把該節點隔離,避免後續任務再被排到同一臺故障機器上。文章提到,像 KARL 這類針對超過千億參數模型進行複雜 rollout 生成與後訓練的專案,可能需要動用數千個 GPU 小時,團隊因此不必反覆排查基礎設施故障,能把精力放回模型改進上。

透過 AIR CLI 與自訂 Docker 容器,團隊可以用程式化方式啟動工作負載、指定所需 GPU,並讓 AIR 處理排程與跨雲的高頻寬網路配置;本機開發用的容器映像檔可以直接拿來訓練,並透過 Databricks Artifact Registry 註冊、在不同實驗間共享,確保環境一致。實驗追蹤則交給 MLflow,AIR 會自動建立並管理對應的 MLflow 實驗,不需要額外設定,團隊可以直接監控任務狀態、串流並檢視訓練日誌、擷取指標,這些資訊同時也提供給 AI agent,讓它們判斷結果並決定下一步要嘗試什麼。所有研究資料存放在 Unity Catalog,透過 Unity Catalog FUSE mounting,團隊即使跨不同 Databricks workspace 工作,也能像存取本機檔案系統一樣使用這些資料,同時維持可追蹤、可共享與治理。

在 GPU 容量管理上,不同專案的資源需求差異很大,一個除錯實驗可能只需要幾張 GPU,一個大型訓練任務卻可能要佔用數百張 GPU 跑上好幾週;AIR 的工作負載優先權與 preemption 機制,讓團隊能依時效性分配資源,並在有閒置容量時(例如週末)用來支援額外的探索性實驗,而不影響優先度較高的工作。

📊 **訓練任務量成長 8 倍**

文章指出,在 AI Functions 相關的研究工作負載中,訓練任務的數量成長了 8 倍。這個成長被歸因於團隊逐漸把更多研究流程交給 agent 執行——讓 agent 提出改動、跑實驗、評估結果、決定下一步要嘗試什麼,形成一個持續循環。

💡 **Autoresearch 把基礎設施的小毛病放大成瓶頸**

文章提到,這種由 Andrej Karpathy 推廣開的「autoresearch」模式正在改變研究的進行方式。當一個人類研究者手動啟動少量實驗時,啟動速度慢一點、設定錯誤訊息不清楚,都還能忍受;但當 agent 一次launch 上百個實驗,同樣的問題會迅速變成瓶頸。因此 agent 驅動的研究,需要的是快速的任務啟動、程式化介面、清楚且可行動的錯誤訊息,以及穩定的執行與容易取得的訓練結果——這些原本服務人類研究員的基礎設施需求,在 agent 規模化之後被放大檢驗。

⚠️ **這是單一平臺供應商的自家案例分享**

文章並未提供具體的成本、延遲改善數字,或是與其他訓練基礎設施方案的比較,內容也集中在 Databricks 自身平臺的使用經驗上,對其他組織或雲端環境的適用性沒有進一步討論。

🎯 **實務啟示**

如果團隊正在往 agent 驅動的研究流程邁進,這個案例提醒的重點是:基礎設施該優先投資的地方,往往不是模型本身,而是節點健康檢查自動化、GPU 資源的優先權與 preemption 機制、以及把實驗追蹤與資料治理整合進同一套工作流——因為一旦讓 agent 大量平行跑實驗,這些原本不起眼的基礎設施缺口,會是第一個被撞到的瓶頸。

🔗 **來源**
- 標題:How our AI Research team uses AI Runtime
- 作者／機構:Databricks
- 連結:https://www.databricks.com/blog/how-our-ai-research-team-uses-ai-runtime

#Databricks #MLOps #AIInfrastructure #GPU #ReinforcementLearning #MLflow #AutoResearch #AgenticAI #ModelTraining #DataEngineering
