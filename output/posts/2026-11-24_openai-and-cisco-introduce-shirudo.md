---
title: OpenAI and Cisco introduce Shirudo
source: OpenAI Blog
url: https://openai.com/index/introducing-shirudo
model: claude-code/sonnet
generated_at: '2026-11-24T03:25:14.645500'
pinned: true
---

📌 OpenAI 攜手 Cisco 推出 Shirudo：不重啟也能擋下漏洞攻擊

TL;DR：OpenAI 與 Cisco 開源 Shirudo，用 eBPF 讓 Linux 系統在等待補丁期間也能即時擋下攻擊。

一個漏洞被公開後，測試與部署正式補丁往往要等上好幾天甚至好幾週。這段空窗期該怎麼辦？如果直接把有風險的功能整個關掉，很可能連帶擋掉所有合法請求，讓服務直接離線。這正是 OpenAI 和 Cisco 這次要解決的問題。

🤔 **補丁與攻擊之間的空窗期**

攻擊行為和合法請求有時會用到同一個 Linux operation，這讓防守變得棘手：擋得太寬，服務跟著掛掉；擋得太窄，漏洞還是能被利用。Shirudo（日文「盾」之意）就是為了處理這個取捨而設計的開源 runtime，讓安全團隊能在服務持續運行的狀態下，先測試一道「暫時防護」（shield）是否真的只擋住觸發漏洞的行為，而不影響正常流量，確認沒問題後再核准部署。

🧩 **用 eBPF 打造即時防護層**

Shirudo 的核心技術是 eBPF，一種可以讓小型程式在 Linux 作業系統內特定位置執行的技術，用來觀察可疑行為並套用針對性的防護。OpenAI 和 Cisco 將 Shirudo 設計為四項核心能力：

- **即時防護**：eBPF shield 能在不重啟系統的前提下封鎖有漏洞的程式碼路徑，團隊可以先觀察一個 shield 對應用程式的影響，再決定是否正式啟用。
- **機器速度的防禦**：agent 能取得可程式化的控制權，調查漏洞、研發針對性的 shield，並對照真實攻擊與實際工作負載驗證效果，但最終部署與否仍由安全團隊把關。
- **可信任的部署流程**：shield 在載入前必須經過加密簽署與驗證，Linux 的 eBPF verifier 會檢查程式是否符合安全規則，核心層的安全控制則限制未授權的變更。
- **硬體層級的驗證**：透過 Trusted Platform Module（TPM），系統會留下一份可驗證的防護載入或移除紀錄,讓操作者能確認系統是否符合自身的安全要求。

📊 **實測案例：擋下 Java4Shell，Elasticsearch 不用停機**

官方分享的一個案例是，團隊用 OpenAI 的 Codex 產生一個 shield，為 Java 的 Base64 解碼器加入輸入檢查，並直接掛載到一個正在運行的 Elasticsearch 程序上。當有人嘗試利用 Java4Shell 漏洞發起攻擊時，這個 shield 成功擋下惡意輸入，攻擊被阻止，Elasticsearch 整個過程中持續正常運作，沒有重啟。

💡 **為什麼選擇開源**

OpenAI 總裁暨共同創辦人 Greg Brockman 表示，發現漏洞不代表所有系統都能馬上修補，與 Cisco 合作推出 Shirudo 是為了在補丁完成前先保護好必須持續運行的系統；因為這麼多團隊用的是同一套軟體，把這類工具公開開發是合理的做法，一個團隊找到更好的防護方式,其他團隊就不用從零開始。Shirudo 以 BSD 2-Clause 授權開源，其中的 BPF 程式則採 BSD 與 GPL 雙重授權。官方的規劃是，未來能讓經過測試的 shield 與漏洞揭露同步發布,讓操作者在準備永久補丁的同時,就有臨時防護可用。

⚠️ **目前只是第一步**

OpenAI 與 Cisco 也坦言 Shirudo 是邁向「能動態應對新興威脅、同時維持可靠性」基礎設施的第一步。後續要持續強化的方向還包括：強化核心與核心服務、限制工作負載的權限範圍、讓更新與復原流程更安全，以及結合前沿 AI 與安全/基礎設施研究,持續發現漏洞並驗證防禦效果。換句話說,現階段的 Shirudo 還是一套需要持續擴充的雛型,而不是一次性的終局方案。

🎯 **實務啟示**

對維運 Linux 服務的工程師與資安團隊來說,Shirudo 提供了一條「補丁之前先頂住」的新路徑。想上手的話,可以照著官方的 VM quickstart 練習簽署、載入並驗證一個測試防護,或透過 Isovalent 的自學實驗室動手操作,12 月 15 日官方也會舉辦技術深度解析的線上研討會。專案程式碼與文件已在 GitHub 上公開,歡迎貢獻新的 shield 或改善 runtime 本身。

🔗 **來源**
- 標題：OpenAI and Cisco introduce Shirudo
- 作者／機構：OpenAI
- 連結：https://openai.com/index/introducing-shirudo

#Shirudo #OpenAI #Cisco #eBPF #LinuxSecurity #OpenSource #Codex #CyberSecurity #InfrastructureSecurity #VulnerabilityManagement
