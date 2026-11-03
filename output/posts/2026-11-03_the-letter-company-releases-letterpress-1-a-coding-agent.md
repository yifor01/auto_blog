---
title: 'The Letter Company Releases Letterpress-1: A Coding Agent Built for Growth
  Engineering'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/02/letter-letterpress-1-growth-engineering-coding-agent/
model: claude-code/sonnet
generated_at: '2026-11-03T22:45:31.622425'
score: 76
---

📌 成長工程專用 Coding Agent:Letterpress-1 讀網站下 PR

TL;DR:The Letter Company 推出會自己讀網站與市場訊號、直接開 PR 的 coding agent,定位是「成長工程」而非一般程式碼擴充。

一般的 coding agent 幫你擴充程式庫,但誰來盯著你的行銷網站對 Google 排名、競爭對手動作和真人訪客的反應?The Letter Company 的答案是做一個只為這件事存在的 agent。

🤔 網站跟 App 不一樣,它會被外部力量推著走

Letter 團隊的論點是,網站不同於一般應用程式,會持續受到外部力量影響,包括 agent 行為、Google 排名、真人訪客與競爭對手動作。一般的 coding agent 是為了擴充程式庫而設計,並不會主動對這些訊號做出反應。Letterpress-1 因此被定位成一個主動的成長工程 agent:它讀取網站與市場訊號,自己判斷「下一步該做什麼」,並建議具體的改動,例如去匿名化(de-anonymization)、新的 landing page、暖身信(warmed emails)、部落格自動化與 agent 遙測。

🧩 同一套迴圈:讀取、規劃、建置、審查、開 PR

Letterpress-1 的目標使用者是把行銷網站放在 git 上管理的團隊。每一次改動都走同一套流程:agent 讀取網站現況,在沙箱(sandbox)中規劃並建置變更,自我審查這個改動,再開出一個 pull request,附上即時預覽連結。報導強調,沒有任何東西會自動上線,使用者必須主動選擇預覽、PR,或是等檢查通過後再合併,才會真正生效。產品依報導分成 3 種模式運作。

Letter 團隊列出 6 個操作介面:web 平臺、一個 Slack app、letterpress CLI、網站入口(portal)、一個獨立 app,以及開放給使用者自己的 agent 呼叫。其中內嵌於網站的 IDE 可直接在線上頁面編輯:按下 ⌘L,在畫面上看到文字的地方直接修改,系統就會開出對應的 PR,showcase 範例也展示了用這種直接編輯方式做 A/B 測試。對開發者而言,agents.md 文件描述了一個位於 app.letterstory.com/api/mcp、支援 OAuth 的 MCP 伺服器,其 MCP manifest、OpenAPI 規格與 API 參考文件合計構成一個包含 760 個工具的註冊表,讓 Claude Code、Codex 或其他支援 MCP 的 agent 可以呼叫跟網站應用本身一樣的功能。發布文宣稱有 4 個「原語(primitives)」是特別針對吸引 AI agent 作為購買方而設計,網站上還列出了 Kernels、Letterbases、Visitors、Mailers 等功能,並會監看競爭對手的 sitemap 以偵測新頁面上線。Letter 團隊把這些功能定位為 G2、Semrush、Profound、RB2B、Instantly 等工具的替代方案。

📊 計價:共用 token 池,一個 PR 落在 1.5 到 9 美元

Letter 採用單一共用 token 池計價,1 個 token 等於牌價 1 美分。方案分為 Basic(100 美元、10,000 tokens)、Starter(500 美元、50,000 tokens)、Growth(1,000 美元、130,000 tokens)與 Scale(2,500 美元、400,000 tokens),Enterprise 方案則從每月 200 萬 tokens 起算,費率為牌價的一半。執行一次 agent 任務的成本是模型花費加 20%,報導指出典型落在每個 PR 150 到 900 tokens 之間,換算約 1.5 到 9 美元;發布一篇文章則需要 1,030 tokens。Basic 與 Starter 方案超量使用的費率是每 1,000 tokens 收 50 美元,是牌價的 5 倍,且未用完的 tokens 不會結轉到下個月。

⚠️ 資訊有限,技術細節仍待觀察

目前公開的資料偏向產品介紹與計價說明,對於 agent 內部如何判斷「該做什麼改動」、審查機制的具體邏輯等核心技術細節,報導著墨不多,工程師若要評估是否導入,應以官方文件與實際試用結果為準。

🎯 實務啟示

對於把行銷網站放在 git 管理、且需要頻繁迭代 landing page、SEO 與內容的團隊,Letterpress-1 的「讀訊號→沙箱建置→自我審查→開 PR→人工決定是否合併」流程提供了一個把成長實驗流程化、agent 化的參考模式;其開放 MCP 工具註冊表的做法,也讓既有的 Claude Code、Codex 等 agent 工具鏈可以直接接上,值得關注其實際落地效果與定價是否符合團隊用量。

🔗 來源
- 標題:The Letter Company Releases Letterpress-1: A Coding Agent Built for Growth Engineering
- 作者／機構:Michal Sutter
- 連結:https://www.marktechpost.com/2026/11/02/letter-letterpress-1-growth-engineering-coding-agent/

#GrowthEngineering #CodingAgent #MCP #AIAgent #PullRequest #MarketingAutomation #DeveloperTools #AgenticAI #SEO #Startup
