---
title: Data-Efficient Autoregressive-to-Diffusion Language Models via On-Policy Distillation
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.06712
score: 100
model: google/gemma-4-31b-it:free
generated_at: '2026-06-08T20:36:50.373954'
---

📌 **將自回歸模型轉換為 Diffusion LM：用 On-Policy 蒸餾降低訓練成本**

目前的 LLM 主流是自回歸 (Autoregressive, AR) 模式，但 Diffusion 模型在生成多樣性與控制力上具有潛力。然而，將 AR 模型轉換為 Diffusion 模型時，最頭痛的往往是「訓練與推論不匹配」以及對海量資料的依賴。

如果能將已經訓練好的 AR 模型「轉化」為 Diffusion 模型，且不需要重新投入天文數字的資料量，這將為模型開發帶來極大的效率提升。

🤔 **訓練與推論的「不匹配」是 Diffusion LM 的痛點**

在傳統的知識蒸餾中，如果學生模型（Diffusion）在訓練時看到的資料分佈與推論時的採樣過程不一致，會導致嚴重的效能下降。這種 Train-Inference Mismatch 使得許多轉換嘗試需要極大量的資料來修正偏差，增加了訓練成本。

🧪 **透過 On-Policy Distillation 實現高效轉換**

這項研究提出了一種新的轉換路徑：利用 **On-Policy Distillation (在線策略蒸餾)**。

核心設計在於讓 Diffusion 模型在訓練過程中，直接學習由其自身採樣產生的分佈，而非僅僅依賴靜態的離線資料集。這種方法讓模型在訓練時就能「預演」推論過程，從而有效消除不匹配問題，並顯著降低對訓練 Token 數量的需求，實現更高的資料效率 (Data-Efficient)。

🚀 **核心發現：更少的資料，更穩定的轉換**

研究結果顯示，透過這種 On-Policy 蒸餾方式，可以將自回歸模型成功地轉換為 Diffusion 語言模型，且在以下兩點有顯著突破：
- **消除不匹配**：解決了訓練與推論之間的分佈差異，提升生成品質。
- **降低成本**：大幅減少了轉換過程所需的訓練資料量，讓模型轉換變得更加輕量且可行。

💡 **從 AR 到 Diffusion：生成範式的轉換**

這項研究的關鍵洞察在於：不需要從零開始訓練一個 Diffusion LM，而是將 AR 模型的知識作為起點，透過 On-Policy 的機制將「預測下一個 Token」的能力，轉化為「逐步去噪生成」的能力。對於想要探索非自回歸生成（Non-autoregressive generation）以追求更靈活生成控制的工程師來說，這提供了一個極具實用價值的路徑。

⚠️ **研究限制與實踐考量**

由於目前僅提供摘要資訊，具體的性能損耗（例如轉換後與原 AR 模型的準確率對比）以及在不同規模模型上的泛化能力仍需參考完整論文的實驗數據。此外，Diffusion 模型的採樣速度與自回歸模型的對比（Latency vs. Quality）也是實務應用時需要權衡的關鍵。

🎯 **降低訓練成本，探索新型生成模型的實踐路徑**

對於 AI 研究者與工程師，這項研究提供了兩個行動啟示：
- **降低門檻**：如果你希望嘗試 Diffusion LM 但缺乏海量資料，On-Policy 蒸餾是一個高效的替代方案。
- **快速驗證**：由於已有開源實作，開發者可以快速測試將現有 AR 模型轉換後的生成效果，探索其在特定任務上的潛力。

🔗 **論文連結**
📝 Data-Efficient Autoregressive-to-Diffusion Language Models via On-Policy Distillation
🔗 論文：https://huggingface.co/papers/2606.06712

你認為 Diffusion 模型未來會取代自回歸模型成為生成主流，還是兩者會採取互補的協作模式？歡迎在評論區分享你的看法 👇

#AI #LLM #DiffusionModel #MachineLearning #HuggingFace #DeepLearning #模型蒸餾
