---
title: Introducing the Life Sciences Verification Program
source: Anthropic News
url: https://www.anthropic.com/news/life-sciences-verification-program
model: claude-code/sonnet
generated_at: '2026-09-17T20:26:06.520829'
pinned: true
---

📌 【Anthropic】生命科學驗證計畫上線，讓 Claude 敢碰「敏感」的生物研究題目

TL;DR：Anthropic 推出 Life Sciences Verification Program，讓經驗證的機構取得更寬鬆的生物研究存取權限。

一款通用 AI 助手要在藥物開發、病原體研究這類生物領域派上用場，往往會先撞上自家的安全防護機制。Anthropic 這次選擇用「驗證身分」換取「更寬鬆權限」的方式，試著解開這個兩難。

🤔 通用安全防護，擋住了合法的生物研究

Anthropic 表示，旗下對外開放的 Fable 模型目前會封鎖不少生物科學相關的任務，涵蓋藥物開發、研究型生物學、臨床開發與製造等領域。問題在於，很多情況下很難單純從一個請求本身判斷使用者究竟是在做正當研究（例如研究病毒病原體以開發疫苗），還是意圖造成傷害（例如試圖提高病毒傳播力）。Anthropic 在最近的威脅報告中也指出，平臺上已出現愈來愈多可能協助生物武器開發的複雜濫用嘗試。

🧩 兩種授權：日常工作用 Standard，敏感專案用 High-risk

Life Sciences Verification Program（LSVP）要求申請機構先通過涵蓋研究資歷、安全標準與倫理研究監督的驗證流程，之後可以申請兩種授權：

- Standard Use：適用於多數生物研究與開發工作流程，可授予整個團隊做多元的日常工作，每年更新一次。目前適用於 Mythos 5.1、Opus 5、Sonnet 5，並將延伸到未來的模型，分類器針對科學任務調整得更寬鬆。
- High-risk Use：針對在 Standard Use 下仍被封鎖、風險較高的工作，會移除所有生物科學相關的封鎖限制。這類授權只對應單一研究專案，每六個月要重新申請，目前開放給 Opus 5 與 Sonnet 5，Mythos 的高風險授權則仍侷限於少數經過額外審核的機構，Anthropic 表示正與美國政府合作擴大適用範圍。

這些授權可以透過 Claude Science、Claude.ai、Claude Code 與 API 等所有產品介面使用。

💡 從即時攔截改成離線監控，抓的是「行為模式」

Anthropic 點出三種特別擔心的威脅情境：帳號或存取權被惡意軟體劫持、內部人員或被脅迫的員工惡意濫用權限，以及 AI agent 在長流程或群體協作中做出未預期的危險行為。因為嚴重的濫用行為往往被拆分成看似無關的多次請求與 session 以規避偵測，LSVP 把防護機制從「每個請求即時攔截」轉為「離線監控行為模式」，讓合法工作能更少被打斷，但也代表 Anthropic 需要保留被標記活動的相關資料以供審查。

為此，LSVP 流量會保留 30 天資料以進行監控，這些資料會被嚴格隔離，不會用於模型訓練，也不會被 Anthropic 內部生命科學研究團隊存取。每個機構的存取範圍會綁定其申請時所述的用途，一旦偵測到超出範圍的使用模式，Anthropic 會通知機構管理員，在事先約定的時限內處理與補救。其他防護機制，例如網路資安相關的分類器，則維持不變。

📊 已有數十家機構搶先加入

Anthropic 表示已透過早期存取計畫讓數十家機構加入 LSVP，並預期在開放申請的第一週內就會有數百家機構送件，未來幾週會進一步擴大到服務多數生命科學社群。來自 Xaira、Edison、Manifold Bio 等機構的研究者也表達了對這項計畫的期待，希望能把 Anthropic 的前沿模型用於藥物發現引擎等工作。

🎯 實務啟示

對在藥廠、生技新創或學術實驗室裡建構 AI 應用的工程團隊而言，LSVP 提供了一條「不必完全繞過安全機制」也能取得更高權限的路徑，但代價是機構得先通過驗證、承擔起監督自身用途範圍的責任。若你的團隊手上有原本被生成式 AI 安全機制擋下的生物研究工作流程，這類驗證計畫值得列入評估。

🔗 來源
- 標題：Introducing the Life Sciences Verification Program
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/news/life-sciences-verification-program

#Anthropic #Claude #LifeSciences #DrugDiscovery #AIsafety #Biosecurity #Bioinformatics #EnterpriseAI #ResponsibleAI #AIforScience
