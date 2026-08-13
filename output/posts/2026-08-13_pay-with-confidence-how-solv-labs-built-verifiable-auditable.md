---
title: 'Pay with confidence: How Solv Labs built verifiable, auditable agent payments
  on Amazon Bedrock AgentCore payments'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/pay-with-confidence-how-solv-labs-built-verifiable-auditable-agent-payments-on-amazon-bedrock-agentcore-payments/
model: claude-code/sonnet
generated_at: '2026-08-13T07:40:52.204032'
score: 60
---

📌 AI Agent 花錢誰來擔保？AWS AgentCore Payments 的可稽核設計

TL;DR：Solv Labs 用 Amazon Bedrock AgentCore payments 打造每筆交易都可獨立驗證的 AI Agent 付款流程。

當 AI Agent 開始自主動用企業真金白銀，問題不再是「它有沒有完成任務」，而是「事後能不能證明這筆錢花得有依據」。這正是 Solv Labs 與 ICME Labs 這篇合著文章想解決的落地問題。

🤔 **稽核缺的不是紀錄，是「紀錄和決策的綁定」**

企業團隊常遇到同一個缺口：一筆 Agent 交易完成後，並沒有一份文件把「這個具體動作」和「授權它的政策、它滿足的限制條件、它承擔的風險」綁在一起。Model card、SOC 2 報告、事後審查描述的是組織層級的控管，而不是單筆決策的執行過程。缺少這種交易層級的綁定，營運方就沒有乾淨的方式解決爭議、應付稽核，或分辨一次正常的 Agent 操作和一次被入侵的操作。

🧩 **五個元件、固定順序，最後才放行結算**

Solv Labs 的方案建立在四項基礎設施之上：Amazon 於 2026 年 5 月與 Coinbase、Stripe 合作推出的 Amazon Bedrock AgentCore payments、AWS Automated Reasoning Checks（ARc）、作為每筆交易硬體證明者的 AWS Nitro Enclave，以及已廣泛採用的 Agent 付款標準 x402。整套工作流由五個專責元件組成：

1. AgentCore payments 負責付款處理基礎設施
2. ORACLE（Solv 的政策引擎）在每筆交易前做預授權決策
3. ICME PreFlight 延伸 AWS Automated Reasoning Checks，做隱私保護且可獨立驗證的合規檢查
4. 在 AWS Nitro Enclave 中運行的完整性服務，負責硬體證明
5. 風險引擎，對每筆交易個別定價

這五步依固定順序執行：先產出 ORACLE 的決策與其可獨立驗證的證明、硬體證明、逐筆風險定價，才會啟動結算，規則是「沒有決策，就沒有結算」。組件之間只透過帶簽章、雜湊綁定的產物跨越信任邊界，因此無論服務怎麼部署，證據鏈都能保持完整。

📊 **每筆交易 4 秒內完成，治理開銷不到 1 秒**

端到端延遲（涵蓋預授權、治理、透過 Coinbase 的鏈上結算）低於 4 秒，其中治理相關開銷不到 1 秒，符合 Agent 工作負載的延遲預算。每筆受治理的付款會產生一份簽章過的證據紀錄，內容綁定五項要素：被評估的政策、政策檢查結果與其可獨立驗證的證明、硬體證明的執行紀錄、逐筆風險定價，以及來自 AgentCore payments 的結算產物。整份紀錄經過正規化、在 Nitro Enclave 內以 Ed25519 簽章，並錨定到鏈上。

💡 **驗證方不是操作方，才是重點**

ICME Labs 共同創辦人 Houman Shadab 指出，這套設計要解的問題是「當付款決策的驗證者不是做出決策的營運方時，你需要一種方式證明檢查確實正確執行過，卻不用把政策內容本身攤在陽光下」；每個決策都附帶一個加密證明，第三方或監管單位可以在一秒內驗證，卻看不到政策細節或交易參數。Solv Labs 執行長 Patrick Duffy 則形容，過去企業拿不到「這筆付款為什麼被允許」的乾淨答案，只能得到關於整個組織的籠統保證，而現在證據跟著交易本身走。

⚠️ **它證明的是「流程合規」，不是「決策正確」**

作者明確劃清界線：這套機制不證明 Agent 底層的判斷是明智的，不證明交易對手有清償能力，也不證明政策本身寫得對——這些仍是營運方自己的責任，就像其他付款方式一樣。它證明的只是「這筆特定付款，在這些特定限制條件下，按這個特定風險定價，通過了這項特定政策的評估，而這個評估結果正是授權結算的依據」。

🎯 **實務啟示**

對於正在評估讓 Agent 自主處理金流的團隊，這個案例提供了一個具體的參照架構：治理決策與硬體證明必須在結算前完成、且彼此雜湊綁定，而不是事後補一份報告。若你的系統也牽涉監管環境下的 Agent 付款，「決策可獨立驗證」會比單純「有紀錄」更能通過稽核與爭議處理的考驗。

🔗 **來源**
- 標題：Pay with confidence: How Solv Labs built verifiable, auditable agent payments on Amazon Bedrock AgentCore payments
- 作者／機構：Patrick Duffy（Solv Labs）、Houman Shadab（ICME Labs）
- 連結：https://aws.amazon.com/blogs/machine-learning/pay-with-confidence-how-solv-labs-built-verifiable-auditable-agent-payments-on-amazon-bedrock-agentcore-payments/

#AgentCore #AIAgents #AWS #AgentPayments #NitroEnclave #AutomatedReasoning #Blockchain #EnterpriseAI #Compliance #AIGovernance
