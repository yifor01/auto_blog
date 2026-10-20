---
title: Structured outputs for Anthropic Claude models on Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/structured-outputs-for-anthropic-claude-models-on-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-10-20T20:55:28.803684'
score: 84
---

📌 Claude on Bedrock 結構化輸出：schema 違規不再發生

TL;DR：Amazon Bedrock 為全系列 Anthropic Claude 模型補上 structured outputs,輸出保證符合 JSON schema,免寫解析與重試邏輯。

每個串接過 LLM API 的工程師大概都寫過同一段防禦性程式碼:try 解析模型回傳的 JSON,失敗就重試,再失敗就 fallback。Amazon Bedrock 這次的更新,目的就是讓這段程式碼可以直接刪掉。

🤔 **從機率輸出到決定性輸出**

Amazon Bedrock 現在為所有 Anthropic Claude 模型提供 structured outputs,涵蓋 bedrock-runtime 與 bedrock-mantle 兩個端點(視模型可用性而定)。無論你是透過 Boto3 呼叫 bedrock-runtime API,還是透過 Messages API 呼叫 bedrock-mantle 端點,現在都能拿到符合你所定義結構的 schema-compliant JSON,不再需要客製解析、重試邏輯或後處理。官方列舉的應用場景包括:從財報與合規文件中抽取所有必填欄位、把臨床筆記解析進電子病歷(EHR)、為商品目錄補上一致且經驗證的屬性資料、分析合約中的關鍵條款與當事方,以及讓客服工單路由的意圖、情緒、實體辨識結果穩定對應到應用程式的資料模型。

🧩 **約束解碼:在生成過程中就擋掉違規 token**

核心機制是 constrained decoding:在 token 生成的當下就強制套用 JSON schema,而不是生成完再事後校驗。模型本身不會產生違反 schema 的 token,因此輸出格式從機率性變成決定性。兩個端點都支援兩種互補機制:一是保證回應永遠是合法 JSON,不再出現 JSON.parse() 錯誤;二是型別安全,欄位型別被強制、必填欄位一定存在。因為輸出永遠符合 schema,不需要靠重試處理 schema 違規,也因為回應只包含 schema 定義的欄位,可以降低輸出 token 數量,對高流量工作負載有助於降低推論成本。

這項功能也支援 batch inference,可以非同步處理大量請求同時維持 schema 合規;在 bedrock-runtime 端點上,也相容於 cross-Region inference,不需額外設定;若需要即時回應,也能以 typed events 的形式串流結構化回應。

在效能上,第一次使用新 schema 的請求會比較慢,因為 Bedrock 需要先編譯出 grammar artifact 才開始生成;之後用同一個 schema 的請求就會因為命中快取而開銷很小。這個快取範圍限定在帳號內,自首次存取起保留 24 小時。改變 JSON schema 的結構會讓快取失效並觸發重新編譯,但只改 name 或 description 欄位則不會動到已快取的 grammar。

在 API 使用上,InvokeModel API 接受 Anthropic 原生的 request body,schema 要放進 output_config.format,作為 JSON 物件而非 JSON 字串傳入。bedrock-mantle 端點則是針對 agentic 應用設計,支援 server-side tools、背景推論與有狀態對話;透過 strict tool use,可以保證工具參數完全符合你定義的輸入 schema,例如把 location 欄位強制為字串、unit 欄位強制只能是 celsius 或 fahrenheit,模型無法額外塞入 schema 之外的欄位。這對 Bedrock Mantle 上以多步驟工作流程呼叫 web search、code interpreter 等 server-side 工具的 agentic 場景特別有價值。

📊 **一個實際場景:Claude Haiku 5.5 處理分類與路由**

官方以 Claude Haiku 5.5 為例,說明它適合處理摘要、壓縮、資料庫查詢與分類這類快速且重複的工作負載,並展示了用 Invoke API 搭配 Haiku 5.5 對輸入資料做分類與路由的範例。

⚠️ **有些 schema 關鍵字只是「建議」,不是「強制」**

文件特別提醒,有些 JSON schema 關鍵字雖然 API 會接受,但生成過程中並不會真的強制套用;就算請求中包含這些關鍵字,回應仍可能成功但數值違反該約束。官方建議這類限制應該在應用層自行驗證,不要依賴 schema 本身來強制執行。

🎯 **實務啟示**

如果你的 pipeline 現在還依賴 prompt 技巧(例如「請務必輸出合法 JSON」)加上事後 try/except 重試來保證格式正確,這類原生的 constrained decoding 方案值得評估替換,尤其是在高流量、對格式正確性要求嚴格的生產場景。同時也要記得,schema 保證的是「格式正確」,不是「語意正確」,官方提醒的那些僅接受但不強制的關鍵字,就是提醒你驗證邏輯不能完全外包給 schema。

🔗 **來源**
- 標題：Structured outputs for Anthropic Claude models on Amazon Bedrock
- 作者／機構：Anshika Saxena, AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/structured-outputs-for-anthropic-claude-models-on-amazon-bedrock/

#AmazonBedrock #Claude #Anthropic #StructuredOutputs #JSONSchema #AgenticAI #ConstrainedDecoding #AWS #LLMEngineering #ProductionAI
