---
title: Build an AI Scientist for Life Science Discovery with NVIDIA BioNeMo Agent
  Toolkit
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/build-an-ai-scientist-for-life-science-discovery-with-nvidia-bionemo-agent-toolkit/
score: 96
model: google/gemma-4-31b-it:free
generated_at: '2026-06-23T20:26:33.370814'
---

📌 【NVIDIA】用 BioNeMo Agent Toolkit 將 AI 轉化為能進行生命科學發現的「AI 科學家」

TL;DR：透過 BioNeMo Skills 提供標準化介面，將 AI Agent 的生命科學任務完成率從 57.1% 提升至 100%。

通用型 AI Agent 能寫程式、讀論文，但生命科學研究不同於軟體工程，沒有一個能直接判定假設正確與否的測試套件。在生物分子研究中，AI 科學家的能力上限，取決於它能多可靠、正確且高效地使用科學工具。

🤔 **通用 Agent 難以直接應用於生物研究的痛點**

科學發現是一個反覆迭代且充滿不確定性的過程，且必須基於物理世界。單純將通用編碼 Agent 指向生物學領域，並不代表就能研發出新藥。要讓 AI 真正成為「AI 科學家」，必須解決它如何正確呼叫專業生物分子模型的問題。

🧩 **BioNeMo Skills：將生物模型封裝為 Agent 可呼叫的服務**

NVIDIA BioNeMo 透過提供「BioNeMo Skills」，將核心的生物分子能力封裝成 Agent 準備就緒（agent-ready）的介面。這些能力包括：
- 結構預測 (Structure Prediction)
- 分子生成 (Molecular Generation)
- 分子對接 (Docking)
- 序列分析 (Sequence Analysis)
- 基因組學 (Genomics)

這些 Skills 可透過託管或本地的 NIM 部署作為可呼叫服務提供。此外，透過 Model Context Protocol 伺服器封裝，明確記錄了模型的用途、輸入要求、預期產出與失敗模式。這使得 Agent 能在不依賴特定後端或執行環境的情況下，自主地發現、選擇、呼叫並解析生物分子模型。

📊 **將任務完成率從 57.1% 提升至 100%**

根據實證基準測試（使用 Codex CLI 與 GPT-5.5 fast），整合 BioNeMo Skills 帶來顯著的效能提升：
- **任務完成率**：從 57.1% 提升至 100%。
- **Token 效率**：Token 使用效率提升至兩倍。
- **流程轉型**：將原本孤立的模型呼叫，轉化為可迭代且符合生產標準的研究迴圈 (Research Loops)。

🎯 **實務啟示**

對於開發科學 AI Agent 的工程師而言，這證明了「工具封裝」的重要性。與其依賴 LLM 的通用推理，不如透過定義明確的輸入/輸出規範（如 Model Context Protocol）將專業領域模型轉化為「技能」，讓 Agent 能在受控且可靠的框架下進行科學探索。

🔗 **來源**
- 標題：Build an AI Scientist for Life Science Discovery with NVIDIA BioNeMo Agent Toolkit
- 作者／機構：Kyle Tretina, Mahan Salehi, Neel Patel and Kris Kersten @ NVIDIA
- 連結：https://developer.nvidia.com/blog/build-an-ai-scientist-for-life-science-discovery-with-nvidia-bionemo-agent-toolkit/

#AI #BioNeMo #NVIDIA #LifeScience #AIAgent #DrugDiscovery #Biomolecular #NIM #ModelContextProtocol #ScientificComputing
