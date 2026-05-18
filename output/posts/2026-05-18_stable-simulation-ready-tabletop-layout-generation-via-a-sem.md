---
title: "STABLE: Simulation-Ready Tabletop Layout Generation via a Semantics-Physics Dual System"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.16137
score: 104
model: tencent/hy3-preview:free
generated_at: 2026-05-18T20:32:46.955499
---

📌 【SII·SUSTech·Shanghai AI Laboratory·SJTU·Spatialtemporal AI·FDU】純 LLM 生成桌面場景總是碰撞？STABLE 用語義＋物理雙系統解決  

大型語言模型在將任務指令轉換為 3D 場景佈局時，常因缺乏立體空間推理而產生物體碰撞或懸浮，這直接影響 Embodied AI 中的模擬訓練品質。研究團隊提出 STABLE，透過語義推理器與物理校正器兩個互補模組，讓場景生成既符合任務語義又滿足物理約束。  

🤔 **純 LLM 難以避免物理衝突**  
現有的任務到場景生成方法全依賴 LLM 直接預測佈局，儘管能捕捉任務語意，但在 3D 空間推理上存在固有缺陷，導致生成的場景常出現物體相互穿透或懸浮於空中，無法直接用於物理模擬。這限制了 Embodied AI 在真實機器人訓練前的場景準備效率。  

🧪 **語義推理器＋物理校正器的交替生成範式**  
STABLE 包含兩個核心模組：  
1. **語義 Reasoner**：針對結構化桌面場景資料進行微調的 LLM，負責從任務指令產生粗略的物體佈局。  
2. **物理 Corrector**：以物理感知的流式去噪模型為基礎，根據當前佈局輸出姿態更新，使場景遠離碰撞與懸浮狀態，同時盡量保持與原始語義的一致性。  
兩個模組交替執行，從任務關鍵物件開始逐步擴充背景物件，實現漸進式場景生成。  

🚀 **生成的場景同時符合任務語義與物理可行性**  
實驗顯示，STABLE 能夠產出嚴格依照任務指令的桌面場景，且與以往純 LLM 方法相比，場景的物理有效性（無碰撞、無懸浮）獲得顯著提升。這意味著生成的場景可以直接投入物理模擬或機器人訓練流程，無需額後修正。  

💡 **語義與物理的互補才是關鍵**  
語義 Reasoner 負責理解「要放什麼、放在哪裡」的高層次任務需求；物理 Corrector 則負責「這樣放會不會碰到或飛走」的低層次約束。透過兩者的迭代協調，STABLE 在不犧牲任務對齊的前提下，解決了純語言模型在空間推理上的盲點。  

⚠️ **目前僅驗證桌面場景，推廣至更複雜環境尚需後續工作**  
論文聚焦於結構化的桌面情境，未涉及較大尺度或非結構化的室內/戶外場景。此外，物理 Corrector 的設計依賴於特定的流式去噪架構，不同物理模擬器的適配度仍需進一步探討。  

🎯 **對 Embodied AI 與機器人模擬的直接啟發**  
- 若需在模擬中快速產生符合任務的場景，可考慮採用類似語義＋物理雙系統的架構。  
- 未來工作可嘗試將此範式擴充至多物體互動、可變形物體或動態環境。  
- 對於實務工程師，這代表著「先讓 LLM 打草稿，再用物理模型修正」可能成為減少後期碰撞清理工作的有效流程。  

🔗 **論文連結**  
📝 STABLE: Simulation-Ready Tabletop Layout Generation via a Semantics-Physics Dual System  
👤 Zhen Luo, Yixuan Yang, Xudong Xu, Jinkun Hao, Zhaoyang Lyu  
🏢 SII; SUSTech; Shanghai AI Laboratory; SJTU; Spatialtemporal AI; FDU  
🔗 https://arxiv.org/abs/2605.16137  

你是否也曾遇過 LLM 生成的場景在模擬中「爆炸」？歡迎在留言區分享你的經驗或對此類雙系統方法的看法 👇  

#AI #EmbodiedAI #SceneGeneration #LLM #PhysicsBased #Robotics #Simulation #SII #SUSTech #ShanghaiAILab #SJTU #SpatialtemporalAI #FDU #CVPR2026
