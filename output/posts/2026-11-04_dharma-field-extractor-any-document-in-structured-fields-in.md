---
title: 'Dharma Field Extractor: Any Document In, Structured Fields in JSON Out'
source: HuggingFace Blog
url: https://huggingface.co/blog/Dharma-AI/dharma-field-extractor
model: claude-code/sonnet
generated_at: '2026-11-04T22:54:31.647988'
score: 83
---

📌 20 億參數打敗 Claude Opus 5:Dharma 的欄位抽取模型

TL;DR：Dharma AI 推出 2B 參數模型,專做「文件轉結構化 JSON 欄位」,品質與成本同時贏過前沿 LLM。

OCR 能把一張發票上的每一行文字原封不動還原出來,但它不會告訴你哪一個字串是日期、哪一個數字是總額。這中間的「對應到資料庫欄位」的工作,還是得靠人寫程式碼補上——除非你換一個專門做這件事的模型。

🤔 **OCR 給你整頁文字,但你要的是幾個欄位**

Dharma AI 今年四月發表的 DharmaOCR-LITE,是一個針對合約、法院文件、發票、證件、表單等文件做 OCR 的專精模型,用更小的模型打敗通用前沿 API 完成「還原整頁文字」的任務。但很多業務場景要的不是整頁文字,而是裡面幾個特定欄位:發票上的每一筆品項、就診單上的病患姓名與檢查日期、證件上對應到員工紀錄欄位的資料。通用 LLM 靠細心設計的 prompt 也能做到,但在需要高頻次執行的場景下,frontier API 的計價與延遲會迅速變得昂貴。Dharma AI 因此另外訓練了一個模型來專門處理這個任務。

🧩 **兩種請求模式,同一個 checkpoint**

Field Extractor 接受一張文件影像,搭配兩種請求方式:

- Open 模式:不提供 schema,模型自己從版面與上下文判斷哪些部分是結構化欄位(標籤後面接著值、表格有對應的表頭欄),回傳所有找到的 key-value pair。
- Schema-directed 模式:使用者指定確切要的欄位名稱與型別(字串、數字、布林),模型就按照這些 key 名稱填值,文件上找不到的欄位回傳 null,而不是編造內容。

同一個 checkpoint 處理所有文件類型,不需要針對每種文件單獨微調。底層是 DharmaOCR-LITE v1.1(2B 參數,透過 supervised fine-tuning 與 DPO 專精化後的新版本),在其上訓練一個 LoRA adapter,使用 43,384 筆涵蓋兩種請求模式的訓練資料,分三個資料流:英語多領域文件、巴西本地文件(葡萄牙語)、以及涵蓋其他歐亞語言的小比例多語資料,三者都在欄位層級做標註。

📊 **F1 0.834,比 Claude Opus 5 還高,成本卻低上百倍**

評測集涵蓋 546 份文件、三種請求情境(無 schema 全抽取、只含真實欄位的部分 schema、刻意加入不存在欄位的 schema)共 1,638 個測試案例,評分方式是欄位層級 F1(依路徑比對,含表格內位置),乘上比對成功數值的 Levenshtein 相似度,再乘上輸出為合法 JSON 的比例。

結果顯示,Field Extractor 拿下 0.834 分,高於測試中每一個前沿模型配置:最接近的 Claude Opus 5 為 0.816(差距 1.8 分),差距最大的 GPT-5.6 Luna 為 0.741(差距 9.3 分)。成本方面,Field Extractor 比各前沿 API 便宜約 6 倍(對比 GPT-5.6 Luna)到 147 倍(對比 GPT-5.6 Sol),前沿模型的成本是依實測每頁平均輸入輸出 token(含 reasoning token)乘上各家公開列表價計算,所有前沿模型都設為低 reasoning(Claude Opus 5 用 adaptive effort),而 Field Extractor 的成本基準是自架在單張 L40S GPU、每小時 2.24 美元的算力費用。

在兩個未納入訓練的公開資料集上做泛化測試:SROIE 收據要求抽取全部 18 個欄位,結果全部正確,包含跨行無標籤的帳單地址被正確整合為單一欄位,兩個空白欄位(業務員、參考號)正確回傳 null,所有數字都精確到小數點。FUNSD 的影印品質變異表單是一份 12 個布林欄位的檢查清單(含一組五個子選項),模型正確標記唯一被勾選的那一項為 true,其餘為 false,也正確讀出手寫的 Bates ID,並對兩個空白欄位回傳 null。

💡 **成本比較的前提要說清楚**

Dharma AI 自己也強調,這個成本對比不是銷售報價,自架成本會隨硬體、流量、延遲需求不同而變化,比較的重點在於證明「自架的 SSLM 是前沿 API 的真實替代方案」,而不是給出一個通用定價結論。

🎯 **實務啟示**

如果你的 pipeline 需要從大量文件中穩定抽出固定欄位(發票、表單、證件),與其每次呼叫 frontier LLM 配合 prompt engineering,評估像 Field Extractor 這種支援 schema-directed 輸出、且對未知欄位回傳 null 而非幻覺值的專精小模型,可能同時拿到更高品質與更低的單次抽取成本。

🔗 **來源**
- 標題：Dharma Field Extractor: Any Document In, Structured Fields in JSON Out
- 作者／機構：Dharma AI
- 連結：https://huggingface.co/blog/Dharma-AI/dharma-field-extractor

#DocumentAI #OCR #StructuredExtraction #SmallLanguageModels #LoRA #JSON #EnterpriseAI #OpenSourceAI #DataExtraction #AIBenchmarking
