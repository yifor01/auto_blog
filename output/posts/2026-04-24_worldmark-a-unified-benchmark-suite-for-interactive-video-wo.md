---
title: "WorldMark: A Unified Benchmark Suite for Interactive Video World Models"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2604.21686
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-04-24T19:49:21.455653
---

📌 **【Shanda AI 研究】WorldMark：統一互動式世界模型的評測標準**

Genie、YUME、Matrix-Game 等互動式影像世界模型正快速演進，但你知道它們到底誰更強嗎？目前的現狀是：各家都在自己的「私有場景」和「私有數據」上跑分，就像讓不同選手在完全不同的跑道上比賽，結果根本無法比較。

🤔 **互動式世界模型的「公說公有理」困境**

隨著 Genie、YUME 等模型在互動生成領域的突破，研究社群面臨一個嚴峻的評測危機。現有的公開基準雖然提供了軌跡誤差、美學評分等指標，但缺乏標準化的測試條件。由於不同模型的控制介面（Action Format）互異，且測試場景（Scenes）不統一，導致這些數據無法在跨模型間進行「蘋果對蘋果」的公平對比。

🧪 **500 個案例、統一 WASD 控制介面的標準化測試**

由 Shanda AI Research Tokyo、The University of Tokyo 等機構提出的 WorldMark，是首個專為互動式 Image-to-Video 世界模型設計的統一基準。研究團隊設計了三個核心模組來解決評測碎片化問題：

 **統一操作介面，實現跨模型公平對決**

WorldMark 的關鍵創新在於其「統一動作映射層」（Unified Action-Mapping Layer）。它將共用的 WASD 風格操作詞彙，自動翻譯成六個主流模型的原生控制格式。這意味著，所有模型現在都在「同一個場景、同一條軌跡」下運行，徹底消除了因輸入差異導致的評測偏差。

💡 **分層測試與模組化評估工具包**

WorldMark 提供了 500 個評估案例，涵蓋第一人稱與第三人稱視角，以及寫實與風格化場景，並依照難度分為三個等級（20-60秒）。此外，它還配備了模組化的評估工具包，專注於視覺質量、控制對齊度與世界一致性。設計上具備高度擴展性，研究人員可以隨時插入自己開發的新指標（Metrics），而不用重跑基礎數據。

🏟️ **World Model Arena：誰是真正的王者？**

除了離線指標，團隊同步推出了線上平台 **World Model Arena (warena.ai)**。這不僅是一個排行榜，更是一個讓所有人都能觀戰頂尖世界模型「同場競技」的介面。你可以直接觀察不同模型在面對相同操作指令時的即時反應，這比單看數據更有說服力。

⚠️ **目前聚焦 Image-to-Video，擴展性待觀察**

雖然 WorldMark 解決了標準化的痛點，但目前主要針對 Image-to-Video 類型的世界模型。對於更複雜的 Video-to-Video 或其他輸入格式的支援，可能還需要後續的版本迭代。此外，500 個案例雖具代表性，但在極端場景的覆蓋度上仍有持續擴充的空間。

🎯 **對於研究與工程選型的實務價值**

對於開發者而言，WorldMark 提供了一個客觀的選型依據。在開發新的互動應用（如遊戲生成、模擬環境）時，你可以直接參考 Arena 的表現來選擇最適合的基礎模型，而不用再花大量時間搭建自己的評測環境。

🔗 **論文連結**
📝 WorldMark: A Unified Benchmark Suite for Interactive Video World Models
👤 Xiaojie Xu, Zhengyuan Lin, Kang He, Yukang Feng, Xiaofeng Mao (Alaya Studio, Shanda AI Research Tokyo; The University of Tokyo; Shanghai Innovation Institute)
🔗 論文：https://arxiv.org/abs/2604.21686
🌐 線上平台：http://warena.ai

你覺得目前哪個世界模型最有可能在 Arena 中稱霸？歡迎在留言區分享你的觀察 👇

#AI #ComputerVision #WorldModels #GenAI #ShandaAI #Research #TechBlog #MachineLearning #VideoGeneration
