---
title: "CoMaTrack: Competitive Multi-Agent Game-Theoretic Tracking with Vision-Language-Action Models"
source: ChatPaper/AI
url: https://arxiv.org/abs/2603.22846
score: 108
model: gpt-4o-free
generated_at: 2026-03-25T19:42:08.252471
---

📌 【Amap & Alibaba】CoMaTrack：競爭追蹤新框架  

你以為模仿專家就能讓 AI 準確追蹤語言目標？實際競爭才是關鍵。  

🤔 **語言指向追蹤需對抗環境考驗**  

Embodied Visual Tracking (EVT) 要求智能體依據語言描述精準跟隨目標。現有多數方法依賴單一智能體的模仿學習，需要大量專家數據且訓練環境靜止，導致泛化能力有限。  

🧪 **競爭多智能體強化學習與新基準**  

我們提出 CoMaTrack，一種以博弈論為基礎的競爭多智能體強化學習框架，在動態對抗環境中訓練智能體，並設計競爭子任務以提升自適應規劃與抗干擾策略。同時發布 CoMaTrack‑Bench，為首個競爭式 EVT 基準，包含追蹤者與適應對手在多樣環境與指令下的對抗場景，提供標準化的穩健性評估。  

 **在標準與新基準上達到 SOTA**  

實驗顯示 CoMaTrack 在現有基準與 CoMaTrack‑Bench 上皆達到最先進表現。特別是，使用 3B 視覺語言動作模型並透過本框架訓練，在具有挑戰性的 EVT‑Bench 上超過以往基於 7B 模型的單一智能體模仿學習方法，達成 STT 92.1%、DT 74.2%、AT 57.5%。  

💡 **競爭訓練如何產生更強適應力**  

透過讓追蹤者與對手在博弈中不斷調整策略，智能體學會在未見過的干擾與環境變化中保持追蹤穩定性，這正是單一智能體模仿學習難以獲得的適應優勢。  

⚠️ **論文未詳細說明具體限制，僅提供實驗結果**  

🎯 **競爭式訓練減少對專家數據依賴，基準碼即將開放**  

此工作为 Embodied AI 社群提供了一種可降低專家標註成本、提升泛化的訓練思路，並隨附基準程式碼（將於 https://github.com/wlqcode/CoMaTrack-Bench 公開），方便直接在各種環境下進行穩健性測試。  

🔗 **論文連結**  
📝 CoMaTrack: Competitive Multi-Agent Game-Theoretic Tracking with Vision-Language-Action Models  
👤 Youzhi Liu, Li Gao, Liu Liu, Mingyang Lv, Yang Cai (Amap; Alibaba Group)  
🔗 論文：https://arxiv.org/abs/2603.22846  
💻 基準碼：https://github.com/wlqcode/CoMaTrack-Bench  

#AI #EmbodiedAI #MultiAgentRL #VisionLanguage #Amap #Alibaba #CoMaTrack
