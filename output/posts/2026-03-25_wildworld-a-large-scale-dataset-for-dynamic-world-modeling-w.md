---
title: "WildWorld: A Large-Scale Dataset for Dynamic World Modeling with Actions and Explicit State toward Generative ARPG"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.23497
score: 112
model: gpt-4o-free
generated_at: 2026-03-25T19:38:05.811603
---

📌 【Alaya Studio 等機構】WildWorld：大規模動作條件下的世界模型資料集  

你以為 AI 看夠多遊戲畫面就能學會角色該怎麼動？沒有明確的「狀態」標註，模型很容易把動作與畫素變化纏在一起，長時間預測就會失準。  

🤔 **現有影片資料集缺少結構化的動作與狀態資訊**  
目前用於世界模型的資料多半只提供原始影像與粗粒度的動作標籤，動作往往直接綁定在畫面上的像素變化上。這種設計讓模型難以分辨「角色真的在做什麼」與「畫面因光線、視角變化而產生的雜訊」，導致學得的動態缺乏語意結構，尤其在長 horizon 預測時狀態會快速漂移。  🧪 **從《Monster Hunter: Wilds》自動蒐集 1.08 億幀、超過 450 種動作的細粒度標註**  
研究團隊利用這款 AAA 動作角色扮演遊戲，同步擷取角色骨骼、世界狀態（如血量、狀態異常）、相機姿態以及深度圖，並將每一幀與對應的動作標籤對齊。資料集規模如下：  - 超過 108 M 幀影像  
- 超過 450 種動作（移動、攻擊、技能施放等）  
- 每幀皆附有骨骼、世界狀態、相機姿態、深度圖的同步標註  

此設計使得動作不再只是像素的變化，而是透過底層狀態來中介，為模型提供了明確的因果線索。  

 **在 WildBench 上評估顯示：語意豐富動作與長 horizon 狀態一致性仍是挑戰**  
團隊進一步提出 WildBench 基準，包含「Action Following」與「State Alignment」兩項任務。廣泛的實驗結果指出，即便擁有豐富的狀態標註，現有的世界模型在：  
- 理解語意層面的複雜動作（例如連擊、技能組合）  - 在較長時間序列上保持世界狀態的一致性  方面仍遇到顯著困難。這凸顯了未來需要更具狀態意識的視訊生成與預測方法。  

💡 **狀態是結構化世界模型的關鍵橋樑**  
當動作直接與像素變化掛鉤時，模型容易學到表層關聯；當動作經由明確的狀態（角色姿勢、世界屬性）傳遞時，模型能更好地分辨「做了什麼」與「畫面因何而改變」。這也說明為什麼在缺少狀態標註的資料集上，長 horizon 預測往往會快速發散。  

⚠️ **資料來源單一、自動標註可能含噪聲，評估指標仍在發展中**  
- 資料僅來自單一遊戲（《Monster Hunter: Wilds*），跨域泛化能力尚未驗證  
- 骨骼、世界狀態等標註是透過遊戲引擎自動產生，雖然精度高，但仍可能含有少量誤差  
- WildBench 作為新基準，其評估尺度與實務需求的對應性仍需後續工作進一步檢驗  

🎯 **對研究與工程的啟示：建構狀態感知的生成模型**  
- 未來的視訊世界模型應該把狀態視為第一類公民，將動作與狀態分開建模  
- 此資料集為強化學習與影片預測提供了一個可用來檢測「模型是否真的理解世界動力學」的試金石  - 研究團隊已開放專案頁面（https://shandaai.github.io/wildworld-project/），歡迎社群下載與基於此進行實驗  

🔗 **論文連結**  
📝 WildWorld: A Large-Scale Dataset for Dynamic World Modeling with Actions and Explicit State toward Generative ARPG  
👤 Zhen Li, Zian Meng, Shuwei Shi, Wenshuo Peng, Yuwei Wu (Alaya Studio, Shanda AI Research Tokyo; Beijing Institute of Technology; Shanghai Innovation Institute; Shenzhen MSU-BIT University; Tsinghua University)  
🔗 https://arxiv.org/abs/2603.23497  

你認為在訓練世界模型時，該如何平衡「像素級細節」與「狀態層面理解」？歡迎在留言區分享你的看法 👇  #AI #WorldModeling #VideoGeneration #ReinforcementLearning #WildWorld #MonsterHunter #ShandaAI #CVPR2026
