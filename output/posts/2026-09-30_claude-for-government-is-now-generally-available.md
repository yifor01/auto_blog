---
title: Claude for Government is now generally available
source: Claude Blog
url: https://claude.com/blog/claude-for-government-is-now-generally-available
model: claude-code/sonnet
generated_at: '2026-09-30T21:33:57.242836'
pinned: true
---

📌 【Anthropic 官方發布】Claude for Government 正式開放，FedRAMP High 環境全面上線

TL;DR：Claude for Government 結束公測，聯邦與州政府機關即日起可直接採購導入。

當商用市場已經習慣用 AI 助手處理程式碳寫、文件審閱時，政府機關卻常被合規要求卡在門外。Anthropic 這次的重點，就是把「跟商用客戶一樣的能力」搬進一個通過 FedRAMP High 認證的環境裡。

🤔 **從公測到正式上線，鎖定聯邦與州政府**

Claude for Government 自今年 7 月起進入公測，如今正式開放給聯邦與州政府機關使用。素材強調，機關端取得的能力與 Anthropic 商用客戶相當，且新功能會依循商用版的發布節奏推送，不會因為走政府專用環境而落後。同步進入早期存取階段的還有 Claude Code CLI 與 Claude for Microsoft 365，透過相同的環境與管理控制項提供。

🧩 **治理設計，貼合政府機關的組織與稽核需求**

在功能面，機關人員可以直接在桌面端操作 Claude，搭配 skills、plugins 與 projects 處理備忘錄撰寫、RFP 審查、案件處理等工作；工程團隊則可用 Claude Code 建構與現代化支撐公共服務的軟體系統。

管理面的設計看得出是針對政府採購與 ATO（Authorization to Operate）流程量身打造：
- 計費採「用量制」而非席位費，機關以固定增量付費，並設有不可超支的硬上限（not-to-exceed cap）。
- 管理員可依部門設定使用者分層、模型限制與支出上限，並在餘額偏低前收到燃盡（burndown）警示。
- 部門層級的管理員可將預付額度分配給下轄機構，各自管理使用者；機關可串接自己的身分識別提供者做 SSO，並用 SCIM 群組對應設定速率限制、額度上限與可用模型。
- 所有管理操作都會記錄在稽核日誌中供機關管理員檢視，Anthropic 端的敏感操作則需要雙人核准；用量匯出僅包含計量資料，對話紀錄留在機關自管的裝置上，方便回應 ATO 與督察長（IG）的查核需求。

💡 **不需要額外綁雲端服務商**

素材特別點出，機關不需要另外建立雲端服務商的關係就能開始使用；既有客戶可以直接切換到桌面應用程式，並透過應用內匯入功能帶走既有的對話紀錄。應用程式也支援透過機關標準的 MDM 平臺部署，降低 IT 團隊導入的門檻。

🎯 **實務啟示**

對於已經在觀望政府雲合規方案的工程團隊來說，這代表可以用熟悉的 Claude Code 工作流程，直接套用在受管制的政府專案上，而不必重新適應一套閹割版工具。採購與資安人員也能提早評估其審計日誌與雙人核准機制是否滿足自身機關的 ATO 要求。

🔗 **來源**
- 標題：Claude for Government is now generally available
- 作者／機構：Anthropic
- 連結：https://claude.com/blog/claude-for-government-is-now-generally-available

#Anthropic #ClaudeForGovernment #FedRAMP #PublicSector #ClaudeCode #GovTech #AICompliance #EnterpriseAI #AIProcurement #GovernmentIT
