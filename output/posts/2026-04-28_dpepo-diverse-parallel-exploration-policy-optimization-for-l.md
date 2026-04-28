---
title: "DPEPO: Diverse Parallel Exploration Policy Optimization for LLM-based Agents"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2604.24320
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-04-28T20:53:53.569123
---

📌 【電子科大 x 滴滴】讓 LLM Agent 同時探索多個環境，突破探索瓶頸

現行的 LLM Agent 大多遵循「先推理、後行動」的單線程模式，每一步只能與一個環境互動。這就像派一個探險家進入迷宮，一次只能走一條路。但如果有辦法讓 Agent 同時分身在多個平行宇宙探索，並共享經驗，效率會如何提升？

🤔 **單線程 Agent 的痛點：探索受限與環境理解不足**

基於 ReAct 等「Reason-then-Act」範式的 Agent 雖然在複雜任務中表現出色，但存在一個根本性的架構缺陷：每一步僅與單一環境互動。這導致 Agent 的探索空間受限，難以全面理解環境動態，且容易陷入局部最優。當任務需要大量試錯時，這種序列化的交互方式成為效率的瓶頸。

🧪 **DPEPO：多環境並行探索與跨軌跡經驗共享**

來自電子科技大學與滴滴的研究團隊提出了一種全新的 Agent 範式，並據此設計了 **DPEPO (Diverse Parallel Exploration Policy Optimization)** 演算法。核心概念是打破單環境限制，讓 Agent 能同時與多個環境交互，並整合不同軌跡的經驗。

DPEPO 的訓練分為兩個階段：
1.  **監督微調 (SFT)**：賦予 Agent 基本的並行推理與動作生成能力。
2.  **強化學習 (RL)**：採用階層式獎勵機制，包含軌跡級的成功獎勵，以及兩個關鍵的步驟級獎勵：
    *   **多樣性動作獎勵 (Diverse Action Reward)**：鼓勵 Agent 採取不同的行動。
    *   **多樣性狀態轉移獎勵 (Diverse State Transition Reward)**：鼓勵探索不同的環境狀態。
    這兩個獎勵會主動懲罰行為冗餘，強制 Agent 進行廣泛探索。

 **在 ALFWorld 與 ScienceWorld 達成 SOTA**

實驗結果顯示，DPEPO 在 ALFWorld (家用環境模擬) 和 ScienceWorld (科學實驗模擬) 兩大基準測試中，均取得了最先進 (State-of-the-Art, SOTA) 的成功率。值得注意的是，在大幅提升探索效率的同時，其運算效率仍與強大的序列基準模型相當，並未帶來過多的額外開銷。

💡 **從「單一試錯」到「平行取樣」的範式轉移**

這篇論文的核心價值在於將 Agent 的互動模式從「序列式」轉向「並行式」。透過跨軌跡的經驗共享，Agent 不再需要從零開始摸索每一條路徑，而是能從多個平行嘗試中快速歸納出最佳策略。這種設計特別適合解決需要大量探索的複雜任務，解決了傳統 RL 訓練中常見的收斂慢與不穩定問題。

⚠️ **實驗環境與泛化能力待驗證**

目前論文主要聚焦在文字互動的虛擬環境 (ALFWorld, ScienceWorld)。雖然概念具備通用性，但該範式在更複雜的具身智能 (Embodied AI) 或多模態場景中的表現，以及並行環境的數量對性能的邊際效應，仍需進一步驗證。

🎯 **開源可用，強化學習 Agent 的新基線**

對於正在開發 LLM Agent 的開發者而言，DPEPO 提供了一個極具參考價值的技術路線。特別是當你的應用場景需要 Agent 具備強大的探索能力時，這種並行架構值得嘗試。好消息是，作者已經開源了完整程式碼，方便社群直接進行復現與二次開發。

🔗 **論文連結**
📝 DPEPO: Diverse Parallel Exploration Policy Optimization for LLM-based Agents
👤 Junshuo Zhang, Chengrui Huang, Feng Guo, Zihan Li, Ke Shi
🏫 University of Electronic Science and Technology of China; DiDi
🔗 論文：https://arxiv.org/abs/2604.24320
💻 開源程式碼：https://github.com/LePanda026/Code-for-DPEPO

你覺得這種「平行探索」的架構，還能應用在哪些 AI 應用場景？歡迎留言討論 👇

#LLM #Agent #ReinforcementLearning #AI研究 #開源 #電子科大 #滴滴 #DPEPO
