---
title: Environment-free Synthetic Data Generation for API-Calling Agents
source: Apple ML
url: https://machinelearning.apple.com/research/environment-free
model: tencent/hy3:free
generated_at: '2026-07-22T00:41:32.864917'
score: 112
---

📌 【Apple ML 研究】不用實際環境，也能訓練 API Agent：利用 LLM 模擬數位世界

TL;DR：透過 LLM 模擬 API 回應與任務，解決訓練 API Agent 時對真實執行環境的依賴。

🤔 **訓練 API Agent 的瓶頸：環境難以規模化**

訓練能操作 API 的大型語言模型 (LLM) Agent，需要大量的高品質互動軌跡 (trajectories)。然而，在現實中收集這些資料存在巨大瓶頸：你通常需要一套完整實作的環境，包含可執行的 API 以及預先填充好資料的後端資料庫。這種對「真實可執行環境」的依賴，嚴重阻礙了資料收集的規模化進度。

🧩 **解決方案：以 LLM 作為即時數位世界模型**

Apple 研究團隊提出了一種「無環境 (Environment-free)」的合成資料生成方法。核心理念是不再依賴真實的後端系統，而是直接利用 LLM 扮演「數位世界模型 (Digital World Models)」，僅憑 API 規格說明 (API specifications)，就能模擬出 Agent 與具備狀態 (stateful) 環境之間的互動。

該流程包含三個關鍵步驟：
1. **任務生成**：由 LLM 首先針對提供的 API 規格，生成各種不同的可解任務。
2. **迭代解題與模擬**：由一個「老師 Agent (Teacher Agent)」嘗試解決任務；同時，一個「LLM 模擬器 (LLM Simulator)」會根據任務背景與模擬歷史，生成連貫的合成 API 回應。
3. **品質篩選**：最後由「LLM 裁判 (LLM Judge)」過濾掉品質不佳的軌跡，確保訓練資料集的品質。

📊 **在挑戰性基準測試中取得顯著成效**

研究團隊在 AppWorld 與 OfficeBench 兩個具挑戰性的基準測試上進行評估，這兩個測試皆包含「資訊檢索」與「狀態變更」兩類任務。

結果顯示，使用這種合成資料進行微調 (Fine-tuning) 後，模型的效能有顯著提升。這證明瞭即便沒有任何可執行的真實環境，也能為 API Calling Agent 提供有效的監督訓練。

🎯 **實務啟示**

對於開發 Agent 的工程師而言，這項技術提供了一種具備高擴充套件性的解決方案。未來在面對全新的、尚未建立完整測試環境的 API 生態系時，可以利用 LLM 模擬環境的方式，快速生成高品質的訓練資料來最佳化模型。

🔗 **來源**
- 標題：Environment-free Synthetic Data Generation for API-Calling Agents
- 作者／機構：Seanie Lee, Sanjoy Chowdhury, Chao Jiang, Cheng-Yu Hsieh, Ting-Yao Hu, Alexander T Toshev, Oncel Tuzel, Raviteja Vemulapalli @ Apple ML
- 連結：https://machinelearning.apple.com/research/environment-free

#AI #LLM #AppleML #APICalling #SyntheticData #Agent #MachineLearning #DigitalWorldModel #SoftwareEngineering #AIResearch
