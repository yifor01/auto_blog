---
title: '180B Parameters, 32GB of RAM: Pushing MoE Inference to the Limit with Transformers'
source: HuggingFace Blog
url: https://huggingface.co/blog/moe-expert-streaming
model: claude-code/sonnet
generated_at: '2026-11-18T23:40:16.752826'
score: 98
---

📌 32GB 記憶體跑 180B 參數模型:把 MoE 專家直接從 SSD 串流出來

TL;DR:Hugging Face 工程師實測把 MoE 模型的專家權重直接從硬碟串流進記憶體,效能達到專用引擎 Strata 的 94%,讓 32GB 筆電也能跑 180B 模型。

一顆 180B 參數的模型,要塞進 32GB 記憶體的 MacBook 裡,聽起來違反常識。但這篇文章的作者 Tarek Ziadé 用自己的實驗證明:只要抓對「哪些權重該放哪裡」,這件事是可行的,只是還不夠快。

🤔 **為什麼現有的 offload 方案都不夠用**

作者先比較了三套主流引擎在 MoE 模型跑不進記憶體時的做法。llama.cpp 用 mmap 映射 GGUF 檔案,可以把專家留在 CPU 上計算(`--cpu-moe`、`--n-cpu-moe N` 等參數),只有 activation 會跨 PCIe,專家權重本身不移動,前提是專家要塞得進 RAM,否則 page cache 會開始抖動。vLLM 的 `--cpu-offload-gb` 把部分權重釘選在 RAM,但沒有快取機制,熱門專家每個 token 都要重新跨 PCIe 讀取一次,也沒有磁碟層。Transformers 透過 Accelerate 做 offload,則是整個專家庫(expert bank)一次性搬到 GPU,即使只用到 8、10 個專家,也要把整層所有專家都複製過去,完全沒有路由概念——而且在 Mac 上,CPU 與 GPU 共享同一塊記憶體,所謂「offload 到 CPU」根本沒有釋放任何東西。

作者在一張 A10G(24GB)上實測 Qwen3.6-35B-A3B,結果差距驚人:

| 引擎 | Decode 速度(tok/s) |
|---|---|
| Strata, Q8_0 | 82–88 |
| llama.cpp, Q8_0, `--fit on` | 63–64 |
| llama.cpp, BF16, `--fit on` | 35–36 |
| vLLM, FP8, cpu-offload-gb 16 + experts | 20.1 |
| vLLM, FP8, 同上 + `--enforce-eager` | 14.7 |
| vLLM, FP8, cpu-offload-gb 16(無 experts 限定) | 9.7 |
| vLLM, BF16, cpu-offload-gb 50 + experts | 7.3 |
| vLLM, BF16, cpu-offload-gb 50 | 3.3 |
| Transformers + Accelerate | 0.16 |

只 offload 專家就能讓 vLLM 速度翻倍,FP8 量化又能再疊加一層效益。而 Transformers 預設的做法,慢到幾乎不可用。

🧩 **把快取做成「slot pool」,讓 grouped_mm 繼續可用**

作者決定直接修 Transformers 的 offload 邏輯。關鍵想法是把快取改造成一個 slot pool:預先配置一塊裝置端的張量,所有層共用,再用一個「專家 ID → slot」的對照表,把 router 選出的專家 ID 重新映射到 slot 上。這樣快取池看起來就像一般的專家庫,原生的 `grouped_mm` 核心可以直接套用,不需要寫自訂的矩陣乘法核心。

先在能完整放進記憶體的 OLMoE-1B-7B 上驗證:第一版(磁碟專家 + LRU 快取 + Python 逐個跑專家迴圈)只有 10.1 tok/s,原生版本是 32 tok/s 左右。改用 slot pool 後提升到 34.6 tok/s,逼近原生的 38.1 tok/s。

這個功能後來變成 `from_pretrained` 的選項 `experts_offload`,對應到 Transformers 的 PR #50717。被 offload 到磁碟的專家,讀取由 8 個 I/O 執行緒處理,每個專家對應一次連續讀取;接下來兩層的 router 會提早在目前的 hidden states 上跑一次,預測下一步會用到哪些專家,提前預取。

📊 **真正的目標:Qwen3.8-Flash-Next 跑進 32GB Mac**

Qwen3.8-Flash-Next 有 48 層、每層 512 個專家(啟用 10 個),FP8 下共 121GB,另外還有一張 51GB 的 n-gram embedding table,同樣需要走磁碟路徑。最終配置是:

- 專家量化到 3-bit:磁碟上 49GB,裝置端快取 12GiB
- 密集層用 8-bit(約 5.4GB,相較 BF16 困惑度只多 0.2%)
- n-gram table 留在磁碟,按需讀取對應的行

轉換過程約需 5 小時。模型載入後約用 18GiB,處理 6K 長度的 prompt 時記憶體峰值為 25.4GiB。整體 token 生成速度落在 Strata 的 6% 以內。

⚠️ **還在討論中的 API,以及尚未解決的速度差距**

這套 `device_map` 的 API 形式仍在和 Transformers 維護者討論,量化專家的部分之後可能會改用更通用的 per-layer 量化方案(對應 PR #50245),而不是獨立的參數。作者也坦言,Strata 在筆電上本來就已經偏慢,而 Transformers 這套方案目前還追不上,對於需要高速反應的 coding agent 使用情境仍嫌吃力。

🎯 **對工程師的意義**

如果你手上的硬體塞不下模型全部的專家權重,這篇文章給出一個明確的設計範式:只串流路由實際選中的專家、用有界快取控制記憶體、量化縮小磁碟讀取量,並盡量重用模型原生的高速核心(如 `grouped_mm`),而不是另寫一套慢速的逐專家迴圈。所有程式碼(Transformers PR、模型轉換套件、Metal 核心)都公開在作者的 Space 裡,值得想在消費級硬體上跑大型 MoE 模型的團隊參考。

🔗 **來源**
- 標題:180B Parameters, 32GB of RAM: Pushing MoE Inference to the Limit with Transformers
- 作者/機構:Tarek Ziadé, Hugging Face
- 連結:https://huggingface.co/blog/moe-expert-streaming

#MoE #LLMInference #HuggingFace #Transformers #Quantization #EdgeAI #ModelOffloading #OpenSource #AppleSilicon #MachineLearning
