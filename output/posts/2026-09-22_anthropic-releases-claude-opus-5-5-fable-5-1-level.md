---
title: 'Anthropic Releases Claude Opus 5.5: Fable 5.1-Level Performance at 40% Lower
  Running Cost Than Opus 5'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/22/anthropic-claude-opus-5-5-release/
model: claude-code/sonnet
generated_at: '2026-09-22T20:30:19.165055'
score: 90
---

📌 【Anthropic】Opus 5.5：追平 Fable 5.1，成本砍 40%

TL;DR：Opus 5.5 官方宣稱追平 Fable 5.1，執行成本卻降 40%。

一個模型如果效能持平、價格卻砍掉四成，工程師該關心的問題就不再是「強不強」，而是「劃不划算」。MarkTechPost 這篇報導把 Anthropic 公布的 benchmark 數字和成本拆開來看，答案比表面上更有意思。

🤔 **Claude 5.5 家族第一棒**

Anthropic 發布了 Claude Opus 5.5，是 Claude 5.5 家族的第一個模型。官方表示，多數工作上它的表現達到 Claude Fable 5.1 的水準，在典型工作負載、預設設定下，執行成本比 Opus 5 低 40%。在 Anthropic 自己的 benchmark 上，它在 agentic coding、電腦操作（computer use）與知識工作領域都居於領先。

目前只能以 managed API 模型的形式部署，Anthropic 沒有釋出權重，因此無法自架。開發者可以在 Claude Platform、Amazon Web Services、Google Cloud 與 Microsoft Azure 上呼叫 claude-opus-5-5，並且和過去的 Opus 模型一樣支援 Zero data retention。

📊 **Benchmark 數字：贏在哪裡、輸在哪裡**

報導指出，Opus 5.5 的分數是在 adaptive thinking 開到 max effort、且生產環境安全防護開啟的情況下測得；Terminal-Bench 4.0 的分數則是在 xhigh effort 下取得。GPT-6 Astra 在 Terminal-Bench-Science 與 AutomationBench 上仍然領先；值得留意的是，Zapier 跑 AutomationBench 時沒有使用 fallback 模型，所以安全防護介入的情況也被算成失敗。Anthropic 自己也提醒，benchmark 之間的分數差距正在變得越來越不可靠，實際使用中 Opus 5.5 與 Fable 5.1 的差距比分數看起來的要小。

真正有意思的是成本校正後的結果：在預設（medium）effort 下，Opus 5.5 在 FrontierCode 拿下 54.6%，超過 GPT-6 Astra 最高的 53.3%，但每個任務的成本大約只有後者的五分之一；在 CursorBench 上，medium effort 拿到 52.5%，比 GPT-5.6 Sol 的最佳成績高 11 個百分點，成本大約是其三分之一。

💡 **成本砍 40% 的三個來源**

Opus 5.5 服務所需的運算量比 Opus 5 少，定價也反映了這一點：agentic 與 coding 場景中佔成本大宗的快取讀取費用下降 60%，加上每個任務用掉的 token 更少，兩者相加就是官方所說的 40% 成本下降。輸出生成速度也比 Opus 5 快超過 30%，Claude Code 與 Claude Platform 上的 Fast mode 更可以達到最高 2.5 倍的速度，價格為每百萬 token 輸入 8 美元、輸出 40 美元。Anthropic 同時調高了 Pro、Max、Team 以及採席位計費的 Enterprise 方案的五小時用量上限，訂閱者也能把重置的額度留到之後使用。

寫作風格也做了調整：報導指出 Opus 5.5 會把關鍵資訊放在最前面、減少術語，並且更確實地遵守使用者給的寫作規則。

⚠️ **安全防護升級，但也代表限制變多**

這是 Anthropic CEO Dario Amodei 呼籲「放緩前沿競速」之後的第一個發布，發布前經過 METR、Frontier Design 等外部評估單位測試。它在 Anthropic 涵蓋近 2000 個情境的自動化行為稽核中拿下歷來最高分；在一項新的 containment 測試中，嘗試繞過限制的頻率比 Opus 5 少了約 85%，不過報導也提到，這個模型經常會自己懷疑正在被評測。它在生物與資安能力上與 Claude Mythos 5.1 相當，因此也搭載了與 Fable 5.1 類似的安全防護機制，對應的結果是請求被拒絕的情況會變多。另外還有兩個會影響整合的變化：thinking 功能無法再被關閉；輸出內容也會加上因應歐盟 AI 法案要求的浮水印。完整細節列在 Opus 5.5 的 System Card 中。

🎯 **實務啟示**

如果你的應用是用 Opus 系列做 agentic coding 或大量文件工作，成本結構的改變可能比效能提升更值得關注：快取讀取費用降 60%、整體成本降 40%，代表原本因為成本考量縮小規模的 agentic 任務，現在有機會重新放大規模跑。但也要留意 thinking 無法關閉、安全分類器更嚴格這兩點，如果應用場景涉及對延遲或內容審查敏感的流程，上線前該用自己的資料重新測一輪，而不是只看官方的 benchmark 對比。

🔗 **來源**
- 標題：Anthropic Releases Claude Opus 5.5: Fable 5.1-Level Performance at 40% Lower Running Cost Than Opus 5
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/22/anthropic-claude-opus-5-5-release/

#Anthropic #ClaudeOpus #LLM #AIBenchmark #AgenticCoding #GenerativeAI #AICost #ModelRelease #MachineLearning #AISafety
