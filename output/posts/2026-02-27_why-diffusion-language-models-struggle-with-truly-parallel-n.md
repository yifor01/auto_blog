---
title: "Why Diffusion Language Models Struggle with Truly Parallel (Non-Autoregressive) Decoding?"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2602.23225
score: 103
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-02-27T23:33:43.868606
---

📌 **Diffusion Language Models 的「並行」陷阱：為什麼它們總是變成 autoregressive？**

Diffusion Language Models (DLMs) 被吹捧為能夠實現平行 token 生成的革命性技術，但為什麼實際上它們總是退化成 left-to-right、autoregressive 的解碼模式？這不僅是理論問題，更是影響推理速度和效率的關鍵瓶頸。

🤔 **並行解碼的承諾 vs. 現實的退化**

DLMs 的理論優勢在於：一次生成多個 token，充分利用 GPU 平行計算能力，減少 sequential bottleneck。但實際上，大多數 fast DLMs 在 decoding 時都會收斂到類似 autoregressive 的行為——一次一個 token，從左到右。

為什麼會這樣？這篇來自香港理工大學、圖賓根 AI 中心等機構的研究，揭示了核心問題：**目標函數與訓練資料的結構性錯配**。

🧪 **52 位工程師的隨機對照實驗**

研究團隊發現，標準 pretraining 語料和長 chain-of-thought (CoT) 數據，其本質上就是 sequential 的。DLMs 在這種數據上訓練，自然會學到「一個接一個」的推理模式，即使在理論上支援平行生成。

💡 **NAP：重新設計數據與解碼策略**

為了解決這個問題，研究團隊提出 **NAP (Non-Autoregressive Parallel DLMs)**，一個 data-centric 的方法：

1. 重新 curate 數據：將例子組織成多個獨立的推理路徑
2. 平行強制解碼：鼓勵多 token 同時更新
3. 結果：在數學推理 benchmark 上，NAP 在平行解碼下表現優於傳統長 CoT 訓練的 DLMs，且隨著平行度增加，優勢還會增長

⚠️ **關鍵洞察：資料結構決定模型行為**

這項研究的深遠意義在於：它告訴我們，**模型的並行能力不僅是架構問題，更是資料問題**。如果你用 sequential 的數據訓練一個理論上支援平行的模型，它還是會學成 sequential 的。

🎯 **對實務的啟示**

- 想要真正實現平行生成，需要重新設計訓練數據的結構
- 標準的長 CoT 數據可能不是最佳選擇
- 未來的 DLMs 需要 data-centric 的優化策略

🔗 **論文連結**
📝 Why Diffusion Language Models Struggle with Truly Parallel (Non-Autoregressive) Decoding?
👤 Pengxiang Li, Dilxat Muhtar, Lu Yin, Tianlong Chen, Shiwei Liu
🏛️ 香港理工大學、圖賓根 AI 中心等
🔗 arxiv.org/abs/2602.23225
🔗 程式碼：github.com/pixeli99/NAP

#DiffusionModels #DLM #NaturalLanguageProcessing #AI效率 #平行計算 #機器學習 #技術研究
