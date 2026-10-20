---
title: MPS in PyTorch 2.15
source: HuggingFace Blog
url: https://huggingface.co/blog/mps-pytorch-2-15
model: claude-code/sonnet
generated_at: '2026-10-20T20:52:57.077108'
score: 88
---

📌 PyTorch 2.15：Mac 上的 MPS 後端，MoE 解碼快了 5 倍以上

TL;DR：PyTorch 2.15 讓 Mac 的 MPS 後端支援 FP8、原生 grouped matmul，MoE 解碼速度大增。

如果你曾經在 Mac 上跑 PyTorch 模型，卡在不支援的運算、效能斷崖或記憶體莫名暴增，Hugging Face 的 PyTorch 團隊這次直接把這些痛點一個個解決掉。

🤔 2026 年初，MPS 還是「能跑就好」的狀態

文中提到，2026 年初在 MPS 上跑模型，即便是小模型，也常常得繞過不支援的運算、忍受效能斷崖，以及應付預期外的記憶體成長。Hugging Face 的 PyTorch 團隊於是拿 Hugging Face Hub 上涵蓋語言、圖像、影片的真實模型，找出 MPS 表現不足的地方，並直接上游修進 PyTorch，愈來愈多時候是把 MPSGraph 換成專屬的 Metal kernel。PyTorch 2.15 就是這段工作的成果，和 PyTorch 核心維護者及社群貢獻者共同完成。

🧩 這次改了什麼：FP8、原生 grouped matmul、GEMV 連接 F.linear

PyTorch 2.15 讓 `torch.float8_e4m3fn` 張量能在 MPS 上使用，一個數值只佔一個位元組，是 FP16 或 BF16 儲存空間的一半，可以用 `F.scaled_mm` 直接在 GPU 上做量化矩陣乘法，支援 tensorwise 與 rowwise 兩種 scaling。範例：

```python
import torch
import torch.nn.functional as F

def quantize_fp8(x):
    limit = torch.finfo(torch.float8_e4m3fn).max
    scale = x.abs().amax().clamp_min(1e-12) / limit
    return (x / scale).to(torch.float8_e4m3fn), scale

x = torch.randn(1, 1024, device="mps", dtype=torch.float32)
weight = torch.randn(1024, 1024, device="mps", dtype=torch.float32)
x_fp8, x_scale = quantize_fp8(x)
w_fp8, w_scale = quantize_fp8(weight)
y = F.scaled_mm(x_fp8, w_fp8.t(), scale_a=x_scale, scale_recipe_a=F.ScalingType.TensorWise,
                 scale_b=w_scale, scale_recipe_b=F.ScalingType.TensorWise, output_dtype=torch.bfloat16)
```

在解碼階段，每個新 token 都是以單一行（row）通過模型，大矩陣乘法會退化成矩陣-向量乘法。過去 `F.linear` 仍走 MPSGraph 路徑，2.15 把它接上從 2.14 就有的 GEMV kernel，常見的 `[1, 1, hidden_size]` 解碼輸入可以直接套用，連帶融合偏置加法；文中指出在 96 種 BF16 層形狀的測試中，幾何平均提速 1.23 倍，小型投影層（例如 MoE 的 gate）受益最明顯。

針對 mixture-of-experts 層，2.15 為 grouped matmul 提供了原生實作：2.14 時，分組的 offset 要先複製到 CPU 再逐組迴圈處理；新的 Metal kernel 直接在 GPU 上讀取 offset，視情況使用 Metal Performance Primitives 或另一條 Metal 路徑，小分組（解碼時的常見情況）還有專屬 kernel。

📊 M3 Ultra 實測：MoE 解碼快 5 到 6.5 倍，影片 VAE 記憶體砍 97%

文中公布的具體數據：在 M3 Ultra 上搭配 `torch.compile`，Qwen3.6-35B-A3B 的解碼速度從 9.4 tokens/s 提升到 61.3 tokens/s，LFM2.5-8B-A1B 從 23.6 tokens/s 提升到 123.6 tokens/s；詞彙表上的 softmax 運算提速約 8 倍；Wan2.2 的 tiled VAE 解碼影片記憶體峰值從 270 GiB 降到約 8 GiB；另外，2.14 版本中 Qwen-Image-2.1 的 VAE 編碼器在 MPS 上會悄悄損壞影像，導致圖像編輯工作流出錯（曾在 ComfyUI 被回報），修正 padding 後，編碼解碼回合的 PSNR 從 10.06 dB 提升到 29.95 dB，與 CPU 結果一致。

線性代數方面，complex64 的 LU 分解、LU 求解與三角求解也已能在 MPS 上運行，連帶解鎖建立在這些運算上的梯度計算（如複數determinant）；4×4 以內的小矩陣求逆也整合進單一 Metal kernel。

⚠️ 使用前的版本要求

MPS 現在要求 macOS 15 以上，PyTorch 2.15 要求 Python 3.11 以上；若作業系統太舊或找不到 Metal GPU，MPS 的可用性檢查現在會明確告知原因。文中也預告，attention 完全搬上 Metal、更多 MPSGraph 遷移到 Metal，以及更快的 LLM 解碼，要等到 2.16 才會到位，代表目前仍有尚未搬完的運算路徑。

🎯 實務啟示

如果你用 transformers、diffusers 或 ComfyUI 在 Mac 上跑本地 LLM 或影片生成，升級到 PyTorch 2.15 能直接拿到 MoE 解碼加速與影片 VAE 記憶體下降的好處；若先前在 MPS 上遇到 Qwen-Image-2.1 編輯結果異常，這版本的 padding 修正值得優先驗證。

🔗 來源
- 標題：MPS in PyTorch 2.15
- 作者／機構：Irakli Salia、Khushi Agrawal（Hugging Face）
- 連結：https://huggingface.co/blog/mps-pytorch-2-15

#PyTorch #MPS #AppleSilicon #FP8 #MachineLearning #LLMInference #MoE #Metal #OnDeviceAI #DeepLearning
