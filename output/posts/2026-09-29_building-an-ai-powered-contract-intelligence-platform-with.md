---
title: Building an AI-powered contract intelligence platform with Amazon Quick and
  Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/building-an-ai-powered-contract-intelligence-platform-with-amazon-quick-and-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-09-29T21:45:34.739241'
score: 84
---

📌 AWS 合約智慧平臺：RAG 為何算不出合約總金額

TL;DR：RAG 擅長回答單一合約問題，卻算不出「250 份合約總值多少」，AWS 改用結構化萃取加雙模型驗證解決。

假設你手上有 250 份供應商合約，每份 10 到 20 頁，加總起來上看 5,000 頁非結構化資料。主管隨口問一句「我們花最多錢的供應商是誰」，你要嘛派人一份份翻閱、抄進試算表，要嘛把整批 PDF 丟給市面上的 AI 聊天工具問答。後者聽起來很誘人，答案也來得又快又篤定，卻常常是錯的。

🤔 問題不在提示詞，而在架構本身

AWS 在部落格中指出，這個錯誤答案不是偶然，而是內建在多數 AI 問答工具的運作方式裡。這些工具內部把每份文件切成一段段文字並向量化，存進知識庫；使用者提問時，系統只取回與問題最相關的 top-k 段落，再用這些段落組出答案。對於「AnyCompany 合約的付款條件是什麼」這類單點查詢，這套機制運作得很好，正確段落會被準確撈出。但換成「250 份合約的總值是多少」這種橫跨整個組合的聚合問題，系統依然只回傳 top-k 段落，並只針對這些段落做加總，因為完整的合約組合根本沒有被放進模型的上下文裡。這不是某個工具做得不夠好，而是 Retrieval Augmented Generation（RAG）機制本身的局限：更好的提示詞救不了它，需要的是不同的架構。

🧩 用結構化萃取取代單純檢索

AWS 團隊的解法是：把合約裡的關鍵欄位先萃取成結構化資料存進資料庫，再交給專門做分析的工具去查詢與計算，讓 AI 負責處理「非結構化轉結構化」，資料庫負責處理「數學」。同時保留原始文件建立知識庫，供單一合約問答使用，達成「橫跨整個組合的聚合問題」與「精準的單一文件查詢」兩者兼顧。

整套流程用 Strands Agent SDK 建構，部署在 Amazon Bedrock AgentCore 的 runtime 上，由 AgentCore 負責無伺服器（serverless）託管、自動擴縮與 session 隔離，AI 元件本身不需要維運任何基礎設施。透過 Amazon Bedrock AgentCore 的 Policy 功能，團隊以 Cedar-based 政策定義安全控管邊界，在執行前先以自動化推理驗證，確保合約定價條款、財務承諾、供應商關係等敏感資訊只有被授權的 agent 與使用者才能存取。

核心是雙模型設計：一個模型負責萃取欄位，另一個獨立模型負責驗證。兩個獨立模型互相不同意，本身就是一個「該交給人類覆核」的強訊號，比單一模型自信滿滿地產出幻覺數值要安全得多。團隊在測試中發現一個很具體的失敗模式：驗證模型有時會以 95% 到 100% 的信心把某份合約標記為「已簽署」，但實際上根本沒有簽名，原因是模型把「簽名欄位」本身（例如「Signature: __________」這樣的空白欄）誤判成簽名已存在的證據。團隊沒有選擇用更精巧的提示詞硬凹過去，而是引入 Amazon Textract 的電腦視覺簽名偵測作為架構上的仲裁者：Textract 靠視覺分析而非語言理解來判斷頁面上是否真的有手寫或數位簽名，且只在兩個模型意見分歧時才啟動，藉此把成本控制在最低,同時抓住這種假陽性。這說明了一個實務上很值得參考的分工原則：LLM 適合處理文件理解、欄位萃取、上下文判讀；視覺元素偵測、精確計數、數學運算則交給確定性（deterministic）服務去做。

團隊也拿一組 20 份合約的樣本資料，人工標註全部 8 個欄位（總計 160 筆數值）建立 ground truth，用來比較不同萃取模型與驗證模型組合的表現，藉此決定最終要採用哪一種模型搭配。

⚠️ 模型會變，架構思路才是重點

AWS 在文中特別提醒，文中提到的模型是解決方案建置當下可用的版本，模型選項變化很快，讀者若要參考落地，應該以自己當下能取得的模型重新測試,而不是照搬文中的模型組合。

🎯 實務啟示

當你的 AI 應用場景需要「跨文件聚合」而不只是「單點查詢」時，先問自己一個問題：答案是不是需要對整個資料集做加總、計數或比較？如果是，單純加大 RAG 的 top-k 或寫更精巧的提示詞多半沒有用，真正該做的是把非結構化資料先萃取成結構化欄位，讓資料庫或分析工具去處理數學運算，同時用雙模型互相校驗、搭配確定性服務仲裁分歧，把 LLM 的幻覺風險關進一個可控的範圍裡。

🔗 來源
- 標題：Building an AI-powered contract intelligence platform with Amazon Quick and Amazon Bedrock AgentCore
- 作者／機構：Konala McGrath, AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/building-an-ai-powered-contract-intelligence-platform-with-amazon-quick-and-amazon-bedrock-agentcore/

#AWS #BedrockAgentCore #RAG #AIAgents #ContractIntelligence #StrandsAgentSDK #AmazonTextract #StructuredExtraction #LLM #EnterpriseAI
