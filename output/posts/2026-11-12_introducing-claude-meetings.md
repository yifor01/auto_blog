---
title: Introducing Claude Meetings
source: Claude Blog
url: https://claude.com/resources/articles/claude-meetings
model: claude-code/sonnet
generated_at: '2026-11-12T23:04:19.020644'
score: 85
---

📌 【Anthropic 新功能】Claude 現在會「坐」進你的視訊會議裡

TL;DR:Claude Meetings 讓 Claude 以可見參與者身分加入視訊會議,邊聽邊做筆記、邊幫你建文件。

開會開到一半想查去年活動預算多少,通常要有人默默切視窗去搜 Jira 或試算表。Anthropic 最新推出的 Claude Meetings(目前為 beta)想解決的就是這個場景:Claude 直接坐在會議裡,聽你們討論,當場動手做事。

🤔 **會議裡多了一個會做事的參與者**

Claude Meetings 目前在 Team 與 Enterprise 方案上開始以 beta 形式推出,支援的視訊平臺目前是 Google Meet,其他平臺支援正在開發中。團隊成員可以用語音或文字在會議中直接問 Claude 問題,預設 Claude 會以文字形式回答,並可以在取得使用者授權後動用已連接的工具。

🧩 **邊開會邊建文件、白板,會後自動留下紀錄**

文章給出的使用情境是這樣的:團隊在討論一場客戶活動的規劃,有人說「Claude,幫我們開一份這個計畫的文件」,Claude 會把目前討論內容整理成文件,其他與會者可以邊聽邊直接編輯這份文件。討論到預算時,有人問 Claude 去年活動花了多少錢,Claude 會先徵求同意才去查詢,查到後貼到會議聊天室,並與目前的計畫做對比。討論時程時,有人要求把進度排上白板,團隊就能在白板上和文件並行協作。會議結束前,只要有人開口要求,Claude 就能整理一份會議摘要分享給團隊。會後,所有筆記、行動項目、計畫與白板都會留在 claude.ai 上這場會議專屬的頁面裡,之後也可以回頭針對這場會議繼續提問 Claude。Anthropic 也提到正在與 Gong、Attention、Granola、Fireflies.ai、Otter 等夥伴合作,讓會議逐字稿未來能直接送進團隊已經在用的工具。

⚠️ **邊界設計:預設不碰外部訪客,不留音訊**

安全與隱私機制上,Claude 加入會議時會在聊天室留下明顯通知,並以參與者身分出現,它保存的是逐字稿、摘要與畫面描述,不會保存音訊。預設情況下,如果會議邀請名單中有組織外部的人,Claude 會自動不加入;如果外部人員在會議中途加入,Claude 會自動離開,除非管理員另外開啟允許外部訪客參與的設定。在有外部訪客的會議中,Claude 會在聊天室貼出通知但不在聊天室回話,訪客的發言仍會被納入逐字稿與筆記。使用已連接工具時,Claude 會在第一次使用前徵求當事人同意,之後的使用就沿用這個授權;若是有人用語音提問,Claude 目前每次都會先確認發言者身分。管理設定上,Team 方案預設開放邀請 Claude 加入會議(管理員可關閉),Enterprise 方案則由管理員決定對組織全部或部分成員開放。文章也提到,beta 期間這項功能尚不支援零資料保留(ZDR)、HIPAA-ready 配置或客戶自管加密金鑰(CMEK)的組織。計費方面,beta 期間 Claude 的筆記、逐字稿與會議內回答在 Team、Enterprise 方案上都是免費的,除非回答動用了已連接工具,那部分才會計入方案用量;Claude 在會議中建立的文件、白板等產出,則免費使用至 2027 年 2 月 10 日。

🎯 **實務啟示**

對工程團隊來說,這個功能比較像是把「會議記錄 + 即時查資料 + 協作文件」整合進一個會議內代理人,概念上並非全新,但把授權控管(逐次確認工具使用、外部訪客自動退出)做得相對細,值得在導入前先盤點團隊會議中會不會談到敏感資訊,再決定是否開啟自動加入。

🔗 **來源**
- 標題:Introducing Claude Meetings
- 作者／機構:Anthropic
- 連結:https://claude.com/resources/articles/claude-meetings

#Anthropic #Claude #AIAgent #ClaudeMeetings #Productivity #EnterpriseAI #Collaboration #MeetingAutomation #GoogleMeet #AIAssistant
