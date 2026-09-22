---
title: Transformers now runs llama.cpp quants
source: HuggingFace Blog
url: https://huggingface.co/blog/transformers-llama-cpp-quants
model: claude-code/sonnet
generated_at: '2026-09-22T20:23:47.866872'
score: 105
---

📌 【HuggingFace】Transformers 直接讀 GGUF，免轉檔跑本地模型

TL;DR：transformers 現在能原生載入 llama.cpp 的 GGUF 量化模型，效能貼近原生引擎。

過去想在筆電跑本地大型語言模型，開發者得在 llama.cpp、Ollama、MLX 這些各自獨立的生態圈裡選一邊站。現在 Hugging Face 把這道牆打通了：直接把 GGUF 檔丟進 `from_pretrained`，就能用熟悉的 transformers API 生成文字。

🤔 **本地推論的痛點：格式各自為政**

llama.cpp 的推論引擎撐起了 Ollama、LM Studio、Jan 等一票本地 AI 工具，加上 MLX，讓本地推論成為日常可用的選項。GGUF 正是由 llama.cpp 團隊開發的格式，官方在 Hub 上以 ggml-org 身分釋出量化 checkpoint，Unsloth、LM Studio Community、bartowski 等發布者也提供多種量化版本，GGUF 模型的下載量已達數百萬次。但這些模型過去主要活在 llama.cpp 生態內，難以直接接上 transformers 慣用的工作流。

🧩 **怎麼接上的：重用 ggml kernels，而非重寫一套**

為了讓相容性不只是「能跑」而是「跑得舒服」，HuggingFace 團隊透過 kernels 函式庫重用 llama.cpp 底層的 ggml kernels，並降低 `generate` 過程中的額外開銷，藉此讓效能貼近 llama.cpp 原生表現。目前的重點是 Apple Silicon 上的本地推論，並先支援 Qwen3.5 架構。

GGUF 檔案把模型權重與 metadata（包含 tokenizer 資訊與可選的 chat template）打包成單一檔案，並支援不同量化等級。以 Q4_K_M 為例，多數權重壓到 4-bit，同時保留敏感 tensor 在較高精度，藉此在檔案大小與精度之間取得平衡。以 Unsloth 的 Qwen3.5-4B 為例：

| GGUF 版本 | 檔案大小 | 特性 |
|---|---|---|
| BF16 | 8.42 GB | 未量化參考版本 |
| Q6_K | 3.53 GB | 比小版本更高精度 |
| Q5_K_M | 3.14 GB | 大小與精度的折衷 |
| Q4_K_M | 2.74 GB | 本地推論的實用起點 |

官方建議從 Q4_K_M 開始嘗試，若記憶體充裕再往 Q5_K_M、Q6_K 調整；更激進的量化能讓更大模型塞進記憶體，但精度取捨因模型與任務而異，應該實際評估在你要跑的工作上。

🧩 **三行程式碼開始生成**

安裝需求包括 Apple Silicon Mac、相容的 PyTorch 版本，以及最新版 transformers（目前需裝 main 分支）與 kernels：

```
pip install -U "git+https://github.com/huggingface/transformers.git" kernels
```

載入時只需把 Hub 上的 `model_id` 與檔名以 `gguf_file` 參數傳入 `from_pretrained`，不需額外設定：

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "unsloth/Qwen3.5-4B-GGUF"
filename = "Qwen3.5-4B-Q4_K_M.gguf"

tokenizer = AutoTokenizer.from_pretrained(model_id, gguf_file=filename)
model = AutoModelForCausalLM.from_pretrained(model_id, gguf_file=filename)
```

當權重能保持打包狀態留在 Metal 上時，transformers 會自動載入相容的 ggml/Metal layer kernels，並以 `ggml-org/ggml-attn` 作為 attention 實作；若該 kernel 抓不到，就會 fallback 到 `sdpa` 並跳出警告，開發者也可以直接傳入 `attn_implementation="sdpa"` 強制指定。若沒有相容的量化 kernel，loader 會退回 dequantize 模型，記憶體用量會增加。

除了直接呼叫 API，也能用 `transformers serve` 開出 OpenAI 相容介面：

```
transformers serve "unsloth/Qwen3.5-4B-GGUF:Qwen3.5-4B-Q4_K_M.gguf"
```

`model` 參數用 `<model_id>:<filename>.gguf` 格式指定要載入哪個量化版本，接著就能用 Jan、Pi 等支援 OpenAI 相容 API 的客戶端，設定 Base URL 為 `http://localhost:8000/v1` 直接連上。

📊 **效能對比：跑分貼近 llama.cpp**

官方以三款 GGUF checkpoint（小型 dense 模型、較大 dense 模型、mixture-of-experts 模型）做基準測試，對照組是 llama.cpp 的 `llama-bench` 工具（build 5f55650a7，release b10200，Metal backend），測試機為 MacBook Pro M2 Max、32 GB 統一記憶體、macOS 26.6、PyTorch 2.12.1、kernels 0.17.0。文章指出，在這三個 checkpoint 上，transformers 的生成速度都非常接近 llama.cpp。

⚠️ **目前限制**

支援範圍還在起步階段：僅鎖定 Apple Silicon，架構上也只先覆蓋 Qwen3.5；缺少相容量化 kernel 時會退回 dequantize，記憶體用量隨之上升。

🎯 **實務啟示**

如果你已經在用 Unsloth、bartowski 等來源的 GGUF checkpoint，現在可以直接用 transformers 生態（`generate`、`transformers serve`）接手，不必在工具鏈之間切換；對已經熟悉 transformers API 的工程師來說，這是把本地推論納入既有 pipeline 的低成本路徑。

🔗 **來源**
- 標題：Transformers now runs llama.cpp quants
- 作者／機構：Marc Sun、Arthur Zucker、Lysandre @ HuggingFace
- 連結：https://huggingface.co/blog/transformers-llama-cpp-quants

#Transformers #GGUF #LlamaCpp #LocalInference #HuggingFace #Quantization #AppleSilicon #Qwen #OpenSource #MachineLearning
