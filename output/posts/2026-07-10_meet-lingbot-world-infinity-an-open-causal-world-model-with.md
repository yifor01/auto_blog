---
title: 'Meet LingBot-World-Infinity: An Open Causal World Model With An Agentic Harness'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/09/meet-lingbot-world-infinity-an-open-causal-world-model-with-an-agentic-harness/
score: 103
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T07:58:14.716165'
---

📌 【螞蟻集團】LingBot-World-Infinity：用 MoBA Attention 解決世界模型「長程漂移」

TL;DR：螞蟻集團推出 14B 因果影片生成模型，透過 MoBA 遮罩解決長程漂移，實現可互動的世界模擬。

當 AI 世界模型試圖模擬長時段的互動時，常會陷入一個困境：隨著生成內容增加，模型反而過度依賴過去的上下文而喪失預測能力，導致視覺品質崩潰，這就是所謂的「長程漂移 (long-horizon drift)」。

🤔 **對抗漂移與延遲的互動式模擬器**

螞蟻集團的具身智慧部門 Robbyant 發表了 LingBot-World-Infinity (LingBot-World 2.0)，將其定位為一個因果影片生成模型 (Causal Video Generation Model)。它能根據使用者的動作流 (stream of user actions) 逐幀生成影片，讓每一幀的狀態僅依賴於過去的畫面與目前的輸入，從而將世界模型轉化為一個可互動的模擬器。

🧩 **MoBA Attention：解決過擬合的關鍵設計**

研究團隊發現，標準的自迴歸 (Autoregressive) 影片訓練使用 teacher forcing 遮罩時，模型在上下文增加後會產生依賴，而非真正預測未來，導致視覺品質下降。為了修正此問題，他們提出了 Mixture of Bidirectional and Autoregressive (MoBA) Attention Mask：

- **正規化機制**：在 teacher forcing 遮罩中加入一個雙向全注意力 (bidirectional full-attention) 區塊，作為正規化工具，防止過擬合並支援靈活的生成長度。
- **輸入處理**：
    - **相機位姿 (Camera Pose)**：使用 Plücker embeddings，透過適應性層正規化 (AdaLN) 注入。
    - **文本提示 (Text Prompt)**：以分塊 (chunk-wise) 方式透過 cross-attention 進入。
- **防止語義洩漏**：自迴歸元件以下三角模式處理背景與分塊提示，確保未來的語義不會向後洩漏；雙向元件則對接一個全域提示 (global prompt)。

📊 **模型規模與訓練流程**

- **模型尺寸**：主模型為 14B 參數；另提供 1.3B 的輕量化版本，可部署於單張 GPU。
- **預訓練**：使用修正流插值 (rectified-flow interpolation) 最佳化條件流匹配 (conditional flow-matching) 目標。
- **後訓練**：將多步驟的 Teacher 模型壓縮為少步驟的 Student 模型，並在長自捲動軌跡 (long self-rollout trajectories) 上應用 DMD 技術。

🎯 **實務啟示**

對於開發具身智慧 (Embodied AI) 的工程師而言，這項研究提醒我們：在設計自迴歸生成模型時，單純的 teacher forcing 可能導致模型在長序列中「偷懶」而過度依賴上下文。引入如 MoBA 這種混合遮罩機制，可以在保持因果預測能力的同時，透過雙向注意力提供必要的正規化，提升長時段生成的穩定性。

🔗 **來源**
- 標題：Meet LingBot-World-Infinity: An Open Causal World Model With An Agentic Harness
- 作者／機構：Asif Razzaq / MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/09/meet-lingbot-world-infinity-an-open-causal-world-model-with-an-agentic-harness/

#WorldModel #EmbodiedAI #VideoGeneration #CausalModeling #MoBA #AntGroup #DeepLearning #AttentionMechanism #FlowMatching #ComputerVision
