---
title: Fixing Tool-Call Accuracy in vLLM
source: Hacker News
url: https://www.ubicloud.com/blog/fixing-tool-call-accuracy-in-vllm
model: claude-code/sonnet
generated_at: '2026-10-26T21:48:01.280332'
score: 96
---

📌 vLLM 的工具呼叫為何失準？約束解碼把 Schema 準確率推到 100%

TL;DR：用 XGrammar 做約束解碼限制 token 取樣範圍，Ubicloud 把 Kimi K2.6 在 vLLM 上的工具呼叫 schema 準確率，從 92% 拉到 100%。

25 次工具呼叫裡有 2 次直接失敗，聽起來不嚴重，但在多輪的 agentic workload 裡，每一次格式錯誤的工具呼叫都會把一堆無意義的錯誤訊息塞進 context，讓後續推理品質一路下滑。Ubicloud 在用 vLLM 0.28 服務 Kimi K2.6 時就遇到這個問題：期望的工具呼叫 schema 只有 92% 的時間能生成正確。

🤔 **為什麼模型會生成格式錯誤的工具呼叫**

工具呼叫的流程分兩步：先把可用工具的 JSON schema 告知模型，再讓模型輸出結構化的呼叫內容，由推理伺服器的 parser 解析成 JSON 物件後交給 agent harness（例如 OpenCode）執行。最簡單的做法是讓模型自由生成、信任訓練成果,這多數時候可行，但模型本質上是機率模型,不是編譯器或型別檢查器,即使 prompt 寫得很清楚，仍可能生成訓練資料裡見過、但目前環境不存在的工具或欄位名稱,例如把現有的 `web_search` 寫成訓練時常見的 `search_web`，或把 schema 要求的 `location` 寫成 `city_name`。

Moonshot AI 為此發布了 K2VV ToolCall 基準,用 2000 個請求評估推理服務「何時觸發工具呼叫」與「生成的呼叫是否符合 schema」,對應兩個指標：trigger similarity（觸發時機與官方服務的相似度）與 schema accuracy（有多少比例的呼叫真正符合 schema、可被成功執行）。

🧩 **約束解碼：在取樣階段就擋掉不合法的 token**

約束解碼的做法是不讓模型自由取樣後再驗證,而是在生成過程的每一步，只允許符合 schema 的 token 被取樣。vLLM 透過 XGrammar 函式庫的 structural tags 實現這套機制,定義出合法的生成路徑：

開始工具呼叫 → 工具名稱 → 工具呼叫索引 → 開始參數 → 符合 schema 的 JSON → 結束工具呼叫

舉例來說，當生成走到「工具呼叫索引」這個階段時，取樣範圍會被限制成只有整數 token，其他所有 token 都被遮罩掉。這把 schema 準確率從「盡力而為」變成「執行期保證」，而且因為遮罩是預先算好、在 GPU 上直接套用,額外的效能負擔相當小。Moonshot AI 官方也建議開啟約束解碼,其自家 API 本身就是這樣運作的。

📊 **升級到官方功能後，準確率反而掉回 91%**

Ubicloud 一開始是在自家的 vLLM fork 裡加入約束解碼。等到 vLLM 0.25 把這個功能併入上游,他們改用官方版本來服務 Kimi 與 DeepSeek,結果工具呼叫準確率卻掉回 91%。

追查後發現 vLLM 本身的約束解碼實作沒有問題，問題出在 vLLM 改變了「沒有明確開啟約束解碼」請求的預設行為。由於 vLLM 要支援非常多種模型,而約束解碼的支援與否是逐模型處理的工作,各模型遇到的問題可以分成三種情況（原文在此處未完整展開）,vLLM 維護者也因此回報,在預設開啟約束解碼後，有多個模型出現了問題。這個功能後來以伺服器端旗標的形式在 vLLM 0.31 正式發布，手動開啟後，新版的 Kimi 與 DeepSeek 模型可以達到 100% schema 準確率。

⚠️ **升級推理引擎版本，不代表功能行為不變**

這個案例的教訓很直接：即使是同一項功能（約束解碼），不同版本的預設行為可能不同。升級推理引擎版本後，原本依賴的最佳化行為可能悄悄被改掉,務必針對關鍵能力（如 schema 準確率）重新跑一次基準測試,而不是假設版本升級只會變好。

🎯 **實務啟示**

如果你在用 vLLM 服務 Kimi、DeepSeek 等支援工具呼叫的開源模型，且 agent 的多輪表現不如預期，第一件事可以檢查的，就是有沒有明確開啟約束解碼這個伺服器端旗標,而不是假設它在新版本裡是預設啟用的。對於 agentic workload，schema 準確率的提升直接等同於更少的無效重試、更乾淨的 context，這筆投資的 ROI 相對清楚。

🔗 **來源**
- 標題：Fixing Tool-Call Accuracy in vLLM
- 作者／機構：coffeemug（Hacker News，原文發布於 Ubicloud）
- 連結：https://www.ubicloud.com/blog/fixing-tool-call-accuracy-in-vllm

#vLLM #LLM #ToolCalling #ConstrainedDecoding #XGrammar #AIAgents #Inference #OpenSource #StructuredGeneration #LLMOps
