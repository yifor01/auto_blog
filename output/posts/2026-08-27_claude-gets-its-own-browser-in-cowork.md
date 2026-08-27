---
title: Claude gets its own browser in Cowork
source: Claude Blog
url: https://claude.com/blog/cowork-built-in-browser
model: claude-code/sonnet
generated_at: '2026-08-27T17:26:01.911501'
score: 91
---

📌 Claude Cowork 內建瀏覽器：不用借用你的分頁，Claude 自己開一個

TL;DR：Claude Cowork 桌面版新增內建瀏覽器，讓 Claude 能獨立瀏覽網頁、填表單，不再需要借用你自己的瀏覽器分頁。

過去要讓 Claude 在 Cowork 裡處理網頁任務，唯一的路是透過 Claude in Chrome 擴充功能，把你自己的瀏覽器交出去。現在 Anthropic 給了 Claude 一個屬於它自己的瀏覽器。

🤔 **兩套瀏覽方式，各自對應不同情境**

Claude Cowork 桌面版現在內建了一個瀏覽器：當任務需要用到網站時，側邊面板會自動開啟瀏覽器，Claude 在裡面導覽網頁、閱讀內容、點擊、輸入文字。這個瀏覽器與你自己的瀏覽器完全獨立，Claude 看不到你的分頁、書籤或密碼；要讓 Claude 保持登入狀態，你可以逐一從 macOS 上的 Chrome、Edge、Firefox，或 Windows／Linux 上的 Firefox，把特定網站的登入資訊帶過去，銀行、email、單一登入（SSO）類網站則預設排除，除非你主動選擇加入。

這也是它與 Claude in Chrome 的分野：如果任務就在你目前開著的那個分頁上，Claude in Chrome 仍是正確選擇；但如果只是需要「一個瀏覽器」去做研究彙整、或到沒有連接器（connector）的入口網站抓資料，內建瀏覽器就能讓你把網頁任務直接交出去，同時繼續手邊的工作。若你已經在用 Claude in Chrome，它會繼續運作並維持為預設；否則 Claude 會改用內建瀏覽器，也可以隨時在「設定 → Cowork → 慣用瀏覽器」切換。

🧩 **同一套安全防護機制**

文章特別提到，內建瀏覽器和任何在瀏覽器中行動的 AI agent 一樣，帶有 prompt injection 風險：頁面中藏著的指令可能試圖操控 Claude 的行為。它套用了和 Claude in Chrome 相同的防護機制，包括會將 Claude 的行動與使用者原始需求進行比對的檢查機制。Anthropic 強調這些措施能有意義地降低風險，但無法完全消除，因此建議先從你信任的網站開始使用。

🎯 **實務啟示**

這項功能對工程師而言，實際價值在於「無連接器任務」的自動化，例如從供應商入口網站彙整當月發票、或從沒有 API 的儀表板抓取數字，這類過去只能手動處理、或得先幫 Claude 接上你自己瀏覽器的工作，現在可以直接交辦出去。但因為 prompt injection 風險依然存在，把這類自動化導入生產流程前，建議先鎖定信任的網站範圍，並留意 Anthropic 提供的安全指南。功能本週開始在 Pro、Max、Team 方案的桌面版（macOS、Windows、Linux beta）陸續推出，Enterprise 管理員則可立即在組織設定中開啟。

🔗 **來源**
- 標題：Claude gets its own browser in Cowork
- 作者／機構：Anthropic
- 連結：https://claude.com/blog/cowork-built-in-browser

#Anthropic #Claude #ClaudeCowork #AIAgent #BrowserAutomation #PromptInjection #AIProductivity #DesktopApp #Automation #AgenticAI
