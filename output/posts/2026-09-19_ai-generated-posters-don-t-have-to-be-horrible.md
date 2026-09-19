---
title: AI-generated posters don’t have to be horrible
source: Hacker News
url: https://john.hartnup.uk/2026/06/07/ai-event-posters.html
model: claude-code/sonnet
generated_at: '2026-09-19T19:31:47.653174'
score: 63
---

📌 千篇一律的AI海報，其實是輸給了提示詞的懶惰

TL;DR：同一個社區活動海報，只要換一種風格提示詞，ChatGPT就能跳出「AI感」樣板。

社群媒體上流傳一張拼貼圖，收集了一堆風格幾乎一模一樣的 AI 生成活動海報：粉彩色調、手繪風花朵、彩帶邊框。問題不在於這些海報難看，而在於同一種風格看了二十次之後，開始讓人厭煩。部落格作者 john.hartnup.uk 決定證明，這個問題其實出在提示詞，而不是模型本身。

🤔 **「請畫一張春季園遊會海報」得到的，還是那套老樣板**

作者先給了 ChatGPT 一份虛構的活動細節（日期、地點、攤位內容），並特別要求「乾淨俐落、避免粉彩水彩風格、避免出現人物」。結果第一次產出的海報，依然帶著那種熟悉的、想要避開的「工藝園遊會」既視感。

🧩 **要求一個完全不同的設計美學，答案立刻不一樣**

作者接著要求 ChatGPT「用完全不同的設計美學重做一張，把前一張當作『不要這樣做』的參考」，這次得到的是 Bauhaus／幾何現代主義風格：粗體無襯線字體、對稱佈局、高對比配色。作者追問這是什麼風格，ChatGPT 給出了具體的名稱與特徵說明（Bauhaus、Swiss Style、Geometric Minimalism 等），並反問是否要推得更極端，例如 brutalist、riso 印刷、90 年代 rave 傳單、日式極簡等。

作者接著請 ChatGPT 直接列出一份風格選單，涵蓋從「乾淨但有個性」（Bauhaus、Swiss Style、雜誌編輯風）、「圖像化但不甜膩」（Risograph、Matisse 剪紙拼貼、現代化植物科學繪圖），到「大膽另類」（Brutalist、90 年代 Rave 螢光、Memphis 後現代主義）等多個方向，並附上針對這次園遊會需求的推薦清單。此後作者依序生成了 Stamp／Letterpress 風格、日式極簡風格、Memphis 風格，甚至致敬知名唱片封面設計工作室 Designers Republic 的版本，以及「專業排版師幫小孩水彩畫加字」和「80 年代龐克地下刊物影印風」等實驗性風格。

💡 **對話上下文會悄悄「污染」後續生成結果**

作者觀察到一個值得留意的細節：在生成 Designers Republic 風格版本時，ChatGPT 自行加上了一行文案「A day of music making and family fun」。因為這段文字已經留在對話上下文中，後續生成的海報也跟著沿用了這句話。作者提醒，如果從頭就明確指定想要的風格，就能避免這種「一路累積不必要元素」的狀況。

⚠️ **仍然帶著一點AI味，但至少不再千篇一律**

作者坦言，這些海報依然帶著「AI 感」，但這本來就不是他的目標。重點不是隱藏 AI 的使用痕跡，而是避開那種讓所有人看膩的單一樣板長相。

🎯 **實務啟示：把設計語彙當成提示詞的一部分**

這篇實驗對工程師的啟發是，圖像生成模型的「風格詞彙量」遠比多數人日常使用的範圍更廣。與其接受模型的預設輸出，不如像作者一樣，主動要求模型列出具體的設計流派名稱（Bauhaus、Swiss Style、Risograph 等），再針對名稱疊代生成。同時要留意多輪對話中不小心「沾染」到上下文的內容，必要時開新對話重新指定風格，避免非預期元素累積。

🔗 **來源**
- 標題：AI-generated posters don't have to be horrible
- 作者／機構：john.hartnup.uk（ereiamjh）
- 連結：https://john.hartnup.uk/2026/06/07/ai-event-posters.html

#AIArt #PromptEngineering #GenerativeAI #ChatGPT #GraphicDesign #ImageGeneration #DesignSystems #CreativeAI #PosterDesign #AIWorkflow
