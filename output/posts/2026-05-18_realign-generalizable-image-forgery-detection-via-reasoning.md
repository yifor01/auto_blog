---
title: "ReAlign: Generalizable Image Forgery Detection via Reasoning-Aligned Representation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.16080
score: 112
model: tencent/hy3-preview:free
generated_at: 2026-05-18T20:22:38.149971
---

📌 【Peking University & SCUT 最新研究】ReAlign：用「推理文字」輕量化偵測 AI 偽圖  

你以為偵測 AI 生成圖像只要看畫素異常就夠？研究顯示，單靠低層特徵或純語言模型都有盲點。  

🤔 **AI 偽圖偵測需同時兼顧低層瑕疵與語義理解**  
隨著 AIGI（AI‑Generated Image）品質日益提高，傳統非 LLM 偵測器雖能快速捕捉畫素層級的偽造痕跡，但缺乏語義層面的判斷；純 LLM 型方法則擁有強大的語義推理與可解釋性，卻運算量大且對細微視覺 artefuct 敏感度不足。這種「低層 vs 高層」的兩極現象，使得現有偵測器在面對高保真偽造時往往難以兼顧準確度與效率。  

🧪 **以 GRPO‑優化 LLM 蒸餾推理文字，透過對比學習得到輕量偵測器**  
研究團隊首先讓一經 GRPO（Generative Reward Policy Optimization）優化的大型語言模型針對圖像生成產出高品質的推理文字（說明為何某圖屬於偽造）。接著，他們採用對比學習將這些推理文字的語義表示蒸餾到一個輕量的圖像編碼器中，使偵測器同時繼承推理文字的語義敏感度與泛化能力。最後，採用聯合優化策略：一端使用對比 loss 使圖像與其對應推理文字在特徵空間對齊；另端使用分類 loss 直接優化偽造/真實的二分類決策。實驗在三個基準資料集上進行：AIGCDetectBenchmark、AIGI-Holmes，以及團隊自行建構的 UltraSynth-10k（涵蓋較新、高保真的生成模型）。  

🚀 **ReAlign 在準確度與泛化能力上持續優於現有 SOTA**  
結果顯示，ReAlign 在所有三個基準上的偵測準確率均顯著高於既有的非 LLM 與 LLM 型方法；尤其在 UltraSynth-10k 複雜、高保真的偽造樣本上，優勢更為明顯，表明其所學到的推理表示確實提升了對未見過生成模型的泛化能力。  

💡 **推理文字提供語義「錯誤敏感度」，彌補低層特徵的盲點**  
進一步分析顯示，ReAlign 的優勢來自於它能同時捕捉：  
1. 低層畫素層級的不一致（傳統方法強項）  
2. 高層語義層級的矛盾（例如物理不可能的光影、不合理的物體關係）  
這種「語義對齊」的表示使得偵測器不僅對已知偽造手法敏感，也能在面對新型生成模型時保持較低的誤報率。  

⚠️ **僅在三個基準測試上驗證，需進一步在更多真實場景中檢驗**  
論文未提供更大規模的跨平台或實時間部署的效能評估，亦未詳細探討不同 GRPO‑優化 LLM 的選擇對最終偵測器的影響。因此，將 ReAlign 應用於多樣化的線上內容審核系統前，仍需進行更廣泛的真實世界測試。  

🎯 **工程師可直接採用的輕量偵測方案，適合數位真實性防護**  
- ReAlign 透過蒸餾保持模型輕巧，適合邊緣設備或雲端批次處理。  
- 其結合低層與高層線索的特性，使得在面對日益逼真的 AIGI 時，能提供較穩定的偵測表現。  
- 對於已有 LLM 推理管線的團隊，可將產出的推理文字直接當作額外的訓練信號，無需重新設計複雜的多模態架構。  

🔗 **論文連結**  
📝 ReAlign: Generalizable Image Forgery Detection via Reasoning-Aligned Representation  
👤 Qing Huang, Zhipei Xu, Xuanyu Zhang, Xiangyu Yu, Jian Zhang  
🏫 Peking University; South China University of Technology  
🔗 https://arxiv.org/abs/2605.16080  

你在偵測 AI 偽圖時，是否也曾感到「看圖不如看說明」的直覺？歡迎在留言區分享你的經驗或對此類 multimodal 偵測方法的看法 👇  

#AI #ImageForgeryDetection #MultimodalLearning #ReAlign #PekingUniversity #SCUT #AIGC #DigitalAuthenticity #CVPR2026
