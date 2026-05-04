---
title: "Prompt-Induced Score Variance in Zero-Shot Binary Vision-Language Safety Classification"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.00326
score: 104
model: tencent/hy3-preview:free
generated_at: 2026-05-04T20:35:32.339959
---

📌 【Johns Hopkins 最新研究】同一張圖、同一個模型，提示詞換個說法，安全分數就崩潰？

你以為零擋（zero-shot）視覺語言模型的安全分類器已經足夠穩定？研究顯示：只要把提示詞改成語意等價的不同說法，首 token 產出的「不安全機率」就會發生顯著擾動——同一個樣本，同一個模型，同一個安全標籤位置，分數卻可以天差地別。

🤔 **零擋安全分類看似省事，卻隱藏提示誘發的方差陷阱**

在紅隊測試與部署越來越多依賴 VLM 安全分類器的當下，工程師常以單一提示詞的 first-token probability 作為決策分數。這種做法直覺上簡單且無需標籤，但 Johns Hopkins 的研究指出：這類分數在語意等價的提示重述（prompt reformulation）下並不可靠，方差直接轉化為標籤歧異與錯誤率上升。

🧪 **跨模型與跨基準的壓力測試：14 組 dataset–model 配對**

研究以多個視覺安全基準與多個 VLM 家族進行評估，固定二元標籤位置後，僅透過語意等價但表面不同的提示詞組合來觀察 first-token 機率波動。重點不在於重新訓練模型，而在於揭示零擋設定下的穩定性邊界，並檢視 prompt-level 機率分佈是否能成為可靠度診斷。

⚠️ **同一個樣本，提示詞換個說法，不安全機率就明顯偏移**

- 語意等價的提示重述會導致 materially different 的 unsafe probabilities  
- cross-prompt 方差愈高，愈容易伴隨 prompt-level 標籤不同意與較高分類錯誤  
- 這種方差提供了一個清晰的「易碎性壓力測試」信號，可直接作為部署前的診斷指標

💡 **無需訓練的均值集成，大幅降低 NLL 與 ECE**

研究提出 training-free mean ensemble 作為標籤免費的第一階段：

- 在全部 14 組 dataset–model 配對上，mean ensemble 均改善 NLL  
- 在 12/14 組上改善 ECE，相較單一提示詞（train-selected baseline）穩健提升  
- 對標有標籤的溫度縮放、Platt scaling 與 isotonic regression，mean ensemble 在 head-to-head NLL 比較中贏面更高

📉 **在 AUROC 與 AUPRC 上的排名穩定性**

- 相較單一提示詞基線，mean ensemble 在 AUROC 與 AUPRC 上均具一致性的排序優勢  
- 對比完整 15-prompt 分布，AUPRC 優勢持續存在；AUROC 則呈現較為和緩的弱化，顯示均值策略在精細排序上仍有提升空間

⚙️ **均值不是終點，而是標籤校準的穩健起點**

研究指出，在有標籤的情境下，以均值作為第一階段、再疊加標籤校準（labeled calibration），可以獲得進一步收斂。這顛覆了「均值集成必須取代校準」的直覺，反而證明 prompt averaging 與後續校準可以協同強化。

🎯 **把 prompt-family 評估與均值聚合當作標準基線**

- 部署前應進行 prompt-family 的可靠度應力測試  
- 將 training-free mean aggregation 作為 label-free 基線，而非僅依賴單一提示詞  
- 紅隊測試與生產環境均可直接採用，降低由提示誘發的方差風險

🔗 **論文連結**  
📝 Prompt-Induced Score Variance in Zero-Shot Binary Vision-Language Safety Classification  
👤 Charles Weng, Dingwen Li, Alexander Martin (Johns Hopkins University; Independent)  
🔗 https://arxiv.org/abs/2605.00326  

你在使用 VLM 做安全分類或紅隊測試時，會不會刻意驗證不同提示詞下的分數穩定性？歡迎分享你的防禦流程 👇  

#AI #VisionLanguageModel #Safety #RedTeaming #MachineLearning #JohnsHopkins #ZeroShot #ModelReliability
