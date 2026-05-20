---
title: "World-Ego Modeling for Long-Horizon Evolution in Hybrid Embodied Tasks"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.19957
score: 126
model: tencent/hy3-preview:free
generated_at: 2026-05-20T20:48:28.933195
---

📌 【Chinese Academy of Sciences 等】World-Ego Modeling：拆解世界與自我，提升長 horizon 混合導航-操作任務  

你有沒好奇，為什麼現在的世界模型在長時間、交叉導航與操作的任務上總是表現不佳？  

🤔 **世界與自我在單一流程中纏結，導致長 horizon 表現下降**  
現有的 embodied world model 通常把「世界」（場景的穩定規則）與「自我」（機器人中心、受指令影響的動態）放在同一個預測流程裡。這種纏結在需要交替進行導航與操作的混合任務中，會讓模型對遠端未來的演化產生誤差。

🧪 **從 motion、語意、意圖三個視角劃分世界‑自我邊界**  
論文提出 World‑Ego Modeling 的概念範式，從三個角度定義世界與自我的邊界：  
- motion‑based（運動特徵）  
- semantic‑based（語義資訊）  
- intention‑based（任務意圖）  
並探討三種解纏策略：後解纏（post‑）、前解纏（pre‑）與完全解纏（full‑disentanglement）。

🚀 **World‑Ego Model (WEM)：獨立規劃 + CP‑MoE 擴散生成器**  
將上述概念具體化為 World‑Ego Model，由兩部分組成：  
1. 一個隱式的分離世界‑自我規劃器（implicit separate world‑ego planner）  
2. 一個串聯‑平行混合專家（cascade‑parallel mixture‑of‑experts, CP‑MoE）擴散生成器  
這樣的設計讓世界與自我可以各自演化，同時又能透過規劃器進行協調。

📏 **HTEWorld：首個長 horizon 混合導航‑操作基準**  
為了嚴格評估，團隊建構了 HTEWorld 基準，包含：  
- 125K 個影片剪輯（超過 4.5M 幀）  
- 細粒度動作標註  
- 300 個多輪評估軌跡（超過 2K 條指令）  
專注於同時包含導航與操作的混合任務。

📊 **在 HTEWorld 上達到 SOTA，在純操作基準上仍具競爭力**  
廣泛實驗顯示，WEM 在 HTEWorld 上達成目前最佳表現，同時在既有的純操作世界模型基準上保持競爭力，證明該範式在不犧牲既有能力的前提下，提升了長 horizon 混合任務的建模能力。

⚠️ **僅在基準測試上評估，實機驗證尚未報告**  
論文目前的實驗皆基於建構的 HTEWorld 基準，未提及實機平台或實際機器人部署的結果，長期泛化能力仍需後續工作驗證。

🎯 **概念與工具雙重貢獻，適合研究與工程參考**  
- 提供一個清晰的世界‑自我分解概念圖，可啟發未來的模型設計  
- 開放的 HTEWorld 基準與實作細節（CP‑MoE 擴散生成器）為社群提供可直接使用的評估平台與起點  

🔗 **論文連結**  
📝 World-Ego Modeling for Long-Horizon Evolution in Hybrid Embodied Tasks  
👤 Zuyao Lin, Jianhui Zhang, Peidong Jia, Xiaoguang Zhao, Shanghang Zhang  
🏫 Chinese Academy of Sciences; University of Chinese Academy of Sciences; Zhongguancun Academy; Shanghai JiaoTong University; Peking University  
🔗 https://arxiv.org/abs/2605.19957  

你認為這種「世界‑自我」分解在未來的機器人學習中會扮演什麼角色？歡迎在留言區分享你的看法 👇  

#AI #EmbodiedAI #WorldModel #Robotics #CVPR2026 #ChineseAcademyOfSciences #HTEWorld #CPMoE #NavigationManipulation
