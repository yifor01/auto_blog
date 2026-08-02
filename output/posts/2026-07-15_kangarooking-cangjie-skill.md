---
title: kangarooking/cangjie-skill
source: GitHub Trending
url: https://github.com/kangarooking/cangjie-skill
score: 91
model: tencent/hy3:free
generated_at: '2026-07-15T08:19:53.067768'
---

📌 書與影片蒸餾成可呼叫 AI Skills

TL;DR：cangjie-skill 把長內容方法論轉為可呼叫 AI 技能，解決知識無法複用痛點。

🎣 開場鉤子：
你可能收藏了幾十支實用長影片、買了好多書，但那些方法論始終停留在「稍後觀看」清單裡被遺忘。現在有一個開源專案嘗試把它們變成 AI agent 能直接呼叫的工具包。

🤔 知識消費的斷層：看過卻用不上
README 指出，現代人面臨幾個痛點：看了很多書、影片、播客但運用不起來，知識停留在「看過／聽過／收藏過」層面，無法在真實決策中被呼叫；摘要、筆記、字幕整理只是壓縮，不是結構化複用，讀完仍不知道「什麼時候該用什麼」；高價值內容裡真正值得變成工具的只有一小部分，需要嚴格篩選；現有閱讀／觀看方法論都是給人看的，不是給 agent 用的。

🧩 RIA-TV++ 七階段流水線（摘要說明前五）
cangjie-skill 的核心設計是使用 RIA-TV++ 流水線，把書籍、影片轉寫、播客文字稿等原始文本變成一組結構化 skill。作者宣稱整個過程分七個階段，並在片段中說明了其中五個關鍵步驟：

1. 整體內容理解（Adler 分析）：借鑑 Mortimer Adler 的分析閱讀法，對整份內容做結構、解釋、批判、應用四步拆解，產出 BOOK_OVERVIEW.md。
2. 並行提取：同時派 5 個專項提取器（框架、原則、案例、反例、術語），從原文提取候選方法論單元。
3. 三重驗證篩選：每個候選必須通過三項檢驗，原內容至少 2 處獨立佐證（跨域）、能回答未明說的新問題（預測力）、不是常識（獨特性）。README 指出通過率通常只有 25-50%。
4. RIA++ 構造：將驗證通過內容按 R（原文引用）／ I（重寫）／ A1（書中案例）／ A2（未來觸發場景）／ E（可執行步驟）／ B（邊界與盲點）六維度結構化。
5. Zettelkasten 連結：找出 skill 之間依賴、對比、組合關係，生成 INDEX。

💡 與蒸餾「人」的 skill 互補，需搭配影片下載工具
專案定位上，作者提到 nuwa-skill 是創造「人類 skill」（如馬斯克 skill），而 cangjie-skill 是蒸餾人「系統性表達過的內容」，屬於另一維度補充。適用物件包含書、有字幕／轉寫文本的影片、播客、訪談、演講、課程、長文和資料集，只要內容存在可抽取、可驗證、可遷移的方法論即可。

若要蒸餾影片，README 建議搭配 video-downloader skill：先下載影片、提取字幕／音訊轉寫和關鍵素材，再把文本交給 cangjie-skill 做方法論抽取、skill 化和壓力測試。

🎯 把收藏清單交給 agent 執行
對工程師而言，與其讓筆記淪為墳場，不如挑選幾份真正高價值的長內容，用 cangjie-skill 產出可組合使用的技能包，讓 AI agent 在真實場景中主動呼叫這些知識。挑選時需注意內容必須包含明確方法論，否則嚴苛的三重驗證會過濾掉大部分素材。

🔗 來源
- 標題：kangarooking/cangjie-skill
- 作者／機構：kangarooking
- 連結：https://github.com/kangarooking/cangjie-skill

#AI #Skill #KnowledgeDistillation #Agent #OpenSource #Methodology #LLM #Productivity #Zettelkasten #GitHub
