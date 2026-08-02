---
title: Scaling Properties of Continuous Diffusion Spoken Language Models
source: Apple ML
url: https://machinelearning.apple.com/research/scaling-properties-continuous-diffusion
score: 98
model: google/gemma-4-31b-it:free
generated_at: '2026-07-06T20:23:15.892655'
---

📌 【Apple ML 研究】連續擴散模型能否打破語音語言模型的尺度瓶頸？

TL;DR：Apple 研究發現連續擴散（CD）語音模型具有 Scaling Laws，且在高算力下對參數與資料比例的敏感度降低。

目前的語音語言模型（SLMs）在效能上落後於純文字或文字轉語音模型。雖然離散自迴歸（AR）模型是目前的趨勢，但將連續語音離散化會產生瓶頸，且需要極高的運算量與資料量才能追上文字模型。

🤔 **離散化瓶頸與連續擴散的替代方案**

為了克服離散化帶來的限制，研究團隊探索了「連續擴散（Continuous Diffusion, CD）」語音語言模型的可能性。為了量化這類模型的語言品質，研究者特別引入了一項新指標：音素 Jensen-Shannon 散度（phoneme Jensen-Shannon divergence, pJSD）。

🧩 **連續擴散模型的尺度律（Scaling Laws）分析**

研究發現 CD SLMs 在驗證損失（Validation Loss）與 pJSD 上展現出與自迴歸模型類似的尺度律行為。關鍵發現如下：

- **參數與資料的比例變動**：隨著運算量增加，最佳的「Token-to-parameter」比例會隨之下降。
- **對配置的容忍度增加**：隨著運算量提升，損失函式對資料量與模型大小的選擇變得較不敏感。這意味著在高算力設定下，即便參數與資料的分配比例有所偏移，仍能維持接近最佳（near-optimal）的效能。
- **推論潛能**：上述的特性顯示 CD SLM 具有實現快速推論（fast inference）的潛力。

📊 **16B 參數模型的生成能力與限制**

當模型規模擴展至 16B 參數，並使用數千萬小時的對話資料進行訓練後，CD SLM 能生成具備以下特性的語音：
- 情感表達（Emotive）
- 韻律感（Prosodic）
- 多說話者（Multi-speaker）
- 多語言（Multilingual）

⚠️ **長文本連貫性仍是挑戰**

儘管在語音品質與多樣性上有顯著進展，但研究指出，要讓模型實現「長篇幅的連貫性（long-form coherence）」仍然是一個重大的挑戰。

🎯 **實務啟示**

對於開發語音 AI 的工程師而言，這項研究證明了連續擴散路徑在擴展規模上的可行性。特別是當運算資源充足時，模型對資料與參數分配的敏感度降低，這為設計高效能語音模型提供了更寬容的超參數調校空間，且連續路徑可能比離散化路徑更具推論速度的優勢。

🔗 **來源**
- 標題：Scaling Properties of Continuous Diffusion Spoken Language Models
- 連結：https://machinelearning.apple.com/research/scaling-properties-continuous-diffusion

#AI #SpeechSynthesis #DiffusionModels #ScalingLaws #AppleML #SLM #NLP #MachineLearning #DeepLearning #SpeechProcessing
