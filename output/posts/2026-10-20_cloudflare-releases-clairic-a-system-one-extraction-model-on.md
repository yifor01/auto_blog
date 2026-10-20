---
title: Cloudflare Releases Clairic, a System One Extraction Model on Workers AI
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/20/cloudflare-releases-clairic-a-system-one-extraction-model-on-workers-ai/
model: claude-code/sonnet
generated_at: '2026-10-20T20:55:28.803532'
score: 88
---

📌 Cloudflare Clairic：抽取不用生成，一次前向出結果

TL;DR：Cloudflare 推出 System One 抽取模型 Clairic，免推理、免輸出 token，把 LLM 常做的欄位抽取任務獨立出來。

當你只是想從一張發票裡挖出總金額、日期和單號，為什麼要讓一個會「思考」的 LLM 逐字生成答案？Cloudflare 給出的答案是：不需要。新推出的 Clairic 讀入文字或圖片，直接回傳帶型別的值，整個過程只跑 1 次前向傳遞（forward pass），沒有 reasoning，也沒有輸出 token。

🤔 **抽取、決策、生成，三件事不該用同一個模型做**

Cloudflare 把整個 agentic 流程拆成 3 層架構：抽取模型（extraction models）把原始輸入轉成帶型別的值；決策模型（decision models）把值轉成決策；LLM 再把決策轉成文字。Clairic 承接的是第一層，概念延伸自 TypeSafe 的 Jev 所提出的「System One」構想（取自 Kahneman 快速直覺思考的比喻）。Jev 與 Cloudflare 自家的 Clef 都是決策模型，負責在你預先列出的選項中評分；而 Clairic 處理的是那些你無法預先窮舉的答案，例如一張發票的總金額、一個日期，或一筆維修費用的估算。

🧩 **一個請求，裡面是 state 加上一張型別欄位表**

Clairic 的請求結構由兩部分組成：state（文字加上最多 4 張圖片）與一張具名、帶型別的欄位表，每個欄位都可以附加自然語言指示。支援的型別包括 text、number、date、time、datetime、duration、list、estimate 與 forecast（依 Workers AI changelog）。每個純量（scalar）答案都會附上 p_null（代表該值不存在的機率）與信心分數；文字答案則回傳精確的文字片段與字元偏移量；estimate 與 forecast 回傳中位數與 80% 區間（p10 到 p90），forecast 最長可預測 64 個時間步。欄位數量沒有上限：若欄位在單一 8,192-token 的視窗內放不下輸入，系統會自動拆成多個平行 pass，每個 pass 都能看到完整輸入內容。

📊 **測試數據：發票、客服信、天氣預報到理賠流程**

文件範例中，一張 61-token 的發票被拆成 3 個 pass 處理，共計入 655 input token（其中 472 token 來自欄位表本身）——欄位表寫得越寬，有時比文件內容本身更貴。在一個客服信範例裡，Clairic 自行把金額和稅額相加得出 $701.10，也計算出「到貨已 11 天」，兩個數字都未直接出現在原信中；面對一張缺少追蹤單號的信件，它正確回傳 null 而非亂猜。一張歪斜拍攝的收據照片中，它讀出全部 7 個存在的欄位值，並對缺失的折扣欄位回傳 null，最低信心分數落在訂單號碼上，為 0.776。在天氣預測測試中，Clairic 預測連續 21 天的 TSA 安檢站通關人數，平均誤差 3.3%，21 天中有 17 天的實際值落在 80% 區間內，4 次失準中有 3 次發生在 Columbus Day 連假。

主測試是一條「商品損壞理賠」流程：Clairic 抽取事實、Clef 決定退款或維修、GLM-5.3 撰寫回覆信。對照組是讓 GLM-5.3 單獨完成全部 3 個步驟。分工版流程 19.3 秒完成，全 LLM 版本要 61.7 秒，快了約 3.2 倍；其中抽取步驟 0.46 秒對比 16.1 秒，決策步驟 0.22 秒對比 21.9 秒。每百萬筆理賠成本從 $11,740 降至 $6,032，下降 49%。回覆撰寫步驟仍是耗時大頭，佔分工版 19.3 秒中的 18.6 秒。兩條流程都得出正確事實與決策，但 Clairic 的維修估價在多次執行中結果一致，GLM-5.3 同一題卻分別給出 $250、$250、$220。Cloudflare 也提到，Gemma 4 與 Qwen 在全 LLM 版本的測試中未能通過。

💡 **定價與可用性**

Clairic 已以 preview 形式上線，模型 ID 為 @cf/cloudflare/clairic，可透過 Workers AI binding 的 env.AI.run() 或 REST API 呼叫，AI Gateway 也支援同一組端點。定價為每百萬 input token $0.10，沒有輸出費用，介於 Jev 的 $0.042 與 Clef 的 $0.24 之間。模型權重目前只是「承諾釋出」，尚未公開。

⚠️ **欄位表本身就是成本**

從發票範例可以看出，欄位 schema 越複雜，所佔的 token 比例可能遠超輸入內容本身，這是設計 extraction schema 時需要留意的取捨。

🎯 **實務啟示**

如果你的 pipeline 裡有大量「抽取 + 決策 + 生成」混用同一顆大模型的步驟，Clairic 這類專用抽取模型的案例顯示，把流程拆開可能同時換來更低延遲、更低成本與更一致的輸出，值得在自己的 agentic workflow 中評估是否要拆分這三層。

🔗 **來源**
- 標題：Cloudflare Releases Clairic, a System One Extraction Model on Workers AI
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/20/cloudflare-releases-clairic-a-system-one-extraction-model-on-workers-ai/

#Cloudflare #WorkersAI #Clairic #AgenticAI #StructuredExtraction #EdgeAI #LLM #AIInfrastructure #MachineLearning #TypedOutputs
