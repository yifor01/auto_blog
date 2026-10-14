---
title: Preparing for the 2026 US midterms
source: Anthropic News
url: https://www.anthropic.com/news/2026-us-midterms
model: claude-code/sonnet
generated_at: '2026-10-14T20:50:10.157644'
pinned: true
---

📌 【Anthropic】期中選舉前,Claude 怎麼防止被濫用

TL;DR：政治對話僅佔 Claude 對話 5.75%,要求投票建議的請求僅 0.01%。

🎣 外界常擔心 AI 聊天機器人會被用來左右選舉,但 Anthropic 公布的實際使用數據卻呈現另一個畫面：大多數人不是來問「該投誰」,而是想弄懂新聞、研究政策與候選人立場。

🤔 人們真正怎麼用 Claude 談政治

Anthropic 透過內部分析工具 Anthropic Insights,以隱私保護的方式分析了 2026 年 9 月 21 日至 27 日間約 25 萬則美國 Claude.ai 對話。結果顯示,廣義觸及政治、公共政策或社會議題的對話約佔全部對話的 5.75%；明確與選舉或投票相關的對話約佔 0.51%；而直接要求 Claude 推薦該投誰或投什麼的請求,僅佔約 0.01%。違反選舉誠信政策的請求更少,僅約 0.002%。多數請求屬於資訊性質,例如整理候選人在特定議題上的立場,幫助使用者自行形成判斷。

🧩 把官方投票資訊直接接進對話

為了在選舉日前提供更可靠的資訊,Anthropic 新增了兩項功能。當使用者在 Claude.ai 詢問選民登記、投票地點或選舉日期時,系統會持續顯示連結至 Democracy Works 旗下非黨派資源 TurboVote 的橫幅。本月稍後,Claude 將進一步從 Democracy Works 直接擷取官方投票資訊整合進回覆內容,讓美國使用者詢問投票地點或應攜帶的證件時,能得到針對其所在州的具體答案。選舉夜及後續幾天,Claude 回覆開票相關問題時也會顯示最新官方計票結果。

📊 模型的政治中立性評測

在每次模型發布前,Anthropic 都會大規模測試模型的政治偏見。最新的 Claude Opus 5.5、Sonnet 5.5 與 Haiku 5.5,在 Anthropic 的政治中立性評估中拿下 99% 的分數,是目前最均衡的版本,同時也更願意參與政治討論、拒答比例更低。

除了內部評測,Anthropic 也邀請三個獨立機構以不同方法審視 Claude 處理言論自由的表現：範德堡大學（Vanderbilt University）智庫 Future of Free Speech 針對數百個具爭議性的請求進行測試；Foundation for American Innovation 以左右立場對應的提示詞進行比較；Collective Intelligence Project 則在美、英、印三國調查超過 2,000 人,透過三階段流程讓參與者提出處理敏感議題的原則,再據此設計評測標準。

💡 評測也揪出了不均衡之處

Future of Free Speech 與 Collective Intelligence Project 都發現,Claude 很少直接拒答,但有時會在回答中加入未被要求的但書或反方論點,例如在替使用者撰寫倡議信件時,擅自插入對立觀點。Foundation for American Innovation 則發現,Claude Sonnet 4.5 在加註但書時並非左右對稱,更常為偏右立場的論述加上緩和語氣。Anthropic 表示已針對直接的是非題與要求簡短回答的情境改善答案的均衡性,也在調整何時、如何加入但書或反方論點,讓模型對不同政治立場的請求回應更一致。

⚠️ 濫用防範與政策界線

Anthropic 的使用政策禁止利用 Claude 欺騙選民或干擾選舉,包括散布候選人或投票方式的假資訊、冒充選務人員、企圖壓低投票率等。今年的政策更新進一步釐清選舉規則的適用範圍,並新增範例協助使用者判斷界線,同時發布指南協助政治競選團隊理解哪些用途合法（如撰寫新聞稿、募款信、辯論準備、投票率數據分析、選民外展素材),哪些被禁止（如製作冒充真人的假社群帳號、灌水留言、假冒獨立媒體撰寫內容)。Anthropic 也部署了專門訓練用來偵測選舉相關濫用行為的自動化分類器。

🎯 實務啟示

對開發政治、新聞或公民科技相關應用的工程師而言,這份報告提供了一個可參考的基準：政治類查詢的真實佔比遠低於輿論想像,但一旦涉及「投票建議」這類高風險場景,仍需要額外的防護層與第三方事實來源（如本文中的 Democracy Works）來降低誤導風險。

🔗 來源
- 標題：Preparing for the 2026 US midterms
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/news/2026-us-midterms

#Anthropic #Claude #AIPolicy #ElectionIntegrity #AISafety #PoliticalBias #ResponsibleAI #Midterms2026 #TrustAndSafety #LLM
