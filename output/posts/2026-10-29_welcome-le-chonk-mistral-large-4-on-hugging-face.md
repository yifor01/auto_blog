---
title: 'Welcome Le Chonk: Mistral Large 4 on Hugging Face'
source: HuggingFace Blog
url: https://huggingface.co/blog/mistral-large4
model: claude-code/sonnet
generated_at: '2026-10-29T21:57:12.931453'
score: 113
---

📌 Mistral Large 4「胖嘬」登場：兆參數 MoE，資安拿下 82%

TL;DR：Mistral 開源兆參數 MoE 模型 Le Chonk，資安測試贏過多個閉源前沿模型，Day-0 支援主流推理框架。

當多數閉源前沿模型在面對「重現漏洞、分析惡意程式」這類資安任務時選擇直接拒答，Mistral 的新模型反而把這件事當成強項來打——這正是 Mistral Large 4（代號 Le Chonk）在 HuggingFace 上發布時最引人注目的地方。

🤔 一個約 1T 參數、只用 49B 做事的模型

Mistral Large 4 是多模態、多語言的 Mixture-of-Experts（MoE）模型，輸入文字與圖片，輸出文字。總參數約 1T，但每次推理只啟動 49B 的active parameter，context window 達 1M tokens。官方釋出 FP8 與 NVFP4 兩個版本，另有 Unsloth 與 llama.cpp 團隊製作的 GGUF 量化版，授權為 Mistral Ecosystem Open-Weight License（MIT 衍生授權，對 model-as-a-service 的商用情境有額外限制）。

🧩 兩種稀疏性：選 Expert，也選要看哪些 token

模型結合大量 expert 池、sparse attention,以及 Pixtral 視覺編碼器。語言模型對每個 token 選一小群 expert 來處理,同時注意力機制中的 indexer 會挑選要關注哪些先前的 token 位置——一個是 feed-forward network 的稀疏選擇,另一個是 context 位置的稀疏選擇。

文字解碼器共 72 層,hidden dimension 6,144,64 個注意力頭。注意力區塊結合 Multi-head Latent Attention（MLA）與 DeepSeek Sparse Attention（DSA）indexer（GLM 5.3 等模型也採用同樣方向）：MLA 保留壓縮後的 KV 表示,DSA 則替每個 query 挑出最多 2,048 個 key 位置。每個 decoder block 採 3:1 的 RoPE 對 NoPE 比例,即每 4 層中有 3 層用 RoPE,第 4 層用 NoPE,並在層間共享 KV 狀態。RoPE 部分使用 LeRope,一種 YaRN 縮放版 RoPE,每個頻率各帶一個可學習乘數。

第一個 decoder 層是密集 feed-forward network,其餘 71 層都是 MoE block,由 softmax router 替每個 token 從 128 個 expert 中選出 4 個,再加上一個永遠啟動的 shared expert,等於每個 token 共有 5 個 active expert。

視覺端採用 1.6B 參數的 Pixtral 編碼器,30 層、hidden dimension 2,048、16 個注意力頭,使用 14×14 patch 與 spatial merge size 2 的 patch-merge projector。

📊 資安測試 82%,編碼代理指標也領先同級

在 Artificial Analysis Cyber Index 的「重現真實漏洞並修補」測試中,Mistral Large 4 拿下 82%,是該指標中目前最高分;Mistral 表示多個閉源前沿模型在同一測試中接近零分,原因是直接拒絕作答。模型在 Cybench(40 道資安競賽題)中解出 93%,在 Lakera B3 的 prompt-injection 抵抗測試中達 93.3%。

編碼方面,DeepSWE v1.1 得 61.7%、SWE-Atlas-QnA 得 59.4%、Terminal-Bench 4 得 28.3%,綜合 Coding Agent Index 為 49.8%,領先 DeepSeek V4 Pro 0813 與 Qwen3.8 Max。在長時程商務任務上,AutomationBench 得 59.9%,AA-Briefcase 達 1,393 Elo。截至 2026 年 10 月 29 日,該模型在 Artificial Analysis Intelligence Index 上是第五強的開放權重模型。

值得注意的是,雖然資安能力突出,模型在 JailbreakBench、StrongREJECT、AgentHarm 等資安相關 prompt 上的平均拒答率,仍高於其他任何開放權重模型——Mistral 將其定位為防禦性資安工具,而非繞過安全限制的捷徑。

💡 開放權重,讓「重現再修補」變成可驗證的 RL 任務

Mistral 內部測試顯示,模型在惡意程式分析、漏洞優先排序、偵測規則撰寫上也表現不錯,即使這些並非模型明確訓練的目標。對社群開發者而言,開放權重意味著可以針對自己的程式碼庫、crash log、惡意程式樣本打造專屬資安系統;由於「重現再修補」任務天生帶有可驗證的 reward,這類資料也適合用 TRL 之類工具,從 Mistral Large 4 產生的 trace 去微調更小的資安專用模型,進一步做 RL。開放權重同時讓研究者能直接量測模型的拒答行為,不必只依賴廠商自述。

🎯 實務啟示

Mistral Large 4 在發布當天就取得 transformers、vLLM、llama.cpp 的支援,並可透過 Inference Endpoints 與 Inference Providers 部署。在 transformers 中可透過 AutoModelForMultimodalLM 與 AutoProcessor 載入,reasoning_effort 可選 low/medium/high,預設為 high,且無法完全關閉推理(即使設為 none 仍會以 high 執行)。對於需要自建資安代理、或是需要在內部環境長時間跑漏洞分析而不想被 API 政策或可用性中斷的團隊,這是目前少數同時具備強資安能力與完全開放部署自由度的選擇。

🔗 來源
- 標題:Welcome Le Chonk: Mistral Large 4 on Hugging Face
- 作者/機構:HuggingFace(merve、Alvaro Bartolome、Rémi Ouazan Reboul、Cyril Vallez、Quentin Gallouédec 等)
- 連結:https://huggingface.co/blog/mistral-large4

#MistralAI #LeChonk #MixtureOfExperts #MoE #OpenWeights #Cybersecurity #LLM #Multimodal #HuggingFace #AIInference
