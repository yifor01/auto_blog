---
title: 'DrugGen 2: A disease-aware language model for enhancing drug discovery'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.08404
score: 93
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T08:15:59.040650'
---

📌 DrugGen 2：結合疾病本體與蛋白序列的藥物分子生成模型  

TL;DR：透過在 GPT-2 上進行監督學習與 GRPO 強化學習，DrugGen-2 能依疾病本體與目標蛋白序列生成具有較高多樣性與結合親和力的小分子。  

🎣 傳統藥物設計依賴大量實驗篩選，而語言模型能否直接從疾病描述與蛋白序列「寫出」潛在藥物分子？  

🧩 方法或架構  
摘要指出，DrugGen-2 是以 GPT-2 為基礎模型，先經監督學習微調，再採用 GRPO（Group Relative Policy Optimization）進行強化學習，以疾病本體與目標蛋白序列作為條件，生成小分子結構。  

📊 資料或結果  
摘要表明，相比於基線模型，DrugGen-2 在分子多樣性與結合親和力上表現較佳。具體資料集、評估指標或基線模型名稱未在摘要中說明。  

💡 深入分析  
因為摘要未提供實驗細節，無法進一步分析模型架構細節或訓練成本。僅可知其結合了監督與強化學習兩階段策略。  

⚠️ 限制  
摘要未提及模型的限制或未來工作，因此無法在此說明具體不足。  

🎯 實務啟示  
若需在藥物發現早期階段利用語言模型生成候選分子，可考慮將疾病本體資訊與蛋白序列作為條件輸入，並探索監督學習後續強化學習的微調流程。  

🔗 來源  
- 標題：DrugGen 2: A disease-aware language model for enhancing drug discovery  
- 連結：https://huggingface.co/papers/2607.08404  

#DrugGen2 #GPT2 #GRPO #DrugDiscovery #MolecularGeneration #DiseaseOntology #ProteinSequence #ReinforcementLearning #SupervisedLearning #AIforScience
