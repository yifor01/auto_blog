---
title: 'Ask, Solve, Generate: Self-Evolving Unified Multimodal Understanding and Generation
  via Self-Consistency Rewards'
source: arXiv
url: http://arxiv.org/abs/2606.27376v1
score: 86
model: google/gemma-4-31b-it:free
generated_at: '2026-06-27T19:34:20.137824'
---

📌 【新研究】無需標註資料：讓多模態模型透過「自問自答」自我演進

TL;DR：提出一套自我演進框架，透過內建三個角色產生一致性獎勵，讓 LMM 在無標註情況下同步提升理解與生成能力。

大多數支援視覺理解與影像生成的統一多模態模型 (LMMs) 仍高度依賴人工標註、偏好標籤或外部獎勵模型。但如果模型能僅憑「無標註影像」就自主提升這兩種能力，會如何？

🤔 **擺脫對人工標註與外部獎勵模型的依賴**

研究團隊提出一個自我演進的訓練框架，旨在讓模型在不需要人類監督的情況下，透過內部一致性訊號 (Consistency Signals) 進行自我最佳化。該框架將模型拆解為三個內部角色：
- Proposer：負責生成視覺問題。
- Solver：負責回答問題並進行評估。
- Generator：負責合成影像。

🧩 **利用一致性訊號與熵值穩定學習**

為了在沒有外部指導的情況下穩定訓練，研究團隊設計了以下機制：

- 穩定學習訊號：引入 Solver Token Entropy (STE)，利用 token 層級的預測不確定性提供連續的難度訊號。當樣本層級的一致性變得不可靠時，STE 仍能提供有效的學習指導。
- 影像生成評估：採用多尺度內部評估方案，結合「問答忠實度評分 (QA fidelity scoring)」與「迴圈一致性描述 (cycle-consistent captioning)」。
- 耦合機制：透過 Solver 建立理解與生成的耦合，更好的視覺理解能讓生成品質的評估更可靠，進而強化內部的訓練訊號。

📊 **跨架構的通用性與效能提升**

該框架不依賴特定架構，僅需模型原生的提示 (prompting) 與生成介面，即可在不同型別的模型上執行，包括：
- 擴散模型 (Diffusion-based) 的 BLIP3o
- 整流流 (Rectified-flow) 的 BAGEL
- 自回歸 (Autoregressive) 的 VARGPT-v1.1

在實驗結果方面，該方法在八項理解指標上均優於對應的基礎模型。其中在 BAGEL 模型上，MMMU 的絕對增益達 3.5%，GenEval 的影像生成效能則從 82% 提升至 85%。

🎯 **實務啟示**

這項研究證明了「自我監督」在多模態領域的可能性。對於工程師而言，這提供了一種新思路：透過設計內部的角色對抗或一致性檢查（例如：生成問題 $\rightarrow$ 回答 $\rightarrow$ 根據回答生成影像 $\rightarrow$ 再次描述），可以在缺乏高質量標註資料的情況下，利用海量無標註影像來強化模型的通用能力。

🔗 **來源**
- 標題：Ask, Solve, Generate: Self-Evolving Unified Multimodal Understanding and Generation via Self-Consistency Rewards
- 作者／機構：Ritesh Thawkar, Shravan Venkatraman, Omkar Thawakar, Abdelrahman Shaker, Fahad Khan
- 連結：http://arxiv.org/abs/2606.27376v1

#LMM #Multimodal #SelfSupervisedLearning #ImageGeneration #ComputerVision #SelfConsistency #DeepLearning #AI #MachineLearning #SelfEvolving
