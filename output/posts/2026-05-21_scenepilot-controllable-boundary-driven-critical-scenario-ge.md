---
title: "ScenePilot: Controllable Boundary-Driven Critical Scenario Generation for Autonomous Driving"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.21168
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-21T20:51:36.493579
---

📌 **ScenePilot：生成可解卻失敗的邊界場景，提升自駕安全測試**  

你以為讓擬人車輛「故意撞車」就能測出自駕漏洞？實際上很多產生的 crash 根本不可能發生，這樣的測試會讓工程師走錯方向。  

🤔 **真正需要的不是「不可能的事故」，而是「可能卻仍會失敗」的情境**  
安全關鍵場景在真實道路上極為罕見，因此必須靠模擬來進行壓力測試。現有做法要麼忽略車輛與道路的物理極限，產生視覺上極端但實際無法發生的碰撞；要麼只單獨 enforce 物理或政策可行性，導致過度聚焦於激進 manœuvre 或綁定於特定控制器的能力邊界。我們需要一種能同時保證「物理可解」且「仍能讓自駕堆疊失敗」的場景生成方法。  

🧪 **以可行性為導向的邊界帶生成框架**  
ScenePilot 將目標定義為「邊界帶」：在理論上可被物理定律解決，但卻足以讓已部署的自駕系統失敗。生成過程被建模為受約束的多目標強化學習，同時優化兩個目標：  
1. 以 RSS 為基礎的物理可行性分數 σ；  
2. 線上學習的自駕風險預測器 Φ。  
為了讓探索停留在可行性邊界且避免產生不可行的 artefact，我們提出了逐層可行性感知 shielding（step‑level feasibility‑aware shielding），在每一步決策時檢查 σ，確保搜尋不會越過物理極限。  

🚗 **在 SafeBench 上的實驗：碰撞率顯著提升且物理有效性保持**  
使用多種規劃器（planner）在 SafeBench 基準上進行測試，ScenePilot 產生的場景使碰撞率提升了 6.2 個百分點，同時場景仍保持物理可行性。進一步的對抗式微調（adversarial fine‑tuning）在這些邊界帶場景上，能顯著降低後續測試中的崩潰率，證明此類場景對改善自駕安全具有實際價值。  

⚠️ **實驗基於特定基準與簡化的風險預測器**  
實驗僅在 SafeBench 上進行，使用了特定的多個規劃器作為評估對象；線上學習的風險預測器 Φ 是基於目前可得的數據訓練，不同的感知或控制模組可能會導致不同的邊界帶分布。長期泛化能力及在更複雜都市場景中的表現尚需後續工作驗證。  

🎯 **工程師可直接利用此框架進行更具意義的安全壓力測試**  
- 將 ScenePilot 作為產生「真正具挑戰性」的測試案例的起點，避免浪費資源在物理不可能的碰撞上。  
- 生成的邊界帶場景可用於對抗式訓練，提升自駕堆疊對邊界案例的韌性。  
- 開源程式碼已於 GitHub 公開，方便直接接入現有的模擬流程。  

🔗 **論文連結**  
📝 ScenePilot: Controllable Boundary-Driven Critical Scenario Generation for Autonomous Driving  
👤 Qiyu Ruan, Yuxuan Wang, He Li, Zhenning Li, Cheng‑zhong Xu (University of Macau)  
🔗 論文：https://arxiv.org/abs/2605.21168  
💻 程式碼：https://github.com/QiyuRuan/ScenePilot  

你目前的自駕測試流程是否也在產生「看起來很危險但實際不可能」的場景？歡迎在留言區分享你的經驗或對邊界帶測試的看法 👇  

#自駕 #AI安全 #ScenarioGeneration #ReinforcementLearning #場景生成 #SafeBench #UniversityofMacau #ScenePilot #AV測試 #機器學習
