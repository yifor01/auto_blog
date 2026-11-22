---
title: Advice for the next 100 Rust GUIs
source: Hacker News
url: https://linebender.org/blog/next-100-guis/
model: claude-code/sonnet
generated_at: '2026-11-22T22:42:34.262246'
score: 64
---

📌 Linebender創辦人談Rust GUI:AI正在拆除最後的門檻

TL;DR:Raph Levien四年後重新審視Rust GUI生態,指出AI輔助編碼讓「用Rust寫UI」的理由前所未有地充分。

四年前,同時精通Rust與UI開發的工程師幾乎是稀有物種;如今,這道門檻正在被LLM悄悄拆除。Linebender創辦人Raph Levien在〈Advice for the next 100 Rust GUIs〉中,接續他2022年那篇〈Advice for the next dozen Rust GUIs〉,盤點了這四年半來Rust GUI生態的進展與未解難題。

🤔 背景:採用遲緩,但理由正在消失

文章指出,自2022年以來已有約20個Rust GUI toolkit相繼發布,但真正用Rust做UI的旗艦應用仍不多,最具代表性的是Zed編輯器,它基於自家框架GPUI打造,證明了用Rust出貨UI是可行的——GPUI也因此成為AI驅動重寫專案的熱門選擇,其中最受關注的案例是Discord。作者認為過去採用緩慢的核心原因,是Rust比TypeScript、Kotlin、Swift更難寫,同時精通Rust與UI的工程師也難找;但有證據顯示LLM寫Rust的成本並未明顯高於其他語言,而Rust的型別系統有助於在大型程式碼庫中維持不變性(invariant),讓維護性更高。既然各語言的AI編寫成本相近,選擇安全性與效能更好的Rust就變得理所當然——這也是Rust正快速成為「AI重寫既有程式碼庫」首選語言的原因。

🧩 技術進展:text layout與accessibility已基本解決,但compositor仍沒人解

作者指出,2022年最大的未解難題之一是text layout,如今透過Parley專案(獲得Google、Canva、Dioxus〔現為Cognition〕持續投入與社群貢獻)已有不錯的解法,目前多數新的Rust UI toolkit都採用它;Cosmic Text則作為替代方案,避免生態過度依賴單一專案。AccessKit也已從起步階段變成多數toolkit採用的穩固基礎設施,但作者提醒「有良好整合」和「只是打勾應付」是兩件事,豐富文字編輯的可及性(accessibility)仍待補強,而啟用accessibility後的效能下滑(例如egui每個動畫幀都要重建並diff樹)也是尚待解決的問題。相對地,善用系統合成器(system compositor)——例如讓影片在硬體加速層播放——至今仍是未解之題,subduction函式庫雖有進展,但尚未被普遍整合進主流toolkit。

💡 深入分析:原生 UI + Rust商業邏輯,成為行動裝置的務實解法

Windows至今沒有明確的原生UI選項,Mac則在AppKit與SwiftUI之間存在分裂,而SwiftUI本身也有效能問題。相較之下,行動平臺持續投入(例如iOS的Liquid Glass),手勢辨識、滾動動態、輸入法等細節若用跨平臺框架很難做到100%貼合原生體驗。因此作者觀察到一條務實路徑:UI層用原生toolkit,「商業邏輯」用Rust撰寫——Shopify近期放棄React Native就採用此架構,1Password據信亦是如此,而Discord在行動端的「Phoenix」計畫同樣走這條路(桌面端則用GPUI)。不過作者也展示了純Rust行動UI的進展:android-view專案的編輯器demo顯示滑動輸入、以空白鍵滾動遊標、語意區塊刪除等IME功能已可運作,CJK所需的composition region也支援,並透過AccessKit具備基本的可及性。

⚠️ 限制:immediate mode的可擴展性疑慮

Rust GUI生態目前在immediate mode與retained mode之間尚無定論。Immediate mode程式碼量少、架構簡單,很適合遊戲開發,但作者擔心它難以規模化——「前90%很好做,後90%卻變得更難」,因為要做到生產等級,必須建立穩定的widget identity以支撐accessibility樹,並可靠地快取如text layout這類昂貴的中間產物。

🎯 實務啟示

對正在評估Rust GUI的工程團隊而言,Parley與AccessKit已是可直接採用的成熟基礎設施;若目標是行動端,原生UI搭配Rust邏輯層仍是風險最低的架構選擇;若考慮immediate mode框架,須提早評估其在accessibility與效能快取上能否撐到生產規模。

🔗 來源
- 標題:Advice for the next 100 Rust GUIs
- 作者／機構:raphlinus
- 連結:https://linebender.org/blog/next-100-guis/

#Rust #GUI #AIcoding #SoftwareEngineering #Zed #GPUI #Accessibility #CrossPlatform #MobileDev #OpenSource
