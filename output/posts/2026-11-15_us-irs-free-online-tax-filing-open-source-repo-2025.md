---
title: US IRS free online tax filing open source repo (2025)
source: Hacker News
url: https://github.com/IRS-Public/direct-file
model: claude-code/sonnet
generated_at: '2026-11-15T21:53:50.540299'
score: 55
---

📌 美國國稅局開源報稅系統：Fact Graph 推理引擎拆解

TL;DR：IRS Direct File 是美國政府免費電子報稅服務，核心靠 Scala 寫成的 Fact Graph 處理「資訊不完整」的稅務推理。

政府系統很少開源，更少見的是連推理引擎的設計細節都一併公開；IRS 的 Direct File 做到了這點，即便專案如今已經被封存。

🤔 **這個專案在解決什麼問題**

Direct File 讓美國納稅人可以免費、直接向 IRS 電子申報聯邦稅表，採訪談式介面設計，無論手機、平板還是桌機都能使用，並提供英語與西班牙語版本，設計上考量不同使用者的能力與近用需求。它把美國稅法（26 USC）轉譯成一般人看得懂的問答，答案再被轉換成標準稅表，透過 IRS 的 Modernized e-File（MeF）API 送出申報。

🧩 **核心架構：Fact Graph**

README 指出，Fact Graph 是一套 declarative（宣告式）、以 XML 為基礎的知識圖譜資料結構，設計用來處理不完整資訊，例如一份尚未填完的稅表。它用 Scala 撰寫，後端跑在 JVM 上，同一套程式碼再透過 Scala.js 轉譯成可在使用者端（瀏覽器）執行的版本，前後端共用同一套業務邏輯。README 特別提到 Fact Graph 並非稅務領域專屬，可作為其他「business rules engine」實作的參考案例。此外還有一個 State API，能把聯邦申報資料轉換成標準 MeF XML，以及額外補充欄位的 JSON 格式，讓第三方工具可以串接完成州或地方稅申報，不必重複輸入資料。

🧩 **怎麼跑起來、誰在維護**

README 指出可參考 ONBOARDING.md 在本機執行。但這個 repo 已被標記為 archived（封存），不再維護，程式碼僅供歷史參考，可能存在未修補或未知的漏洞，明確註明不應用於生產環境。另外，任何涉及個人識別資訊（PII）、聯邦稅務資訊（FTI）、敏感未分類資訊（SBU）或國家安全系統（NSS）的程式碼與資料，依法被排除在外，因此部分功能已被移除或改寫。

⚠️ **限制**

專案由 IRS 內部技術團隊主導開發，並有 USDS、GSA 支援，加上 TrussWorks、Coforma、ATI 等廠商協作完成；但由於已停止維護、敏感程式碼被抽離，實際可參考與重用的完整度有限。

🎯 **實務啟示**

對開發 regulatory、compliance 或任何需要處理「使用者資料尚未填完」情境的系統的工程師來說，Fact Graph 示範了一種做法：用同一套宣告式邏輯，透過 Scala.js 同時跑在 JVM 後端與瀏覽器前端，專門處理不完整資訊的推理問題。即使不碰稅務領域，這個架構思路也值得作為 business rules engine 設計的參考。

🔗 **來源**
- 標題：US IRS free online tax filing open source repo (2025)
- 作者/機構：accountinhn（Hacker News）／IRS-Public
- 連結：https://github.com/IRS-Public/direct-file

#OpenSource #Scala #GovTech #BusinessRulesEngine #KnowledgeGraph #IRS #DirectFile #ScalaJS #TaxTech #SoftwareArchitecture
