---
title: An update on independent evaluators
source: Anthropic News
url: https://www.anthropic.com/news/an-update-on-independent-evaluators
model: claude-code/sonnet
generated_at: '2026-10-15T20:27:54.049433'
pinned: true
---

📌 Anthropic 讓 METR 員工「常駐內部」，審查自家風險決策

TL;DR：Anthropic 開放 METR 團隊享有近似員工的內部存取權限，建立三層級第三方評估框架，公開監督自家前沿模型風險。

一家開發前沿 AI 模型的公司，願意讓外部非營利組織的員工拿到和自己風險評估團隊同等的硬體、辦公空間與內部系統存取權，這聽起來像是公司治理裡少見的讓步，但 Anthropic 認為，這正是建立可信安全監督的必要一步。

🤔 **問題：想公開透明，卻不能公開一切**

隨著模型能力提升，所需的安全防護與風險評估也越來越複雜。Anthropic 表示，他們想對自己做出的決策負起公開責任，但部分資訊涉及可能被惡意利用的細節，或屬於商業機密（例如算力與訓練資訊），無法直接全文公開。上個月，Anthropic 已承諾加強獨立第三方評估，並簽署了白宮「超級智慧協議」（White House Accord on Super Intelligence），承諾與獨立外部稽核者或評估者合作。

🧩 **解法：把評估者「請進門」，而非只給報告**

Anthropic 的做法是讓第三方評估者深入取得內部資訊，由評估者自行提出證據與推論結論，而不是公司自行摘要後對外公布。文中將此類比為銀行監理制度，銀行比監理機關更了解自身風險部位，因此監理機關會派駐常駐稽核員進駐大型銀行，及早發現可能危及公眾的風險行為。

Anthropic 目前建立了三層級的評估者存取框架：

| 層級 | 代表夥伴 | 存取範圍 | 發布權限 |
|---|---|---|---|
| 第一層 | SecureBio | 範圍明確界定的風險調查，存取範圍由 Anthropic 決定 | 需經 Anthropic 核准才能發布 |
| 第二層 | （推進中的夥伴關係） | 可取得更多資訊，但特定類別仍可被要求刪節 | 不需核准即可發布，並可公開評論刪節是否合理 |
| 第三層 | METR | 員工等級存取：公司硬體、辦公空間、內部工具權限，大致與 Anthropic 自身風險評估團隊相當 | 發布不受公司否決，僅限預先定義的窄類別資訊需刪節 |

目前已有 6 名 METR 員工以此模式進駐 Anthropic，過去一年雙方已針對 Anthropic 的風險報告（Risk Reports）進行過多次審查合作。SecureBio 則處於第一層，正在審查 Anthropic 八月風險報告中的化學與生物武器章節，此前已完成並公開了一份前期風險報告的試點審查。Anthropic 也正與 Accenture 與 Faculty 推進包含紅隊測試、對齊評估、安全防護測試等範圍更廣的合作，並與包括 Hugging Face 在內的多個組織進行早期接觸。

⚠️ **仍有邊界：哪些資訊不會分享**

即便是「員工等級存取」的 METR，仍有少數類別資訊被排除在外，例如客戶資料、律師與客戶間的特權資訊，以及模型架構資訊。文中特別說明，架構資訊外洩風險高，但對風險評估的相關性通常較低，若確實高度相關，Anthropic 會尋求分享，但需要額外的內部核准。

💡 **深入看：評估者能公開，但不是毫無限制**

這套機制的關鍵設計在於「發布權」：METR 可以自行決定公開其風險評估結果與結論，Anthropic 無法否決其發布，只能要求針對少數預先定義類別的資訊進行刪節；而 METR 也有權公開評論這些刪節是否合理，只是不能揭露被刪節的內容本身。這種「有限否決權加上透明評論權」的設計，試圖在保護敏感資訊與維持第三方公信力之間取得平衡。

🎯 **實務啟示**

對從事 AI 安全評估、紅隊測試或模型風險治理的團隊而言，這套三層級框架提供了一個可參考的漸進式模型：從範圍限定的審查開始累積互信，逐步擴大存取範圍與發布自主權，而不是一步到位要求完全透明。對關注前沿模型治理的工程師來說，值得持續關注 METR 未來公開的風險評估報告內容。

🔗 **來源**
- 標題：An update on independent evaluators
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/news/an-update-on-independent-evaluators

#Anthropic #METR #AISafety #ModelEvaluation #AIGovernance #RedTeaming #FrontierAI #RiskAssessment #ThirdPartyAudit #ResponsibleAI
