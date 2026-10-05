---
title: Evaluating multi-agent systems for explainability and helpfulness with Amazon
  Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/evaluating-multi-agent-systems-for-explainability-and-helpfulness-with-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-10-05T23:26:06.364492'
score: 80
---

📌 多代理系統上線前，你怎麼知道agent的決策講得通？Amazon Bedrock AgentCore的解法

TL;DR：AgentCore Evaluations用三層評估器,從「有沒有幫助」一路驗到「決策理由講清楚了沒」。

LLM能生成流暢的回答,但企業場景要的不只是「講得好」,而是agent有沒有選對工具、有沒有守住業務限制、推理過程能不能被解釋清楚。當多代理系統從實驗階段走向生產環境,這個落差會直接變成風險。

🤔 **多代理系統上生產線前，缺的是「可解釋」這一層**

企業導入多代理系統,是為了處理需要跨資料來源、跨工具、跨業務限制推理的複雜問題,從供應鏈規劃到財務分析、客戶營運都是如此。這些系統不只是問答,而是協調多個專職agent做決策、執行工作流、產出可行動的建議。傳統只看模型回應品質的評估方式,對這類系統並不夠用,因為正確性還取決於工具選擇、工作流執行與業務限制的遵守程度。

Amazon Bedrock AgentCore是一個用來建置、串接、最佳化agent的平臺,其中的AgentCore Evaluations是一套全代管的能力,用來在開發與生產階段評估agent表現,涵蓋正確性、任務成功率與多個品質維度的行為。文章特別強調,評估（Evaluations）發生在執行之後,評估agent的品質;而Amazon Bedrock Guardrails則是在執行期間強制安全限制,兩者互補而非取代。

🧩 **以虛構的AnyCompany Retail為例，拆解供應鏈決策agent**

文章用一家虛構的跨國零售商AnyCompany Retail做示範案例：該公司常見庫存失衡問題（某些地區促銷缺貨、某些地區庫存過剩）,也要在配送速度、運力與成本之間權衡。解決方案用Strands Agents SDK搭配Amazon Bedrock AgentCore MCP伺服器與AgentCore Evaluations,建出一個orchestrator agent再分派給四個專職sub-agent：最佳化agent、配送agent、路由agent、分析agent,每個agent都跑在AgentCore runtime上,並開啟AgentCore memory與Observability。

orchestrator接到規劃人員的請求後,把工作分派給被包裝成工具的專職agent：最佳化agent呼叫背後接著模擬API Gateway REST介面的MCP工具取得最佳化決策;配送agent呼叫推薦API建議庫存在配送中心、門店、數位通路間的重新分配;路由agent呼叫物流API推薦承運商與路線;分析agent則回答供應鏈診斷類問題。

📊 **三層評估法：從通用品質一路驗到業務正確性**

文章採用的是漸進式的三層評估架構：

第一層是**內建評估器**,不需額外設定。所有agent都套用Helpfulness作為通用基準,再依各自最常出錯的地方加一個專屬評估器：orchestrator用Tool Selection Accuracy,最佳化與配送agent用Response Relevance,路由agent用Instruction Following,分析agent用Faithfulness。

第二層是**自訂評估器**,用來編碼業務規則,驗證「這個建議有沒有守住預算限制、是否用了真實庫存資料、輸出在業務上是否可行」：最佳化agent驗證constraint satisfaction、配送agent驗證data grounding、路由agent驗證route feasibility、分析agent驗證SQL correctness、orchestrator驗證plan coherence。

第三層則把**可解釋性**當成獨立評估維度,驗證agent是否明確闡述決策理由、引用支撐的資料或工具輸出,並解釋像成本與服務水準之間的取捨。

評估支援兩種模式：on-demand模式用於開發階段的benchmark、迴歸測試與CI/CD關卡;online模式用於生產環境的持續監控,透過OnlineEvaluationConfig物件設定抽樣率（例如1%到10%的production traces）與選用的session過濾條件,服務會自動從AgentCore Observability讀取trace、評分,再把結果串流到Amazon CloudWatch儀表板與告警。

⚠️ **案例是虛構示範，重點在評估框架本身**

AnyCompany Retail是文章用來示範概念的虛構公司,實際導入時每個企業的業務限制與可解釋性要求都不同,內建評估器只能打底,真正貼近業務的驗證仍需要自訂評估器。

🎯 **對正在上線多代理系統的團隊的意義**

如果你的多代理系統已經要從實驗走向生產,單靠「回答得通順」是不夠的評估標準。值得借鏡的是這套漸進式架構：先用內建評估器建立品質基準,再疊加業務規則的自訂評估器,最後把「解釋理由」本身當成可被量測的指標,搭配on-demand與online兩種模式把評估嵌進開發與維運流程,而不是上線後才發現agent的決策無法被稽核。

🔗 **來源**
- 標題：Evaluating multi-agent systems for explainability and helpfulness with Amazon Bedrock AgentCore
- 作者／機構：Kanishk Mahajan, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/evaluating-multi-agent-systems-for-explainability-and-helpfulness-with-amazon-bedrock-agentcore/

#AWS #Bedrock #AgentCore #MultiAgent #AIEvaluation #Explainability #EnterpriseAI #StrandsAgents #ResponsibleAI #AIObservability
