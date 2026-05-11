---
title: "LiteGUI: Distilling Compact GUI Agents with Reinforcement Learning"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.07505
score: 104
model: tencent/hy3-preview:free
generated_at: 2026-05-11T20:37:34.924998
---

📌 LiteGUI：輕量 GUI 代理訓練新範式  

你是否曾覺得手機或邊緣設備上的自動化代理，總是因模型太小而「笨手笨腳」？  
傳統的監督微調在小模型上常導致過擬合與遺忘，難以發揮真正潛力。  
這篇來自 Moore Threads AI 的工作提出了一種免 SFT 的新訓練範式，聲稱能讓 2B/3B 級的 GUI 代理表現媲美更大模型。  

🤔 **小模型 GUI 代理受限於容量，傳統 SFT 無法克服過擬合與遺忘**  
當前的 on‑device 視覺語言 GUI 代理受模型容量限制，傳統的監督微調（SFT）在小規模模型上易產生過擬合、災難性遺忘與政策僵化，因而無法完全解決效能瓶頸。  

🧪 **構建自動化資料管道並提出導引式 on‑policy 蒸餾與多解雙層 GRPO 框架**  
研究先建立一個自動化的資料生成管道，合成具備豐富多解標註的 GUI 任務軌跡。在此基礎上，提出「導引式 on‑policy 蒸餾」（Guided On-policy Distillation），引入參考軌跡與動態檢索機制以降低幻覺並減少多解任務中的認知偏移。進一步設計「多解雙層 GRPO」框架，同時對宏觀子任務規劃與微觀執行匹配進行對齊，以增強長距離 GUI 代理的探索能力。  

🔍 **在多個基準上輕量模型達到 SOTA，並與大型模型競爭**  
廣泛實驗表明，所提出的方法在所有基準上使輕量模型的表現達到現有 SOTA 水準，且與規模顯著更大的模型具有競爭力。消融研究進一步顯示，導引式 on‑policy 蒸餾與多解雙層探索是充分釋放 2B/3B 級代理潛力的關鍵因素，超越了傳統模仿學習的效能上限。  

💡 **導引式 on‑policy 蒸餾減少幻覺與認知偏移，多解雙層探索提升長程規劃**  
通過引入 oracle 軌跡與動態檢索，蒸餾過程能對齊參考策略，從而降低模型在多解情境下的錯誤推論。雙層 GRPO 則讓模型在高層規劃與低層動作之間保持一致，使得長序列 GUI 任務中的探索更為有效。  

⚠️ **實驗主要聚焦於特定 GUI 基準，長期穩效與真實設備部署尚需驗證**  
論文的實驗評估集中在既有的 GUI 基準上，未涉及長期穩定性或真實邊緣設備上的部署測試，這些方面仍需後續工作進一步驗證。  

🎯 **對邊緣設備開發者而言，可考慮採用免 SFT 的導引蒸餾＋雙層 GRPO 策略來提升小模型 GUI 代理**  
對於資源受限的裝置，建議嘗試該免 SFT 訓練管道：先透過自動化管道產生多解標註資料，再應用導引式 on‑policy 蒸餾降低幻覺，最後使用多解雙層 GRPO 加強宏微層面的對齊，以在不增加模型規模的情況下獲得更佳的 GUI 自動化表現。  

🔗 **論文連結**  
📝 LiteGUI: Distilling Compact GUI Agents with Reinforcement Learning  
👤 Yubin Wu, Zicheng Cai, Liping Ning, Hua Wang, Zhi Chen @ Moore Threads AI  
🔗 https://arxiv.org/abs/2605.07505  

#AI #GUIAgent #ReinforcementLearning #KnowledgeDistillation #EdgeAI #MooreThreads #LightweightModels #Automation
