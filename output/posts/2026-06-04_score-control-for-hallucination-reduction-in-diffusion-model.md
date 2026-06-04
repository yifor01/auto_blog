---
title: Score-Control for Hallucination Reduction in Diffusion Models
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.00377
score: 90
model: tencent/hy3-preview:free
generated_at: '2026-06-04T21:09:36.670139'
---

📌 **Score-Control for Hallucination Reduction in Diffusion Models**  
*Variance‑Guided Score Modulation 平滑分數函式，降低幻覺而不犧牲圖像品質*

你是否曾見過擴散模型生出「合理但錯誤」的細節？這種幻覺（hallucination）在圖像生成任務中一直是工程師們需要權衡的痛點——提升創意往往伴隨著不真實的 artefactual 元素。  

🤔 **當創意遇上可信度：擴散模型的幻覺挑戰**  
擴散模型透過逐步去噪產生高保真圖像，但其得分函式（score function）在高曲率區域容易產生過度尖銳的梯度，導致模型在去噪過程中「想象」出不存在的結構。過去的解決方案多半依賴於後處理、增加採樣步數或犧牲多樣性來抑制幻覺，卻常伴隨圖像細節的流失或生成速度的下降。  

🧪 **Variance-Guided Score Modulation：透過雅可比矩控制得分函式平滑度**  
論文提出的一個新思路是直接調控得分函式的局部平滑度。具體而言，它利用得分函式對輸入的雅可比矩陣（Jacobian）來估計局部變異（variance），然後根據這個變異值對得分函式進行縮放調制。這樣的設計使得在得分函式過於不平滑（高變異）的區域上施加較強的抑制，而在平坦區域則保持原始梯度，從而在不顯著影響整體去噪軌跡的前提下，降低產生不真實細節的機率。  

🔬 **核心發現：幻覺減少，圖像品質持平**  
根據論文的實驗報告，該方法在多個標準擴散模型基準上觀測到幻覺指標的明顯下降，同時在常用的圖像品質度量（如 FID、IS）上未見顯著劣化。也就是說，透過雅可比導向的變異調制，模型能在保持生成圖像真實感與多樣性的前提下，減少不實際的生成 artefactual。  

💡 **深入分析：為何雅可比調制能同時兼顧品質與可靠性**  
得分函式的雅可比矩陣反映了模型對輸入微小擾動的敏感度。當該敏感度過高時，微小的噪聲會被放大，導致後續去噪步驟產生偏離真實數據分布的軌跡——也就是我們所感知的幻覺。透過根據雅可比的變異值對得分函式進行縮放，實際上是在對模型的局部 Lipschitz 常數進行自適應約束，使得去噪過程更加穩健，而不需要改變全局的噪聲排程或增加額外的網路參數。  

⚠️ **研究限制：僅憑摘要可見的資訊**  
目前公開的摘要未詳細說明實驗規模、使用的特定模型架構（如 UNet、DiT 等）、訓練資料集或是消融實驗的具體結果。因此，無法在此判斷該方法在不同擴散變體（例如潛在擴散、條件擴散）或極端高解析度場景下的表現。完整的限制與適用條件仍需參考論文全文。  

🎯 **實務啟示：一種可直接插入的得分函式調制技巧**  
對於已經在 production 中部署擴散模型的團隊來說，此方法提供了一種不需重新訓練或大幅修改推理管線的選項：只需在得分函式的計算步驟中加入雅可比導向的變異調制模組，即可嘗試降低幻覺而不顯著影響生成速度或圖像保真度。若作者後續開放原始碼，將進一步降低實驗門檻，使得社群能快速在自家的 Stable Diffusion、DALL·E 等變體上驗證其效果。  

🔗 **論文連結**  
📝 Score-Control for Hallucination Reduction in Diffusion Models  
👤 作者／機構：未在摘要中顯示  
🔗 https://huggingface.co/papers/2606.00377  

你有在專案中遇過擴散模型的幻覺問題嗎？歡迎在留言區分享你的經驗或對此類得分函式調制方法的看法 👇  

#AI #DiffusionModels #Hallucination #ScoreFunction #GenerativeAI #MachineLearning #HuggingFace #深度學習 #圖像生成 #技術分享
