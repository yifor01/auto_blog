---
title: OpenAI says its Jalapeño chip can power faster AI responses than the competition
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/984290/openai-jalapeno-ai-chip-benchmarks
model: claude-code/sonnet
generated_at: '2026-08-26T06:32:28.325326'
score: 67
---

📌 OpenAI 自研 Jalapeño 晶片，推論效能宣稱贏過 Nvidia GB200/GB300

TL;DR：OpenAI 首度公布 Jalapeño 推論晶片實測數據，稱能同時做到低延遲與高吞吐量。

延遲與吞吐量通常是一場零和賽局，要快就得犧牲同時處理量，反之亦然。但 OpenAI 硬體副總裁 Richard Ho 在記者會上宣稱，Jalapeño 打破了這個慣例，「魚與熊掌兼得」。

🤔 **一顆為推論而生的 ASIC**

Jalapeño 是 OpenAI 與 Broadcom 合作開發的 Application-Specific Integrated Circuit（ASIC），今年 6 月首次亮相，設計目的鎖定 AI 推論（inference）：也就是執行已訓練好的模型來完成任務或驅動 agent 的階段，而非模型訓練。

📊 **對比 Nvidia 超級晶片的實測數字**

OpenAI 使用推論基準測試平臺 InferenceX，將 Jalapeño 與當時最佳成績的 Nvidia GB200、GB300 超級晶片相比較，測試模型涵蓋 GPT-OSS 120B、DeepSeek R1、Kimi K2.5 1T 三款。結果顯示：

- 每瓦特能完成的 AI 工作量提升 1.5 到 1.9 倍
- 端到端延遲降低 1.7 到 3.6 倍

文中也附上一張 time between tokens（TBT，token 間隔時間，反映回應速度）的圖表，用以佐證上述延遲改善。Ho 表示，這意味著使用者能得到「更快的回應、反應更靈敏的 agent，以及需求成長時更穩定的服務可用性」。

💡 **不是要取代 Nvidia，而是分散供應鏈風險**

即便數據亮眼，Ho 也明確表示 OpenAI 不打算讓 Jalapeño 取代整個晶片陣容，公司的整體算力策略仍包含 Nvidia 等「非常好的合作夥伴」。OpenAI 計畫今年底先「小規模」部署 Jalapeño，2027 年起才會逐步擴大量產規模，但並未透露明年具體部署數量。同時，第二代與第三代晶片的研發也已在進行中。

⚠️ **一份出自廠商之手的基準測試**

目前公開的所有效能數字都來自 OpenAI 自行釋出的部落格與記者會，比較對象、測試方法與具體測試條件的細節有限，尚待第三方或更完整的技術報告驗證。

🎯 **實務啟示**

對於用 GPT-OSS、DeepSeek R1、Kimi K2.5 這類大型模型跑推論服務的工程師而言，Jalapeño 若如期在 2027 年放量，代表未來雲端推論的硬體選項會更多元，也可能間接影響 API 定價與延遲 SLA。但短期內，Nvidia 生態仍是主流選擇，不必急著調整基礎設施規劃。

🔗 **來源**
- 標題：OpenAI says its Jalapeño chip can power faster AI responses than the competition
- 作者／機構：Emma Roth, The Verge
- 連結：https://www.theverge.com/ai-artificial-intelligence/984290/openai-jalapeno-ai-chip-benchmarks

#OpenAI #Jalapeno #AIChip #Inference #Nvidia #Broadcom #ASIC #AIInfrastructure #LLM #ChipRace
