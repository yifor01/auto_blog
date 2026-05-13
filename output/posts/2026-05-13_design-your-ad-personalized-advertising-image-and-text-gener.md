---
title: "Design Your Ad: Personalized Advertising Image and Text Generation with Unified Autoregressive Models"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.12138
score: 100
model: tencent/hy3-preview:free
generated_at: 2026-05-13T20:51:22.930419
---

📌 【統一自回歸模型】一起生成廣告圖文  

你見過廣告圖片和文案是同一個模型一次產出的嗎？傳統做法分別訓練圖像和文字模型，卻忽略了它們之間的關聯。這篇研究提出一種端到端的方法，直接從使用者點擊行為中學習偏好，同時產出更真實的廣告內容。  

🤔 **統一自回歸框架讓圖文廣告一起生成**  
現有廣告生成管線通常依賴多個獨立模型，僅以平均點擊率（CTR）作為控制信號，缺乏跨模態感知。作者設計了 Uni-AdGen，單一自回歸架構同時輸出廣告圖像與文字，並透過前景感知模組與指令調校提升生成內容的寫實度。  

🧪 **從雜湊多模態點擊歷史中粗到細捕捉使用者偏好**  
為實現個性化，團隊在 Uni-AdGen 中加入粗到細的偏好理解模組。該模組能從噪聲多模態歷史點擊行為中提取使用者興趣，進而驅動個性化圖文廣告的生成。同時，他們構建了首個大規模個性化廣告圖文資料集 PAd1M，並提出 Product Background Similarity（PBS）指標作為訓練與評估的依據。  

 **在通用與個性化廣告生成上均優於基線**  
廣泛實驗顯示，Uni-AdGen 在一般廣告生成與個性化廣告生成兩個任務上，皆超越現有基線方法。這意味著統一模型不僅簡化管線，亦能在保持或提升生成品質的同時，更好地對應個別使用者的偏好。  

💡 **端到端設計減少模組間誤傳，偏好模組是關鍵貢獻**  
作者認為，將圖像與文字生成統一在單一自回歸框架中，可避免傳統管線中各模組獨立訓練導致的信息損失。此外，從雜湊點擊歷史中逐步細化使用者偏好的設計，使模型能在嘈雜真實數據中仍學得有用的訊號，這是實現真正個性化廣告的核心。  

⚠️ **實驗主要聚焦短期生成品質，長期使用效果尚未探討**  
現有評估侷限於生成圖文的寫實度與相關度指標，未涵蓋長期曝光對使用者點擊行為或購買轉換的影響。此外，資料集來源與實驗環境可能限制方法在其他電商場景的直接遷移。  

🎯 **對工程師的啟示：可直接採用開源實作，注意偏好數據的品質**  
- 專案已開放程式碼與資料集（https://github.com/JD-GenX/Uni-AdGen），可快速在多模態內容生成 pipeline 中試用。  
- 在實際部署時，建議投入資源清理與標註歷史點擊行為，以提升粗到細偏好模組的效能。  
- 若需評估個性化廣告的商業價值，應補充長期 A/B 測驗，觀察點擊率與轉換率的持續變化。  

🔗 **論文連結**  
📝 Design Your Ad: Personalized Advertising Image and Text Generation with Unified Autoregressive Models  
👤 Yexing Xu, Wei Feng, Shen Zhang, Haohan Wang, Yuxin Qin (Sun Yat‑Sen University; JD.COM; Northeastern University)  
🔗 論文：https://arxiv.org/abs/2605.12138  
💻 程式碼：https://github.com/JD-GenX/Uni-AdGen  

你是否曾嘗試讓同一個模型同時產出廣告圖片與文案？歡迎在留言區分享你的經驗或疑問 👇  

#AI #多模態 #廣告生成 #個性化推薦 #Uni-AdGen #JDGenX #電商技術
