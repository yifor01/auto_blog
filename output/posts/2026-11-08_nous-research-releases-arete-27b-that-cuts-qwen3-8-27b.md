---
title: Nous Research Releases Arete-27B that Cuts Qwen3.8-27B Propaganda From 22%
  to 0.9%
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/07/nous-research-arete-27b-qwen3-8-27b-propaganda-fine-tune/
model: claude-code/sonnet
generated_at: '2026-11-08T21:15:03.109751'
score: 87
---

📌 純SFT把Qwen的「國家敘事」砍到剩0.9%

TL;DR：Nous Research用純監督式微調把Qwen3.8-27B的宣傳式回答比例從22%降到0.9%，權重、資料、評測全部公開。

不用RL、不碰架構，只靠監督式微調，就能讓一個模型在敏感議題上的回答內容出現劇烈轉變——這是Nous Research的Arete-27B想證明的事。

🤔 為什麼挑Qwen3.8-27B當base model

Nous團隊表示，他們在base model回答敏感話題時觀察到refusal、deflection，以及帶有中國官方立場框架的答案。選擇Qwen3.8-27B是因為它是當時能力最強、同時又明顯表現出這種行為的本地可跑模型。

🧩 方法：只做SFT，teacher是開放模型Inkling

Arete-27B是Qwen3.8-27B經過監督式微調後的版本，沒有用RL，沒有preference optimization，也沒有改動架構，授權延續base model的Apache 2.0。Teacher模型用的是Thinking Machines的開放模型Inkling，選用開放teacher是為了避開蒸餾相關的使用條款限制；團隊原本考慮過Nemotron 3 Ultra，但發現它在中國相關議題上同樣有「不一致的紀錄」而放棄。

🧩 資料與訓練設定

訓練資料約52.8M tokens，context長度64k，沒有使用sequence packing。訓練跑了2個epoch、1,202步，batch size 48，優化器用AdamW，peak learning rate 1e-5，tensor parallel 4。所有語言模型權重都參與訓練；因為資料全是文字，視覺encoder維持凍結；multi-token-prediction head則被停用。

公開的arete-data-pairs資料集含34,878筆跨7個主題的prompt，每一筆都同時附上Inkling與Qwen的回答，其中29,236筆被接受的teacher回答組成最終的SFT訓練集。評測用的Propaganda_Eval資料集含803筆prompt，跨7個價值類別，包括言論自由、國家意識形態、資料隱私與民主，每筆prompt都附帶2到4個來自引用來源的必要事實。評分由Grok 4.7擔任judge，分別針對「事實分數」與「是否含宣傳用語」兩件事獨立打分，且judge必須引用具體文字才能判定為宣傳。Nous也把所有與評測集重疊的訓練prompt移除掉，評測集本身是MIT授權，連評分腳本都一併公開。

📊 事實分數上升，宣傳比例大降

| 指標 | Qwen3.8-27B（base） | Arete-27B |
|---|---|---|
| Fact mean | 2.32 | 2.98 |
| 含宣傳回答比例 | 22% | 0.9% |
| 得0分的回答數（/803） | 359 | 216 |
| 言論自由類別 Fact score | 0.89 | 2.44 |
| 言論自由類別 宣傳比例 | 60% | 1% |

能力面大致持平：Hermes Bench從65.77%變成65.60%，Nous認為這屬於誤差範圍內的noise；Terminal-Bench-2.1在Nous自家測試harness下從67%上升到70%，但Nous表示不把這項進步歸功於這次微調。

⚠️ 比較時要注意的條件差異

文中特別註明，Arete與Qwen在Nous的評測裡以temperature 0運行，作為對照的Muse Glimmer與Gemma則用0.6，取樣條件並不相同；Terminal-Bench的數字也來自不同的測試harness，彼此不能直接比較。目前沒有任何hosted inference provider上架這個模型，權重以BF16格式放在Hugging Face，社群製作的GGUF量化版本（8.64GB到53.81GB）可以在llama.cpp、LM Studio、Ollama上執行，這些GGUF版本也包含了image projector。

🎯 實務啟示

如果應用場景需要Qwen級別的agentic能力，但想避開特定意識形態框架的回答內容，Arete-27B提供了一條公開可驗證的路徑：權重、訓練資料與評測腳本全部開放，可以自行重現結果，甚至照同樣的流程套用到其他base model上。

🔗 來源
- 標題：Nous Research Releases Arete-27B that Cuts Qwen3.8-27B Propaganda From 22% to 0.9%
- 作者／機構：Asif Razzaq（MarkTechPost）；Nous Research
- 連結：https://www.marktechpost.com/2026/11/07/nous-research-arete-27b-qwen3-8-27b-propaganda-fine-tune/

#NousResearch #Qwen #SFT #OpenWeights #LLM #FineTuning #AIAlignment #Distillation #ApacheLicense #MachineLearning
