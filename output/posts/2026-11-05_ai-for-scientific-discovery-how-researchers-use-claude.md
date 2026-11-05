---
title: 'AI for scientific discovery: How researchers use Claude'
source: Anthropic Research
url: https://www.anthropic.com/research/how-researchers-use-claude
model: claude-code/sonnet
generated_at: '2026-11-05T22:47:08.415108'
pinned: true
---

📌 【Anthropic 研究】20 萬筆對話顯示科學家這樣用 Claude

TL;DR：分析 20.7 萬筆 Claude 對話發現，科學家最常用 AI 做資料分析，而非發想點子。

科學家自己說「發想假說」最重要，但實際上，他們打開 Claude 時做的事，卻幾乎都不是這件事。Anthropic 這份研究想搞清楚的，正是這個落差從何而來，以及它對未來研究速度意味著什麼。

🤔 **AI 能加速科學發現嗎？關鍵在「怎麼用」**

Anthropic 指出，AI 能否加速科學發現，不只取決於 AI 的能力上限，還取決於科學家實際如何把這些能力套用到研究中各種細碎又彼此關聯的任務上。為了回答這個問題，研究團隊分析了 207,000 筆 Claude、Claude Code 與 Claude Science 的科學研究對話。

🧩 **方法：用隱私保護的分類器標記任務，而非讀對話內容**

研究團隊採用隱私保護（privacy-preserving）的方式進行分析：先用一個分類器判斷對話是否涉及科學研究，再用第二個分類器依照「SciNet taxonomy」（由 Alamos 與 Althoff 於 2026 年提出的分類體系）把每筆對話標記到特定領域、子領域與任務。SciNet 總共涵蓋 34 個領域、318 個子領域、7,262 項任務。研究團隊強調，分類器不會提取或保存對話中的研究資料集、假設、實驗方法或未發表論文等具體內容，所有結果只以符合最低帳戶數門檻的彙總形式呈現。

📊 **科學家最常用 Claude 做什麼：資料分析與寫作，不是發想點子**

分析結果顯示，以研究人員數量為基準，Claude 在計算機科學、數學、統計等形式科學（formal sciences）領域的使用率較高，在健康醫學與需要實驗室操作的物理科學領域則使用率較低。從任務類型來看，資料分析約佔 Claude 使用場景的三分之一，在 Claude Code 上更接近一半；相對地，發想點子、提出假說與資料蒐集的使用量偏低，儘管在同步進行的研究者調查中，這兩項任務被評為對科學發現「最重要」的工作。報告也提到一個例外：在專為科學工作設計的 Claude Science 上，發想點子的使用佔比大約是一般 Claude 的兩倍，顯示專用工具有機會縮小「最常用」與「最重要」之間的落差。

💡 **用量跟著 AI 能力走：AI 擅長的任務，用量是預期的 2 到 4 倍**

研究團隊另外建構了一套指標，衡量 AI 理論上能把每項研究任務做到多好。結果顯示，AI 最擅長的前 20% 任務，其 Claude 使用量是依研究人員投入時間推估的 2 到 4 倍；而 AI 最不擅長的後 20% 任務（多為需要實體操作的工作）則幾乎沒有被使用。這個模式在不同領域間一致：計算機科學、統計等 AI 表現較好的領域，Claude 使用率也較高。報告的結論很直接：科學家傾向在 AI 做得好的地方用 AI。

📊 **加速科學的情境推估：部分領域產出可翻倍，甚至衝上 15 倍**

基於一個簡化模型，報告推估：若現有 AI 能力被廣泛採用，部分領域的研究產出有可能翻倍，主要來自任務層級的增強效果。若進一步假設 AI 能完全自動化所有非實體性的研究工作，計算機科學、統計等高度認知性領域的產出最多可提升到 15 倍，而受限於實體瓶頸的化學、生物等實驗科學領域，產出則可能提升 3 到 4 倍。在針對積極使用 AI 的研究者所做的調查中，約 40% 的受訪者預期 AI 模型會在 2030 年前能夠獨立執行完整的研究專案。

⚠️ **加速的另一面：監督變少、研究動機被改變**

報告也提出警示：人類監督的減少，可能讓危險或不符倫理的研究方向更容易被追求；同時 AI 深度參與研究，也可能重塑研究者的職業生涯，改變研究工作本身的成就感與人類追求知識的意義。報告特別點出一個回饋循環：由於加速潛力最大的領域中就包含 AI 研究本身（如計算機科學），更快的 AI 研究可能催生更強的 AI，進而進一步加速研究，形成自我強化的循環。

🎯 **實務啟示**

對 AI/ML 工程師而言，這份報告等於是一張「AI 在科學研究中的實際落點地圖」：資料分析與寫作是目前最成熟的應用，而發想假說與資料蒐集仍是明顯的能力缺口，這也是打造專用科學研究工具（如 Claude Science）時最值得投入的方向。

🔗 **來源**
- 標題：AI for scientific discovery: How researchers use Claude
- 作者／機構：Johannes Hermle, Ben Jones, Lukas Althoff 等（Anthropic）
- 連結：https://www.anthropic.com/research/how-researchers-use-claude

#Anthropic #Claude #AIforScience #ScientificDiscovery #ClaudeCode #ResearchAutomation #LLM #AIResearch #DataAnalysis #FutureOfResearch
