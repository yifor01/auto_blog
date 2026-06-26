---
title: Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory
  Signals Fix It
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.26027
score: 95
model: google/gemma-4-31b-it:free
generated_at: '2026-06-26T20:03:12.695479'
---

📌 解決多步驟工具使用崩潰：監督訊號如何穩定 RL 訓練？

TL;DR：透過交替使用 SFT 與 RL 的訓練策略，解決 LLM 在多步驟工具使用中容易發生的崩潰與格式敏感問題。

當我們嘗試讓 LLM 透過強化學習 (RL) 學習呼叫工具時，常會遇到一個棘手問題：模型在訓練過程中突然效能崩潰，或者對輸出格式變得極其敏感，導致原本能執行的工具呼叫失效。

🤔 **多步驟工具使用的訓練挑戰**

在執行需要多個步驟的工具使用任務時，模型面臨兩個核心痛點：
1. 災難性崩潰 (Catastrophic Collapse)：模型在 RL 過程中可能失去原有的能力或陷入錯誤的迴圈。
2. 格式敏感度 (Format Sensitivity)：模型對工具呼叫的特定格式要求過高，導致微小的格式偏差就導致任務失敗。

🧩 **交替訓練策略：SFT 與 RL 的協同作用**

為了提升穩定性與效能，研究提出了一套結合監督微調 (SFT) 與強化學習 (RL) 的訓練方法：

- 透過 interleaved (交替) 的訓練模式，將 SFT 提供的正確方向與 RL 的自我探索能力結合。
- 引入特定的監督訊號 (Supervisory Signals) 作為引導，防止模型在 RL 探索過程中偏離正確的工具呼叫路徑。

💡 **穩定性與效能的提升**

這種方法旨在解決單純依賴 RL 導致的不穩定性，透過監督訊號的介入，讓模型在學習「如何選擇工具」的同時，能維持正確的輸出格式，從而提高在複雜多步驟任務中的成功率。

🎯 **實務啟示**

對於開發 Agent 或工具呼叫系統的工程師，這項研究提醒我們：單純的 RL 探索在處理多步驟邏輯時風險較高。在訓練流程中加入適當的監督訊號，或採取 SFT 與 RL 交替的訓練路徑，能有效降低模型崩潰的風險並提高格式穩定性。

🔗 **來源**
- 標題：Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It
- 連結：https://huggingface.co/papers/2606.26027

#LLM #ReinforcementLearning #ToolUse #SFT #Agent #MachineLearning #AIStability #MultiStepReasoning #SupervisorySignals #HuggingFace
