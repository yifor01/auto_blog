---
title: More visibility and control over Claude Enterprise for security teams
source: Claude Blog
url: https://claude.com/resources/articles/claude-enterprise-security-updates
model: claude-code/sonnet
generated_at: '2026-11-05T22:50:44.807577'
pinned: true
---

📌 Claude Enterprise 新增安全中心與推論鉤子，資安團隊有了統一管理臺

TL;DR：Anthropic 為 Claude Enterprise 加入 security center、inference hooks、跨組織集中管理與更多存取控制。

資安團隊最怕的往往不是 AI 做錯了什麼，而是根本不知道 AI 在公司裡做了什麼。Anthropic 這次把能見度和控制權，直接攤在一個管理頁面上。

🤔 **資安團隊真正需要的三件事**
素材點出的需求很直接：看懂 Claude 目前怎麼設定、知道它在公司裝置上做了什麼、確認資料怎麼被處理。這一輪更新對應的就是這三點。

🧩 **Security center：一頁對照 Anthropic 建議設定**
這是 Organization settings 裡的新頁面，把 chat、Cowork、Claude Code 的安全設定集中列出，與 Anthropic 的建議設定值逐項對照，顯示目前值、建議值與修改連結，並標示哪些設定是新增或近期變更的。頁面每次載入都會重新檢查自動化項目，開了 Compliance API 的組織也能透過 API 讀到同樣的結果。Attestations 功能讓多位管理員可以一起完成一次安全審查紀錄，包括確認目前狀態、接受風險、標記問題；整頁內容也能下載成報告給稽核人員，報告會標明哪些項目是自動檢查、哪些是人工確認。目前是 beta，素材也特別說明這只是 Anthropic 的建議指引，不是合規認證或任何法規保證。

🧩 **Inference hooks：讓既有 DLP 政策套用在 Claude 身上**
兩種 hook 都已正式發布（GA）：prompt hooks 會在支援的產品送出 prompt 前，先交給企業自己的安全工具檢查；pre-tool-call hooks 則在工具呼叫真正執行前先做檢查。重點是企業不用重寫政策，只是把既有的資料外洩防護（DLP）規則接到 Claude 的使用流程上。

🧩 **Centralized management：跨組織的單一身分與存取控制台**
在 admin.claude.com 新增的管理臺，讓代表整個公司的 parent organization 可以一次管理旗下所有 Claude Enterprise／Claude Platform 組織的公司層級設定，包括 SSO、SCIM 目錄同步、網域驗證、群組與 Compliance API 金鑰。新增了兩種角色：parent organization owner 可以管理一切，包含指派 owner／admin 角色；parent organization admin 則除了角色指派以外都能管理。公司也可以同時串接多個 identity provider，被併購的公司可以保留原本的 provider，或逐個網域慢慢遷移過去。每個子組織仍保留自己的成員、角色與組織層級安全控制（例如 IP allowlist、tenant restriction、session 時長）；parent 層級的角色預設不會自動取得子組織內部的存取權，但在 parent 層建立的 Compliance API 金鑰可以跨組織讀取資料。目前是 beta，且設定完成後無法復原，官方特別提醒要先確認好 parent organization admin 名單再開始設定。

📊 **存取控制：一鍵登出與防止 Shadow IT**
資安團隊現在可以用單一次 Admin API 呼叫，把某位成員從所有瀏覽器與裝置上登出，而不需要把這個人從組織裡移除；這會結束該成員在各處的登入 session（像 Claude Code 之後會要求重新登入），但不影響 API 金鑰、已在跑的雲端 session 或排程任務，之後該成員仍可重新登入。Enterprise 管理員現在可以自行管理 IP allowlist，不需要再透過 Anthropic 處理；也可以直接設定受管電腦上最常用的 Claude Desktop 設定，不需要走裝置管理推送流程，並可封鎖受管電腦上的個人或其他外部 Claude 帳號，用來防止 Shadow IT。Owner 另外還能限制哪些 workspace 資料夾可以搭配 Claude 使用。

🧩 **Cowork 虛擬機內的 EDR 整合**
Cowork 與 unified Claude 在本機執行時，會把 shell 指令與程式碼放進電腦上一個隔離的虛擬機裡執行，做額外保護。現在管理員可以把公司自己的 EDR（端點偵測與回應）感應器裝進這個虛擬機，活動記錄會回報到資安團隊原本就在用的同一套監控主控臺，但這只涵蓋使用者電腦上的這個虛擬機，不包含雲端上執行的 Cowork session。設定方式是透過 macOS／Windows 的裝置管理，虛擬機每次啟動時 Claude 會先驗證感應器套件的廠商簽章才安裝，感應器以偵測模式運作，只回報不會主動阻擋。

⚠️ **目前多為 beta，且非合規保證**
Security center、centralized management、Admin API 登出、自助 IP allowlist、Claude Desktop 集中設定，以及 Cowork 的 EDR 整合（目前限 macOS／Windows）都還在 beta 階段；已 GA 的只有 inference hooks。

🎯 **實務啟示**
這組更新把「AI agent 存取了什麼資料、執行了什麼動作」變成可以被企業既有 DLP 與 EDR 工具鏈治理的對象，是導入 agentic 工具時常見的治理缺口。如果公司正在評估導入，建議先盤點 inference hooks 要接哪個安全廠商、再規劃 SSO／SCIM 跨組織遷移與 parent organization 的角色名單，畢竟 centralized management 一旦設定完成就無法復原。

🔗 **來源**
- 標題：More visibility and control over Claude Enterprise for security teams
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/claude-enterprise-security-updates

#Anthropic #Claude #EnterpriseSecurity #ClaudeEnterprise #DLP #SecurityOps #AdminAPI #IdentityManagement #EDR #Compliance
