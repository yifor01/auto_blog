---
title: "Relit-LiVE: Relight Video by Jointly Learning Environment Video"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.06658
score: 122
model: tencent/hy3-preview:free
generated_at: 2026-05-08T19:57:28.296478
---

📌 【多機構聯合】Relit-LiVE：無需相機姿勢即可實現穩定視訊重光  

你以為只要分解出內在特徵就能隨意改變視訊光線？實際上這一步往往是失敗的根源，導致顏色變形、材質破壞與時間閃爍。  

🤔 **內在分解的不穩定性是現有重光方法的瓶頸**  
先前的做法先把視訊分解為內在場景表示（如反射率、法線），然後在新光照下進行前向渲染。然而，這一步在真實影片上極不可靠，常會產生扭曲的外觀、破壞的材質以及隨時間累積的瑕疵。  

🧪 **透過原始參考圖像與環境視訊聯合預測的擴散框架**  
Relit-LiVE 的核心是直接將未處理的參考圖像引入渲染流程，讓模型能補回內在表示中易遺失或被破壞的場景線索。同時提出一種「環境視訊預測」的聯合擴散過程：在同一次去噪中，既生成重光後的視訊，也輸出與每個機位對齊的逐幀環境圖。這樣的設計天然強化了幾何與光照的一致對齊，且不需要先知道每幀的相機姿勢。  

🚀 **Relit-LiVE 在合成與真實基準上均優於現有 SOTA，無需已知相機姿勢即可得到時間穩定、物理一致的結果**  
實驗顯示，該方法在多個合成與真實視訊重光基準上持續勝過既有的視訊重光與神經渲染技術。受益於聯合預測與參考圖像的補償，輸出的視訊在時間上更穩定、在物理上更一致，並支援動態光照與相機移動。  

💡 **原始參考圖像提供了內在表示易遺失的場景線索，使模型能保持幾何與光照的一致對齊**  
與僅靠內在表示的方法不同，Relit-LiVE 把真實圖像的細節（如邊紋、微小遮擋）直接帶入生成過程，從而減少了因分解錯誤導致的外觀異常與時間閃爍。這也讓框架自然擴展到場景級渲染、材質編輯、物體插入以及串流視訊重光等下游任務。  

⚠️ **目前僅在有限的數據集上驗證，長極長視訊及極端光照變化的穩定性仍需進一步探討**  
雖然在現有基準上表現優異，但論文未說明在極長時序或極端光照條件下的行為，且僅在特定合成與真實數據上進行了評估。  

🎯 **對於影片後期、AR/VR 及即時串流重光應用，該方法提供可直接使用的開源實作，降低對相機追蹤的依賴**  
工程師可透過開源程式碼（https://github.com/zhuxing0/Relit-LiVE）快速實作視訊重光，無需額外的相機姿勢估計管線，同時獲得材質編輯與物體插入等創作彈性。  

🔗 **論文連結**  
📝 Relit-LiVE: Relight Video by Jointly Learning Environment Video  
👤 Weiqing Xiao, Hong Li, Xiuyu Yang, Houyuan Chen, Wenyi Li (Nanjing University; BAAI; BUAA; Tsinghua University; HKUST; UCAS; HUST; CUHK-Shenzhen)  
🔗 論文：https://arxiv.org/abs/2605.06658  
💻 程式碼：https://github.com/zhuxing0/Relit-LiVE  

你在視訊後期或即時應用中是否也曾為光照一致性頭痛？歡迎在留言區分享你的經驗與想法 👇  

#AI #ComputerVision #VideoRelighting #DiffusionModel #NanjingUniversity #BAAI #Tsinghua #HKUST #OpenSource #ARVR
