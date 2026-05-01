---
title: "AesRM: Improving Video Aesthetics with Expert-Level Feedback"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2604.28078
score: 123
model: tencent/hy3-preview:free
generated_at: 2026-05-01T19:37:34.547895
---

📌 【港大 & 阿里】用專家級框架拆解視訊美學：AI 生成的畫面，終於不只是「像」，還要「美」

當前的 AI 視訊已經能畫出逼真的人臉與場景，但在電影與廣告等真實應用中，和諧的色調、電影級光影、恰到好處的構圖，往往比「像不像」更重要。現有研究多半從圖像出發，把美學簡單定義為「視覺愉悅」，缺乏系統性的評估與訓練方案。

🤔 **視訊美學不只是「好看」，而是可拆解、可訓練的技術問題**

視訊美學長期被當作模糊的直覺判斷，導致模型優化時缺乏穩定目標。若無法精準評價何謂「好的構圖、光影與色調一致性」，後訓練與對齊便容易陷入指標失真或過度擬合。

🧪 **三維度、十五細則、2500 組專家標註的對照實驗**

研究團隊提出層次化評估框架，將視訊美學拆解為視覺美學（VA）、視覺真實度（VF）與視覺合理性（VP），並細化出十五項具體評分準則（如構圖、燈光、動態一致性）。以此建構 AesVideo-Bench，包含約 2500 組視訊對與專家偏好標註，作為評估與訓練基礎。

☑️ **AesRM 勝出基線，位置偏差更低，在多項美學基準表現更穩定**

- AesRM-Base 直接預測成對偏好，提供高效後訓練獎勵訊號
- AesRM-CoT 額外生成可解釋的思維鏈（CoT），對齊全部十五項準則
- 經三階段訓練（單元美學能力學習、冷啟動對齊、GRPO 優化）後，評估準確率與魯棒性明顯提升
- 位置偏差較低，評價結果不易受影片順序干擾

💡 **用 CoT 解釋美學決策，讓模型「知道為什麼這樣評分」**

AesRM-CoT 引進自我一致性驗證的思維鏈合成方式，並在 GRPO 中設計基於 CoT 的過程獎勵。這使模型不僅能判斷「哪支視訊較好」，還能依據具體準則說明原因，讓後訓緩對齊過程更透明、可控。

⚠️ **專家標註成本與場景廣度仍有限，長期對齊效果待驗證**

目前評估與訓練高度依賴專家標註，擴展成本較高；資料與任務多樣性仍以現有範疇為主，長期對模型生成品質與泛化能力的影響，尚需更多跨場景驗證。

🎯 **後訓練與對齊可直接落地，AesRM 為視訊 GenAI 提供穩定目標**

- 開放評估基準與訓練流程，適合用於視訊模型的 RLHF 與後訓練
- 已實驗性對齊 Wan2.2，顯示出比現有美學獎勵模型更明顯的視覺提升
- 開發者可依據十五項準則設計更精細的優化目標與評估檢查點

🔗 **論文連結**  
📝 AesRM: Improving Video Aesthetics with Expert-Level Feedback  
👤 Yujin Han, Yujie Wei, Yefei He, Xinyu Liu, Tianle Li  
🏫 The University of Hong Kong; Fudan University; Zhejiang University; HKUST; University of Sydney; Alibaba Group  
🔗 論文：arxiv.org/abs/2604.28078  

你的團隊在視訊生成後訓練時，最在意哪一項美學準則？歡迎留言討論 👇  

#AI #VideoGeneration #Aesthetics #RLHF #GenAI #CVPR #後訓練 #模型對齊
