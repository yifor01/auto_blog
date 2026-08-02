---
title: A Sovereign, Open-Source Foundation Model for German and English
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.09424
score: 97
model: google/gemma-4-31b-it:free
generated_at: '2026-07-13T08:54:02.464562'
---

📌 SoofiS‑30B‑A3B：結合 MoE 與 Mamba 的開源德英雙語基礎模型

TL;DR：SoofiS‑30B‑A3B 以 30 B 參數的 MoE‑Mamba 混合架構，在德語與英語基準上匹配 14‑27 B 密集模型，同時在長上下文與高併發部署上具顯著效能優勢。

隨著大型語言模型在多語言應用的需求持續增長，歐洲尤其需要具備主權、開源且效能可控的基礎模型。SoofiS‑30B‑A3B 正是針對德語與英語市場，以混合式專家模型（Mixture‑of‑Experts，MoE）結合 Mamba 時序結構，提供高效長上下文推理的解決方案。

🧩 **混合 MoE‑Mamba 架構**

- **MoE 參數啟用**：模型總參數 30 B，推理時僅啟用 3 B（即 10%）參數，使每個 token 只使用少量專家，降低計算成本。
- **Mamba 時序層**：在 Transformer 之上加入 Mamba 結構，負責捕捉長距離依賴，保持推理快取（cache）大小近乎恆定，隨上下文長度增長不會大幅膨脹。
- **效能優勢**：相較於全密集模型，該設計在長序列（>4 k tokens）與高併發服務（多請求同時推理）下，吞吐量提升顯著。

📊 **訓練規模與語言偏重**

- **資料量**：約 27 兆 token，刻意提升德語比例，使德語語料在訓練集合中佔較大權重。
- **語言表現**：在綜合英語與德語基準測試中，SoofiS‑30B‑A3B 的成績與 14‑27 B 的密集模型相當，且在 17 個開源基礎模型中，取得最高的程式碼生成聚合分數（英、德雙語皆領先）。

⚠️ **比較與限制**

- 與歐洲其他主權基線模型（包括參數更多但活躍參數較少的模型）相比，SoofiS‑30B‑A3B 在所有測試中均有優勢。
- 於開源模型中，英、德雙語評分最高，僅次於 Olmo‑332B 與 Apertus‑70B（這兩者均非開源），顯示在開放環境下的競爭力。

🎯 **實務啟示**

- **長上下文應用**：檔案摘要、法律條文分析等需要處理數千 token 的場景，可直接受惠於近恆定快取的效能。
- **高併發服務**：雲端 API 或企業內部聊天機器人，因僅啟用部份參數，可在相同硬體上支援更多同時請求。
- **主權部署**：模型全程於德國 Industrial AI Cloud 於 Deutsche Telekom Munich 資源上訓練，符合歐洲資料主權與合規需求。

🔗 來源
- 標題：A Sovereign, Open-Source Foundation Model for German and English
- 連結：https://huggingface.co/papers/2607.09424

#SoofiS #MixtureOfExperts #Mamba #OpenSourceLLM #GermanNLP #EnglishNLP #LongContext #HighThroughput #AIInfrastructure #HPC #GermanAI #Transformer #LLM #MachineLearning #AIResearch #HuggingFacePapers
