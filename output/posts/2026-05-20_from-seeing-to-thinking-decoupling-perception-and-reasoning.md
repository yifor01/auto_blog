---
title: "From Seeing to Thinking: Decoupling Perception and Reasoning Improves Post-Training of Vision-Language Models"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.20177
score: 111
model: tencent/hy3-preview:free
generated_at: 2026-05-20T21:05:45.880611
---

📌 【Amazon 等最新研究】從「看」到「想」：把視覺感知與推理分開訓練，讓 VLM 更準又更簡潔  

你以為提升視覺語言模型的推理能力，只需要讓它「想」得更久、鏈條更長？其實問題可能出在「看」得不夠清楚。  

🤔 **視覺感知是瓶頸，而非推理本身**  
近期 VLM 的進步常著重於長鏈條思考，但作者發現，視覺任務的表現主要受限於感知能力的不足，而非推理本身。若感知不夠穩固，再多的推理也只是在彌補缺失的視覺資訊。  

🧪 **分階段訓練：先固定感知，再訓練推理**  
研究把 VLM 的後訓練切成三個階段——視覺感知、視覺推理、文字推理——並為每個階段使用專門的資料。這種「能力為基礎的課程」與傳統以難度為基礎的課程正交，可獨立或併用。  

 **分階段訓練讓推理準確度提升 1.5%，思考鏈縮短 20.8%**  
與傳統合併訓練相比，分階段訓練在多個開放權重 VLM 上同時提升視覺感知與視覺推理表現。具體來說，推理準確度提高 1.5%，同時推理鏈長度平均縮短 20.8%，表示更好的感知減少了對冗長推理的需求。  

 **感知透過強化學習學得比圖像說明更好，且為後續推理奠定基礎**  
進一步分析顯示：視覺感知需要針對性的優化，且在強化學習（RL）下學習效果優於以圖像說明為基礎的監督微調（SFT）。當感知階段先鞏固後，視覺推理階段才能在堅實的感知基礎上進行，從而獲得更高的準確度與更簡潔的推理過程。  

⚠️ **僅在開放權重模型上驗證，未涉及閉源巨模或真實場景延伸**  
實驗主要在數個開放權重 VLM 上進行，樣本與任務範圍有限；是否同樣適用於更大規模的閉源模型或複雜的實際應用，仍需後續研究驗證。  

🎯 **後續 VLM 後訓練可採用感知先行的課程，搭配難度課程可獲得加成**  
對工程師來說，這項研究提供了一個可直接採用的訓練策略：在後訓練階段先以專門的感知資料進行強化學習，再進行視覺推理與文字推理的階段訓練。若同時納入傳統的難度課程，可獲得額外的加成效果。在公開基準上，此策略已在 WeMath 上提升 5.2%、在 RealWorldQA 上提升 3.7%。  

🔗 **論文連結**  
📝 From Seeing to Thinking: Decoupling Perception and Reasoning Improves Post-Training of Vision-Language Models  
👤 Juncheng Wu, Hardy Chen, Haoqin Tu, Xianfeng Tang, Freda Shi (Amazon; UC Santa Cruz; University of Waterloo; Vector Institute)  
🔗 https://arxiv.org/abs/2605.20177  

你在微調 VLM 時，是否曾經把「看」和「想」混在一起訓練？試著把感知先鞏固，看看準備度與效率會不會有意外的提升？歡迎在留言區分享你的經驗或疑問 👇  

#AI #VisionLanguageModel #VLM #PostTraining #ReinforcementLearning #AmazonResearch #機器學習 #深度學습
