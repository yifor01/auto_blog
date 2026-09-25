---
title: Some Supabase customers are publicly exposing reams of people’s data to the
  web
source: TechCrunch AI
url: https://techcrunch.com/2026/09/25/some-supabase-customers-are-publicly-exposing-reams-of-peoples-data-to-the-web/
model: claude-code/sonnet
generated_at: '2026-09-25T20:57:27.212281'
score: 69
---

📌 1.6萬個 Supabase 資料庫正公開外洩個資

TL;DR：資安公司 UpGuard 發現約 1.6 萬個 Supabase 資料庫存在個資外洩，凸顯 vibe coding 熱潮下的設定風險。

當建站門檻因 AI 輔助程式設計降到近乎為零，資安門檻並沒有跟著一起下降。開發平臺 Supabase 今年稍早才以 100 億美元估值站上鎂光燈下，主因之一正是大量開發者把「vibe-coded」的應用架設在其平臺上；但這家公司也一直被批評使用者的資安意識與設定沒能跟上成長速度。

🤔 資料庫外洩早已不是新聞，這次是規模認定

多年來，儲存伺服器、資料庫與網站設定不當已導致無數資料外洩事件，範圍涵蓋軍方敏感郵件、移民與簽證申請資料、機密政府檔案、數十萬筆駕照掃描檔，乃至兒童個資。如今 AI vibe coding 的興起，正在為這波外洩再添柴火，而其中越來越多案例都與 Supabase 有關——原因很簡單，越來越多人用它來存放資料。

📊 名稱、地址、電話、密碼都在公開網路上

UpGuard 告訴 TechCrunch，他們找到約 1.6 萬個 Supabase 上曾存在某種程度個資外洩的資料庫，公開暴露的內容包含姓名、地址、電話號碼與使用者密碼，另外也發現數量較少的密碼與驗證 token。這些資料庫牽涉多個不同專案，例如印度一家成人直播網站上使用者與性工作者的私人對話紀錄、美國一家代客泊車服務的數千筆車牌資料，以及一家移民與搬遷服務用戶的聯絡資訊。其中一個資料庫屬於某非洲國家駐法國領事館，另一個則被用於攔截簡訊的虛擬 SIM 卡農場所使用，這類農場通常用來為線上帳號驗證一次性密碼，進而發動詐騙與釣魚攻擊。多數外洩資料集位於美國，但 UpGuard 強調這是全球性問題，這項發現也延續了先前針對 Supabase 上曝露資料庫（包括多家 Y Combinator 新創與其他知名應用）的研究。

💡 官方回應：安全是共同責任

Supabase 資安長 Bil Harmer 回應表示，公司尚未看過這份研究，但強調旗下專案「預設安全」，資安是公司與客戶的共同責任：「我們提供安全的預設值與工具，客戶則掌控自己專案的實際設定」，公司在發現資安問題時也會通知受影響客戶。UpGuard 研究員 Greg Pollock 則表示，這份研究的重點在於喚起外界對資料外洩問題的關注。

⚠️ 這不是新漏洞，而是既有風險的規模量化

這篇報導呈現的是既有「使用者誤設定或不自知地公開資料庫」問題的規模化調查，並非揭露新的漏洞或修補方案，文中也未說明 UpGuard 具體的掃描方法。

🎯 給工程團隊的啟示

用 AI 快速生成的應用程式碼，本身可能就帶有安全缺陷，或需要開發者主動理解並設定的安全機制（例如 Row Level Security、公開存取權限）。在把資料庫接上任何 vibe-coded 專案之前，先確認預設的存取權限範圍，並把資料庫公開暴露檢查納入上線前的例行檢查清單，而不是等外部研究機構先發現。

🔗 來源
- 標題：Some Supabase customers are publicly exposing reams of people's data to the web
- 作者／機構：Zack Whittaker, TechCrunch
- 連結：https://techcrunch.com/2026/09/25/some-supabase-customers-are-publicly-exposing-reams-of-peoples-data-to-the-web/

#Supabase #DataBreach #VibeCoding #CyberSecurity #DataPrivacy #CloudSecurity #Misconfiguration #AppSecurity #UpGuard #SoftwareEngineering
