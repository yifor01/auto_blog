---
title: 'Meta AI Releases Muse Code (Beta): A Terminal Coding Agent Powered by the
  New Muse Spark 1.2 Model'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/05/meta-superintelligence-labs-releases-muse-code/
model: tencent/hy3:free
generated_at: '2026-08-06T08:42:23.654248'
score: 88
---

📌 【Meta AI】推出 Muse Code Beta：具備持久性背景代理能力的終端機編程助手

TL;DR：Muse Code 透過 Muse Spark 1.2 模型，實現能在大型專案中進行長期、複雜任務的終端機編程代理。

隨著 AI 代理（Agent）從簡單的對話轉向複雜的軟體工程任務，Meta AI 推出了 Muse Code (Beta) 版本。這不僅僅是一個對話框，而是一個能在大型程式碼庫中規劃、編寫並驗證結果的終端機代理，其核心動力來自於全新的 Muse Spark 1.2 模型。

🧩 **透過背景代理與事件日誌，實現長效且穩定的任務執行**

與傳統「針對單一任務啟動一個代理」的模式不同，Muse Code 採用了一種全新的設計理念：

* **異步背景代理 (Async Background Agents)**：一組專門的背景代理會在整個工作階段（Session）中保持活躍，而非在每個任務後重新啟動。這種設計能避免重複進行資訊收集，並在處理複雜的多步驟任務時，降低延遲並提升操控精準度。
* **可重啟的事件日誌 (Replay-exact Event Log)**：系統會將每一次的模型呼叫、工具執行、使用者核准以及程式碼編輯，都記錄在一個本地的「僅限追加」事件日誌中。這讓代理具備「斷點續傳」的能力，即使發生當機，也能從上次停止的地方精確恢復。

🛠️ **內建三大核心指令：從規劃到壓力測試**

Muse Code 提供了一套預設的技能指令，協助工程師管理開發流程：
* `/plan`：將任務轉化為一個需要經過核准的執行計畫。
* `/grill`：對該計畫進行壓力測試，直到計畫足以支撐複雜邏輯。
* `/goal`：朝著指定的最終目標持續執行任務。

📊 **Muse Spark 1.2：針對編程工作流深度優化的模型**

Muse Spark 1.2 是對前代 1.1 版本的升級，Meta 特別強調該模型與其測試框架（Harness）進行了協同訓練（Co-trained）。

* **效能提升**：在程式碼生成、複雜除錯（Debugging）、程式碼庫理解以及端到端開發工作流方面皆有顯著進步。
* **訓練規模**：研究團隊大幅提升了編程任務的訓練算力，並擴大了環境的多樣性。
* **評估基準**：
    * **Terminal-Bench 2.1**：測試 89 個任務。
    * **DeepSWE v1.1**：涵蓋 91 個專案、5 種語言的 113 個任務。
    * **Meta Internal Coding Bench**：包含 440 個源自內部實際 Pull Request 的任務。
* **對比基準**：實驗中對比了 Grok 4.5、Claude Opus 5、GPT-5.6 Terra、Gemini 3.6 Flash 與 Kimi K3。

💡 **深度技術案例：GPU Kernel 優化**

Meta 展示了一個極端的測試案例：針對 GPU Kernel 進行迭代優化，該過程包含超過 1,000 次工具呼叫，持續時間長達 24 小時。模型會針對基準進行編寫、編譯、分析效能（Profiling）並逐步改進。在 NVIDIA Hopper GPU 上的測試顯示，模型能針對 KDA 與 MLA kernel 進行高度複雜的優化工作。

⚠️ **使用限制與安裝方式**

目前 Muse Code 僅提供 Beta 版本，且根據發布資訊，模型似乎是透過託管方式（Hosted dependency）提供，並未釋出可下載的權重（Weights）。

* **支援平臺**：macOS 與 Linux。
* **安裝指令**：`curl -fsSL https://dev.meta.ai/install.sh | bash`

🎯 **實務啟示**

對於需要處理大規模既有專案（Legacy Codebase）的工程師來說，這種具備「持久狀態」與「背景代理」能力的工具，比單純的程式碼補全更具實戰價值。它更像是一個能理解專案上下文、並能自主進行長期除錯與優化的虛擬夥伴。

🔗 **來源**
- 標題：Meta AI Releases Muse Code (Beta): A Terminal Coding Agent Powered by the New Muse Spark 1.2 Model
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/05/meta-superintelligence-labs-releases-muse-code/

#MetaAI #MuseCode #MuseSpark #CodingAgent #SoftwareEngineering #LLM #MachineLearning #GPUOptimization #DevTools #AIResearch
