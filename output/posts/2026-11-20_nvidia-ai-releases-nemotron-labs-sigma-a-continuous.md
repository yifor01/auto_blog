---
title: NVIDIA AI Releases Nemotron-Labs-Sigma, a Continuous Diffusion Language Model
  with 14 checkpoints at 3B/8B
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/20/nvidia-nemotron-labs-sigma-continuous-diffusion-language-model/
model: claude-code/sonnet
generated_at: '2026-11-20T23:17:20.773558'
score: 106
---

📌 NVIDIA Nemotron-Labs-Sigma：讓文字擴散改走連續空間

TL;DR：NVIDIA 首個連續嵌入空間擴散語言模型，推理最快提速逾 3 倍。

多數擴散語言模型（diffusion LLM）在離散 token 上去雜訊，像走格子一樣跳來跳去；NVIDIA 的新模型選了一條不同的路：讓文字在連續空間裡像影像擴散模型一樣被平滑地「雕」出來。

🤔 離散擴散為什麼難以被引導

LLaDA、Dream 等現有擴散語言模型都在離散 token 狀態之間跳轉去雜訊，這類離散跳轉讓生成軌跡很難被引導（steer），也限制了少步驟蒸餾（few-step distillation）的效果。NVIDIA 研究團隊因此提出 Nemotron-Labs-Sigma，並稱其為「首個大規模的連續擴散語言模型家族」，共有 14 組開權重，分為 3B 與 8B 兩個尺寸，每個尺寸各有 4 種變體類型。

🧩 把 token 變成 16 維空間裡的一個點

Sigma 把每個 token 映射到一個學習出來的 16 維嵌入空間中的一個點。訓練時對這些嵌入加入高斯雜訊，再教模型把雜訊去除；嵌入空間的幾何結構與去雜訊器（denoiser）一起聯合學習。由於走的是平滑的 ODE/SDE 路徑而非離散跳轉，論文指出這類軌跡在步驟數少時能更優雅地退化，也更適合蒸餾；嵌入空間的引導還能用來調節 pass@k 取樣時品質與多樣性之間的取捨。

生成過程以區塊方式進行，預設每區塊 64 個 token，每個去雜訊完成的區塊會先寫入 KV cache，再開始下一個區塊。骨幹網路是 Ministral 風格的 decoder-only Transformer，搭配 grouped-query attention、SwiGLU 與旋轉位置編碼。推理時，classifier-free guidance 與 score temperature 是最關鍵的兩個參數，模型卡建議在 32 步 DDIM 取樣下使用 guidance 3、temperature 0.3。

🧪 先學自迴歸，再學擴散

訓練先以約 1T token 的自迴歸暖啟動，再接續約 0.3T token 的擴散訓練。

📊 8B 擴散模型追上甚至打平自迴歸基準

在 NVIDIA 自家的 6 項基礎任務測試中，以 256 步 DDPM 取樣的 Sigma-8B 平均分數為 71.16，對照組 NLD-8B 擴散模式為 70.22、Dream-7B 為 58.74、LLaDA-8B 僅 41.78；作為自迴歸基準的 Qwen3-8B 則是 68.91。即便把取樣步數砍到更便宜的 32 步 DDIM，Sigma-8B 仍維持 70.18 的平均分數。

程式碼能力是亮點：Sigma-8B 在 HumanEval 拿下 65.12 分，優於 NLD-8B 的 62.80；但在 MBPP 稍弱，65.74 分對 NLD-8B 的 67.00。經過 SFT 之後，Sigma-8B-instruct 在 GSM8K 拿下 91.96、MATH-500 為 78.40、HumanEval 為 82.50，10 項任務平均 59.14，略低於 NLD-8B 的 59.92。以上分數皆為 NVIDIA 自家評測。

蒸餾版本 Sigma-distill-8B-nfe8 每個 32-token 區塊只需 8 次去雜訊器呼叫加 1 次讀出，6 項任務平均分數達 70.34（GSM8K 88.44、HumanEval 65.18），已相當接近使用 256 步的教師模型；NVIDIA 將這個效率提升形容為數學任務每次前向推理可產出 8 個 token、程式碼任務則是 4 個。distill-spec 系列更進一步加入自我推測解碼：擴散頭負責起草一個 32-token 區塊，模型自己的自迴歸頭負責驗證，輸出結果與貪婪自迴歸解碼完全一致。在單張 GB200 搭配 SGLang 的測試中，8B 的 spec 模型平均比自迴歸解碼快 3.46 倍，NLD-8B 則是 3.04 倍，峰值加速分別達到 4.20 倍與 3.18 倍。

⚠️ 困難推理題仍是弱點

Sigma 在困難推理任務上明顯不足，AIME24 僅 23.33、AIME25 僅 17.00，顯示連續擴散的生成方式在需要長鏈推理的題型上還有落差。

🎯 實務啟示

14 組 checkpoint 全數上架 Hugging Face，採用 NVIDIA Nemotron Open Model License，模型卡標示可用於商業用途。部署門檻相當明確：需要支援 bfloat16 的 CUDA GPU（Ampere、Lovelace、Hopper 或 Blackwell），不支援 CPU 推理，載入需要 PyTorch 2.4+、Transformers 4.55+ 並開啟 trust_remote_code；單張 H100 上基礎模型約可產出每秒 120 到 140 個 token。蒸餾版模型卡列出 vLLM、SGLang 與 Docker Model Runner 作為建議的服務框架，NVIDIA 本身不提供託管 API，要用得自己架設伺服器。對已經在用擴散式 LLM 做低延遲生成的團隊，distill-spec 系列的自我推測解碼值得優先評估，因為它保證輸出與自迴歸貪婪解碼一致，不犧牲正確性卻能換到數倍的生成速度。

🔗 來源
- 標題：NVIDIA AI Releases Nemotron-Labs-Sigma, a Continuous Diffusion Language Model with 14 checkpoints at 3B/8B
- 作者／機構：Asif Razzaq／MarkTechPost；模型由 NVIDIA 釋出
- 連結：https://www.marktechpost.com/2026/11/20/nvidia-nemotron-labs-sigma-continuous-diffusion-language-model/

#NVIDIA #DiffusionModel #LLM #OpenWeights #TextGeneration #SpeculativeDecoding #AIInference #MachineLearning #GPU #DeepLearning
