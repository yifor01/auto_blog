---
title: Introducing Tool Retrieval in the Gemini API
source: Google AI Blog
url: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/
model: claude-code/sonnet
generated_at: '2026-11-19T23:41:38.552416'
pinned: true
---

📌 Gemini API 推出 Tool Retrieval,工具庫破百也不卡 token

TL;DR:Gemini API 新增 Tool Retrieval,讓 agent 按需載入工具參數結構,省 token 又能維持挑選準確度。

當你的 agent 從串接 10 個工具擴張到上百個工具時,每次請求都把整份工具庫的完整參數結構塞進 prompt,會發生什麼事?輸入 token 暴增、延遲拉長,模型在一堆候選工具裡挑選時反而更容易選錯。Google 在 Gemini Interactions API 的 preview 功能 Tool Retrieval,就是為了解決這個規模化痛點。

🤔 **工具庫越大,context 越肥**

過去的做法是把每個工具的名稱、描述、完整參數結構(parameter schema)一次性全部塞進 prompt。工具數量一多,這份清單本身就會吃掉大量輸入 token,連帶拖慢回應速度,也讓模型在挑選工具時準確率下降。

🧩 **先看名字,需要才載入完整結構**

Tool Retrieval 的做法是讓 agent 把完整工具庫「待命」著,模型一開始只看到每個工具的名稱與描述,完整的參數結構則延後載入。啟用方式很簡單:在請求裡加入一個 `tool_search` 工具,並在想延後載入的工具上設定 `defer_loading: true`。

以官方範例來說,一個客服 agent 可能有 50 個以上的工具函式,其中 `issue_refund`(退款)被設為延後載入。當使用者說「訂單 A-1042 損壞,退 40 元」,模型會在同一次 API 呼叫中依序完成三個步驟:先用 `tool_search_call` 搜尋 `issue_refund`,API 回傳 `tool_search_result`(完整參數結構),模型再發出 `function_call` 實際呼叫。這三步都會記錄在 `interaction.steps` 裡,方便開發者除錯,檢查模型當時到底考慮了哪些工具名稱與描述。

後續流程和一般 function calling 完全一樣:你的程式執行退款邏輯,再把 `function_result` 傳回去即可。整個搜尋過程由 Gemini 在伺服器端完成,開發者不需要自建索引或額外的檢索服務。

Tool Retrieval 也能搭配遠端 MCP 伺服器使用:在 `mcp_server` 工具上設 `defer_loading: true`,該伺服器底下所有工具就會按需載入,不必逐一列出。此外,因為延後載入的結構不會出現在 prompt 開頭,只會在對話後段才被載入,所以不會破壞 prefix caching 的快取前綴。

如果開發團隊自己維護工具註冊表、embedding 索引或依使用者權限做過濾,也可以把 `tool_search` 宣告為 `"execution": "client"`,自訂搜尋參數。這種客戶端檢索模式會多一次來回請求,但好處是工具不需要預先宣告,甚至可以在對話中途,使用者連接新整合服務時才動態加入新工具。

📊 **計費與支援模型**

Tool Retrieval 本身不另外收費,輸入與輸出 token 仍依呼叫模型的標準費率計算。開啟 `tool_search` 會固定增加一小塊輸入 token,之後每次被模型載入的參數結構,會從那之後都算作該對話的輸入 token,和原本直接宣告工具的計費方式一致。換句話說,省下的 token 來自「沒被載入的那些工具」,工具庫越大、長尾工具越多,省下的比例通常也越可觀,但實際效益仍需用自己的流量實測。此功能支援 Gemini 3.6 及更新版本,包括所有 Gemini 4 系列模型。

🎯 **實務啟示**

對正在把 agent 從玩具原型擴展到上百工具規模的團隊來說,Tool Retrieval 提供了一個不需要自建檢索基礎設施的選項:常用工具留在 prompt 前段,長尾工具延後載入,同時還能保留 prefix caching 的效益。如果你的 agent 工具庫正在快速膨脹,這是值得實測的第一步優化。

🔗 **來源**
- 標題:Introducing Tool Retrieval in the Gemini API
- 作者/機構:Lucia Loher, Nora Kassner, Google DeepMind
- 連結:https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/

#GeminiAPI #GoogleDeepMind #AIAgents #FunctionCalling #LLMTools #TokenOptimization #MCP #AgentEngineering #PromptCaching #DeveloperTools
