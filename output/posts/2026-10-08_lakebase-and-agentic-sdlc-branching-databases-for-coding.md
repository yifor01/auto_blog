---
title: 'Lakebase and Agentic SDLC: Branching Databases for Coding Agents'
source: Databricks
url: https://www.databricks.com/blog/lakebase-and-agentic-sdlc-branching-databases-coding-agents
model: claude-code/sonnet
generated_at: '2026-10-08T22:23:41.002790'
score: 92
---

📌 Lakebase資料庫分支:讓每個Coding Agent都有專屬資料庫

TL;DR:Databricks Lakebase用copy-on-write技術讓資料庫像Git一樣可以秒級分支，解決多個coding agent並行開發時的資料庫衝突問題。

當你同時開好幾個coding agent處理不同任務時，程式碼可以用Git worktree各自隔離，但資料庫呢？多數團隊仍共用一個開發或staging資料庫，這正是Databricks這篇文章點出的被忽視的痛點。

🤔 **共用資料庫，agent們互相踩到對方**

文章指出，隨著coding agent承擔越來越多開發工作，開發者傾向同時平行執行多個agent。每個agent都需要讀取資料庫schema、套用變更、填入測試資料、執行測試。在傳統共用環境下，agent之間會在schema變更上互相衝突、干擾彼此，或是退而求其次使用無法反映真實情況的mock資料。agent移動速度快、又平行運作，風險因此被放大：可能讓production資料暴露，或處理到敏感資訊。

🧩 **像Git branch一樣分支整個資料庫**

Lakebase Postgres架構的解法是資料庫分支（database branching）。就像Git讓你分支程式碼，Lakebase讓你在一秒內分支整個資料庫，且不受資料庫大小影響。它採用copy-on-write，分支會共享parent branch的資料，只有在資料產生分歧時才會額外消耗儲存空間；閒置的分支還能scale-to-zero，不佔用運算資源。

實際做法是搭配Git worktree：每個agent在自己的worktree目錄下工作，透過repository的post-checkout hook，自動為每個新worktree建立對應的資料庫分支。Agent的行為可以透過AGENTS.md或CLAUDE.md這類repository指令檔案來引導，例如完成開發後自動開PR。一旦PR建立，對應的worktree與資料庫分支就可以一起退役。

💡 **分支不會合併回去，schema變更要靠migration工具**

文章特別強調一個與Git不同之處：Lakebase分支不會合併回main branch。因為parent和child可能各自獨立變化，要協調兩邊的資料很快會變得不切實際。取而代之的作法是把schema變更寫進程式碼中，隨應用程式邏輯一起管理，再透過Drizzle、Flyway、Liquibase或Alembic等migration工具，將變更promote到parent branch（範例repository中使用的是Drizzle）。

在CI流程中，每個PR會從production分支出一個暫時的Lakebase分支，作為該PR的資料庫環境，自動測試與preview應用程式都可以對著這個分支跑。因為分支源自production，schema migration也能在真正推上production前先在這裡驗證過。PR合併後，程式碼與migration被promote，暫時分支就被刪除。

除了開發流程，文章也提到分支可以用在debug（從production某個時間點分支出來重現bug）與migration安全驗證（先在分支上套用migration並測試，驗證無誤後才promote到production）等場景，但這兩者並未在範例repository中實作。

⚠️ **目前以單一workspace示範，企業場景通常更複雜**

文章提到常見的作法是每個環境（dev、staging、prod）各用一個Databricks workspace，主要是出於安全與合規考量；分支來源通常也是「已填入測試資料的seeded資料庫」而非直接用production，以避免暴露PII。文章為求簡化採用單一workspace示範，但強調核心概念同樣適用於多workspace設定。

🎯 **實務啟示**

如果你的團隊正在用coding agent並行開發，資料庫隔離和程式碼隔離（Git worktree）同樣重要。「每個agent一個分支、每個PR一個分支、production驗證用隔離分支」這三個模式，構成了一個可以直接套用的Lakebase開發迴圈，值得在導入多agent開發流程時一併考慮資料庫層的隔離策略。

🔗 **來源**
- 標題：Lakebase and Agentic SDLC: Branching Databases for Coding Agents
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/lakebase-and-agentic-sdlc-branching-databases-coding-agents

#Databricks #Lakebase #Postgres #CodingAgents #DatabaseBranching #DevOps #AgenticSDLC #CICD #GitWorktree #SchemaManagement
