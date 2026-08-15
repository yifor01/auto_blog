---
title: Custom reward functions for multi-turn reinforcement learning with Amazon Nova
  Forge
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/custom-reward-functions-for-multi-turn-reinforcement-learning-with-amazon-nova-forge/
model: nvidia/nemotron-3-ultra-550b-a55b:free
generated_at: '2026-08-15T06:17:43.609195'
score: 95
---

📌 AWS Nova Forge 多輪強化學習：自訂獎勵函數怎麼設計才不會「看起來在學、其實沒學到」

TL;DR：Nova Forge 採 BYOO 架構讓你在自管容器跑多輪 RL，核心在於設計「組內有變異」的複合獎勵，避免單一標量或零變異元件讓 GRPO 失去梯度。

隨著 Agent 應用從單輪問答延伸到多輪工具呼叫、程式碼執行與錯誤復原，強化微調（RFT）成為教導模型「行為」的關鍵。但 AWS 這篇實戰筆記直指痛點：獎勵函數寫錯一點，訓練曲線漂亮卻學歪方向；寫對了卻沒變異，GRPO 直接算不出優勢函數，模型原地踏步。

🤔 **多輪 RFT 與單輪根本不同：軌跡才是評估單位**

傳統 SFT 需要人工標註推理路徑，RFT 則直接拿模型自產出來的輸出去評分。Nova Forge 採用 GRPO，對每個提示詞取 K 組 rollout，依獎勵排序再算正規化優勢更新權重。關鍵差別在多輪：一個 rollout 不再是單一回覆，而是完整的「劇集」，包含工具呼叫、程式執行、中間失敗重試等一連串狀態。Lambda 15 分鐘限制擋不住這類長跑任務，Nova Forge 因此提供 BYOO（Bring Your Own Orchestration）：你在自管容器（如 ECS）跑環境、模擬器、驗證器，最後回傳 `aggregate_reward_score` 與可選的 `metrics_list` 給訓練端。

🧩 **複合獎勵三層結構：結果、行為、懲罰各司其職**

單一標量獎勵容易被「玩弄」，終端稀疏獎勵又太難學。實務上組合三類訊號：

- **結果獎勵**：最終產物是否達標（如單元測試通過），目標導向但稀疏、早期近乎零
- **行為獎勵**：中間步驟是否展現期望行為（先問再寫、呼叫正確工具、避免迴圈），用來塑形、補足稀疏性
- **懲罰項**：明確打擊猜測、重複、卡住等失敗模式，拉開策略間差距讓優勢函數有梯度

文中以 500 道協作編程任務為例，在 Nova Lite 2.0 上跑 LoRA 多輪 RFT，設計四元件加權獎勵：
1. `asked_before_coding`：先發問才給分，**不綁定正確性**，但要求最終必須提交程式碼（堵住「只問不答」漏洞）
2. `guessed_immediately`：一上來就猜直接扣分，讓「猜」嚴格劣於「問」
3. 程式碼正確性驗證（結果導向）
4. 格式/流程合規檢查

兩大設計原則：**解綁想要的行為**、**明確懲罰不想要的模式**。前者讓行為獎勵獨立發揮，後者確保 GRPO 組內有變異可學。

💡 **隱形殺手：權重最高的元件卻貢獻零梯度**

作者親身踩過的坑：最高權重的獎勵元件在某次實驗中「靜默貢獻零學習訊號」。原因在於 GRPO 只對組內變異負責——若某元件在同組 K 個 rollout 全部拿同分（全 0 或全 1），其優勢為 0，梯度直接消失。訓練曲線依然下降，因為其他元件在更新，但這個元件完全沒教到模型任何事。

解法三步驟：
1. **逐元件記儀**：在 `metrics_list` 記錄每個元件的分布，確認組內方差 > 0
2. **組內統計監控**：追蹤每個元件的 mean/std/advantage，發現標準差趨近 0 即預警
3. **解綁條件依賴**：像範例把「先問」與「正確性」解綁，避免早期全錯導致行為獎勵全歸零

另一實務細節：獎勵函數需在沙箱安全執行模型產生的程式碼，文中示範用隔離容器跑驗證器，避免任意碼注入風險。

🎯 **給工程師的可執行啟示**

- 採用 Nova Forge BYOO 時，**先把獎勵拆成可獨立觀測的元件**，再加權；不要只看總分
- **每個元件都要能在 GRPO 組內產生變異**，否則它只是裝飾
- **懲罰項不是懲罰性的，是「製造梯度」的必要手段**——沒有負向訊號，優化器分不清好壞策略
- 基礎設施（HyperPod、CDK 部署、容器編排）Part 1 已涵蓋，這篇專注獎勵邏輯本身；程式碼僅供參考起手，實際部署仍需依任務調整驗證器與模擬器

🔗 **來源**
- 標題：Custom reward functions for multi-turn reinforcement learning with Amazon Nova Forge
- 作者／機構：Maria Masood @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/custom-reward-functions-for-multi-turn-reinforcement-learning-with-amazon-nova-forge/

#AWS #NovaForge #ReinforcementLearning #GRPO #RFT #MultiTurnRL #RewardDesign #LLMTraining #SageMakerHyperPod #BYOO
