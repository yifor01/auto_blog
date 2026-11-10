---
title: 0sec Labs Open-Sources 0, an AI Security Harness With Web UI, CLI and MCP
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/08/0sec-labs-open-sources-0-ai-security-harness/
model: claude-code/sonnet
generated_at: '2026-11-10T00:51:05.012509'
score: 97
---

📌 0sec Labs 開源「0」：把滲透工具搬進 LLM Agent 的控制平面

TL;DR：瑞士團隊開源 AI 安全測試框架「0」，整合逆向工程與滲透測試工具，支援 Web UI、CLI、MCP。

滲透測試與逆向工程長年依賴一堆各自為政的工具和老練工程師的直覺，0sec Labs 這次想做的是把 LLM agent 接上這些既有工具，變成一個可重複執行、可驗證結果的控制平面。

🤔 **它不是一個模型，是一套工具調度層**

0 是一個圍繞 LLM 與安全工具建立的控制平面（control plane），本身不是模型，使用時需要自行接上模型供應商，再由 0 執行針對已授權目標的「範圍受限」工作流程。研究團隊將其描述為「自我演進、多模型的 harness」，背後由 Y Combinator 投資。架構文件訂下一條核心規則：reproduce before trusting，也就是任何發現都必須先能被重現才能被信任。

🧩 **Web 滲透走 shell-first，編譯目標另有專屬引擎**

在 Web 滲透測試的場景裡，agent 採用 shell-first 的做法，直接用 bash 搭配 curl、python3、sqlmap 操作，而不是依賴固定的 HTTP 工具集，每個發現都會被標上從「candidate」到「impact-proven」的證據分級。面對編譯後的二進位目標，則交給一個獨立於主程式之外的引擎「0verse」處理，它包裝了 Ghidra、angr 與 AFL++ 三套逆向與 fuzz 測試工具；其本地 MCP 伺服器對外開放 9 個工具，涵蓋掃描、分類（triage）、PoV（概念驗證攻擊）產生與報告產出。

模型存取採 bring-your-own 模式，API 金鑰頁面列出的供應商包含 OpenAI、Anthropic、DeepSeek、OpenRouter、Azure、Qwen、Kimi、GLM 與 Grok，另外也支援 Claude、Codex、Gemini CLI 這幾種既有 runtime。

🧩 **怎麼用：一支腳本裝起來，三種操作介面任選**

安裝只需要跑一支腳本。啟動後會直接開啟本機瀏覽器主控臺，不需要帳號登入，主控臺內含聊天介面、發現項目的佇列與看板、工作流程範本，以及技能（skills）與記憶功能。偏好無頭操作的使用者可以透過 CLI 執行相同的 workflow runner，指令包括 `0 workflow run`、`0 runs list`；想接進既有 coding agent 的話，則可以用 `0 mcp-server --workflows` 把 0 的工作流程以 MCP 伺服器形式暴露出去。

📊 **自報成績：平均每題 XBOW 挑戰約 5.2 美元**

文中列出的所有數據皆為自我回報（self-reported）。團隊公開的研究頁面提到，解出一題 XBOW 挑戰的平均成本約 5.2 美元，另外累積了超過 30 個已被合併進 Linux kernel 的 0-day 揭露，涵蓋 Bluetooth、NFC、mac802154、TIPC、mlx5e 等子系統，函式庫層級的 CVE 則包括 jsonata、node-forge、protobuf.js 與 Wireshark。

⚠️ **數字來自團隊自報，授權範圍是前提**

需要留意的是，上述所有成果數字都是 0sec Labs 自己公布的，尚未有素材外的第三方驗證資訊；而整套工具的設計前提也是「針對已授權目標」執行，這點在使用前必須謹記。

🎯 **實務啟示**

0 以 MIT OR Apache-2.0 授權開源，目前屬於研究預覽階段，開源版本本身免費、只需自付模型供應商的費用；若想要託管版本，0cloud 目前開放候補名單，提供 100 美元試用額度，並以每次 PR 安全測試 5 美元計價。對安全研究或紅隊工作流程已經大量依賴 Ghidra、angr、AFL++、sqlmap 等工具的團隊來說，這類把 LLM agent 接到既有工具鏈上、同時保留「先重現再信任」驗證紀律的開源框架，值得拿來評估能否補上自動化與報告產出這段流程。

🔗 **來源**
- 標題：0sec Labs Open-Sources 0, an AI Security Harness With Web UI, CLI and MCP
- 作者／機構：Michal Sutter（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/11/08/0sec-labs-open-sources-0-ai-security-harness/

#AISecurity #Pentesting #OpenSource #ReverseEngineering #MCP #LLM #CyberSecurity #VulnerabilityResearch #YCombinator #SecurityTools
