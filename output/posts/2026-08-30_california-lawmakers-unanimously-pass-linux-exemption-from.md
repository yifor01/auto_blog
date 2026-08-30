---
title: California lawmakers unanimously pass Linux exemption from age-verification
  law
source: Hacker News
url: https://www.tomshardware.com/software/linux/california-lawmakers-unanimously-pass-linux-exemption-from-age-verification-law-software-distributed-under-the-gpl-mit-bsd-and-apache-licenses-are-exempt
model: claude-code/sonnet
generated_at: '2026-08-30T11:04:14.998655'
score: 45
---

📌 加州修法：GPL／MIT／BSD 授權軟體，正式豁免年齡驗證法

TL;DR：加州參眾兩院無異議通過修正案，Linux 發行版與開源軟體不再被納入年齡驗證法規範。

如果你的產品建立在 Debian、Fedora、Ubuntu 或 Arch 之上，原本可能得在明年開始向使用者收集年齡資料。現在，這個風險被一條修正案擋掉了。

🤔 **Digital Age Assurance Act 原本要管到哪裡**

加州去年 10 月由州長 Gavin Newsom 簽署的 Digital Age Assurance Act，預計於 2027 年 1 月 1 日生效，要求作業系統供應商在帳號設定階段收集使用者年齡資料，並將訊號傳遞給應用程式商店與開發者。過去近一年，Linux 發行版與 SteamOS 是否也必須比照 Windows、macOS、iOS、Android 辦理，一直沒有定論，也引發 Linux 開發者與 Electronic Frontier Foundation 的批評。

🧩 **修正案 AB 1856 怎麼劃出豁免範圍**

加州眾議員 Buffy Wicks（同時是原法案與這次修正案的起草人）今年 2 月提出豁免條文，該修正案已於 8 月 26 日以 39 比 0 通過參議院表決，隔日眾議院也完成一致性表決，目前已送交州長簽署。修正案的核心做法是重新定義「作業系統供應商」，排除任何以「允許使用者複製、再散布、修改」的授權條款釋出軟體的個人或機構；換句話說，只要是採用 GPL、MIT、BSD 或 Apache 授權釋出，就符合豁免條件，這直接讓 Debian、Fedora、Ubuntu、Arch 及 BSD 家族全數脫離法規範圍。

修正案還加了兩項排除：一是排除「未透過受規範的應用程式商店以獨立可執行應用程式形式提供給消費者」的軟體元件，涵蓋透過 apt、pacman 等套件管理工具散布的函式庫與相依套件；報導指出，雖然法條沒有明講套件庫不算應用程式商店，但商店在法規下的主要義務是向作業系統供應商索取年齡訊號並轉交開發者，而豁免的開源系統本來就不會產生這種訊號。二是排除僅在宿主應用程式內執行的擴充功能／外掛商店，讓瀏覽器擴充功能商店也不在規範範圍內。

此外，修正案刪除了原法條中「使用裝置的主要使用者即為兒童」的「使用者」定義；報導指出，這個定義在字面上等於把加州每一位裝置擁有者都歸類為兒童，與整套年齡訊號機制（讓成年人在設定帳號時宣告年齡，裝置因此被標記為 18 歲以上）互相矛盾。修正案也新增規定，禁止任何人在法律未要求的情況下，向作業系統供應商或應用程式商店索取年齡訊號，避免這個 API 被挪用成通用資料蒐集管道；同時給予平臺與開發者「善意安全港」保護，避免訊號有誤時被追究責任。

⚠️ **SteamOS 歸屬仍是灰色地帶**

Windows、macOS、iOS、Android 仍完全在法規範圍內，須自 2027 年 1 月 1 日起於帳號設定階段收集年齡資料，在此日期前已設定好的裝置則適用 2027 年 7 月 1 日的較晚期限。至於 SteamOS，報導指出其歸屬尚不明確：系統元件基於 Arch、屬於開源，但 Valve 是將它與私有的 Steam 用戶端一起打包發行。另外，以 MIT 與 Apache 授權釋出的 GrapheneOS，因為完全符合修正案的豁免條件而不再受該法規範，不過報導也提到巴西的 Digital ECA 法規仍會適用於它。

🎯 **實務啟示**

若你的專案或發行版是以 GPL、MIT、BSD 或 Apache 等開放授權釋出，這次修正案等於明確排除了在加州因年齡驗證法而需要額外實作年齡收集流程的義務；但如果產品是「開源系統元件 + 私有用戶端」的混合形態（如 SteamOS 的模式），仍需要持續關注後續是否會被單獨認定為受規範對象。

🔗 **來源**
- 標題：California lawmakers unanimously pass Linux exemption from age-verification law
- 連結：https://www.tomshardware.com/software/linux/california-lawmakers-unanimously-pass-linux-exemption-from-age-verification-law-software-distributed-under-the-gpl-mit-bsd-and-apache-licenses-are-exempt

#Linux #OpenSource #GPL #MIT #BSD #California #TechPolicy #DigitalRights #SteamOS #GrapheneOS
