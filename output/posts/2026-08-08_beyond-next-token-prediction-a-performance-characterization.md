---
title: 'Beyond Next-Token Prediction: A Performance Characterization of Diffusion
  versus Autoregressive Language Models'
source: Apple ML
url: https://machinelearning.apple.com/research/diffusion-autoregressive-performance
model: tencent/hy3:free
generated_at: '2026-08-08T06:49:22.475133'
score: 87
---

📌 【Apple ML 研究】Diffusion 與 Autoregressive 模型性能對比：並行生成的優勢與長文本挑戰

TL;DR：研究指出 Diffusion 模型具備更高算術強度，但在長文本擴展性與批次吞吐量上仍遜於 Autoregressive 模型。

🤔 **逐字預測的瓶頸：序列依賴與低算術強度**

目前的 LLM 主流架構是 Autoregressive Language Models (ARMs)，這類模型依賴於「下一字預測」（next-token prediction），必須根據已生成的 token 序列逐一生成下一個 token。這種內建的序列依賴性導致了推論時的算術強度（arithmetic intensity）較低，限制了硬體效能的發揮。

🧩 **Diffusion 模型的潛力：並行生成的機會**

為了突破序列生成的限制，Diffusion Language Models (DLMs) 成為一種具備潛力的替代架構。DLMs 的核心差異在於它可以並行生成輸出 token，藉由利用 token 位置間的並行性，DLMs 能展現出比 ARMs 更高的算術強度。

📊 **性能對比：並行性與擴展性的權衡**

研究透過理論分析與實證分析，揭示了兩者在不同維度的表現差異：

- **長文本擴展性**：雖然 DLMs 具備並行優勢，但在處理長文本時，其擴展性表現不如 ARMs。
- **批次推論效能**：在進行批次推論（batched inference）時，ARMs 表現更佳，因為它們能更有效地利用批次中不同序列間的並行性，從而獲得更高的吞吐量（throughput）。

💡 **解決方案：透過 Block-wise Decoding 提升擴展性**

為了讓 DLMs 能像 ARMs 一樣有效處理長文本，研究探索了「分塊解碼」（block-wise decoding）技術。這種方法將算術強度與序列長度解耦（decouple），進而讓 DLM 在長文本場景下擁有更好的擴展能力。

⚠️ **DLM 的關鍵優化方向：減少採樣步數**

研究強調，若要讓開源 DLM 在延遲（latency）表現上超越 ARMs，減少採樣步數（sampling steps）是關鍵的優化機會。

🎯 **實務啟示**

對於開發者而言，若追求極高的推論吞吐量，目前的 ARMs 仍具優勢；但若希望發揮硬體並行效能，開發更高效的 DLM 採樣演算法（減少採樣步數）並結合分塊解碼技術，將是實現低延遲並行生成的關鍵路徑。

🔗 **來源**
- 標題：Beyond Next-Token Prediction: A Performance Characterization of Diffusion versus Autoregressive Language Models
- 作者／機構：Minseo Kim, Coleman Hooper, Aditya Tomar, Chenfeng Xu, Mehrdad Farajtabar, Michael W. Mahoney, Kurt Keutzer, Amir Gholami @ Apple ML / Seoul National University / UC Berkeley / UT Austin / ICSI / LBNL
- 連結：https://machinelearning.apple.com/research/diffusion-autoregressive-performance

#LLM #DiffusionModels #AutoregressiveModels #NLP #MachineLearning #InferenceOptimization #ParallelGeneration #AIResearch #AppleML #DeepLearning
