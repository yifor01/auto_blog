---
title: What a task costs on Opus 5.5
source: Claude Blog
url: https://claude.com/blog/what-a-task-costs-on-opus-5-5
model: claude-code/sonnet
generated_at: '2026-09-22T20:17:53.192132'
pinned: true
---

📌 Opus 5.5 憑什麼比 Opus 5 便宜三成？

TL;DR：Anthropic 拆解 Claude Code 任務的成本結構，說明 Opus 5.5 降價背後省的到底是哪筆錢。

同樣的每 token 單價，兩個模型跑同一個任務的帳單可以差到一倍以上，因為真正燒錢的不是「單價」，而是「跑了幾輪」。

🤔 **一個任務的成本，其實是一個迴圈的成本**

Anthropic 在這篇由 Addy Osmani 撰寫的文章中指出，Claude Code 裡的一個任務本質上是一個迴圈：模型讀取對話紀錄、呼叫工具、讀取結果，然後重複這個過程直到完成。每繞一圈就是一次 request，而每次 request 都會把「目前為止的對話」整包重送一次。也就是說，輪數（turns）愈多，重複傳送的成本就愈高，就算單價完全相同。

🧩 **決定帳單的四個因素**

文章把成本拆成四塊：

- **輪數（Turns）**：每一輪都要重送先前的對話，輪數愈少，處理的 input 就愈少。
- **快取讀取（Cache reads）**：大部分重送的內容其實是上一輪已經看過的文字，會以 cache read 計費，價格只有 input 價的一小部分。
- **輸出 token 類型**：輸出（包含 thinking／推理過程）是最貴的 token 類型，文中提到約為 input 價的五倍；使用者只會看到摘要，但這些推理 token 全部都要付費。
- **模型**：每個模型有自己的定價表，選哪個模型就決定了每一種 token 的價格。

文中以 Opus 5.5 的 API 定價為例：每百萬 input token 4 美元、output token 20 美元、cache read 0.20 美元。

📊 **輪數怎麼影響帳單：一個範例**

文章舉了一個範例：任務一開始 context 是 2 萬 token，隨著模型讀檔案與工具結果成長到 12 萬 token。

- 若跑 40 輪，平均每輪要送出約 7 萬 token，整個任務累積約 280 萬 input token；若有 90% 命中快取，input 成本約 1.62 美元。
- 若同樣的任務只跑 25 輪，累積約 175 萬 token，input 成本約 1.02 美元。

同樣的 280 萬 token，若完全沒有快取命中則要價約 11.2 美元；命中率 90% 降到 1.62 美元；命中率提升到 96% 則約 0.99 美元。文章強調，快取命中率是唯一能把 input 成本壓低到這種幅度的因素。至於輸出端，一個典型任務約 6 萬個 output token，換算成本約 1.2 美元，相當於從快取讀 600 萬 token 的價格，這也是為什麼「思考量」（thinking，計入 output）的多寡對帳單影響很大。

💡 **Opus 5.5 到底改了什麼**

文章指出 Opus 5.5 有兩處變動：單價下降，以及模型完成任務所需的工作量改變。

- Input 與 output 單價都比 Opus 5 便宜 20%。
- Cache read 價格便宜 60%，從 input 價的十分之一降到二十分之一（反推換算，Opus 5 的 cache read 價格約落在 0.5 美元／百萬 token 上下）。
- 在 Pro、Max、Team 方案上，較低的 Opus 5.5 價格也會反映到用量額度，官方表示額度大約可以多用 25%。

文章用一個「相同 token 數，只換模型」的範例來隔離出純粹的價格效應：同一個工作階段若在 Opus 5 上要價 3.5 美元，換算到 Opus 5.5 大約便宜 31%。這還只是價格變動本身的效果；如果 Opus 5.5 實際跑同一任務所需的輪數更少（例如減少「走錯路再重試」的情況），實際省下的金額會更多，但文章也提醒這一點因任務而異，需要各自實測。

⚠️ **省 token 不等於省錢**

文章特別點出一個容易忽略的取捨：降低 effort、換用更小的模型、或減少 context，確實都能省下 token，但如果因此導致任務失敗需要重跑，一次 retry 的成本很可能超過原本省下的錢。換句話說，每一種「省 token」的做法，都可能以「任務做不完」為代價。

🎯 **實務啟示**

文章給出的具體建議是：讓模型有辦法自行檢查工作成果，例如可執行的測試、build 流程，或是能直接呼叫的驗證腳本，這樣模型能更早抓到自己的錯誤，減少不必要的來回輪數；同時盡量在一次工具呼叫中批次蒐集所需資訊，避免同樣的內容被重複重送。若想量化自己團隊的實際狀況，文章建議在任務結束後執行 `/usage` 指令，直接讀出該次 session 的 input、output 與 cache 數據，再依自己的定價與輪數重新試算，而不是直接套用文章中的示意數字。

🔗 **來源**
- 標題：What a task costs on Opus 5.5
- 作者／機構：Addy Osmani, Anthropic
- 連結：https://claude.com/blog/what-a-task-costs-on-opus-5-5

#Anthropic #ClaudeCode #Opus55 #LLM #AIcost #TokenEconomics #AIEngineering #PromptCaching #DeveloperTools #AIProductivity
