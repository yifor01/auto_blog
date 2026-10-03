---
title: Apple changes full-disk access permissions to curb abuse from AI agents
source: Ars Technica AI
url: https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/
model: claude-code/sonnet
generated_at: '2026-10-03T19:59:54.589065'
score: 72
---

📌 Apple 緊縮全磁碟權限，起因是一次 AI 代理誤讀訊息

TL;DR：Meta 的 Muse 被曝讀取使用者私人訊息，逼得 Apple 修改 macOS 權限機制。

你授權一個 AI 助理「存取檔案」,但它實際上讀到的,可能遠比你想像的多。這正是促使 Apple 出手調整 macOS 隱私權限設定的起點。

🤔 **一條沒被授權的訊息,引爆信任危機**

科技專欄作家 Jason Aten 兩週前指出,Meta 的通用型 AI 代理 Muse 向他發出一則通知,內容提及他與同事在 Apple Messages 上的對話串。Aten 表示自己從未授權 Muse 讀取訊息,原以為這部分對他來說是不可觸及的。社群媒體隨後出現大量聲音呼應他的說法,認為擁有行事曆、電子郵件、訊息、購物帳戶存取權的 AI 助理,就像電鋸之類的動力工具:有用,但若使用不慎會造成真正的損害。

🧩 **問題出在兩道權限的疊加**

Meta CTO David Singleton 隨後出面回應,解釋 Muse 要存取 Apple Messages,使用者必須手動授予兩項權限:一是 macOS 系統層級的「完整磁碟存取權」(full-disk access),二是在 Muse 內另外開啟一個 Messages 連接器設定。Apple 則在上週五宣布,將修改這項隱私設定,阻止第三方開發者濫用它來存取訊息紀錄。

💡 **權限授予的認知落差,才是真正的風險**

這起事件的關鍵不在於 Muse 是否「違規」讀取了訊息,技術上使用者確實完成了兩道授權。問題在於,一般使用者對「完整磁碟存取權」這個系統級權限實際涵蓋的範圍,往往缺乏清楚認知,等於在不自覺中把遠超預期的資料暴露給第三方代理。

🎯 **實務啟示**

對正在設計 AI 代理的工程師來說,這是一個關於權限粒度的警示:系統層級的broad permission(如完整磁碟存取)一旦與應用內部的功能開關疊加,使用者很容易低估自己實際授予的存取範圍。設計代理功能時,應該朝最小權限原則靠近,並在 UI 上清楚告知每項權限實際能讀到什麼,而不是把責任全部交給一次性的系統彈窗。

🔗 **來源**
- 標題：Apple changes full-disk access permissions to curb abuse from AI agents
- 作者／機構：Dan Goodin／Ars Technica
- 連結：https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/

#AppleSecurity #macOS #AIAgent #PrivacyByDesign #MetaAI #Muse #DataPrivacy #AgenticAI #LeastPrivilege #TechPolicy
