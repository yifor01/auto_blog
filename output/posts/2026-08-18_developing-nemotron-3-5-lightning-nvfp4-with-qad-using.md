---
title: Developing Nemotron 3.5 Lightning NVFP4 with QAD Using NVIDIA Model Optimizer
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/developing-nemotron-3-5-lightning-nvfp4-with-qad-using-nvidia-model-optimizer/
model: claude-code/sonnet
generated_at: '2026-08-18T06:25:31.497624'
score: 98
---

📌 壓到 22GB、吞吐量衝 4 倍：Nemotron 3.5 Lightning 的 NVFP4 量化蒸餾實戰

TL;DR：NVIDIA 用量化感知蒸餾把 Nemotron 3.5 Lightning 壓成 NVFP4，準確度損失有限，吞吐量大幅提升。

把模型壓到 4-bit 通常意味著犧牲準確度換取速度，但如果只做訓練後量化，能榨出的效能終究有限。NVIDIA 這篇文章示範了如何用量化感知蒸餾（quantization-aware distillation，QAD），在更激進的量化設定下，把準確度損失補回來。

🤔 **PTQ 不夠用時的下一步**

NVIDIA Nemotron 系列讓開發者能依延遲、速度、記憶體與運算需求挑選合適大小的模型。新推出的 Nemotron 3.5 Lightning NVFP4 checkpoint，把原本 66 GB 的全精度 checkpoint 壓縮到 22 GB，同時把吞吐量最高提升到 4 倍。訓練後量化（PTQ）是壓縮到 NVFP4 最常見的方法，能滿足大多數需求；但如果目標是在更緊的記憶體限制下衝更高吞吐量，就需要更激進的量化，這時 QAD 是比較合適的選擇。

🧩 **兩階段流程：先 PTQ，再蒸餾**

QAD 的做法是用原始全精度模型當老師，教量化後的學生模型。第一階段先對全精度模型跑 PTQ，產生一個量化後的學生模型；第二階段再用凍結的 BF16 教師模型，透過比較教師與學生 logits 的 KL 散度損失，對學生模型做蒸餾。訓練過程中，學生模型的每一次前向傳播都會經過模擬量化，讓模型提前適應推論時會遇到的量化雜訊，同時透過蒸餾損失學習重現教師模型的完整行為，而不只是預測下一個 token。

因為後面還有 QAD 能把準確度補回來，PTQ 階段可以量化得更激進。針對 Nemotron 3.5 Lightning，團隊發現把 Mamba 線性層量化到更激進的 W4A16，而不是較保守的 FP8，能在準確度沒有大幅下滑的前提下解鎖更高吞吐量。單純只做 PTQ 時，一般會以 99% 以上的中位準確度回復率為目標；但搭配 QAD 之後，PTQ 階段的目標可以放寬到 95%-99%，因為後續的 QAD 會把差距補回來，這也代表量化已經被推得夠激進，足以換取尺寸與延遲的收益。

🧩 **五種 PTQ 配方的取捨**

作為老師的基礎模型是 NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16，學生模型則以同一個基礎模型跑 PTQ 產生。團隊測試了多種 PTQ 配方，差異在於權重校準方式，以及 Mamba 投影層與 KV 快取的量化激進程度：max-calibrated 配方對應訓練階段的動態縮放（dynamic scale）QAD，MSE-based 配方則對應固定縮放（frozen-scale）QAD。所有配方都把 lm_head 量化到 W4A16，attention 投影層則維持 BF16，校準使用 1,000 筆樣本，在單臺 NVIDIA DGX B300 上執行。

其中最激進的 four_over_six 加 NVFP4 KV 配方，把 K 和 V 都量化到 NVFP4（W4A4），QK 轉置與 attn 乘 V 的矩陣乘法維持 BF16，Q 則不量化。團隊也測試了 8k 到 128k 不等的校準序列長度，發現通常序列越長 PTQ 結果越好，其中 32K 序列長度在 four_over_six 配方上表現最佳，因此所有 QAD 實驗都基於這個 32K 校準的 four_over_six checkpoint 進行。綜合評估後，team 認為採用 W4A16 Mamba 線性層的 four_over_six 配方，在準確度下降與推論效能提升之間取得了最好的平衡。

🎯 **實務啟示**

這篇文章示範的流程可以透過 NVIDIA Model Optimizer 在自己的模型上重現，Hugging Face 上也提供了對應的 PTQ 範例程式碼。對於已經在用 Nemotron 系列、又想在有限顯卡記憶體下衝高吞吐量的團隊，這套「先用 PTQ 激進量化、再用 QAD 補回準確度」的兩階段思路，是一個值得直接套用的量化策略範本，尤其是 Mamba 線性層與 KV 快取的量化選擇，值得對照自己模型的架構做調整。

🔗 **來源**
- 標題：Developing Nemotron 3.5 Lightning NVFP4 with QAD Using NVIDIA Model Optimizer
- 作者／機構：Tanya Lenz, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/developing-nemotron-3-5-lightning-nvfp4-with-qad-using-nvidia-model-optimizer/

#NVIDIA #Nemotron #Quantization #NVFP4 #ModelOptimizer #KnowledgeDistillation #LLMInference #EdgeAI #DeepLearning #ModelCompression
