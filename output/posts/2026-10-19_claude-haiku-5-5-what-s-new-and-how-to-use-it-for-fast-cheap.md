---
title: 'Claude Haiku 5.5: What’s New and How to Use It for Fast, Cheap AI Workflows'
source: KDnuggets
url: https://www.kdnuggets.com/claude-haiku-5-5-whats-new-and-how-to-use-it-for-fast-cheap-ai-workflows
model: claude-code/sonnet
generated_at: '2026-10-19T21:41:35.566783'
score: 94
---

📌 【Anthropic 最新模型】Claude Haiku 5.5：降價九成,但三處會讓舊程式碼壞掉

TL;DR：Anthropic 推出 Claude Haiku 5.5,context window 擴到 1M token、新增 adaptive thinking,但換了 tokenizer 讓實際省下的成本不到表面數字。

如果你的系統大量呼叫 Haiku 做分類、摘要或資料庫查詢,這次更新值得停下來看一眼：官方列表價砍了九成,但同時悄悄引入了三個會讓 Haiku 4.5 程式碼直接報錯的變動。

🤔 **小模型,為高量、低成本任務而生**

Anthropic 於 2026 年 10 月 7 日發布 Claude Haiku 5.5,API 的 model ID 為 `claude-haiku-5-5`。官方把它定位在高流量、成本敏感的工作上,例如摘要、context 壓縮、資料庫查詢與分類,並可作為搭配 Opus 5.5、Sonnet 5.5 的 subagent。目前已可在 Claude Platform、AWS、Google Cloud 與 Microsoft Azure 上使用,安全評估記錄在官方 system card 中,官網目前列出的最早退役日期是 2027 年 10 月 7 日。

📊 **跟 Haiku 4.5 比,規格全面上調**

| 項目 | Haiku 4.5 | Haiku 5.5 |
|---|---|---|
| Context window | 200K tokens | 1M tokens |
| 最大輸出 | 64K tokens | 128K tokens |
| Thinking 控制 | 手動設定 thinking budget | Adaptive thinking + effort 設定（Haiku 系列首次) |
| 價格／百萬 token（prompt ≤100K,輸入／輸出) | $1.00／$5.00 | $0.10／$0.50 |
| 價格／百萬 token（超過 100K) | $1.00／$5.00 | $0.50／$2.50 |
| 最小可快取 prompt | 4,096 tokens | 512 tokens |
| GDPval-AA（知識工作) | 735 | 1620 |
| OSWorld 2.1 offline subset（電腦操作) | 15.7% | 72.4% |
| Humanity's Last Exam（無工具) | 10.2% | 45.9% |
| Terminal-Bench 4.0（agentic coding) | 0.0% | 39.2% |

這些 benchmark 數字來自 Anthropic 自家公布的結果,而官方發布頁面也顯示 Sonnet 5.5 在這四項全部領先 Haiku 5.5（例如 Terminal-Bench 4.0 上 Sonnet 5.5 拿到 70.6%)。值得留意的是,Haiku 5.5 換了新的 tokenizer,同樣的文字會多算出約 30% 的 token 數,因此 Anthropic 自己估計實際平均省下的成本約 75%,而非表面上看起來的九成——這個估計已經把超過 100K token 的那一成請求算進去。

⚠️ **三個會讓舊程式碼直接報錯的改動**

官方的 what's-new 頁面列出三項破壞性變更：傳入 `temperature`、`top_p` 或 `top_k` 會回傳錯誤；在對話結尾放 assistant prefill 會回傳錯誤；手動設定 `budget_tokens` 的 thinking 方式也會回傳錯誤。另外還有兩個行為變化要注意：adaptive thinking 預設開啟,代表回應可能以一個 thinking block 開頭,而且 thinking token 會計入 `max_tokens` 額度；安全分類器也可能直接拒絕請求,程式必須處理 `stop_reason: "refusal"` 這個情況。安全面上,Anthropic 表示 Haiku 5.5 的資安防護比 4.5 更嚴格,會封鎖滲透測試類請求。

🧩 **用 JSON outputs 做分類與資料擷取**

文章提供的 Python 範例鎖定 Haiku 最擅長的場景：短輸入、短且結構化的輸出,重複跑幾千次。核心函式 `ask_json` 把 schema 放進 `output_config.format`,並將 `effort` 設為 `low`,讓模型在簡單任務上少花時間思考；因為 Haiku 5.5 會拒絕 `temperature` 參數,範例完全沒有設定它。程式碼也刻意檢查 `stop_reason` 是否為 `refusal` 或 `max_tokens`,並在讀取回應文字時依 block type 過濾,因為回應可能先夾帶一個 thinking block。作者選擇用 JSON outputs 而非強制工具呼叫,原因是 Haiku 5.5 雖然接受強制工具呼叫,但 Opus 5.5 會以 400 錯誤拒絕,JSON outputs 才是三個模型都能共用的做法；但要注意 Amazon Bedrock 上的 Haiku 5.5 目前不支援 JSON outputs,得自己在 prompt 裡描述格式並驗證結果。

🎯 **實務啟示**

升級前務必先過一遍這三個破壞性變更,尤其是還在用 `temperature` 或手動 thinking budget 的舊程式碼。也別被「降價九成」的標題誤導,實際省下的成本因 tokenizer 改變大約是 75%,升級前建議用真實流量跑一次 token 計數再估算帳單。若任務牽涉複雜 agentic coding 或推理密集的工作,Sonnet 5.5 在官方 benchmark 上仍全面領先,Haiku 5.5 更適合當成高量、低複雜度任務或 subagent 的角色。

🔗 **來源**
- 標題：Claude Haiku 5.5: What's New and How to Use It for Fast, Cheap AI Workflows
- 作者／機構：Shittu Olumide（KDnuggets）
- 連結：https://www.kdnuggets.com/claude-haiku-5-5-whats-new-and-how-to-use-it-for-fast-cheap-ai-workflows

#ClaudeHaiku #Anthropic #LLM #AIWorkflow #PromptEngineering #JSONOutputs #CostOptimization #Python #APITutorial #AdaptiveThinking
