---
title: '[AINews] Hot Chips: OpenAI’s Jalapeño, Cerebras CS-5, Groq 3 LPX, Apple M6'
source: Latent Space
url: https://www.latent.space/p/ainews-hot-chips-openais-jalapeno
model: claude-code/sonnet
generated_at: '2026-08-27T17:18:44.249880'
score: 109
---

📌 OpenAI 自研 Jalapeño 晶片首曝光，每瓦效能挑戰 NVIDIA

TL;DR：OpenAI 公布自研推理晶片 Jalapeño 首批數據，效能每瓦與延遲雙雙優於 GB200/GB300。

過去一年，業界都在談論 OpenAI 與 Broadcom 合作自研晶片的消息，但這次在第 37 屆 Hot Chips 大會上，OpenAI 拿出的不只是路線圖，而是第一批真實跑分。這件事之所以引起熱議，是因為比較對象不是上一代硬體，而是 NVIDIA 目前最新的 GB200／GB300 系統。

🤔 **從「有沒有自研晶片」到「每瓦能做多少工作」**

報導指出，這次揭露的關鍵指標已經從單純的算力轉向效能每瓦（performance per watt）。OpenAI 表示，在自家測試的真實模型負載下，Jalapeño 在尖峰吞吐量下每瓦能多做 1.5~1.9 倍的工作，端到端延遲低 1.7~3.6 倍，在高互動性負載上效能更高出 2.1~4.1 倍。晶片額定功耗為 700W，但在受測情境中實際運作多維持在 550W 或以下。

🧩 **不靠花招也能贏，且已排進部署時程**

多篇技術分析特別提到一個細節：部分比較情境中，Jalapeño 甚至沒有動用預填充／解碼分離（prefill/decode disaggregation）或推測解碼（speculative decoding）等常見加速手法，卻仍勝過有使用這些技巧的對手系統。SemiAnalysis 的分析認為，以第一代 ASIC 而言這樣的表現並不常見，並直接把它拿來和 Blackwell、Rubin 等級的系統對比。OpenAI 表示，Jalapeño 將於今年底前開始部署進自家基礎設施，第二代已在深度開發中，第三代也已啟動。

💡 **模型本身也參與了寫核心程式碼**

另一個值得工程師留意的細節：OpenAI 表示 GPT-Astra 搭配 Codex 協助撰寫並最佳化底層核心程式碼（kernel），在大約兩個月內把三個原本不在計畫內的開放權重模型帶到 Jalapeño 上的高效能水準；針對特定的 attention 與 MoE 區塊，這些由模型輔助完成的實作據稱比既有的人類專家手寫程式碼還快 1.5~1.8 倍。這代表編譯器與核心層級的最佳化工作，正逐漸被納入模型改進的迴圈中，而不只是應用層的程式撰寫。

⚠️ **封裝與代工產能仍是硬瓶頸**

即便如此，多篇評論也提醒，即使前沿實驗室在推理經濟上不再完全依賴 NVIDIA，封裝與晶圓代工（如 TSMC、CoWoS）的產能仍是難以繞過的限制，這部分不會因為晶片設計本身的進步而自動解決。

🎯 **實務啟示**

對於營運大規模推理服務的工程團隊，Jalapeño 釋出的訊號是：效能每瓦與延遲的平衡，正在成為和單純吞吐量同等重要的採購與架構決策依據；同時，模型輔助寫核心程式碼的做法，也值得評估是否能加進自家的效能最佳化流程中。

🔗 **來源**
- 標題：[AINews] Hot Chips: OpenAI's Jalapeño, Cerebras CS-5, Groq 3 LPX, Apple M6
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-hot-chips-openais-jalapeno

#OpenAI #Jalapeño #AIChip #Inference #HotChips #NVIDIA #ASIC #PerformancePerWatt #AIInfrastructure #Semiconductors
