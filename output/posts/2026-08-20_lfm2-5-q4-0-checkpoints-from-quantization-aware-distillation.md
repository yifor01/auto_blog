---
title: LFM2.5 Q4\_0 Checkpoints from Quantization-Aware Distillation
source: HuggingFace Blog
url: https://huggingface.co/blog/LiquidAI/qad
model: claude-code/sonnet
generated_at: '2026-08-20T06:33:31.096265'
score: 87
---

📌 4-bit 量化不再掉分：LiquidAI 用 QAD 找回 97% 的 BF16 精度

TL;DR：Liquid AI 釋出以 Quantization-Aware Distillation 訓練的 LFM2.5 系列 Q4_0 GGUF，記憶體與速度不變，精度損失大幅回補。

模型量化到 4-bit 通常意味著要在記憶體、速度與準確度之間妥協，一般的 post-training quantization（PTQ）會讓精度明顯掉分。Liquid AI 這次釋出的 QAD Q4_0 checkpoints，想在不犧牲 Q4_0 原本記憶體與速度優勢的前提下，把這段損失的精度找回來。

🤔 PTQ 量化的老問題

一般 Q4_0 GGUF 是用 post-training quantization 直接把高精度權重壓成 4-bit，速度與記憶體佔用都很吸引人，但相較 BF16 全精度版本，準確度會有明顯落差。Liquid AI 這次針對 LFM2.5-230M、LFM2.5-350M、LFM2.5-1.2B-Instruct、LFM2.5-2.6B 四個模型，重新釋出用不同訓練方式產生的 4-bit checkpoint。

🧩 用「高精度老師教量化學生」的方式訓練

這次的方法是 Quantization-Aware Distillation（QAD）：用一個高精度的 teacher model，把知識蒸餾（distill）進一個量化後的 student model，而不是先訓練好再單純做後製量化。產出的 checkpoint 維持與原生 Q4_0 GGUF 相同的記憶體佔用與運算速度，等於是在同樣的硬體成本下，換來更接近全精度的表現。

📊 四個模型都拿回九成六以上的 BF16 準確度

Liquid AI 用涵蓋推理、指令遵循、工具呼叫與 agentic 能力的評測組合來比較：GPQA Diamond、MMLU-Pro、IFEval、IFBench、Multi-IF、BFCLv4，並依模型規模加測一項數學題，230M 與 350M 用 GSM8K，1.2B-Instruct 與 2.6B 用 AIME25，所有分數取五次重複的平均值，以 BF16 GGUF 作為同格式下的精度上限。

| 模型 | QAD Q4_0 保留 BF16 精度比例 |
|---|---|
| LFM2.5-230M | 97.1% |
| LFM2.5-350M | 96.5% |
| LFM2.5-1.2B-Instruct | 97.4% |
| LFM2.5-2.6B | 96.6% |

在 MacBook Pro、NucBox EVO-X2（皆為 GPU 推論）以及 Samsung Galaxy S26 Ultra、Raspberry Pi 5（皆為 Arm CPU 推論）四種真實邊緣裝置上，230M 與 350M 的 QAD Q4_0 checkpoint 在解碼吞吐量上比對應的 Q5_K_M 高出 4% 到 33%，同時精度落在評測誤差範圍內視為相當；1.2B 與 2.6B 的 QAD Q4_0 則比 Q4_K_M 高出 3% 到 14% 的吞吐量，精度同樣相當。在 230M 與 1.2B 這兩個有對照組的規模上，QAD Q4_0 的精度也與 Unsloth 的 UD-Q4_K_XL（一個強力的外部 PTQ checkpoint）相當。

💡 拿到就能直接用 llama.cpp 跑

這些 checkpoint 是標準 GGUF Q4_0 格式，可以搭配 llama.cpp 或任何支援 GGUF Q4_0 的 runtime 直接使用，例如：

```
llama-cli -hf LiquidAI/LFM2.5-350M \
  --hf-file LFM2.5-350M-QAD-Q4_0.gguf \
  -p "What is C. elegans?"
```

🎯 對邊緣部署工程師的意義

如果你的部署場景本來就鎖定 Q4_0（受限於記憶體或延遲），這批 QAD checkpoint 幾乎是零成本的升級：不用換更大的量化格式、不用犧牲吞吐量，就能把精度拉到接近 BF16 的水準。四個尺寸（230M 到 2.6B）都已在 Hugging Face 上架，適合直接替換現有的 Q4_0 部署。

🔗 來源
- 標題：LFM2.5 Q4_0 Checkpoints from Quantization-Aware Distillation
- 作者／機構：Aditya Tadimeti、Leonie Monigatti，Liquid AI（HuggingFace Blog）
- 連結：https://huggingface.co/blog/LiquidAI/qad

#Quantization #EdgeAI #GGUF #LLM #LiquidAI #ModelCompression #Distillation #OnDeviceAI #llamacpp #OpenSourceAI
