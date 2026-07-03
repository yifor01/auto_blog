---
title: Learning Unmasking Policies for Diffusion Language Models
source: Apple ML
url: https://machinelearning.apple.com/research/unmasking
score: 93
model: google/gemma-4-31b-it:free
generated_at: '2026-07-03T19:52:32.652916'
---

📌 【Apple ML 研究】不再依賴經驗調校：用強化學習最佳化 Diffusion LLM 的解碼策略

TL;DR：提出用 RL 訓練輕量化 Policy，取代 Diffusion LLM 取樣時的手動閾值設定，提升生成品質與效率。

目前的 Diffusion 大語言模型 (dLLMs) 在許多工上的表現已能與傳統的自迴歸 (Autoregressive) 模型媲美，且在推論效率上具有潛在優勢。然而，dLLMs 面臨一個核心設計挑戰：在每一輪擴散步驟中，該選擇哪些 token 進行「去遮蔽」(unmasking)？

🤔 **手動啟發式策略的侷限性**

目前常見的作法是使用啟發式策略（如信心閾值 thresholding），根據 token 的信心值來決定是否解碼。雖然這比隨機解碼能提升樣本品質與吞吐量，但存在兩大問題：
- 需要耗費大量時間進行手動調校 (manual tuning)。
- 當使用較大的區塊大小 (block sizes) 時，效能會出現下降。

🧩 **將取樣過程形式化為馬可夫決策過程 (MDP)**

為瞭解決上述問題，研究團隊提出不再依賴經驗法則，而是直接「訓練」一個取樣程式。其技術路徑如下：
1. **環境定義**：將 masked diffusion 的取樣過程定義為一個馬可夫決策過程 (MDP)，其中 dLLM 本身即作為環境 (environment)。
2. **Policy 設計**：設計一個輕量化的策略模型，僅使用單層 Transformer。
3. **運作流程**：該 Policy 接收 dLLM 輸出的 token 信心值 $\rightarrow$ 決定哪些 token 應該被去遮蔽 (unmasking decisions)。
4. **訓練方式**：利用強化學習 (Reinforcement Learning) 來最佳化該 Policy 的決策。

📊 **實驗結果：超越啟發式策略**

研究結果顯示，這種經由 RL 訓練的 Policy 在不同生成設定下表現強勁：
- **半自迴歸 (Semi-autoregressive/Block) 生成**：表現與目前最頂尖的啟發式策略相當。
- **全擴散 (Full-diffusion) 設定**：表現優於現有的啟發式策略。

🎯 **實務啟示**

對於開發 dLLM 的工程師而言，這項研究提供了一個將「取樣策略」從硬編碼的閾值轉向「可學習模型」的新方向。透過引入輕量化 Policy，可以減少對超引數調校的依賴，並在全擴散生成場景中獲得更好的效能。

🔗 **來源**
- 標題：Learning Unmasking Policies for Diffusion Language Models
- 作者／機構：Metod Jazbec, Theo X. Olausson, Louis Béthune, Pierre Ablin, Michael Kirchhof, João Monteiro, Victor Turrisi, Jason Ramapuram, Marco Cuturi @ Apple ML
- 連結：https://machinelearning.apple.com/research/unmasking

#DiffusionLM #LLM #ReinforcementLearning #NLP #AppleML #SamplingPolicy #ICML #GenerativeAI #MachineLearning #DeepLearning
