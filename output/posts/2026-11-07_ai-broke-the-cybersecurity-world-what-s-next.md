---
title: AI broke the cybersecurity world. What’s next?
source: The Verge AI
url: https://www.theverge.com/podcast/1029038/ai-cybersecurity-hackers-data-breach-dark-age-alex-stamos
model: claude-code/sonnet
generated_at: '2026-11-07T21:11:36.735769'
score: 49
---

📌 開源工具就能入侵銀行？AI 把攻擊鏈整個反過來了

TL;DR：Cognition 資安長 Alex Stamos 警告，AI 讓攻擊鏈即時化，開源工具已能入侵跨國企業。

過去一個月，光是看得到的破口就有：PHP、Node 的重大漏洞、一連串 AI 新創遭入侵、史上最大規模的加密貨幣盜竊案，還有一次從單一廠商外洩一路炸開五千家公司的連鎖攻擊。資安圈的一位 CISO 朋友問同行「大家是不是都累了」，得到的答案是齊聲說「對」。

🤔 一個月內炸開的供應鏈

在 Decoder 播客的這集訪談中，Cognition 資安長（同時也是史丹佛網路政策中心講師）Alex Stamos 指出，十月以來的攻擊事件並非個別孤立事件，而是彼此串接：攻擊者先入侵提供 AI 服務的 Fireworks，竊得 API 金鑰後用來打進 Cursor，再透過 Cursor 推送一個惡意外掛，一口氣波及約 5,000 家下游企業。同時期還發生了 Binance 遭竊案（Stamos 稱之為人類史上規模最大的一次盜竊），以及南韓多家銀行與約 200 家企業接連失守。Stamos 形容十一月初的狀態，是資安團隊「長時間維持在 DEFCON 2 等級戒備」。

🧩 攻擊鏈被倒過來做

Stamos 用「kill chain（攻擊鏈）」這個從軍事借來的詞解釋為何這波攻擊特別棘手。傳統模式是：攻擊者先花大量時間研究目標軟體、找漏洞、寫 exploit，準備好後才一次性對幾百、幾千個目標發動攻擊，前期準備與後期執行是分開的兩個階段。他指出，AI 讓這個順序整個反過來：現在可以讓一套 AI 系統直接對著目標「放著跑」，即時找漏洞、即時寫 exploit、即時入侵，研究與攻擊變成同一個即時迴圈。

他提到一個具體案例：一款名為 ARTEX 的中國開源工具（GitHub 上有英文翻譯版），只要在後端接上一個被移除安全限制（obliterated）的 GLM-5.3 模型，就能讓使用者入侵數量驚人的企業，而且這一切是「下載即用」的等級。Stamos 將現況比作上世紀九十年代的網路世界：規則尚未成形、工具卻已經足夠強大，差別是如今全世界的基礎設施都掛在網路上，攻擊可以被自動化到過去無法想像的規模。

💡 誰在用，又為什麼現在失控

Stamos 強調，這波攻擊不只是因為對手「決定」要攻擊，而是開放權重模型（open-weight models）的能力已經跨過一個門檻，足以自動化完成大部分攻擊鏈。更關鍵的是，攻擊者不再需要依賴那些有安全防護、有紀錄可供執法單位追蹤的前沿模型，他們改用被移除限制的開源模型，等於繞開了原本內建在商用 AI 服務裡的守門機制。他也提到，九十年代那批具備這類技能的人多數集中在一個房間裡（早期 DEFCON 只有幾百人），而現在擁有工具、具備經濟動機、又身處執法難以觸及地區的人大幅增加。

⚠️ 不是末日論，但要先過一段黑暗期

Stamos 並不認為長期而言這是無解的末日局面，但他直言接下來會是一段「黑暗時代」，整個產業得重新摸索如何應對這種攻防節奏。資安產業過去數十年建立的防禦模式，是假設攻擊者需要時間準備，而當攻擊與研究被壓縮進同一個即時流程，傳統「先補丁、再觀察」的節奏將跟不上。

🎯 實務啟示

對工程團隊而言，這段訪談點出的具體風險是供應鏈串接攻擊：你依賴的 AI 服務供應商被攻破，金鑰外洩後可能直接波及你產品的使用者。盤點並限制第三方 API 金鑰的權限範圍、縮短金鑰生命週期、對外掛／套件更新加入簽章驗證，會是眼下比較務實的優先事項，而不是等著單一一次性的「資安升級」解決問題。

🔗 來源
- 標題：AI broke the cybersecurity world. What's next?
- 作者／機構：Nilay Patel／The Verge（Decoder Podcast，訪談對象：Alex Stamos, Cognition CSO）
- 連結：https://www.theverge.com/podcast/1029038/ai-cybersecurity-hackers-data-breach-dark-age-alex-stamos

#AI #Cybersecurity #Hacking #SupplyChainAttack #OpenWeightModels #AIsecurity #DataBreach #Decoder #TheVerge #InfoSec
