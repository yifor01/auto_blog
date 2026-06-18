---
title: 'Beyond the Current Observation: Evaluating Multimodal Large Language Models
  in Controllable Non-Markov Games'
source: arXiv
url: http://arxiv.org/abs/2606.19338v1
score: 98
model: google/gemma-4-31b-it:free
generated_at: '2026-06-18T20:51:18.329084'
---

📌 **【新基準發佈】MLLM 能在「看不見」的情況下做決策嗎？RNG-Bench 揭露多模態模型的記憶短板**

當我們將多模態大模型（MLLM）部署為閉環策略（Closed-loop Policies）時，面臨的最大挑戰之一是：模型能否在當前觀測不到資訊時，依然根據「過去看到的內容」做出正確行動？

目前的評測基準大多存在缺陷：要麼直接給出完整狀態（Full State），要麼將「記憶重建」與「操作能力」混為一談，甚至僅在回合結束後才測試記憶。這導致我們很難判斷模型是「忘了之前看到了什麼」，還是「知道看到了什麼但不知道怎麼操作」。

🤔 **目前的評測無法區分「記憶失效」與「決策失誤」**

在非馬爾可夫遊戲（Non-Markov Games）中，當前的觀測並不包含所有必要資訊，模型必須依賴歷史記憶來重建狀態。然而，現有的基準測試缺乏精確的控制變數，使得開發者難以釐清模型在複雜任務中失敗的真正原因：究竟是視覺記憶力不足，還是邏輯推理能力欠缺？

🧪 **RNG-Bench：專為「重建能力」設計的對抗性測試**

研究團隊提出了 **RNG-Bench (Reconstructive Non-Markov Games)**，旨在將「重建過去觀測」的能力與「執行行動」的能力分離。該基準包含兩款互補的遊戲：
1. **Matching Pairs**：卡片身份僅在特定位置短暫顯現，模型必須在後續步驟中精準回憶。
2. **3D Maze**：模型需將第一人稱視角（Egocentric views）整合進一個空間地圖中。

為了確保測試的嚴謹性，研究團隊設計了三個可控的難度軸心：**網格大小 (Grid size)**、**視覺模式 (Visual pattern)** 與 **觀測模態 (Observation modality)**。此外，還引入了「對頭對決協議 (Head-to-head duel protocol)」來降低單一樣本帶來的隨機誤差。

📉 **Memory Gap：揭露模型失敗的真兇是「遺忘」**

研究中提出了一個關鍵指標 **Memory Gap**，用以將「遺忘（Forgetting）」與「糟糕的行動選擇（Poor action selection）」解耦。

實驗結果顯示：在最困難的配置下（每回合需處理約 128K tokens 與 350 張影像輸入），頂尖的 MLLMs 依然遠未達到飽和。最重要的是，Memory Gap 分析證明：**大多數的殘差錯誤（Residual errors）源自於模型遺忘了早期的觀測資訊，而非決策邏輯錯誤。**

💡 **透過最佳策略微調，可有效提升記憶重建能力**

研究團隊嘗試對 **Qwen3.5-9B** 進行微調，使用了最佳策略的 Rollouts 以及經過過濾的模型演示數據。結果顯示，這種微調方法不僅提升了模型在 RNG-Bench 上的表現，且能遷移到其他現有基準測試中，且不會損害模型原有的通用多模態能力。

⚠️ **極端長文本與大量影像輸入仍是瓶頸**

雖然微調有成，但面對高達 128K tokens 與數百張影像的極端情境，目前的 MLLM 仍面臨顯著的記憶衰減。這意味著在實務部署需要長期記憶的 Agent 任務時，單純依賴 Context Window 可能不足以解決問題。

🎯 **對 AI 工程師的實務啟示：區分記憶與推理**

- **診斷工具**：在開發多模態 Agent 時，建議引入類似 Memory Gap 的指標，確認模型失敗是因為「沒記住」還是「不會做」，避免在錯誤的方向上優化 Prompt。
- **訓練策略**：使用高品質的最佳策略 Rollouts 進行微調，能有效強化模型對歷史觀測的重建能力，且不影響通用能力。
- **長上下文挑戰**：在處理多圖輸入的長序列任務時，需關注模型對早期視覺資訊的保留率。

🔗 **論文連結**
📝 Beyond the Current Observation: Evaluating Multimodal Large Language Models in Controllable Non-Markov Games
👤 Shengyuan Ding, Xilin Wei, Xinyu Fang, Haodong Duan, Dahua Lin
🔗 論文：http://arxiv.org/abs/2606.19338v1

面對複雜的長序列任務，你認為目前的 MLLM 記憶能力足以應對實務部署嗎？歡迎在評論區討論 👇

#AI #MLLM #ComputerVision #RNGBench #MemoryGap #Qwen #深度學習 #AIAgent
