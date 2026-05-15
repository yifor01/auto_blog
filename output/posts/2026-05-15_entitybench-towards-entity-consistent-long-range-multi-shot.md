---
title: "EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.15199
score: 113
model: tencent/hy3-preview:free
generated_at: 2026-05-15T20:23:46.624313
---

📌 EntityBench：長片角色一致性基準  

你以擴散模型已能生成流暢的單鏡頭視訊，但把多個鏡頭串起來，角色、物件、場景是否真的能保持一致？現有評估常依賴簡單的提示集合，難以真正衡量長距離的一致性。  

🤔 長片生成需解決的不是畫質，而是角色在時間上的身份認同  
隨著多鏡頭視訊生成需求的增長，如何讓同一個角色、同樣的道具或場景在不同鏡頭中保持外觀與位置的一致，成為實用敘事生成的瓶頸。既有基準多獨立生成提示，缺乏對實體完整追蹤的標準化測量。  

🧪 從真實影集中萃取 140 集、2,491 鏡頭，建立實體排程與三層評估框架  
EntityBench 取材自實際敘事媒體，提供 140 個片段（共 2,491 鏡頭），並為每個鏡頭標註字元、物件與位置的出現排程。依照難度分為 easy/medium/hard 三個層級，最長可達 50 鏡頭，涵蓋 13 個跨鏡頭角色、8 個跨鏡頭場景與 22 個跨鏡頭物件，實體間隔最遠可達 48 鏡頭。評估採用三個支柱：單幀品質、提示遵循度與跨鏡頭一致性，並加入「保真門檻」——只有正確出現的實體才會計入跨鏡頭得分。  

📊 隨著間距增加，現有方法的一致性急遽下降；顯式記憶顯著提升角色保真度 (Cohen's d = +2.33)  
實驗顯示，現有生成模型在跨鏡頭實體一致性上會隨著實體再次出現的間距變長而明顯惡化。相比之下，EntityMem —— 一種在生成前將每個實體經驗證的視覺參數存入持久記憶庫的系統 —— 在所有評估方法中達到最高的角色保真度與出現率，效果大小為 Cohen's d = +2.33。  

💡 為什麼顯式記憶能打破一致性瓶頸？因為它在生成前就把每個實體的視覺參考固定在記憶庫中  
與僅依賴即時條件生成不同，EntityMem 在開始生成時已經為每個角色、物件與場景準備了穩定的視覺原型。這種「預先註冊」的方式減少了模型在長距離推斷中產生漂移的空間，從而提升了跨鏡頭的實體身份辨識。  

⚠️ 基準聚焦於特定類型的敘事媒體，且僅評估單一記憶架構，泛化能力仍待驗證  
EntityBench 的數據來源主要為特定類型的影集，未涵蓋所有可能的視訊風格或非敘事內容。此外，僅測試了 EntityMem 這種記憶設計，其他可能的記憶或耦合策略尚未在同一基準上進行比較。  

🎯 在開發長片生成系統時，優先考慮實體級的記憶機制，而非僅提升單幀生成品質  
若目標是製造可用於敘事、廣告或教育的多鏡頭視訊，設計應該在模型前端加入可更新的實體記憶庫，確保每個角色與物件在整個序列中都有可參考的視覺錨點。單纯提升單幀保真度無法解決跨鏡頭的一致性問題。  

🔗 論文連結  
📝 EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation  
👤 Ruozhen He, Meng Wei, Ziyan Yang, Vicente Ordonez (ByteDance; Rice University)  
🔗 https://arxiv.org/abs/2605.15199  
💻 Code & Data: https://github.com/Catherine-R-He/EntityBench/  

你目前的視訊生成流程是否已經實作了實體記憶？歡迎在留言區分享經驗或疑問 👇  

#AI #VideoGeneration #MultiShot #EntityConsistency #ByteDance #RiceUniversity #CVPR #MachineLearning #深度學習
