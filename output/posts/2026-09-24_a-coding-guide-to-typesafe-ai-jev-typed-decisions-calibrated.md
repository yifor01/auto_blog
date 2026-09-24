---
title: 'A Coding Guide to TypeSafe AI Jev: Typed Decisions, Calibrated Confidence,
  and Speculative Fan-Out with a System One Model'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/23/a-coding-guide-to-typesafe-ai-jev/
model: claude-code/sonnet
generated_at: '2026-09-24T20:50:40.586574'
score: 83
---

📌 Jev教學：AI模型不寫文字，只回你機率與分數

TL;DR：TypeSafe的System One模型Jev拿掉文字生成，直接回傳可讓程式碼分支的typed決策。

🎣 多數LLM教學都在教你用更好的prompt拿到更精準的文字輸出，再自己寫程式碼把文字剖析回結構化資料。MarkTechPost這篇教學介紹的Jev，乾脆把「生成文字」這一步整個拿掉。

🤔 問題：文字輸出中間還要再剖析一次，太浪費
當你需要的其實只是「這個客訴符合退款政策嗎」「這封信該分到哪個意圖類別」這類是非題或選擇題，讓LLM先生成一段文字說明、再由程式碼剖析成布林值或列舉值，等於多繞了一圈，剖析步驟本身也是額外的錯誤來源。TypeSafe AI的System One模型Jev想解決的正是這個問題：模型不輸出自然語言，只輸出選項、分數與是非機率，讓程式碼直接拿去做判斷分支。

🧩 三種typed問題原語，一次request平行作答
一次System One請求由兩部分組成：state（描述情境的文字、JSON物件或陣列）與一組具名問題。三種問題型別分別是：
- Choice：從你定義的選項中挑一個標籤，並回傳每個標籤的機率。
- Score：把狀態放到一個有序量表上，回傳機率加權後的等級，結果因此可以落在兩個等級之間。
- Noul：回傳單一「這句話是否為真」的機率。

問題的名稱只是給你自己看的，不會傳給模型，真正決定模型理解的是問題描述本身，且可以用反引號路徑指向state裡的巢狀欄位。同一個request中的所有問題會平行、且彼此隔離地被回答，回應中還會附上實際應答的模型版本與計費token數。

📊 state怎麼寫，答案就怎麼變
教學做了一個對照實驗：同一個問題（顧客是否符合退款政策資格）分別餵三種state——純字串的客訴內容、加上對話紀錄的陣列、再加上訂單明細與退款政策全文的JSON物件。問題本身完全沒變，答案機率的差異因此完全來自state內容的豐富程度，token欄位也同步顯示多餵脈絡要付出的成本。文件建議只要state有多個部分，就該用具名欄位，讓instruction可以直接點名引用。

confidence這個統計量的定義也很明確：選項數乘上最高機率，減一，再除以選項數減一。教學實際從Choice回傳的機率重新算一次，驗證跟API回傳的confidence欄位一致；Score則是把每個等級乘上其機率後加總回推。Noul本身沒有confidence欄位，因為它的值本身就是「是」的機率，接近0.5代表模型無法判斷，而不是「中等把握」。

批次測試也證實了「彼此隔離」的設計：把10個問題（2個Choice、2個Score、6個Noul）塞進同一個request，跟拆成10次個別呼叫相比，前者的延遲與輸入token都明顯較低，原因是state只需要傳一次；agreement欄位則驗證同一個問題無論獨自出現還是跟其他問題一起出現，答案都一致。

🧩 四種可直接套用的生產模式
教學展示了幾種把typed答案組裝成決策服務的寫法：
- confidence-gated routing：依意圖分類並設定隨風險升高的confidence門檻（例如查詢餘額0.5、關閉帳戶0.9），未達門檻或分類為other一律轉人工處理。
- composite scoring：每個候選人問四個Score問題，各自除以最高等級做正規化後存表，再用一組寫在程式碼裡的權重向量做排序，換職位權重就能立即重新排名，且每個名次都能回推是哪個維度貢獻的。
- typed function calling：一個Choice選工具（含一個明確的none選項），每個參數各自用一個Choice在同一request內推測性地問完，程式只讀取被選中工具對應的參數，並把最弱的那個判斷當作整體呼叫的confidence。
- 計數的workaround：因為Jev在單一問題內無法可靠計數，教學改成對每個項目各問一個Noul，加總的工作交還給程式碼處理。

生產化還有四個細節：用Pydantic繼承SystemOneResponse拿到型別安全的屬性存取；AsyncTypeSafeClient搭配asyncio.gather平行送出整批獨立決策；RetryPolicy控制重試次數、退避與總時間預算；把錯誤也typed化，例如空的問題集合會在送出請求前就被擋下，未知模型名稱則會拋出帶HTTP狀態碼的TypeSafeAPIError。

⚠️ 已知限制：模型不擅長數數
教學明確指出Jev在單一問題內無法可靠計數，這也是為什麼要拆成多個Noul再由程式碼加總，是這個typed問答設計目前已知且被文件化的限制。

🎯 對工程師的實務啟示
如果你的agent或分類系統裡有大量「這個要不要做」「該路由到哪」的判斷，把這些判斷改寫成typed問題丟給類似Jev的System One模型，好處是風險門檻、排序權重都留在自己的程式碼裡，可以照一般程式碼一樣做code review、版本控管與測試，而不是埋在prompt字串裡不好追蹤。批次送出共享同一個state的問題，也是容易被忽略但能直接省下延遲與token成本的做法。

🔗 來源
- 標題：A Coding Guide to TypeSafe AI Jev: Typed Decisions, Calibrated Confidence, and Speculative Fan-Out with a System One Model
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/23/a-coding-guide-to-typesafe-ai-jev/

#TypeSafeAI #Jev #SystemOneModel #LLMEngineering #StructuredOutput #AIagents #PythonSDK #FunctionCalling #ConfidenceScoring #ProductionAI
