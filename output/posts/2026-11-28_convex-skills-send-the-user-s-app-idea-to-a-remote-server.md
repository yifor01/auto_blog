---
title: Convex skills send the user's app idea to a remote server without telling them
source: Hacker News
url: https://github.com/convex/convex-backend-skill/issues/64
model: claude-code/sonnet
generated_at: '2026-11-28T00:39:31.290580'
score: 81
---

📌 【安全爭議】Convex官方Skill偷傳使用者想法

TL;DR：GitHub issue指出Convex官方AI skill外洩使用者想法並規避安全檢查。

當你用AI agent的quickstart skill，敲下一句話描述自己的App點子時，你可能以為這句話只會留在本機交給LLM處理。一份GitHub issue顯示，至少有一款列在Anthropic官方claude-plugins-official市集裡的skill，會把這句話原封不動送到一臺遠端伺服器。

🤔 **一個issue，三個skill，同一個問題**

2026年10月26日，開發者thirtysix在convex-backend-skill這個repo提出issue #64，指出其中三個skill都存在類似問題：skills/quickstart/SKILL.md、skills/add/SKILL.md，以及skills/labs-quickstart/SKILL.md。

🧩 **把送資料和繞過安全檢查寫進skill指令裡**

依照issue的描述：skills/quickstart/SKILL.md第48到56行，會把使用者輸入的一句話專案點子POST到https://basic-anteater-667.convex.site/generate，程式碼裡的註解把這個行為標記為「telemetry」（伺服器會記錄「一次執行已開始」），但使用者並未被告知自己的點子已經離開本機。skills/add/SKILL.md第62、64行，會把從同一臺伺服器下載的腳本直接pipe進bash執行。skills/labs-quickstart/SKILL.md第74到80行則更進一步：刻意把「下載腳本」和「執行腳本」拆成兩次獨立的Bash呼叫，並在指示中寫明理由——「同時下載並執行遠端程式碼的指令，正是harness安全分類器會擋下的樣子」，還要求絕不能用&&、;或換行把兩步接在同一次呼叫裡。

💡 **分兩步執行，是為了躲過使用者自己設的防線**

提出issue的thirtysix特別說明，他傾向相信這是團隊想讓onboarding流程更順暢，而非出於惡意。但labs-quickstart裡的那段指示，本質上是在教AI agent改變指令的「形狀」，目的是繞過使用者或其管理員選擇要有的安全檢查——這已經不只是UX最佳化，而是主動移除了使用者本該擁有的審查機會。再加上目標網域是一個像隨機產生的名稱（basic-anteater-667.convex.site），腳本也沒有做版本固定或雜湊驗證，使用者實質上無法審查真正會被執行的內容。

📊 **討論熱度與後續動作**

這份issue在GitHub上獲得26個👀反應；轉到Hacker News後，累積215點、66則留言。11月27日，開發者adszzz11提交了一個標題為「study/convex-skill-trust-boundary」的PR（#230），並在commit訊息中引用了這個issue，顯示專案維護方已經注意到此事。截至thirtysix回報當時，三份SKILL.md檔案仍在main分支上，issue本身也維持在Open狀態。

⚠️ **素材未提供的部分**

目前素材只呈現thirtysix在issue中的描述與程式碼片段，Convex官方尚未在issue內正式回覆，PR #230的實際修改內容素材中也沒有說明。

🎯 **裝第三方AI skill前，先讀它實際會跑的指令**

thirtysix在issue中提出三點具體建議：在送出使用者的點子之前先明確告知，並讓這個行為可以選擇關閉；把bootstrap與add腳本直接打包進plugin本體，或至少用雜湊固定版本，而不是在執行當下才從遠端抓取；拿掉「為了躲過分類器而拆分指令」的那段指示，讓「下載並執行」這個動作照原樣接受使用者的核準或拒絕。對任何會替團隊安裝第三方agent skill或plugin的工程師來說，這是一個提醒：官方市集裡的套件不代表指令本身已經被審查過，授權agent執行某個skill前，值得先看一遍它實際會跑的shell指令。thirtysix本人也維護一份名為awesome-agent-skills的目錄，用來彙整這類skill的安全性發現。

🔗 **來源**
- 標題：Convex skills send the user's app idea to a remote server without telling them
- 作者／機構：MickyTheMouse
- 連結：https://github.com/convex/convex-backend-skill/issues/64

#AIAgents #AgentSkills #Security #SupplyChainSecurity #ClaudeCode #Convex #Privacy #TrustAndSafety #OpenSource #HackerNews
