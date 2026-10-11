---
title: OrcaRouter Releases OrcaCyber Zero 1.5 Cybersecurity Model With 1M Context
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/10/orcarouter-releases-orcacyber-zero-1-5-cybersecurity-model-with-1m-context/
model: claude-code/sonnet
generated_at: '2026-10-11T21:06:36.242870'
score: 83
---

📌 OrcaCyber Zero 1.5：百萬 context 滲透測試模型上線

TL;DR：OrcaRouter 推出資安模型新版，主打漏洞複現與滲透測試，但效能數據全為廠商自報。

一款宣稱能自動複現 CVE、開發 exploit 的語言模型，聽起來像是資安界的噩夢，還是解方？端看是誰在用。

🤔 從 Zero 1.0 到 1.5，鎖定授權資安研究

OrcaRouter 於 2026 年 10 月 10 日發布 OrcaCyber Zero 1.5，接替今年 9 月 17 日上線的 OrcaCyber Zero 1.0。官方表示這是一款針對資安研究與授權資安工程進行 post-training 的模型，列出的用途包括漏洞複現（vulnerability reproduction）、exploit 開發、滲透測試、資安稽核與 cyber reasoning。模型本身具備 1M token 的 context window，並支援 native function calling 與結構化輸出（structured outputs）。

📊 四項廠商自報測試：Cybench、CVE-Bench、SWE-bench Pro V2

模型頁面列出 4 項「廠商自報」成績，最後更新時間為 2026 年 10 月 10 日：

- Cybench：涵蓋 40 道專業 CTF 題目，Orca 的 100% 成績實際涵蓋其中 39 題。
- CVE-Bench：基於 40 個 critical-severity 的 web CVE 建構，Orca 的 95.8% 涵蓋可評估的 24 題子集。
- SWE-bench Pro V2：官方特別註明此分數「不能直接與標準 SWE-bench Pro 的結果比較」。

值得留意的是，所有競品數據同樣來自各自廠商的自行公告，沒有任何一項經過獨立複現驗證。

🧩 OpenAI 相容 API，但存取被鎖在「資安研究」層級

開發者可將 base_url 設為 https://api.orcarouter.ai/v1，呼叫 orca/orcacyber-zero-1.5 使用模型，介面與 OpenAI API 相容。不過存取權限被限制在 Security Research tier，官方要求申請者提供 engagement（委託證明）、passkey 與簽署同意條款，目標族群鎖定受信任的資安研究者、紅隊與授權測試人員。

計價方面，輸入每 1M tokens 為 3 美元，輸出每 1M tokens 為 7.5 美元，cache read 則是每 1M tokens 0.75 美元。延遲數據顯示過去 7 天 p50 time-to-first-token 為 500 毫秒，p95 為 2.36 秒，但官方也坦承這個樣本只涵蓋 1.3K tokens 的流量，樣本量偏小；相較之下，Zero 1.0 在更大流量視窗下記錄的 p50 為 3.43 秒，兩者並非同等條件下的乾淨比較。

💡 延續性 post-training，而非架構創新

從公開資訊看，OrcaCyber Zero 1.5 更像是既有 Orca 模型線的 post-training 升級，鎖定垂直場景（漏洞複現、exploit 開發），而非全新的模型架構。其賣點在於把 context window 拉到 1M token，搭配 function calling 與結構化輸出，讓自動化的漏洞驗證與報告產出流程更順暢。對資安團隊而言，官方給出的訴求很直白：減少無效報告，提高驗證過與修復過的漏洞比例。

⚠️ 數字都來自廠商自己，無獨立覆核

所有列出的 benchmark 成績，包括 Cybench、CVE-Bench 與競品對比數字，都只是官方自行公布，沒有第三方重現。延遲比較也因樣本量與流量視窗不同而難以一對一對照。在採信這些宣稱前，仍需要獨立測試或第三方稽核佐證。

🎯 給資安團隊的實務提醒

若考慮導入此類模型進行授權滲透測試，建議先以內部 CVE 或已知弱點做小規模驗證，而非直接信任官方公布的百分比；同時留意存取權限審核流程（engagement、passkey、條款同意）可能拉長導入時間。

🔗 來源
- 標題：OrcaRouter Releases OrcaCyber Zero 1.5 Cybersecurity Model With 1M Context
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/10/orcarouter-releases-orcacyber-zero-1-5-cybersecurity-model-with-1m-context/

#AI #Cybersecurity #LLM #PenetrationTesting #CVE #VulnerabilityResearch #RedTeam #AISecurity #ExploitDevelopment #CTF
