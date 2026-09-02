---
title: 'Anthropic Introduces Enterprise Frontier Safeguards (EFS): Zero-Data-Retention
  Privacy Plus Cross-Session Misuse Detection'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/02/anthropic-enterprise-frontier-safeguards-efs/
model: claude-code/sonnet
generated_at: '2026-09-02T10:26:20.516140'
score: 80
---

📌 【Anthropic 新架構】零資料保留與跨會話濫用偵測，真能兩者兼得？

TL;DR：Anthropic 推出 EFS，把濫用偵測所需的資料留在客戶自己的雲端，而非供應商手上，但目前尚未全面開放。

企業導入 LLM 時常卡在一個死結：受監管產業要求零資料保留（zero data retention, ZDR），任何 prompt 或 agent transcript 都不能留在供應商伺服器上；但資安團隊要做濫用偵測，過去的做法卻恰好需要供應商把同一批資料留存夠久才能做關聯分析。這週 Anthropic 公布的 Enterprise Frontier Safeguards（EFS），試圖同時滿足這兩個互斥的需求。

🤔 **偵測濫用為何非留資料不可**

Anthropic 表示，它觀察到的最複雜濫用行為往往橫跨多項任務、多個 session、甚至多個帳號，其中也包含被竊取或被濫用的企業憑證案例。如果每筆互動都送進分類器跑完就立刻丟棄，這種跨時間、跨帳號的攻擊模式根本抓不到，關聯分析需要一個時間窗。Anthropic 表示這個模式與其自身的間諜活動偵測工作中所記錄的情況一致。過去的問題是，即使受監管客戶認同這套安全邏輯，也無法在合規前提下採用，因為留存本身就違反 ZDR 要求。

🧩 **把「時間窗」搬到客戶自己手上**

EFS 的解法不是取消留存，而是把留存資料的位置換掉：監控資料存放在客戶自己控制的雲端基礎設施，而非 Anthropic 的伺服器；偵測邏輯仍由 Anthropic 負責，但資料的保管權、加密金鑰與人工審查則留在客戶手中。Anthropic 也強調，留存資料的目的是提升偵測品質，不是拿去訓練模型，並重申從未在未經明確授權下使用企業資料進行訓練；公司自 Claude Fable 5 起導入 30 天資料留存政策。

Anthropic 表示 EFS 的設計過程有超過 100 家客戶參與，橫跨金融服務、醫療、製造、電信、法律、零售與公部門，並與 AWS、Google Cloud、Microsoft Azure 共同合作。參與貢獻的還包括 Analysis and Resilience Center for Systemic Risk（成員涵蓋高盛、摩根士丹利、花旗、美國銀行、富國銀行的 CISO），以及 Comcast、KPMG、萬事達卡、Salesforce、Visa 等企業團隊。Anthropic 指出，這些設計討論涵蓋了四分之一的 Fortune 100 企業，以及美國每一家全球系統重要性銀行（G-SIB）。

📊 **與 Fable 5.1 同期釋出的另外兩項讓步**

EFS 是 Anthropic 隨 Claude Fable 5.1 與 Mythos 5.1 一起釋出的三項企業讓步之一，另外兩項是價格與精準度。Fable 5.1 把 cache read 成本砍了 75%，降到每百萬 token 0.25 美元，在一般工作負載下大約可省 25% 成本，高度 agentic 的工作負載甚至可省到約 45%。其資安防護機制在每個 Claude Code session 中的介入次數，也比 Fable 5 減少約 60%，部分原因是 Fable 5.1 被允許在不開發實際 exploit 的情況下識別軟體漏洞。

⚠️ **還沒真的能用**

EFS 目前尚未開放部署，將分階段推出，目標是今年秋天later達成廣泛可用，存取權需透過申請取得。在正式上線前，符合資格的客戶可以在 ZDR 模式下運行 Claude Fable 5 與 Fable 5.1。

🎯 **實務啟示**

對於卡在「要合規還是要資安」兩難的企業 AI 團隊，EFS 展示了一種思路：與其爭論該不該留存資料，不如重新設計資料留存的「歸屬權」——監控資料仍然存在，只是換了誰來保管。但在正式全面開放前，這仍是一個值得追蹤而非立即可依賴的方案。

🔗 **來源**
- 標題：Anthropic Introduces Enterprise Frontier Safeguards (EFS): Zero-Data-Retention Privacy Plus Cross-Session Misuse Detection
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/02/anthropic-enterprise-frontier-safeguards-efs/

#Anthropic #EnterpriseAI #DataPrivacy #AISecurity #ZeroDataRetention #ClaudeAI #ThreatDetection #AICompliance #CloudSecurity #LLMOps
