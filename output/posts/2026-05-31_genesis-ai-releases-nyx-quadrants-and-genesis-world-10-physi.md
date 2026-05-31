---
title: "Genesis AI Releases Nyx, Quadrants, and Genesis World 1.0 Physics Platform for Scalable Robotics Foundation Model Evaluation"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/30/genesis-ai-releases-nyx-quadrants-and-genesis-world-1-0-physics-platform-for-scalable-robotics-foundation-model-evaluation/
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-05-31T19:29:09.803847
---

📌 【Genesis AI】Genesis World 1.0：機器人模型評估提速100倍  

你以為機器人訓練的瓶頸是資料量？Genesis AI 說，真正的慢點是評估速度——一次完整的政策評估在真實機器人上要跑超過 200 小時，而他們的平台只要 0.5 小時就能完成，且結果完全可重現。  

🤔 **機器人模型開發的真正瓶頸在於評估速度，而非資料量**  
機器人基礎模型的發展受限於兩個因素：資料與迭代速度。雖然社會多聚焦於如何收集更多真實數據，但 Genesis AI 指出，評估一個候選政策所需的時間才是較少被討論的關鍵瓶頸。一次完整的評估包含數百個任務，每個任務數百個 episode，在真實機器人上跑完需要一台機器人、一名操作員連續運作超過 200 小時。  

🧪 **在模擬平台上跑完 14 個任務、每任務 200 次 episode 的零射擊評估**  
研究團隊構建了 Genesis World 1.0，該平台由四個部分組成：Genesis World 物理引擎、Nyx 實時光線追蹤渲染器、Quadrants Python‑to‑GPU 編譯器以及一個統一的模擬介面。他們採用「零射擊 real‑to‑sim」的方式：評估時的政策僅在真實世界資料上進行預訓練，模擬資料不會進入訓練管道，以確保效能提升反映真實模型品質而非對模擬動態的過度適配。評估涵蓋三種模型變體（Small、Medium、Large），在 14 個不同任務上，每個任務跑 200 個 episode。  

💡 **Genesis World 1.0 讓評估時間從 200 小時縮至 0.5 小時，誤差極小**  
在同一組評估上，Genesis World 1.0 的總執行時間低於 0.5 小時，且無需人工或硬體介入，多次運行的結果位元精確一致。與真實機器人評估相比，速度提升約兩個數量級（約 100 倍）。模擬與真實硬體 rollout 之間的 Pearson 相關係數為 0.8996（95% 信賴區間：[0.7439，0.9314]]，顯示模擬結果能高度預測真實表現。  

🔍 **將評估與訓練資料流程分離，可避免模擬過擬合帶來的假性提升**  
團隊刻意將評估與用於生成訓練資料的模擬分開。他們的推論是：如果兩個管道共用同一個模擬分布，則觀察到的效能提升可能只是模型對模擬動態的更好適配，而非對真實世界的真正改進。分離後，所得的訊號更乾淨，有助於團隊辨識真正的模型品質差距。  

⚠️ **僅報告相關性，未給出絕對誤差，且未在真實硬體上長期驗證**  
該研究主要呈現模擬與真實硬體之間的高相關性，但沒有提供絕對誤差範圍或誤差分布的詳細數據。此外，評估僅在單次短期運行中進行，長期穩定性以及在不同硬體平台上的表現仍需進一步驗證。  

🎯 **團隊應先用此平台快速篩選模型，再在實機上做少量驗證**  
對於機器人與 AI 基礎設施從業者，Genesis World 1.0 提供了一種低成本、高重複性的評估手段。建議在模型迭代早期階段，利用該平台快速比較不同 checkpoint；在最終選定候選模型後，僅需在真實機器人上進行少量驗證，以確保模擬優勢能轉化為實際表現。  

🔗 **論文連結**  
📝 Genesis AI Releases Nyx, Quadrants, and Genesis World 1.0 Physics Platform for Scalable Robotics Foundation Model Evaluation  
👤 Michal Sutter (MarkTechPost)  
🔗 https://www.marktechpost.com/2026/05/30/genesis-ai-releases-nyx-quadrants-and-genesis-world-1-0-physics-platform-for-scalable-robotics-foundation-model-evaluation/  

你的團隊在機器人模型評估上是否也遇到過「等待跑完實機實驗」的瓶頸？歡迎在留言區分享你的經驗或看法 👇  

#AI #Robotics #Simulation #GenesisAI #FoundationModel #機器學習 #Nyx #Quadrants #GenesisWorld #技術評估
