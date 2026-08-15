---
title: Alignment with experimental data improves protein generative modeling
source: Nature.com
url: https://www.nature.com/articles/s41592-026-03138-2
model: nvidia/nemotron-3-ultra-550b-a55b:free
generated_at: '2026-08-15T06:16:25.749885'
score: 101
---

📌 以 DPO 對齊實驗數據，打造可生成耐熱蛋白序列的 ProteinDPO

TL;DR：將偏好最佳化引入蛋白質語言模型，利用實驗穩定性數據訓練出 ProteinDPO，能評分並生成耐熱序列，並在 H5N1 血球凝集素上驗證成效。

🎣 **蛋白質設計的新關鍵：不只「合理」，還要「耐熱」**

蛋白質語言模型（pLM）已能生成結構合理的序列，但合成生物學與疫苗開發真正需要的，往往是能在高溫、極端環境下保持功能的「耐熱蛋白」。傳統流程需大量溼式實驗篩選，成本高、週期長。若能讓模型直接內化實驗穩定性偏好，生成即可用的熱穩定序列，將大幅縮短設計迴路。

🧩 **Direct Preference Optimization 直擊實驗偏好**

論文提出 **ProteinDPO**，核心思路是將 **Direct Preference Optimization (DPO)**——原本用於大型語言模型對齊人類偏好的演算法——移植到蛋白質生成任務：
1. 以預訓練蛋白質語言模型為基礎。
2. 收集實驗測得的蛋白質熱穩定性數據（如熔點 Tm 或殘留活性），構建「偏好數據對」：穩定序列為 chosen、不穩定序列為 rejected。
3. 以 DPO 損失函數最佳化模型，使其隱性學習穩定序列的分佈特徵，無需額外訓練獎勵模型，流程較 RLHF 更輕量。

此法讓模型從「模仿天然序列分佈」轉向「生成高穩定性序列分佈」，推理階段可直接對候選序列打分或進行條件生成。

📊 **H5N1 血球凝集素實證：大幅提升熱穩定性**

作者將 ProteinDPO 應用於 **H5N1 流感病毒血球凝集素**，這是疫苗株開發與抗病毒研究的關鍵靶標。結果顯示，模型生成的變體序列在實驗驗證中展現出 **顯著提升的熱穩定性**，證實「對齊實驗數據」確能將模型能力從結構合理性延伸至物理化學性質優化。

💡 **為何這對蛋白質工程師很重要**

- **資料效率**：DPO 僅需成對偏好數據，不需昂貴的絕對親和力標註，適合實驗室常見的相對比較數據（如熱位移實驗篩選結果）。
- **部署門檻低**：無需訓練獨立 Reward Model，單一模型即可評分與生成，易於整合進既有設計管線。
- **泛化潛力**：同樣框架可擴展至溶解度、表達量、酵素活性等任何可構建偏好對的表型。

⚠️ **素材未提及的細節**

摘要被截斷，具體效能指標（如 Tm 提升幅度、成功率、與 Rosetta 或其他基線比較）、訓練超參數、資料集規模、模型架構細節（如 ESM-2 還是自訓練 pLM）均未在提供素材中出現，故不在此補充。

🎯 **實務啟示：把「溼式實驗篩選結果」餵給模型**

若你手邊有深度突變掃描或高通量篩選的相對比較數據（A 比 B 穩定），即可嘗試以 DPO 微調現有 pLM，將實驗經驗蒸餾為生成式先驗知識。這比訓練預測器再配合優化演算法更直覺，也更接近「生成即優化」的理想工作流。

🔗 **來源**
- 標題：Alignment with experimental data improves protein generative modeling
- 連結：https://www.nature.com/articles/s41592-026-03138-2

#ProteinDesign #DPO #ProteinLanguageModel #GenerativeAI #Thermostability #H5N1 #Hemagglutinin #ComputationalBiology #MachineLearning #NatureMethods
