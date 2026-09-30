---
title: 'One Bad Prompt Took Down a Company’s Salesforce: RSA’s Jim Taylor on Agent
  ID and Taming the 4,000 Shadow AI Agents Hiding in Your Enterprise'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/29/rsa-launches-agent-id-to-discover-secure-and-govern-ai-agents-in-regulated-industries/
model: claude-code/sonnet
generated_at: '2026-09-30T21:49:26.719580'
score: 81
---

📌 一句提示詞，如何讓一家公司的 Salesforce 整套當機

TL;DR：RSA 推出 Agent ID，要解決企業裡數千個「影子 AI 代理」無人管的治理黑洞。

沒有駭客，沒有惡意程式碼，只有一位客服人員對 AI 代理說了一句話：「去 Salesforce 把所有資料抓下來，做客戶健康度圖表。」結果這個代理開始把整個 Salesforce 資料庫下載一空，Salesforce 的防禦系統判定這是攻擊流量，直接關閉了該公司的實例，還警告對方疑似遭受阻斷服務攻擊。RSA 總裁暨產品與策略長 Jim Taylor 在 The AI Conference 上分享這個案例時強調：「那位客服人員什麼都沒做錯。」

🤔 **代理不是服務帳號，它們不會累**

Taylor 指出 AI 代理與傳統服務帳號的根本差異：代理是動態的，一旦任務描述不夠精確，它就會自行判斷「必要手段」去完成任務，而且不分晝夜持續執行。更麻煩的是代理會隨時間累積權限與資料存取，卻很少有人回頭檢查。Gartner 預估，一般《財星》500 大企業到 2028 年將運行約 15 萬個 AI 代理，而 2025 年時這個數字還不到 15 個；目前僅 13% 的組織認為自己具備適當的代理治理能力。一家中型跨國銀行原本告訴 RSA「我們沒有代理，政策禁止」，但實際稽核後發現企業內部竟跑著超過 4,000 個代理。根據 IBM 的數據，涉及影子 AI 的資安事件平均比一般事件多花費 67 萬美元處理成本。

🧩 **Discover、Secure、Govern 三模組**

RSA Agent ID 可獨立部署，也能整合進 RSA Unified Identity Platform：

- **Discover**：透過 CrowdStrike、Zscaler 等連接器即時掃描端點、裝置、網路與應用程式，找出所有代理與 MCP 伺服器（不論是否為公司核准），將每一個都註冊為具名擁有者、風險等級與生命週期狀態的第一級身分，並與 Microsoft Entra ID、Okta、AWS IAM 等既有身分供應商掛鉤。
- **Secure**：一套內嵌的 AI/MCP 閘道，會針對每一次工具呼叫在工具與參數層級檢查政策，符合政策的放行，違反的擋下，高風險操作則升級給登記的擁有者，透過抗釣魚憑證的頻外（out-of-band）管道核准，代理本身無法觸及該管道。
- **Govern**：記錄每一次受治理的操作，將證據對應到十種法規與產業框架，並串流至客戶的 SIEM。

💡 **不是無限彈窗，而是風險引擎打分**

Taylor 特別批判現行「核准疲勞」的做法：「一天一百個彈窗只是在邀請使用者按下同意，這本身就是另一種阻斷服務攻擊。」Agent ID 改用風險引擎，針對使用者行為是否符合預期、操作屬於讀取或寫入、目標資料與端點的敏感度三個維度打分，只有超過門檻的操作才會交由人工判斷，門檻本身由客戶依自身業務風險定義。針對多代理委派的情境，系統會在工具執行當下攔截並強制「繼承式權限模型」：子代理只能使用母代理被授予的權限，無法借用其他代理的權限，藉此堵住透過委派鏈提權的路徑。

⚠️ **RSA 也坦承自己不是萬能**

被問到程式碼代理從儲存庫偷取其他團隊 API 金鑰之類的閘道繞過情境，Taylor 直言：「我們沒有那麼神。」他認為 API 閘道、防火牆與流量檢測等既有安全機制仍須並存，「我們不需要重新發明資安，而是要在既有有效的防護上疊加代理層級的安全。」核心設計原則是讓授權管道與代理執行管道分離：「叫代理去把考試考好，最簡單的方法就是去偷答案。」

🎯 **給工程團隊的啟示**

Taylor 建議 CISO 評估時先問自己三個問題：企業內到底有多少代理在跑、誰擁有它們、出事時能不能立刻關掉。多數團隊答不出來。他建議的試點方式是先串接幾個關鍵系統跑一次 Discovery，「結果通常會讓他們大吃一驚」，這也是後續指派負責人與制定政策的起點。RSA Agent ID 的 Discover 與 Secure 預計 2026 年 11 月 16 日全面上市，Govern 則排在 2027 年上半年。

🔗 **來源**
- 標題：One Bad Prompt Took Down a Company's Salesforce: RSA's Jim Taylor on Agent ID and Taming the 4,000 Shadow AI Agents Hiding in Your Enterprise
- 作者／機構：Jean-marc Mommessin, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/29/rsa-launches-agent-id-to-discover-secure-and-govern-ai-agents-in-regulated-industries/

#AIAgents #AgentSecurity #ShadowAI #IdentitySecurity #RSA #EnterpriseAI #MCPSecurity #Governance #CISO #AgenticAI
