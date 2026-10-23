---
title: Does Your Model Run on AWS Trainium? Look It Up
source: HuggingFace Blog
url: https://huggingface.co/blog/torch-neuronx-model-support
model: claude-code/sonnet
generated_at: '2026-10-23T20:50:59.804270'
score: 69
---

📌 你的模型能不能上 AWS Trainium？一個 Space 幫你查

TL;DR：Hugging Face 推出查詢工具，一鍵確認模型能否原生跑在 Trainium 上並附執行腳本。

部署模型到新硬體前，最怕的就是花了時間設定環境，最後才發現根本跑不起來。Hugging Face 在先前介紹過 TorchNeuron（torch-neuronx 套件）之後，這次直接把答案做成一個可查詢的 Space：torch-neuronx model support。

🤔 問題：Transformers 理論上都能跑，但實際上呢

有了 TorchNeuron，Transformers 可以在 AWS Trainium 上執行自己原生的建模程式碼，就像在其他裝置上一樣，理論上 Hub 上任何 Transformers 模型都能跑。但「理論上能跑」跟「實測真的能跑」是兩件事，這個 Space 要回答的正是後者，而且聚焦在 Hub 上最熱門的模型。

🧩 怎麼查、怎麼用

Space 預設開啟在 Selected 檢視，列出團隊自己從下載量與熱門分數挑出的代表性模型，每一列顯示結果、模型被切分（shard）到幾個 Trainium 核心、含編譯時間的總執行時間，以及裝置峰值記憶體。如果想查特定模型，可以切到 Trending 或 Downloads 檢視，這兩個檢視跟著 Hub 自己的排行榜走（依任務分類），輸入模型名稱的一部分即可查詢，不管該模型測過沒有。沒被測試到的模型，Space 也會說明原因，多數是「沒被排進優先順序」，少數才是「真的不相容」。使用者還能切換要查看的 Neuron 編譯器（neuronx-cc）與 Transformers 版本組合。

選定一個模型後，可以看到它實測所用的完整 Neuron 技術堆疊、需額外安裝的套件，以及實際執行的 run.py 腳本。腳本遵循 TorchNeuron 公告裡的作法：用 from_pretrained 載入模型（需要切分時就切分），再用 static cache 搭配 torch.compile(backend="neuron") 進行生成。在裝好對應堆疊的 Trainium2（trn2）執行環境（例如 AWS Neuron Deep Learning Container）上，裝好套件後執行 python3 run.py 即可，不需要 torchrun，因為模型切分時腳本會自己啟動對應的 torch.distributed rank。

第一次執行會先編譯模型的計算圖，如果想跳過這一步，可以直接從公開的 NEFF cache bucket 複製同一版編譯器產生的計算圖，Space 會給出對應編譯器版本的指令：hf buckets sync hf://buckets/aws-neuron/torch-neuronx-neff-cache/neuronxcc-<version> /tmp/neff_cache。

📊 「跑得動」具體代表什麼

每次測試都是在 trn2 執行環境上，用能容納模型權重的最少 Trainium 核心數來載入模型，多數模型用 tensor parallelism 切分，沒有 tensor-parallel 方案的 mixture-of-experts 模型則只用 expert parallelism。測試會生成 32 個 token 並檢查：單核心執行時，直接跟同一個 checkpoint 在 CPU 上的輸出比對；切分到多核心時，則改用一個小型的 judge model 檢查生成文字是否為流暢的英文。目前只測試能塞進 4 臺 Trainium2（也就是最多 16 核心）的模型，而且 PASS 只代表能正確生成，不代表吞吐量表現，也不代表更長序列生成時依然沒問題。

所有結果其實就是一份公開資料集 aws-neuron/torch-neuronx-model-support，每一組 neuronx-cc 與函式庫版本組合對應一個 Parquet 檔，每一列記錄模型結果、失敗時的錯誤訊息、完整堆疊版本與對應的 run.py。可以直接用 pandas 查詢，例如：

```python
import pandas as pd
df = pd.read_parquet("hf://datasets/aws-neuron/torch-neuronx-model-support/data")
df[df.model_id == "Qwen/Qwen3-0.6B"][["neuronx_cc", "library", "library_version", "neuron_cores", "result"]]
```

每個 result 欄位的確切定義則寫在資料集卡片裡。

⚠️ 目前只覆蓋一部分任務與模型規模

截至發文當下，只測試了 Transformers 模型，任務範圍限於 text-generation 與 image-text-to-image（image-text-to-text），diffusers、sentence transformers 等其他任務類型的覆蓋還在規劃中；模型規模也限制在能塞進 16 顆核心內，超出此範圍的模型目前沒有實測資料。

🎯 實務啟示

在投入時間最佳化部署前，先查一下這個 Space 能省掉不少試錯成本；如果模型已經測過，直接用公開 NEFF cache 跳過編譯步驟，也能讓第一次執行更快進入可用狀態。對於還沒被測試到的模型，Space 給出的「沒被優先測試」還是「真的不相容」的說明，也能幫忙判斷值不值得自己動手試。

🔗 來源
- 標題：Does Your Model Run on AWS Trainium? Look It Up
- 作者／機構：David Corvoysier（dacorvo），Hugging Face
- 連結：https://huggingface.co/blog/torch-neuronx-model-support

#AWSTrainium #HuggingFace #PyTorch #TorchNeuron #ModelDeployment #Transformers #MLOps #NeuronSDK #OpenSource #Inference
