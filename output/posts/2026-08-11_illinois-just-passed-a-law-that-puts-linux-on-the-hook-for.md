---
title: Illinois just passed a law that puts Linux on the hook for age verification
source: Hacker News
url: https://linuxstans.com/illinois-hb5511-operating-system-age-verification/
model: tencent/hy3:free
generated_at: '2026-08-11T07:25:36.931212'
score: 65
---

📌 【法規警訊】伊利諾州通過新法：開源作業系統也必須落實年齡驗證

TL;DR：伊利諾州新通過的 HB5511 法案，要求作業系統供應商必須建立年齡驗證機制，且未排除開源軟體。

隨著各州針對兒童網路安全加強立法，伊利諾州（Illinois）最近通過的 HB5511 法案（Children’s Social Media Safety Act）引起了開發者社群的熱議。雖然政府宣傳重點聚焦在 TikTok 與 Instagram 等社群平臺，但該法案實際上對「作業系統供應商」提出了全新的法律義務。

🤔 **法案細節：除了社群媒體，還管到了作業系統**

根據該法案的定義，任何開發連網作業系統的實體（無論是商業或非營利性質）都屬於「受規管製造商」（covered manufacturer）。這意味著，該法律的範疇不僅限於社群平臺，也涵蓋了作業系統層級的設計。

該法案將「作業系統供應商」列為一個獨立的法律類別，並設定了明確的合規期限。

🧩 **2028 年期限：作業系統必須提供的技術規格**

根據法案規定，作業系統供應商必須在 2028 年 1 月 1 日前完成以下開發工作：

1. **建立年齡聲明介面**：在裝置設定階段，提供一個易於操作的畫面，讓帳戶持有者可以標示出生日期或年齡。
2. **提供加密 API 訊號**：當應用程式或平臺請求年齡資訊時，作業系統必須透過一致且加密的 API，回傳一個「年齡層級」（age-bracket）訊號。
3. **嚴格的資料最小化原則**：回傳的訊號並非具體的生日，而是將年齡劃分為特定區間：
   - 13 歲以下
   - 13 至 15 歲
   - 16 至 17 歲
   - 18 歲以上
   且系統僅能回傳回答問題所需的最小資訊，不得將資料提供給法律規定之外的第三方。

一旦應用程式收到「未成年」的訊號，法律即視為該用戶為未成年人，進而啟動社群平臺的預設保護機制（如：預設關閉演算法推薦、禁止深夜通知、限制陌生人聯繫等）。

⚠️ **關鍵差異：伊利諾州未排除開源軟體**

這正是此法案與其他州（如科羅拉多州）最大的不同點。在科羅拉多州，為了避免對開源生態系造成負擔，法律明確豁免了使用「開放授權」（open license）發佈的作業系統、應用程式、程式碼儲存庫（如 GitHub、GitLab）以及容器平臺（如 Docker、Podman）。

然而，伊利諾州的 HB5511 法案在定義上極其寬泛，目前並沒有針對開源軟體設置豁免條款。這對於維護開源社群、缺乏專門合規部門的非營利專案來說，可能構成嚴峻的法律挑戰。

📊 **執行與罰則：數字上的落差**

關於違規罰則，目前存在資訊不一致的情況：
- **法案條文內容**：針對過失違規，每名受影響兒童最高罰款 2,500 美元；針對故意違規，最高罰款 7,500 美元。
- **州長新聞稿宣稱**：最高罰款可達每次違規 50,000 美元。

目前該法案的執行權僅歸屬於伊利諾州檢察長（Attorney General），並不允許個人提起私人訴訟。

🎯 **實務啟示**

對於開源軟體維護者與作業系統開發者而言，這是一個值得關注的信號。雖然 2028 年的期限尚有餘裕，但「數位年齡保證」（Digital Age Assurance）已成為各州立法的趨勢。開發者需密切關注各州對於「開放授權軟體」豁免條款的立法走向，以評估未來是否需要實作標準化的年齡訊號 API。

🔗 **來源**
- 標題：Illinois just passed a law that puts Linux on the hook for age verification
- 連結：https://linuxstans.com/illinois-hb5511-operating-system-age-verification/

#Linux #OpenSource #OperatingSystem #HB5511 #TechLaw #Privacy #SoftwareEngineering #Cybersecurity #DigitalSafety #Compliance
