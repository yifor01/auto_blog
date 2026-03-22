---
title: "Beyond Sequential Distance: Inter-Modal Distance Invariant Position Encoding"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.10863
score: 120
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-12T18:54:41.280647
---

📌 【MLLM 長上下文視覺衰退】創新 DIPE 讓 AI 看圖說故事更穩定

隨著多模態大語言模型 (MLLM) 越來越成熟，AI 看圖說故事的能力讓人驚艷。但你知道嗎？當文字敘述變長時，AI 對圖片的理解能力會逐漸「視覺衰退」。

🤔 **為什麼 AI 看長圖會「視覺衰退」？**

當你給 AI 一張圖片加上長篇文字時，它會優先關注文字，圖片的訊號會隨著文字長度增加而逐漸被邊緣化。這是因為多模態模型的注意力機制，會隨著圖文距離增加而自然衰減。

🧪 **傳統 Multimodal RoPE 的致命缺陷**

現有的 Multimodal Rotary Position Encoding (RoPE) 會對「圖文距離」進行懲罰。也就是說，當圖片 token 與文字 token 距離越遠，AI 對圖片的注意力就越低，導致視覺訊號在長上下文中逐漸消失。

💡 **DIPE：距離不變的位置編碼**

來自 MAIS、CASIA、UCAS 和騰訊雲元團隊的研究者提出 Inter-Modal Distance Invariant Position Encoding (DIPE)，核心創新在於：

- **區分處理**：對「圖對圖」和「文對文」的注意力，保持原有的距離感知
- **固定視覺錨點**：對「圖對文」的注意力，無論距離多遠，都保持一致的感知強度

🎯 **為什麼這很重要？**

想像 AI 在分析醫學圖片時，需要同時理解長篇病歷和 X 光片。如果視覺衰退，AI 可能只關注文字描述而忽略了關鍵的影像訊號。DIPE 確保了在長篇敘述中，圖片訊號仍然能保持穩定的影響力。

📊 **實驗結果：視覺衰退大幅改善**

整合 DIPE 與 Multimodal RoPE 後，模型在長上下文場景下：
- 維持穩定的視覺錨定能力
- 顯著緩解視覺衰退問題
- 同時不影響標準短上下文任務的表現

🔗 **開源程式碼已釋出**

這項研究已經開源，包含完整的實作程式碼：
https://github.com/lchen1019/DIPE

🎯 **實務啟示**

- 對於需要長文本理解的 MLLM 應用（如醫療診斷、文檔分析），DIPE 能確保視覺訊號不被邊緣化
- 這種「選擇性距離感知」的設計思路，未來可能應用在其他多模態場景

你的應用場景需要處理長篇圖文對話嗎？歡迎分享你的想法 👇

#AI #ComputerVision #Multimodal #PositionEncoding #MLLM #長上下文 #視覺理解 #科技研究

📝 Beyond Sequential Distance: Inter-Modal Distance Invariant Position Encoding
👤 Lin Chen, Bolin Ni, Qi Yang, Zili Wang, Kun Ding
🔗 論文：arxiv.org/abs/2603.10863
