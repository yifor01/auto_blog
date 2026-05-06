---
title: "Self-Improvement for Fast, High-Quality Plan Generation"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.03625
score: 112
model: tencent/hy3-preview:free
generated_at: 2026-05-06T20:16:12.619198
---

📌 【Amazon 最新研究】用自我改進機制，讓 AI 規劃又快又準

傳統規劃演算法通常面臨兩難：要麼追求最優解但計算時間爆炸，要麼快速生成但品質參差不齊。Amazon 團隊提出了一種結合生成式模型與自我改進的新框架，試圖打破這個僵局。

🤔 **AI 規劃不只求「可行」，更要追求「高品質」**

在自動規劃（Automated Planning）領域，過去的生成式模型多專注於找到「任何一個有效的計畫」，而非「最佳計畫」。然而，在物流調度或機器人路徑規劃中，計畫的長度與效率直接影響成本。Amazon 這篇論文的核心在於解決一個計算困難的問題：如何在次指數時間（sub-exponential time）內生成高品質的計畫。

🧪 **結合 Decoder-only Transformer 與圖形搜尋的迭代訓練**

研究團隊設計了一個自我改進（Self-Improvement）循環。首先，他們使用一個 Decoder-only Transformer 作為基礎模型。接著，每一輪改進都結合了多次模型推論與圖形搜尋（Graph Search），利用這些搜尋結果生成更高品質的計畫數據，再用這些數據對模型進行微調（Fine-tuning）。

 **平均縮短 30% 計畫長度，超過 80% 達到最優解**

在 Blocksworld、Logistics、Labyrinth 和 Sokoban 四個經典領域的實驗中，該模型展現了驚人的效率：
- 相較於源頭的符號規劃器，計畫長度平均減少了 30%。
- 在已知最優解的情況下，模型生成的計畫有超過 80% 達到了最優。
- 關鍵在於，模型的延遲（Latency）呈現次指數級擴展，這遠優於傳統的滿意型（satisficing）或最優型（optimal）符號規劃器。

💡 **自我改進是提升品質的關鍵加速器**

研究發現，僅僅依靠次優數據訓練的模型有其天花板。透過「模型生成 + 搜尋驗證 + 數據回饋」的閉環，模型能夠逐步修正自身的規劃策略。此外，配合推理時搜尋（Inference-time search），計畫品質還能進一步提升。

⚠️ **目前僅驗證於標準規劃領域，泛化極限待考驗**

雖然實驗結果亮眼，但目前的測試範圍仍侷限於學術界常見的標準規劃領域（如 Sokoban 等）。對於真實世界更複雜、動態的開放式場景，這種自我改進機制的穩定性與擴展性仍需進一步驗證。

🎯 **生成式模型不僅是「生成」，更是「優化」的工具**

這項研究對 GenAI 工程師的啟示在於：生成式模型不應只被視為模仿數據的分布，結合符號搜尋的自我改進機制，能讓模型在複雜推理任務中實現超越傳統演算法的效能。對於需要高品質決策的應用場景，這套 Fine-tuning 與 Inference 策略極具參考價值。

🔗 **論文連結**
📝 Self-Improvement for Fast, High-Quality Plan Generation
👤 Robert Gieselmann, Henrike von Huelsen, Mihai Samson, Marie-Christine Meyer, Dariusz Piotrowski @ Amazon
🔗 https://arxiv.org/abs/2605.03625

你認為這種「自我改進」機制，未來有機會取代傳統的硬編碼規劃演算法嗎？歡迎在留言區討論 👇

#AI #AutomatedPlanning #MachineLearning #Amazon #Transformer #GenAI #人工智慧 #技術部落格
