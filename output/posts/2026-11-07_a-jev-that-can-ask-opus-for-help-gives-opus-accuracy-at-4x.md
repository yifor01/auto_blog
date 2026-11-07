---
title: A Jev that can ask Opus for help gives Opus accuracy at 4x lower cost
source: Hacker News
url: https://hightouch.com/blog/llm-judges-identity-resolution
model: claude-code/sonnet
generated_at: '2026-11-07T21:03:11.317433'
score: 84
---

📌 Jev + Opus 混合判官：身分解析準確率打平前沿模型，成本砍 4 倍以上

TL;DR：用便宜的決策模型 Jev 先篩、交由 Claude Opus 複判疑難案例，準確率逼近前沿模型，成本省逾 4 倍。

人工抽查身分解析（identity resolution，IDR）結果有多慢？一個人一小時大約只能看 50 筆，要把過度合併（over-merging）率的誤差壓到正負 1% 以內，得抽超過 1000 個樣本。這篇來自 Hightouch 的部落格文章做了一個實驗：如果讓 LLM 當這個判官，能不能又快又準？

🤔 **身分解析最怕「過度合併」，但沒有答案可對**

IDR 的任務是把一堆資料記錄 D 對應到一組真實身分 I，確保每個身分只對應一個真人。現實資料充滿 typo、同音誤寫（Phillips → Filips）、暱稱（Robert → Bob）、甚至欄位空白，最常見也最麻煩的錯誤是「過度合併」：把兩個不同的人誤判成同一人。問題是，真實資料沒有答案key可以對照——如果有，就不需要做 IDR 了。這讓團隊只能靠人工抽樣評估準確度，而且樣本量要求極高才能估出可信的誤差率。

🧩 **用模擬小鎮資料造 1000 個身分，一半正常一半刻意過度合併**

團隊用 pseudopeople（華盛頓大學健康指標與評估研究所的工具）模擬一個虛構美國小鎮，從 2020 到 2040 年間產生戶政普查、家戶調查、WIC 福利計畫、社會安全局、W-2 和 1040 報稅等多來源記錄，並加入大量真實型態的資料錯誤，組出 1000 個身分，一半是單一人的噪聲記錄，一半是刻意製造的過度合併。

Prompt 設計分三層疊加：先給基本審核指令，再列出各種資料錯誤類型範例（typo、月日對調、暱稱等），最後補上資料來源的背景說明。結果發現，加入錯誤範例對所有模型的提升最大；而補充資料來源背景，對前沿模型最多只加一分，對決策模型（Jev、Luna）幾乎沒用——團隊的解讀是，決策模型本質上不太做推理，給它再多背景也吃不進去。

📊 **五個模型的準確率、成本與速度對照**

在 50% 信心門檻下的結果：

| 模型 | 準確率 | False Positive | False Negative | 每筆耗時 | 每千筆成本 |
|---|---|---|---|---|---|
| Claude Opus 5.5 | 99.0% | 3 | 7 | 2.2s | $3.86 |
| Gemini 3.1 Pro | 98.3% | 10 | 7 | 4.2s | $4.48 |
| GPT-6 Sol | 98.3% | 14 | 3 | 2.1s | $2.50 |
| GPT-6 Luna（Decisions API，50% cutoff） | 97.3% | 17 | 10 | 0.17s | $0.10 |
| Jev（50% cutoff） | 95.6% | 31 | 13 | 0.15s | $0.05 |

決策模型 Jev 和 Luna 出廠即有 88.8%~97.3% 的準確率，比前沿模型最多便宜 90 倍、快 10 倍以上，但在較難的 benchmark 上仍落後 Opus 約 6 個百分點。團隊接著把信心門檻從 50% 調整到 Jev 60%、Luna 70%，各自在自己的最佳門檻上拿到最高準確率。

💡 **關鍵不是準確率，是「知不知道自己可能錯」**

真正讓混合模型奏效的,是兩個決策模型犯錯的方式不同：Jev 的信心校準較好，它的錯誤大多發生在「低信心」的時候；Luna 則相反，犯錯時往往自信滿滿。這代表 Jev 能準確標記「我不確定」的疑難案例，把這些案例轉交給 Opus 複判，而不需要的案例就留在便宜的 Jev 身上處理。這種「Jev 篩選 + Opus 複判」的混合架構，最終達到接近前沿模型的準確率，但成本降到 4 倍以下。

⚠️ **決策模型仍有上限，門檻調校也不是一次到位**

即便校準門檻後，決策模型在困難樣本上仍比不上 Opus，前沿模型目前還是準確率天花板；信心門檻對 Jev 影響很大、對 Luna 影響很小，代表每個模型都需要分別調校，不能套用同一套閾值。

🎯 **實務啟示：把信心分數當作路由開關**

對要大量跑 LLM-as-judge 的團隊,這個案例示範了一個可複製的架構：先用快又便宜的決策模型過一輪，依信心分數做門檻切分，低信心的案例才升級給前沿模型複判。這樣既能把百萬級樣本的評估時間從數週壓縮到幾秒，又不必為每一筆都付前沿模型的價錢。

🔗 **來源**
- 標題：A Jev that can ask Opus for help gives Opus accuracy at 4x lower cost
- 作者／機構：theanomaly（Hightouch Blog）
- 連結：https://hightouch.com/blog/llm-judges-identity-resolution

#LLM #AIJudge #IdentityResolution #PromptEngineering #ModelRouting #ClaudeOpus #CostOptimization #MachineLearning #DataQuality #AIEngineering
