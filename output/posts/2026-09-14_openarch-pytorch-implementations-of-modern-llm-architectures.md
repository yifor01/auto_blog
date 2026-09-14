---
title: OpenArch – PyTorch implementations of modern LLM architectures
source: Hacker News
url: https://github.com/anuj0456/OpenArch
model: claude-code/sonnet
generated_at: '2026-09-14T21:06:26.049505'
score: 85
---

📌 OpenArch：把主流LLM架構寫成一個個能讀懂的檔案

TL;DR：OpenArch用手刻PyTorch重現GPT-2到DeepSeek R1等架構，讓attention、正規化、位置編碼的差異一目了然。

讀官方模型的程式碼常常很痛苦，不是因為架構本身難懂，而是那些程式碼是為了速度、切分（sharding）與向後相容而寫的，不是為了讓人看懂。OpenArch這個在Hacker News上拿下126點讚、29則留言的專案，反其道而行。

🤔 為誰而做：把架構差異攤開來比較

現代LLM架構共用一套基本骨架，卻在許多細節上做出不同選擇：attention可能是MHA、GQA、MQA、MLA、sliding-window，或是linear／DeltaNet混合型；正規化可能是pre-norm、post-norm、QK-Norm、sandwich norm或RMSNorm；位置編碼可能用RoPE、NoPE、部分RoPE或YaRN；decoder可能是dense、稀疏MoE（有無shared expert）,或是Mamba與attention的混合型。OpenArch的README直言，這個專案的目標不是要和transformers這類正式函式庫競爭，而是追求「清晰與學習」，讓每種架構有一個好讀的單一檔案，把上述結構性選擇都寫得明明白白，方便並排比較。

🧩 設計理念：一個模型、一個資料夾、一份可讀的實作

每個模型都放在自己的資料夾裡，包含一份model.py與一份簡短的README.md，記錄該架構用到的結構性選擇與參考來源。目前的資料夾結構分成text（文字模型）與multimodal（多模態模型）兩大類，例如text/gpt2、text/llama3、text/qwen3、text/deepseek_v3等。所有實作都是依據原始論文、技術報告、官方config.json，以及Sebastian Raschka的LLM Architecture Gallery、Big LLM Architecture Comparison系列文章與Machine Learning Mastery團隊的教學寫成的，README特別致謝了這兩方的貢獻，也是整個專案背後最主要的參考依據。

📊 目前收錄了哪些模型

專案目標是涵蓋Architecture Gallery裡列出的72種架構，目前已完成（標記✅，可用於forward pass）的文字模型包括GPT-2 XL（1.5B）、Llama 2（7B）、Llama 3（8B，改用GQA）、OLMo 2（7B）、DeepSeek R1（671B，採用Multihead Latent Attention與MoE）、Gemma 3（27B，GQA加sliding window）、Mistral 3（24B）、Llama 4 Maverick（400B，帶MoE）、Qwen 3（4B與30B-A3B的MoE版本）、Kimi K2（1T，MLA加MoE）、GLM 4.5（355B，GQA加Multi-Token Prediction與MoE）、GPT-OSS（20B，GQA加sliding window與MoE）；Grok-2.5（270B）則標記為施工中（🚧）。多模態部分已完成PaliGemma（3B），Qwen3多模態版與影像模型Dall-e仍在施工中。

⚠️ 只做forward pass，不是生產級函式庫

README明確寫了幾個限制：這些實作只到forward pass可用，並非完整訓練或推論最佳化的產品程式碼；作者強調「實作應優先考慮可讀性而非效能」，這是一個學習資源，不是要取代transformers這類正式函式庫；專案也附上免責聲明，所有實作是依公開論文、技術報告與config.json盡力還原，並未獲得原始模型作者的背書或關聯，若要正式生產使用，建議還是採用官方實作或transformers。專案採用Apache 2.0授權，個別模型另依原始模型授權條款而定。

🎯 實務啟示

如果你想搞懂DeepSeek R1的Multihead Latent Attention、GLM 4.5的Multi-Token Prediction，或是Qwen3 MoE版本的路由設計到底和GPT-OSS差在哪裡，與其硬啃官方為效能與切分最佳化過的程式碼，不如直接對照OpenArch裡對應模型的單一model.py檔案。專案目前仍在積極尋找貢獻者，無論是補上尚未實作的架構、幫既有模型寫README、或加上驗證forward pass輸出的測試，都是不錯的切入點。

🔗 來源
- 標題：OpenArch – PyTorch implementations of modern LLM architectures
- 作者／機構：anuj0456（Hacker News，126 points，29 comments）
- 連結：https://github.com/anuj0456/OpenArch

#LLM #PyTorch #OpenSource #DeepLearning #TransformerArchitecture #MoE #Attention #MachineLearning #AIEngineering #ModelArchitecture
