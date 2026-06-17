---
title: From the Hugging Face Hub to robot hardware with Strands Agents and LeRobot
source: HuggingFace Blog
url: https://huggingface.co/blog/amazon/strands-lerobot-hub-to-hardware
score: 95
model: google/gemma-4-31b-it:free
generated_at: '2026-06-17T20:35:47.778806'
---

📌 【AWS & Hugging Face】從 Hub 到硬體：用 Strands 與 LeRobot 打造機器人學習流水線

在機器人開發中，最痛苦的往往不是演算法本身，而是「破碎的工具鏈」。錄製數據用一套工具、訓練用一套、模擬用一套、部署到實體硬體又是另一套，這些環節之間缺乏統一的溝通機制，導致從模擬到實體 (Sim-to-Real) 的過程充滿摩擦。

🤔 **破碎的工具鏈讓機器人開發變成「拼圖遊戲」**

目前的典型開發流程通常需要五個獨立工具：錄製、訓練、模擬、硬體部署以及多機協調。雖然每個工具單獨運作良好，但它們彼此互不相通。這意味著開發者必須花大量時間在不同格式的轉換與環境配置上，而非專注於機器人的任務學習。

🧪 **用 Strands SDK 將 LeRobot 整合為統一的 Agent**

為了打破這個僵局，AWS 推出了開源的 Strands SDK (Apache 2.0)，其核心理念是將 LeRobot 的能力封裝成 `AgentTools`，讓開發者能將整個流程組合成單一的 Agent。

這個整合方案的關鍵在於「輕量化」：
- **數據一致性**：模擬環境錄製的 `LeRobotDatasets` 與實體硬體寫入的格式完全一致。
- **統一接口**：透過 `LerobotLocal` 接口，無論是 GR0OT 還是 MolmoAct2 的 checkpoints 都能以相同路徑執行推理。
- **基礎設施解耦**：利用 Zenoh mesh 實現對遠端機器人集群的指令分發。

🚀 **單一 Agent 即可完成從模擬到實體的 5 個步驟**

這項整合讓開發者只需在一個 Agent 循環中完成以下流程：
1. **構建 Agent**：基於 LeRobot 的 `AgentTools` 搭建核心邏輯。
2. **模擬錄製**：在模擬環境中錄製 `LeRobotDataset`。
3. **策略執行**：在同一台模擬機器人上測試訓練後的 Policy。
4. **硬體部署**：僅需修改一個關鍵字參數 (Keyword Argument)，即可將同樣的代碼部署到實體 SO-101 機器人上。
5. **集群廣播**：透過 Zenoh mesh 將指令同步到整個機器人機隊。

💡 **Sim-to-Real 的關鍵：數據格式的完全統一**

這項方案的核心洞察在於「讓數據格式成為通用語言」。當模擬器產出的數據與實體硬體讀取的格式完全相同時，Sim-to-Real 的遷移成本將大幅降低。開發者不再需要編寫複雜的轉換腳本，而是將 LeRobot 作為底層執行器，而 Strands 則扮演「黏著劑」的角色，協調整個生命週期。

⚠️ **目前側重於 SDK 整合，端到端性能仍需實測**

此方案重點在於解決工具鏈的碎片化問題，提供一套標準化的 SDK 抽象層。至於在極端複雜任務下的推理延遲或多機同步的精準度，仍需開發者根據具體硬體環境進一步測試。

🎯 **對機器人工程師的實務建議：嘗試標準化數據管線**

如果你正試圖將 LLM/VLM 部署到實體機器人，建議優先考慮如 LeRobot 這種開源且具備社群支持的數據格式，並利用類似 Strands 的抽象層來解耦硬體與邏輯。減少對自定義轉換腳本的依賴，能讓你的研究更易於復現且快速迭代。

🔗 **資源連結**
📝 From the Hugging Face Hub to robot hardware with Strands Agents and LeRobot
👤 Sundar Raghavan & Cagatay Cali @ AWS / Hugging Face
🔗 閱讀全文：https://huggingface.co/blog/amazon/strands-lerobot-hub-to-hardware
💻 GitHub 範例：可直接在筆電上執行模擬應用（請參考原文連結）

如果你對 Sim-to-Real 或機器人 Agent 部署有經驗，歡迎在下方分享你的實作心得 👇

#Robotics #HuggingFace #AWS #LeRobot #SimToReal #OpenSource #AI #機器人學習
