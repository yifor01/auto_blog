---
title: Inkling-2-Mini in 5.4 GB Memory
source: Hacker News
url: https://github.com/ShinMegamiBoson/lookatmyquant
model: claude-code/sonnet
generated_at: '2026-11-22T22:36:09.377086'
score: 107
---

📌 開源量化壓縮工具，把53GB模型塞進7GB記憶體

TL;DR：LookAtMyQuant用逐權重誤差分析做量化，同檔案大小下精度大幅優於主流 GGUF。

模型瘦身這件事，業界常見做法是「每個權重都砍一樣多位元」。但 LookAtMyQuant 的思路反過來：先量出哪個權重砍下去最痛，再決定怎麼砍。

🤔 均勻量化的盲點：不是每個權重都一樣重要

LookAtMyQuant 是一套量化編譯器（quantization compiler），核心作法是逐一測量模型中每個被儲存的「片段」（權重區塊）在壓縮後對輸出造成多少傷害，再為每個片段挑選一種編碼方式，讓整個模型在固定的檔案大小預算內，把傷害降到最低。作者在 Gemma 4 E2B 上的測試顯示，同樣檔案大小下，LookAtMyQuant 產出的 GGUF 相較於常見的 Q4_K_M，KL 散度低了 12 倍，代表輸出分佈更貼近未壓縮的原始模型。整套程式碼採 MIT 授權開源。

🧩 核心配方：trellis 編碼、Fisher 資訊逐列分配、再蒸餾一輪

後續版本 LookAtMyQuant 2 把這套方法套用在 Qwen3.5-4B 上，壓到 1.23GB（每權重 2.3 bits）。公開的配方是：後訓練量化搭配 trellis 編碼，用模型自己生成的數學解題過程做校準資料，其中數字 token 的權重放大 10 倍；位元預算依 Fisher 資訊逐列（per-row）分配；接著進行 4,000 步蒸餾，每一層都從原始權重重新量化一次。整個流程的 GPU 成本公開為約 34 美元。

📊 和同量級對手比數學題、程式碼與知識測驗

在 540 題可驗證答案的數學題上，1.23GB 的 Qwen3.5-4B 解出 330 題；同檔案大小的 Prism ML Bonsai 2 Ternary 4B 解出 328 題，未壓縮原始模型解出 359 題。在保留文字（held-out text）上，LookAtMyQuant 的 KL 是 0.45 nats，Bonsai 是 0.59 nats。

同一套配方套用到 Qwen3.8-27B，把 53.7GB 壓到 7.2GB（2.1 bits/weight），校準與蒸餾資料換成英文文章、對話、程式碼與數學。結果是 540 題數學解出 401 題，和原始模型打平；同檔案大小的 Unsloth UD-IQ2_XXS GGUF 只解出 348 題。HumanEval（73.8% 對 67.1%）、MMLU（78.8% 對 75.0%）、GSM8K（94.5% 對 92.7%）三項都高於 Unsloth 版本。配合一個 1.02GB 的 4-bit DSpine 投機解碼草稿模型，Apple Silicon 上數學與程式碼任務的解碼速度大約可以翻倍。

最大手筆的實驗，是把 thinkingmachines/Inkling-2-Mini（26.4B 實體參數、5.4B 活躍參數的 3 倍迴圈 MoE 架構，128 專家 top-8）從 18.89GB 文字權重，壓成六個對應不同裝置的 Apple Silicon MLX 版本：3.85GB、4.72GB、5.38GB、8.87GB、11.18GB、12.76GB，分別對應 1.18 到 3.92 bits/weight。用到的技巧包括 4KB SRAM 雜湊區塊向量 trellis 編碼、列級 trellis 編碼、以 128 列為一組的 Fisher 離群值分配、針對 attention 投影層的專門位元下限，以及把最敏感的部分專家直接以原生 NVFP4 精度無損保留。

用 GSM8K（200 題）、完整 164 題 HumanEval、4 題視覺問答，以及 13 種語言的文字混合測試評分後，12.76GB 版本在所有基準上都和未壓縮的 BF16 教師模型打成平手（合計 349/349），記憶體卻省了 32.5%。11.18GB 與 8.87GB 兩個版本維持在 99.2%～99.3% 的三項任務平均分，8.87GB 版本在英文、對話、程式碼上的 KL 比同尺寸的 Unsloth UD-Q2_K_XL GGUF 低 2.34 倍。往更小尺寸走，5.38GB（1.65 bits）仍拿下 87% GSM8K、71.3% 嚴格版 HumanEval；3.85GB（1.18 bits，給 8GB iPhone 用）則從「靜態量化直接崩潰」（GSM8K 僅 1.0%）回升到 89.5% GSM8K、59.1% HumanEval。在 Apple M5 Max 上，各版本搭配投機解碼草稿模型後，解碼速度落在每秒 60～125 tokens 之間，依版本大小而異。

🧩 怎麼用：一行指令跑量化後的模型

在 Apple Silicon 上可直接安裝 runtime 套件：

pip install git+https://github.com/ShinMegamiBoson/lookatmyquant.git

從原始碼安裝則用 pip install -e . 取得 lamq 指令，或直接以 python -m runtime_mlx 執行。指令可以直接指向本機模型資料夾或 Hugging Face repo ID，例如：

lamq generate shinmegamiboson/Qwen3.8-27B-LookAtMyQuant-7.2GB -p "What is 17 times 23? Show the steps."

也支援搭配草稿模型加速解碼，以及互動式的 lamq chat 模式。

⚠️ 愈小愈省，代價也愈清楚

數據中有個明顯的 trade-off：bits per weight 一旦降到 2 以下，程式碼能力（HumanEval）下滑速度比數學能力快很多，像 3.85GB 版本的 HumanEval 只剩 59.1%，遠低於它的 GSM8K 表現。想把模型塞進 8GB 裝置，等於要先接受程式碼生成品質打折。

🎯 實務啟示

對需要在邊緣裝置（手機、筆電）部署大模型的工程師來說，這套工具提供了一條可重現、附完整成本與誤差數字的量化路線，而不只是一句「我們壓得更小」。評估量化方案時，與其只看檔案大小，KL 散度和具體任務分數（而非單一聚合分數）才是判斷「壓縮有沒有傷到關鍵能力」的更可靠依據。

🔗 來源
- 標題：Inkling-2-Mini in 5.4 GB Memory
- 連結：https://github.com/ShinMegamiBoson/lookatmyquant

#Quantization #LLM #MLX #AppleSilicon #OpenSource #ModelCompression #EdgeAI #Qwen #Distillation #OnDeviceInference
