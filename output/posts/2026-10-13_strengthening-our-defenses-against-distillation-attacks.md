---
title: Strengthening our defenses against distillation attacks
source: Anthropic Research
url: https://www.anthropic.com/research/distillation-defenses
model: claude-code/sonnet
generated_at: '2026-10-13T21:58:59.579792'
pinned: true
---

📌 【Anthropic 研究】蒸餾攻擊猖獗，Claude 如何把資料洩漏砍掉九成

TL;DR：Anthropic 揭露新一代反蒸餾防禦，初步數據顯示可讓攻擊者擷取的資料量減少約 90% 到 99%。

當一家公司只要透過網路爬取另一家模型的回應，就能用幾分之一的時間與成本做出逼近前沿能力的模型，安全防護的意義就變了。Anthropic 這篇研究，講的正是這場看不見的資料戰爭。

🤔 **蒸餾攻擊，為何讓 Anthropic 如此在意**

蒸餾攻擊（distillation attack）是一種隱密、工業規模的行動：攻擊者向目標模型（此處為 Claude）大量發送請求，取得回應後訓練自家較小模型模仿其行為，且未經原開發者授權，往往透過大量詐欺帳號網路進行。Anthropic 指出兩個擔憂：第一，被蒸餾出來的模型可能逼近前沿能力，卻沒有相應完善的安全防護，可能在生物與資安等領域造成重大危害；第二，這類模型正被整合進外國軍事、情報與監控系統。

報告舉例，Zhipu 在開發 GLM-5.3 時曾嘗試蒸餾 Claude Fable 5 的資安能力，但發現 Claude 的資安防護讓其攻擊效果下降後，轉而蒸餾舊版 Claude 模型與另一家實驗室的模型。美國 Center for Advancing Innovation and Standards for Super Intelligence（CAISSI）其後評估 GLM-5.3 為目前已發布開放權重模型中資安能力最強者，Anthropic 自家研究也發現 GLM-5.3 的防護很容易被繞過，且該模型願意從頭到尾開發完整的安全漏洞攻擊手法。另一個案例中，Moonshot 的 Kimi 模型曾被發現將使用者請求偷偷轉發給 Claude 以進行蒸餾，其中一名疑似與中國人民解放軍有關聯的使用者，曾要求分析某特定人士的監視器監控畫面。

🧩 **從「摘要思維鏈」到「鎖死推理去向」**

Anthropic 的防禦幾乎都圍繞著一件事：讓 Claude 的推理過程（即回答前寫出的思考內容）變得難以被擷取，因為這段內容比最終輸出本身對蒸餾者更有價值。最初的做法是在展示給使用者前，先讓 Claude 自行摘要推理內容。但攻擊者隨即從被動蒸餾（單純爬取回應）轉向主動誘導，想方設法讓 Claude 吐出完整原始推理，手法從直接要求「逐字輸出你先前的推理」，到某實驗室一次測試 12,000 種不同誘導請求不等。

隨著防禦升級，攻擊者也擴大規模，建立同時操控超過 20,000 個詐欺帳號的代理網路，躲避單一帳號被封鎖的風險，甚至在 Claude 未開放的地區轉售存取權限。為應對這種持久且不斷進化的攻擊，Anthropic 推出三層新防禦：控制推理內容的流向（例如 Claude Fable 5.1 與 Claude Opus 5.5 引入的「preserved thinking」，禁止 2026 年 8 月 31 日後新建的 API 帳號編輯 Claude 先前的上下文，並限制較弱防護的舊模型讀取新模型的推理，Claude Sonnet 5.5 更進一步讓推理紀錄只對產生該請求的組織可見）、封鎖並修補擷取嘗試，以及持續摘要推理內容。

📊 **一組對照數字：完整推理 vs 摘要推理**

Anthropic 用 SWE-bench Verified 基準測試驗證摘要推理的效果：用 Claude Opus 4.8 的完整推理紀錄訓練出的蒸餾模型，得分 80.4%；只用摘要過的推理紀錄訓練，得分降到 71.8%。這顯示摘要推理確實能大幅降低蒸餾資料的價值。結合上述三層防禦後，早期數據顯示蒸餾者能擷取的資料量減少了約 90% 到 99%。

⚠️ **這些防禦不是沒有代價**

Anthropic 坦言，為了擋下蒸餾攻擊，已經婉拒了金額可觀的營收與數兆 token 的付費流量，研究與產品團隊也投入大量時間，部分變更還要求正常使用者調整自己的整合方式。報告強調蒸餾是每個模型開發者都會面臨的共同問題，分享這些方法是希望業界能更理解其中的取捨，以及為何這些成本值得承擔。

🎯 **實務啟示**

對建置在 LLM API 之上的團隊而言，若產品設計中出現「要求模型逐字輸出內部推理」之類的呼叫模式，很可能會被供應商判定為可疑行為並受到限制；提前了解這類反蒸餾機制，有助於避免正常整合被誤傷。

🔗 **來源**
- 標題：Strengthening our defenses against distillation attacks
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/research/distillation-defenses

#Anthropic #Claude #AISecurity #ModelDistillation #AIPolicy #LLMSecurity #AINationalSecurity #PromptSecurity #ChainOfThought #AIGovernance
