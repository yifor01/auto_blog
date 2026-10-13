---
title: 'Janas: Run LLMs larger than RAM by streaming experts from SSD'
source: Hacker News
url: https://github.com/prabanta-dev/janas
model: claude-code/sonnet
generated_at: '2026-10-13T22:06:43.129815'
score: 91
---

📌 32GB 筆電跑 80B 模型:Janas 用 SSD 串流打破記憶體上限

TL;DR:開源工具 Janas-LLM 把 MoE 模型的專家權重即時從 SSD 串流進記憶體,實測在同一臺筆電上全面快過 llama.cpp。

一顆 48GB 的模型,塞進一臺只有 32GB 記憶體的筆電裡跑,聽起來違反常識。但 Janas 這個以 C 語言寫成、零外部依賴的開源專案,靠著「只把當下需要的專家權重留在記憶體裡」的設計,讓這件事真的發生了。

🤔 **MoE 模型的記憶體困境**

Mixture-of-Experts(MoE)模型雖然每次推論只啟用一小部分參數,但完整權重仍得全部載入記憶體才能運作,這讓一般筆電望著 70B、80B 等級的模型只能興嘆。Janas 的作者 Maurizio「camauri」Cammalleri 認為,既然每個 token 只需要少數專家,那麆不如把權重留在硬碟上,只把真正用到的部分讀進記憶體,常被重複呼叫的專家才留在快取裡。

🧩 **核心設計:SSD 常駐、記憶體做快取**

Janas 是一個「人工智慧工具家族」的第一個元件 Janas-LLM,專門用來在一般電腦(不論有無 GPU)上運行大型 MoE 語言模型。它的做法是:模型權重留在磁碟上,每個 token 所需的專家(experts)透過 NVMe SSD 即時串流讀取,反覆被用到的專家則留在記憶體快取中。README 特別強調這是一個「實驗,不是產品」——目前處於早期開發階段,公開 API 與命令列介面每週都在變動,唯一的例外是模型檔案格式(.jns,目前為 format version 2),保證未來版本都能讀取。

📊 **實測數據:同一臺筆電,全面領先 llama.cpp**

作者在一臺 Debian 13、搭載 Intel Core Ultra 9 185H(含內建 Arc GPU)、32GB DDR5 記憶體、讀取速度約 5.7GB/s 的 NVMe SSD 的筆電上,對比了 Janas-LLM 與 llama.cpp 在多個模型上的表現(日期為 2026 年 10 月 9-12 日):

| 模型 | 讀取 prompt (Janas / llama.cpp) | 生成 (Janas / llama.cpp) |
|---|---|---|
| Qwen3-Next-80B-A3B(48.4GB,超過記憶體) | 62 / 16 tok/s | 24 / 2.8 tok/s |
| Qwen3-Coder-Next(48.4GB) | 66 / 14 tok/s | 22 / 2.2 tok/s |
| Qwen3.6-35B-A3B | 104 / 79 tok/s | 19 / 12 tok/s |
| Qwen3-30B-A3B | 135 / 122 tok/s | 32 / 15 tok/s |
| Qwen3.8-27B(dense) | 30.6 / 25.6 tok/s | 4.4 / 2.1 tok/s |

對於超出記憶體容量的 80B 模型,Janas-LLM 的生成速度達到 llama.cpp 的將近 9 倍。README 也坦言有個例外:3-bit 量化的 Qwen3-30B 讀取 prompt 時比 llama.cpp 慢,因為其 Q3_K 權重目前還無法送上 GPU 的快速 prompt 路徑,不過生成速度仍是對手的三倍。在 Windows 11 上測試結果與 Linux 相近,dense 模型因權重整塊送上 GPU,讀取速度甚至快了 1.8 倍。

💡 **怎麼用**

Linux x86-64(Ubuntu 22.04、Debian 12 以後)可直接下載執行檔解壓後執行 `./janas-chat`,程式會列出已知模型供選擇、自動下載並校驗;Windows 10/11 x86-64 則下載對應 zip 解壓後執行 `.\janas-chat`。模型檔案皆已從 Hugging Face 轉換好,也可以從原始碼自行建置。

⚠️ **穩定性尚未驗證,使用前要有心理準備**

README 明確警告:引擎刻意把機器資源用到極限,會用專家快取填滿可用記憶體,並以 O_DIRECT 全速讀取磁碟;在記憶體餘裕不足的機器上,可能把桌面環境逼進 swap 而變慢甚至無回應。作者也提到曾有一次使用 GPU 導致 driver reset,連帶讓桌面環境當掉。若要控制風險,可用 `--cache <GiB>` 限制記憶體用量,或用 `JANAS_GPU=0` 完全關閉 GPU;程式只會寫入 `~/.cache/janas`,不會更動原始模型檔案。目前只在作者的那臺筆電上開發與測試過,其他 CPU(尤其缺乏 AVX-VNNI 或 AMD 平臺)、獨立顯卡、更慢的磁碟都未經驗證。

🎯 **實務啟示**

如果你的團隊想在邊緣裝置或個人筆電上跑超出記憶體容量的 MoE 模型做原型驗證,Janas 提供了一個值得關注的方向,但鑑於其「實驗性」定位與尚不穩定的 API,生產環境部署前務必先用 `janas-bench` 在自己的硬體上實測,並預留應對當機與資源耗盡的空間。

🔗 **來源**
- 標題:Janas: Run LLMs larger than RAM by streaming experts from SSD
- 作者/機構:Maurizio "camauri" Cammalleri(GitHub: prabanta-dev)
- 連結:https://github.com/prabanta-dev/janas

#MoE #LLMInference #EdgeAI #LlamaCpp #OpenSource #GPUComputing #NVMe #OnDeviceAI #ModelServing #QwenModels
