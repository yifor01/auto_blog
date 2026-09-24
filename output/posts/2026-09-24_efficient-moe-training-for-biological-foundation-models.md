---
title: Efficient MoE Training for Biological Foundation Models
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/efficient-moe-training-for-biological-foundation-models/
model: claude-code/sonnet
generated_at: '2026-09-24T20:38:55.116362'
score: 98
---

📌 NVIDIA 實測：Transformer Engine 讓 MoE 訓練快 2.21 倍

TL;DR：BioNeMo MoE recipe 用 GroupedLinear、MXFP8、融合核心解決 MoE 訓練三大瓶頸，B200 上實測吞吐最高提升 2.21 倍。

Mixture-of-experts（MoE）架構被寄望能用更低的計算成本擴大模型容量，但「理論上更省」和「實際上更快」之間，往往隔著一堆破碎的 kernel 呼叫、通訊開銷與記憶體壓力。NVIDIA 在這篇教學中，示範如何用 Transformer Engine（TE）把 BioNeMo 生物基礎模型的 MoE 訓練，從理論效益兌現成實測加速。

🤔 MoE 擴展的三個工程瓶頸

在 dense transformer 裡，每個 token 都要經過每一層，容量增加直接等於計算量增加。MoE 改用多個子網路（專家），每個 token 只啟用其中一小部分，理論上能更有效率地擴展模型容量。但這個優勢高度依賴實作品質：破碎的專家運算會拉低 GPU 使用率，路由本身帶來通訊開銷，更大的參數量也讓記憶體與分散式訓練變得更棘手。NVIDIA Transformer Engine 針對這些瓶頸提供了最佳化的 primitive：分組專家運算、kernel 融合，以及低精度訓練。

🧩 挑戰一：破碎的專家 kernel

以 Hugging Face 的基準實作為例，它用 Python 迴圈逐一走訪每個專家，每個專家各自觸發獨立的 kernel 啟動：

```python
for expert_idx, expert_layer in enumerate(self.experts):
    idx, top_x = torch.where(expert_mask[expert_idx])
    current_state = hidden_states[None, top_x].reshape(-1, hidden_dim)
    current_hidden = expert_layer(current_state) * routing_weights[top_x, idx, None]
    final_hidden_states.index_add_(0, top_x, current_hidden)
```

TE 的 GroupedLinear 改用「分組執行」：保留每個專家各自的權重矩陣，但把工作一次提交。因為每個專家收到的 token 數量不同，GroupedLinear 額外接受一個 `split_sizes` 參數，把各個 local expert 送進 TE 的 grouped GEMM 路徑，而不是為每個專家各自呼叫一次 PyTorch Linear，藉此減少啟動與排程開銷：

```python
from transformer_engine.pytorch.ops import GroupedLinear

experts_gate_up = GroupedLinear(
    num_groups=num_local_experts,
    in_features=hidden_size,
    out_features=2 * intermediate_size,
    bias=False,
    dtype=torch.bfloat16,
    device="cuda",
)
gate_up_output = experts_gate_up(tokens, split_sizes)
```

Hugging Face Transformers 也提供了 `grouped_mm`，但 TE 能更進一步，把 GroupedLinear 與 MXFP8 量化、activation、路由權重縮放、中間資料搬移一起融合成單一的 GroupedMLP kernel。

🧩 挑戰二：模型體積與 activation 記憶體壓力

MoE 架構會拉高總參數容量，而基因體學這類工作負載常需要長序列，兩者疊加對訓練期間的 activation 記憶體造成壓力。BF16 每個權重與 activation 用 16 位元表示；BioNeMo recipe 透過 TE 支援 FP8 與 MXFP8 訓練，兩者都改用 8 位元表示數值。FP8 與 MXFP8 的主要差異在於縮放粒度：MXFP8 為每 32 個連續數值指定一個縮放因子，有助於保留數值範圍與精度。在 NVIDIA Blackwell GPU 上，MXFP8 有硬體加速，可以用專屬的 Tensor Core 指令執行 MXFP8 GEMM。

🧩 挑戰三：低精度訓練的量化開銷

即使大部分訓練運算用 8 位元精度，模型仍需保留 16 位元的主權重（master weights），訓練框架因此得在格式間插入量化與反量化步驟：量化把 BF16 的權重與 activation 轉成 MXFP8 供低精度 GEMM 使用，反量化再把結果轉回較高精度。若這些步驟各自獨立執行，會產生額外開銷，這正是融合 MLP 路徑要解決的問題：

```python
fp8_recipe = te_recipe.MXFP8BlockScaling()
model = TEMixtralMXFP8ForCausalLM(config, fp8_recipe=fp8_recipe, dispatcher=dispatcher)
```

TE 的 autocast API 讓模型的前向與反向傳播都以 MXFP8 精度執行：

```python
with te.autocast(enabled=True, recipe=self._fp8_recipe):
    for decoder_layer in self.layers:
        hidden_states = decoder_layer(hidden_states)
```

要使用融合版 MLP，可以透過 TE 的 Sequential API 把 `GroupedLinear`、`ScaledSwiGLU`、`GroupedLinear` 串接起來，`ScaledSwiGLU` 會把路由機率（scales）與專家 FFN 運算結合在一起：

```python
from transformer_engine.pytorch.ops import GroupedLinear, ScaledSwiGLU, Sequential

experts_ffn = Sequential(GroupedLinear(gate_up), ScaledSwiGLU(), GroupedLinear(down))
```

Sequential API 會掃描這串操作，一旦模式匹配，就把 `GroupedLinear → ScaledSwiGLU → GroupedLinear` 整段替換成融合的運算物件（前向為 `ForwardGroupedMLP_CuTeGEMMSwiGLU_MXFP8`，並搭配對應的融合反向運算），減少框架開銷，並避免產生部分中間結果。

📊 8 張 B200 上實測快 2.21 倍

在 8 張 NVIDIA B200 Tensor Core GPU 上，針對 Mixtral-8x7B 的訓練基準測試顯示，這套 recipe 的吞吐量最高可達 Hugging Face 基準實作的 2.21 倍。

🎯 實務啟示

想要驗證環境是否設好，可以先用 2 GPU 的 sanity 設定：

```
torchrun --nproc_per_node=2 train_fsdp2_ep.py --config-name L0_sanity
```

確認無誤後，再擴展到 8 GPU、EP=8、MXFP8 精度的 Mixtral-8x7B 設定：

```
torchrun --nproc_per_node=8 train_fsdp2_ep.py --config-name L1_8x7B_ep checkpoint.ckpt_dir=/path/to/ckpt
```

要注意的是，融合的 MXFP8 GroupedMLP kernel 需要 Blackwell GPU 才能使用；選擇 BF16 或 MXFP8 應依自身 GPU 與記憶體條件決定，並確保 data-parallel 與 expert-parallel 大小的乘積等於總 GPU 數。對於正在訓練或打算訓練 MoE 架構基礎模型（不限生物領域）的團隊，這套 recipe 提供了一個可直接參考、已驗證過吞吐提升的工程範本。

🔗 來源
- 標題：Efficient MoE Training for Biological Foundation Models
- 作者／機構：Michelle Horton，NVIDIA
- 連結：https://developer.nvidia.com/blog/efficient-moe-training-for-biological-foundation-models/

#MoE #NVIDIA #TransformerEngine #MXFP8 #BioNeMo #DistributedTraining #GPUOptimization #FP8 #ModelTraining #Blackwell
