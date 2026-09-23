---
title: 'OpenAI Releases GPT-6 Sol and Luna: 50% Cheaper API Pricing and Benchmarks'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/22/openai-releases-gpt-6-sol-and-luna-50-cheaper-api-pricing-and-benchmarks/
model: claude-code/sonnet
generated_at: '2026-09-23T20:41:04.713807'
score: 85
---

📌 【OpenAI】GPT-6 Sol、Luna 上線：價格砍半，部分項目打贏 Opus 5

TL;DR：GPT-6 Sol 與 Luna API 價格較 GPT-5.6 促銷價降 50%，多項 benchmark 顯示成本效益大幅優於 Claude 對手。

一個模型分數贏過對手，但成本只要對方的十分之一，這樣的組合才是企業真正在意的東西。OpenAI 這次發布的 GPT-6 Sol 與 Luna，主打的不是「更聰明」，而是「用更少的錢做到接近，甚至超越的表現」。

🤔 GPT-6 家族補齊中低階產品線

繼本月稍早發布頂規模型 GPT-6 Astra 之後，OpenAI 再推出 Sol 與 Luna 兩款定位在 Astra 之下的模型。三者訓練方式類似，目標是把 Astra 的進展帶進更快、更平價的版本。目前 GPT-6 家族分為三層：Astra 負責最困難的任務；Sol 鎖定複雜的程式開發與專業工作，成本較低；Luna 則主打快速、高流量的日常任務。兩款模型皆已在 OpenAI API 中上線（gpt-6-sol、gpt-6-luna），僅提供 API 存取，不釋出權重供自行部署。

🧩 更好的快取與推論效率支撐降價

OpenAI 表示，更好的 caching 與推論技術讓這兩款模型能以更低成本服務，因此將 Sol 與 Luna 的 API 定價相較 GPT-5.6 促銷價下砍 50%。值得注意的是 Luna 的輸出價格從每百萬 token $1.20 降至 $0.50，實際降幅約 58%，比官方宣稱的 50% 更多。

📊 跨多項 benchmark 的成本效益比較

| Benchmark | 模型（Effort） | 分數 | 成本備註 |
|---|---|---|---|
| AutomationBench 1.0.6 | GPT-6 Sol（xhigh） | 33.2% | $0.27／task |
| AutomationBench 1.0.6 | Claude Opus 5（max） | 26.9% | 11.1 倍 Sol 成本 |
| AutomationBench 1.0.6 | GPT-6 Astra（low） | 30.3% | 3.9 倍 Sol 成本 |
| Agents' Last Exam | GPT-6 Sol（max） | 56.4% | 較 Claude Opus 5 最佳成績低 60% 成本 |
| DeepSWE v1.1 | GPT-6 Sol（max） | 68.8% | 較 Claude Fable 5（xhigh）低 1.1 分，成本低約 80% |
| DeepSWE v1.1 | GPT-6 Luna（max） | 66.6% | 與 Opus 5、Fable 5（medium）相當，成本分別低 93%／96% |
| OSWorld 2.0（offline） | GPT-6 Sol（xhigh） | 60.5% | 對比 Opus 5（medium）60.3%，成本低約 80% |

此外，Luna 在 high effort 下較前代提升 5.4 分，成本卻降低 58%；在 FrontierCode 1.1 Main（評估程式碼是否可直接合併）上，Sol 的表現追平 Claude Fable 5.1（xhigh），但成本明顯更低。Luna 在 max effort 下也能以十分之一的成本打贏 GPT-5.6 Sol（medium）於 OSWorld 2.0 的表現。

📊 事實準確度與溝通風格也有進展

在 OpenAI 使用去識別化 ChatGPT 對話（使用者標記錯誤）所做的內部測試中，Sol 犯錯機率約為前代的一半；Luna 在較高 effort 下，準確度可與 GPT-5.6 Sol 打平，成本卻只要約百分之一。OpenAI 也將 Astra 的溝通風格延續到 Sol 與 Luna，回答預期更清楚、稍短、少術語，尤其在程式相關對話中更明顯。

🧩 更聰明的 prompt caching 同步上線

配合這次發布，GPT-6 也預設提供更高快取命中率的 prompt caching 系統，命中快取的輸入最高可折扣 90%，且在 30 分鐘視窗內重複使用的共用前綴（shared prefix）也符合資格。根據報導，GitHub 表示這項改動讓需要重新處理的 prompt token 比例減少超過 50%，有助於 Copilot 更快回應。

🎯 實務啟示

如果你的應用場景是高流量、對延遲敏感的任務（如客服、程式輔助），Luna 的成本效益值得優先評估；若需要更強的推理與 agentic 能力但仍要控制成本，Sol 在多項 benchmark 上展現出比 Claude Opus 5 更划算的表現。導入前建議針對自己的任務跑一輪基準測試，畢竟公開 benchmark 分數未必完全反映實際工作負載。

🔗 來源
- 標題：OpenAI Releases GPT-6 Sol and Luna: 50% Cheaper API Pricing and Benchmarks
- 作者／機構：Sana Hassan／MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/22/openai-releases-gpt-6-sol-and-luna-50-cheaper-api-pricing-and-benchmarks/

#GPT6 #OpenAI #LLMBenchmark #AIÐPricing #ClaudeOpus #AgenticAI #CodingAssistant #APIeconomics #MachineLearning #LLMOps
