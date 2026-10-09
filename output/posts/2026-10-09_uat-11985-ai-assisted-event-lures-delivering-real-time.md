---
title: 'UAT-11985: AI-assisted event lures delivering real-time Google AitM phishing'
source: Talosintelligence.com
url: https://blog.talosintelligence.com/uat-11985/
model: claude-code/sonnet
generated_at: '2026-10-09T22:05:29.801039'
score: 76
---

📌 鎖定臺灣智庫的AI輔助即時釣魚攻擊

TL;DR：Talos揭露APT組織UAT-11985，用AI生成活動誘餌，對臺灣研究機構發動即時Google AitM釣魚。

如果你收到一封看起來來自知名智庫、邀你參加公開研討會的信，你會不會順手點進連結、用Google帳號登入？Cisco Talos這次抓到的攻擊，賭的正是你會。

🤔 **鎖定臺灣研究機構相關人士的APT行動**

Talos研究員Joey Chen在報告中指出，一個代號UAT-11985的APT組織，針對與臺灣研究機構有關聯的個人發動魚叉式釣魚（spear-phishing）攻擊。這起行動的特別之處在於，攻擊者並非憑空捏造釣魚內容，而是借用真實存在、公開舉辦的活動主題作為誘餌，同時冒充具公信力的學術與政策機構身分，藉此降低受害者的戒心。

🧩 **AI生成誘餌＋即時AitM，繞過登入防線**

從標題可知，這起行動結合了兩項手法：一是用AI協助產生貼合真實活動情境的誘餌內容，讓釣魚信更難被識破；二是對Google帳號發動「即時」（real-time）Adversary-in-the-Middle（AitM）釣魚。AitM本質上是攻擊者在受害者與真實登入頁面之間架設一個即時代理，當受害者輸入帳密甚至完成多因子驗證時，攻擊者能同步側錄並劫持登入後的session，進而繞過傳統一次性密碼（OTP）類型的雙因子驗證。Talos目前公開的細節仍集中在攻擊主題與冒充手法上，對於具體的技術基礎設施與受害範圍，報告並未提供更進一步的數據。

⚠️ **情資仍屬初步揭露**

必須說明的是，摘要中並未提及具體的受害人數、攻擊起止時間或完整的技術指標（IOC），因此本篇僅能就Talos已公開揭露的攻擊主題與手法輪廓進行說明，讀者若需要完整的技術細節，建議直接查閱原始報告。

🎯 **對研究機構與工程師的實務啟示**

對於任何與學術、政策研究機構有往來、或本身在相關組織任職的技術人員，這起事件提醒我們：活動邀請信、研討會通知這類「看起來很正常」的信件，正是AitM釣魚最容易得手的場景。防禦上最實際的作法，是將帳號登入從OTP類雙因子驗證，升級為具備防釣魚特性的FIDO2／passkey機制，因為AitM代理無法複製passkey背後的裝置綁定金鑰；同時也該對寄件網域、連結目標進行更嚴謹的檢查流程。

🔗 **來源**
- 標題：UAT-11985: AI-assisted event lures delivering real-time Google AitM phishing
- 作者／機構：Joey Chen @ Cisco Talos
- 連結：https://blog.talosintelligence.com/uat-11985/

#AitM #Phishing #ThreatIntelligence #CyberSecurity #APT #Taiwan #GoogleSecurity #SpearPhishing #CiscoTalos #AIThreats
