---
title: The current balance of power in open models
source: Interconnects
url: https://www.interconnects.ai/p/the-current-balance-of-power-in-open
model: claude-code/sonnet
generated_at: '2026-09-21T21:16:39.319553'
score: 95
---

📌 開源模型的地緣政治現況：中國已經領先多久了？

TL;DR：Interconnects 作者向美國國會簡報指出，中國開源模型下載量已是美國兩倍，且下游能力差距仍在拉開。

當國會議員與幕僚想了解「美中開源模型競爭到底誰在贏」，答案不是一句模糊的「差不多」，而是一組具體到月份的落後時間表。Interconnects 作者 Nathan Lambert 最近受邀向美國國會議員與幕僚簡報開源權重模型現況，這篇文章是他公開分享的簡報內容整理。

🤔 **先搞清楚「開源」在講什麼**

開放語言模型指的是權重可公開檢視或下游使用的 AI 模型，常被拿來與僅透過 API 或產品（如 ChatGPT、Claude Code）存取的「封閉」模型對比。開放模型主要分兩類：open-weight（如 Meta 的 Llama、Alibaba 的 Qwen、Google 的 Gemma、DeepSeek 的模型），這類模型有授權條款規範下游用途，通常搭配 Transformers、vLLM、SGLang 等推論函式庫；真正的 open-source 模型則除了權重、授權、推論程式碼之外，還會釋出訓練程式碼與訓練資料，近期最具代表性的是 Allen Institute for AI 的 Olmo 系列（Lambert本人曾在該機構參與建構 2.5 年）、OpenAthena 的 Marin，以及 EleutherAI 的 Pythia，這些都由美國的非營利組織主導。開放程度其實是一道光譜：Nvidia 的 Nemotron 系列釋出大量訓練資料，開放度遠高於一般 open-weight 模型，卻仍稱不上完全 open-source，因為並未釋出全部資料。

🧩 **下載量：中國總量已是美國兩倍**

美國曾是開放語言模型的早期領先者，主要靠 Meta 的 Llama 系列在研究與商業場景被廣泛使用。但大約 18 個月前，中國的 open-weight 模型在這兩個關鍵面向上超車美國。最簡單的量化指標是 Hugging Face 下載量：中國自 2025 年 7 月起靠 Alibaba Qwen 系列的成功取得領先。Lambert 自己維護追蹤工具，自他 2025 年 8 月發布 American Truly Open Models（ATOM）Project 以來，中國的下載量領先幅度已擴大到約 16 億，總下載量來到 32 億，是美國總量的兩倍。

📊 **能力榜單：GLM-5.3、Kimi K3 站上前段班**

在 Artificial Analysis Intelligence Index（AAII）這類熱門能力 benchmark 上，中國的 open-weight 模型明顯領先美國同類產品。截至 2026 年 9 月 14 日，排名前三的中國模型是 Z.ai 的 GLM-5.3（45 分）、GLM-5.3-Flash（42 分）與 Moonshot AI 的 Kimi K3（44 分）；相比之下，美國領先的模型是 Thinking Machines 的 Inkling 與 Inkling Small（皆為 26 分），以及 Nvidia Nemotron 3 Ultra（23 分）。這幾個美國模型分別在 2026 年 6 月、7 月發布，更新頻率也低於中國對手；中國實驗室拿到超越這些美國模型的分數，往往早了 2 到 6 個月（例如 GLM-5 或 DeepSeek V4 Pro）。雖然 Arcee AI、Poolside、IBM 等更多美國公司開始釋出模型，但整體並未快速拉近差距。

💡 **差距到底有多大，又是怎麼形成的**

整體而言，中國的 open-weight 模型大約落後美國封閉前沿模型 2 到 5 個月，而美國自己的 open-weight 模型則落後 OpenAI、Anthropic 這類封閉前沿約 6 到 9 個月。中國實驗室在使用者需求明確的任務（如 agentic coding）上追得最緊，在更開放式的科學任務（如物理、生物）上則落後較多。

文章指出，中國實驗室能以較少資源做出強模型，原因仍有爭議，受不同工作文化影響很大，但也有幾個技術因素：釋出速度更快、任務分布相對較窄，這讓他們在公開 benchmark 上略微佔優——因為所有實驗室都在持續進步，誰的模型「完工」時間點較晚，分數自然較高。即便如此，作者強調這些模型是真材實料的競爭者，不是靠榜單取巧。這種競爭態勢不會因為封閉實驗室修補蒸餾（distillation）漏洞而顯著縮小：作者估計，就算完全阻止蒸餾（例如 Anthropic、OpenAI 導入 KYC 工具），美國最強模型與中國 open-weight 模型的差距也只會多拉開 1 到 2 個月。值得留意的是，中國實驗室在 2026 年對訓練資料的態度也在轉變：年初 Moonshot AI、Z.ai 等頂尖團隊偏好自建資料流程，但到了夏天，他們已開始向美國老牌公司與中國新創購買高難度的 agentic 任務 RL 環境資料。

⚠️ **開放帶來的風險難以單靠限制解決**

隨著中國 open-weight 模型逼近前沿，加上網路安全等領域的前沿模型風險文件持續增加（例如 OpenAI-HuggingFace 事件），監管上的不確定性也在成長。文章指出一個結構性難題：幾乎沒有有效方法能阻止開放軟體流向惡意行為者；如果嘗試限制中國最強 open-weight 模型的取得管道，反而會先傷到依賴這些模型的美國企業。作者舉例，HuggingFace 之所以能理解某次網路攻擊，正是因為用了一款中國 open-weight 模型，而封閉模型當時拒絕回答相關請求。因此，管理 open-weight 模型風險的關鍵其實在於「生態系整備」，而不是單純限制存取。

🎯 **實務啟示**

對於依賴開放模型做產品的團隊，這篇分析的現實意義在於：中國 open-weight 模型在下載量和多數能力榜單上已經領先，且釋出節奏更快，這代表評估開源選型時，不能只盯著美國陣營；同時也要留意授權與資料來源的差異——open-weight 不等於 open-source，兩者在可稽核性與合規風險上差異很大，尤其在監管不確定性升高的當下，選型前把這些光譜位置摸清楚會更重要。

🔗 **來源**
- 標題：The current balance of power in open models
- 作者／機構：Nathan Lambert, Interconnects
- 連結：https://www.interconnects.ai/p/the-current-balance-of-power-in-open

#OpenWeightModels #OpenSourceAI #LLM #Qwen #GLM #KimiK3 #Llama #AIGeopolitics #ATOMProject #AIPolicy
