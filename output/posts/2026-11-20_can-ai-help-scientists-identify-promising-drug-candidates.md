---
title: Can AI help scientists identify promising drug candidates?
source: OpenAI Blog
url: https://openai.com/index/introducing-medchembench
model: claude-code/sonnet
generated_at: '2026-11-20T23:11:17.866542'
pinned: true
---

📌 MedChemBench：AI 能挑出對的候選藥物嗎？

TL;DR：OpenAI 推出 MedChemBench，用真實藥物化學論文數據測試 AI 的分子推理能力。

一個化合物可能對目標蛋白質的抑制效果很強，卻因為吸收不良或代謝太快而無法成藥。藥物化學家每天都在這種「顧此失彼」的權衡中做決策：改一個官能基救了活性，卻可能毀了穩定性。OpenAI 發布的 MedChemBench，就是為了測試 AI 模型能不能理解並參與這種權衡。

🤔 核心問題：結構與證據能不能連起來

要讓 AI 真正協助藥物研發，它必須能把分子結構的變化和實驗證據連結起來，解釋結果、比較化合物、並對性質做出預測。MedChemBench 想測的，正是模型在這條推理鏈上的表現。

🧩 基準怎麼設計

MedChemBench 取材自 117 篇已發表論文與專利，涵蓋 761 個不同的分子結構，共設計 99 道題目。大多數題目會給模型一個研究進程中某個時間點所能取得的資訊：生物目標、研究者的目標、已經研究過的化合物，以及部分實驗發現。評分分成四個面向：

- 分子結構：根據提供的繪圖與化學基團，正確組裝出原子連結與立體化學。
- 科學推理：解釋是否有實驗證據支撐，例如為什麼選擇某個化合物而非另一個。
- 排序與選擇：化合物排序與選擇是否符合題目要求。
- 性質預測：數值與分類預測是否與原始文獻的實測結果一致。

舉例來說，有一題取材自 PRMT5（一種被研究用於癌症藥物開發的蛋白質）抑制劑的研究，模型要根據既有結構和實驗結果，預測三個相關化合物在細胞內抑制 PRMT5 的強度、穿過細胞屏障的能力，以及被肝臟酵素分解的速度。題目藏起來的後續實驗結果顯示：化合物 23 在較低濃度下就能抑制 PRMT5，但化合物 24 穿透細胞屏障的能力更好、在肝酵素分析中分解得更慢，典型的此消彼長。

在結構重建的測試中，有一題要求模型從中心結構與兩個附加基團組裝出分子，同時保留一個 18 個原子的環。在所有模型共享的最高推理設定（xhigh）下，GPT‑6 Astra 在十次回答中全部正確重建；GPT‑5.6 Sol 與 GPT‑5.6 Luna 則十次全部失敗，分別組出 15 個原子的環、或把分子拆成兩個不相連的片段。

📊 分數看模型之間的差距

| 模型 | 整體得分（xhigh 設定） |
|---|---|
| GPT‑6.2 Astra | 84.5% |
| GPT‑6 Astra | 83.3% |
| GPT‑6.1 Sol | 82.0% |
| GPT‑6.1 Terra | 75.1% |
| GPT‑5.6 Sol | 58.2% |

GPT‑6 Astra 在 max 推理設定下可到 83.8%。拆開四個面向來看，Astra 在「分子結構重建」上拿下 95.4% 的可得分數，在「解釋科學證據」上也表現突出；但在「選擇化合物」與「預測數值性質」這兩個面向，大約只拿到一半的可得分數，顯示這兩類任務仍是明顯的弱點。

⚠️ 這個基準測不出什麼

OpenAI 在文章中明確提醒：這些結果並不能證明模型能夠發現新藥或改善實驗室的決策。模型是否曾經接觸過這些已發表的來源資料無法排除，而且每個回答都只是單次嘗試，沒有工具、回饋或新實驗的介入。換句話說，MedChemBench 測的是模型從既有歷史證據中推理的能力，而不是真實世界的藥物研發能力。

🎯 實務啟示

如果你的團隊在評估用 LLM 輔助藥物化學或材料科學研究，這個基準提供了一個具體的切入點：先看模型能不能正確重建結構、看懂證據，再看它能不能做排序與數值預測，這兩層能力目前的落差相當大，部署前該針對性驗證,而不是假設模型全面可靠。

🔗 來源
- 標題：Can AI help scientists identify promising drug candidates?
- 作者／機構：OpenAI
- 連結：https://openai.com/index/introducing-medchembench

#OpenAI #MedChemBench #DrugDiscovery #AIforScience #MedicinalChemistry #LLMBenchmark #GPT6Astra #ComputationalChemistry #AIResearch #ScientificReasoning
