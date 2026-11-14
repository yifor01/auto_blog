---
title: 'Cmpnd Releases dspy-wsp: Weight-Space Programming Comes to DSPy'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/14/cmpnd-dspy-wsp-weight-space-programming/
model: claude-code/sonnet
generated_at: '2026-11-14T21:34:42.431026'
score: 90
---

📌 LLM直接改寫模型權重：DSPy迎來Weight-Space最佳化器

TL;DR：Cmpnd推出dspy-wsp，讓frontier LLM直接讀寫模型權重最佳化決策模型，無需梯度與訓練資料。

多數人最佳化模型不脫三條路：調prompt、篩資料、或梯度下降微調。Cmpnd最新發布的dspy-wsp提出第四條路——讓一個frontier LLM直接「讀」另一個模型的權重，推理出每個部分在算什麼，再直接動手「改」。

🤔 **把權重當成一段可以被讀寫的程式**

Weight-space programming（WSP）這個概念來自MIT研究《Sparks of Weight-Space Programming》：把神經網路的權重視為一段可以被讀取與改寫的程式。研究中使用的frontier模型是GPT-6-Astra，它看著權重張量，推理出每個部分大致在計算什麼，再依照一段用plain English寫下的目標去修改。研究團隊特別強調，WSP描述的是一種正在出現的能力，而不是一套固定方法；他們的實驗禁用了梯度，但這個概念本身並不排斥梯度。這被視為LLM最佳化路徑的下一步：先前的做法是讓LLM在prompt、harness、訓練程式碼這類text artifact上做hill-climbing，權重本身還是交給Adam或weight-generating network，WSP則主張LLM的推理能力現在可以直接碰到權重。

🧩 **固定預算的writer，加上可驗證的patch**

dspy-wsp把這個研究流程包裝成一個標準DSPy optimizer，叫WeightSpace，可以插進任何DSPy程式與metric。GitHub repo描述了三個角色，其中writer分多輪運作，每輪先給一段簡短說明，再給一個code block用來編輯權重。forward pass的次數有固定預算，測試中設為max_passes=25，預算用完後，writer目前最好的一次編輯就會成為最終patch。之後會用一份隱藏的validation set，在相同的examples與seeds下比較原始與編輯後的權重，repo特別強調資料要分離開來，避免驗證結果失真。每次執行的patch會寫到run_dir，內含manifest.json與只記錄改動項目的edit.npz，同時存下每個base與edited tensor的sha256 hash——只要有公開的base model，任何人都可以精確重建出編輯後的權重。實際編輯相當精準且局部：d1-2B沒有decision head，writer就改了它backbone的第23層；d1-omni-600M則是改寫了decision head裡scorer的一部分。

使用方式上，範例以支援單分流為例，DSPy signature只用decision-type輸出，compile完後程式會呼叫本地編輯過的模型而非hosted API，compiled.wsp_patch.summary()能看到具體改了什麼。文字生成LLM透過VLLMBackend（NVIDIA）、HFBackend（CUDA/MPS/CPU）、MLXBackend（Apple Silicon）運作，編輯後的決策模型在Apple Silicon上跑MLX，Linux上跑PyTorch（有NVIDIA GPU則用GPU）。另外還有一個由Michael Isaac貢獻的GEPASearch選項，為決策模型加入population search。

📊 **幾美元的呼叫，換來兩位數的分數提升**

Cmpnd用Typed Decisions這個benchmark測試：模型讀一段非結構化狀態，同時回答5個typed問題，每個答案是一個機率分布，測試集有400 cases、2,000 decisions，每個模型拿到25次forward pass的額度。以gpt-6.1-sol當writer時，WeightSpace單獨使用在d1-omni-600M上拿到+5.8分，NanoJev上+12.1分，d1-2B上則是−0.6分；換成GPT-6-Astra後分別是+16.1、+13.3、+13.4分，標準誤差約±0.7到1.4點。Cmpnd另一個optimizer叫ReAnchor，靠重新校準決策模型輸出機率對應的門檻值（不需要LLM呼叫）來最佳化；WeightSpace改的是模型本身，ReAnchor校準的是輸出，兩者可以疊加使用。

⚠️ **只能移除障礙，補不上原本就缺的能力**

MIT原始研究在Gemma 3 270M上測試時，編輯只把MATH-500從6.8%推到7.0%至7.7%之間，研究團隊自己並不把這算作真正的進步：編輯可以移除障礙，但無法補上模型本來就缺的能力。dspy-wsp預設讓writer可以在它的kernel內重新計算decision head，如果設定simulate_head=False強制套用論文更嚴格的規則，d1-omni-600M的提升就只剩+2.8±0.7分，再疊加ReAnchor也只到+9.3分，並沒有比單用ReAnchor更好。

🎯 **低成本的權重編輯，值得先在小模型上試試**

這目前仍是prototype階段，且測試模型與樣本量都偏小，但對已經訓練好decision model、又不想重新跑一輪fine-tuning的團隊而言，用幾美元的LLM呼叫去「編輯」既有權重是一個值得關注的低成本手段；透過sha256與可重建的patch機制，這類權重編輯也具備可驗證、可追溯的特性，方便納入既有的模型治理流程。

🔗 **來源**
- 標題：Cmpnd Releases dspy-wsp: Weight-Space Programming Comes to DSPy
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/14/cmpnd-dspy-wsp-weight-space-programming/

#DSPy #WeightSpaceProgramming #LLM #MachineLearning #ModelEditing #AIOptimization #OpenSource #MIT #PromptEngineering #AIResearch
