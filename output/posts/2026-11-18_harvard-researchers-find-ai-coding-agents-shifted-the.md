---
title: Harvard researchers find AI coding agents shifted the bottleneck to code review
source: Hacker News
url: https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/
model: claude-code/sonnet
generated_at: '2026-11-18T23:42:37.690373'
score: 96
---

📌 哈佛研究：AI 寫更多程式碼，審查時間卻暴增 49%

TL;DR：718 家企業的實證顯示，AI coding agent 讓程式碼量增加三成，但完工量沒動，瓶頸全部轉移到 code review。

工程團隊導入 AI coding agent 後，產出的程式碼變多了，這聽起來像是生產力的勝利。但哈佛大學兩位博士候選人 Fiona Chen 與 James Stratton 的最新工作論文（job-market paper）給出了一個反直覺的結論：多寫的程式碼，幾乎完全被卡在了審查階段，最終交付的工作量並沒有增加。

🤔 一份橫跨 718 家公司、72.5 萬名工程師的資料

這份研究的資料來自工程分析平臺 Jellyfish，並與 Revelio Labs 收集的 LinkedIn 就業紀錄進行比對，涵蓋 2021 年 1 月到 2026 年 3 月、725,938 名工作者、718 家公司。資料規模相當可觀：6,830 萬筆 Jira issue、2.009 億筆 commit、4,910 萬筆 pull request，以及 2,130 萬筆行事曆事件（僅 213 家公司提供行事曆資料）。研究方法採用 staggered difference-in-differences，按月比較已導入 AI 工具的公司與尚未導入的公司之間的變化。

作者指出，各公司導入時間點的差異主要來自資訊取得的時機與採購流程（大型公司採購可能僅需一天，也可能長達六到十二個月），他們認為這與公司成長速度無關，因此支持用這種方式做比較。研究也承認大公司普遍較早導入，並以公司規模做了控制；作者認為若仍存在未控制的差異，反而會讓 AI 的效果被高估，而非低估。

📊 多寫 30% 程式碼，完工量卻統計上無法區分於零

每位工作者每月新增程式碼行數上升 1,494 行，基準值為 5,017 行，約增加 30%；commit 數成長 20%，pull request 數成長 23%。然而論文以「Jira issue 被標記完成並部署到正式環境」來定義完工量，這項指標每位工作者每月僅增加 0.12 件，基準值為 3.67 件，標準誤高達 0.17——在統計上與零無法區分，95% 信賴區間甚至排除了超過基準值 12% 的成長可能，遠低於程式碼量 30% 的成長幅度。

研究團隊也檢驗了「工程師改做更大任務，導致 issue 數量雖平但單位工作量其實變大」這個可能的解釋：他們用 GPT-4o 標記 0.5% 的 issue 樣本大小，再用 text-embedding 模型推展到全部 issue，結果發現平均 issue 規模與 pull request 大小都沒有明顯變化，排除了這個解釋。

瓶頸落在哪裡？PR 從送出到合併的時間從基準值 7.03 天延長到增加 3.45 天，暴增 49%；收到正式變更請求（change request）的 PR 比例從基準值 13% 大幅上升約 12 個百分點，幾乎翻倍；每份 PR 的審查留言數增加 35%；參與 code review 的工作者比例從約 29% 上升 14%，而寫程式碼的工作者比例則沒有明顯變化。即便到 2026 年 3 月，近 80% 的公司已使用 AI 審查工具，AI 產生的審查留言卻只佔 23.3%，僅 10.8% 的 PR 曾獲得至少一則 AI 留言——AI 審查工具並未解除這個瓶頸。

💡 兩個管道：審查量暴增，與程式碼品質可能下降

論文訪談中，一名初階工程師描述了團隊實況：專案中只有一位資深工程師能核准變更，而他每週只能審查一次自己的程式碼；在幾次由 AI 生成的 commit 造成當機事件後，團隊新增了規定，AI 生成的程式碼必須經資深工程師核准，這進一步加劇了審查壅塞。作者將觀察到的現象歸納為兩個管道：一是更快的草稿產出把更多程式碼塞進固定規模的審查人力，這部分可以靠重新分配人力緩解；二是變更請求與留言數的上升幅度無法單靠數量解釋，暗示草稿品質本身可能下降，這個問題則需要更好的技術才能解決。

⚠️ 研究限制

這份論文目前版本為 2026 年 8 月 4 日（最初版本為 1 月 7 日），作為 job-market paper，沒有證據顯示已完成同儕審查或獲期刊接受。研究對象是軟體工程，而非法律或其他知識工作；文中提及的 Harvey 動議駁回工作流與 Cooley 與 Google Cloud 合作開發中的法律文件遮蔽（redaction）代理人，雖然同樣在流程中保留人工審查這一關卡，但兩者的官方發布都未公開審查階段的具體數據，無法直接比對。

🎯 實務啟示

對導入 AI coding agent 的團隊而言，單看「程式碼產出量」或「commit 數」是不夠的指標。更值得追蹤的是完工量、PR 核准前的修訂次數，以及審查者實際耗費的時間；若審查人力沒有同步擴充或重新分配,更快的草稿只會把壓力轉移、累積在審查隊伍裡，而不是真正縮短交付週期。

🔗 來源
- 標題：Harvard researchers find AI coding agents shifted the bottleneck to code review
- 作者／機構：ComplexDiscovery OÜ Staff（報導哈佛大學 Fiona Chen、James Stratton 之研究）
- 連結：https://complexdiscovery.com/harvard-researchers-find-ai-coding-agents-shifted-the-bottleneck-to-code-review/

#AICoding #CodeReview #SoftwareEngineering #DeveloperProductivity #AIAgents #Harvard #EngineeringMetrics #PullRequest #AIAdoption #TechResearch
