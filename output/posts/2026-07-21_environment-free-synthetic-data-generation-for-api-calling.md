---
title: Environment-free Synthetic Data Generation for API-Calling Agents
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.16900
score: 91
model: tencent/hy3:free
generated_at: '2026-07-21T08:30:33.673839'
---

📌 【新研究】無需執行環境，利用 LLM 模擬數位世界來生成 API 呼叫資料

TL;DR：透過 LLM 模擬 API 回應，無需實際執行環境即可生成高品質的 Agent 訓練軌跡。

🎣 **擺脫對實體 API 環境的依賴**

訓練具備 API 呼叫能力的 LLM Agent，需要海量的高品質互動軌跡（trajectories）。然而，傳統做法通常需要建置完整的執行環境，包含可執行的 API 以及預先填入資料的後端資料庫，這對大規模擴充套件訓練規模而言，構成了嚴重的技術瓶頸。

🧩 **用 LLM 當作「隨選數位世界模型」**

研究提出了一種無需環境（environment-free）的合成資料生成方法，其核心理念是利用 LLM 來擔任「隨選數位世界模型」（on-the-fly digital world models）。只要提供 API 規格，就能模擬 Agent 與環境之間的互動。

該流程包含三個關鍵步驟：
1. **任務生成**：LLM 首先根據提供的 API 規格，生成多樣化的任務。
2. **迭代解決**：由一個「教師 Agent」（teacher agent）嘗試解決任務，同時由一個「LLM 模擬器」（LLM simulator）根據任務背景與模擬歷史，生成連貫的合成 API 回應。
3. **品質過濾**：最後由一個「LLM 裁判」（LLM judge）過濾軌跡，確保生成資料集的品質。

📊 **在 AppWorld 與 OfficeBench 取得顯著成效**

研究團隊在包含「資訊檢索」與「狀態改變（state-changing）」任務的挑戰性基準測試（AppWorld 與 OfficeBench）上進行了評估。結果顯示，使用這種合成資料進行微調（fine-tuning），能為模型帶來顯著的效能提升，證明瞭無需實際執行環境也能為 API 呼叫 Agent 提供有效的監督訓練。

💡 **模擬 API 是大規模訓練的實用解方**

這項研究證實，基於 LLM 的 API 模擬技術，是針對不同 API 生態系訓練 Agent 時，一種具備實用性且可擴充套件（scalable）的解決方案。

🔗 **來源**
- 標題：Environment-free Synthetic Data Generation for API-Calling Agents
- 連結：https://huggingface.co/papers/2607.16900

#LLM #AI #Agent #SyntheticData #APICalling #MachineLearning #DigitalWorldModel #AppWorld #OfficeBench #DeepLearning
