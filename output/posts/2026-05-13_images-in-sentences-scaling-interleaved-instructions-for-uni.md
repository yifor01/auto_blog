---
title: "Images in Sentences: Scaling Interleaved Instructions for Unified Visual Generation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.12305
score: 110
model: tencent/hy3-preview:free
generated_at: 2026-05-13T20:36:57.659803
---

📌 **INSET：圖文混編生成模型**

你以為把圖片直接塞進文字序列就能解決複雜指令的圖像生成嗎？事實上，現有方法在長距離依賴上仍然吃力，導致多圖一致性與文字對齊隨著指令複雜度急劇下降。

🤔 **圖文分離造成長距離依賴瓶頸**  
現行多模態語言模型把圖像與文字視為兩種不同的 modality，生成時必須跨越較長的 token 距離才能把描述與視覺目標對齊。這種結構分離使得在交錯指令（圖文交替出現）時，模型難以保持精準的物件綁定。

🧪 **將圖像視為原生詞彙的統一架構**  
INSET 把視覺特徵直接嵌入文字序列對應的語義槽中，使圖像成為密集、富有表達性的語言 token。如此一來，Transformer 的局部上下文能夠自然捕捉圖文對應關係。為支撐訓練，團隊設計了一個可擴展的資料引擎，利用 VLM 與 LLM 從常規圖像與影片資料庫合成 1500 萬筆高品質交錯樣本，構建長距離的多圖指令序列。

🚀 **在複雜交錯基準上顯著領先**  
在 InterleaveBench 評估中，INSET 在多圖一致性與文字對齊兩項指標上均優於現有最佳方法。值得注意的是，隨著輸入指令複雜度的增加，性能差距會進一步擴大，顯示該方法在處理長距離依賴時具備更好的伸縮性。

🔍 **局部上下文是關鍵優勢**  
因為圖像被放置在與其語義位置相鄰的 token 位置，模型不需要透過多層注意力來跨越遙遠的距離來建立對應。這種設計讓 INSET 在處理「先描述物件，再在後續文字中指示修改」或「多輪圖文交替」的場景中，能更精準地保留物件身份與屬性。

⚠️ **依賴合成資料、基準限制**  
資料引擎雖能產生龐大樣本，但最終仍是經由 VLM/LLM 合成，可能引入合成偏差。此外，主要實驗僅在 InterleaveBench 上進行，尚未在更廣泛的真實世界交錯指令集合上驗證泛化能力。

🎯 **實務建議：將視覺 token 化納入未來模型設計**  
- 在構建多模態生成或編輯系統時，可考慮將圖像特徵直接當作可訓練的詞彙嵌入，以利用 Transformer 的局部特性。  
- 若資料來源受限，可參考其合成管線：先用 VLM 生成圖像說明，再用 LLM 擴展為長圖文序列，最後過濾品質。  
- 在評估新方法時，除了常規單圖生成基準，應加入交錯指令測試，以更完整反映模型在複雜上下文中的表現。

🔗 **論文連結**  
📝 Images in Sentences: Scaling Interleaved Instructions for Unified Visual Generation  
👤 Yabo Zhang, Kunchang Li, Dewei Zhou, Xinyu Huang, Xun Wang @ ByteDance Seed  
🔗 https://arxiv.org/abs/2605.12305  

你在使用 AI 圖像生成時，是否曾遇到「描述越多，圖片越亂」的問題？歡迎留言分享經驗 👇

#AI #ComputerVision #Multimodal #ByteDance #INSET #CVPR #生成模型 #圖文交替
