---
title: How Clay Builds GTM Agents — Jeff Barg, Head of AI
source: Latent Space
url: https://latent.space/p/how-clay-builds-gtm-agents-jeff-barg-head-of-ai/
model: claude-code/sonnet
generated_at: '2026-11-27T01:14:48.686326'
score: 71
---

📌 Clay的GTM Agent，為何讓自家銷售團隊跑去用Cursor？

TL;DR：Clay重建Agent架構換來三個教訓，也給出了自訓模型該不該出手的推理支出門檻。

當一家公司自己的銷售團隊拒絕用自家產品的介面，寧願活在Cursor裡，工程團隊該怎麼辦？Clay的答案是：把CLI直接做出來給他們用。

🤔 從Avenue到Head of AI：一個人打天下的Agent團隊

Jeff Barg加入Clay，是因為Clay收購了他和別人共同創辦的維運警示新創Avenue。當時Clay約50人、Avenue約5人，AI雖已是Clay產品思路的重要部分，但公司內部沒人專門負責AI。Jeff接手Head of AI時，Clay的Agent工作全靠一位工程師撐著，這位工程師後來離職自己創業。此後Clay業務成長約10倍，團隊擴張到約600人，今年9月以71億美元估值完成1.15億美元募資。

🧩 Sculptor重生記：從system prompt調校到跑在雲端沙盒裡的Coding Agent

Jeff的第一個產品是Sculptor，2025年9月上線，跑在Sonnet 3.5世代的模型上，核心是一套工具搭配團隊精心調校的system prompt，在迴圈裡反覆呼叫。它很擅長幫表格加欄位，卻訂不出十場合格會議，而原有的評測方式（用LLM判斷Sculptor呼叫了哪些工具）完全抓不到問題——因為真實使用情境是請它分析一張表格，或處理一張上百萬行的企業級表格。Jeff總結出三個教訓：coding agent非常擅長Bash和Python；Sculptor原有的工具太有限，難以靠串接完成複雜任務；而且Agent根本看不到CRM資料與campaign成效。於是Clay把Sculptor重建成跑在Pi harness上的coding agent，在雲端沙盒裡執行Clay CLI，並新增一個叫Audiences的資料層，把CRM與Gong的紀錄對齊，讓Agent能同時看到兩邊的資料。

📊 查遍4000萬家公司只要1500美元，但模型早就不是瓶頸

Jeff粗略估算：Clay資料庫裡有約4000萬家公司，一個LinkedIn頁面約1000個token，加上ideal customer profile再多約500個token，用像TypeSafe的Jev這樣的分類器把全部4000萬家公司跑一遍，帳單大約是1500美元。目前大多數客戶只對約1萬家公司做資格審查。Jeff認為合理的enrichment預算是每條合格線索1到10美元，每場成功預約的電話則是10到100美元；lead qualification這件事，模型在Clay的評測上已經接近「解決」狀態，過去一年幾乎任何模型的分數都差不多高，反而是深度研究與orchestration這類任務，前沿模型帶來的差距可以到十倍甚至百倍。基礎設施上，Clay用BullMQ維持Agent工作運行，Postgres與ClickHouse存放產品資料，Snowflake做分析，而不是用Temporal或LangGraph；近期上線25到30個新整合，合約與測試花的時間比工程本身還久。

💡 自己訓練模型，門檻落在1000萬到1億美元推理支出之間

Jeff入職前一年半，團隊一直在討論要不要自訓模型，直到最近幾個月才看起來真的可行。他認為降低成本有兩條路：先換成一個現成的開源權重模型（已經比Opus便宜很多），再用自己的工具與查詢對它做post-training，直到在自家任務上追平Opus。他看到兩種常見的錯誤：一是想在單一領域裡打敗前沿模型，這依然非常難；二是在推理支出還沒到位時就急著自訓，省下的成本根本不划算——那個門檻大約落在1000萬到1億美元推理支出之間。至於客戶抱怨的模型選擇器，Clay即將推出能自動依任務挑模型的router，但選擇器不會消失，因為代理商與重度使用者仍然想要控制權。

⚠️ Agent還不能debug Agent

Jeff最想要的是一個能讀懂長串Agent執行紀錄、指出哪一步真正出錯的模型。現在的模型傾向標記耗時最長的那一步，而不是真正出錯的那一步；模型也還會犯基本錯誤，比如用相同輸入反覆重試同一個CLI指令。此外，隨著規模成長，Clay遇到的另一個問題是：使用者習慣每一行資料跑一個Agent，一旦有人對5萬家公司的表格啟動任務，推理需求會瞬間暴增，Clay因此引入LangSmith觀測，並自建節流與暫停／恢復機制應付供應商限流，更難的是如何對所有客戶都公平——小客戶的workflow也要能跟正在處理百萬行資料的企業客戶同時順利跑完。Clay也曾在ChatGPT apps上線前兩天被OpenAI臨時取消合作，當時Clay已投入約四分之一工程團隊整整一個月做這個整合，三、四天後OpenAI又改變主意重新上線。

🎯 實務啟示

想自建Agent平臺的團隊，可以從Clay的經驗裡拿到兩個可操作的參考點：別用單純的LLM-as-judge評Agent的工具呼叫，要拿真實的大規模、邊緣案例去測評測覆蓋率；也別急著自訓模型，先確認推理支出規模是否已經到了post-training真正划算的門檻。

🔗 來源
- 標題：How Clay Builds GTM Agents — Jeff Barg, Head of AI
- 作者／機構：Latent Space
- 連結：https://latent.space/p/how-clay-builds-gtm-agents-jeff-barg-head-of-ai/

#GTM #AIAgents #Clay #LatentSpace #AgentInfrastructure #PostTraining #LLMRouting #SalesAutomation #CodingAgents #AIEngineering
