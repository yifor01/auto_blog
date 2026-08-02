---
title: 'Anthropic Releases Claude Security Plugin for Claude Code in Beta: A Multi-Agent
  Vulnerability Scanner That Runs in Your Terminal'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/22/anthropic-releases-claude-security-plugin-for-claude-code-in-beta-a-multi-agent-vulnerability-scanner-that-runs-in-your-terminal/
model: tencent/hy3:free
generated_at: '2026-07-23T08:21:21.676556'
score: 87
---

這篇內容屬於**產業新聞**，重點在於 Anthropic 發布的新工具功能、運作機制與安裝方式。

---

📌 【Anthropic Beta 版新功能】在終端機內用 Multi-Agent 進行安全性掃描

TL;DR：Anthropic 推出 Claude Security 外掛，透過多代理（Multi-Agent）機制在 Claude Code 中執行漏洞掃描。

🔐 **從全專案掃描到 Commit 前檢查，都在終端機完成**

Anthropic 推出了 Claude Security 外掛（目前處於 Beta 階段），這是一個能在現有的 Claude Code session 中執行的多代理漏洞掃描工具。使用者可以選擇對整個程式碼庫進行全面掃描，或者在提交（commit）前，直接針對變更內容進行檢查。

🧩 **以 JavaScript 協作驅動的多代理工作流**

該外掛的核心是一個動態工作流，透過 JavaScript 協作指令碼將任務分配給不同的子代理（subagents）。整個掃描流程包含六個階段，其中「研究（Research）」階段會針對四個固定類別進行檢查：

- injection-and-input（注入與輸入）
- auth-and-access（身分驗證與存取）
- memory-and-unsafe（記憶體與不安全操作）
- crypto-and-secrets（加密與機密資訊）

💡 **針對記憶體安全語言的自動最佳化**

為了提升效率，該工具具備智慧判斷能力：如果元件完全由記憶體安全語言（如純 Python 或 TypeScript）撰寫，系統會自動捨棄「memory-and-unsafe」檢查類別，僅執行另外三個檢查維度。

📊 **四種效能層級與動態配置**

掃描的規模由四種努力程度（effort tiers）決定：low、medium、high 與 max。系統會根據選擇的層級，動態調整以下參數：

| 參數 | Low / Medium | High / Max |
| :--- | :--- | :--- |
| 最大元件數量 | 12 個 | 24 個 |
| 研究人員數量 (Researchers) | 1 位 | 2 位 |
| 補缺掃描次數 (Gap-fill sweeps) | 0 (Low) / 1 (Medium) | 2 |

若掃描範圍僅限於有限的範圍或較小的差異（diff），系統會自動縮減為單一研究人員配置，以確保評估過程精確且不浪費資源。

🛠️ **如何安裝與使用**

使用者只需透過單一指令 `/claude-security` 即可開啟包含三種任務選單的選單。

安裝步驟如下：
1. 若系統找不到 marketplace，請先執行：`/plugin marketplace add anthropics/claude-plugins-official`
2. 接著從官方 marketplace 安裝該外掛即可。

目前該外掛版本為 0.10.0，原始碼已公開於 `claude-plugins-official` 儲存庫。

🎯 **實務啟示**

這項工具將安全性檢查從傳統的獨立工具，整合進了開發者的開發流程（Workflow）中。工程師可以將掃描結果轉化為 patch 檔案，並親自進行審核與套用，實現「AI 發現問題 $\rightarrow$ 人類審核 $\rightarrow$ 應用修補」的閉環流程。

🔗 **來源**
- 標題：Anthropic Releases Claude Security Plugin for Claude Code in Beta: A Multi-Agent Vulnerability Scanner That Runs in Your Terminal
- 作者／機構：Michal Sutter @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/22/anthropic-releases-claude-security-plugin-for-claude-code-in-beta-a-multi-agent-vulnerability-scanner-that-runs-in-your-terminal/

#AI #Anthropic #ClaudeCode #Cybersecurity #MultiAgent #LLM #SoftwareDevelopment #DevSecOps #MachineLearning #Programming
