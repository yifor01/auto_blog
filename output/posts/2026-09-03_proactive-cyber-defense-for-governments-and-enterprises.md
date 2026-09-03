---
title: Proactive cyber defense for governments and enterprises
source: Google DeepMind
url: https://deepmind.google/blog/proactive-cyber-defense-for-governments-and-enterprises/
model: claude-code/sonnet
generated_at: '2026-09-03T20:05:08.984719'
pinned: true
---

📌 【Google DeepMind 官方發布】漏洞修補進入分鐘級，Fairwind Program 正式啟動

TL;DR：Google DeepMind 宣布 Fairwind Program，用 Gemini 3.8 Flash Cyber 與 CodeMender 讓政府與企業自主修補漏洞。

漏洞被發現到被修補之間的空窗期，一直是資安防禦最脆弱的環節。Google DeepMind 這次公布的做法，是把這段時間從「以週計」壓縮到「以分鐘計」。

🤔 **防禦端的老問題：強模型難控管，小模型修不動複雜漏洞**

Google DeepMind 指出，想用先進 AI 做資安防禦的團隊，長期面臨兩難：要嘛採用龐大的前沿模型，部署成本高、在企業整套程式碼庫中難以控管；要嘛改用較小的開放權重模型，卻可能在複雜的漏洞修復任務上力有未逮，還得自己從頭搭建工具鏈與基礎設施。2026 年 9 月 2 日，Google 宣布啟動 Fairwind Program，這是一個限量存取計畫，開放給政府機關與受信任的合作夥伴，讓他們能主動、大規模地解決資安風險，第一步就是提供進階 Gemini 模型的存取權，協助防禦者自主找出並修復漏洞，藉此保護關鍵基礎設施、公共服務與國家安全。

🧩 **CodeMender 加上專屬網路安全模型，把修補流程接上 agentic 規模**

Fairwind Program 的核心組合，是 Google 目前最先進的網路安全模型 Gemini 3.8 Flash Cyber，搭配既有的 CodeMender 修補框架，讓防禦者得以在 agentic 規模上找出、驗證並修復漏洞。文中特別點出一個立場：單純標示出弱點只會製造警覺與恐懼，真正帶來安全感的是自動化地把它找出來並修好。藉助 CodeMender 與 Gemini 3.8 Flash Cyber 的組合，防禦者能以遠低於傳統前沿模型的營運成本，寫出並驗證程式碼修補；原本可能耗時數週的手動修復流程，如今能在組織自有的安全雲端環境中，於數分鐘內產出經過驗證、可直接部署的修補程式。

📊 **650 個以上合作夥伴，優先開放三大類對象**

計畫採取分階段開放存取，目前全球已有超過 650 個參與夥伴，初期優先鎖定三類對社會韌性最關鍵的政府與企業：
- 政府與國家級網路安全主管機關：強化公部門網路與公民服務，抵禦針對性入侵。
- 關鍵基礎設施營運商：保護醫療、電信、能源與金融網路等核心服務，避免營運中斷。
- 核心技術平臺：強化被廣泛使用的軟體基礎，一次提升下游數百萬使用者的數位安全水準。

為確保這些強大能力被負責任使用，參與組織須遵守嚴格的操作規範，包含將存取權限限制在內部資安、事件應變或滲透測試團隊成員，並部署如多因子驗證等防護措施。

💡 **開放模型之外，也留了一條給所有 Google Cloud 客戶的路**

Google DeepMind 表示，Fairwind Program 目前優先讓計畫內客戶使用 Gemini 3.8 Flash Cyber，但任何 Google Cloud 客戶都可以主動運用 CodeMender，搭配 Gemini Enterprise Agent Platform 上公開可用的模型，並結合 AI Threat Defense 提供的解決方案來保護自身程式碼。文中也強調，這項計畫建立在 Google 多年來推動零信任（zero-trust）架構、進階 AI 防禦與內建安全機制的基礎上，這些機制目前每天保護著數十億個帳號。透過 Google.org，Google 全球資安相關資助總額已超過 1 億美元；根據最新公布的 2026 年 Google.org 美國資安影響報告，已投入 3,600 萬美元支持 35 間網路安全診所，為美國超過 1,250 間醫院、公立學區與市政公用事業單位提供免費的實務資安支援。

⚠️ **尚未揭露的技術細節**

素材未提供 Gemini 3.8 Flash Cyber 的模型規格、CodeMender 修補成功率等量化指標，也未列出 650 個合作夥伴的完整名單，這些留待 Google 後續資訊釋出。

🎯 **實務啟示**

對於營運關鍵基礎設施或大型軟體平臺的團隊而言，「修補速度」正在成為新的防禦指標。即使暫時不在 Fairwind Program 的優先名單內，也可以先透過 Google Cloud 上的 CodeMender 與公開模型組合，評估自動化修補流程能否嵌入既有的資安維運節奏。

🔗 **來源**
- 標題：Proactive cyber defense for governments and enterprises
- 作者／機構：Google DeepMind
- 連結：https://deepmind.google/blog/proactive-cyber-defense-for-governments-and-enterprises/

#GoogleDeepMind #CyberSecurity #Gemini #CodeMender #AIAgent #VulnerabilityManagement #CriticalInfrastructure #ZeroTrust #GovernmentTech #AIforSecurity
