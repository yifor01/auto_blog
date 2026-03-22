---
title: "GUI-Libra: Training Native GUI Agents to Reason and Act with Action-aware Supervision and Partially Verifiable RL"
source: ChatPaper/AI
url: https://arxiv.org/abs/2602.22190
score: 121
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-02-26T20:21:24.515594
---

📌 【GUI-Libra】開源 GUI 代理的訓練瓶頸被攻破了！81K 資料集 + 創新 RL 技巧，讓 AI 真正學會「看螢幕、點按鈕」

開源的 GUI 代理（圖形使用者介面代理）一直面臨一個尷尬的局面：它們在長時間序列的導航任務上，表現遠不如閉源系統。為什麼會這樣？UIUC、Microsoft 和 UNC-Chapel Hill 的研究團隊深入分析後發現，問題出在兩個關鍵點上。

🤔 **標準訓練方法為何讓 GUI 代理表現不佳？**

現有的通用後訓練流程存在兩個根本缺陷：
- **推理與實作脫鉤**：標準的 SFT（Supervised Fine-Tuning）搭配 Chain-of-Thought 推理，反而會傷害「實際操作」的能力
- **部分可驗證性困境**：在 RLVR（Reinforcement Learning from Verifiable Rewards）中，多種動作都可能是正確的，但驗證時卻只承認單一示範動作，導致離線指標無法準確預測線上任務成功率

🧪 **GUI-Libra 的三層次解決方案**

**1. 資料建構與過濾系統**
團隊建立了一套資料建構與過濾流程，並釋出一個精選的 81K GUI 推理資料集。這解決了行動對齊推理資料稀缺的問題。

**2. 行動感知 SFT**
創新的訓練方法混合了「推理後行動」和「直接行動」資料，並重新加權 token 來強調行動和 grounding。這有效調和了推理與實作之間的矛盾。

**3. 穩定 RL 訓練**
研究發現 KL 正則化在 RLVR 中被低估了，適當的 KL 信任區域對提升離線到線上的預測能力至關重要。團隊進一步引入成功適應性縮放，降低不可靠負梯度的重要性。

 **跨平台的顯著提升**

在多樣化的網頁和行動裝置基準測試中，GUI-Libra 持續提升了步驟準確性和端到端任務完成率。這意味著，透過精心設計的後訓練和資料整理，可以顯著提升任務解決能力，而無需昂貴的線上資料收集。

⚠️ **為何這項研究很重要**

這不只是又一個模型改進，而是對開源社群的實質貢獻：
- 提供 81K 高品質資料集，解決資料稀缺問題
- 提出針對 GUI 代理特性的訓練方法論
- 釋出程式碼和模型，讓研究者可以基於此進一步探索資料高效的後訓練

🎯 **對開發者的實際意義**

如果你正在開發 GUI 自動化、測試工具，或任何需要螢幕操作的人工智慧應用，GUI-Libra 的研究成果提供了：
- 資料建構的最佳實踐
- 訓練過程的關鍵超參數調整策略
- 評估指標選擇的參考

🔗 **論文連結**
📝 GUI-Libra: Training Native GUI Agents to Reason and Act with Action-aware Supervision and Partially Verifiable RL
👤 Rui Yang, Qianhui Wu, Zhaoyang Wang, Hanyang Chen, Ke Yang
🏛️ UIUC; Microsoft; UNC-Chapel Hill
🔗 arxiv.org/abs/2602.22190

你認為開源 GUI 代理未來最關鍵的突破會是什麼？歡迎分享你的看法！

#AI #MachineLearning #GUI #自動化 #開源 #UIUC #Microsoft #研究突破
