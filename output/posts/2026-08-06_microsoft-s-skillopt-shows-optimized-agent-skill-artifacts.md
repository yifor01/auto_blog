---
title: Microsoft’s SkillOpt Shows Optimized Agent Skill Artifacts Transfer Across
  Model Scales and Between Codex and Claude Code Harnesses
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/05/microsoft-skillopt-agent-skill-transfer-portability/
model: tencent/hy3:free
generated_at: '2026-08-06T08:43:36.288148'
score: 87
---

📌 【Microsoft 研究】SkillOpt 實現 Agent 技能轉移：從 Codex 到 Claude Code 都能用的通用技能檔

TL;DR：SkillOpt 能將優化後的自然語言技能封裝成單一 Markdown 檔，實現跨模型與跨工具環境的技能轉移。

當我們在為 AI Agent 優化工作流程時，最頭痛的問題之一就是：在 A 工具環境下學到的「最佳實踐」，換到 B 工具或更小的模型時，還能用嗎？Microsoft 與多所大學合作開發的 SkillOpt 提出了新的解法：透過優化自然語言指令，讓 Agent 具備可移植的「技能檔案」。

🤔 **解決「技能與環境綁定」的困境**

目前的 Agent 技能優化往往依賴於微調（fine-tuning），這意味著技能與特定的模型參數緊密耦合。SkillOpt 則採用「文字空間優化」（text-space optimizer）的思路：
- **凍結模型**：目標模型（Target Model）在訓練過程中保持不變。
- **優化器模型**：由一個專門的優化模型讀取評分後的執行軌跡（rollouts），並提出「新增、刪除、替換」的編輯建議。
- **單一檔案輸出**：最終產出一個名為 `best_skill.md` 的 Markdown 檔案，這就是 Agent 的「技能清單」。

🧩 **跨工具、跨模型的技能轉移實驗**

研究團隊測試了技能在不同規模模型與不同開發工具（Harnesses）之間的遷移能力。這裡的關鍵指標不是「直接訓練」，而是「轉移後的效能能保留多少原本在目標領域訓練出的增益」。

📊 **從 Codex 到 Claude Code：跨越工具界限的成功案例**

研究中一個極具意義的發現是，在 Codex 環境下優化出的技能，竟然能直接應用在 Claude Code 上：
- **SpreadsheetBench 表現**：在 Codex 中優化出的技能，讓 Claude Code 的分數從 22.1 提升至 81.8，甚至超越了從頭在 Claude Code 中訓練出的 80.4 分。
- **為什麼這很重要？** 因為 Codex 與 Claude Code 使用完全不同的工具 API 與指令介面。這證明 SkillOpt 學習到的是「程序性知識」（procedural knowledge），而非僅僅是針對特定工具的指令指令集。

💡 **程序性技能 vs. 推理型技能**

研究發現，技能的遷移率並不均勻，這取決於技能的本質：
- **程序性技能（Portable）**：例如「先檢查工作簿結構與公式，再寫入靜態值」這種步驟化的流程。這類技能在跨環境時表現優異，因為其邏輯不依賴於特定的 CLI 工具。
- **推理型技能（Tied to environment）**：這類技能與訓練環境的關聯較深，在跨環境轉移時效能下降較明顯（例如 Codex 到 Claude Code 在 LiveMath 任務中僅保留了 10% 的增益）。

⚠️ **部署與成本的優勢**

對於工程師而言，SkillOpt 帶來了兩項實務上的改變：
1. **一次訓練，隨處部署**：訓練成本僅需支付一次（離線完成），且在部署時不需要額外的推理開銷（inference-time calls），因為技能已經內化在 Markdown 檔中。
2. **可審核性（Auditability）**：與黑盒子的權重檔案不同，`best_skill.md` 是人類可讀的文字檔。每一項編輯都有 `edit_apply_report.json` 記錄，讓開發者可以清楚追蹤技能是如何被優化出來的。

🎯 **實務啟示**

如果你正在開發 AI Agent，SkillOpt 告訴我們：**優化「如何做」的程序，比優化「答案是什麼」的推理更具擴展性。** 透過將最佳實踐封裝成可讀的 Markdown 檔案，你可以實現「在成本最低的環境進行優化，並在實際產品環境中部署」的高效工作流。

🔗 **來源**
- 標題：Microsoft’s SkillOpt Shows Optimized Agent Skill Artifacts Transfer Across Model Scales and Between Codex and Claude Code Harnesses
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/05/microsoft-skillopt-agent-skill-transfer-portability/

#AI #Agent #Microsoft #SkillOpt #MachineLearning #LLM #SoftwareEngineering #Productivity #AIResearch #Automation
