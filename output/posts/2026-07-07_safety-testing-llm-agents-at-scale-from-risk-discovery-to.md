---
title: 'Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded
  Verification'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.01793
score: 91
model: google/gemma-4-31b-it:free
generated_at: '2026-07-07T21:20:42.500952'
---

📌 如何大規模測試 LLM Agent 的安全性？Vera 框架將風險發現與驗證系統化

TL;DR：Vera 透過三階段管線，將風險分類、案例生成與沙盒驗證自動化，提升 Agent 安全測試規模。

當 LLM Agent 從單純的對話轉向具備執行能力的代理人，安全性挑戰也隨之升級。傳統的紅隊測試（Red Teaming）過於依賴人工，難以在大規模部署前全面覆蓋所有潛在風險，如何系統化地發現並驗證 Agent 的安全漏洞，成為落地前的核心痛點。

🧩 **Vera 框架的三階段自動化測試管線**

為了實現大規模的安全測試，Vera 採取了由風險定義到實作驗證的結構化流程：

1. **結構化風險分類 (Structured Risk Taxonomies)**：首先定義風險分類法，將潛在的安全風險模組化，確保測試覆蓋面完整。
2. **組合式案例生成 (Combinatorial Case Generation)**：基於上述分類，透過組合不同的變數與情境，自動生成大量測試案例，避免人工設計的侷限。
3. **自適應沙盒執行與證據驗證 (Adaptive Sandbox Execution & Evidence-based Verification)**：將案例在沙盒環境中執行，並透過基於證據（Evidence-grounded）的驗證機制，確認 Agent 的行為是否真的觸發了安全風險。

🎯 **實務啟示**

對於開發 Agent 的工程師而言，這套流程提供了一個從「定義風險 → 自動生成測試 → 閉環驗證」的標準化路徑。在部署具有執行許可權的 Agent 前，建立類似的沙盒驗證機制，能將安全性測試從「隨機抽樣」提升至「結構化覆蓋」，降低生產環境中的不可預測風險。

🔗 **來源**
- 標題：Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Verification
- 連結：https://huggingface.co/papers/2607.01793

#LLM #LLMAgents #AI_Safety #SecurityTesting #Vera #RedTeaming #Sandbox #Automation #Verification #AI_Risk
