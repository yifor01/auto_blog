---
title: 'Claude Mythos 5.1 and Fable 5.1: Capabilities'
source: Don't Worry About the Vase
url: https://thezvi.wordpress.com/2026/09/05/claude-mythos-5-1-and-fable-5-1-capabilities/
model: claude-code/sonnet
generated_at: '2026-09-06T19:20:22.401233'
score: 77
---

📌 Anthropic 發布 Fable 5.1：分數小漲，真正大招是降價與鬆綁分類器

TL;DR：Fable 5.1 基準測試小幅進步，但降價 25~45%、分類器誤攔減六成才是重點。

這是一個很奇怪的時間點寫模型評測：同一週，Anthropic 和 OpenAI 都在說自己推出了「全球最強模型」。Claude Fable 5.1 和 GPT-6 Astra 幾乎前後腳登場，兩邊都各自宣稱奪冠，讀者只能自己判斷。

🤔 **同週雙雄，但缺乏直接對照**

根據 TheZvi 的整理，Fable 5.1 是在 Astra 發布前上線的，因此本篇評測絕大部分只能單獨看 Fable 5.1，還無法拿它跟 Astra 做逐項比較。少數幾次同題測試中，兩者答案風格不同但都相當出色，TheZvi 表示接下來會「雙持」（同時詢問兩個模型），並打算之後另外寫一篇完整的 Astra 評測。值得注意的是，他的主觀印象是「從上一代到 Astra 的跳躍」感覺比「Fable 5 到 Fable 5.1」更大更興奮，這與過去從 Opus 世代跳到 Fable 世代時的觀感類似。Anthropic Claude Code 創辦人 Boris Cherny 則表示，Fable 5.1 是他們目前在寫程式、資料分析、電腦操作、簡報設計乃至最困難的長時間 agentic 任務上表現最好的模型，他個人已經全面改用。

📊 **基準測試小幅進步，部分項目不進反退**

Anthropic 公布了大量基準數據，多數相對 Fable 5／Opus 5 呈現「小幅進步，沒有明顯規律」：

| 基準測試 | 前代（Fable 5／Opus 5） | Fable 5.1 |
|---|---|---|
| FrontierSWE v2 | 0.52（Opus 5）／0.48（Fable 5） | 0.57 |
| Terminal-Bench-Science 0.1 | 24.7% | 52.6% |
| CursorBench 3.2（封頂分數） | 70.5% | 73.4% |
| CritPT-Corrected | 85.5% | 88.4% |
| ArXivMath（無工具／有工具） | 91%／91% | 91%／94% |
| ProgramBench | 86.3% | 87.6% |
| Humanity's Last Exam（無工具／有工具） | 57.8%／63.8% | 60.9%／65% |
| Chartography | 37%／84% | 43%／86% |
| BenchCAD Vision2Code | 38%／67% | 44%／84% |
| OSWorld 2.0（partial／strict） | 75%／39% | 78%／42% |

另外，DeepSWE v1.1 得分 67.4%（五次試驗平均），但缺乏對照基準；Legal Agent Benchmark（Harvey AI 提供）在最高 effort 下全通過率為 19.1%，平均條件通過率 90.8%，在額外的 held-out 測試集上分別為 16.7% 與 93.3%。

💰 **降價才是這次真正的重頭戲**

Fable 5.1 的標價與 Fable 5 相同，但 cache read 價格從每百萬 token $1 降到 $0.25，Anthropic 表示這會讓一般用量成本降低約 25%，高度 agentic 的工作最多可降約 45%；Boris Cherny 則說一般 Claude Code 使用情境可省下 38% 的費用。OpenRouter 上列出的 Fable 5.1 定價為輸入每百萬 token $10、輸出 $50。同時，Anthropic 也大幅調整了分類器：生物安全防護對「無害請求」的誤攔次數比 Fable 5 上市時減少 85%，Claude Code 使用者每個 session 遇到的資安誤攔次數約減少 60%，分類器整體誤判率至少降低 60%。他們也表示未來會推出讓「符合資格的客戶」透過自行保存資料來達成零資料保留（zero data retention）的新機制，在此之前，仍先對部分客戶提供完整的零資料保留方案。

💡 **11% 採用率能不能翻身，是接下來的觀察指標**

文中提到一個關鍵背景數字：儘管公認是市面上最好的模型，Fable 5 在企業支出平臺 Ramp 上的 Anthropic 相關花費佔比從未超過約 11%。兩大障礙分別是分類器誤攔範圍過廣、干擾正常工作，以及不少企業因法規考量無法接受 Anthropic 原本要求保留 30 天紀錄的資料政策；反倒是個人開發者，因為不受這些限制影響，能拿到明顯的程式撰寫優勢。這次 Fable 5.1 同時降價、鬆綁分類器、佈局零資料保留，等於是一次自然實驗：如果採用率仍然遠低於 11%，那就代表市場真的只是單純被標價嚇跑，而沒有細算實際成本。

⚠️ **一些留意事項**

FrontierCode 1.1 Extended 在較高 effort 等級下分數反而變差，Anthropic 將原因歸咎於模型在高 effort 下停不下來、持續做「額外的有幫助的修改」，結果被判為錯誤；這某種程度上也呼應了「Fable 5.1 很愛主動做事」的普遍回饋——如果給它高 effort，它一定會找事做，但不見得每次都是你要的。多個 multi-agent 測試也缺乏可比較的基準，難以判斷實際強弱。GDP.pdf 這項測試也出現「用工具反而分數持平或略降」的反常現象。

🎯 **給工程團隊的實務啟示**

如果你原本因為分類器太敏感或無法接受 30 天資料保留政策而放棄 Claude，Fable 5.1 的鬆綁與即將推出的零資料保留機制值得重新評估；cache read 降價對重度使用 Claude Code 或長 agentic 流程的團隊是實打實的成本下降。但在對比 GPT-6 Astra 之前，不要單憑任何一方釋出的基準測試下定論，兩者目前都缺乏正式的頭對頭比較，實務上不妨像 TheZvi 建議的那樣，把兩個模型都跑一輪再自行判斷。

🔗 **來源**
- 標題：Claude Mythos 5.1 and Fable 5.1: Capabilities
- 作者／機構：TheZvi @ Don't Worry About the Vase
- 連結：https://thezvi.wordpress.com/2026/09/05/claude-mythos-5-1-and-fable-5-1-capabilities/

#Anthropic #ClaudeAI #LLM #AIBenchmark #AgenticAI #ClaudeCode #AIRelease #GPT6 #AIInfrastructure #MachineLearning
