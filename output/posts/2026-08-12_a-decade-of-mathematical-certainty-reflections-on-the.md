---
title: 'A decade of mathematical certainty: Reflections on the Automated Reasoning
  Group'
source: Amazon Science
url: https://www.amazon.science/blog/a-decade-of-mathematical-certainty-reflections-on-the-automated-reasoning-group
model: claude-code/sonnet
generated_at: '2026-08-12T07:29:35.279161'
score: 105
---

📌 十年之後:Amazon 如何用數學證明取代「測試」保障 AWS 安全

TL;DR:AWS Automated Reasoning Group 十年來把形式驗證做成日處理數十億次查詢的正式服務。

多數團隊靠測試案例找出系統的漏洞,但測試永遠只能覆蓋「想得到的情境」。2016 年,一支叫做 Automated Reasoning Group(ARG)的 Amazon 研究團隊喊出更大膽的目標:不是測試 AWS 系統對不對,而是用數學邏輯證明它一定對。十年後,這支團隊的成果已經是數十億次日常查詢背後的基礎設施。

🤔 **從一場 Demo Day 到日常基礎設施**

2016 年 ARG 第一次對 AWS Security 團隊辦 Demo Day,展示的幾個專案,如今都已經是 2026 年 AWS 內部與客戶端仍在倚賴的系統。Sean McLaughlin 當時介紹了一個叫 Tiros 的工具,用來自動回答關於虛擬私有雲(VPC)網路的問題,協助辨識設定錯誤或安全漏洞。同一天展示的深度自動化分析基礎設施專案,後來發展成證明 TLS 交握與加密、儲存、虛擬化程式碼正確性的工作。

🧩 **從研究原型長成客戶天天在用的服務**

Tiros 後來成為 Amazon Inspector 網路安全分析功能的基礎,目前也是 Reachability Analyzer 背後的引擎,並在 AWS 內部用來自動化合規認證與安全不變量的檢查。Tiros 的研究後來又獨立出一個新專案 Zelkova,專門用自動化推理分析政策(policy)以及政策未來可能造成的後果。Zelkova 目前是 S3 Block Public Access、IAM Access Analyzer 等多個工具的核心引擎。

IAM Access Analyzer 讓 USAA、GoTo 這類客戶不用再「祈禱」自己的安全政策設定正確,而是能拿到政策實際允許什麼的數學證明。Reachability Analyzer 不必真的送出封包,就能透過數學方式分析所有可能的網路路徑,回答目的地是否可達、若不可達是被哪個元件擋下。Amazon Bedrock Guardrails with Automated Reasoning checks 則把這套方法帶進生成式 AI,用形式邏輯驗證模型回應是否符合既定政策,協助降低幻覺,驗證準確率最高可達 99%。這些服務共用同一套底層技術:satisfiability modulo theories(SMT)求解器與其他自動化推理技術,提供遠超傳統測試能做到的正確性保證。

📊 **證明雲端最核心的基礎設施**

除了面向客戶的工具,ARG 也把心力放在 AWS 內部最核心、卻要求絕對正確的基礎設施上,包括 AWS Nitro Isolation Engine、s2n-bignum 這類加密實作、資料中心的開機程式碼,以及 S3 等儲存系統的正確性證明。其中一個規模最大的專案,是團隊證明並無縫替換了處理每秒十億次 API 呼叫的整套授權引擎:團隊撰寫規格與證明,並用數量級達「千萬億」(quadrillions)筆的正式生產授權紀錄驗證新引擎。

隨著 Lean 這類證明輔助工具興起(Lean 由團隊資深首席科學家 Leo de Moura 開發),團隊也開始把語言模型和證明工具結合,為更大、更多的系統尋找證明,近期公布的 Nitro Confidentiality Engine 證明、AWS 政策解譯器證明,以及加密基礎的正確性證明都是這個方向的成果。

💡 **意外的發現:證明正確,反而讓系統更好維護**

團隊十年來最意外的發現,是形式驗證不只讓系統更安全,往往還讓系統更有效率、更容易維護。當團隊必須為驗證撰寫精確規格時,常常會因此發現更簡單、更優雅的解法。這是因為自動化推理採取的是系統化取徑:與其驗證系統在特定情境下的行為,不如直接定義系統應該如何運作、找出達成該行為的必要條件,再用數學證明驗證這些條件成立,等於驗證系統本身是正確的。這個發現印證了團隊的信念:數學的嚴謹與務實的工程並不衝突,反而互補。

🎯 **對工程師的啟示:自動化推理正在成為 Agentic AI 的地基**

ARG 過去十年在分散式系統與關鍵程式碼驗證上累積的方法論,現在直接應用到驗證 AI 生成程式碼的正確性;而在 AWS 政策與 VPC 網路誤設方面的研究,也延伸為驗證 AI 生成內容正確性的基礎。Amazon Bedrock Guardrails with Automated Reasoning checks 把原本需要深厚專業知識才能操作的工具,變成內建在日常服務中的能力;Amazon Bedrock AgentCore 中的 Policy 功能,則用自動化推理為自主運作的 agent 劃出明確的合規邊界。對正在打造 agent 系統的工程師而言,這代表「形式驗證」正從研究圈的專門技術,逐漸變成保護自主系統行為邊界的標準工具之一。

🔗 **來源**
- 標題:A decade of mathematical certainty: Reflections on the Automated Reasoning Group
- 作者／機構:Amazon
- 連結:https://www.amazon.science/blog/a-decade-of-mathematical-certainty-reflections-on-the-automated-reasoning-group

#AWS #AutomatedReasoning #FormalVerification #Amazon #CloudSecurity #SMTSolver #IAMAccessAnalyzer #AgenticAI #BedrockGuardrails #Lean
