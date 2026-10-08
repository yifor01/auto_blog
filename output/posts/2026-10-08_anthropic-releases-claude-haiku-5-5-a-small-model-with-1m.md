---
title: 'Anthropic Releases Claude Haiku 5.5: A Small Model With 1M Context Priced
  at $0.10 per Million Input Tokens'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/07/anthropic-releases-claude-haiku-5-5-a-small-model-with-1m-context-priced-at-0-10-per-million-input-tokens/
model: claude-code/sonnet
generated_at: '2026-10-08T22:21:21.251540'
score: 92
---

📌 Haiku 5.5 定價拆解：百萬 token 入門價砍到 1 折

TL;DR：Claude Haiku 5.5 百萬輸入 token 僅 $0.10，但換 tokenizer 後實際省幅要重新算。

官方標價寫著「降價 90%」，但這句話只對一部分請求成立。MarkTechPost 的報導把 Claude Haiku 5.5 的定價規則、部署管道與效能數字拆得更細，值得工程團隊對照自己的流量結構重新算一次成本。

🤔 **定位：高流量場景的執行模型**

Anthropic 釋出 Claude Haiku 5.5，官方定位是目前最便宜、最快的小模型，主打摘要、上下文壓縮（compaction）、分類與子智慧體任務。模型維持 1M token 的上下文視窗，輸出上限則到 128K token，支援文字與圖片輸入、輸出文字，知識截止日期為 2026 年 6 月。目前已在 Claude API、Amazon Bedrock、Google Cloud、Microsoft Foundry 以及 Claude Platform on AWS 全面上線，批次（batch）作業在 beta 階段支援最多 300K 輸出 token。

🧩 **effort 參數下放，但取樣參數被鎖死**

Haiku 5.5 是首個支援 effort 調節的 Haiku 模型，自適應思考預設開啟，effort 參數預設為 medium。報導特別提醒兩個容易踩雷的地方：非預設的 temperature、top_p 或 top_k 數值會直接回傳 400 錯誤；新的 tokenizer 對同樣文字的計數，大約比 Haiku 4.5 多出 30%。這兩點都已寫進官方遷移指南。

📊 **定價門檻設在 10 萬 token**

定價以 10 萬 token 為分界：10 萬 token 以內，輸入每百萬 token $0.10、輸出 $0.50，快取讀取 $0.01、5 分鐘快取寫入 $0.125；超過 10 萬 token，輸入升到 $0.50、輸出升到 $2.50。相較之下，Haiku 4.5 的價格是輸入 $1、輸出 $5。Anthropic 表示大約 90% 的 Haiku 4.5 請求落在 10 萬 token 以內，考慮新 tokenizer 的膨脹效果後，估計 Haiku 5.5 平均成本約便宜 75%，批次處理再額外省 50%。

報導也做了跨模型比價：GPT-6 Luna 在短上下文的定價與 Haiku 5.5 完全相同，但它的高價門檻要到 272K input token 以上才啟動（$0.20 輸入／$0.75 輸出）。換算下來，若提示詞落在 150K token 這種中段區間，GPT-6 Luna 的標價反而更便宜，說明定價門檻的位置差異會直接影響實際帳單，不能只看起步價。

💡 **Sonnet 5.5 仍是效能天花板**

在報導引用的系統卡數據中，Sonnet 5.5 在所有項目都領先，包括 Terminal-Bench 4.0 的 70.6%。Anthropic 自己也建議複雜 agentic 編碼任務優先選用 Sonnet 5.5 或 Opus 5.5，這再次印證 Haiku 5.5 的定位是高流量、低複雜度的執行型任務，而非全面取代中高階模型。

⚠️ **比價不能只看起步價**

這篇報導最實用的地方，是把「10 萬 token 分界」「272K token 分界」這類門檻數字並列呈現，提醒工程團隊在不同廠商之間比價時，必須對照自己實際的提示詞長度分佈，單看起步價格很容易得出錯誤結論。

🎯 **實務啟示**

升級或選型前，先統計自家請求的 token 長度分佈，看落在哪個定價區間；若提示詞經常超過 10 萬 token，Haiku 5.5 的降價幅度會被稀釋，甚至不如 GPT-6 Luna 的中段定價。同時務必檢查呼叫程式碼是否使用了非預設的 temperature／top_p／top_k，升級前先過一輪遷移指南可以省下不少除錯時間。

🔗 **來源**
- 標題：Anthropic Releases Claude Haiku 5.5: A Small Model With 1M Context Priced at $0.10 per Million Input Tokens
- 作者／機構：Michal Sutter（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/10/07/anthropic-releases-claude-haiku-5-5-a-small-model-with-1m-context-priced-at-0-10-per-million-input-tokens/

#ClaudeHaiku #Anthropic #LLMPricing #AmazonBedrock #GoogleCloud #AIInfrastructure #ContextWindow #AICostOptimization #APIPricing #CloudAI
