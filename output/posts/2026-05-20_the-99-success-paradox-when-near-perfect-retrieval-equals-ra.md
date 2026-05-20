---
title: "The 99% Success Paradox: When Near-Perfect Retrieval Equals Random Selection"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.18857
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-20T21:16:37.650598
---

📌 【Meta 最新研究】99% 檢索成功率其實是隨機猜？

你以為檢索越準越好？當成功率達到 99% 時，實際上可能只是在亂猜。

🤔 **高成功率掩蓋了隨機水準的選擇性**

傳統檢索評估側重於找到更多相關文件，但忽略了結果是否真的具有辨識力。當人類不再擔任最終過濾器時，這種盲點就會被放大。

🧪 **Bits‑over‑Random 度量揭露真實選擇性**

論文提出 BoR = log₂(P_obs / P_rand)，其中 P_rand 是根據成功規則（此處為 top‑K 內至少有一篇相關）的超幾何基準。此指標直接量測「比隨機猜測好多少」。

📊 **BM25 與 SPLADE 在 K=100 時 BoR≈0，成功率卻超過 99%**

在 20 Newsgroups 上，兩種稀疏檢索器皆報告 >99% 的覆蓋率（≥1 相關在前 100），但 BoR 接近零，意味著在該深度上其選擇性與隨機選擇無異。

💡 **當預期覆蓋率 K·R̄_q / N 超過 3‑5，選擇性崩潰**

當檢索深度導致預期命中數過大時，隨機基準佔主導，BoR 趨近零，進一步增加 K 只會提升計算成本而不帶來實質選擇性提升。

🔬 **下游 RAG 評估證實此現象：LLM 準確度在 K=100 時顯著下降**

檢索增強生成的實驗顯示，當使用上述深度時，LLM 的答案正確率明顯惡化，與 BoR 接近零的上限一致。

✅ **在 BEIR/SciFact 與 MS MARCO 上 BoR 仍為正值，系統間差距小**

在此兩個基準上，BoR 保持正數，且 41 個系統聚集在理論上限 0.2 bits 內，儘管召回率相差達 13 點，證實了度量在不同規模與稀疏度下的穩定性。

⚠️ **實驗範圍限於所列基準與單次 RAG 評估，未擴展至其他語言或任務**

🎯 **實務建議：在選擇檢索深度時參考 BoR，避免無效的計算開銷**

工程師可在報告傳統召回率同時補充 BoR 值；當 BoR 趨近零時，意味著再增加 K 不會提升選擇性，應該考慮更精準的過濾或重新設計檢索管線。

🔗 **論文連結**
📝 The 99% Success Paradox: When Near-Perfect Retrieval Equals Random Selection
👤 Vyzantinos Repantis, Harshvardhan Singh, Tony Joseph, Cien Zhang, Akash Vishwakarma @ Meta Platforms Inc.
🔗 https://arxiv.org/abs/2605.18857

#InformationRetrieval #RAG #LLM #Meta #BoR #Evaluation
