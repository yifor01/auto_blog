---
title: Kobo can run apps now
source: Hacker News
url: https://bandarlabs.github.io/Cobalt/
model: claude-code/sonnet
generated_at: '2026-08-22T06:24:14.917855'
score: 85
---

📌 開源專案讓 Kobo 電子閱讀器變身應用程式平臺

TL;DR:Cobalt讓Kobo電子閱讀器能透過簽名商店安裝第三方應用程式,且完全不影響原廠韌體,可隨時回復原狀。

電子書閱讀器通常被鎖死成單一功能裝置,但一個叫Cobalt的開源專案證明,Kobo的電子紙螢幕上其實可以跑Hacker News閱讀器、OPDS圖書館用戶端,甚至用摩斯電碼在前光燈上閃字傳訊息——而且不需要對韌體進行破解。這則貼文在Hacker News上獲得480個讚、166則留言,討論度不低。

🤔 解決什麼問題、為誰而做

Cobalt是一套開源的應用程式平臺,包含啟動器(launcher)、經簽名的App Store、Rust SDK,以及讓每個應用程式都在自己獨立、無特權(unprivileged)行程中執行的執行環境(runtime)。使用者只需要透過USB安裝一次,之後所有應用程式的安裝、更新、移除都能直接在裝置上透過Wi-Fi完成。重開機則會回到原廠的Kobo閱讀器介面,代表整個安裝是可逆的。

🧩 核心架構與設計理念

每個應用程式都是一支靜態編譯的ARM執行檔,以獨立、無特權行程的形式跑在原生硬體上。開發者只需實作KoboApp介面,以宣告式的方式描述畫面,執行環境便會負責處理版面配置、電子紙螢幕的更新(refresh)規劃、返回鍵導覽與生命週期管理。

安全模型上,應用程式不能直接開啟裝置資源,而是必須「請求」授權——網路、儲存空間、音訊、前光燈與Wi-Fi都是能力閘控(capability-gated)的資源,一旦被拒絕,回傳的會是應用程式可以自行處理的值,而不是直接崩潰。App Store則從一個固定的GitHub Release讀取經簽名的目錄(catalog),每個安裝包只包含一支ARM執行檔與一份經簽名的標準化清單(manifest),執行環境在應用程式啟動前會驗證目錄、安裝包、已安裝的清單與執行檔本身。

另一個值得注意的設計是應用程式與平臺版本的解耦:應用程式的發布獨立於平臺版本,只要合併一個應用程式的PR,系統就會自動編譯出ARM版本、簽名並更新目錄,不需要Cobalt本身升版或重新安裝,應用程式就會直接出現在Store裡。平臺本身的更新則透過Settings頁面走另一條獨立於應用程式目錄的通道,同樣經由Wi-Fi完成。所有安裝與目錄交易都具備recovery-safe特性,萬一更新中途被中斷,裝置會停留在原本的版本,而不會變成無法開機的磚。

目前README列出的應用程式相當多元:讀取arXiv自2023年12月起釋出的HTML版論文(摘要、章節、數學式與結果表格會依螢幕分頁呈現)的閱讀器、支援Project Gutenberg、Standard Ebooks、Open Library等任何OPDS圖書館的閱讀器、包含完整留言串的Hacker News用戶端、把網站文章抽離版面呈現的類RSS閱讀器、在背景蒐集當日新聞的應用程式、把前光燈當摩斯電碼發報機使用的訊息應用(僅存在於Store,用來證明Wi-Fi安裝管道確實能送達平臺原始安裝包沒有內建的程式)、由AI生成劇本並朗讀的有聲書應用,以及讓使用者離開鍵盤也能核准或拒絕coding agent請求的應用程式。

🧩 怎麼安裝、怎麼貢獻

完整的安裝流程(含復原步驟)記載在docs/INSTALL.md,USB纜線只有第一次安裝時需要用到。應用程式的貢獻方式就是提交一般的PR:只要能在你的裝置上跑,而且PR附上運作證明,就會被合併並發布。若想移植到其他Kobo機型,專案也歡迎,但建議先開issue討論並取得裝置設定檔(device profile)的共識,細節見docs/CONTRIBUTING_APPS.md。

⚠️ 限制

Cobalt不會取代Kobo原本的開機鏈,裝置寫入動作也被限制在完全相符的硬體與韌體版本上,重開機即回到原廠閱讀器。不過,第一次安裝仍會修改使用者儲存分割區上的檔案,且專案聲明不提供任何保固。目前只有Kobo Clara BW這款機型的設定檔經過硬體測試,在尚未有經審查、經硬體測試的設定檔之前,不建議安裝到其他機型上。Cobalt是獨立專案,與Rakuten Kobo沒有官方關聯。

🎯 實務啟示

對工程師而言,Cobalt是在受限的嵌入式硬體上,用能力閘控(capability-gated)沙箱與簽名式應用程式分發打造安全第三方生態系的一個具體案例,值得作為思考「如何在鎖死的消費性裝置上安全開放第三方應用」的參考架構。

🔗 來源
- 標題:Kobo can run apps now
- 作者/機構:thepoet(Hacker News 發文者)
- 連結:https://bandarlabs.github.io/Cobalt/

#Kobo #OpenSource #Ereader #EInk #RustLang #EmbeddedSystems #AppStore #Sandboxing #HackerNews #DIY
