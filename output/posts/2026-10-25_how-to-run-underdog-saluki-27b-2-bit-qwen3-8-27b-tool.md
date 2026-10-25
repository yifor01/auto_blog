---
title: 'How to Run Underdog Saluki 27B: 2-Bit Qwen3.8-27B Tool-Calling Guide'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/24/underdog-saluki-27b-coding-guide-llama-cpp/
model: claude-code/sonnet
generated_at: '2026-10-25T19:48:02.663762'
score: 80
---

📌 2-bit量化模型真能贏原模型？逐byte拆穿Saluki 27B

TL;DR：逐byte比對量化模型與原模型GGUF檔案，再用BFCL基準驗證。

官方說法是：這個只有7.9GB的2-bit量化版本，在他們自己的120題benchmark上甚至贏過54GB的原始模型。這份教學沒有直接相信，而是把兩個檔案放進同一套llama.cpp，從header到byte全部核對一遍。

🤔 要驗證的問題
Underdog Saluki 27B是Qwen3.8-27B的7.9GB build，約每個權重2 bits，開發者宣稱保留完整的tool calling能力。它建立在ISTA-DASLab的GSQ-RCO量化版本之上，教學想確認的是：Saluki究竟只是把ISTA的量化結果重新包裝，還是權重真的被動過。

🧩 怎麼驗證：從header diff到paired統計測試
整套流程先把所有依賴版本與檔案的SHA-256全部pin住，包括llama.cpp的release版本、兩個模型檔案，以及14個BFCL檔案，並固定sampler，避免llama-server用到預設值干擾結果。驗證分四層：
1. 先讀兩個GGUF檔案的header，逐tensor比對型別與形狀。
2. 對型別沒變的tensor做byte-level比較，判斷Saluki是否只是ISTA檔案的remix。
3. 把兩個模型分別serve在同一張GPU上，讀取記憶體佔用與prefill／decode速度。
4. 用Berkeley Function Calling Leaderboard（BFCL）自行抽出的120道種子任務，讓兩個模型對同一批題目作答，用BFCL自己的checker做strict與lenient兩種評分，再對分數不一致的題目做exact McNemar test，得到一個paired比較。

📊 header一致，但weights確實被改過
- 兩個檔案的851個tensor形狀完全相同；Saluki改變了146個tensor的型別，而且每一次改變都是在縮減位元，多數集中在feed-forward down projection與輸出層，DeltaNet的gate向量從BF16降到Q8_0；attention與DeltaNet的投影矩陣沒有變動，header仍然標註ISTA DASLab為量化者。
- 在型別沒變的705個tensor裡，352個量化矩陣中只有1個與原檔完全一致，但有98.4%的bytes吻合；未量化的norm與gate向量，變化中位數只有萬分之幾。結論是：Saluki是一個被輕度修改過的模型，不是單純的重新編碼，與開發者自稱的「preview checkpoint」說法一致。
- 架構上，Qwen3.8-27B是hybrid設計：64個block中有48個是帶固定recurrent state的Gated DeltaNet linear-attention層，每四個block才保留一次完整attention，因此KV cache只需要每個token 64 KiB（而非256 KiB），外加每個序列約150 MiB的額外state。

⚠️ 教學自己也承認的限制
樣本量小、用的是greedy decoding、而且只跑一次，這些都限制了結論的強度。教學也明確指出沒有測試的部分：完整尺寸的Qwen3.8-27B、廠商自己的任務清單、agentic與math類的benchmark，以及vision擴充功能。

🎯 實務啟示
這份教學真正的價值未必在「Saluki到底值不值得用」，而是示範了一套可重複的量化模型驗證流程：把所有依賴版本與檔案hash全部pin住、用同一套harness跑兩個模型以避免prompt與parser差異污染比較、用paired statistical test而不是肉眼比分數。如果你要在production導入量化模型做tool calling，這套流程比任何單一結論都更值得照搬；但驗證方法本身延續自既有的GGUF diff與BFCL評測作法，並非全新的技術。

🔗 來源
- 標題：How to Run Underdog Saluki 27B: 2-Bit Qwen3.8-27B Tool-Calling Guide
- 作者／機構：Sana Hassan（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/10/24/underdog-saluki-27b-coding-guide-llama-cpp/

#Quantization #LLM #Qwen #llamacpp #ToolCalling #ModelEvaluation #BFCL #GGUF #EdgeAI #OpenWeights
