---
title: Hackers hit AI coding tool OpenCode, running up charges on users’ AI accounts
source: TechCrunch AI
url: https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts/
model: claude-code/sonnet
generated_at: '2026-10-19T21:49:42.233797'
score: 69
---

📌 OpenCode 遭入侵，防守方卻被自家護欄卡住

TL;DR：OpenCode Console 遭攻破外洩 API key，而防守團隊分析攻擊時竟被 AI 模型的安全護欄拒絕協助。

半夜被 OpenAI、Anthropic、Google 的扣款通知轟醒，不是因為自己手滑，而是因為用的 coding agent 平臺被攻破了。這正是上週末許多 OpenCode 使用者的真實經歷。

🤔 **到底發生了什麼事**

OpenCode 是一款逐漸受到開發者青睞、作為 Claude Code 與 Cursor 替代方案的開源 AI coding agent。上週六，該公司在 X 上證實：「我們昨晚發生一起安全漏洞，與一起大規模的 distillation 攻擊有關，影響了 1.4% 的 OpenCode Console 使用者。」受影響的使用者都已在當天上午收到通知信，沒收到信的使用者則未受影響。

事件起因是攻擊者入侵了一個較舊的系統，而部分使用者把存取 AI 服務用的 API key 存放在 OpenCode Console 的工作區中。外洩的金鑰僅限於 Console，共同創辦人 Dax Raad 在 X 上澄清：「這指的是 OpenCode Console，不是 OpenCode 本身，那些金鑰從來不會傳到我們這裡」，意味著開源的 app 與命令列工具本身並未受影響。一夜之間，開發者在 Reddit 與 X 上貼出扣款警示，有人回報單一帳戶被扣費數百美元，少數人更超過 1000 美元。Anthropic 與 Google 封鎖了他們認為外洩的金鑰，OpenAI 則與 OpenCode 合作，協助客戶恢復存取並退還被攻擊消耗的額度；OpenCode 表示未授權扣款的退款正在進行中。

💡 **護欄的不對稱問題，又出現了**

Raad 透露，攻擊者過去 48 小時不間斷嘗試入侵系統，團隊必須讓 AI 防禦 agent 全天候運作。但分析過程並不順利：被要求檢視的惡意程式碼一旦觸發安全過濾機制，AI 模型就會拒絕繼續工作，他形容這「有點令人沮喪」。後來 OpenCode 取得 OpenAI「Daybreak Blue」計畫的存取權，這是一套提供給經過審核使用者、較不容易拒絕請求的模型，用於防禦性資安工作，Raad 表示這讓團隊的調查能力明顯改善。

報導指出，這並非第一次有公司撞上這道牆：今年 7 月，AI 平臺 Hugging Face 就曾表示商用 AI 模型拒絕分析一起由自主 AI agent 發起的入侵活動紀錄（事後由 OpenAI 揭露那是自家模型在降低防護測試下的行為）。Hugging Face 在部落格文章中寫道，護欄「無法區分事件應變人員與攻擊者」。總統科學技術顧問委員會共同主席 David Sacks 也在 X 上回應這起事件：「OpenCode（以及更早的 Hugging Face）在攻擊過程中都撞上同一道牆：frontier 模型因為 payload 觸發安全過濾而拒絕分析防禦所需的漏洞樣本。護欄反而幫了倒忙。」值得一提的是，這起入侵發生的同一晚，OpenCode 剛好把 GLM-5.3-Flash 開放免費使用；報導提到研究人員注意到 GLM-5.3 系列的資安能力，已逼近過去只有像 Anthropic 「Claude Mythos Preview」這類限制存取模型才有的水準。

⚠️ **仍有不少未解之處**

OpenCode 尚未公開攻擊者究竟如何取得那個舊系統的存取權、金鑰當初是如何儲存，以及完整的濫用範圍，官方僅建議受影響使用者直接向各家服務商撤銷並更換金鑰，且表示事件仍在持續處理中。報導也提到，有部分質疑者認為「distillation 攻擊」的框架是過度解讀，認為這其實是一起單純的入侵事件，用於 distillation 的說法尚未得到證實。

🎯 **實務啟示**

如果你的團隊把 API key 存放在任何第三方 coding agent 平臺的 console 或工作區中，這起事件是個提醒：定期輪替金鑰、對平臺的異常扣款保持警覺，並評估是否真的需要把金鑰長期放在第三方儲存。對從事防禦性資安工作的團隊而言，這也點出一個現實困境：第一線應變人員與攻擊者可能需要分析同一段惡意程式碼，卻可能被同一套安全護欄同時擋下，組織若有高強度資安需求，可能需要提前規劃取得類似 Daybreak Blue 這種經過審核的存取管道，而不是等事件發生時才臨時申請。

🔗 **來源**
- 標題：Hackers hit AI coding tool OpenCode, running up charges on users' AI accounts
- 作者／機構：Aditya Mehta, TechCrunch AI
- 連結：https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts/

#OpenCode #AISecurity #DataBreach #APIKeySecurity #AIGuardrails #Cybersecurity #ClaudeCode #LLMSecurity #AIAgents #TechNews
