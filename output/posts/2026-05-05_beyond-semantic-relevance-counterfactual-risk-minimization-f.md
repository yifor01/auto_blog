---
title: "Beyond Semantic Relevance: Counterfactual Risk Minimization for Robust Retrieval-Augmented Generation"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.01302
score: 126
model: tencent/hy3-preview:free
generated_at: 2026-05-05T19:37:11.215695
---

📌 打破相關性迷思：北大與騰訊提出 CoRM-RAG 讓 RAG 敢拒絕偏誤查詢

標準 RAG 系統越「相關」，在偏誤查詢下反而越容易跟著使用者一起幻覺。最新研究指出，當查詢帶有錯誤前提或確認偏誤時，單純最大化語義相關性等同於主動檢索「奉承式證據」，讓模型更難自我糾偏。

🤔 **語義相關性不保證決策正確**

現實中的使用者查詢常帶有認知偏誤：錯誤前提、確認偏誤或片面歸因。傳統 RAG 以語義相關性作為效用代理，卻在這類場景中出現「相關性—魯棒性缺口」——檢索越相關，越容易強化錯誤假設，放大幻覺與安全風險。

🧪 **反事實風險最小化與認知干擾協議**

研究團隊提出 CoRM-RAG（Counterfactual Risk Minimization for RAG），以因果干預重新對齊檢索目標：
- **Cognitive Perturbation Protocol**：在訓練階段模擬使用者的偏誤查詢，迫使檢索與推理經受對抗性干擾。
- **輕量 Evidence Critic**：將上述干預經驗蒸餾為一個可部署的評分模組，用以判斷文件是否具備足夠的「證據強度」，而非僅僅與查詢相似。

🛡️ **在對抗設定下顯著降低偏誤跟風與幻覺**

在多項決策導向基準上，CoRM-RAG 相比強勢稠密檢索器與 LLM 重新排序器表現更穩：
- 更低的事實偏離率與較少的偏誤跟風回應；
- 具備可靠的風險感知能力，可在證據不足時有效拒絕或退避（abstention），而非盲目生成。

💡 **從「拉取相關內容」轉向「維持決策安全」**

關鍵差異在於目標函式的設計：CoRM-RAG 不以相似度為最終終點，而是透過反事實風險最小化，使檢索結果能抵禦查詢層的干擾。輕量 Evidence Critic 讓系統在低延遲下同時具備判斷力與可解釋性，適合對可靠性要求高的決策場景。

⚠️ **研究以對抗性設定為主，實務部署長期穩定性待驗證**

實驗主要在對抗與偏誤誘導設定下進行，雖顯著改善短期的魯棒性，但在長時間線、資料偏移與真實使用者反饋環節中的穩定表現仍需持續觀察；此外，Evidence Critic 的泛化能力依賴干擾協議的覆蓋度。

🎯 **在決策導向 RAG 中引入風險感知與可控退避機制**

- 將「是否足夠說服模型拒絕偏誤」納入檢索評估，而非僅看相似度；
- 對高風險應用（如金融、醫療、審查）優先啟用 Evidence Critic 風險評分；
- 結合可配置的退避閾值，在低證據強度下主動拒絕生成或請求澄清。

🔗 **論文連結**  
📝 Beyond Semantic Relevance: Counterfactual Risk Minimization for Robust Retrieval-Augmented Generation  
👤 Peiyang Liu, Qiang Yan, Ziqiang Cui, Di Liang, Xi Wang  
🏢 National Engineering Research Center for Software Engineering; Peking University; PX Securities; City University of Hong Kong; Tencent Technology  
🔗 https://arxiv.org/abs/2605.01302  
💻 原始碼：https://github.com/PeiYangLiu/CoRM-RAG.git

你的 RAG 系統如何處理帶有偏誤或錯誤前提的查詢？是否曾因過度依賴語義相關而跟風生成錯誤？歡迎分享實務經驗 👇

#RAG #AI安全 #檢索增強 #DecisionMaking #NLP #可信AI #大模型 #北大 #騰訊技術
