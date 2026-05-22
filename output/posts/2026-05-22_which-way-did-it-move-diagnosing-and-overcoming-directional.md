---
title: "Which Way Did It Move? Diagnosing and Overcoming Directional Motion Blindness in Video-LLMs"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.22823
score: 110
model: tencent/hy3-preview:free
generated_at: 2026-05-22T20:33:50.265268
---

📌 【Kyung Hee & Princeton 最新研究】Video-LLM 為何分不清左右？方向盲點診斷與解決方案  

你以為 Video-LLM 已經能理解影片中的運動方向？實際上，它在判斷單一物體左、右、上、下的運動時，表現幾乎就像隨機猜測。  

🤔 **方向盲點源於「讀出」階段的錯誤綁定**  
研究團隊發現，即使視覺編碼器、投影層以及 LLM 隱藏狀態中仍保存著線性可讀的運動方向資訊，模型卻無法將這個訊號正確地映射到對應的文字選項（“左”、“右”等）。他們將此現象命名為 **directional motion blindness**，並指出其根源是方向訊號與答案選項的綁定失誤（direction binding gap）。  

🧪 **透過 MoDirect 資料集與 DeltaDirect 目標進行診斷與修正**  
- 首先構建 **MoDirect** 資料集家族（含合成與真實影片基準），用於系統化測量運動方向理解能力。  
- 推出 **DeltaDirect**，一個在投影層級的簡單目標：利用相鄰幀特徵差異預測歸一化的 2‑D 運動向量。  
- 在 **MoDirect‑SynBench** 上，僅使用 DeltaDirect 進行指令調整，使運動方向準確率從 **25.9%** 提升至 **85.4%**。  
- 在 **MoDirect‑RealBench** 上，DeltaDirect 使真實世界的方向準確率比未使用任何真實資料調整的基準高出 **21.9 個百分點**，同時未顯著影響標準視訊理解任務的表現。  

💡 **訊號強度受視覺複雜度影響，泛化仍有限**  
進一步的概念向量分析顯示，當影片背景或物體外觀變得更複雜時，方向訊號的幅度會變弱，這限制了模型在未見領域的表現。因此，雖然合成資料的指令調整能有效縮小綁定差距，但真實世界的視覺雜訊仍是提升泛化能力的關鍵挑戰。  

⚠️ **樣本以合成資料為主，真實場景仍需更多驗證**  
本研究主要依賴 MoDirect‑SynBench 進行指令調整；真實基準的改善雖然顯著，但仍建議在更多樣化的真實影片上進一步驗證，以確保在複雜實務場景中的穩定性。  

🎯 **工程師可直接採用的改進方案**  
- 在現有 Video-LLM 架構的投影層加入 DeltaDirect 目標，訓練成本低且不需重新設計整個模型。  
- 使用 MoDirect 資料集進行方向指令調整，可在不犧牲一般視訊理解能力的前提下，顯著提升基本運動方向辨識。  
- 此方法適合快速作為模組化插件，幫助現有系統修正方向盲點，提升對需要精準方向判斷的應用（如自駕、機器人、動作辨識）的可靠性。  

🔗 **論文連結**  
📝 Which Way Did It Move? Diagnosing and Overcoming Directional Motion Blindness in Video-LLMs  
👤 Jongseo Lee, Hyuntak Lee, Sunghun Kim, Sooa Kim, Jihoon Chung (Kyung Hee University; Princeton University)  
🔗 論文：https://arxiv.org/abs/2605.22823  
💻 程式碼與資料集：https://github.com/KHU-VLL/DeltaDirect  

你在使用 Video-LLM 時，是否也遇過「看得見卻說不出方向」的情況？歡迎在留言區分享你的經驗與看法 👇  

#AI #VideoLLM #MotionDirection #ComputerVision #KyungHee #Princeton #DeltaDirect #MoDirect #機器學習 #深度學習
