---
title: 'Self-service data analytics in Slack: how Anthropic deploys Claude Tag for
  ad-hoc questions'
source: Claude Blog
url: https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions
model: claude-code/sonnet
generated_at: '2026-08-14T07:20:18.091573'
pinned: true
---

📌 Anthropic 如何在 Slack 打造自助式資料分析 agent

TL;DR：用治理語意層＋持續更新的 skill files，讓全公司在 Slack 問數據也有分析師水準的答案。

想像在 Slack 隨口問一句「這個指標為什麼掉了」，幾秒後得到的不只是一個數字，還附上當天發生的事故與影響範圍——這正是 Anthropic 資料團隊在 Claude Tag（公開 beta）上打造的自助分析體驗。

🤔 **從 Claude Code 到全公司都能問的 Slack agent**

Anthropic 先前的文章說明，團隊透過三項核心元件讓 Claude 以約 95% 準確度回答資料分析問題：治理過的語意層、一套編碼分析慣例的 skill files，以及用來衡量表現的評測套件。當時的重點是 Claude Code，主要服務資料科學家與資料工程師。這篇文章則說明如何把同一套基礎延伸到 Claude Tag，讓非分析師也能在 Slack 直接提問，並拿到與分析師使用同一套治理定義的答案。

🧩 **Skill files 要跟著資料模型一起更新**

Anthropic 團隊表示，最重要的架構決策是把 skill files 當成「持續發布的內容」，而非一次性交付就不再更動的文件。資料模型可能一天內變動好幾次：欄位改名、指標定義修正、表格被棄用。因為 Slack 使用者往往只拿到一兩個數字，沒有儀表板的趨勢線可以幫忙做「合理性檢查」，一旦 Claude 讀到過期的 skill file，很容易自信滿滿地給出錯誤答案卻沒人發現。為此，Claude Tag 的執行環境會掛載資料庫程式碼庫中的 `skills/` 目錄，並在每一次對話都重新讀取。

除了教 Claude「該查哪張表」的知識型 skill，團隊也額外掛載了一批分析手法／runbook 型 skill，包括：
- **預測**：何時、如何套用簡單趨勢與季節性假設，以及資料序列太短或太雜訊時該拒答。
- **世代與留存分析**：標準的世代定義、向管理層回報用的留存曲線範本，以及容易踩雷的細節（如左側截尾、倖存者偏誤）。
- **漏斗分析**：關鍵產品漏斗的標準階段定義，確保「使用者在 onboarding 哪裡流失」這類問題每次回答都一致。
- **圖表製作**：什麼問題該用什麼圖、配色慣例，以及何時該用表格而非圖表。
- **分析寫作**：如何組織一則發現（先講結論、再給數字、講機制、附但書），以及該有多少保留語氣。

團隊指出，這些慣例多數本來就存在，只是通常只存在資深分析師的腦中，寫成 skill 之後才能確保 Claude 的表現與人類分析師一致。

💡 **接上業務脈絡，而不只是資料倉儲**

即使有知識型與 runbook 型 skill，很多問題的答案根本不在資料模型裡，而是散落在 Slack 討論串、事故追蹤系統、發布紀錄裡。Anthropic 因此把 Claude Tag 接上內部知識索引，能在偵測到指標異動時，同步搜尋當下的背景事件，例如當天上午發生的付款服務事故，把答案變成「週二註冊數下滑 12%：當天上午 9 點到 11 點有一起付款服務事故，且降幅集中在受影響地區」。團隊建議，若組織已有知識圖譜、內部搜尋或整理良好的事故／變更紀錄，把 Claude Tag 接上這些來源，是僅次於接上資料倉儲本身、投資報酬率最高的一步。

⚠️ **權限設計必須刻意為之**

Claude Tag 是以服務帳號、而非提問者本人的身份查詢資料倉儲——這是正確的設計，畢竟不該讓每個 Slack 使用者都持有倉儲的直接憑證，但代價是沒有逐用戶的列層級權限：只要能標記機器人，就等於擁有這個服務帳號能讀到的所有資料。Anthropic 文中提到共有五種作法來把關這個風險，目前完整揭露的包括：把服務帳號的存取範圍限定在治理過的語意層輸出表與精選 mart，不得讀取原始事件流、staging schema 或個人沙盒，若問題超出這個邊界，agent 會直接說明無法回答，而非亂猜；以及在欄位層級分類 PII，維護含欄位血緣的資料目錄，一旦有新欄位上線，Claude 會掃描並標記疑似 PII 欄位交由人工複核。

🎯 **實務啟示**

對正在把 LLM agent 部署進 Slack 的資料團隊來說，這篇文章給出兩個可直接複用的原則：skill files 要當成活文件持續同步資料模型的變動，而不是一次性文件；權限設計要在部署前就想清楚服務帳號的存取邊界與 PII 分類機制，因為 Slack 環境沒有逐用戶權限這道防線，一旦設計錯誤會很難事後補救。

🔗 **來源**
- 標題：Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions
- 作者／機構：Clement Peng, Lily Zhao／Anthropic
- 連結：https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions

#Anthropic #ClaudeTag #DataAnalytics #Slack #LLMAgent #DataGovernance #SkillFiles #SelfServiceAnalytics #AIatWork #DataEngineering
