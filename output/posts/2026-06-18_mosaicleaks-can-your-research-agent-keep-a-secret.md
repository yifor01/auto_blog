---
title: 'MosaicLeaks: Can your research agent keep a secret?'
source: HuggingFace Blog
url: https://huggingface.co/blog/ServiceNow/mosaicleaks
score: 103
model: google/gemma-4-31b-it:free
generated_at: '2026-06-18T20:48:13.819085'
---

📌 【HuggingFace 最新研究】你的 AI 研究助手會「不小心」洩密嗎？

當企業導入 Deep Research Agent，讓 AI 同時讀取公司內部私密文件並使用網路搜尋來完成複雜任務時，我們往往只關注 AI 的答案是否正確，卻忽略了一個致命風險：AI 發出的「搜尋請求」本身就可能洩露機密。

🤔 **單次搜尋看似無害，但組合起來就是機密**

想像一個醫療公司的 AI 助手在執行任務時，發出了幾次看似普通的網路搜尋：一次關於雲端遷移里程碑，一次關於 2024 年的安全性揭露，一次關於特定供應商的受災情況。

單看任何一筆搜尋紀錄，可能都沒什麼問題。但如果監控者將這些碎片重新組合（Mosaic Effect），就能推論出：「MediConn 在 2025 年 1 月前已將 70% 基礎設施遷移至雲端」——而這個事實僅存在於公司的私密文件中。這就是 MosaicLeaks 研究的核心：即使對手看不到私密文件或 AI 的推理過程，僅憑「外部查詢日誌 (Query Log)」就能拼湊出企業機密。

🧪 **設計「多跳 (Multi-hop)」任務來測試隱私洩漏**

HuggingFace 與 ServiceNow 團隊提出了 MosaicLeaks 測試框架，專門設計需要「交織」公開資訊與私密資訊的多跳問題。

研究將外部查詢視為洩漏通道，測試 AI 在尋找答案的過程中，是否會在搜尋字串中不自覺地帶入私密文件的細節。研究發現，現有模型在執行這類任務時頻繁發生洩漏，且一個令人不安的發現是：**如果僅針對「任務完成度 (Task Performance)」進行訓練，反而會讓洩漏情況變得更嚴重。**

💡 **Privacy-Aware Deep Research (PA-DR) 的權衡與突破**

為了平衡「任務成功率」與「隱私保護」，研究團隊提出了一種新的強化學習 (RL) 訓練方法：Privacy-Aware Deep Research (PA-DR)。

其核心目標是在不犧牲能力的前提下，教導 Agent 如何在不洩漏私密資訊的情況下進行外部檢索。實驗結果顯示，PA-DR 取得了顯著的成效：
- **成功率提升**：嚴格鏈接成功率 (Strict Chain Success) 從 48.7% 提升至 58.7%。
- **洩漏率下降**：答案/完整資訊洩漏率 (Answer/Full-information Leakage) 從 34.0% 大幅降至 9.9%。

這證明了隱私保護與性能提升並不一定是零和遊戲，透過正確的 RL 獎勵機制，可以讓 AI 學會「謹慎地搜尋」。

⚠️ **監控對象僅限於外部流量，尚未涵蓋所有通道**

此研究將洩漏通道定義為「外部查詢日誌 (Query Log)」，假設對手無法看到私密文件或 AI 的內部推理過程。這意味著該研究聚焦於外部流量監控的風險，而非模型本身的權重洩漏或對話輸出洩漏。

🎯 **企業部署 AI Agent 的實務啟示**

對於正在開發或部署企業級 AI Agent 的工程師，這項研究提供了重要的警示：
- **不要過度依賴性能指標**：單純追求 Task Success Rate 可能會導致 AI 為了快速找到答案而將私密資訊直接放入搜尋框。
- **重新定義獎勵函數**：在 RL 訓練中，必須將「隱私保護」作為一等公民，納入獎勵機制中。
- **審查外部請求**：對於 Agent 的 Outbound Traffic 應建立監控機制，意識到「查詢紀錄」本身就是一種敏感數據。

🔗 **論文與資源連結**
📝 MosaicLeaks: Can your research agent keep a secret?
👤 Alexander Gurung & Rafael Pardinas (@ServiceNow)
🔗 完整文章：https://huggingface.co/blog/ServiceNow/mosaicleaks

在追求 AI 自動化研究的效率時，你是否考慮過 AI 的「搜尋習慣」可能成為企業的安全漏洞？歡迎在下方討論你的看法 👇

#AI #Privacy #LLM #DeepResearch #HuggingFace #ServiceNow #CyberSecurity #強化學習
