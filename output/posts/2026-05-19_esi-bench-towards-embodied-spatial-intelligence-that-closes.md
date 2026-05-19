---
title: "ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.18746
score: 111
model: tencent/hy3-preview:free
generated_at: 2026-05-19T20:40:44.444763
---

📌 【Stanford 大學等最新研究】ESI‑Bench：主動探索勝過被動感知  

你以為讓 AI 多看幾張圖就能提升空間理解？實際上，隨機多視角反而可能加雜訊。  

🤔 **空間智慧不該只看，還要動**  
過去的空間智慧評估多半假設代理人能直接取得完美觀測，忽略了「動作」在獲得資訊中的角色。ESI‑Bench 把觀察者重新定義為行動者，要求代理人透過感覺、 locomotion 與 manipulation 來主動蒐集任務相關的證據，這樣才能揭開被遮蔽的結構、動力學、容納與功能等無法被動感知解決的資訊。  

🧪 **基於 OmniGibson 的 10 大類 29 小項 Embodied 基準**  
該基準建構在 OmniGibson 模擬環境中，涵蓋 10 個任務類別與 29 個子類別，參照 Spelke 的核心知識系統。代理人必須決定要部署哪些能力（感覺、移動、操作）以及如何排序它們，以主動累積解決任務所需的證據。  

🔍 **主動探索顯著優於被動感知，隨機多視角反而加噪**  
在最新多模態大語言模型（MLLM）上的廣泛實驗顯示：主動探索的策略遠勝於被動式的單靠觀測；代理人甚至能在沒有明確指示的情況下自發發現新的空間策略。相反，隨機多視角雖然消耗了遠更多的圖像，卻常常只是加入雜訊而非有效資訊。  

💡 **失敗來源於行動盲目，而非感知不足**  
錯誤主要不是因為感覺模組弱，而是因為「行動盲目」：不當的動作選擇導致貧弱的觀測，進而觸發連鎖錯誤。即便在對深度敏感的任務中，顯式的 3D 基礎能穩定推論，但不完美的 3D 表示反而會扭曲空間關係，使表現優於單純 2D 基線的情況變得更糟。  

⚠️ **基於模擬環境，真實世界適用性待驗證**  
研究僅在 OmniGibson 模擬世界中進行，真實物理環境中的感覺噪聲、動作延遲與硬體限制尚未涵蓋；因此基準的結論需要進一步在實機平台上驗證。  

🎯 **設計 Embodied Agent 時應優先行動決策與元認知**  
- 在開發空間推論模型時，應該同等重視「如何選擇下一個動作」而不只提升感覺品質。  
- 人類在實驗中會尋找 falsifying 視角並在矛盾出現時修正信念，而模型則容易在證據品質不佳時仍抱持高信心，這凸顯了元認知上的落差。  
- 未來的工作可從改善動作規劃與錯誤回饋機制著手，而不僅是堆疊更多視角或更精細的 3D 表示。  

🔗 **論文連結**  
📝 ESI-Bench: Towards Embodied Spatial Intelligence that Closes the Perception-Action Loop  
👤 Yining Hong, Jiageng Liu, Han Yin, Manling Li, Leonidas Guibas (Stanford University; UCLA; Northwestern University)  
🔗 https://arxiv.org/abs/2605.18746  

你在設計 Embodied Agent 時，是否已經開始考慮「該動哪一步」而不只是「該看什麼」？歡迎在留言區分享你的經驗與思考 👇  

#AI #EmbodiedAI #SpatialIntelligence #CVPR #Stanford #UCLA #Northwestern #MLLM #Robotics
