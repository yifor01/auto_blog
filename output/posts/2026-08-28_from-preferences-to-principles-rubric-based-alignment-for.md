---
title: 'From Preferences to Principles: Rubric-Based Alignment for Grounded Knowledge
  Answers'
source: Apple ML
url: https://machinelearning.apple.com/research/rubric-based-alignment
model: claude-code/sonnet
generated_at: '2026-08-28T18:00:47.220129'
score: 97
---

📌 從「偏好」到「原則」:用 Rubric 取代單一分數的獎勵設計

TL;DR:Apple ML 提出以檢索證據為基礎的多維度 rubric 獎勵框架,在開放域問答的對齊訓練中比 baseline 提升 6.5%。

一個問答系統的回答好不好,從來不是一個分數能講完的事:內容對不對、有沒有證據支撐、有沒有回答到問題的每個要求,這些都是不同維度的問題,硬要壓成一個標量獎勵訓練訊號,注定會丟掉細節。

🤔 **單一標量獎勵,裝不下多維度的答案品質**

在開放域問答任務的 post-training 階段,設計有效的獎勵訊號本身就是一個難題,因為高品質的回答必須同時滿足答案品質的多個面向,而這些面向很難用單一的整體性標量目標去捕捉。

🧩 **針對每個查詢生成專屬 rubric,並依證據分解成多個維度**

Apple ML 團隊提出的 rubric-based reward framework,會針對每一個查詢生成專屬的 rubric,這些 rubric 以檢索到的證據(retrieved evidence)為基礎,並分解成多個品質維度,在 post-training 過程中提供細粒度的監督訊號,而不是只給一個籠統的整體分數。

📊 **三項評測軸平均提升 6.5%,比「扁平版」rubric 再多 4%**

在 composition(組織架構)、grounding(證據支撐)、instruction-following(指令遵循)三個評測軸上取平均,這套方法相較於經過 instruction-tuning 的 baseline 提升了 6.5%,相較於沒有拆分維度的「扁平版」rubric 變體,也再多出 4% 的提升,且在所有評測資料集上都呈現一致的增益。

💡 **證據對應到事實正確,拆分維度對應到組織與遵循度**

研究結果進一步指出兩個機制上的差異:把 rubric 建立在檢索到的證據之上,主要改善的是答案的事實支撐(factual support);而把 rubric 拆解成各自獨立的品質維度,則進一步改善了回答的連貫性、組織架構,以及對查詢要求的遵循程度。換句話說,「有沒有證據」和「有沒有拆分維度」分別對應到答案品質的不同面向,兩者疊加才帶來完整的提升。

🎯 **實務啟示**

如果你正在為 RAG 或開放域問答系統設計 RLHF 式的獎勵模型,與其用單一的偏好分數去訓練 reward model,更值得考慮的是針對每個查詢動態生成、並綁定檢索證據的多維度 rubric,把「內容對不對」「有沒有根據」「格式與遵循度好不好」拆開來給訊號,理論上能讓對齊訓練學到更精準的信號,而不是被單一分數平均掉的雜訊淹沒。

🔗 **來源**
- 標題:From Preferences to Principles: Rubric-Based Alignment for Grounded Knowledge Answers
- 作者/機構:Aman Saini, Priyanshu Kumar, Eric Peng, Kai Yuan, Harsh Girase, Wanming Chen(Apple ML)
- 連結:https://machinelearning.apple.com/research/rubric-based-alignment

#RLHF #RewardModel #OpenDomainQA #AppleML #Alignment #RAG #LLMTraining #PostTraining #RubricGrading #NLProc
