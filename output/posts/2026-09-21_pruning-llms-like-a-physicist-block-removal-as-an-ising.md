---
title: 'Pruning LLMs Like a Physicist: Block Removal as an Ising Optimization Problem'
source: HuggingFace Blog
url: https://huggingface.co/blog/MultiverseComputingCAI/pruning-llms-like-a-physicist-block-removal-as-an
model: claude-code/sonnet
generated_at: '2026-09-21T21:16:39.319369'
score: 97
---

📌 把 LLM 剪枝當成 Ising 模型來解

TL;DR：Multiverse Computing 把 transformer 區塊刪除問題轉成自旋玻璃能量最小化，Llama-3.3-70B 在 50% 壓縮下 MMLU 多贏近 23 個百分點。

刪掉整個 transformer 區塊（block removal，又稱 depth pruning）是壓縮 LLM 最直接的手法之一，模型變短，推論速度和記憶體用量都跟著下降。難的不是「刪不刪」，而是「刪哪幾個」——刪錯區塊模型直接崩潰，而且刪除任何一個區塊的影響，取決於你同時刪了哪些其他區塊。這種互相牽連的組合問題，恰好就是統計物理學描述自旋系統時最擅長的題型。

🤔 **為什麼選區塊是個多體問題**

現有的區塊刪除方法大多對每個區塊各自打分（用 magnitude、sensitivity 或「block influence」之類的啟發式指標），再刪掉分數最低的幾個。用物理學的語言講，這是 mean-field 方法：把每個區塊的貢獻當成獨立事件處理，就像平均場理論用一個平均場取代自旋的鄰居交互作用。另一種常見的簡化做法，是只允許刪除連續的一段區塊，這樣搜尋空間雖然變小，卻也丟掉了絕大部分的可能組合。

問題在於區塊之間並不獨立，就跟真實磁鐵裡的自旋一樣。刪除區塊 20 會不會傷害模型，取決於你是否同時刪了區塊 19 或區塊 24——這是兩個決策之間的耦合（coupling）。模型越深、越異質，忽略這些耦合就越容易在「一次刪很多區塊」的場景下犧牲品質。而組合數量隨區塊數指數成長，暴力搜尋看似不可行，這正是統計物理工具能派上用場的情境。

🧩 **把區塊選擇變成能量最小化問題**

作者團隊給每個 transformer 區塊配一個二元變數：0 代表保留，1 代表刪除，就像一個能朝上或朝下的自旋。接著對模型損失函數做二階泰勒展開，得到一個（近似）Hessian 矩陣：對角線代表每個區塊自身的重要性，非對角線項則正是區塊間的成對耦合——也就是 mean-field 方法直接丟棄的那部分多體物理。

這樣一來，「該刪哪些區塊」就變成一個乾淨的最佳化問題：在 N 個區塊中找出一組 M 個區塊，使能量 xᵀH⁰x 最小，同時滿足恰好刪除 M 個的限制條件。數學上這是一個 constrained binary optimization（CBO）問題；物理上則等價於一個自旋玻璃（Ising glass），一個具有全連接耦合、且磁化量（即被刪除的區塊數）守恆的自旋系統。作者建立的關鍵性質是：這個能量是下游模型品質的強力代理指標——低能量狀態對應高效能的剪枝模型，最小化能量與最大化 benchmark 分數因此變成同一個搜尋問題。

這套方法之所以可行，關鍵在成本。完整的耦合矩陣（Hessian）只需要在一小批校準資料上跑一次前向與反向傳播就能算出來；之後評估任何候選組合，只是一次便宜的能量計算，完全不需要真的跑模型、更不用說跑 benchmark。而且由於耦合本身不依賴壓縮目標，同一份 Hessian 可以重複用來求解不同的 M 值。

📊 **精確解法用到量子啟發式求解器**

對大多數模型來說，配置空間雖大但仍可窮舉。由於算一次能量的成本很低，作者直接在單一 GPU 上暴力搜尋，最多驗證到數百億種自旋組態：數百萬種組合只要幾秒，而目前處理過最難的可行案例——在 Llama-3.3-70B 的 80 個區塊中刪除 8 個（約 290 億種組合）——耗時約兩天。

超過這個規模，暴力法就撐不住了，這時候把問題重新表述為 Ising glass 的第二個好處就浮現：轉成等價的 QUBO 形式後（把限制條件吸收進懲罰項），同一個任務可以直接丟給專門處理這類 Hamiltonian 的最佳化求解器——量子退火、QAOA、tabu search、專用分支界定法等等。作者發現一款開源 tabu 求解器能在幾秒內穩定找到最低能量狀態，即便是目前能用暴力法驗證的最難案例也不例外。

這裡有個和一般最佳化思路相反的重點：通常 CBO 或退火求解器的好壞取決於能不能找到真正的基態（ground state），但作者團隊其實不需要基態，他們需要的只是快速產生「幾個」品質不錯的低能量狀態，這個門檻低得多，也是為什麼輕量求解器在這裡表現得這麼好、甚至可以同時跑好幾種求解器。

💡 **低能量光譜比單一答案更重要**

能量是強力但並不完美的品質代理指標，所以單一最低能量狀態未必就是最好的模型。這反而是優點：一旦 Hamiltonian 建好，讀出基態和鄰近的激發態幾乎不用額外成本，等於一次拿到一整組候選剪枝方案，而不是賭一個脆弱的答案。

一個具體案例：對 Llama-3.1-8B-Instruct 刪除 16/32 個區塊時，大多數高分狀態都傾向刪除模型後段的區塊，符合先前研究的預期；但第 17 個激發態是第一個提議刪除模型前段區塊的組態，經過輕量重訓後，這個組態在多個 benchmark 上的表現反而超越了基態。

📊 **50% 壓縮下的實測差距**

在 Llama-3.3-70B-Instruct 進行 50% 壓縮的深度壓縮場景下，這套方法相較於目前最好的競爭區塊刪除方法，在 MMLU 上取得將近 23 個百分點的提升。

🎯 **實務啟示**

如果你的壓縮流程還停留在「逐區塊打分、砍最弱的」，這篇工作提醒你：區塊之間的耦合在深度壓縮時不能忽略。而且方法本身成本可控——Hessian 只算一次、可重複用於不同壓縮比，遇到搜尋空間爆炸時也有現成的 tabu solver 可用，是少數把物理學工具直接接上模型壓縮工程實務、且論文可複現的案例。

🔗 **來源**
- 標題：Pruning LLMs Like a Physicist: Block Removal as an Ising Optimization Problem
- 作者／機構：Antonio Tiene, Ali Hashemi, David Jansen, Roman Rausch（Multiverse Computing）
- 連結：https://huggingface.co/blog/MultiverseComputingCAI/pruning-llms-like-a-physicist-block-removal-as-an

#LLMPruning #ModelCompression #IsingModel #QUBO #QuantumInspired #DepthPruning #TransformerOptimization #MMLU #Llama #AIResearch
