---
title: Vercel Introduces ‘Is Agentic’, a Free Agent-Readiness Scoring Tool That Audits
  Public Websites Using Ora’s 100+ Checks
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/23/vercel-introduces-is-agentic-a-free-agent-readiness-scoring-tool-that-audits-public-websites-using-oras-100-checks/
model: claude-code/sonnet
generated_at: '2026-08-24T06:32:03.357587'
score: 92
---

📌 Vercel推出免費工具，幫網站打AI代理友善度分數

TL;DR：Vercel與Ora合作推出免費工具Is Agentic，用118項檢查為網站打分，評估AI agent能否順利存取。

隨著愈來愈多任務由AI agent代為完成——瀏覽網站、比價、填表、串接API——網站是否「對agent友善」開始變成一個可以被量化的問題。Vercel推出的Is Agentic，正是要回答「AI agent能不能順利發現、存取、理解並使用這個網站」。

🤔 當「使用者」變成AI agent

素材指出，掃描與評分由Ora（era labs旗下的agent experience研究公司）執行，Vercel則負責介面、報告頁面、儲存，以及把檢查結果分組成最終顯示分數。整個服務目前完全免費，沒有付費方案、訂閱費或按報告計費，公開網站、唯讀API、CLI與MCP伺服器都不需要API金鑰或帳單帳號。使用方式很直接：在瀏覽器輸入URL，或直接跑CLI指令即可產生報告。

🧩 四層檢查，重新分組成自己的分數

Ora的方法論把agent的使用歷程拆成四層：Discovery（發現，20分／15項檢查）、Access（存取，30分／41項檢查）、Usability（可用性，40分／56項檢查）、Payments（付款，10分／6項檢查），合計118項檢查，對應到「100+ checks」的宣稱。Ora表示這份檢查清單是從真實agent執行紀錄反推而來，而非主觀擬定。Ora另外提供字母等第：A+（95–100）、A（86–94）、B（70–85）、C（48–69）、D（28–47）、F（0–27）。

Vercel則把這些檢查重新分組成自己的顯示分數：Essential檢查共用80分池，Recommended檢查共用20分池，Emerging signals則是上限5分的加分項，缺少這類訊號不會扣分。不適用的檢查會直接排除，而非算作失敗；部分符合的項目按比例給分；同一檢查ID若在多個MCP介面重複出現，則取平均值。這套「適用性判斷」很關鍵：Recommended檢查只有在掃描證據確實偵測到API、OAuth流程、GraphQL端點、MCP伺服器、開發者入口或商務功能時才會啟用，一個單純的行銷網站不會因為沒有這些介面而被扣分。

📊 每個檢查項目都附證據與修復建議

每項檢查結果都會附上觀察到的證據，以及（如果有）具體的修復建議。素材揭露的一段實際API回應顯示，報告資料結構包含score、score_label、scanned_at、eligible_checks，以及列出每個分級已得分／可得分的score_breakdown，再加上issues陣列，每筆issue帶有id、name、details、recommendation、result與tier欄位。實際檢查ID範例包括content-no-js、agent-friendly-404、markdown-negotiation-vary、json-ld、sitemap、trust-anchors、metadata-completeness；例如404檢查要求網站回傳真正的HTTP 404狀態碼，而不是用200狀態碼回應一個空殼應用程式頁面。

報告也包含一段「觀察到的agent旅程」，呈現某次agent實際執行時卡在哪裡，但Vercel刻意把這段紀錄排除在數字分數之外，理由是單一任務無法代表所有agent的使用情境。另外，「Prompt to fix」功能可以把建議直接轉成一份可以丟給coding agent執行的實作簡報。

🧩 三種唯讀介面，方便整合進工作流

已完成的報告可以透過三種唯讀介面存取：Report API位於`/api/v1/report`，限制為每個client IP每60秒120次請求；錯誤訊息採用RFC 9457的problem details格式，附帶invalid_url、report_not_found、rate_limit_exceeded等穩定錯誤碼；OpenAPI描述是官方支援的整合合約，可透過RFC 9727 API catalog探索；若有功能棄用，會透過RFC 9745標頭公告，且Sunset時間至少提前90天通知。MCP伺服器則位於`https://is-agentic.com/mcp`，透過Streamable HTTP暴露is_agentic_get_report、is_agentic_get_methodology、is_agentic_get_developer_docs三個工具，支援MCP Apps的host還能直接渲染互動式分數卡。官方agent skill則可透過`npx skills add vercel-labs/is-agentic`安裝。

值得一提的是，Is Agentic自己的網站也實踐了它所評分的標準：報告頁面會在初始HTML回應中就渲染分數，並在`Accept: text/markdown`時提供Markdown版本，同時設定`Vary: Accept`標頭，確保共享快取不會混淆不同格式的回應。

🎯 實務啟示

對已經在營運公開網站或串接MCP伺服器、OpenAPI介面的團隊來說，這個工具最直接的用法是把`--json`輸出接進CI流程，當伺服器端渲染內容退化時直接讓建置失敗；企業則可以拿它跨業務單位比較文件站、開發者站與商務頁面的agent可用性，優先修復扣分最多、又附有具體修復建議的項目。

🔗 來源
- 標題：Vercel Introduces 'Is Agentic', a Free Agent-Readiness Scoring Tool That Audits Public Websites Using Ora's 100+ Checks
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/23/vercel-introduces-is-agentic-a-free-agent-readiness-scoring-tool-that-audits-public-websites-using-oras-100-checks/

#AIAgents #WebDev #DeveloperTools #Vercel #MCP #AgentExperience #APIDesign #OpenAPI #AIReadiness #WebStandards
