---
title: "CAST: Modeling Visual State Transitions for Consistent Video Retrieval"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.08648
score: 113
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-11T00:01:56.288663
---

📌 【Google 最新研究】用 AI 讓影片接續更流暢，CAST 模型讓長篇故事敘述更連貫

隨著 TikTok、Reels 等短影音平台的興起，創作者正從製作零散片段轉向編排長篇敘事。但現有的影片檢索系統卻存在一個根本問題：它們只看當下畫面，不記得前面的故事，導致影片接續時常出現角色突然變臉、場景跳接不自然的狀況。

🤔 **AI 只看當下，忘了前面的故事**

現有的影片檢索模型在推理時是「上下文無感」的，只關注當前片段的局部語義匹配，忽略了畫面狀態和角色身份的一致性。這就像讓人看連續劇時，每 5 秒就忘記前面發生了什麼。

🧪 **CAST 模型：讓 AI 記住故事脈絡**

Google 與加州大學聖克魯茲分校、MIT 合作提出了 CAST (Context-Aware State Transition) 模型，這是一個輕量級、可插拔的適配器，能與多種預訓練的視覺語言嵌入空間兼容。

CAST 的核心創新在於：它透過預測一個「基於狀態的殘差更新 (Δ)」來建模視覺歷史，為潛在狀態演化引入明確的歸納偏置。簡單說，就是讓 AI 學會根據前面的畫面，預測下一幀應該是什麼樣子。

 **用 CAST，影片接續更連貫**

在 YouCook2、COIN 和 CrossTask 等多個標準基準測試中：

- 在 YouCook2 和 CrossTask 上性能顯著提升
- 在 COIN 上保持競爭力
- 在多種基礎骨幹模型上一致超越零樣本基準

更重要的是，CAST 能為黑盒影片生成候選（如 Veo）提供有用的重新排序信號，促進更具時間連貫性的延續。

💡 **為什麼這很重要？**

這項研究解決了視頻生成和檢索領域的一個核心挑戰：如何維持長時間的視覺一致性。對於敘事電影、教學影片、遊戲實況等需要連貫 storytelling 的應用場景，CAST 提供了一個實用的技術路徑。

⚠️ **研究限制與展望**

目前 CAST 主要聚焦於視覺狀態的轉移建模，未涵蓋語義層面的長期依賴。未來可探索如何結合多模態時序建模，進一步提升敘事的連貫性。

🎯 **實務啟示**

- 對於影片生成平台，CAST 可作為後處理階段的重新排序模組
- 對於影片檢索系統，可作為輕量級一致性檢查器
- 對於敘事設計，提供了一種結構化的視覺連貫性評估方法

🔗 **論文連結**
📝 CAST: Modeling Visual State Transitions for Consistent Video Retrieval
👤 Yanqing Liu, Yingcheng Liu, Fanghong Dong, Budianto Budianto, Cihang Xie
🏫 Google, UC Santa Cruz, MIT
🔗 arxiv.org/abs/2603.08648

你怎麼看待 AI 在影片創作中的一致性挑戰？歡迎分享你的想法 👇

#AI #ComputerVision #VideoGeneration #GoogleResearch #CVPR #MachineLearning #影音創作
