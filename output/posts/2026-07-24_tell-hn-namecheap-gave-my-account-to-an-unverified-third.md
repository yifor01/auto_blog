---
title: 'Tell HN: Namecheap gave my account to an unverified third party'
source: Hacker News
url: https://news.ycombinator.com/item?id=49028037
model: tencent/hy3:free
generated_at: '2026-07-24T08:27:10.063671'
score: 63
---

這是一篇基於 Hacker News 討論內容的產業新聞／案例分析。

📌 【安全性警示】只要「講得好聽」就能奪走帳號？Namecheap 帳號驗證機制遭質疑

TL;DR：一名資深使用者投訴 Namecheap 在未進行身分驗證的情況下，僅憑電話請求就將帳號控制權移交給第三方。

🎣 **當「求助」變成「劫持」：一個 13 年老客戶的噩夢**

對於一名擁有 13 年經驗的使用者來說，帳號安全性本應是理所當然的保障。然而，這名使用者在 Hacker News 分享了一段令人震驚的經歷：他為大學社團代付域名費用，結果社團接班人僅憑一通電話，就在完全沒有進行身分驗證的情況下，成功奪走了他的 Namecheap 帳號控制權。

🤔 **驗證流程的邏輯漏洞**

這起事件的起因非常單純，卻暴露了服務商在處理客戶請求時的嚴格度差異：

1. **主動警示被忽視**：當社團接班人嘗試重設密碼時，原使用者立即收到重設郵件，並主動向 Namecheap 客服提交支援單（Support Ticket）申報「我並未發起此操作」。
2. **雙重標準的驗證**：Namecheap 客服先前確實有能力透過電話聯絡原使用者以確認其申報內容，但在面對社團接班人的電話請求時，卻完全放棄了對帳號擁有者的核實。
3. **無須驗證的許可權移轉**：該接班人僅憑口頭聲稱「該域名所登記的姓名與地址屬於我們社團」，Namecheap 便直接修改了原使用者的密碼以及帳號關聯的電子郵件地址。

⚠️ **這不只是社交工程，更是嚴重的安全性漏洞**

原使用者指出，這甚至稱不上是複雜的「社交工程（Social Engineering）」，而是一個顯而易見的系統性漏洞。當服務商可以輕易地因為「對方說得很有禮貌」或「要求很堅定」就更改帳戶核心資產（如電子郵件與密碼）時，該平臺的安全性防線便形同虛設。

💡 **資產轉移的教訓：分散風險與備援意識**

由於這次事件，該使用者已將其十幾個最關鍵的域名從 Namecheap 轉出。這提醒了所有數位資產管理者：
- **避免單一依賴**：將最關鍵的域名與重要帳號分散在不同的註冊商。
- **實施嚴格的轉移流程**：對於涉及域名所有權的變更，應要求多重身分驗證（MFA）或更嚴格的法律檔案審核，而非僅憑電話口頭說服。

🎯 **實務啟示**

對於工程師與系統管理員而言，這是一個警示：在設計任何涉及「許可權變更」或「身分驗證」的系統時，絕對不能僅依賴「客服的判斷」或「單一溝通管道」來確認身分。任何涉及資產所有權的變更，都必須建立在不可抵賴（Non-repudiation）的技術驗證機制之上。

🔗 **來源**
- 標題：Tell HN: Namecheap gave my account to an unverified third party
- 連結：https://news.ycombinator.com/item?id=49028037

#CyberSecurity #Namecheap #DataPrivacy #AccountTakeover #DomainRegistration #InfoSec #SocialEngineering #CyberAttack #TechNews #SecurityVulnerability
