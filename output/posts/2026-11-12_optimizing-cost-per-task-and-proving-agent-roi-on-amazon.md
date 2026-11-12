---
title: Optimizing cost per task and proving agent ROI on Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/optimizing-cost-per-task-and-proving-agent-roi-on-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-11-12T23:01:44.264387'
score: 89
---

📌 你的 Agent 真的划算嗎?從「每個任務成本」拆解 Amazon Bedrock 真實花費

TL;DR:價格表上的 token 單價不等於實際帳單,AWS 提供一套算真實任務成本與驗證 agent ROI 的具體方法。

同樣一個任務,價格表上「更貴」的模型,實際帳單可能反而便宜 65%。這聽起來違反直覺,但這正是這篇文章想拆解的核心問題:當你只看 Bedrock 定價頁的每 token 價格,你其實看不到帳單真正的樣子。

🤔 問題:每 token 定價,但你付的是每個任務的錢

這篇文章是系列的第二篇。第一篇建立了控制 Bedrock 支出的營運模型:用 IAM principal tags 與 Cost and Usage Report 2.0 做歸因,用模型呼叫日誌做可觀測性,再加上三層執行機制與定期檢視節奏——那一層回答的是「誰花的、能不能擋下來」,但回答不了「這筆錢花得值不值得」。這篇文章要回答兩個問題:這個工作流為什麼貴?以及,這個 agent 真的比人做得好嗎?

任務(task)是你的應用要求模型完成的一個完整工作單位,例如處理一封客服信、從一張發票抽取欄位、回答一個使用者問題,不管中間跑了幾次模型呼叫,從請求到可用結果才算完成。

🧩 四個定價頁看不到的隱藏成本驅動因素

1. Tokenizer 差異:每個模型家族用不同的 tokenizer 與詞彙表,同一段文字、程式碼或 JSON payload 會被切成不同數量的 token。如果 A 模型標價低 15%,但它的 tokenizer 對你的資料需要多切 40% 的 token(結構化 schema 與數值陣列常見這種情況),A 模型反而更貴。非英文文字的落差更大,許多 tokenizer 會把非拉丁字元切成英文等量文字的兩到三倍 token 數。

2. 輸出 token 的溢價:輸出 token 的價格通常是輸入 token 的 3 到 5 倍(比例依模型家族而異)。如果模型不遵守「只回傳純 JSON」之類的格式限制,塞進填充字句,你就得為這些多出來的輸出 token 付溢價;反過來,遵守格式限制的模型能省下這筆錢。

3. 代理式工作流的多輪迴圈:工具呼叫(function calling)需要多輪對話:分析提示、決定呼叫工具、等待結果、產生答案。每一輪都要把完整的對話歷史和工具結果重新當作輸入 token 送出去,跑四輪的模型(且每輪 context payload 越來越大)成本遠高於一輪就結束的模型。

4. 推理 token 的隱藏帳單:支援 extended thinking 的模型會在看得到的答案之前跑一段思維鏈,這些推理 token 算作輸出 token 計費——模型想了 2,000 token 才給出 200 token 的答案,帳單就是 2,200 token,有些模型甚至把推理內容遮蔽起來但照樣收費。文章建議預設關閉推理功能,只有在 benchmark 證明品質差距值得這筆成本時才開啟。

📊 一個具體比較:標價兩倍的模型反而便宜 65%

文章舉了一個代理式工作流的例子:讀取一封 750 字的客戶信、抽取實體、呼叫 API 驗證帳戶狀態、輸出嚴格 JSON 格式(以下為示意價格,請務必用自己的資料與當前 Bedrock 定價重新 benchmark):

| 模型 | 計算方式 | 每任務成本 |
|---|---|---|
| Model A | (6,150 input x $0.50 + 750 output x $1.50) / 1,000,000 | $0.0042 |
| Model B | (1,000 input x $1.00 + 150 output x $3.00) / 1,000,000 | $0.00145 |

Model B 的標價是 Model A 的兩倍,但實際成本反而低 65%,原因是三個因素疊加:Model A 的 tokenizer 把這封信切成多 50% 的 token,拉高每個輸入 payload;它在 JSON 輸出裡塞填充字句,讓輸出 token 翻三倍;再加上它沒對齊工具 schema,需要兩輪修正,每輪都重送越來越大的歷史紀錄。

文章也給出失敗情境下的成本公式:若工作流是「重試到成功」,每個成功任務的成本 = 每次嘗試成本 / 成功率;若工作流是「失敗就升級」,每個成功任務的成本 = 每次嘗試成本 + (1 - 成功率) x 升級成本。另外,開啟 prompt caching 後,輸入 token 還會再拆成未快取(基礎費率)、快取讀取(低於基礎費率)、快取寫入(高於基礎費率)三種計費方式。

💡 四個驅動因素,各有對應的 Bedrock 功能

哪個模型真的划算,只有拿自己的資料 benchmark 才看得出來。Amazon Bedrock model evaluation 負責品質這一半:定義評估標準、上傳自己的 prompt 資料集,得到含自動指標與可選人工審查的評分結果。再搭配三個功能解決成本這一半:prompt caching 減少重送的 context,在代理式工作流上收益最大;intelligent prompt routing 把簡單請求導向同家族裡較便宜的模型;工具 schema 加上 maxTokens 上限,比純文字指令更可靠地壓低冗長輸出,extended thinking 則維持關閉直到 benchmark 證明值得;batch inference 能把單輪、非工具呼叫的大量任務費率砍半,但不支援工具呼叫與多輪對話。

🎯 省錢之外:證明 agent 真的比人做得好

優化成本和證明價值是兩件事,一個被完美優化的 agent 仍然可能不值得跑。文章指出最常見的錯誤,是在沒有先描述現有人工流程之前就想證明 agent 的價值。正確順序是:先用營運語言寫下現有流程(誰觸發工作、哪些角色參與、交接點在哪、怎麼算完成),這看似官僚作業,其實是在設計測量方法——後續「什麼算一次執行」、「什麼算成功」、「人力花在哪裡」都是從這份描述推導出來的。

接著要在 agent 上線前量出人工基準線:完成時間、排隊時間、實際投入的工作時間、重開率、升級率、每任務成本、產出品質。基準線必須在上線前量測,事後回想會系統性地偏向美化 agent,因為人只會記得平均情況,忘了最快的那幾次。agent 上線後則要從第一天就把它當成一個實驗來追蹤:每次執行都有 trace ID,每個關鍵步驟都可觀測,彙總成一筆工作流執行紀錄。文章特別點出其中最常被遺漏、卻最該有的欄位是 humanMinutes(人力投入時間),以及在執行建立時就打上、並一路傳遞進 Bedrock request metadata 的實驗區塊標記,讓模型層與工作流層的紀錄可以乾淨地對應起來。

🔗 來源
- 標題:Optimizing cost per task and proving agent ROI on Amazon Bedrock
- 作者/機構:Majd Arbash(AWS ML Blog)
- 連結:https://aws.amazon.com/blogs/machine-learning/optimizing-cost-per-task-and-proving-agent-roi-on-amazon-bedrock/

#AmazonBedrock #AgentROI #CostOptimization #FinOps #LLMCost #PromptCaching #AIAgents #TokenEconomics #MLOps #AWS
