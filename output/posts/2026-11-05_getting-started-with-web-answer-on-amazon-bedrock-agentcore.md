---
title: Getting started with Web Answer on Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/getting-started-with-web-answer-on-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-11-05T23:09:04.879684'
score: 77
---

📌 Amazon Bedrock AgentCore上線Web Answer,一次MCP呼叫換一個附來源的答案

TL;DR:AWS推出的Web Answer讓agent不必自建搜尋pipeline,一次tool call就拿到附引用來源的合成答案。

想讓agent回答「現在正在發生什麼」這類問題,工程師過去得自己兜出一整條pipeline:呼叫搜尋API、判斷哪些結果可信、抓取並清理頁面內容、用模型合成答案、再手動比對citation有沒有對上來源。每一步都是要維護的程式碼,每一步也都是幻覺、過時內容或引用斷鏈冒出來的地方。AWS這次把整條pipeline收進了一次API呼叫裡。

🤔 背景:自建檢索pipeline的三個老問題

證據不足時模型會幻覺,搜尋索引更新後內容容易過時,claim和來源之間也常常因為工程疏漏而對不上。Web Answer要解決的就是這三件事。

🧩 架構:問題怎麼變成一個附引用的答案

整個流程是:agent把問題傳給AgentCore Gateway → Gateway用AWS IAM或JWT驗證這次呼叫 → Gateway用自己的service role呼叫Web Answer(一個AWS自家擁有、託管的connector) → Web Answer規劃搜尋策略、平行跑好幾個查詢、讀取關鍵頁面核對事實,證據不夠就再搜一次 → 寫出答案,把每個claim連到對應的來源URL → Gateway把答案與citations包成MCP tool result回傳給agent。

AWS同時提供Web Search工具,兩者的分界線在於「誰負責跑模型」:Web Search把原始搜尋結果交給agent自己的模型去推理,Web Answer則直接吐出一份合成好、附引用的答案。官方建議兩者可以並用——廣泛研究任務用Web Search,具體事實型問題用Web Answer。

🧩 怎麼用:從掛上Gateway到拿到答案

Gateway的service role需要一個inline policy,允許它呼叫Web Answer;這個role只管Gateway對外的呼叫,不需要bedrock:InvokeModel權限,因為agent的模型是用agent自己的身份執行的。接著在Gateway上新增一個Web Answer connector target,指定connectorId;因為用GATEWAY_IAM_ROLE做outbound驗證,不用另外建立或儲存任何憑證。等get_gateway_target回報狀態為READY後就能用了。Gateway管理者還能在target層設domain filter,例如只允許bis.org、排除unreliable-source.net。agent這端透過標準的MCP流程,用tools/list找到名為web-answer-tool___WebAnswer的工具,再用tools/call呼叫——這套流程相容Strands Agents、LangChain、LangGraph、CrewAI等任何MCP client。呼叫時除了問題本身,還能帶上domain filter、發布日期範圍、國家這幾個可選參數做本地化,但agent端的filter只能比target的設定更嚴格,不能放寬target已經排除的網域。回傳結果同時有content(markdown文字,內含[1]這種inline citation標記)和structuredContent.answer(同樣的文字加上結構化的citations清單,每筆citation帶著來源url與domain)。

📊 定價與目前限制

Web Answer每1000次tool call收費10美元,目前只在美國東部(維吉尼亞北部,us-east-1)上線,AWS表示之後會擴增到更多region。文章也提醒,測試完要依序刪掉target、Gateway,再刪掉為它建立的service role與policy,否則會持續產生費用。

⚠️ 限制

目前僅限單一region,且agent層的domain filter只能在target設定的範圍內做縮限、不能擴張,使用前也得先有一個現成的AgentCore Gateway才能掛上這個connector。

🎯 實務啟示

如果產品需要的是「有時效性、要附來源」的問答,Web Answer能直接省掉整條檢索合成pipeline的開發與維護成本;如果任務需要agent對原始搜尋結果做更深入的推理判斷,Web Search仍是更合適的選擇,兩者甚至可以在同一個agent裡依任務類型切換使用。

🔗 來源
- 標題:Getting started with Web Answer on Amazon Bedrock AgentCore
- 作者／機構:Adrianna Chudy, AWS Machine Learning Blog
- 連結:https://aws.amazon.com/blogs/machine-learning/getting-started-with-web-answer-on-amazon-bedrock-agentcore/

#AWS #BedrockAgentCore #WebAnswer #MCP #AIAgents #RAG #CloudComputing #LLMTools #AgenticSearch #AWSBedrock
