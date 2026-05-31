---
title: "nicobailon/pi-subagents"
source: GitHub Trending
url: https://github.com/nicobailon/pi-subagents
score: 23
model: tencent/hy3-preview:free
generated_at: 2026-05-31T19:48:23.016225
---

📌 【nicobailon】pi-subagents：讓 Pi 能派遣專注子代理協作  

你是否曾希望在寫程式、審查程式碼或規劃方案時，能再多一雙「模型之眼」來檢查正確性、測試或不必要的複雜度？  

🤔 **當開發工作需要第二或第三個視角時，手動切換對話或重新啟動會話顯得繁瑣**  

在日常的編碼流程中，我們常會想讓 AI 再看一次 diff、諮詢第二個意見，或是讓不同的專注點（正確性、測試、複雜度）同時進行。然而，建立獨立的子會話、撰寫設定或學習特殊指令往往會增加使用門檻。  

🧪 **安裝後直接用自然語言派遣子代理**  

- **安裝方式**：`pi install npm:pi-subagents`（此為唯一必要步驟）  
- **使用方式**：安裝後，僅需在 Pi 對話中用平實的語言提出需求，Pi 會自動啟動一個專注的子會話（subagent），執行指定任務並將結果帶回主會話。  
- **前景與背景**：  
  - 前景執行的子代理會即時在對話中流式回饋結果。  
  - 背景執行的子代理會持續工作，之後可隨時檢查進度或結果。  
- **不會自動啟動**：安裝擴充功能本身不會在背景啟動任何審查者；它僅賦予 Pi 一個「委派」工具，需要你在提示中明確說明要使用哪種子代理。  

💡 **常見的第一次使用範例**（涵蓋大多數日常場景）  

- `Use reviewer to review this diff.`  
- `Ask oracle for a second opinion on my current plan.`  
- `Use scout to understand this code based on our discussion then ask me clarification questions.`  
- `Run parallel reviewers: one for correctness, one for tests, and one for unnecessary complexity.`  

這些指令示範了如何讓不同焦點的子代理同時或依序處理程式碼審查、方案驗證、程式理解等任務，無需手動建立代理、撰寫設定或學習斜線指令。  

⚠️ **使用時需注意的幾點**  

- 必須先執行 `pi install npm:pi-subagents` 才能使用委派功能。  
- 目前的說明中未提及自動背景審查或預設工作流程；所有子代理的啟動均來自於你的明確提示。  
- 功能的實際表現會依賴於底層 Pi 模型的能力與你提供的具體指令清晰度。  

🎯 **適合想要在工作流程中加入「第二雙眼」而不增加複雜度的開發者**  

- 程式碼審查：讓 reviewer 子代理快速檢視 diff。  
- 方案驗證：透過 oracle 取得第二個意見。  
- 程式理解：使用 scout 先行探索，再根據對話提出澄清問題。  
- 多維度平行檢查：同時啟動多個專注子代理，分別關注正確性、測試覆蓋度與複雜度。  

🔗 **專案連結**  
📂 專案名稱：pi-subagents  
👤 作者：nicobailon  
🔗 GitHub：https://github.com/nicobailon/pi-subagents  

你有試過讓 Pi 分派子代理來協助程式審查或方案驗證嗎？歡迎在留言區分享你的使用心得或想嘗試的場景 👇  

#AI #Pi #subagents #程式審查 #開發工具 #GitHubTrending #nicobailon #開發效率
