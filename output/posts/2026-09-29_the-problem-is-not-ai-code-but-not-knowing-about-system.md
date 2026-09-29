---
title: The problem is not AI code, but not knowing about system architecture or intent
source: Hacker News
url: https://www.ssp.sh/brain/the-problem-is-not-the-ai-code-but-nobody-knows-anything-anymore/
model: claude-code/sonnet
generated_at: '2026-09-29T21:47:59.880194'
score: 80
---

📌 沒人不會用 Claude，但也沒人懂系統架構了

TL;DR：一篇 HN 熱議文章指出，AI 編碼真正的風險是團隊集體喪失對架構與意圖的理解。

「規格、程式碼、測試、PRD、ticket、報告，全部都是 Claude Code 做的。沒有人在讀任何東西。」一位在大公司待了半個月的工程師這樣描述現況。這篇引發 379 點讚、238 則留言的討論，指出的不是 AI 寫的程式碼品質問題，而是更深一層的：當每個人都只會問 Claude，整個團隊還剩下什麼計畫可言？

🤔 問題不是程式碼平庸，而是無人知曉

文章引用一則觀察：AI 寫出的程式碼水準大概是「平均」，如果原本的程式碼庫低於平均，AI 確實能把它拉到平均。但作者認為真正的問題不在這裡，而在於「沒有人知道任何事，大家都只是去問 Claude」，結果變成完全沒有計畫的開發狀態。

🧩 一個令人熟悉的工作現場

文中引述一則匿名貼文，描述在一間快速推動 AI 的大公司裡的日常：從 L1 到 L7 的工程師做的都是同一件事——跟 Claude 對話；沒有人在解 bug，沒有人在思考；管理層認為「寫程式碼不是瓶頸」，於是要求大家一天工作 12 到 13 小時只為了按下 Enter；沒有人有機會真正檢視程式碼跑到哪裡去了，唯一的目標就是「出貨」。另一位引用者 Matthew Mullins 則將此類比為 COBOL 工程師逐漸退場的問題，認為 agent coding 會把同樣的處境帶到每一種開發語言。

💡 產品經理可以憑空造出產品，但架構感仍是稀缺能力

文章也提出另一面：一個不會寫程式、但懂得管理團隊做出想要軟體的產品經理，其實一直都存在其價值——知道自己要什麼，向來是最困難的部分。但作者也提醒，若完全不懂架構與程式基礎，即使 AI 能協助迭代，一開始選錯語言或錯誤的心智模型，產品從起點就會有難以維護的地基。文中也引用另一種說法：資料工程師這個族群向來被迫從第一天就要懂完整的產品與業務脈絡，AI 只是替他們移除了摩擦；但對於今天才入行、直接靠提示詞工作的新人來說，這份原本必須具備的知識可能就此缺席。

⚠️ 最終大魔王仍是維護

作者的結論是：親手寫程式碼或許已經式微，但思考系統、架構、意圖與設計的能力，仍然是讓工程師變得更好的關鍵。產生一支 pipeline、一個 app 或一個 BI 儀表板越容易，日後需要維護的東西就越多；如果沒有人懂系統在做什麼，維護會變得非常困難。文章引用 Harry Dry 的說法：好點子從來不是靠創意，而是靠 conviction（信念），而「沒有任何 AI 提示詞可以生成 conviction」。

🎯 實務啟示

對工程團隊來說，這篇文章是一個提醒：把 AI 當成加速器沒有問題，但如果團隊因此停止閱讀規格、停止追問「為什麼這樣設計」，架構知識就會在無人察覺的情況下流失。具體可行的作法，是把「解釋這段程式碼為何這樣設計」納入 code review 或 onboarding 流程，用 AI 幫助建立理解，而不是讓它取代理解本身。

🔗 來源
- 標題：The problem is not AI code, but not knowing about system architecture or intent
- 作者／機構：zazuke（Hacker News）
- 連結：https://www.ssp.sh/brain/the-problem-is-not-the-ai-code-but-nobody-knows-anything-anymore/

#AICoding #SoftwareArchitecture #EngineeringCulture #ClaudeCode #TechDebt #DeveloperProductivity #VibeCoding #SoftwareMaintenance #AIAgents #HackerNews
