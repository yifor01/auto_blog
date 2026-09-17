---
title: Cloudflare/Security-Audit-Skill
source: Hacker News
url: https://github.com/cloudflare/security-audit-skill
model: claude-code/sonnet
generated_at: '2026-09-17T20:31:09.522051'
score: 104
---

📌 Cloudflare 開源：讓 Coding Agent 變成資安稽核員

TL;DR：Cloudflare 開源六階段安全稽核 skill，用對抗式驗證把 agent 的幻覺漏洞壓到最低。

讓 AI agent 幫你找程式碼漏洞聽起來很誘人，但沒有結構化流程約束，它很容易把「可能有問題」寫成「確認漏洞」。Cloudflare 開源的 security-audit-skill，正是為了解決這個信任問題而生。

🤔 **從單一 repo 起步的稽核框架**

這個 skill 是 Cloudflare 用來建構其漏洞發現框架（在部落格〈Build your own vulnerability harness〉中描述）的起點。原始的 harness 後來演化成一套多階段、跨整個機群的系統，而這個開源 skill 保留了最初單一 repo 版本的核心流程，讓任何使用 coding agent 的人都能套用同一套稽核方法。

🧩 **六階段流程，責任分離是核心設計**

整個稽核拆成六個階段：Reconnaissance（繪製架構、信任邊界、輸入介面，寫入 architecture.md 與 coverage-ledger.json）、Coverage-led hunting（依覆蓋清單指派獨立的 hunter agent，並用 coverage critic 找出遺漏）、Candidate validation（每個候選漏洞都交給一個全新的 verifier 嘗試證偽）、Structured output（產出 confirmed / needs_validation / rejected 三種紀錄，並用 schema 驗證）、Independent record verification（獨立 agent 再次驗證最終的來源證據，重大修改需再經一輪獨立驗證）、Target-neutral reporting（依驗證後紀錄產出 REPORT.md、FINDINGS-DETAIL.md、NEEDS-VALIDATION.md）。

三種判定的邊界很明確：confirmed 需要完整的來源追溯與有界限的實際觀測結果；needs_validation 代表存在一個明確但尚未解決的事實，且不給嚴重性評級；rejected 則是已被證偽的候選。設計原則上，Cloudflare 強調「只確認已證實的邊界失效」、「驗證漏洞的 agent 絕不是發現漏洞的那個 agent」、「嚴重性必須來自實際影響，而非偏離檢查清單」，以及「深度防禦缺口不算漏洞」——若上層防護已擋下攻擊，下層缺失只算加固建議。官方也提到，在他們的測試中，單次執行大約只能找到多次重複執行合計發現漏洞數的一半。

📌 **怎麼用**

透過 Skills CLI 安裝：

```
npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit
```

加上 `--global` 可做使用者層級安裝。安裝後，只要對 agent 提出類似「security audit this codebase」「find security vulnerabilities in ./src」的請求即可觸發。直接要求稽核或滲透測試會進入完整稽核模式；未指定輸出目錄時預設寫入 `~/security-audit-skill/<repo-name>/run-<N>`，只有在明確指定且該目錄被版本控制忽略時，才會寫進目標 repo 內部。

⚠️ **執行需要沙箱環境，缺了它結果只能停在待驗證**

這個流程需要一個支援工具呼叫與平行子代理的 coding agent、Node.js（跑零依賴的驗證腳本），以及一個系統層級強制隔離的沙箱，用於執行目標程式碼相關的建置、測試、fuzzing、瀏覽器與模擬器。沙箱必須關閉對外連網、使用清理過的白名單環境、限制資源，並只允許寫入指定的暫存路徑。若沒有這些控制，工作流程會把相關線索保留在 needs_validation，而不會去實際執行目標程式碼。

🎯 **實務啟示**

想在自己的程式碼庫上跑一輪 AI 資安稽核，這個開源 skill 提供了現成、責任分離明確的流程骨架，比自己臨時拼湊 prompt 可靠得多；但務必先準備好隔離沙箱，且官方也建議多跑幾輪以提升覆蓋率，別指望單次執行就能找齊漏洞。

🔗 **來源**
- 標題：Cloudflare/Security-Audit-Skill
- 作者／機構：Cloudflare（Hacker News 使用者 donk8r 提交）
- 連結：https://github.com/cloudflare/security-audit-skill

#Cloudflare #SecurityAudit #AIAgent #OpenSource #AppSec #VulnerabilityResearch #CodingAgent #DevSecOps #LLMSecurity #PenTesting
