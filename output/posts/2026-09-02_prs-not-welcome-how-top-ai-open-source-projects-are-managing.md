---
title: 'PRs NOT Welcome: How Top AI Open Source Projects Are Managing Thousands of
  Contributors'
source: Latent Space
url: https://www.latent.space/p/pr-not-welcome
model: claude-code/sonnet
generated_at: '2026-09-02T10:21:12.367890'
score: 90
---

📌 「PR 不歡迎」：頂尖 AI 開源專案為何集體關閉外部貢獻

TL;DR：Vercel、Astro、tldraw、Flue 改用自家 agent 處理 issue 與 PR，重新定義開源貢獻的意義。

🎣 GitHub 發明 pull request 這18年來，PR預設開放幾乎是開源世界的鐵律。但現在，包括 Flue、tldraw 在內的多個頂尖 AI-native 開源專案，正在做一件反直覺的事：直接拒絕外部PR。

🤔 為何要把大門關上

原因之一，是這些PR有不少其實是AI產生的。與其花時間審查品質參差的外部AI生成程式碼，維護者發現讓自己的 agent 來寫、來管理PR，反而更有效率也更值得信任。

🧩 「軟體工廠」：一組 agent 分工處理issue

Vercel 近期發布〈Building a software factory for AI SDK〉一文，描述旗下開源專案 AI SDK（每週超過2000萬次 npm 下載）如何部署 agent 群，奪回issue與PR積壓的控制權——到六月底時，AI SDK已累積「超過1,000個未解決issue，將近800個PR」。

Vercel的系統中，不同agent各司其職：有負責重現bug的agent、有負責套用修復的agent，還有負責審查修復結果的agent。整套架構包含一個UI、一個web app、底層API、執行空間與sandbox，並與GitHub同步觸發後續動作。

工程師 Lars Grammel 在 YouTube 影片中解釋，Vercel會信任自己的agent配置多過社群成員送出的agent產物：「如果我們有一個非常特定的agent，搭配我們最佳化過的特定prompt——而且從歷史紀錄看，它在修復某類bug上一直很成功——我們就會對這個agent配置產生信任。」他也建議其他開源專案「值得考慮建立自己的agent與流程，而不是預設信任社群」，因為這樣能大幅縮短審查時間。

📊 四週見效：25-35%的PR由工廠產生

導入這套軟體工廠僅四週後，Vercel表示這套系統「已經負責產出25%至35%已合併的PR，並解決了70%至80%的issue」。

擁有6.2萬顆GitHub星星的 Astro 框架也採用了同樣的「software factory」概念。創辦人 Fred Schott 告訴 Latent Space：「過去五年，issue湧入的速度一直快過我們能處理的速度。」如今讓agent負責triage、重現問題、並在維護者親自查看前先讓回報者驗證agent提出的修復方案，情況「在過去六個月徹底翻轉」。他說：「我在超過十年的開源經驗裡從沒見過這種事——現在issue不再是一堆越滾越大的積壓，而是每週都能被優先處理完的清單。」

這套自動化triage系統，也直接催生了Schott打造的全新agent框架 Flue。Flue採取更激進的做法：所有外部PR都會被自動關閉，並轉換成issue或discussion——bug回報變成issue，功能請求變成discussion。Flue的貢獻者指南寫道，這是為了防止「隨手一丟的AI垃圾PR」（drive-by AI slop PR），「如果你送出PR，別介意，我們會把它改寫成issue或discussion幫你呈現，再從那裡想辦法讓你參與進來」。Flue會結合團隊自身經驗與「目前可取得的最先進（SOTA）LLM」來判斷優先處理順序，決定之後才會派agent進行研究、設計、實作與初步審查。

同樣採取自動關閉外部PR政策的，還有擁有5萬顆星星的繪圖工具 tldraw。創辦人 Steve Ruiz 一月宣布此政策，五個月後重申，稱這是「因應程式撰寫方式改變（更多討論、更多agent）、公開貢獻的社會慣例變化，以及程式碼安全格局變化」所做的決定。HashiCorp共同創辦人、Ghostty作者、現為Superlogical共同創辦人的 Mitchell Hashimoto 講得更直接：「未來大型開源專案會完全關閉貢獻管道。」Ruiz回應：「如果issue描述得夠清楚，程式碼可以由agent寫出來，那讓人送PR這件事本身就越來越沒道理。」

💡 貢獻的意義正在轉移

傳統開源裡，PR審查不只是把關程式碼，也是維護者觀察、培養未來接班人的方式。如果連程式碼審查與實作都交給agent，社群成員還能怎麼參與？Schott坦承這是風險：「這仍然留下一個破洞——如果專案範圍一直被收窄，某天你我都去度假了怎麼辦？這並不能解決所有問題。」不過Flue與tldraw都不接受PR、卻接受issue與discussion的做法，或許指出一條路：透過更多對話，社群成員彼此認識、建立信任，這既是向同儕學習的方式，也可能是證明自己有資格成為維護者的途徑。至於程式碼，正如Ruiz所說：「更好的做法是把社群貢獻限縮在真正重要的地方：回報問題、討論、觀點與關心。」

🎯 實務啟示

如果你維護開源專案，與其被動等待外部PR品質參差不齊，不如評估自建專屬agent流程處理triage與修復——這不代表要完全拒人於外，而是把人力資源留給真正需要判斷與信任的環節：討論優先順序、審核方向、培養社群關係。

🔗 來源
- 標題：PRs NOT Welcome: How Top AI Open Source Projects Are Managing Thousands of Contributors
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/pr-not-welcome

#OpenSource #AIAgents #SoftwareEngineering #DeveloperTools #Vercel #Astro #tldraw #GitHub #AgentOrchestration #CodeReview
