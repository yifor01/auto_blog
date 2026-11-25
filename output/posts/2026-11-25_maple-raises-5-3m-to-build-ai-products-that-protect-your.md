---
title: Maple raises $5.3M to build AI products that protect your data, even from itself
source: TechCrunch AI
url: https://techcrunch.com/2026/11/24/maple-raises-5-3m-to-build-ai-products-that-protect-your-data-even-from-itself/
model: claude-code/sonnet
generated_at: '2026-11-25T01:52:58.175308'
score: 65
---

📌 Maple 募得 530 萬美元：連公司自己都看不到你的資料

TL;DR：Maple 用 TEE 架構讓 AI agent 存取你的資料時，連公司自己都技術上碰不到。

你的 AI 助理能讀信件、瀏覽器、日曆,甚至操控整臺電腦——但如果連開發這套助理的公司自己都"技術上"拿不到你的資料,會不會比較安心?這正是 Maple 想賣的信任感。

🤔 為什麼要把自己擋在資料外面

Maple 的共同創辦人暨 CEO Mark Suman 曾在 Apple 待過六年,做 AI 與機器學習,聚焦 computer vision,當時面對的課題就是如何在 Apple 重視隱私的前提下仍能做出有用的 AI 產品。共同創辦人暨 CTO Anthony Ronning 的背景則是國防科技、資安與網路,2023 年先成立了一家主打隱私的金融科技公司,直到 2024 年 8 月兩人合作,才誕生了 Maple AI,2025 年 1 月正式以手機 App 形式公開。Maple 的主張很直接：不是要使用者"相信"公司不會濫用資料,而是直接讓公司在架構上拿不到資料。做法是開源程式碼,搭配可驗證的 Trusted Execution Environment（TEE）,使用者可以自己稽核伺服器上實際跑的程式碼,不需要單方面接受公司的保證。

🧩 資料全程加密,只在 TEE 裡短暫解密

技術流程是：資料先在裝置端用只有使用者自己知道的密碼加密,傳進跑在美國資料中心的 TEE（一臺有硬體加密的伺服器）之後才解密,歐洲用戶則透過合作夥伴架在歐洲的伺服器處理;AI 處理完畢後,資料會重新用使用者的密碼加密再送回。Suman 強調公司"不管資料在傳輸中還是靜態儲存時都拿不到原始內容"。這個設計的好處是,即便系統遭入侵或政府拿傳票來要資料,公司能交出的也只有加密檔案——Suman 的說法是"這就不是我們的 business model,也不該是我們的 threat model"。底層跑的是多種開源模型,包括 DeepSeek、Kimi、GLM、Thinking Machines 的 Inkling、Google 的 Gemma,以及 OpenAI 的 GPT OSS,使用者可以自行挑選,或在「快速模型」與「強力模型」之間簡單切換。

🧩 桌面版 Maple Work：讓 agent 操作電腦,但只給它任務需要的資料

新推出的桌面應用 Maple Work 提供更 agentic 的體驗：AI 可以控制電腦、處理檔案與應用程式、操作瀏覽器完成線上任務。App 內建整合商店,可連接 Gmail、日曆等服務;它還能啟動一個 subagent,寄生在電腦上其他支援 Agent Client Protocol（ACP）的 AI 應用裡工作,例如 Claude、Codex,讓使用者可以用自己偏好的 AI 工具處理特定任務,卻不必把所有資料都交給它,只傳遞任務真正需要的那一部分。

📊 募資與成長數字

Maple 剛完成一輪超額認購的 530 萬美元種子輪,由 EPIC Ventures 領投,Draper Associates、Planetary VC、Epoch VC 跟投,此前還有一輪不到百萬美元的天使輪。這筆資金將投入下一個產品——一個雲端 agent,即使使用者的電腦沒開著也能持續工作,直接對位 Meta 的 Muse、Instinct 等聊天式 AI agent。公司計畫 2027 上半年進行 A 輪募資。Maple 並未透露註冊用戶數,但表示過去三個月成長了 60 倍;目前收費採訂閱制,Pro 方案每月 20 美元,Max 與 Max Plus 方案分別每月 100 美元與 200 美元。明年 Maple 計畫進軍企業市場做試點,推出自家版本的 zero data retention（多數情況下不保留用戶資料,少數必須保留時也採加密）,目前正在進行 SOC 2 合規與資安稽核。公司總部設於 Austin 與 San Francisco,團隊目前僅四人,仍在招募中。

⚠️ TEE 隱私保護的概念本身並非 Maple 原創,報導中也沒有提供第三方對其 TEE 或加密實作的獨立稽核結果,目前的成長與信任主張主要來自公司自述。

🎯 給工程師的實務啟示

如果團隊正在評估要不要讓 agentic AI 助理接上機敏資料（信箱、日曆、瀏覽器）,TEE 加上用戶端加密是值得研究的架構方向,重點在於是否真正開源、能否讓第三方驗證伺服器上實際執行的程式碼,而不只是行銷用語。Maple 讓 subagent 透過 ACP 寄生在其他 AI 應用裡、只傳遞任務所需資料的設計,也提供了一種"最小權限"思路,值得在自家 multi-agent 系統裡參考。

🔗 來源
- 標題：Maple raises $5.3M to build AI products that protect your data, even from itself
- 作者／機構：Sarah Perez, TechCrunch
- 連結：https://techcrunch.com/2026/11/24/maple-raises-5-3m-to-build-ai-products-that-protect-your-data-even-from-itself/

#AIPrivacy #Maple #TEE #DataPrivacy #AIAgents #Startup #Encryption #Funding #PrivacyTech #SeedRound
