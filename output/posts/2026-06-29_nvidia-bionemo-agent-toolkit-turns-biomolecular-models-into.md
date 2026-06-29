---
title: NVIDIA BioNeMo Agent Toolkit Turns Biomolecular Models Into Callable Skills
  for AI Agents in Drug Discovery
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/29/nvidia-bionemo-agent-toolkit-turns-biomolecular-models-into-callable-skills-for-ai-agents-in-drug-discovery/
score: 102
model: google/gemma-4-31b-it:free
generated_at: '2026-06-29T20:24:17.935986'
---

📌 【NVIDIA 新工具】BioNeMo Agent Toolkit：將生物分子模型轉化為 AI Agent 的可呼叫技能

TL;DR：NVIDIA 推出開源工具集，讓 AI Agent 能直接呼叫蛋白質摺疊、分子對接等生物模型來加速藥物研發。

科學發現與軟體工程截然不同。在開發程式時，測試通過（Test Suite turns green）即代表成功；但在生物醫學研究中，假設是否正確必須在物理世界中反覆驗證，過程充滿不確定性且高度迭代。

🎣 **通用 Coding Agent 寫不出新藥**

NVIDIA 指出，僅僅讓一個擅長寫程式的通用 AI Agent 處理生物學問題是不夠的。在生物分子研究中，Agent 的能力上限取決於它能多可靠、正確且高效地使用專業工具。為了填補這個鴻溝，NVIDIA 推出了 BioNeMo Agent Toolkit，旨在將複雜的生物分子模型轉化為 AI Agent 可直接呼叫的「技能（Skills）」。

🧩 **將生物模型封裝為「可呼叫技能」的架構**

BioNeMo Agent Toolkit 是一個開源儲存庫，其核心理念是將生物模型封裝成 Agent 可理解的介面。該平臺由兩個主要部分組成：

1. **加速工具層 (Accelerated Tool Layer)**
   - 透過 NVIDIA NIM (NVIDIA Inference Microservices) 與 BioNeMo 開放模型提供核心能力。
   - 底層由 cuEquivariance（針對結構模型）與 Parabricks（針對基因組學）等函式庫進行效能加速。

2. **Agent 準備介面 (Agent-ready Interfaces)**
   - **BioNeMo Skills**：為每個能力建立封裝，明確定義模型的用途、必要輸入、選用引數、預期產出以及失敗模式。
   - **MCP 伺服器封裝**：針對尚未封裝成 NIM 的開放模型，使用 Model Context Protocol (MCP) 伺服器進行封裝。
   - 這讓 Agent 能自主地發現、選擇、呼叫並解析生物分子模型的結果。

📂 **技能分類與多步驟工作流**

該儲存庫將技能分為三類：`nim-skills`、`open-models-skills` 以及 `library-skills`。此外，`workflows` 資料夾中定義了「元技能（Meta-skills）」，可用於處理多步驟的複雜任務。

例如，在 `generative_protein_binder_design`（生成蛋白質結合劑設計）的工作流中，Agent 會按照以下鏈路執行：
RFdiffusion $\rightarrow$ ProteinMPNN $\rightarrow$ OpenFold3

每個技能都獨立於一個目錄中，並包含一個 `SKILL.md` 檔案，內含 YAML 格式的前置資料（Frontmatter）與詳細操作指令。

🎯 **實務啟示**

對於 AI 工程師而言，這套工具集定義瞭如何將「專業領域模型」轉化為「Agent 技能」的標準化路徑：定義明確的輸入輸出 $\rightarrow$ 描述失敗模式 $\rightarrow$ 封裝為可呼叫服務 $\rightarrow$ 組合成工作流。這種模式可以被遷移到其他需要高度專業領域知識的 AI Agent 應用場景中。

🔗 **來源**
- 標題：NVIDIA BioNeMo Agent Toolkit Turns Biomolecular Models Into Callable Skills for AI Agents in Drug Discovery
- 作者／機構：Asif Razzaq
- 連結：https://www.marktechpost.com/2026/06/29/nvidia-bionemo-agent-toolkit-turns-biomolecular-models-into-callable-skills-for-ai-agents-in-drug-discovery/

#NVIDIA #BioNeMo #AIAgent #DrugDiscovery #BiomolecularModeling #ProteinFolding #OpenSource #NIM #MCP #GenerativeChemistry
