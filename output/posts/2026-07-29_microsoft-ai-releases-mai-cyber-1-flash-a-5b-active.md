---
title: 'Microsoft AI Releases MAI-Cyber-1-Flash: A 5B-Active-Parameter Cyber Model
  That Pushes MDASH to 95.95% on CyberGym'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/28/microsoft-ai-releases-mai-cyber-1-flash-a-5b-active-parameter-cyber-model-that-pushes-mdash-to-95-95-on-cybergym/
model: tencent/hy3:free
generated_at: '2026-07-29T14:23:12.364767'
score: 69
---

📌 【Microsoft AI 新發佈】MAI-Cyber-1-Flash：專為網路防禦打造，驅動 MDASH 效能衝向 95.95%

TL;DR：Microsoft 推出首款網路防禦專用模型 MAI-Cyber-1-Flash，透過 MoE 架構大幅提升 MDASH 掃描效能。

隨著 AI 進入 Agentic（代理式）時代，如何讓模型處理高度專業且複雜的網路安全任務成為關鍵。Microsoft AI 近期釋出了 MAI-Cyber-1-Flash，這不僅是其首個專為網路防禦設計的模型，更展現了透過專用微調模型優化多模型代理系統（Multi-model Agentic System）的強大威力。

🧩 **基於 MoE 架構的輕量化專業模型**

MAI-Cyber-1-Flash 並非獨立的 API 終端點，而是整合於 Microsoft 的多模型代理掃描架構 MDASH 之中。其技術細節如下：

*   **模型架構**：採用 Transformer 架構，結合了 Self-attention 與稀疏混合專家（Sparse Mixture-of-Experts, MoE）層。
*   **參數規模**：總參數達 137B，但每次運算僅需 5B 活性參數（Active Parameters）。
*   **上下文長度**：支援高達 256k 的 context length。
*   **技術血統**：由輕量化代理編碼模型 MAI-Code-1-Flash（已整合於 GitHub Copilot 與 VS Code）微調而成，並衍生自 MAI-Thinking-1 系列。
*   **輸入輸出**：僅限文字格式。

📊 **MDASH 效能大幅攀升，CyberGym 分數達 95.95%**

在針對 CyberGym（包含 1,507 個來自 188 個 OSS-Fuzz 專案的真實漏洞重現任務）的測試中，MAI-Cyber-1-Flash 展現了極高的專業能力。

在 MDASH 框架下，將 MAI-Cyber-1-Flash 與 GPT-5.4 結合使用，於 CyberGym 預設的 Level 1 配置（提供漏洞原始碼與高層次描述）下，取得了 95.95% 的高分。這比 Anthropic 的 Mythos 高出約 12 個百分點，也遠超其他競爭系統（介於 83.2% 至 85.6% 之間）。

研究團隊指出，透過將 MDASH 中 80% 的既有模型替換為此類專用模型，架構的總體分數從 88.4% 提升至 95.95%。

💡 **透過模型路由實現成本與效能的平衡**

為了在規模化掃描時控制前沿模型（Frontier Model）的成本，MDASH 採用了精密的任務分配策略：

1.  **任務分配**：MAI-Cyber-1-Flash 承擔了 MDASH 高達 90% 的任務。
2.  **難度升級**：僅將最困難的 10% 任務交由 GPT-5.4 處理。
3.  **成本節省**：相較於先前使用 GPT-5.4、5.4 mini 與 5.3 codex 的配置，這種路由方式節省了 50% 的成本。

此外，MDASH 透過五個階段管理超過 100 個專業代理（Agents）：Prepare（準備）、Scan（掃描）、Validate（驗證）、Dedupe（去重）與 Prove（證明）。其中「Prove」階段會執行觸發輸入，並針對 C/C++ 目標使用 ASan（AddressSanitizer）進行驗證。

🎯 **實務啟示**

MAI-Cyber-1-Flash 的推出證明瞭「專用模型 + 混合專家架構 + 智能路由」是提升專業領域（如網路安全）AI 效能的有效路徑。對於工程師而言，這提示了在構建複雜的 Agentic Workflow 時，不一定要依賴單一最強模型，透過針對特定任務進行微調的輕量化模型來處理大部分工作，能大幅優化成本與系統整體表現。

🔗 **來源**
- 標題：Microsoft AI Releases MAI-Cyber-1-Flash: A 5B-Active-Parameter Cyber Model That Pushes MDASH to 95.95% on CyberGym
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/28/microsoft-ai-releases-mai-cyber-1-flash-a-5b-active-parameter-cyber-model-that-pushes-mdash-to-95-95-on-cybergym/

#MicrosoftAI #Cybersecurity #MoE #MachineLearning #MDASH #CyberGym #LLM #AgenticAI #Transformer #SoftwareEngineering
