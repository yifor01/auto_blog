---
title: 'Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.08716
score: 89
model: google/gemma-4-31b-it:free
generated_at: '2026-07-12T08:03:56.394112'
---

📌 **解決「行為狀態衰減」：主動記憶代理讓長程任務不再遺忘**

TL;DR：透過獨立的記憶代理主動注入關鍵提醒，顯著提升長程任務的成功率，且能即插即用。

在處理長程任務（Long-horizon tasks）時，AI 代理常面臨一個尷尬困境：隨著執行路徑（Trajectory）越來越長，早期的任務要求、環境事實或之前的嘗試紀錄會被淹沒在龐大的上下文視窗中，甚至被直接擠出視窗。

🤔 **當記憶變成負擔：行為狀態衰減（Behavioral State Decay）**

作者將這種現象定義為「行為狀態衰減」。當決定任務成敗的關鍵資訊分散在不斷擴張的軌跡中，行動代理（Action Agent）往往無法在正確的時機提取這些資訊，導致即便資訊在上下文之中，卻無法有效影響最終決策。

🧩 **從被動檢索轉向「主動幹預」的記憶機制**

為了克服此問題，該研究將記憶視為一種「主動幹預機制」，而非傳統的被動檢索（Passive Retrieval）。其核心設計如下：

- **雙代理架構**：一個不經修改的「行動代理」負責執行，另一個獨立的「記憶代理」同步執行。
- **結構化記憶庫**：記憶代理負責從近期軌跡中更新結構化的記憶庫。
- **選擇性注入**：記憶代理會判斷何時該注入基於記憶的提醒（Reminder），或在不需要時保持沉默。
- **即插即用**：此模組可直接整合至現有的頂尖行動代理與代理框架（Agent Harnesses）中。

📊 **在兩大基準測試中顯著提升成功率**

研究在 Terminal-Bench 2.0 與 $\tau^2$-Bench 上進行測試，結果顯示無論是較弱或較強的行動代理，pass@1 表現均有所提升：
- **Terminal-Bench**：成功率提升 8.3 個百分點 (pp)。
- **$\tau^2$-Bench**：成功率提升 6.8 個百分點 (pp)。

消融實驗（Ablations）進一步證明，這種「選擇性幹預」的效果優於以下方案：
- 僅將記憶庫暴露給模型（Passive bank exposure）。
- 持續不斷地注入記憶（Always-on injection）。
- 僅提供建議（Advisor-only guidance）。
- 一般的檢索機制（General retrieval）。

💡 **開源記憶策略的初步嘗試**

為了探索開源的記憶策略，研究團隊使用 SFT（監督式微調）與 GRPO 演算法，在 SETA 資料集上訓練了 Qwen3.5-27B 模型。結果顯示該模型提升了驗證獎勵（Validation reward），並在 Terminal-Bench 上實現了部分遷移效果。

🎯 **實務啟示**

對於開發複雜 AI Agent 的工程師而言，這項研究提供了一個重要方向：與其盲目擴大上下文視窗或依賴 RAG 檢索，不如建立一個「監控者」角色。透過讓記憶代理主動決定「什麼時候提醒」而非「讓模型自己去找」，可以有效減少長程任務中的資訊遺失，提升執行穩定性。

🔗 **來源**
- 標題：Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents
- 連結：https://huggingface.co/papers/2607.08716

#AI #LLM #Agent #LongHorizonTasks #MemoryAgent #Qwen #SFT #GRPO #MachineLearning #Reasoning
