---
title: vercel-labs/deepsec
source: GitHub Trending
url: https://github.com/vercel-labs/deepsec
score: 108
model: tencent/hy3:free
generated_at: '2026-07-21T08:23:01.876774'
---

📌 【Vercel Labs 開源專案】DeepSec：用 Agent 驅動的大規模程式碼漏洞掃描工具

TL;DR：DeepSec 是由 Agent 驅動的漏洞掃描器，專為大規模 Repository 設計，能找出隱藏已久的深層問題。

🤔 **傳統掃描難以發現隱藏的深層問題**

在大型專案中，許多嚴重的安全性漏洞可能已經潛伏在程式碼庫中很久。傳統工具往往難以處理複雜的邏輯錯誤，而 DeepSec 的設計初衷，就是透過 Agent（代理）驅動的模式，針對現有的大規模 Repository 進行按需（on-demand）審查，目標是挖掘出那些極難被發現的安全性問題。

🧩 **透過 Agent 驅動與平行處理提升效能**

DeepSec 的運作核心在於其高度的自動化與擴展性：

- **Agent 驅動與思考深度**：DeepSec 配置使用最頂尖的模型，並支援最高層級的「思考（Thinking）」模式（可透過 `--thinking-level` 參數進行調整）。
- **高成本與高回報**：由於使用了高強度的模型運算，針對大型程式碼庫的掃描成本可能高達數千甚至數萬美元，但使用者回饋，這種成本在快速修補漏洞所帶來的價值面前是非常值得的。
- **平行與斷點續傳**：針對大型專案，工作負載會分散到多臺工作機（worker machines）進行平行處理。若掃描過程中斷或發生錯誤，只需重新執行指令，DeepSec 會自動跳過已分析過的檔案，從上次中斷的地方繼續執行。

🛠️ **快速上手流程**

若要在你的基礎設施中執行 DeepSec，流程如下：

1. 在目標 Repository 根目錄執行 `npx deepsec init` 以建立專案設定。
2. 進入 `.deepsec` 目錄並執行 `pnpm install` 安裝工具。
3. **與 Agent 協作**：這是 DeepSec 的獨特之處。你需要啟動你偏好的 Coding Agent，並指令它：
   - 閱讀 `.deepsec/node_modules/deepsec/SKILL.md` 以理解工具。
   - 閱讀 `.deepsec/data/<id>/SETUP.md` 並遵循其指令。
   - 讓 Agent 快速瀏覽 README、`AGENTS.md` 或 `CLAUDE.md` 以及部分代表性程式碼，隨後依照指示完成後續操作。

🎯 **實務啟示**

DeepSec 將掃描模式從「靜態分析」轉向「Agent 代理分析」，這意味著安全工程師可以利用 LLM 的推理能力來理解複雜的業務邏輯，進而發現傳統工具無法察覺的邏輯漏洞。然而，開發者在使用時必須預留充足的預算，因為高層級的思考模式會帶來顯著的 API 成本。

🔗 **來源**
- 標題：vercel-labs/deepsec
- 連結：https://github.com/vercel-labs/deepsec

#AI #Security #DeepSec #VercelLabs #CyberSecurity #AIAgent #OpenSource #VulnerabilityScanning #LLM #DevSecOps
