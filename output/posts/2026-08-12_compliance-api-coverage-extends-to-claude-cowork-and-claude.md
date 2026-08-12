---
title: Compliance API coverage extends to Claude Cowork and Claude Code
source: Claude Blog
url: https://claude.com/blog/compliance-api-cowork-and-claude-code
model: claude-code/sonnet
generated_at: '2026-08-12T07:23:32.158660'
pinned: true
---

📌 【Anthropic 產品更新】Claude Code 與 Cowork 也能被稽核了

TL;DR:Claude 的 Compliance API 擴大涵蓋 Cowork 與 Claude Code,企業合規團隊可用同一介面拉取工作階段紀錄。

企業導入 AI 工具時,合規團隊最怕的不是工具本身不好用,而是「看不到」員工到底用它做了什麼。Anthropic 這次補上了 Claude 產品線中的一塊缺口。

🤔 **稽核缺口:Cowork 與 Claude Code 原本不在合規視野內**

根據素材說明,Claude 的 Compliance API 目前已擴大涵蓋 Cowork(桌面版、網頁版與行動版)以及 Claude Code(CLI 與桌面版),此功能對 Claude Enterprise 客戶開放為 beta 測試。在此之前,安全與合規團隊仰賴 Compliance API 查看 Claude 在組織內的使用狀況以進行稽核(audits)與電子證據開示(eDiscovery),但 Cowork 與 Claude Code 的工作階段並不在這套稽核機制的覆蓋範圍內。

🧩 **新端點如何運作**

新的 session 端點會為每個 Cowork 與 Claude Code 工作階段回傳一份整合的、伺服端託管的逐字稿(transcript),將提示詞(prompt)、回應與工具活動一併收錄在單一 session 紀錄中。每筆 session 紀錄包含兩類資料:

- **Session content**:提示詞與回應、工具呼叫內容(涵蓋 web 與 MCP)、skills 與 artifacts 內容,皆以逐字稿文字形式呈現。
- **Session metadata**:已驗證的使用者 ID 與電子郵件地址、組織 ID、session 與訊息層級的 ID,以及時間戳記。

素材也提到,這次擴充是「附加式」(additive)的,原本透過 Compliance API 拉取的資料不受影響;已經在使用 OpenTelemetry 匯出資料的組織,也能讓 Compliance API 與其並行運作,不需額外建置基礎設施。

⚠️ **目前 beta 版尚未涵蓋的範圍**

素材明確列出這次 beta 尚未涵蓋:透過網頁使用的 Claude Code、透過 Claude Platform 存取的 Claude Code,以及在 Amazon Bedrock、Google Cloud Vertex AI 或 Microsoft Foundry 上執行的工作階段。

🎯 **實務啟示**

若你的組織已經是 Claude Enterprise 客戶且已啟用 Compliance API,可以直接查詢新的 session 端點,無需另外建置整合;若尚未啟用,則需要先參考官方文件開通。對於已將 Claude Code 或 Cowork 導入日常開發流程的團隊,這項更新代表合規與安全稽核終於能涵蓋到「AI 輔助開發」這一塊,對需要滿足稽核或法規要求的企業會是實質幫助。

🔗 **來源**
- 標題:Compliance API coverage extends to Claude Cowork and Claude Code
- 作者/機構:Anthropic
- 連結:https://claude.com/blog/compliance-api-cowork-and-claude-code

#Anthropic #Claude #ClaudeCode #ClaudeCowork #ComplianceAPI #EnterpriseAI #AIGovernance #eDiscovery #SecurityCompliance #DevTools
