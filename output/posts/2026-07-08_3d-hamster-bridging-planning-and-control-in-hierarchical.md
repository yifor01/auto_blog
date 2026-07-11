---
title: '3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language
  Action Models through 3D Trajectory Guidance'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.31329
score: 85
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T13:27:48.139099'
---

📌 3D HAMSTER：用深度視覺語言產生實際 3D 軌跡，串接規劃與控制  

TL;DR：3D HAMSTER 結合視覺‑語言模型與深度編碼，直接輸出可供點雲控制器使用的真實尺度 3D 軌跡，提升機器人操作的精準度。

在機器人操作中，視覺語言模型（VLM）已能根據文字指令描述「要抓什麼」或「要放哪裡」，但多半隻產生 2D 影像或抽象的語意向量，缺乏真實世界的空間資訊，讓下游的控制政策必須自行估算深度與路徑。這樣的斷層使得規劃與控制難以協同，導致操作不穩定或需要大量手動校正。

🤔 **核心問題：視覺語言缺乏可直接執行的 3D 軌跡**  
- 文字指令 → VLM → 2D/語意輸出，無法直接驅動基於點雲的控制策略。  
- 控制政策必須自行推測深度或手動規劃路徑，增加錯誤來源。

🧩 **3D HAMSTER 方法概覽**  
- **深度編碼整合**：在視覺語言模型中加入深度資訊編碼，使模型同時理解影像與其空間結構。  
- **3D 軌跡生成**：模型在接受文字指令與視覺輸入後，直接輸出「度量正確」的 3D 軌跡，座標以點雲格式呈現。  
- **點雲控制政策**：產生的 3D 軌跡可直接餵入現有的點雲基礎控制器，省去額外的深度估計或路徑規劃步驟。

📊 **實務意涵**  
- **即插即用**：開發者只需提供文字指令與相機深度影像，即可得到可執行的 3D 動作序列，減少系統整合工作。  
- **提升精準度**：因為軌跡是「metrically accurate」的，控制政策不必再補償深度誤差，操作更穩定。  
- **跨領域應用**：適用於任何以點雲作為感測基礎的機器人平臺，例如抓取、裝配或搬運任務。

🎯 **對工程師的可行動建議**  
1. 若已有 VLM（如 CLIP、BLIP）與深度相機，考慮在模型輸入階段加入深度通道，參考 3D HAMSTER 的深度編碼方式。  
2. 評估現有點雲控制政策是否支援外部 3D 軌跡輸入，若不支援，可在軌跡產生後加入簡易的座標轉換層。  
3. 在實驗室或原型階段，先以簡單的抓取指令測試模型輸出與實際機械手臂執行的誤差，驗證「度量正確」的宣稱。

🔗 來源  
- 標題：3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance  
- 連結：https://huggingface.co/papers/2606.31329  

#3DHamster #VisionLanguageModel #RobotManipulation #3DTrajectory #PointCloudControl #DeepLearning #Robotics #AIPlanning #DepthEncoding #HierarchicalModels
