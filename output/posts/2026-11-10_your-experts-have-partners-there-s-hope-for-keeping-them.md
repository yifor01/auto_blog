---
title: Your Experts Have Partners. There's HOPE for Keeping Them Together
source: HuggingFace Blog
url: https://huggingface.co/blog/amazon/higher-order-pruning-experts
model: claude-code/sonnet
generated_at: '2026-11-10T00:51:05.012345'
score: 102
---

📌 【Amazon 研究】MoE 剪 Expert 前，先搞懂它們的「合作關係」

TL;DR：Amazon 提出二階剪枝法 HOPE，在 50% 裁剪率下編程任務最高多拿 6.1% 準確率。

一個擁有數百個 expert 的 MoE 模型，推理時真正被用到的往往只是其中一小撮，但整組 expert 卻得全部塞進記憶體待命。這篇研究要問的是：剪掉用不到的 expert，真的能剪得「聰明」嗎？

🤔 **95% 的記憶體躺在用不到的 Expert 身上**

文章以 Qwen3.5-122B 為例：這個模型每層 MoE 有 256 個 expert、共 48 層，約 250GB 的參數記憶體中有 95% 被 expert MLP 佔據，但對任一個 token，每層實際只會用到其中 8 個。Expert pruning（永久刪除最不重要的 expert）因此成為直接的解方：它不需要額外訓練、不會造成動態載入/卸載帶來的延遲問題，而且可以和量化（quantization）疊加使用。

真正困難的是「怎麼判斷哪個 expert 可以安全刪掉」。現有方法多半是一階方法：用校正資料集（calibration dataset）為每個 expert 獨立算出一個重要性分數，然後在各層裡砍掉分數最低的那些，等於假設每個 expert 的貢獻彼此獨立。但作者觀察到，expert 之間會形成穩定的合作群組，共同被同一批 token 啟用，這個現象在其他獨立研究中也被證實是 MoE 訓練後期趨於穩定、且對模型效能有重要影響的性質。一階方法完全忽略了這點：若 expert A 看起來不重要就被刪掉，但 A 經常與同樣重要的 expert B 合作，刪掉 A 其實是拆散了一整個合作群組，裁剪率越高，拆散的合作鏈就越多。

🧩 **HOPE：把 Expert 兩兩之間的交互作用算進去**

在標準 MoE 層裡，每個輸入 token 由一個 gating 層產生 softmax 正規化的門控權重，挑出權重最高的 K 個 expert（常見 K=8）組成該 token 的作用集合，該層輸出即為作用集合內每個 expert 輸出乘上各自門控權重後的加總。

直接去找「能讓裁剪後誤差最小」的刪除組合是不可行的，因為誤差大小取決於被替換上來的 expert 是誰，而這又取決於你刪的是哪些 expert，形成循環依賴。HOPE 的做法是定義一個可計算的替代目標：把被刪除、但原本會被選中的 expert，其門控權重乘上輸出向量的大小加總起來，再取平方，這個值可以嚴格上界真正的裁剪誤差中佔主導的部分。因為是「先加總再平方」，展開後自然會產生成對 expert 之間的交叉項，這正是一階方法直接丟棄掉的交互訊息。

把這個替代目標在校正資料集上取期望值後，整個問題可以重新表述成一個二元二次規劃：在「總共刪除數量固定」的限制下，找出一組 0/1 的刪除標記向量，讓該向量與一個 expert 兩兩交互矩陣相乘後的二次型數值最小。這個交互矩陣的每個元素，代表兩個 expert 在同時被啟用的 token 上，門控權重與輸出大小乘積的平均值；矩陣對角線上的值等於單一 expert 的重要性分數（等同一階方法在算的東西），非對角線上的值則衡量兩個 expert 的合作貢獻程度。求解時先對這個二次規劃做連續鬆弛，再把結果捨入回二元解，得到最終的刪除集合。

作者以 GLM-4.5-Air（128 expert/層，總參數 106B）視覺化這個交互矩陣，分別取早、中、晚期三個代表層，並把 expert 做群聚排序後發現：對角線附近會出現明顯的亮塊結構，顯示同一群組的 expert 彼此交互作用特別強，而且這種結構會隨著層數不同而改變。

📊 **50% 裁剪率下，HOPE 拿下最佳平均排名**

在 50% 的裁剪率測試中，HOPE 在所有比較方法裡取得最佳平均排名，在 agentic coding 任務上比次佳的裁剪方法最多高出 6.1%。作者強調，裁剪率越高，第二階交互項的影響越明顯，這也是為什麼 HOPE 的優勢在高裁剪率下最顯著。

🎯 **實務啟示**

如果你的團隊正在為大型 MoE 模型做推理端的記憶體瘦身，單純依賴對每個 expert 打分數的一階剪枝方法，在裁剪比例拉高時很容易誤砍掉合作群組裡的關鍵 expert。HOPE 這類考慮 expert 間交互作用的二階方法，提供了一個不需要額外訓練、可與量化疊加使用的選項，值得在壓縮前先評估自家模型的 expert 共啟動模式再決定裁剪策略。

🔗 **來源**
- 標題：Your Experts Have Partners. There's HOPE for Keeping Them Together（Higher-Order Pruning of Experts in Mixture-of-Experts Language Models）
- 機構：Amazon（HuggingFace Blog）
- 連結：https://huggingface.co/blog/amazon/higher-order-pruning-experts

#MoE #MixtureOfExperts #ModelPruning #LLM #Quantization #Amazon #HOPE #Inference #DeepLearning #AIResearch
