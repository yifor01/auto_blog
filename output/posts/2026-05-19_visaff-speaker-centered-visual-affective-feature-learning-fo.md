---
title: "VISAFF: Speaker-Centered Visual Affective Feature Learning for Emotion Recognition in Conversation"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.18547
score: 120
model: tencent/hy3-preview:free
generated_at: 2026-05-19T20:24:13.084142
---

📌 【ZJUT & ETH Zurich】VISAFF：說話者中心視覺情感學習  

你以為視覺模型只需要看臉就能辨情緒？實際上，對話中的情感線索往往藏在說話者的微表情與語音文字中，而現有大模型卻常被背景噪音分散。  

🤔 **對話情感辨識需要多模態，但視覺模型易被背景干擾**  
早期純文字方法無法捕捉諷刺等細微情感，因為它們忽略了非語言訊息。雖然視覺‑語言模型（VLM）能直接分析影像，但它們並未為對話情感辨識（ERC）量身設計，常聚焦於情緒無關的背景或被動聆聽者，且微調這類巨型模型的計算成本高昂。此外，單純的視覺訊號在缺乏語音與語言語境時，往往模糊或易受技術噪聲影響。  

🧪 **說話者聚焦與可靠性導向的兩階段框架**  
我們提出 VISAFF（Speaker‑Centered Visual Affective Feature Learning），分為兩個階段：  
1️⃣ **Speaker‑Centered Affective Grounding** – 利用免調校的方式，引導凍結的 VLM 聚焦於 active speaker 的情感視覺線索，避免大量額外訓練。  
2️⃣ **Reliability-Guided Affective Complementation** – 當視覺特徵的可信度降低時，動態引入文字與語音模態來補充不確定性，使情感表示更穩健。  

📌 **免調校下達到 SOTA 可比性能，並大幅降低運算成本**  
在兩個真實世界的對話資料集上的實驗顯示，VISAFF 在不進行任何微調的情況下，能與現有最佳方法達成可比的辨識表現；同時，因為省去了對大型 VLM 的昂貴微調過程，運算效率獲得顯著提升。  

💡 **以說話者為中心的視覺引導與多模態不確定性補償**  
核心思想是讓模型「知道誰在說話」以及「什麼時候視覺線索可靠」。第一階段透過設計的 grounding 機制，將 VLM 的注意力引向說話者的臉部與上半身微表情；第二階段則根據視覺特徵的可靠度指標，即時啟用文字與語音資訊來填補視覺上的缺口，這種互補設計使得系統在嘈雜或遮擋的對話環境中仍能保持較高的情感辨識準確度。  

⚠️ **僅在兩個真實資料集上驗證，長期穩定性與極端情境尚未探討**  
目前的實驗僅限於兩個公開的對話資料集，未涵蓋更長時間序列或極端情緒（如強烈憤怒、極度壓抑）的表現；此外，雖然方法是免調校的，但仍依賴於預訓練 VLM 的代表能力，不同 backbone 的泛化效果尚需進一步驗證。  

🎯 **適合資源受限的即時對話系統，可直接凍結 VLM 進行情感特徵提取**  
對於需要即時回應且計算資源有限的場景（如客服機器人、線上教育助理），VISAFF 提供了一種「 plug‑and-play 」的方案：使用現有的凍結 VLM，僅加入輕量的 grounding 與 complementation 模組，即可獲得與微調相近的情感辨識效果，同時大幅降低延遲與能源消耗。  

🔗 **論文連結**  
📝 VISAFF: Speaker-Centered Visual Affective Feature Learning for Emotion Recognition in Conversation  
👤 Linan ZHU, Zihao Zhai, Xiao Han, Yuqian Fu, Xiangfan Chen (Zhejiang University of Technology; ETH Zurich)  
🔗 https://arxiv.org/abs/2605.18547  
💻 程式碼：https://anonymous.4open.science/r/speaker-2365/  

你在開發多模態對話系統時，是否也曾為了效能犧牲模型解釋性？歡迎在留言區分享你的看法與經驗 👇  

#AI #EmotionRecognition #MultimodalLearning #VLM #ERC #ZJUT #ETHZurich #MachineLearning #對話系統 #視覺語言模型
