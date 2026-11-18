---
title: Reducing token costs and latency in Amazon Bedrock AgentCore JSON workloads
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/reducing-token-costs-and-latency-in-amazon-bedrock-agentcore-json-workloads/
model: claude-code/sonnet
generated_at: '2026-11-18T23:42:37.690557'
score: 94
---

📌 AgentCore 代理省 71% token、砍 80% 延遲的實戰

TL;DR：AWS 分享用 S3 卸載大型 JSON 與結果分頁，把 agent 的 token 成本與延遲大幅壓低的實作方法。

當一個 agent 掛了 40 多個工具、每次呼叫都要把動輒數十 MB 的 JSON 塞進 context window 時,「context 爆炸」不是比喻,是真實會卡住生產環境的問題。AWS 這篇文章分享了他們替航空業維運平臺 Flightscape 打造的訓練排班最佳化 agent 的優化過程,把平均延遲從超過 15 秒,壓到大幅縮短。

🤔 40 多個工具、20MB+ JSON 撐爆 context 的問題

Flightscape 的 Training Schedule Optimization agent 用來驗證機組排班是否符合業務規則,背後是一套最佳化器(Optimizer)接收 Request JSON、輸出 Response JSON,再經 Business Rules Validator 產出 Validation Report JSON——這三份 JSON 文件,都要餵給一個用 LangGraph 建構、跑在 Amazon Bedrock AgentCore 上的對話式 agent,讓使用者能查詢最佳化結果、理解驗證錯誤、探索排班指派。問題在於:每次工具呼叫都把完整 payload 塞進模型 context,資料量一大,token 數與成本隨之膨脹;遇到更大的資料集,context window 甚至會在 agent 完成推理前就被填滿,平均請求延遲超過 15 秒。

🧩 把重的留在 S3,context 裡只留輕量參照

團隊導入了三種可組合的策略來處理這個問題,文章詳細說明了其中兩種。第一種是改變 session 狀態的持久化方式:把 request JSON、response JSON、驗證資料等大型 artifact 移到 Amazon S3,AgentCore memory 只保存指向這些物件的穩定參照。他們設計了一套專用的 PersistedState schema,只保留輕量欄位與 artifact 參照;即時運行中的 graph state 仍保有完整的領域物件供工具執行使用,但寫入持久層時會先經過 dehydrate_state() 轉成輕量形式,session 恢復時再透過對應的 rehydration 流程重建:反序列化訊息、重新解析 payload、還原每個參照鍵,讓後續輪次能找到對應的 artifact。

這裡的關鍵技巧是內容定址(content addressing):把 JSON 以排序過的 key 與緊湊分隔符序列化後,取其 SHA-256 雜湊值作為參照鍵,而不是隨機產生 key。這讓寫入具備冪等性——同一份未變更的 payload 在不同輪次會映射到同一個 key,直接重用 S3 裡已存在的物件,不需要重新上傳。負責存取的 S3ArtifactStore 類別包裝了 put_json / get_json 介面,並內建一層 process 內快取,同一次呼叫中已經讀寫過的 payload 不需要再往返 S3 一次。

📊 工具回應才是真正的瓶頸:結果分頁上場

把大型 artifact 的持久化搬到 S3 之後,團隊發現工具呼叫「回應」本身才是真正的 token 消耗大戶。很多工具結果本身就過大,即使模型只需要其中一小部分,系統仍把完整清單送進 context,不僅拖慢每一輪互動,也讓多輪對話的 context window 很快被塞滿;文章提到部分案例中,單一工具回應的 token 數甚至超過 80,000。為此,團隊引入了「on-demand 結果分頁」:當工具回傳過大的清單或字典時,完整結果先存進 S3,模型只拿到一份精簡摘要加上一個 handle,之後若需要更多細節,可以透過 get_result_page_tool() 主動取得指定分頁的內容,而不是一次性全部塞進 context。

📊 壓測結果:token 省 71%,延遲砍 80%

這些優化加總後,在一個具代表性的 23MB payload 基準測試中,整體 token 消耗最高降低 71%,平均延遲最高縮短 80%。

⚠️ 文中未詳述的部分

文章開頭提到團隊共用了「三種可組合的策略」,但素材中只具體說明了狀態持久化(S3 + 內容定址)與結果分頁這兩種,第三種策略的實作細節未在提供的內容中展開,因此本文不做推測描述。

🎯 實務啟示

如果你的 agent 也有「工具回應動輒數萬 token、多輪對話把 context 撐爆」的症狀,這篇文章給出的思路值得借鏡:先把真正重的資料搬出對話 context、只留可還原的參照,再對工具回應做按需分頁,讓模型預設只看摘要,需要細節時再主動要。內容定址這個小技巧也值得注意——它不只是省儲存空間,更重要的是讓重複未變更的 payload 寫入變成冪等操作,減少不必要的 S3 寫入次數。

🔗 來源
- 標題：Reducing token costs and latency in Amazon Bedrock AgentCore JSON workloads
- 作者／機構：Pallav Gupta，AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/reducing-token-costs-and-latency-in-amazon-bedrock-agentcore-json-workloads/

#AWS #BedrockAgentCore #LangGraph #AIAgents #TokenOptimization #LatencyReduction #ContextWindow #LLMOps #S3 #AgenticAI
