---
title: "EndPrompt: Efficient Long-Context Extension via Terminal Anchoring"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.14589
score: 129
model: tencent/hy3-preview:free
generated_at: 2026-05-15T20:08:49.531410
---

📌 【Nankai 大學等】EndPrompt：用短序列也能把 LLaMA 推到 64K 上下文  

你以為要訓練超長序列才能延伸模型上下文？其實只要兩段短文就能做到。  

🤔 **長上下文訓練不必真的長**  
傳統做法需要在目標長度的完整序列上進行微調，這會導致二次方的記憶與運算成本，使長上下文適應變得昂貴且難以重現。  

🧪 **兩段構造：保留原始片段＋終端提示**  
EndPrompt 的核心是把原始短語境保留為第一段，再附加一段極短的終端提示作為第二段，並將該提示的位置索引設置為接近目標上下文長度。這種做法在極短的實際序列中同時產生局部與遠端的相對位置距離，同時維持訓練文本的語義連續性——這正是以分塊方式模擬長序列所缺少的特性。  

📊 **在 LLaMA 系列模型上的表現**  
將模型從 8K 上下文延伸至 64K，EndPrompt 在 RULER 基準上取得平均分 76.03，在 LongBench 上達到最高平均分，超越 LCEG（72.24）、LongLoRA（72.95）以及完整長度微調（69.23），而所需的計算資源顯著減少。  

💡 **位置插值帶來的平滑約束**  
論文提供了基於 Rotary Position Embedding（RoPE）與 Bernstein 不等式的理論分析，表明位置插值會在注意力函數上施加嚴格的平滑條件；共享的 Transformer 參數進一步抑制對未觀測到的中間距離進行不穩定的外推。  

⚠️ **研究的限制**  
目前的實驗僅針對 LLaMA 家族模型從 8K 到 64K 的延伸進行驗證；未涉及其他架構或更長的目標長度；理論分析假設了特定的位置編碼形式。  

🎯 **對工程師的實務建議**  
若需要在有限計算資源下擴大模型上下文窗口，可嘗試採用 EndPrompt 的兩段訓練策略：保留原始短文本作為語義基礎，僅加入少量終端提示並賦予遠端位置索引。此方法既能獲得長距離位置訊號，又避免了完整長序列的高昂成本。  

🔗 **論文連結**  
📝 EndPrompt: Efficient Long-Context Extension via Terminal Anchoring  
👤 Han Tian, Luxuan Chen, Xinran Chen, Rui Kong, Fang Wang (Nankai University; Baidu Inc.; Shanghai Jiao Tong University; Independent Researcher)  
🔗 https://arxiv.org/abs/2605.14589  
💻 程式碼：https://github.com/clx1415926/EndPrompt  

#AI #LLM #長上下文 #EndPrompt #Nankai #Baidu #上海交通大學 #機器學習 #深度學習 #開源代碼
