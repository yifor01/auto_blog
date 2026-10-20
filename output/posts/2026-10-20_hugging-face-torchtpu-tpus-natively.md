---
title: 'Hugging Face ❤️ TorchTPU: TPUs, Natively'
source: HuggingFace Blog
url: https://huggingface.co/blog/hf-torchtpu
model: claude-code/sonnet
generated_at: '2026-10-20T20:44:32.554937'
score: 103
---

📌 PyTorch 終於原生支援 TPU，免 XLA 痛點

TL;DR：Hugging Face 推出 TorchTPU 整合，Transformers、Diffusers 現在能直接把模型送上 TPU 跑。

如果你曾經想在 TPU 上跑 PyTorch，大概不是把程式碼移植到 torch_xla，就是乾脆跑去學 JAX。這個「軟體門檻比硬體門檻還高」的老問題，隨著 TorchTPU 的出現，終於有了不同的解法。

🤔 **TPU 的硬體很強，軟體一直很麻煩**

TPU（Tensor Processing Unit）是 Google 專為神經網路矩陣運算設計的加速晶片，Google 已經開發了大約十年，用來訓練與服務自家模型（包括 Gemini），在 Google Cloud 上可以從單顆晶片一路擴展到數千顆的 pod。但 TPU 軟體堆疊是跟著 TensorFlow 與 JAX 一起長大的，PyTorch 使用者過去得透過 PyTorch/XLA（torch_xla）才能用上 TPU：張量是 lazy 的（意思是它很懶，不是你很懶），程式碼不一定在你以為的時間點執行，一點小改動就可能觸發 graph 重新編譯，除錯也很難推理。Hugging Face 先前推出的 Optimum TPU 是為了緩解這個痛點，但現在有了 TorchTPU 原生支援，Optimum TPU 已不再是跑 Hugging Face 模型所必需。

🧩 **TorchTPU：把 TPU 變成 PyTorch 的另一個裝置**

TorchTPU 為 PyTorch 新增了 TPU 作為原生 backend，寫法就是一般 PyTorch 程式碼。它內建針對 TPU 調校過的 Pallas kernels、支援分散式訓練，也整合了 torch.compile 以取得更高效能。安裝在 TPU VM 上只需一行指令：

```
pip install torch-tpu --extra-index-url https://download.pytorch.org/whl/cpu
```

額外的 index 是為了拉取 CPU 版本的 torch，避免在 TPU 上還裝進完全用不到的 CUDA build。

📊 **Transformers、Diffusers、Kernels 全部原生可用**

在 Transformers v5 裡，只要把 device_map 設成 "tpu" 就能直接把模型載到 TPU 上：

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
model_id = "Qwen/Qwen3.5-9B"
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="tpu")
tokenizer = AutoTokenizer.from_pretrained(model_id)
inputs = tokenizer("The future of AI is", return_tensors="pt").to("tpu")
out = model.generate(**inputs, max_new_tokens=64)
```

模型預設以 eager mode 執行，也可以搭配 torch.compile 或分散式設定取得更好效能。Diffusers 這邊，TPU 同樣是一級裝置：原型階段用 pipe.to("tpu") 即可，要部署時再加一行 compile 呼叫；對於單張晶片裝不下的大模型，傳入 TensorParallelConfig 就能在載入時把 transformer 切分到多顆晶片上，文章提到多數熱門 pipeline 已原生支援，其餘的只需補上一個 tp_plan。Kernels Hub 上也已經有現成的 TPU kernel，用 Pallas 寫成，文章示範了把 Tokamax 的 ragged-dot kernel 接進 MoE 模型，在 batch size 64 時，Qwen3-30B-A3B 的解碼速度提升了 21.5 倍，Gemma 4 26B-A4B 提升了 12.8 倍（在 Cloud TPU v6e-8 上測試，相較預設實作）。

⚠️ **還在打磨中，但問題被主動找出來**

Hugging Face 持續在 TPU 上跑 Transformers 的測試套件，目前有跑在 TPU 上的測試中，96.5% 通過；團隊已經回報了 34 個 issue 到 TorchTPU repo，其中 19 個已修復。這個過程也順帶在 Transformers 本身抓出一些 bug，例如 StaticCache 與 Qwen3 的 tensor-parallel plan，這些都已在上游修正。文章也坦言「還沒有全綠」，代表目前仍是持續改進中的狀態，而非完全成熟的生產方案。

🎯 **實務啟示**

如果團隊過去因為 torch_xla 的 lazy tensor 與重新編譯問題而對 TPU 望而卻步，TorchTPU 加上 Hugging Face 生態系的原生整合，讓「從 Hub 挑一個模型、送到 TPU」變成跟用 GPU 幾乎一樣簡單的事。但考量目前仍在持續修 bug 的階段，上生產前建議先針對自己實際用到的模型與 pipeline 跑過一輪驗證，而不是直接假設所有功能都已穩定。

🔗 **來源**
- 標題：Hugging Face ❤️ TorchTPU: TPUs, Natively
- 作者／機構：Hugging Face（Alvaro Moran、Jingya Huang、Simon Pagezy、Jeff Boudier、Régis Pierrard）
- 連結：https://huggingface.co/blog/hf-torchtpu

#PyTorch #TPU #HuggingFace #Transformers #Diffusers #GoogleCloud #DeepLearning #ModelServing #Pallas #MachineLearningInfra
