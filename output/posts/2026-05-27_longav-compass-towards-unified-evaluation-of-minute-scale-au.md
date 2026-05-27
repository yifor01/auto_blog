---
title: "LongAV-Compass: Towards Unified Evaluation of Minute-Scale Audio-Visual Generation Across T2AV, I2AV, and V2AV"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.26244
score: 83
model: tencent/hy3-preview:free
generated_at: 2026-05-27T21:30:54.861540
---

📌 **LongAV-Compass：統一評估分鐘級音視訊生成的新基準**

你是否曾好奇，現在的 AI 能否生成一分鐘長、畫聲同步的影片？現有評估方式可能都在短片上打轉，缺乏對長時間序列的可靠度量。

🤔 **長時程音視訊生成亟需統一尺度**

隨著文生AV（T2AV）、圖生AV（I2AV）與影生AV（V2AV）模型不斷進步，研究社群發現現有評估指標多聚焦於數秒級片段，難以反映模型在延伸時間維度上的品質、一致性與跨模態對齊表現。這導致模型間的比較缺乏共同參考基準。

🧪 **提出跨模態、長時程的評估框架**

LongAV-Compass 為一個綜合基準，專門設計用於測評分鐘級的音視訊生成。它同時涵蓋文字→AV、圖像→AV 與影片→AV 三種任務，透過一套統一的度量方式來考量生成結果的品質、時間內部一致性以及音訊與視訊的對齊度。

🔍 **提供品質、一致性與對齊的多維度量測**

該基準的核心貢獻在於提出一組適用於長時序的評估指標，使研究者能在相同的尺度下比較不同模型在延伸時間窗口上的表現。這樣的設計旨在填補目前長時程音視訊生成評估的空白，為後續模型改進提供可量化的回饋。

⚠️ **依賴隨後公開的程式碼與資料集，實際推廣尚待觀察**

儘管 LongAV-Compass 在概念上提供了統一的評估工具，但其實際採用程度仍取決於隨後是否會開放相關的程式碼與基準資料集。此外，基準目前主要聚焦於品質、一致性與對齊三個面向，其他潛在維度（例如創意度或敘事連貫性）尚未納入考量。

🎯 **研究者可直接用來進行跨模態、長時程模型比較**

- 將新提出的 T2AV、I2AV 或 V2AV 模型放入同一基準下進行評估。  
- 透過品質與一致性分數快速識別模型在長時序生成上的優勢與不足。  
- 作為未來模型改進的參考點，特別是當目標是生成分鐘級以上的連貫音視訊內容時。

🔗 **論文連結**  
📝 LongAV-Compass: Towards Unified Evaluation of Minute-Scale Audio-Visual Generation Across T2AV, I2AV, and V2AV  
🔗 https://huggingface.co/papers/2605.26244  

你認為這樣的長時程評估基準會成為音視訊生成領域的新標準嗎？歡迎在留言區分享你的看法 👇

#AI #AudioVisualGeneration #Benchmark #Multimodal #T2AV #I2AV #V2AV #HuggingFace #研究工具
