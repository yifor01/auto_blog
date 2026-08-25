---
title: OpenAI is building AI agents for everything. Will everyone use them?
source: TechCrunch AI
url: https://techcrunch.com/2026/08/24/openai-is-building-an-ai-agent-for-everything-will-everyone-use-them/
model: claude-code/sonnet
generated_at: '2026-08-25T06:31:54.982923'
score: 79
---

📌 OpenAI 想讓每個上班族都有 AI Agent，但採用率只有 1%

TL;DR：ChatGPT Work 想把 Codex 的能力帶給非工程師，但目前個人訂閱戶採用率不到 1%。

OpenAI 內部有 98% 員工在用 Codex，但同一款工具面向一般訂閱用戶時，採用率卻不到 1%。這個巨大落差，正是 OpenAI 力推 ChatGPT Work 想要解決的問題。

🤔 **從程式碼助手到「什麼都能做」的助手**

ChatGPT Work 於上個月推出，是 OpenAI Codex 編碼工具的改造版本，目前開放在最低階的每月 20 美元訂閱方案中使用。目標是讓會計師、投資人、醫師等「非工程師」白領工作者，也能擁有軟體工程師早已享有的 agent 體驗：不只是回答問題，而是自主完成多步驟專案。OpenAI 產品負責人 Thibault Sottiaux 表示：「ChatGPT 現在能自主完成非常複雜的整個任務，而且是以令人愉悅且安全的方式。」

負責 OpenAI 桌面應用的工程負責人 Andrew Ambrosino，為了測試產品未來型態，讓應用程式取得他的收件匣、Slack 帳號、手機、Notion、Figma 等工具的存取與控制權限。他坦言這代表模型有可能從私訊中擷取資訊、並在不知情的情況下用到不該分享的內容上，「我願意為了工作承擔這個風險，而且目前還沒發生過。」

🧩 **每個 LLM 都需要一副「挽具」**

文章解釋了讓模型變成 agent 的關鍵技術概念：每個 LLM 都需要一個「harness」（挽具）——包在模型外層的軟體，決定模型能看到什麼資訊、能使用哪些工具，以及如何呈現答案。要讓模型處理長期任務，harness 必須提供工具與使用指引。對開發者來說，一個能讓 LLM 寫程式的命令列介面（CLI）就足以改變軟體開發方式；但多數一般使用者不會用 CLI，就像 Windows 取代 DOS 的道理一樣。因此 OpenAI 想把 OpenClaw 這類原本給工程師用來驅動 LLM 的能力，做成像輸入 prompt 一樣簡單。

📊 **內部近乎全員採用，外部使用者卻寥寥無幾**

一份 OpenAI 資助的研究發現，今年 6 月時 OpenAI 內部有 98% 員工在使用 Codex，但組織訂閱戶中只有 17%、個人訂閱戶中不到 1% 的人在使用這款 agentic coding 工具。目前 ChatGPT Work 與 Codex 合計使用者約 2,000 萬人，相較之下 OpenAI 宣稱 ChatGPT 整體有超過 10 億使用者在進行日常對話式提問。

💡 **易用性與可發現性的內部拉鋸**

Ambrosino 提到公司內部對於介面設計仍有爭論：一些員工認為既然使用者可以直接對模型下指令，就不需要額外的按鈕；但他的團隊反對這種看法，理由是「現在還太早，這個階段可發現性（discoverability）很重要，等到某個時間點我們就不需要按鈕了。」他將這種設計取捨比喻為擬物化設計（skeuomorphism，例如把計算機 App 做成實體計算機的樣子）——這類設計曾幫助使用者完成轉換期的適應，而非單純的懷舊裝飾。

⚠️ **競爭與商業張力**

文章也指出，OpenAI 與其他大型模型實驗室在推進垂直領域應用時，面臨像 Harvey（法律）、Clay（銷售）這類採取「模型無關」策略的專業領域競爭者的挑戰，這些公司會依當下表現彈性選用最適合的模型。a16z 的 Christian Catalini 認為，如果實驗室無法快速取得規模化 AI 所需的關鍵互補資產，「價值就會流向別處」。此外，agent 執行長時間任務會消耗更多 token，這對 OpenAI 而言是商業上更有利可圖的使用模式。

🎯 **實務啟示**

對工程師而言，這篇報導提醒了一件事：agent 能力已經在程式碼領域被驗證，但要跨越到「messy world」的一般辦公場景，挑戰不在模型能力本身，而在 harness 設計、權限管理與使用者信任的建立。若你的團隊正在打造面向非技術使用者的 agent 產品，可發現性（明確的按鈕與引導）與漸進式授權，可能比一味追求「純自然語言」介面更重要。

🔗 **來源**
- 標題：OpenAI is building AI agents for everything. Will everyone use them?
- 作者／機構：Tim Fernholz, TechCrunch AI
- 連結：https://techcrunch.com/2026/08/24/openai-is-building-an-ai-agent-for-everything-will-everyone-use-them/

#OpenAI #ChatGPT #Codex #AIAgent #EnterpriseAI #ProductDesign #LLM #AgenticAI #Automation #WorkplaceAI
