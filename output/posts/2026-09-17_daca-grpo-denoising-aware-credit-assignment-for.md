---
title: 'DACA-GRPO: Denoising-Aware Credit Assignment for Reinforcement Learning in
  Diffusion Language Models'
source: Apple ML
url: https://machinelearning.apple.com/research/denoising-aware-credit-assignment
model: claude-code/sonnet
generated_at: '2026-09-17T20:33:35.374720'
score: 98
---

📌 【Apple ML 研究】擴散語言模型的 RL 訓練,漏掉了「哪一步比較重要」

TL;DR：DACA-GRPO 幫擴散語言模型的強化學習補上時序信任分配，插即用最多帶來 36.3pp 提升。

擴散大型語言模型（diffusion LLM）被視為自迴歸模型的另一種可能，但當研究者把主流的 GRPO 強化學習方法直接搬過來用時,卻忽略了一件事：去噪過程中的每一步,重要性真的都一樣嗎？

🤔 **GRPO 用在擴散模型上的兩個結構性問題**

Apple ML 團隊指出，現有把 GRPO 套用在擴散語言模型上的做法，存在兩個根本弱點。第一，缺乏跨去噪軌跡的時序信任分配（temporal credit assignment）：所有去噪步驟被一視同仁地對待，沒有區分哪一步的決策對最終結果影響更大。第二，用於策略最佳化的 mean-field 概似估計本身帶有系統性偏誤，而且變異度高，這會直接影響梯度更新的品質。

🧩 **兩個輕量機制：去噪進度分數 + 分層遮罩概似**

論文提出 DACA-GRPO（Denoising-Aware Credit Assignment for GRPO），設計成可以直接疊加在任何 GRPO 風格訓練器上的輕量插件，包含兩個互補機制：

第一是去噪進度分數（Denoising Progress Scores）：從模型的中間預測結果中，直接萃取每個 token 的重要性權重，且不需要額外的前向傳遞成本。第二是分層遮罩概似（Stratified Masking Likelihood）：把 token 位置切分成不同的層（strata），讓每個 token 在被預測時，都能參考序列中大部分的上下文，藉此降低 mean-field 估計帶來的偏誤。

📊 **七項基準測試，最高提升 36.3 個百分點**

作者將 DACA-GRPO 疊加在三種 GRPO 基礎方法之上，並在涵蓋數學推理、程式碼生成、約束滿足與受限生成的七項基準上測試，結果顯示效果一致提升：

| 任務類型 | 最高提升幅度 |
|---|---|
| 數學推理 | 5.6 個百分點 |
| 程式碼生成 | 7.4 個百分點 |
| 約束滿足 | 36.3 個百分點 |
| JSON schema 遵循 | 5.9 個百分點 |

其中約束滿足任務的提升幅度特別顯著，遠高於其他任務類別。

💡 **把「去噪步驟不等價」這件事真正納入訓練訊號**

這篇研究的核心貢獻，是把擴散語言模型獨有的結構特性（多步去噪、每步預測品質不一）真正轉化為可用的訓練訊號，而不是像過去那樣直接套用為自迴歸模型設計的信任分配邏輯。兩個機制都刻意設計成低成本、可插拔，這意味著它不是要取代 GRPO，而是補上一塊原本被忽略的資訊，這對已經投入 GRPO 訓練管線的團隊而言，遷移成本相對友善。

🎯 **實務啟示**

如果團隊正在用 GRPO 類方法訓練擴散語言模型，且在約束滿足或格式遵循類任務上表現不如預期，這篇論文提出的兩個機制，特別是不需要額外前向成本的去噪進度分數，值得作為優先嘗試的低成本改進項。

🔗 **來源**
- 標題：DACA-GRPO: Denoising-Aware Credit Assignment for Reinforcement Learning in Diffusion Language Models
- 作者／機構：Amin Karimi Monsefi, Dominic Culver, Nikhil Bhendawade, Lokesh Boominathan, Manuel R. Ciosici, Yizhe Zhang, Irina Belousova（Apple ML）
- 連結：https://machinelearning.apple.com/research/denoising-aware-credit-assignment

#AppleML #DiffusionLanguageModel #ReinforcementLearning #GRPO #RLVR #LLM #NLP #MachineLearning #CodeGeneration #MathReasoning
