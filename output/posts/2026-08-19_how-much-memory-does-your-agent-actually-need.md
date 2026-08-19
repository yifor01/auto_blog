---
title: How Much Memory Does Your Agent Actually Need?
source: HuggingFace Blog
url: https://huggingface.co/blog/ibm-research/altk-evolve-hmm
model: claude-code/sonnet
generated_at: '2026-08-19T06:34:12.122240'
score: 92
---

📌 【IBM Research】AI Agent 的記憶該給多少？8 個模型實測給答案

TL;DR：IBM 實測 8 個模型證明，agent 記憶不是開關，是要依模型校準的劑量。

「餵給 agent 更多過去經驗，效能應該更好」——這個直覺在 IBM Research 最新測試中被打臉：同一套自我萃取出來的 guideline，塞給不同模型會有完全不同的結果，有的模型突飛猛進，有的完全沒反應。

🤔 **記憶該怎麼給，比有沒有記憶更重要**

前一篇文章比較了 ALTK-Evolve 與 ACE，發現「怎麼餵 guideline」（每個任務只檢索幾條 vs. 整套塞進去）會同時影響準確率與成本。這篇文章退一步問更根本的問題：到底該給 agent 多少記憶？

🧩 **三種 context 配置，同一套 guideline**

ALTK-Evolve 讓 agent 從自己過去的 trajectory 中學習：萃取出可重複使用的 guideline，在 inference 時注入回 context，全程不更新模型權重、不需要人工標註。研究比較三種配置，guideline 集合來自同一次萃取（只用 AppWorld 訓練資料，測試集完全沒有進入這個萃取過程）：

- Baseline：沒有任何記憶，agent 照出廠設定跑。
- Full guideline set：把萃取出的每一條 guideline，每個 ReAct step 都注入。
- Curated retrieval：一組固定的高信心核心 guideline，加上依任務檢索出來的少量相關 guideline。

評測用 AppWorld benchmark：585 個多步驟任務（168 個 test_normal + 417 個 test_challenge），涵蓋 9 款模擬 app（日曆、訊息、支付等）。評分用兩種指標：TGC（Task Goal Completion，任務是否完整達成）與 SGC（Scenario Goal Completion，情境的每個變體是否都通過，門檻更嚴格）。

📊 **三種模式，劑量各不相同**

橫跨 8 個模型（從 30B dense 模型到前沿專有系統）的測試，浮現三種規律：

| 模型 | 型態 | Baseline TGC/SGC | 最佳記憶設定 TGC/SGC | 最佳配置 | ΔTGC | ΔSGC |
|---|---|---|---|---|---|---|
| gpt-oss-120b (117B MoE) | 較弱／需精選 | 39.9 / 21.4 | 56.0 / 37.5 | curated retrieval | +16.1 | +16.1 |
| DeepSeek-V3.2 (671B MoE) | 強、有餘裕 | 79.8 / 64.3 | 89.3 / 80.4 | full guideline set | +9.5 | +16.1 |
| Claude Opus 4.6 | 強、有餘裕 | 90.5 / 87.5 | 94.6 / 94.6 | full guideline set | +4.1 | +7.1 |
| GPT-5.5 | 強（接近天花板） | 92.3 / 82.1 | 95.2 / 89.3 | full guideline set | +2.9 | +7.2 |
| GLM-5 (745B MoE) | 飽和 | 87.5 / 80.4 | 87.5 / 80.4 | full guideline set | 0.0 | 0.0 |

有餘裕的強模型（如 DeepSeek-V3.2）能吃下整套 guideline，連罕見的邊緣案例都用得上；較弱的模型（如 gpt-oss-120b）給太多反而被「淹沒」，用精選核心加檢索表現更好；已接近天花板的模型（如 GLM-5）則完全沒有反應，研究團隊把這稱為「飽和模式」，並強調這只是觀察到的現象標籤，不代表已證實的成因：可能模型本來就已逼近該任務上限，也可能 guideline 沒對到它真正的失敗點，或它沒能有效套用 guideline。

值得注意的是，SGC（更嚴格的指標）漲幅往往比 TGC 更大——DeepSeek 的 SGC 漲了 16.1pp，TGC 只漲 9.5pp，因為好的 guideline 特別能幫助 agent 把一個情境的每個變體都做對，而不只是平均表現。即使是已接近上限的 GPT-5.5 與 Opus，SGC 依然分別多拿 7.2 與 7.1pp，代表只要模型還有殘餘的失敗模式，記憶就還有用。

💡 **最便宜的策略，可能同時是最好的策略**

把整套 guideline 每一步都塞進 context，會讓 token 用量大幅膨脹。實測結果：

| 模型 | 設定 | Baseline tokens/task | 加記憶後 | 增幅 |
|---|---|---|---|---|
| DeepSeek-V3.2 | full guideline set | 148K | 263K | +78% |
| gpt-oss-120b | full guideline set | 110K | 166K | +51% |
| gpt-oss-120b | curated retrieval | 110K | 116K | +5% |

對 gpt-oss-120b 來說，curated retrieval 不只效果最好（+16.1pp TGC），token 增幅還只要 +5%，遠比 full guideline set 划算。文章也提到，prompt caching 能讓即使是 full guideline set 的方案在正式環境中仍然負擔得起。

⚠️ **飽和模式的成因還沒釐清**

「飽和模式」背後的成因，團隊自己也承認還沒完全釐清：是 benchmark 的天花板高度、context window 大小、guideline 品質，還是任務分布造成的，目前仍在拆解中，並非單純看參數量就能預測。

🎯 **實務啟示**

幫 agent 做記憶系統時，不要預設「guideline 越多越好」。先確認你的模型是「有餘裕」還是「容易被雜訊淹沒」的類型：強模型可以考慮全量注入，較弱或成本敏感的場景優先做 curated retrieval，這往往是準確率與成本的雙贏解，而不是效能打折換便宜。

🔗 **來源**
- 標題：How Much Memory Does Your Agent Actually Need?
- 作者／機構：IBM Research（Vatche Isahagian、Gaodan Fang、Jayaram Radhakrishnan、Punleuk Oum、Ashwath Vaithinathan Aravindan、Evelyn Duesterwald、G Thomas、Vinod Muthusamy、Merve Unuvar、Ayhan Sebin）
- 連結：https://huggingface.co/blog/ibm-research/altk-evolve-hmm

#AgenticAI #LLMAgents #AppWorld #IBMResearch #HuggingFace #PromptEngineering #AIMemory #DeepSeek #GPTOSS #TokenEfficiency
