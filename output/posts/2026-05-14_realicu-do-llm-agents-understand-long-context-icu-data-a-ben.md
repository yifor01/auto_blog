---
title: "RealICU: Do LLM Agents Understand Long-Context ICU Data? A Benchmark Beyond Behavior Imitation"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.13542
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-05-14T20:45:07.903455
---

📌 **RealICU：評估 LLM 在 ICU 長序列決策的新基準**

你以為讓 AI 看完病歷就能給出正確建議？研究顯示，即使是最強的 LLM，在真實 ICU 長情境下也會陷入兩種致命錯誤。

🤔 **ICU 資料冗長且時刻變化，現有基準以醫師過去行為為真值，可能偏誤**  
重症監護病房產出長、密且持續演變的臨床資料流，醫師必須在時間壓力下反覆重新評估病人狀態。現有的 ICU 基準常以歷史臨床決策作為 ground truth，但這些決策本身是在資訊不完整、時間視野有限的情況下做出，可能並非最佳，因而難以真正衡量 AI 的推理能力。

🧪 **以後見註釋建立真實標籤，分為兩個資料集**  
研究團隊讓資深醫師在完整病人軌跡可見的情況下進行後見標註，構建 RealICU 基準。他們設計了四項醫師導向任務：評估 Patient Status、Acute Problems、Recommended Actions 以及可能導致不安全結果的 Red Flag actions。每段病程以 30 分鐘為窗口進行切分，釋出兩個資料集：  
- **RealICU‑Gold**：來自 94 位 MIMIC-IV 病人的 930 倔窗口標註。  
- **RealICU‑Scale**：在 Gold 基礎上，經由醫師驗證的 LLM（稱作 Oracle）擴展至 11,862 倔窗口。

💡 **現有 LLM 在四項臨床任務上表現不佳，暴露兩種失誤模式**  
即使是記憶增強的大型語言模型在 RealICU 上也普遍表現不佳。分析揭示兩種主要失誤：  
1. **召回‑安全權衡**：在給出臨床建議時，模型往往在召覆完整資訊與避免不安全建議之間難以同時取得佳績。  
2. **早期錨定偏見**：模型對病程初期的解讀過度影響後續判斷，導致後續資訊被忽略或誤讀。

🔍 **記憶增強的 agent 改善長程推理但無法完全消除安全失誤**  
為了改善長距離依賴建模，團隊提出結構化記憶的 ICU‑Evo agent。實驗顯示該方法確實提升了長 horizon 的推理能力，但在安全相關的 Red Flag 任務上仍無法完全克服上述失誤模式。

⚠️ **標註依賴 Oracle LLM，真實醫師驗證範圍有限**  
RealICU‑Scale 的擴展依賴於經醫師驗證的 LLM 作為標註者（Oracle），此過程雖經驗證，但最終標註仍帶有模型偏見；此外，樣本主要來源於單一公開資料集 (MIMIC-IV)，不同醫院與人種分布的一般性有待進一步驗證。

🎯 **未來需同時考慮召回與安全，並警惕早期錨定偏見**  
對於高風險的臨床決策支援，單纯追求模型在長文件上的記憶或召回是不足的。設計時應該：  
- 在訓練與評估中明確區分「召回」與「安全」兩個目標，避免片面優化其中之一。  
- 引入機制來減少對早期資訊的過度依賴，例如輪動注意力或外部知識校正。  
- 結合結構化記憶與人類在迴路中的驗證，以提升長期序列推論的可靠性。

🔗 **論文連結**  
📝 RealICU: Do LLM Agents Understand Long-Context ICU Data? A Benchmark Beyond Behavior Imitation  
👤 Chengzhi Shen, Weixiang Shen, Tobias Susetzky, 等（Technical University of Munich; TUM University Hospital; LMU Munich; University of Sheffield; University of Oxford; Zhongshan Hospital Fudan University; Sun Yat-sen University Cancer Center; Imperial College London; Munich Center for Machine Learning; relAI – Konrad Zuse School of Excellence in Reliable AI）  
🔗 https://arxiv.org/abs/2605.13542  
🌐 頁面：https://chengzhi-leo.github.io/RealICU-Bench/

你認為在 ICU 這類高 stakes 場景中，該如何平衡 AI 的長文理解與安全決策？歡迎留言討論 👇

#AI #醫療AI #LLM #床決策支援 #RealICU #TUM #醫學研究 #機器學習 #醫療科技
