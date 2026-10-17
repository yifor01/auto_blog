---
title: 'Building trust in AI agents: A production-ready evaluation framework with
  Amazon Bedrock AgentCore'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/building-trust-in-ai-agents-a-production-ready-evaluation-framework-with-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-10-17T19:35:05.718810'
score: 83
---

📌 AWS 揭露內部教訓：Agent 答得流暢,不代表答得對

TL;DR：AWS 分享用 Bedrock AgentCore 建立 Agent 持續評估框架的實戰經驗，核心問題是傳統監控抓不到「答錯但看起來很確信」的失敗。

傳統軟體壞掉的時候會大聲抗議：拋錯誤、當機、紅燈亮起。AI Agent 不會。它會用流暢、自信的語氣,給出一個看起來完全正常的答案,而這個答案可能是錯的。等到有人類發現問題,信任已經先碎了。

🤔 **監控全綠,答案卻是錯的**

AWS 的 Sales, Marketing, and Global Services（SMGS）Operations 團隊建置了一套服務全球 AWS Field Sales 的多 Agent 系統,讓業務人員能用自然語言、透過 Amazon Quick 詢問業務問題。背後由多個專職子 Agent 協作：Performance Insights Agent 負責依地區範圍產出營收與績效的敘事型洞察,Customer Insights Agent 整合產品使用狀況、支援歷程、合約狀態與互動資料,拼出完整的客戶視角,Data Insights Agent 則是讓業務團隊用白話查詢結構化分析資料的 text-to-SQL agent。所有答案都依使用者所屬地區與角色權限做範圍限制,業務團隊會拿這些數字去規劃客戶策略、準備會議,所以答案必須是對的。

上線前評估 Customer Insights Agent 時,團隊發現：在多次執行過程中,監控訊號始終是綠燈,但那只代表系統「有回應」,不代表回應「是對的」。如果這些錯誤沒被攔下來就上線,業務人員引用了灌水的數字,付出代價的是他們在客戶面前的信譚。

🧩 **風險不會隨著發布結束,反而隨著每次變動而增加**

這個風險會隨著新 Agent 加入、資料、prompt、程式碼或模型的每一次變更而擴大,甚至在完全沒有發版的情況下也會擴大,因為上游資料管線每週都會刷新。更麻煩的是「協調發布」本身的風險：當一次資料變更、工具變更,以及對應的 prompt 更新本該同時上線,卻分批落地時,系統會在所有變更到齊之前,以不匹配的狀態運作。

📊 **一次版本錯位,通過率從 78% 掉到 38%**

在一次 pre-production 測試中,光是這種不匹配的時間窗口,就讓通過率從 78% 直接摔到 38%。這個數字具體說明了為什麼「上線前評估一次就算了」是不夠的,必須有一套框架能持續判斷答案是否有憑有據、是否正確,並能把每一次失敗往回追溯到根因究竟出在資料、prompt 還是 Agent 程式碼。

🧩 **以 AgentCore Evaluations 為核心骨架,橫跨五個評估維度**

團隊用 Amazon Bedrock AgentCore 的 Evaluations 能力作為整套品質體系的連結組織,搭配 Amazon Bedrock Guardrails 處理安全性、Amazon CloudWatch 負責指標與告警追蹤、Amazon S3 與 Amazon Redshift 做評估結果持久化、Amazon Quick 呈現儀表板,以及 AWS Lambda 執行客製化的評估邏輯。

文章把 Agent 評估拆成五個維度：安全性（是否在界定的行為邊界內）、品質（回應是否正確、連貫、有憑有據）、效能（是否夠快夠穩定）、成本（是否能有效率地規模化運作）,以及操作可控性（能否快速偵測、診斷並修復問題）。安全性是第一優先,沒有任何 Agent 可以在不符合安全門檻的情況下上線或持續運作;品質則是五者中最難做好、也最需要獨立框架支撐的一環。

💡 **三層評估：工具、Agent、多 Agent 協作**

這套框架同時套用在三個層級：工具層級（每個能力,例如客戶去重工具或圖檢索工具,都有自己的評估契約）、Agent 層級（每個子 Agent 做端到端評估）,以及多 Agent 層級（跨 Agent 邊界的協作路徑要評估連貫性、路由是否正確、整合結果是否準確）。文章強調這套九階段的評估流程會同時作用在這三個層級上,而且這個心智模型不只適用於這套系統,也適用於任何要新建或整合的生產級 Agent。

這也呼應了文章對 Agent 本質的定位：傳統軟體是確定性的,相同輸入必然得到相同輸出;機器學習模型引入了機率性輸出,催生了 MLOps;而 Agent 疊加了第三層複雜度:自主、多步驟的推理,問題從「有沒有壞掉」變成「整條推理鏈上的每個決策是否合理」。Agent 是非確定性的,同樣的輸入可能走不同的推理路徑,而且會在路由、工具選擇、結果整合上做連鎖決策,任何一步悄悄出錯都可能污染後面所有環節,最致命的是它會靜靜地劣化:延遲不變、錯誤率不變,但回應品質正在流失,因為 Agent 依然「有回應」,只是「回應錯了」。

🎯 **實務啟示**

如果你的團隊正在把 Agent 推向生產環境,這篇文章最值得帶走的一句話是：品質不該是最後一道 QA 關卡,而該是 Agent 本身的作業系統,被持續測量、自動防護,並隨著每一次互動改善。具體做法上,值得參考的是把評估契約下放到工具層級,而不只是在整個系統跑完之後做端到端驗收,這樣才能在問題擴散之前,精準定位到底是哪一個工具、哪一次 prompt 變更出了錯。

🔗 **來源**
- 標題：Building trust in AI agents: A production-ready evaluation framework with Amazon Bedrock AgentCore
- 作者／機構：Rui Li, AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/building-trust-in-ai-agents-a-production-ready-evaluation-framework-with-amazon-bedrock-agentcore/

#AIAgents #AWS #BedrockAgentCore #AgentEvaluation #MLOps #ProductionAI #LLMOps #AgenticAI #QualityAssurance #CloudAI
