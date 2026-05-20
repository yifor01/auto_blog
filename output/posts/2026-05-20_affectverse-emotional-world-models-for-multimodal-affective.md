---
title: "AffectVerse: Emotional World Models for Multimodal Affective Computing"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.19950
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-05-20T21:07:45.806882
---

📌 **AffectVerse：讓模型學會「預測」情緒的變化**  

你以為情緒識別只要分析當下的聲音、畫面和文字就夠了？研究顯示，讓模型學會預測未來幾幀的情緒軌跡，才能在多模態情感計算上獲得實質提升。  

🤔 **靜態融合難以捕捉情緒動態**  
現有的多模態大語言模型（MLLM）多半把情感識別視為對完整音視頻‑文本輸入的靜態融合，情緒如何隨時間演變往往被隱藏在模型內部，缺乏顯式的動態建模。  

🧪 **在 Qwen2.5‑Omni 上加入 Emotion World Module**  
研究團隊在 Qwen2.5‑Omni 基礎上設計了 Emotion World Module（EWM），該模組僅在表示層面運作，無需額外動作標籤。EWM 包含三個子模組：  
1. **Cross‑Modal Temporal Imagination**：利用過去的 token，多步推演未來的視訊／音訊表示。  
2. **MAMA（Modality‑Aware Multi‑step Attention）Belief Aggregation**：將推測出的 token 壓縮為具模態感知的 belief token。  
3. **Belief Injection**：把這些 belief token 注入語言模型，供情緒推理使用。  
該設計把未來情緒的預測當作過去觀測的自監督信號：它不取代對歷史的建模，也不需要在推理時看到未見的訊號，而是迫使當前的 belief state 編碼出能預測後續情緒變化的過渡線索。  

📊 **九個基準測試上平均提升 2.57%**  
在九個公開的情感計算基準上，AffectVerse 比其他基線模型至少高出 2.57%。消融實驗顯示，時間想象、跨模態推演以及 belief 聚合三個部分的貢獻是可加性的，缺一不可。  

💡 **預測式 belief 狀態是實用的替代方案**  
結果表明，將短 horizon 的情感預測作為世界模型的一部分，能為多模態情感識別帶來穩定且可插拔的改進，無需重新設計整個架構。這種做法特別適合已經在使用 Qwen2.5‑Omni 系列的工程團隊，作為情感感知能力的實用補強。  

⚠️ **目前僅驗證短 horizon 預測，長期效果尚未探索**  
論文著重於短 horizon（幾幀到數秒）的情感預測，長期情感趨勢的建模能力尚未在實驗中檢驗。此外，改幅度雖然在多個基準上一致，但絕對值仍屬於 modest 提升，需視應用場景評估是否值得額外計算成本。  

🎯 **工程實務上的建議**  
- 若你的系統已經基於 Qwen2.5‑Omni，可直接採用 EWM 作為 plug‑and‑play 模組，提升情感推理的時間一致性。  
- 在資源受限的情境下，可先啟用 Cross‑Modal Temporal Imagination 與 MAMA Belief Aggregation，觀察是否能帶來足夠的增益。  
- 記住這一方法的核心是「讓目前的 belief 包含未來變化的線索」，因此在設計資料 pipeline 時，確保過去的多模態序列足以支援未來幾幀的預測。  

🔗 **論文連結**  
📝 AffectVerse: Emotional World Models for Multimodal Affective Computing  
👤 Bo Zhao, Fanghua Ye, Yixin Ji, Sicheng Zhao, Xiaojiang Peng (Great Bay University; Tencent; Tsinghua University; Shenzhen Technology University)  
🔗 https://arxiv.org/abs/2605.19950  

你是否也在嘗試讓模型「預見」使用者的情感變化？歡迎在留言區分享你的經驗或疑問 👇  

#AffectVerse #EmotionAI #MultimodalLLM #Qwen2.5 #AffectiveComputing #AIResearch #Tencent #GreatBayUniversity #TsinhuaUniversity #ShenzhenTechUniversity
