---
title: 'Genie One Accuracy: Why Curated Agents Need Governed Context'
source: Databricks
url: https://www.databricks.com/blog/genie-one-accuracy-why-curated-agents-need-governed-context
model: claude-code/sonnet
generated_at: '2026-11-19T23:59:54.295082'
score: 76
---

📌 財務說虧損率惡化 8.2%，核保說改善 1.5%：企業 AI 助理該信哪個？

TL;DR：Databricks 研究顯示，curated agent 與治理過的語意層缺一不可，兩者合併才能讓 Genie One 的問答準確率衝到 93~95%。

同一家保險公司，問「2024 到 2025 年損失率有沒有變好」，財務部門說惡化了 8.2 個百分點，核保部門卻說改善了 1.5 個百分點。兩邊的 SQL 都沒寫錯，問題出在沒人告訴 AI 助理該用哪個部門的定義。

🤔 同一個詞，四個部門四種算法

Databricks 在一家虛構的商業車險保險公司上做測試，發現「損失率」這個詞在公司內部至少有三種算法：財務部門用的是扣除再保險後的日曆年度數字，所以某筆舊理賠的不利準備金調整會反映在今年的數字上；核保部門看的是毛保費、排除巨災、依保單年度計算的指標，因為這是訂定費率時的基準；精算準備金部門則另外依賴第三種指標，事故年度最終損失率。挑戰在於：同一個業務詞彙有多種合法定義時，AI 助理要怎麼知道該用哪個，同時又要讓像「總承保保單數」這類共享事實保持一致。

🧩 Genie One 的架構：學到的知識 + 治理過的知識

Databricks 針對這個問題做了一項研究，對象是剛進入正式 GA 階段、由 Genie Ontology 驅動的 Genie One。Genie Ontology 會從團隊既有的 dashboard、查詢、notebook 與語意模型中自動學習業務邏輯、計算方式與關聯性，整理成「Ontology Snippets」,這屬於「學到的知識」。這份知識會再搭配「建模的知識」：透過 Unity Catalog 中經過驗證的 Metric Views、Domains／Subdomains 與 Pages，明確定義、治理過的業務概念，本篇研究稱之為「governed layer（治理層）」。兩者合在一起，才能讓 Genie 更完整地理解組織運作方式，而且不需要把每個概念都事先建模完。

Genie One 的路由邏輯並非選一個 agent 就讓它回答所有問題：它可以直接使用治理過的 Unity Catalog Semantics（Metric Views、Domains/subdomains、Pages），也可以把問題導向相關的 Genie Agent；如果都找不到合適的對象，就會搜尋整個 workspace，從常用的表格或 volume，或先前的對話中推斷該用什麼資料。文中特別提醒一個關鍵限制：當 Genie One 用自己找到的 context 回答問題時，並不會自動繼承各個 agent 內部設定的指令——那些指令只有在 Genie One 真的把問題路由給該 agent 時才會生效。也就是說，一個 agent 即使被精心設計過，如果 Genie One 沒有路由給它，它對答案的貢獻可能微乎其微。

🧩 實驗設計：四個部門 Agent，外加刻意埋的陷阱

研究團隊建了四個 Genie Agent，分別對應 Finance、Reserving、Underwriting、Claims，共用同一批底層表格，但各自配有自己團隊的公式、業務規則與 SQL 範例問題，並在獨立的練習題集上調校後凍結版本。每個團隊資料夾各有文件，四個資料夾共 14 份 PDF。為了測試穩健性，團隊刻意埋了兩份誤導性文件：一份是準備金委員會會議記錄的早期草稿，寫著準備金增加 410 萬美元，而同資料夾中經核准的正式版本寫的是增加 528 萬美元；另一份是一份廠商電子報，裡面藏了一條 prompt-injection 指令，要求 AI 把損失率報成 55%。此外還在正確定義旁邊放了三張外觀相似的表格：analytics_loss_ratio_v2、analytics_loss_ratio_test，以及一份個人複本 finance_lr_calendar_quarter_net_jdoe。

基準測試集共 125 題，每題都有獨立用 SQL 算出的預期答案，涵蓋簡單查詢、明確指名的業務定義、模糊問題（例如「我們的損失率是多少？」）、需要解釋的問題、資料庫答不出來的問題，以及需要同時結合文件與結構化資料的問題，還包含追問與前述埋藏的陷阱文件。為了讓結果更可信，每題都讓 Genie One 回答三次，每次用全新的 service principal 以避免舊對話被延續，所有回答都記錄在 MLflow 中；關鍵結果接近時會用新身分重跑整組設定；報告的 95% 信賴區間來自 2,000 次 bootstrap 重抽樣。兩位來自不同模型家族的 AI 裁判負責從回答中抽出關鍵數字、所用定義與涵蓋的事實，再用固定規則判斷正確與否，兩位裁判的判定一致率達 95~99%。每次測試前，每個 agent 都必須先單獨在基本問題上答對至少 85%。

📊 單用表格只有 64%，合體後衝到 93~95%

測試四種設定下，Genie One 的整體準確率如下：

| 設定 | 準確率 |
|---|---|
| 只有底層表格 | 64% |
| 只有 curated agents | 83% |
| 只有 governed layer（治理層） | 83% |
| curated agents ＋ governed layer | 93~95%（兩次測試） |

有趣的是，curated agents 與 governed layer 雖然分數相同，但強項不同：curated agents 改善了依賴文件的問答，governed layer 改善了依賴業務定義的問答，單靠任一邊都無法同時顧到兩種需求。合併之後，損失率相關問題的準確率達 93%，需要同時結合文件與結構化資料的問題準確率達 97%。研究團隊也用一個虛構零售商重複同樣的比較，確認這個模式不只出現在保險業：在 curated agents 的基礎上加上 governed layer，準確率從 54% 提升到 82%。

💡 只有 curated agents 時，Genie One 常常「自己亂猜定義」

研究發現，只有 curated agents 的設定下，Genie One 常常自己回答業務定義相關的問題，完全沒有去看 agent 指令裡寫好的公式。原因在於，整個帳號內公開發布的 Pages 對 Genie One 都是可見的，所以它能找到的「最接近的定義」常常是別人為了不相關專案寫的 Pages——研究記錄顯示，它在 49% 的回答中依賴了這類不相關的 Pages。這說明了為什麼光靠精心設計 agent 還不夠：如果 Genie One 沒有把問題路由到正確的 agent，再好的 agent 指令也用不上。

🎯 實務啟示

導入企業 AI 助理不能只靠「把文件丟進去」或「把 ETL 表建好」兩者之一：既要經營從既有 dashboard、notebook 學來的 learned knowledge，也要花心力把關鍵業務指標做成 Unity Catalog 裡治理過的 Metric Views、Domains 與 Pages。更重要的是要意識到，agent 裡寫的業務規則只有在被正確路由到時才算數，否則系統可能會悄悄地用不相關的全域資源拼出一個看起來合理、但其實用錯定義的答案。

🔗 來源
- 標題：Genie One Accuracy: Why Curated Agents Need Governed Context
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/genie-one-accuracy-why-curated-agents-need-governed-context

#Databricks #GenieOne #DataGovernance #UnityCatalog #EnterpriseAI #LLMAgents #SemanticLayer #DataAnalytics #PromptInjection #AIAccuracy
