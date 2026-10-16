---
title: How an Anthropic Japan BDR runs his day with a fleet of Claude agents
source: Claude Blog
url: https://claude.com/resources/articles/how-an-anthropic-japan-business-development-representative-runs-his-day
model: claude-code/sonnet
generated_at: '2026-10-16T20:07:37.122933'
pinned: true
---

📌 【Anthropic 實戰案例】業務員怎麼靠 6 隻 Agent 跑完一整天

TL;DR：Anthropic 日本業務用 Claude Managed Agents 組了一支代號「Nakama」的 agent 機隊，包辦分案、回信與 CRM 更新。

每天早上花兩小時分派名單、再寫一輪中英文郵件，剩下時間拿來補 CRM，而且常常慢了一天以上——這是 Anthropic 日本團隊一位 business development representative（BDR）過去的日常。現在，這些事在他開始上班前就已經處理好大半，他只需要審核。

🤔 **手動流程的真實痛點**

這篇文章作者的工作是向日本企業展示 Claude 如何簡化工作流程，諷刺的是，他自己的工作大多還是手動進行：早上篩選與分派 leads、用日文或英文寫信，剩餘時間追更 Salesforce 紀錄，進度經常落後。他先用 Claude 一次處理一項工作、修正錯誤、保存修正結果，久而久之累積成一組 agent，同事得知後也想要他的 prompt 和 skills，但他只能給一個 zip 檔，對方還得自己上傳、回答一輪設定問題才能動起來。

🧩 **一支日文命名的 agent 機隊**

作者把工作流程拆成多個 agent，每個只負責一件事，方便追蹤出錯點，並統一取名為「Nakama」（夥伴）：

- **Furiwake**（分揀）：讀取每日 inbound 名單，依負責業務的名額與該名單的優先度分案，確保每個 lead 在大家開工前都有主人，並在 Slack 頻道貼出報告。
- **Sabaki**（處理）：篩選分派給作者本人的 lead，依預設條件分類、採取對應的下一步（引導自助或客製首封信），更新 Salesforce 紀錄，並草擬第一封信，內容來自 Nakama 共用的知識庫。
- **Henji**（回覆）：每小時掃描信箱，為需要回覆的客戶郵件草擬日文或英文回信，同樣取材自共用知識庫,供作者審閱、修改、寄出。
- **Shoudan**（商機）：讀取近期客戶互動，把更新寫回 Salesforce，讓商機紀錄不需要手動輸入。
- **Nokori**（剩餘事項）：在每天結束時掃描行事曆、讀取會議逐字稿，摘要會議內容並草擬後續追蹤信。
- **協調者（coordinator）**：機隊的「營運經理」，在各次執行之間更新所有 agent 的指令與共用知識庫；作者只要在 Slack 頻道用白話文寫下想要的改動，協調者每 15 分鐘左右檢查一次並套用更新。

每個 agent 都依排程自動執行。

💡 **從 Claude 原型到 Managed Agents**

作者先在 Claude 裡用三個元件原型化整支機隊：每個 agent 一個 skill（工作指令）、一個排程任務、以及一個筆電上的共用資料夾作為知識庫，記錄草稿與實際寄出內容的差異，以及過程中挖到的新資訊。遷到 Claude Managed Agents（beta）後，skill 變成 agent 的 system prompt，排程任務變成部署上的 schedule，共用資料夾變成 memory store。

轉移後最關鍵的三個改變：agent 可以在背景執行，不受筆電開關機影響，排程寫在部署設定裡，不需要自己維護 cron job；所有 agent 共用同一個 memory store，彼此能從作者的修改中學習，一處改好 Henji 的措辭，Sabaki 和 Nokori 就不會再犯同樣的錯；登入信箱與 Salesforce 的憑證則集中存放在具權限範圍的 managed vault 裡，各 agent 只拿得到自己工作所需的憑證，且作者可以一鍵撤銷存取權。

🎯 **給想自建 agent 的業務人員**

作者建議先在 Claude 裡用 skill＋排程任務原型化，等 agent 數量多到難以追蹤時，再搬到 Managed Agents 集中管理版本與權限，這樣不需要具備開發者背景也能維運一支自動化機隊。

🔗 **來源**
- 標題：How an Anthropic Japan BDR runs his day with a fleet of Claude agents
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/how-an-anthropic-japan-business-development-representative-runs-his-day

#Anthropic #ClaudeAI #AIAgents #Automation #SalesTech #ManagedAgents #WorkflowAutomation #LLM #ProductivityTools #Agentic
