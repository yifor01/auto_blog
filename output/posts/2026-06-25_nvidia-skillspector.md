---
title: NVIDIA/SkillSpector
source: GitHub Trending
url: https://github.com/NVIDIA/SkillSpector
score: 126
model: google/gemma-4-31b-it:free
generated_at: '2026-06-25T20:20:09.681899'
---

📌 【NVIDIA 開源】SkillSpector：在安裝 AI Agent Skills 前，先掃描其安全性

TL;DR：針對 AI Agent Skills 的安全掃描工具，透過靜態分析與 LLM 評估，偵測漏洞與惡意模式。

當我們使用 Claude Code、Codex CLI 或 Gemini CLI 等 AI Agent 時，通常會安裝各種「Skills」來擴展其能力。然而，這些 Skills 往往在極少審核的情況下就被賦予隱含的信任，這為系統留下了巨大的安全漏洞。

🤔 **26.1% 的 Agent Skills 潛在風險**

根據研究顯示，AI Agent Skills 的安全性堪憂：約 26.1% 的 Skills 包含漏洞，更有 5.2% 表現出可能的惡意意圖。為了回答「這個 Skill 是否安全可以安裝？」的問題，NVIDIA 推出了 SkillSpector。

🧩 **兩階段分析與 68 種漏洞模式**

SkillSpector 透過一套分析管線（Analyzer Pipeline）來偵測風險，其核心技術流程如下：

1. 掃描輸入 $\rightarrow$ 支援 Git 儲存庫、URL、zip 壓縮檔、目錄或單一檔案。
2. 兩階段分析 $\rightarrow$ 先進行快速的靜態分析 (Static Analysis)，接著可選擇執行 LLM 語義評估 (Semantic Evaluation)。
3. 漏洞比對 $\rightarrow$ 涵蓋 17 個類別共 68 種漏洞模式，包含 prompt injection、資料外洩 (data exfiltration)、許可權提升、供應鏈風險、系統提示詞洩漏 (system prompt leakage) 以及 MCP 工具中毒 (MCP tool poisoning) 等。
4. 即時查詢 $\rightarrow$ 透過 SC4 查詢 OSV.dev 以獲取即時的 CVE 資料，並提供離線備援機制。

📊 **量化風險評分與靈活的報告格式**

為了讓工程師快速判斷風險，SkillSpector 提供以下功能：
- **風險評分**：提供 0-100 的評分，並附上嚴重程度標籤與明確的建議。
- **多樣化輸出**：支援 Terminal、JSON、Markdown 以及 SARIF 報告格式。
- **雜訊抑制**：可透過 glob-rule 或指紋 (fingerprint) 建立基準線 (Baseline)，以抑制已知或可接受的偽陽性 (false-positive) 結果。

🎯 **實務啟示**

對於開發或部署 AI Agent 的工程師而言，不能再將第三方 Skills 視為安全。在將新技能整合進 Agent 之前，應將 SkillSpector 納入 CI/CD 或安裝前的審核流程。此外，該專案提供 Pi 擴充功能，讓開發者能直接在 Agent 運作會話中掃描 Skills，實現即時的安全防護。

🔗 **來源**
- 標題：NVIDIA/SkillSpector
- 作者／機構：NVIDIA
- 連結：https://github.com/NVIDIA/SkillSpector

#NVIDIA #AIAgent #CyberSecurity #OpenSource #VulnerabilityScanning #LLM #MCP #PromptInjection #StaticAnalysis #SkillSpector
