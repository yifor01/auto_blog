---
title: People are using AI to make their smart TVs dumb again
source: TechCrunch AI
url: https://techcrunch.com/2026/10/19/people-are-using-ai-to-make-their-smart-tvs-dumb-again/
model: claude-code/sonnet
generated_at: '2026-10-19T21:49:42.233883'
score: 66
---

📌 用 Claude Code 把智慧電視變回「笨電視」

TL;DR：開發者們用 AI coding agent 遠端清掉智慧電視的廣告與追蹤功能，掀起一波「vibe coding 電視」熱潮。

一臺電視，開機第一眼看到的不是 Netflix，而是一則贊助廣告。開發者 Gathin T. 受夠了這件事，於是做了一件很多人想做卻沒做的事：直接叫 AI agent 幫他的電視動手術。

🤔 **這股風潮是怎麼開始的**

Gathin T. 在 X 上寫道：「今天下午幫我爸媽的電視做了 vibe coding！它在你進 Netflix 之前先放了一則贊助廣告。我把型號告訴 Claude Code，它在 Wi-Fi 上找到那臺電視，移除了 25 個小米套件，並寫了一個新的啟動器。」他把這個改造過程整理成一個名為 cleanyourtv 的專案放上 GitHub，承諾可以透過 Wi-Fi 清除任何 Android TV 或 Google TV 上的 bloatware，並把啟動器換成外觀類似 Apple TV 的版本。這則貼文在兩天內帶動數千人對自家電視如法炮製，涵蓋小米、TCL、Sony、Fire TV、LG，甚至投影機。

另一個類似專案 dumbtv，由開發者 Muzzammil Yasin Sabuwala 打造，在 GitHub 上自我定位是：「你的電視應該只做你付錢買的事：你的 App、你的 HDMI 輸入，僅此而已。沒有電視自己放的廣告，沒有觀看追蹤，沒有你沒要求的更新。」他表示這個專案已在 Fire TV Edition 以及 Sony、TCL、Philips、Hisense、小米、Shield 等機型上的 Android／Google TV 平臺完成端到端測試，開發過程混合使用了 Deepseek V4.1 Flash、Claude Opus 5.5 與 Claude Sonnet 5.5。他告訴 TechCrunch，自己之所以動手，是因為厭倦了廣告以及無法直接跳到想看的內容，並計畫持續維護這個 GitHub 專案，之後逐步加入對更多模型的支援。

類似案例還在持續擴散：X 用戶 Ryan Doyle 直接把自己電視的型號貼給 Claude Code，問「你能駭入這個嗎？」，agent 一步步引導他移除廣告與 bloatware、加速卡頓的使用者介面，並客製化螢幕保護程式；另一位用戶 Mihir Gupta 則表示一個下午就用 Claude Code 停用了 25 個 bloat app，把原本 192MB 的原廠啟動器換成一個 83MB 的自訂版本，還加上了輪播桌布。

💡 **為什麼這件事值得注意**

現代智慧電視普遍搭載自動內容識別（ACR）技術，透過畫面截圖、音訊片段等數位指紋技術辨識使用者正在看什麼內容。智慧電視的廣告產業正是靠出售這些觀看資料給廣告主，或用來在自家介面上投放個人化廣告而獲利。報導指出，如果這類「笨電視化」的改造普及到一般消費者，有可能衝擊這整套商業模式。值得一提的是，cleanyourtv 的設計不需要取得電視的 root 權限，也沒有讓裝置無法恢復原廠設定。

⚠️ **仍是半成品，有人把電視搞當了**

報導也提醒，這些解決方案都還在持續開發中，不同使用者正在各種電視平臺上測試並提出修正建議。有些人發現 Claude 不會回應單純的「幫我駭電視」這類指令，必須寫更複雜的 prompt 才有反應；也有人警告 AI agent 可能出錯，誤停用重要的系統套件。報導中提到，有人因此把自己的 Android TV 搞磚了，另一人則在改造 Fire TV 的過程中卡在一半動彈不得。

🎯 **實務啟示**

對工程師而言，這其實是一個有意思的案例：把電視型號丟給 agent、讓它自行在區域網路上找到裝置並動手改寫系統設定，展示了 coding agent 在「網路裝置探索 + 遠端操作」這類場景的潛力，但也暴露出讓 agent 在沒有完整回滾機制的真實硬體上操作系統套件的風險。如果不想冒硬體變磚的風險，報導也提到市面上已有現成的、非 AI 驅動的 Android 電視啟動器替代方案，例如 ATV Launcher、Projectivy Launcher 與 FLauncher，可以作為風險較低的選擇。

🔗 **來源**
- 標題：People are using AI to make their smart TVs dumb again
- 作者／機構：Sarah Perez, TechCrunch AI
- 連結：https://techcrunch.com/2026/10/19/people-are-using-ai-to-make-their-smart-tvs-dumb-again/

#VibeCoding #ClaudeCode #SmartTV #AIAgents #ConsumerTech #PrivacyTech #HackTheTV #AndroidTV #TechCulture #DIYTech
