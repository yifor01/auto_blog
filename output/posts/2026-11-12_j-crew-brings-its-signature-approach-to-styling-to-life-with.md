---
title: J. Crew brings its signature approach to styling to life with Claude
source: Claude Blog
url: https://claude.com/resources/articles/j-crew-style-advisor-with-claude
model: claude-code/sonnet
generated_at: '2026-11-12T22:51:34.510715'
pinned: true
---

📌 J.Crew 用 Claude 把「單品搜尋」變成「整套穿搭對話」

TL;DR：J.Crew 用 Claude Fable、Opus、Sonnet、Haiku 分工打造 Style Advisor，讓線上購物從找單品變成討論整套穿搭。

線上購物有個長期沒被解決的小麻煩：找到一件喜歡的毛衣後，還得重新搜尋一次搭配的褲子和鞋子。J.Crew 今天推出的 Style Advisor，就是衝著這個痛點而來。

🤔 **四十年造型經驗，怎麼變成一個能對話的工具**

J.Crew 的團隊用 Claude Code 搭配多個 Claude 模型打造出 Style Advisor，目前已上線 JCrew.com，供美國市場的女裝與男裝使用。超過 40 年來，J.Crew 自家造型師靠著比例、色彩與層次搭配，以及出乎意料的單品組合，打造出完整的穿搭look。Style Advisor 的目標，就是把這套專業搬到線上：顧客描述需求，例如「海灘婚禮該穿什麼」或「第一次求職面試該穿什麼」，系統會給出取自 J.Crew 自家拍攝的完整穿搭，顧客還能持續調整，讓購物變成一場視覺化的對話。

🧩 **一套任務，四個模型各做各的強項**

J.Crew 產品團隊的建置流程分成幾個階段：先用 Claude Fable 5.1（Anthropic 用於複雜、開放式工作的模型）規劃 Style Advisor 該如何像一位造型師一樣推理；接著用 Claude Opus 5.5 在 Claude Code 中打造出可運作的原型；J.Crew 的工程師再把這個原型推進到生產環境。在正式上線的對話流程裡，Claude Sonnet 5.5 扮演造型師的角色，決定每一步的回應方式，而 Claude Haiku 5.5 負責處理快速、範疇明確的小任務，讓 Style Advisor 能快速回答。由於每一套推薦都來自 J.Crew 自家造型師所構思的穿搭，系統給出的建議能維持與 J.Crew 一貫的風格觀點一致。

📊 **顧客實際能怎麼用**

- 整套購物：每個推薦都源自 J.Crew 造型師為品牌型錄拍攝所設計的穿搭，Style Advisor 會以照片呈現完整的look。
- 從單品延伸：顧客可以從一件單品開始，取得能完成整套穿搭的其他建議。
- 依場合穿搭：顧客說出目的地或場合，例如度假、節日派對或婚禮，就能取得對應的推薦。
- 延續 J.Crew 的風格觀點：Style Advisor 套用的是 J.Crew 門市造型師會使用的同一套搭配原則。

💡 **接下來的規劃**

J.Crew 表示目前階段 Style Advisor 主要幫助顧客找到新的穿搭靈感，並更有信心地購物；未來計畫根據每位顧客的偏好與過往購買紀錄做得更個人化，並擴展到更多市場與產品線。J.Crew Group 執行長 Libby Wadle 表示，公司希望藉此跳脫傳統「單品搜尋」的線上購物模式，走向更連結、更具啟發性的體驗；Anthropic 商務長 Paul Smith 則提到，J.Crew 用前沿模型來打造體驗，再用更快、更有效率的模型來實際運行，讓顧客能快速得到符合品牌風格的答案。

🎯 **實務啟示**

這個案例示範了一種常見但值得留意的多模型架構分工模式：用最強的推理模型做「規劃與原型」，用中階模型處理「正式對話中的核心判斷」，再用輕量模型處理「高頻率、低複雜度」的子任務。對於想把 AI 功能真正推上生產環境、同時控制延遲與成本的團隊，這種依任務特性分配模型的做法值得參考。

🔗 **來源**
- 標題：J. Crew brings its signature approach to styling to life with Claude
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/j-crew-style-advisor-with-claude

#Anthropic #ClaudeAI #ClaudeCode #Retail #AIStylist #Ecommerce #ClaudeFable #ClaudeOpus #ClaudeSonnet #ClaudeHaiku
