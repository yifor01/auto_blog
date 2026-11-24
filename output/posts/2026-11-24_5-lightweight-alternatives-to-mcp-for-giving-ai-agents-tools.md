---
title: 5 Lightweight Alternatives to MCP for Giving AI Agents Tools
source: KDnuggets
url: https://www.kdnuggets.com/5-lightweight-alternatives-to-mcp-for-giving-ai-agents-tools
model: claude-code/sonnet
generated_at: '2026-11-24T03:41:01.553986'
score: 89
---

📌 不是每個工具都需要 MCP 伺服器

TL;DR：用現有的 Python 函式、框架或 REST API 就能讓模型呼叫工具,不必急著上 MCP。

你的應用程式裡,可能早就躺著一個叫 `lookup_product(sku)` 的函式,功能只是讀一列庫存、回傳價格。現在想讓模型呼叫它,第一個念頭往往是「要不要架一臺 MCP 伺服器」。KDnuggets 的這篇文章給出的答案是:通常不需要,但值得公平地說清楚為什麼。

🤔 **MCP 解決的是「多對多」,不是「一對一」**

MCP(Model Context Protocol)是一種讓工具被許多 host 共用的協定:伺服器描述自己有哪些工具,任何相容的 client 都能發現並呼叫它們。文章指出,目前的 MCP 架構(2026 年 7 月 28 日修訂版)可以跑在本機的 stdio 上,也可以用 Streamable HTTP,所以採用 MCP 並不強迫你架一個網路服務。但如果你現在只有「一個應用程式呼叫一個函式」,MCP 要解決的多對多問題根本還沒出現。

🧩 **五個選項,其實是同一個合約放在五個不同的地方**

文章強調,這五個替代方案不是五套互相競爭的標準,而是依照你手上已經擁有的東西(幾個 Python 函式、一個 agent 框架、一個 REST API、一支命令列工具、一個工作流平臺)決定工具要放在哪裡。無論選哪個,流程都遵守同一個順序:模型提出一個呼叫(工具名稱+參數)→ 應用程式依自己擁有的合約檢查(名稱是否在允許清單、參數形狀是否正確、這個使用者是否有權限)→ 執行器跑完工作,回傳結構化資料或明確的錯誤。文章引用 OWASP 的「過度代理(excessive agency)」指引,把風險拆成三種:功能過多、權限過多、自主性過高,而這三者永遠是應用程式該決定的事,跟你用哪種傳輸方式無關。

文章整理的對照表大致是:

| 你已經擁有 | 連接方式 | 仍要自己做的事 | 什麼時候該升級 |
|---|---|---|---|
| 幾個本地 Python 函式 | 原生 tool calling + 白名單 dispatcher | 訊息處理、權限、錯誤 | 多個 provider 或 client 需要共用合約時 |
| Python agent 框架 | 型別化的 function tools | 業務授權、依賴維護 | 框架耦合的成本超過省下的黏合程式碼時 |
| 有 HTTP 介面的服務 | 精選過的 REST adapter(以 OpenAPI 當地圖) | 憑證、允許的操作、回應處理 | 規格廣或常變動,需要專人維護 adapter 層時 |
| 可信任的窄範圍命令 | 受限的 subprocess | 參數政策、權限、程序失敗處理 | 要跑不受信任的程式碼或更廣的存取時,需要真的隔離 |
| 已維運的工作流平臺 | 認證過的 webhook | 工作流所有權、憑證、完成語意 | 部署平臺的成本超過省下的整合工作時 |

📊 **實際示範:原生 tool calling + dispatcher**

文章用一個假造的商品目錄做示範(SKU `BK-17` 是一本 A5 筆記本,1299 分、美元計價),搭配 Ollama 0.40.13 上的 `qwen3.5:4b` 模型。流程是:把工具 schema 隨 chat request 送出,模型回覆帶著 `tool_calls` 而不是文字,應用程式自己執行呼叫、把結果包成 tool message 送回去,再問模型一次。核心是一個 `DISPATCH` 字典,工具名稱不在字典裡就不會被執行。

實際跑起來:問「BK-17 多少錢?」,模型提出 `lookup_product({"sku": "BK-17"})`,應用程式回傳該筆目錄資料,模型回答「12.99 美元」。問一個不存在的 SKU `BK-99` 時,應用程式回傳結構化的錯誤訊息,模型沒有編造價格,而是老實告訴使用者找不到這個 SKU。

💡 **這條路的安全模型,就是那個字典**

文章特別提醒,`DISPATCH` 必須是固定寫死的字典,絕對不能用 `getattr` 去動態查模組裡的函式,否則等於讓模型自己決定能呼叫什麼。這條路換來的代價是沒有可攜性:訊息格式是 Ollama 專屬的,換一家 provider 就要重寫一遍,而且回合數上限、錯誤處理全部要自己管。對一個只有少數函式、只服務一個應用程式的情境來說很划算;但一旦第二個 client 也想用同一組工具,這條路立刻變得吃力。文章也提到,工具函式本身可以很「厚」,例如 PDF 表格解析可以整個包在一個由 SDK 支撐的函式背後,agent 只拿到解析後的欄位,不需要自己管理 PDF 解析器。

🎯 **實務啟示**

在動手架 MCP 伺服器之前,先盤點自己手上已經有什麼:如果只是一兩個函式要讓單一應用程式呼叫,原生 tool calling 加一個白名單字典就夠了;等到真的有多個 provider 或多個 client 要共用同一套工具合約時,才是 MCP 開始划算的時間點。

🔗 **來源**
- 標題：5 Lightweight Alternatives to MCP for Giving AI Agents Tools
- 作者／機構：Nahla Davies，KDnuggets
- 連結：https://www.kdnuggets.com/5-lightweight-alternatives-to-mcp-for-giving-ai-agents-tools

#MCP #AIAgents #ToolCalling #LLM #Ollama #PythonDevelopment #AgentFrameworks #APIDesign #SoftwareArchitecture #AIEngineering
