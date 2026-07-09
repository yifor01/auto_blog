---
title: Data for Agents
source: HuggingFace Blog
url: https://huggingface.co/blog/nvidia/open-data-for-agents
score: 91
model: google/gemma-4-31b-it:free
generated_at: '2026-07-09T09:58:33.951469'
---

📌 【NVIDIA 觀點】AI Agent 的核心不在權重，而是在於高品質的開放資料

TL;DR：NVIDIA 強調 Agent 的能力取決於資料工程，並透過 Nemotron 系列合成資料提升推理與工具使用能力。

許多人將 AI Agent 視為「能使用工具的自動補完器」，但真正的 Agent 必須能處理現實世界的不可預測性，例如修復失效的 API 呼叫或應對未見過的流程。

🤔 **從「自動補完」到「真正 Agent」的資料挑戰**

要讓模型從單純的工具呼叫演進為具備韌性的 Agent，核心問題在於資料的缺乏。作者指出，開發 Agent 需要以下關鍵型別的資料支援：
- 軟體工程軌跡 (Software engineering traces)
- 工具使用失敗的案例 (Tool-use failures)
- 多步驟推理 (Multi-step reasoning)
- 檢索 (Retrieval) 與安全 (Safety)
- 使用者模擬 (User simulation)
- 工作流執行 (Workflow execution)
- 最終的物理世界互動 (Physical world interaction)

🧩 **利用合成資料 (Synthetic Data) 擴充套件能力邊界**

由於現實資料有限，NVIDIA 透過 Nemotron 系列產品利用合成資料來填補缺口，提升模型的基礎能力：
- **Nemotron-CC**：利用合成資料強化 Common Crawl 資料集，用於預訓練。
- **Nemotron-CC-MATH**：利用合成的數學問題來提升模型的推理能力。
- **Nemotron Pretraining**：一個涵蓋通用、程式碼、數學及合成資料的龐大集合，規模達數兆 (trillions) 個 token。

💡 **權重開放不夠，資料透明才是可重複性的關鍵**

NVIDIA 主張，雖然開放權重 (Open weights) 很重要，但對於 Agent 的開發來說，權重僅是故事的一部分。要實現真正的可重複性 (Reproducibility)，必須公開模型背後的：
- 資料集 (Datasets)
- 資料篩選選擇 (Curation choices)
- 訓練配方 (Training recipes)
- 評估方法 (Evaluation methods)

🎯 **實務啟示**

對於開發 AI Agent 的工程師而言，提升模型韌性的方向不在於單純增加引數，而是在於構建包含「失敗案例」與「多步推理軌跡」的資料集。合成資料能有效解決特定領域（如數學或程式碼）的資料稀缺問題，但透明的資料篩選與訓練流程才是確保 Agent 行為可預測且可稽核的前提。

🔗 **來源**
- 標題：Data for Agents
- 作者／機構：NVIDIA / HuggingFace
- 連結：https://huggingface.co/blog/nvidia/open-data-for-agents

#AI #AIAgents #NVIDIA #Nemotron #SyntheticData #LLM #MachineLearning #OpenData #DataEngineering #Pretraining
