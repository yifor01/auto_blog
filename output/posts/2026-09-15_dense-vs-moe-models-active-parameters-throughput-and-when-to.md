---
title: 'Dense vs. MoE Models: Active Parameters, Throughput, and When to Choose Each'
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/dense-vs-moe-models-active-parameters-throughput-and-when-to-choose-each/
model: claude-code/sonnet
generated_at: '2026-09-15T20:39:55.167842'
score: 82
---

📌 30B 模型只點亮 3B 參數，Dense 與 MoE 該怎麼選？

TL;DR：參數量相同時，架構決定的是吞吐量與記憶體成本，而非單純的能力上限。

一個 30B 參數的模型，如何在每個 token 只動用 3B 參數的情況下，還能享有大模型的容量優勢？NVIDIA Developer 部落格用 Nemotron 3.5 Lightning 這個例子,說明了 Dense 與 Mixture-of-Experts（MoE）兩種架構的根本差異：怎麼組織參數，和參數量本身一樣重要。

🧩 **兩種引擎：全缸點火 vs 選擇性點火**

Dense 模型的每一層 decoder 都只有一個共享的 feed-forward network（FFN）區塊，每個 token 通過時都會啟動全部參數。MoE 模型則把這個單一 FFN 換成多個 FFN 區塊（也就是所謂的「專家」，數量可能是 8、64 甚至 128 個），並在前面加上一個學習出來的 router network，為每個 token 挑選 top-k 個分數最高的專家來運算，其餘專家則被跳過。多數現代 MoE（如 Mistral Small 4）還會保留一個「共享專家」，讓每個 token 無論如何都會經過。

值得注意的是，這裡的路由決策是逐層獨立進行的，token 並不會被分配到某個專家後就固定不變，而是在每一層依據當下的表徵重新路由。這些專家也不是傳統意義上的「主題專家」，其分工主要落在語法與 token 類型模式（如標點符號、數字等），但這會因架構與訓練方式而異。無論路由怎麼跳過 FFN，token 依然會完整通過 attention 機制。因此模型卡上寫的「3B active parameters」，其實包含每個 token 都會用到的 attention 與 embedding 權重，再加上被選中的 FFN 權重。

此外還有變體存在，例如 Nemotron 3.5 Lightning 採用的是 Mamba-2 + MoE + Attention 混合架構：多數層以 Mamba-2 取代 attention，用固定大小的循環狀態取代不斷成長的 KV cache，這在長上下文情境下帶來的記憶體效益,是單純稀疏化無法達到的。

📊 **實測數據：速度差距懸殊**

以下是 NVIDIA Developer 引用 Artificial Analysis 的資料（10K token 輸入，2026 年 8 月 31 日擷取）：

| 模型 | 架構 | 總參數 | 啟用參數 | VRAM（原生） | VRAM（4-bit） | AA 智慧指數 | 輸出速度 | 每百萬輸出 token 價格 |
|---|---|---|---|---|---|---|---|---|
| Gemma 4 31B | Dense；多模態 | 31B | 31B | ~61 GB BF16（1×H100） | ~16 GB | 30 | 36.9–222.4 t/s | $0.40 |
| Qwen3.8-27B | Dense；混合線性／全 attention；MTP head；多模態 | 27B | 27B | ~56 GB BF16（1×H100） | ~14 GB | 52 | 46.8 t/s | $3.00 |
| Nemotron 3.5 Lightning | MoE + Mamba-2 attention 混合 | 30B | 3B | ~60 GB BF16（1×H100） | ~20 GB | 24 | 235.7–494.2 t/s | $0.22 |
| Mistral Small 4 | MoE；多模態 | 119B | 6B（含 embedding 為 8B） | ~121 GB FP8（4×H100） | ~71 GB | 20 | 147.3 t/s | $0.60 |

從 Gemma 4 31B 與 Nemotron 3.5 Lightning 這組總參數相近的比較就能看出稀疏化的效果：兩者的輸出速度區間完全沒有重疊，啟用 3B 參數是主因之一，但 Lightning 的 Mamba-2 層與推測性解碼（speculative decoding）也各自貢獻了一部分。

💡 **記憶體看總參數，速度看啟用參數**

兩種架構最關鍵的差異在於：Dense 模型的托管成本與運算成本是綁在一起的，而 MoE 把兩者解耦了。MoE 模型的所有專家都必須常駐在 GPU 記憶體中（VRAM 成本按總參數計），但運算成本只隨實際啟用的專家數量而變（FLOPs 按啟用參數計）。閒置的專家不消耗運算資源,卻仍佔用記憶體,這就是 MoE 把「每 token 可變運算」換成「固定記憶體開銷」的核心取捨。

在 batch size 為 1 的情境下，解碼主要受限於記憶體頻寬而非運算量，這正是 MoE 的優勢所在,因為它每個 token 讀取的權重位元組更少。隨著 batch size 增加，token 集合會逐漸用到網路中大部分的專家，這項優勢會隨之收斂，但每個 token 運算量降低的效益依然存在。也因此，MoE 在各種 batch size 下大致都保有吞吐量優勢，但相較於最佳化良好的 Dense 模型，其延遲優勢會在高併發時被壓縮。此外，由於所有專家都得同時常駐 GPU 記憶體，MoE 留給 KV cache 的空間也會比同等規模的 Dense 模型更少。

🎯 **怎麼選：看你的部署限制，不是看參數量**

記憶體預算取決於總參數量而非啟用參數量，因此一個 30B 的 MoE 模型和一個 30B 的 Dense 模型,吃的 VRAM 大致相同。真正的問題是：同樣的記憶體,你想換成什麼——Dense 把它轉換成能力，MoE 把它轉換成吞吐量。以 Lightning 與 Qwen3.8-27B 為例，前者輸出速度是後者的四到五倍、價格卻只要十四分之一，但通用能力指數不到後者的一半。這適合大量執行明確步驟的 agentic 執行層，卻不適合單次困難推理就決定成敗的場景。

🔗 **來源**
- 標題：Dense vs. MoE Models: Active Parameters, Throughput, and When to Choose Each
- 作者／機構：Elizabeth Goodman（NVIDIA Developer）
- 連結：https://developer.nvidia.com/blog/dense-vs-moe-models-active-parameters-throughput-and-when-to-choose-each/

#MixtureOfExperts #DenseModels #LLMInference #ModelArchitecture #NVIDIA #GPUInference #ModelServing #Nemotron #AIInfrastructure #MachineLearning
