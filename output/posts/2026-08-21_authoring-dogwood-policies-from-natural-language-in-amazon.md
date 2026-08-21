---
title: Authoring Dogwood policies from natural language in Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/authoring-dogwood-policies-from-natural-language-in-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-08-21T06:33:25.358121'
score: 87
---

📌 【AWS新功能】白話政策秒變可執行規則

TL;DR：AWS新工具能把白話政策文件，自動轉成可即時執行的正式規則。

AI agent一旦被賦予呼叫工具的權限，等於同時被賦予犯錯的空間。與其把規則寫進文件指望agent自己遵守，不如把規則變成程式碼強制執行；但要親手寫一套正式規格語言，多數團隊根本沒有這種人力。AWS這次更新的Policy Authoring，想解決的正是這個落差。

🤔 Agent失控的風險，需要即時攔截

AI agent能自動化複雜工作流程，但若缺乏適當控制，可能採取不符合組織政策或法規限制的行動。為此，Amazon Bedrock AgentCore建置了Policy功能，讓團隊能對執行中的agent套用統一控制。近期這項功能新增了跨時間限制的能力，例如速率限制、工具呼叫的前置條件與順序要求、以及累積效果限制。這些政策以開源治理語言Dogwood表示，並由內建於AgentCore Gateway的Dogwood監控器即時套用到agent的行動上。

🧩 Policy Authoring：把政策文件當「翻譯」而非「摘要」

這次新增的Policy Authoring，是一套AI驅動工具，能把自然語言撰寫的政策規格文件，轉換成語法與語意都正確的Dogwood正式規格。新版除了原本就支援的工具輸入參數限制，還能產生涉及時間與行動軌跡限制的政策，並可呼叫Amazon Bedrock Guardrails服務，偵測自由文字語意中的不當內容。

運作上，Authoring會搭配一份從agent的Model Context Protocol（MCP）工具清單自動產生的schema，包含工具名稱、參數與回傳值，確保產生的政策引用的是agent實際呼叫時使用的名稱；同時也會取得可用的Bedrock Guardrails檢查項目，以及政策可以引用的身分聲明。AWS建議，Policy Authoring最適合用在已有一套散文形式規則、工作內容偏向「轉錄」而非「設計」的情境；如果文件把規則和背景說明、理由夾雜在一起，最好先整理出純粹的規則部分。此外有兩個慣例：Dogwood預設為拒絕（default-deny），且forbid會覆蓋permit，所以授予能力的規則會變成帶條件的permit，限制或設上限的規則則會變成forbid；條件既可以檢視當前這次呼叫，也可以檢視同一個session裡已經發生過的事。

📊 六個銀行客服案例：從白話規則到Dogwood公式

文章以一個零售銀行客服agent為例，示範六條規則的轉換結果。退款只能在營業時間（UTC上午9點到下午5點）且金額在2,500美元以下時核准，被轉成一條帶兩個條件的政策，兩個條件都要成立才放行。除非來電者身分在過去15分鐘內針對同一帳戶完成驗證，否則不得啟動轉帳，這條規則無法只看轉帳請求本身判斷，因此生成的條件會查詢session歷史，區分歷史事件裡的欄位與當前呼叫的欄位，確保「同一帳戶」精準對應。若過去12小時內的轉帳總額將超過5萬美元則封鎖轉帳，這條規則不是查詢歷史，而是加總歷史事件裡的金額欄位；由於原文只寫「轉帳」，沒說明失敗或被拒的嘗試算不算數，生成結果採取較保守的讀法，把每一次嘗試都算進去。同一帳戶一小時內最多嘗試三次退款，這條規則明確寫了「嘗試」，因此連被拒或失敗的退款都算數，當前這次呼叫本身也算在計數內，所以第四次嘗試會被拒絕。爭議申報內容若包含社會安全碼則予以拒絕，這類規則涉及自由文字的語意判斷，生成的政策會直接呼叫Bedrock Guardrails檢查，並比對信心分數與門檻值，原文沒寫門檻就採用該檢查項目的預設值，若寫了具體數字或「高信心」等描述則會照樣沿用。超過500美元的退款需要主管在過去30分鐘內核准該筆款項，這條規則同時包含對當前呼叫參數的門檻檢查，以及對session歷史的條件檢查，兩者以不同方式驗證。

💡 語意留白比想像中常見

從轉帳上限那個例子可以看出，白話文件裡經常存在沒說清楚的模糊地帶，例如「轉帳」到底算不算失敗的嘗試。Policy Authoring遇到這種情況會採取較安全的預設讀法，但AWS明確建議，與其讓工具去猜，不如把這類邊界情境直接寫進原始文件裡，這樣才能徹底消除模糊。

🎯 實務啟示

對負責治理agentic系統的團隊來說，這是個可行的模式：合規規則繼續用團隊原本熟悉的散文形式維護，再交給AI翻譯成可即時執行的正式政策；而讓生成的政策精準對齊agent實際介面的關鍵，在於schema直接來自MCP工具清單。另外，撰寫政策文件時，遇到「失敗的嘗試算不算」這類邊界情況，最好明確寫出來，而不是留給翻譯工具去猜。

🔗 來源
- 標題：Authoring Dogwood policies from natural language in Amazon Bedrock AgentCore
- 作者／機構：Sandesh Swamy（AWS）
- 連結：https://aws.amazon.com/blogs/machine-learning/authoring-dogwood-policies-from-natural-language-in-amazon-bedrock-agentcore/

#AgenticAI #AWS #AmazonBedrock #AIGovernance #PolicyAsCode #LLMAgents #ResponsibleAI #MCP #CloudAI #AISafety
