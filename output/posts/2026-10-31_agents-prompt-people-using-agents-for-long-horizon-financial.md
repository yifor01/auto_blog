---
title: 'Agents Prompt People: Using Agents for Long-Horizon Financial Work'
source: Latent Space
url: https://latent.space/p/arca/
model: claude-code/sonnet
generated_at: '2026-10-31T20:40:50.765684'
score: 76
---

📌 Arca給的啟示：理財Agent為何要「提示人類」而非被人類提示

TL;DR：AI原生理財顧問公司Arca讓Agent處理長達十天的理財任務，但交易決策權仍完全留給人類顧問。

多數人想像的AI Agent是「你下指令、它執行」。但在AI原生財富管理公司Arca，情況反過來了：Agent會主動提示顧問下一步該做什麼。該公司AI工程負責人Aman Singh在AI Engineer New York的分享中，用一句話點出這個反直覺的設計：「Agent提示人類，比人類提示Agent更多。」

🤔 **理財工作是長週期，但不是長時間運行**

Singh指出，金融服務裡的AI任務有個特殊性質：工作橫跨的時間很長（long-horizon），卻不是持續運算（long-running）。他提到，Arca的Agent任務可能耗時長達十天，過程「非常地停停走走，中間有很多角色參與、很多決策點、很多交接」。podcast章節中也提到像是處理一筆10萬美元稅務帳單這類情境，正是Agent分析加上人類核准交織而成的流程。

🧩 **每個客戶都有一套持續運作的記憶系統**

為了撐住這種跨多日、多角色的流程，Arca自建了內部記憶系統，為每位客戶維護持久化狀態：目前進展到哪裡、接下來要追蹤什麼、未來幾天內必須立即處理的事項，以及每個行動由哪位負責人承接。這些資訊全部由Agent持續寫入並更新。

在模型選擇上，Arca使用Anthropic與OpenAI等前沿實驗室的模型，其中Claude是主要供應商。公司自建了harness（執行框架），依照內部benchmark自動為每個任務挑選最適合的模型；自建而非採用現成的managed agent harness，也讓Arca保有更換模型供應商的彈性。

⚠️ **安全護欄是「完全確定性」的，決策權不留給Agent**

Singh強調，Agent的角色被限制在分析與提出方案，交易執行與任何資金移動都必須經由人類顧問處理。「我們所有的安全限制都是完全確定性的（fully deterministic），」他說，「這把決策權從Agent手上拿走。」換句話說,哪些工具與任務Agent可以自行執行是明確界定的，涉及客戶風險的動作則不在此列。

Arca也針對已知的AI安全問題（如prompt injection）進行驗證檢查。Agent本身沒有被沙箱化,但運算會在沙箱中進行;針對敏感資料,他們做了更進一步的防護——把Agent寫的程式碼轉譯成一種嚴格格式,丟棄原始程式碼,並在這個格式上安裝guardrail,確保格式合規後才能碰到後端資料。這讓Agent可以用程式碼查詢、彙整、處理資料,進而產出像財務計畫這類成果,同時降低任意程式碼執行帶來的風險。

🎯 **把人類回饋變成Agent的下一輪訓練資料**

另一個值得注意的機制是:Arca會把顧問的人類回饋與Agent的執行軌跡(trace)一起餵給一個「meta-agent」,由它分析這些資料並提出harness的改進建議。對於正在打造高風險領域Agent系統的工程師而言,這個案例提供了幾個可借鏡的設計原則:用確定性護欄把「決策」與「分析」分開,而不是指望模型自律;為跨多日、多角色的任務建立持久化記憶,而非依賴單次對話的context;以及建立顧問回饋→trace→meta-agent→harness迭代的閉環,讓evals隨實際使用不斷進化。

🔗 **來源**
- 標題：Agents Prompt People: Using Agents for Long-Horizon Financial Work
- 作者／機構：Latent Space
- 連結：https://latent.space/p/arca/

#AIAgents #WealthManagement #FinTech #AgenticAI #Claude #Anthropic #LLMOps #AIEngineering #AgentMemory #AISafety
