---
title: Migrate agentic workloads to Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/migrate-agentic-workloads-to-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-09-03T20:21:01.641968'
score: 89
---

📌 從Notebook到正式環境：LangGraph客服Agent遷移AgentCore實錄

TL;DR：AWS示範將LangGraph客服agent分階段搬上Amazon Bedrock AgentCore，用具體行數量化每階段成本。

「能在notebook裡跑」和「能在正式環境裡跑」，中間隔著十項與agent推理邏輯完全無關的維運工作。AWS這篇文章示範了怎麼把這段距離走完，而且每一步改了多少程式碼都算給你看。

🤔 **Agent上線後，你要扛起十項與「推理」無關的工作**

文章從一個已經存在的agent出發：一個LangGraph客服agent，會分類每則訊息，把生氣的顧客升級處理，其餘顧客則透過三個工具回答問題，模型呼叫已經走Amazon Bedrock。作者指出，真正上線後要處理的，是與agent推理無關的維運負擔：把不同使用者的session彼此隔離、跨輪次與跨日期保存狀態、每個工具呼叫的身分驗證、底層作業系統的修補等。當agent進入正式環境，還需要加上Amazon Bedrock Guardrails，過濾有害內容、驗證回答是否有依據來源文件、阻擋prompt injection攻擊，這些防護不論你的agent停在哪個遷移階段都適用。

🧩 **三階段遷移：搬家、換大腦、交出方向盤**

遷移分成三個階段，每個階段都可以跟前一階段比較行為是否一致：

- **Stage 0（基準線）**：現狀的LangGraph agent，`classify_intent`向模型要一個字的分類結果，手寫的`route_intent`讀取該結果決定路由。生氣的顧客走向`escalate`，回傳固定的轉接訊息且不呼叫模型；其他人走向`assist`，帶著綁定的工具呼叫模型。三個工具（`lookup_order`、`process_return`、`search_faq`）以`@tool`函式包裝一個HTTP後端，回傳`{"error": ...}`而非拋出例外，因為工具節點內的例外會直接讓整次執行中斷，而錯誤負載是模型可以繼續處理的資訊。狀態則靠`MemorySaver`這個以`thread_id`為鍵的checkpointer保存——這是唯一有硬限制的部分：它是進程內的字典，進程一死狀態就沒了，兩個副本之間也看不到彼此的對話。模型呼叫使用`ChatBedrockConverse`，因此推論本來就已經走Amazon Bedrock，Stage 0完全不涉及任何AgentCore API；若你原本是直接呼叫OpenAI或Anthropic，這個建構子就是你唯一要改的地方。
- **Stage 1（搬遷執行環境）**：把agent搬上Amazon Bedrock AgentCore的Runtime、Gateway與Memory，graph結構完全不變。Runtime接手運算資源，OS修補、自動擴展與session隔離不再是你的責任，預設跑在AWS代管基礎設施上，也可以接上自己的VPC；不論哪種模式，網路設計、邊界防護與授權決策仍是你自己的工作。Gateway接手工具的身分驗證，以自己的執行角色呼叫你的函式；checkpoint儲存搬到Memory，跨輪次、跨進程、跨天保存對話狀態。IAM政策、VPC設定、WAF規則與密鑰輪替在每個階段都仍歸你管，依賴套件更新則要到Stage 3才移交。另外三項服務可以附加但不取代任何既有元件：Identity負責代理憑證與刷新OAuth token（本次示範未使用到）；Policy在Gateway層決定個別工具呼叫是否放行；Observability則自動把Runtime的日誌、指標與追蹤送進Amazon CloudWatch。遷移套件不是複製Stage 0的程式碼，而是直接import它，把graph拓撲、路由邏輯、狀態結構、所有prompt與工具實作原封不動地帶過來。
- **Stage 2／3（換大腦、交出方向盤）**：Stage 2把手寫的路由迴圈，改造成建立在Strands Agents之上的model-driven planning；已經先在Stage 1把Gateway、target與Memory建好的團隊，若決定直接重寫agent，也可以從Stage 2開始。Stage 3則是把整個推理迴圈交給AgentCore harness處理，文章中僅記載其存在與文件位置，並未實際建置與展示。

📊 **用行數量化的遷移成本**

作者刻意用可從硬碟量測、而非憑感覺估計的數字來描述遷移代價：Stage 1只改動agent內部**45行程式碼**，新增**22行**SDK未提供的支援程式碼，另外**85行**是原封不動被import進來的內容。文章也強調，Stage 1能一次性解決十項維運負擔中的五項：Runtime接手運算，Gateway接手兩項工具的身分驗證，Memory接手對話狀態，而推論本身完全沒動，因為「它從來就不是問題所在」。

⚠️ **AgentCore拿走了什麼？答案是：關於架構決策的部分，什麼都沒拿走**

文章特別強調「AgentCore從你手上拿走了什麼」這個問題的答案是「沒有」：Runtime只是agent運行的地方，不會替你決定agent下一步該做什麼。放棄手寫的路由分支是Stage 2才做的選擇，而不是遷移到Runtime時被迫的結果。前置條件也不輕：需要已啟用Amazon Bedrock模型存取權的AWS帳號、Python 3.12、能建立AgentCore、Lambda、S3與IAM資源的AWS CLI認證，還需要為帳號啟用一次CloudWatch Transaction Search，否則本次示範產生的追蹤資料將無法檢視。

🎯 **實務啟示**

如果你手上已經有一個在notebook或本地環境跑得動的agent，這篇文章給出的路徑是：先做Stage 1把運算、工具驗證與狀態搬到託管服務，此時graph邏輯完全不動，可以直接拿Stage 0的行為當基準線做回歸比對；等對Runtime有信心後，再考慮Stage 2把手寫路由換成model-driven planning。這種「先搬家、再換大腦」的順序，讓每次變動只涉及一個變數，方便定位問題出在遷移本身還是agent邏輯的改動。

🔗 **來源**
- 標題：Migrate agentic workloads to Amazon Bedrock AgentCore
- 作者／機構：Sruthi Vedula, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/migrate-agentic-workloads-to-amazon-bedrock-agentcore/

#AmazonBedrock #AgentCore #LangGraph #AIAgents #AWS #AgenticAI #MLOps #CloudArchitecture #ProductionAI #StrandsAgents
