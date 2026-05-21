---
title: "RankE: End-to-End Post-Training for Discrete Text-to-Image Generation with Decoder Co-Evolution"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.21195
score: 122
model: tencent/hy3-preview:free
generated_at: 2026-05-21T20:30:10.727337
---

📌 【Westlake University 等】RankE：離散 T2I 模型的端到端後訓練，解碼器共進化打破對齊‑保真度權衡  

你以為只調整「策略網路」就能讓 AI 畫圖更貼合提示？實際上，這種做法可能讓圖像品質悄悄下降。  

🤔 **政策優化獨自進行時，隱藏的分佈漂移悄悄毀掉圖像品質**  
現有的離散自回歸（AR）文字到圖像模型通常只在後訓練階段更新 AR policy，而將 VQ‑decoder 凍結。隨著 policy 不斷靠近人類偏好的分布，產生的 token 分布逐漸偏離 decoder 原本訓練時看到的 ground‑truth 分布，這種「Latent Covariate Shift」會讓獎勵分數（如 CLIP）上升，但解碼出的圖像在像素空間（FID）卻變差。  

🧪 **交替優化讓 policy 與 decoder 共同演化**  
RankE 提出端到端後訓練框架：在每一個訓練步中，先以 ranking‑based 對齊目標更新 policy，再以相同目標更新 decoder；每一方的更新都受到一個適合其參數空間的穩定性正則化（anchor）約束。這樣的共進化使得兩個模組能夠同步適應彼此的分布，避免單一方向的漂移。  

 **同時提升對齊與圖像品質，打破傳統權衡**  
在 LlamaGen‑XL（775M）上的實驗顯示：傳統 RL 僅提升 CLIP 分數，卻導致 FID 惡化；而 RankE 同時讓 FID 降至 15.21、CLIP 上升至 33.76（MS‑COCO 30K）。同樣的改善也在更大的 Janus‑Pro（1B）上得到驗證，說明 decoder co‑evolution 能可靠地將獎勵優化轉化為像素層面的品質提升。  

💡 **共進化機制的關鍵在於對抗分佈漂移**  
當 policy 改變時，decoder 若不跟進，會面臨「訓練時看到的 token 分布與當前產生的 token 分布不匹配」的問題，導致解碼錯誤。RankE 透過交替更新，使得 decoder 持續看到 policy 產出的最新 token 分布，從而在對齊目標的驅動下保持解碼器的忠實度。正則化 anchor 則防止過度漂移，確保兩個模組在參數空間內保持相對穩定。  

⚠️ **僅在特定模型與資集上驗證，泛化性尚需更多證據**  
本研究主要在 LlamaGen‑XL 與 Janus‑Pro 兩個離散 AR 模型上進行，並以 MS‑COCO 30K 子集評估。不同 tokenizer、更大規模的模型或其他圖像基準（如 LAION）上的表現尚未報告，且 anchor 正則化的超參數敏感度也待後續工作進一步探討。  

🎯 **實務上可直接將 decoder 加入後訓練迴路**  
對於正在使用離散 AR T2I 模型的團隊，RankE 提供一個可插拔的訓練流程：在原本的 policy 優化步驟後，加入 decoder 的 ranking‑based 更新與穩定性正則化。這樣不僅能避免「獎勵升圖像降」的困境，還能在不額外增加推論開銷的情況下獲得更好的生成品質。  

🔗 **論文連結**  
📝 RankE: End-to-End Post-Training for Discrete Text-to-Image Generation with Decoder Co-Evolution  
👤 Siyong Jian, Siyuan Li, Luyuan Zhang, Zedong Wang, Xin Jin  
🏫 Westlake University; Zhejiang University; Tsinghua University; Hong Kong University of Science and Technology; Shanghai AI Lab  
🔗 https://arxiv.org/abs/2605.21195  

你的後訓練流程是否只在調整 policy？是否該考慮讓 decoder 一起演化？歡迎在留言區分享你的經驗與看法 👇  

#AI #TextToImage #Diffusion #RankE #WestlakeUniversity #ZhejiangUniversity #Tsinghua #HKUST #ShanghaiAILab #MachineLearning #GenerativeModels
