---
title: '[AINews] Claude Haiku 5.5 — better than GPT-6 Luna at the same pricing'
source: Latent Space
url: https://www.latent.space/p/ainews-claude-haiku-55-better-than
model: claude-code/sonnet
generated_at: '2026-10-08T22:29:15.595612'
score: 78
---

📌 Claude Haiku 5.5 開賣：同價位打到 GPT-6 Luna？

TL;DR：Anthropic 推出降價約 75% 的 Haiku 5.5，多項第三方 benchmark 顯示它領先同價位的 GPT-6 Luna。

Haiku 這個產品線已經快一年沒更新，眼看 Sonnet、Opus、Fable 都衝到 5.5 版，連 OpenAI 都已經推出 GPT-6 Luna，外界幾乎要把它遺忘——結果這次更新來得既便宜又兇。

🤔 時隔一年的小模型更新

Anthropic 上週出貨 Claude Haiku 5.5，是 Haiku 系列自 2025 年 10 月 15 日 Haiku 4.5 發布以來，約一年內的第一次更新。官方將其定價對齊 OpenAI 的 GPT-6 Luna，同一天還調降了 Sonnet 5.5 與訂閱方案的價格。Anthropic 形容它是「目前為止最便宜、最快、也最強的小模型」，平均執行成本比 Haiku 4.5 低約 75%。目前已在 Claude Platform 與 Claude Code 上線，官方將它定位為搭配 Opus 5.5 或 Sonnet 5.5 使用的 subagent，專門處理摘要、context 壓縮、資料庫查詢等高用量、成本敏感的工作。Anthropic 員工 @mikeyk 的說法很貼切：「Opus 負責重度思考，Haiku 負責高用量的工作。」

🧩 分級定價與同日配套更新

Haiku 5.5 採用依 prompt 長度分級的定價：

| 輸入長度 | Input / Output（每 1M tokens） | Cache 讀取（每 1M tokens） |
|---|---|---|
| 100K tokens 以下 | $0.10 / $0.50 | $0.01 |
| 100K tokens 以上 | $0.50 / $2.50 | $0.05 |

同一天，Sonnet 5.5 的 cache 讀取價格也從每 1M tokens $0.20 砍半到 $0.10，Anthropic 表示這讓 Sonnet 5.5 在多數長任務或 agentic 工作上便宜約 20%。訂閱方案（Max 5x、Max 20x、Team）也新增可跨任意模型使用的 API 額度，分別最高 $100、$200、至多 $500（Team 為共用額度）。同日，Python 與 TypeScript 的 Claude SDK 也內建了 computer-use 與 browser-use 工具集，可直接串接 browser_use、Browserbase、E2B、Daytona 等 driver，開發者不再需要自己寫這段 action loop。

📊 第三方 benchmark 怎麼說

根據 Artificial Analysis 的測試，Haiku 5.5 的 Intelligence Index（max effort）為 43 分，比前一代 Haiku 進步 26 分：

| 模型 | Intelligence Index（max effort） |
|---|---|
| Sonnet 5.5 | 56 |
| Kimi K3（2.8T 參數開源模型） | 44 |
| Haiku 5.5 | 43 |
| GLM-5.3 Flash | 42 |
| Gemini 3.8 Flash | 41 |
| GPT-6 Luna | 38 |

在知識準確率與幻覺率方面（AA-Omniscience）：

| 模型 | 準確率 | 幻覺率 |
|---|---|---|
| Gemini 3.8 Flash | 55% | 55% |
| GPT-6 Luna | 44% | 77% |
| Haiku 5.5 | 36% | 40% |

Haiku 5.5 的準確率較低，但幻覺率也明顯更低，部分原因是它更願意承認「不知道」。其他數據包括：Terminal-Bench 4.0 從 Haiku 4.5 的 0% 升到 33%（領先 Gemini 3.8 Flash 的 20% 與 GPT-6 Luna 的 13%）；AA-Briefcase（私有 agentic 知識工作評測）拿下 1578 Elo，領先 Kimi K3 與 GLM-5.3；context 視窗從 20 萬 tokens 擴大到 100 萬 tokens。Anthropic 自行公布的數字則是 OSWorld 從 15% 提升到 72%、TerminalBench 從 0% 提升到 39%（與 Artificial Analysis 獨立測出的 33% 有差異）。

💡 便宜,但不是「無腦便宜」

Artificial Analysis 的數據點出一個重要但容易被忽略的細節：Haiku 5.5 在 max effort 下平均每個任務要用掉約 16.2 萬個 output tokens，大約是 GPT-6 Luna 在其 max 設定下（約 5 萬 tokens）的三倍。在效果相同的情況下比較，Haiku 5.5 用 high effort 跑出 38 分要花約 5.5 萬 tokens，而 Luna 用 max 設定跑出同樣 38 分只要約 5 萬 tokens——換言之，Haiku 5.5 的「便宜」有一部分會被它更高的 token 用量抵銷，這也是為什麼 Cursor 宣稱短請求下便宜十倍、而 Anthropic 官方宣稱平均便宜 75% 會出現落差。另外，超過 10 萬 tokens 的長 prompt 會被收取 5 倍價格，這對長 context 的 agent 迴圈來說是個需要事先盤算的成本因素。

⚠️ 已知的限制

AutomationBench-AA 上 Haiku 5.5 僅拿到 35%，落後 Luna、Gemini 3.8 Flash、GLM-5.3 Flash 的 53% 至 60%；Anthropic 表示這是因為一個發布前的安全性 bug 導致模型過度拒絕回答，目前正在修復中，Artificial Analysis 預計分數之後會回升。此外，Haiku 5.5 在事實知識回憶上仍弱於 Gemini 3.8 Flash 與 GPT-6 Luna。

🎯 實務啟示

如果你的應用場景是高頻、低延遲、成本敏感的子任務（摘要、資料庫查詢、context 壓縮），Haiku 5.5 搭配 Opus/Sonnet 的分層架構值得一試；但若任務需要長 prompt 或要求 max effort 才能達標，務必實際算一遍 token 用量成本，不要只看官方宣稱的降價幅度。

🔗 來源
- 標題：[AINews] Claude Haiku 5.5 — better than GPT-6 Luna at the same pricing
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-claude-haiku-55-better-than

#ClaudeHaiku #Anthropic #LLM #GPT6Luna #AIpricing #Benchmark #AgenticAI #ClaudeCode #SmallModels #AIInfra
