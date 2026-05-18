---
title: "GenShield: Unified Detection and Artifact Correction for AI-Generated Images"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.16122
score: 120
model: tencent/hy3-preview:free
generated_at: 2026-05-18T20:15:15.846689
---

📌 **GenShield：偵測+修復 AI 生成圖像**  

你以為偵測 AI 偽圖就夠了？當偽圖變得逼真到肉眼難辨，僅靠標記是不夠的——我們還得把它修回真實樣子。  

🤔 **偵測技術進步卻留下修復空白**  
擴散模型讓 AI 生成圖像（AIGI）越來越寫實，假訊息、數位鑑識與內容審核面臨更大挑戰。儘管偵測方法已有顯著進步，但對被偵測出來且含有可見瑕疵的圖像進行修復、恢復真實外觀的研究仍然較少，且偵測與修復兩項任務很少被統一討論。  

🧪 **閉環自回歸框架與視覺鏈式思考課程學習**  
我們提出 GenShield，一種統一的自回歸框架，在同一個模型中同時完成可解釋的 AIGI 偵測與可控的瑕疵修復，從診斷到修復形成閉環，顯示兩任務間具有互相促進的關係。為實現多步驟的「診斷‑然後‑修復」過程，我們引入了基於視覺鏈式思考（Visual Chain‑of‑Thought）的課程學習策略，使模型能自行解釋每一步驟，並內建明確的停止準則。同時，我們構建了一個大規模的「瑕疵‑復原」配對資料集，並設計了一個統一的評估流程。  

🔺 **在修復與偵測基準上達到最先進表現**  
在我們建立的修復基準以及主流的 AIGI 偵測基準上進行的廣泛實驗顯示，GenShield 具備最先進的效能與良好的泛化能力。程式碼已於 GitHub 開放（https://github.com/zhipeixu/GenShield），便於工程師直接在深偽偵測與內容審核場景中使用。  

⚠️ **資料規模與實驗範圍為主要限制**  
目前的工作主要基於我們自行建構的 artefact‑restored 資料集，尚未在更多樣化的真實世界圖像上進行廣泛驗證；此外，研究聚焦於擴散模型生成的圖像，其他生成模型的適用性仍需進一步探討。  

🎯 **工程師可直接採用的統一偵測‑修復方案**  
- 在內容審核管線中，先使用 GenShield 進行偵測，隨即得到帶有解釋的修復結果，減少兩個獨立模型的部署成本。  
- Visual Chain‑of‑Thought 課程學習提供可視化的決策路徑，方便除錯與模型行為審計。  
- 開放原始碼與統一評估管線降低了重新實作的門檻，適合快速原型與產品化。  

🔗 **論文連結**  
📝 GenShield: Unified Detection and Artifact Correction for AI-Generated Images  
👤 Zhipei Xu, Xuanyu Zhang, Youmin Xu, Qing Huang, Shen Chen (Peking University; Tencent Youtu Lab)  
🔗 論文：https://arxiv.org/abs/2605.16122  
💻 程式碼：https://github.com/zhipeixu/GenShield  

你在處理 AI 生成圖像時，是偵測為主，還是也需要同步修復？歡迎在留言區分享你的經驗與看法 👇  

#AI #深偽偵測 #圖像修復 #ComputerVision #PekingUniversity #TencentYoutu #GenShield #內容審核 #AIGC
