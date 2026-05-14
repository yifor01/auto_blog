---
title: "AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.13724
score: 127
model: tencent/hy3-preview:free
generated_at: 2026-05-14T20:21:02.108075
---

📌 【NVIDIA x NUS x MIT】AnyFlow：任意步數視訊擴散模型，透過流映射蒸餾解決少步驟退化  

你以為少步驟的 AI 視訊生成越快越好？研究顯示，當你給模型更多步驟時，它的品質竟會變差。  

🤔 **少步驟生成的品質會隨步數增加而惡化**  
現有的 consistency distillation 方法能在極少步數（例如 1‑4 步）下產出高品質視訊，但其核心是把原本的 probability‑flow ODE 軌跡替換為 consistency‑sampling 軌跡。這樣做雖然讓少步驟變快，卻削弱了 ODE 採樣原本應該具備的「步數越多、品質越好」的特性，導致在分配更多步驟時表現反而下降，限制了其在「任意步數」場景中的實用性。  

🧪 **以流映射為目標的全軌跡蒸餾**  
AnyFlow 把蒸餾的目標從端點一致性映射 $z_{t}\rightarrow z_{0}$ 改為在任意時間區間上的流映射過渡學習 $z_{t}\rightarrow z_{r}$。也就是說，它不只學習「從噪聲直接到圖像」的捷徑，而是學習中間狀態之間的微小流動。為了在訓練時能高效使用這個目標，團隊提出 **Flow Map Backward Simulation**，將完整的 Euler 推導分解成多個短距離的流映射跳躍，這樣既能在訓練階段貼近真實的 ODE 軌跡（on‑policy），又能減少兩種主要誤差：少步驟採樣的離散誤差與因果生成的曝露偏差。  

📈 **在少步驟與多步驟兩端皆具競爭力**  
實驗涵蓋雙向與因果兩種架構，模型規模從 1.3B 到 14B 參數。結果顯示：  
- 在極少步驟（few‑step） regime 下，AnyFlow 的表現與傳統 consistency‑distilled 模型相當，甚至在某些基準上略勝一籌。  
- 隨著可用採樣步數的增加，其品質會持續提升，也就是具備「步數越多、品質越好」的可擴展行為。  

💡 **為何流映射能改善擴散行為**  
傳統 consistency distillation 只關注起點與終點的對應，忽略了中間軌跡的形狀。AnyFlow 透過學習流映射，實際上在近似原始 ODE 的向量場上進行蒸餾，使得模型在測試時能更忠實地遵循連續時間的動力學。這同時減少了因離散步數太大而產生的誤差（discretization error），也因為訓練過程已經看到完整的前後文脈，降低了因果模型在生成過程中對未來資訊的不正確依賴（exposure bias）。  

⚠️ **實驗範圍與未探索面**  
- 現有結果僅涵蓋 1.3B‑14B 參數規模、雙向與因果兩類架構，更大規模或其他變體（例如純 autoregressive）尚未驗證。  
- 評估主要聚焦在圖像品質與步數關係，長視訊的時間 Cohérence（長期一致性）與複雜動作的細節尚未在論文中詳細報告。  
- 未提及開源程式碼或商業授權狀態，實務落地前仍需參考原始碼發行情況。  

🎯 **對工程師的啟示**  
如果你需要在實際產品中兼顧生成速度與品質，AnyFlow 提供了一種「依步數可調」的選擇：  
- 在嚴格延遲預算下，可使用少步驟模式獲得可接受的品質。  
- 若有額外運算餘裕，增加步驟即可帶來明確的品質提升，無需擔心品質會因步數增加而反轉。  
這意味著未來的視訊生成服務可以根據使用者設備或服務等級動態調整採樣步數，以達到更好的資源與體驗平衡。  

🔗 **論文連結**  
📝 AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation  
👤 Yuchao Gu, Guian Fang, Yuxin Jiang, Weijia Mao, Song Han (NVIDIA; National University of Singapore; MIT)  
🔗 https://arxiv.org/abs/2605.13724  

你在視訊生成時會怎樣取樣步數？歡迎在留言區分享你的經驗與想法 👇  

#AI #VideoGeneration #DiffusionModels #AnyFlow #NVIDIA #NUS #MIT #MachineLearning #CVPR2026
