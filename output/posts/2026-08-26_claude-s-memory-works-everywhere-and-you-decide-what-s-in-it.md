---
title: Claude's memory works everywhere, and you decide what's in it
source: Claude Blog
url: https://claude.com/blog/claudes-memory-works-everywhere-and-you-decide-whats-in-it
model: claude-code/sonnet
generated_at: '2026-08-26T06:19:26.749363'
pinned: true
---

📌 Claude 記憶不再分app：一份記憶，聊天與 Cowork 通用

TL;DR：Claude 的記憶從即日起在 chat 與 Claude Cowork 間共用，且使用者能逐條檢視、編輯、刪除記憶內容。

每次切換到新工具就要重講一次背景，是多數人用 AI 助理的日常痛點。Anthropic 這次的更新，直接把「記憶」這件事從單一介面的功能，升級成跨產品的共用基礎設施。

🤔 **問題：換個工具，AI 就失憶**

過去在 chat 裡建立起的脈絡——例如你 Q3 的優先事項、專案進度——換到 Cowork 執行任務時往往要重新交代一次。這種重複說明的摩擦，是這次更新想解決的核心問題。

🧩 **一份記憶，兩個入口互通**

Cowork 現在使用與 chat 相同的記憶庫。Cowork 在雲端執行任務時，能讀到你在 chat 中累積的脈絡，反之在 Cowork 中產生的資訊也會回饋到 chat。文章舉例：請 Cowork 幫忙寫一封給主管的進度更新信，它已經知道主管是誰、偏好怎樣的寫法；在 chat 中討論會議籌備細節後，Cowork 建立預算與後勤文件時就知道人數、地點與講者；在 chat 說明團隊如何定義指標一次，之後 Cowork 產出的每份季度報告都會沿用，不必重複交代。

另一項變化是記憶的更新方式：Claude 現在會在對話進行中即時把重點加入記憶，而不是等對話結束才做摘要。例如你提到專案截止日改到九月，下一次對話就已經知道，不需要特別說「記住這個」。記憶也可以隨時暫停或重置。

**記憶內容你能全部看到、逐條修改**：Memory 設定裡的 Topics 清單，會把 Claude 記得的內容整理成一則則檔案，可以閱讀、編輯或刪除。文章特別提到一個實務效益：只要在一個檔案裡修正公司舊名稱，之後所有對話都會用對的名稱。

⚠️ **敏感主題預設不記，可自行開啟**

Claude 預設不會把健康狀況、種族、宗教信仰、政治立場、性別認同等被視為敏感的主題存入記憶。若使用者主動在設定中開啟「include sensitive topics in memory」，Claude 才會記住例如「對麩質過敏」這類資訊，並在每次存入敏感主題時跳出提示；開啟前的舊對話內容不會被回溯收錄。即使開啟此設定，社會安全碼、政府證件號碼、犯罪紀錄、移民身分，以及任何違反 Anthropic 使用政策（AUP）的內容，Claude 仍不會存入記憶，並會告知使用者無法更新。

**適用範圍**：記憶功能在 Free、Pro、Max 方案的網頁版、桌面版與行動版預設開啟，敏感主題記憶預設關閉；Team 與 Enterprise 方案則由管理員控管，個別使用者的記憶功能預設為關閉狀態，需自行開啟。

🎯 **給工程師的實務啟示**

如果你的團隊同時用 Claude.ai 對話發想、又用 Claude Cowork 執行實際任務，這次更新等於省去一大段「context 搬運」的手動工作。值得注意的設計取捨是：記憶以主題檔案（topic files）呈現而非黑盒摘要，使用者可逐條稽核與修正，這種透明化的記憶管理方式，對於需要向使用者交代「AI 到底記住了什麼」的產品設計，是值得參考的模式。

🔗 **來源**
- 標題：Claude's memory works everywhere, and you decide what's in it
- 作者／機構：Anthropic
- 連結：https://claude.com/blog/claudes-memory-works-everywhere-and-you-decide-whats-in-it

#Claude #Anthropic #ClaudeCowork #AIMemory #ProductivityAI #EnterpriseAI #AIAssistant #PrivacyByDesign #LLM #AIProductUpdate
