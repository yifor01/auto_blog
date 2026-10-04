---
title: We want you to build the next Git platform on Cloudflare
source: Hacker News
url: https://blog.cloudflare.com/next-git-platform-on-cloudflare/
model: claude-code/sonnet
generated_at: '2026-10-04T20:27:53.907057'
score: 66
---

📌 Cloudflare公開徵件：誰能造出Agent時代的GitHub

TL;DR：Cloudflare開放Artifacts程式化原語，徵件打造多agent協作的下一代Git平臺，首獎2.5萬美元額度。

GitHub是為「人類寫程式碼」的世界設計的：分支、commit、issue、pull request，背後假設是一個人或一個小團隊在推進變更。但當同一個程式碼庫上同時有數百、甚至數千個agent在工作時，誰在改什麼、衝突怎麼解、怎麼審查，這套假設還成立嗎？Cloudflare的答案是：不知道，所以把問題交給社群來解。

🤔 現有Git工作流撐不住agent規模

Cloudflare在部落格裡提出一串尖銳問題：agent如何知道其他agent在做什麼？衝突的變更怎麼處理？要怎麼審查agent產出的所有程式碼？又該如何追蹤「不只改了什麼，還有為什麼這樣改」？他們認為，下一代Git平臺不會是「現有GitHub加裝agent功能」，而需要從根本重新設計repository、分支、pull request、worktree、程式碼審查與合併衝突的概念。

🧩 Artifacts提供的基礎設施

今年早些時候，Cloudflare推出了Artifacts：一個支援Git語義、可擴展到數百萬個repository的版本化檔案系統，從設計之初就是一組可程式化原語，讓開發者在其上建構自己的產品與工作流。隨著Artifacts進入公開測試，Cloudflare也補上了幾項新能力：

- **部署到Workers**：透過Workers Builds將Artifacts repository連接到Worker，推送到正式分支會自動建置部署，推送到其他分支則自動建立或更新Workers Previews，產生可分享的預覽版本。
- **從Worker管理Artifacts**：透過Artifacts binding，可以在Worker裡建立/fork repository、讀取檔案與commit、發出repository範圍的Git token。例如以下範例展示如何為新任務fork專案並讀取其AGENTS.md指示：

```js
using project = await env.ARTIFACTS.get("my-project");
const { defaultBranch } = await project.info();
const workspace = await project.fork(`task-${crypto.randomUUID()}`);
using repo = await env.ARTIFACTS.get(workspace.name);
const instructions = await repo.readFile({
  ref: defaultBranch,
  path: "AGENTS.md",
});
```

- **事件訂閱**：Artifacts會在repository建立、匯入、fork、刪除、推送、clone、fetch時發布事件，可訂閱後觸發CI、程式碼審查agent或部署流程。
- **資料主權設定**：建立namespace時可指定美國或歐盟的資料處理轄區。
- **使用量指標**：儀表板可查看每個repository的操作數、pull/push次數、錯誤率等指標。

⚠️ 這是一場尚無答案的徵件，不是現成方案

必須說清楚：這篇文章本身並未公布任何「下一代GitHub」的具體技術方案，而是Cloudflare提供底層原語（Artifacts）後，邀請開發者自行設計agent協作的工作流、審查與合併機制。官方明確表示「不是在現有GitHub上加裝agent功能」，但也沒有給出自己的答案，一切都要等社群投稿。另外，Artifacts從2026年10月15日起開始依操作量與儲存量計費，且目前僅對Workers Paid方案的客戶開放公開測試。

📊 徵件規則與獎勵

- 參賽需提交：5到10分鐘的示範影片、以寬鬆開源授權（MIT、Apache或BSD）發布的原始碼連結、執行或試用說明。
- 至少要展示多個agent同時處理變更的場景。
- 截止日期為2026年10月14日。
- 前三名團隊中各派最多兩名成員飛往舊金山參加Cloudflare Connect；第一名額外獲得2.5萬美元Cloudflare額度，並受邀參加Connect的VIP演講者晚宴。

🎯 實務啟示

如果你的團隊已經在用多agent並行開發，這是一個低成本測試「agent原生」Git工作流設計的機會：用Artifacts的fork、binding與事件訂閱機制，先把「衝突解決」「審查觸發」「上下文保存」這幾個痛點跑一輪原型，再評估是否要投稿競賽或自行落地到正式流程。

🔗 來源
- 標題：We want you to build the next Git platform on Cloudflare
- 作者／機構：geoffbp, Hacker News（原文出自Cloudflare部落格）
- 連結：https://blog.cloudflare.com/next-git-platform-on-cloudflare/

#Cloudflare #Artifacts #GitPlatform #AIAgents #DeveloperTools #CloudflareWorkers #OpenSource #AgenticCoding #VersionControl #DevEx
