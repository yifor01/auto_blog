---
title: Developing Enterprise Frontier Safeguards with our customers
source: Anthropic News
url: https://www.anthropic.com/news/enterprise-frontier-safeguards
model: claude-code/sonnet
generated_at: '2026-09-02T10:02:01.685719'
pinned: true
---

📌 Anthropic推出EFS：資料留在企業自己的雲端，還能抓惡意行為

TL;DR：Anthropic發表Enterprise Frontier Safeguards，讓企業在保有零資料保留隱私的同時，仍能監控跨時段的惡意濫用。

一邊是監管產業對資料主權的堅持，一邊是偵測複雜濫用行為所需的跨時段資料關聯，這兩件事過去被視為魚與熊掌難以兼得。Anthropic這次的解法，是把「誰存資料」和「誰做偵測」這兩件事拆開來看。

🤔 **問題出在哪：偵測濫用需要時間跨度，但客戶要的是零保留**

Anthropic在文中指出，隨著Mythos等級模型（例如Claude Fable 5.1）帶來智慧與agentic能力的大幅提升，濫用與自主性偏差行為的風險也隨之升高。過去幾個月，Anthropic觀察到大量嘗試濫用AI模型的證據，範圍從一般詐騙到複雜的網路攻擊，甚至包括agent自主進行破壞性行為，部分案例涉及企業客戶憑證遭竊或誤用。這類複雜濫用往往橫跨多個工作階段與帳號，單獨分析每次互動、事後立即銷毀資料的做法並不足以偵測出來,因此有效偵測需要在一段有意義的時間內保留資料，以便跨時間、跨帳號進行關聯分析。這正是Anthropic從Fable 5開始導入30天資料保留政策的原因——Anthropic強調此舉並非為了訓練模型，公司從未在未經明確許可下使用企業資料訓練，未來也不會。但對許多受監管產業的企業客戶來說，資料保留本身就難以採用。

🧩 **EFS怎麼運作：資料留在客戶自己的雲端**

Enterprise Frontier Safeguards（EFS）的核心設計，是把用於監控的活動資料儲存在客戶自己控制的雲端基礎設施中，而非Anthropic端。客戶可以將這些資料放在自己的Amazon S3、Azure Blob Storage或Google Cloud Storage帳戶內，並套用自己的加密金鑰、存取政策與稽核紀錄。EFS採用自動化安全監控，不需要Anthropic員工進行人工審查；自動化系統會分析一段滾動時間窗內的流量，找出嚴重濫用的訊號，包括嘗試開發攻擊性網路或生物能力、以及憑證遭竊或外洩的跡象，一旦偵測到異常模式，訊號會直接送給客戶，由客戶自己已受過訓練、具備權限的人員判斷是否為真實濫用或誤判——這一點對於處理法律特權資料、非公開資訊、藥物安全報告等高度敏感內容的企業尤其重要。

EFS將分階段推出給客戶，預計從今年秋天稍晚開始。為了讓過渡更平順，符合資格的客戶在EFS準備就緒前，可以在Fable 5與Fable 5.1上先使用零資料保留（ZDR）。這項功能將支援Claude Code、Claude Enterprise、Claude Platform、Amazon Bedrock、AWS上的Claude Platform、Google的Agent Platform，以及Microsoft Foundry。

💡 **超過100家企業與三大雲端夥伴共同打造**

Anthropic表示EFS是與100多家客戶密切合作開發的，涵蓋金融服務、醫療、製造、電信、法律、零售與公部門，並與Amazon Web Services、Google Cloud、Microsoft Azure等雲端夥伴共同規劃。參與討論的組織包括Analysis and Resilience Center for Systemic Risk（ARC，成員涵蓋高盛、摩根士丹利、花旗、美國銀行、富國銀行等美國大型銀行的資安長），以及Comcast、KPMG、Mastercard、Salesforce、Visa等企業領袖。文中提到，相關對話涵蓋了四分之一的Fortune 100企業、美國每一家全球系統性重要銀行，以及幾乎所有受監管產業。文中一位客戶合作夥伴也提到，這次合作是在架構層級、而不只是政策層級，共同打造新的安全與隱私能力。

🎯 **實務啟示**

對於在受監管產業中評估Claude的團隊，EFS等於提供了一條「資料不出自家雲端、仍能享有frontier模型監控能力」的路徑，值得留意秋季開始的分階段開放時程，並提前確認自家雲端帳戶（AWS S3 / Azure Blob / GCS）的權限與稽核架構是否已準備就緒。若目前正卡在資料保留政策而無法導入Fable系列模型，過渡期的ZDR選項也值得先行申請評估。

🔗 **來源**
- 標題：Developing Enterprise Frontier Safeguards with our customers
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/news/enterprise-frontier-safeguards

#Anthropic #Claude #EnterpriseAI #DataPrivacy #AISecurity #ZeroDataRetention #CloudSecurity #AIgovernance #FinancialServices #EnterpriseFrontierSafeguards
