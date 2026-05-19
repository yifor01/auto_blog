---
title: "SPIKE: An Adaptive Dual Controller Framework for Cost-Efficient Long-Horizon Game Agents"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.18636
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-19T20:55:05.849136
---

📌 **SPIKE：雙控制器框架讓長 horizon 遊戲代理更省 token**

你以為讓 LLM 每一步都做規劃才能玩好開放世界遊戲？實際頻繁推理不只浪費 token，還可能讓代理陷入重複失敗。

🤔 **在 token 與延遲雙重約束下，如何保持目標導向而不浪費資源？**

🧪 **雙控制器與事件觸發的階層記憶設計**  
SPIKE 包含兩層控制器：Strategic Controller 負責低頻的全局規劃、失敗分析與復原；Reactive Controller 在嚴格的 token 預算下負責快速的局部執行。Event Trigger 會即時監視視覺變化、任務進度、重複動作與失敗訊號，決定是否維持反應式執行或升級至戰略規劃。記憶層面採用階層設計，State‑Action Memory Bank（SA‑MB）儲存短期經驗以供複用，State Action Knowledge Graph（SA‑KG）則保存結構化的證據，使兩個控制器能分別取得所需的上下文。

📈 **在 StarDojo Lite-100 上成功率提升 5 個百分點，token 減半**  
相較於最強的 Lite-100 基線，SPIKE 使成功率（SR）提升 5.0 個百分點（相對提升 38.5%）；在預算限制的情況下，較最強預算基線提升 9.3 個百分點（相對提升 75.6%）。同時，token 消耗下降 54.9%，延遲降低 40.8%。這些數據表明，透過在穩定片段重複使用戰略規劃、僅在事件邊界重新呼叫昂貴推理，可同時提升成功率與效率。

💡 **選擇性觸發昂貴規劃才是關鍵**  
消融實驗顯示，事件觸發機制、反應式覆蓋（當計畫過時時允許局部覆蓋）以及異質記憶（SA‑MB 與 SA‑KG 的分離）各自對成功率與復原能力都有顯著貢獻。這支撐了「選擇性推理」而非「每一步都推理」的設計理念：只有當環境出現有意義的變動時，才啟用耗費較高的戰略控制器，其餘時間由高效的反應式控制器維持穩定執行。

⚠️ **僅在單一遊戲基準上驗證，長期穩定性尚未知**  
目前的實驗僅在 StarDojo 的 Lite-100 分割上進行，樣本主要集中於短 horizon 任務的即時表現。長期遊戲中的策略漂移、跨場景知識遺忘以及不同遊戲類型的適應性仍需後續工作進一步探究。

🎯 **將昂貴推理留給真正需要的瞬間，可直接搬移到其他互動式 Agent**  
對於受 token 或 latency 限制的場景（例如即時對話助手、機器人任務規劃），可採用類似的雙控制器結構：將高成本的全局規劃保留給語境顯著改變或失敗發生的時刻，日常步驟則由輕量的反應模組處理。這樣的設計不需要重新訓練大模型，僅在推理端加入事件監測與記憶分離的邏輯，即可在保持效能的同時大幅降低資源消耗。

🔗 **論文連結**  
📝 SPIKE: An Adaptive Dual Controller Framework for Cost-Efficient Long-Horizon Game Agents  
👤 Wencan Jiang, Jiangning Zhang, Jianbiao Mei, Jinzhuo Liu, Yu Yang (Zhejiang University; National University of Singapore; Nanyang Technological University)  
🔗 https://arxiv.org/abs/2605.18636  

你的 Agent 是否也在每一步都做昂貴規劃？歡迎在留言區分享你的看法與經驗 👇

#AI #GameAI #LLMAgent #SPIKE #ZhejiangUniversity #NUS #NTU #機器學習 #強化學習 #資源效率
