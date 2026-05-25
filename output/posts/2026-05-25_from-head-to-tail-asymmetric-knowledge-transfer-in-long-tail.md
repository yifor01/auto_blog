---
title: "From Head to Tail: Asymmetric Knowledge Transfer in Long-tail Recommendation with Generative Semantic IDs"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.23310
score: 119
model: tencent/hy3-preview:free
generated_at: 2026-05-25T20:29:22.654452
---

📌 【阿里巴巴】From Head to Tail：語義ID提升長尾推薦  

隨著電商平台商品種類爆炸，頭部商品擁有豐富行為數據，而尾部商品卻因樣本稀少難以建立有效表示。傳統方法常嘗試把多模態特徵與協同訊號結合，卻忽略了一個關鍵事實：尾部的雜訊反而會損害頭部表示的學習。  

🤔 **你以為更多數據就能解決長尾問題？實際上，尾部雜訊反而會傷害頭部表現**  

這種非對稱的知識傳輸問題促使研究者思考：是否能讓頭部的穩定知識安全地流向尾部，同時避免尾部噪聲回流？  

🧪 **基於多模態LLM生成語義ID的端到端框架**  

AKT‑Rec 首先使用經監督微調的多模態LLM（MLLM）將商品和使用者的內容特徵與協同訊號對齊，得到連續的語義表示。接著透過Residual‑Quantized VAE（RQ‑VAE）將這些表示離散化為語義ID，形成語義聚類。  

🔑 **Cluster‑Guide適應性嵌入與非對比對齊**  
該框架把每個ID的表示分解為聚類級嵌入（捕捉共享語義）與個體嵌入。透過非對比對比目標和活動感知的門控機制，知識被有方向地從頭部ID傳遞至尾部ID，而尾部的噪聲被門控機制抑制。  

🔗 **階層特徵聚合與自適應融合**  
為了應對不同活動程度的樣本，AKT‑Rec 建立平行的特徵視圖，並依樣本活動度自適應地融合這些視圖，以優化預測。  

📈 **離線指標顯著提升，線上實驗驗證產業價值**  
在大規模工業數據集上的離線實驗顯示，AKT‑Rec 使AUC提升0.35%，GAUC提升1.53%，優過多個基線。在阿里巴巴Tmall平台的線上A/B測試中，CTR提升2.76%，GMV提升3.47%，說明該方法在真實生產環境中具有顯著商業價值。  

💡 **知識傳輸的非對稱性是關鍵設計**  
研究指出，頭部商品的表示較為穩定且富含協同訊號，適合作為知識來源；尾部商品則容易受樣本稀少導致的噪聲影響。透過聚類級嵌入捕捉共享語義，並讓門控機制依據活動度調整頭部知識對尾部的貢獻，模型得以在保護頭部品質的同時，提升尾部的表示質量。  

⚠️ **需多模態LLM微調與RQ‑VAE，實作複雜度較高**  
評論中指出，AKT‑Rec 的實現依賴於對多模態LLM進行監督微調以及使用Residual‑Quantized VAE，這在工程落地時會增加訓練資源與模型部署的開銷。  

🎯 **對工程師的啟示：以語義ID為橋樑，非對稱傳輸可平衡頭尾表現**  
- 在長尾場景中，先利用頭部的穩定訊號建立語義聚類，再透過非對比目標將知識方向性地導向尾部。  
- 活動感知門控可自適應抑制尾部噪聲對頭部的回流，提升整體穩定性。  
- 若資源允許，投入多模態LLM的微調與RQ‑VAE構建將是提升尾部商品表示的有效途徑。  

🔗 **論文連結**  
📝 From Head to Tail: Asymmetric Knowledge Transfer in Long-tail Recommendation with Generative Semantic IDs  
👤 Chenyi Yan, Ruocong Tang, Xing Fang, Yang Huang, He Guo @ Alibaba Group; Beijing University  
🔗 論文：https://arxiv.org/abs/2605.23310  

你在處理長尾推薦時，是否也嘗試過利用頭部知識來補強尾部？歡迎在留言區分享你的經驗與思考 👇  

#AI #推薦系統 #長尾問題 #語義ID #多模態LLM #阿里巴巴 #CTR #GMV #機器學習 #産業應用
