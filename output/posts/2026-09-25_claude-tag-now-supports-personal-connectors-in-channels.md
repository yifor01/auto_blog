---
title: Claude Tag now supports personal connectors in channels
source: Claude Blog
url: https://claude.com/blog/claude-tag-now-supports-personal-connectors-in-channels
model: claude-code/sonnet
generated_at: '2026-09-25T20:39:03.147935'
pinned: true
---

📌 【Anthropic 官方發布】Claude Tag 加入個人連接器，頻道權限終於能「跟人走」

TL;DR：Claude Tag 現在能在 Slack 頻道裡呼叫你個人綁定的連接器，權限跟著人、不跟著頻道。

在 Slack 頻道裡拉 Claude 進來幫忙，過去有個尷尬的限制：Claude 只能用管理員裝在該頻道上的連接器（connector）。這代表多數組織會刻意把頻道的連接器清單縮到最短，因為誰都不想讓整個頻道共用某個人的日曆或帳戶存取權。Anthropic 這次的更新，正是要解決「權限該跟著頻道走，還是跟著人走」這個根本問題。

🤔 **問題：頻道級連接器，權限沒辦法細到個人**

Claude Tag（beta）讓 Claude 以團隊成員身分進駐 Slack 頻道，與人協作。但在此之前，Claude 在頻道裡能碰到的工具，僅限於管理員預先設定給整個頻道的連接器。如果你想請 Claude 幫你對照自己 Google Drive 裡的文件、或查詢只屬於你的 CRM 待辦帳戶，頻道層級的權限模型完全無法支援，因為那些資料本來就不該讓頻道裡每個人都看得到。

🧩 **做法：個人連接器加入頻道，只有你能觸發**

現在，Claude 可以在頻道中的請求裡使用「你自己」連接到 Claude 帳戶的個人連接器，例如你的日曆、你的 Drive、CRM 裡指派給你的帳戶，或是你的 staging 部署環境。這些連接器只有你本人能觸發，其他頻道成員無法借用。

輸出的呈現方式也由你決定：可以選擇「逐則審核」，每次 Claude 要貼出結果前先讓你確認；也可以開啟自動模式，讓 Claude 直接貼文，除非它判斷內容含有敏感資訊才會轉為需要你審核。Enterprise 方案的管理員則可以進一步要求所有人都必須經過審核流程。

官方舉的例子是 Priya 在 #checkout-migration 頻道（該頻道已連接 GitHub）裡問 Claude：「幫我核對 Google Drive 裡『Checkout migration, Q3』這份文件，跟目前已上線的內容比對，還有哪些沒做完？」Claude 透過頻道的 GitHub 連接器讀取已合併的 pull request，再透過 Priya 個人的 Google Drive 連接器讀取只有她能打開的文件，最後把落差整理出來。因為這份文件內容不算敏感，Priya 用自動模式讓 Claude 先自行篩選再貼出；換成她想先過目的文件，則可以切換成審核模式。

每一次 Claude 透過個人連接器執行的動作，都會記錄在該工具自己的操作紀錄裡，掛在你自己的帳戶下，就跟你在私訊裡使用連接器一樣；頻道本身的既有工作仍掛在頻道的服務帳戶下，不會混淆。連接器隨時可以由你自行解除連結。

⚠️ **限制：個人連接器不能無人值守**

這個功能有一個明確的邊界：排程任務，或任何 Claude 自行主動觸發的行動，一律只能使用管理員裝在頻道上的共用連接器，個人連接器不會在無人監督的情境下自動執行。因此像 #on-call 這類需要 Claude 在下班時間自主做 CI 巡檢與初步處置的頻道，仍然要靠管理員設定好共用的 runbook、監控工具與部署紀錄連接器。

反過來，完全只靠個人連接器運作的頻道，適合的是需要密切監督的協作場景，例如共同起草 RFP 回覆時，需要拉取只有部分人能看到的報價等敏感資料來源。值得留意的是，不論資料來源是誰的連接器，只要 Claude 貼進頻道，內容就對頻道所有成員可見。

管理員這邊也多了幾種治理選項：可以用共用的 agent 身分提供一組工具、要求頻道成員一律只能用各自的個人連接器以延續既有的角色權限模型（RBAC），或是逐一決定每個工具的存取方式。

🎯 **實務啟示**

對於管理 Slack 工作流程的工程團隊來說，這個更新讓「頻道機器人」與「個人助理」兩種使用情境不必再互相妥協：需要無人值守自動化的頻道（如 on-call）繼續靠共用連接器；需要拉取個人敏感資料的臨時查詢，則交給個人連接器處理，且全程留有審核與紀錄機制。這功能目前在 Team 方案上線，Enterprise 方案將陸續跟進，不需要額外安裝，Claude 會在第一次用到某個連接器時主動詢問授權。

🔗 **來源**
- 標題：Claude Tag now supports personal connectors in channels
- 作者／機構：Anthropic
- 連結：https://claude.com/blog/claude-tag-now-supports-personal-connectors-in-channels

#Anthropic #ClaudeAI #ClaudeTag #Slack #EnterpriseAI #AIAgents #Connectors #ProductivityTools #AIGovernance #WorkplaceAutomation
