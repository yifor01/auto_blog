---
title: Introducing the llama.cpp benchmark dashboard for AMD Ryzen and Radeon
source: HuggingFace Blog
url: https://huggingface.co/blog/ggml-org/llamacpp-amd-bench
model: claude-code/sonnet
generated_at: '2026-11-27T01:10:28.456905'
score: 74
---

📌 AMD 本地推理有多快？llama.cpp 官方儀表板給答案

TL;DR：HuggingFace 與 ggml 團隊推出 llama.cpp × AMD 效能儀表板，公開追蹤 Ryzen／Radeon 上的推理效能。

本地跑大型語言模型時，「這個量化版本在我的 AMD 顯卡上到底多快」往往只能自己土法煉鋼測一次。現在 ggml 團隊與 HuggingFace 把這件事做成了一個持續更新、公開可查的儀表板。

🤔 **本地推理效能是持續變動的目標，但很少人持續追蹤**

模型、kernel 與 llama.cpp 的 build 版本都在不斷演進，推理效能自然也隨之變化。對 AMD 開發者來說，若想知道某個模型在自己的硬體上該用哪個量化版本、哪個 build，過去缺乏一個公開、可比對的參照點。這個儀表板的目標，就是讓使用者可以挑硬體、挑模型、挑 build，直接比較不同量化版本的表現，並追蹤效能隨時間的變化。

🧩 **三個分析視角：Overview、Build history、Context scaling**

儀表板在 Configuration 側邊欄提供 Hardware、Model、llama.cpp build 三個篩選項，目前支援的硬體是 Radeon 8060S（gfx1151）與 Radeon AI Pro R9700S（gfx1201）。三個分析頁籤各有用途：

- Overview：針對選定的硬體、模型、build，比較不同量化版本的表現，用兩張圖呈現 PP512（處理512個輸入 token，不生成文字）與 TG128（在零上下文下生成128個 token）。
- Build history：追蹤同一個硬體、模型、量化版本在所有已記錄 build 上的 PP512 與 TG128 變化，方便觀察版本更新帶來的效能差異。
- Context scaling：觀察在選定的 build、硬體、模型、量化版本下，隨著既有上下文增長，token 生成吞吐量如何變化。

所有測試都以 tokens per second 為單位，圖上繪製的是平均吞吐量（avg_ts）。PP512 用來評估模型處理 prompt 的速度，TG128 用來評估模型產出文字的速度，兩者都從 context depth 零開始測量。

測試基準是透過 llama-install.sh（也就是 llama.app 背後的建置與安裝專案）所發佈的預編譯二進位檔。公開的 gfx1151 與 gfx1201 workflow 採每週排程執行，使用 llama-bench 工具,在 Flash Attention 開啟與關閉兩種情境下各跑10次重複測試。目前涵蓋的模型包含 Inkling 2 Mini、Qwen、Gemma、gpt-oss 與 LFM 系列,涵蓋 dense 與 MoE（混合專家）兩類架構;可用的 GGUF 格式包括 Q4_K_M、Q8_0 等量化版本,以及 BF16、F16 等高精度格式。

📊 **資料全公開，可自行重現或延伸分析**

儀表板背後的資料直接讀取自 Hugging Face 上公開的 ggml-org/install.sh-benches-data Storage Bucket。每張圖的標題旁都有資料來源連結,可直接開啟對應 build、硬體、模型的資料夾。標準測試結果存放路徑格式為 `<build>/<hardware>/<model>/<quant>.jsonl`,工作負載掃描（workload sweeps）則使用同一資料夾下的 `<quant>-tg.jsonl` 檔名。這代表任何人都可以拿這些原始資料自行繪圖、驗證測試方法,或和自己本機跑出來的結果做比對。

🎯 **實務啟示**

對於想在 AMD Ryzen／Radeon 上跑本地推理的工程師，這個儀表板提供了一個不用自己架測試環境就能查到的效能基準，挑選模型與量化版本前可以先來這裡比對 PP512／TG128 數字，再決定要不要自己動手驗證。由於測試資料與方法完全公開，也可以把它當作自建 benchmark pipeline 時的參照範本。文中也提到團隊歡迎回饋想看到哪些模型與工作負載，顯示這會是一個持續擴充的專案而非一次性成果。

🔗 **來源**
- 標題：Introducing the llama.cpp benchmark dashboard for AMD Ryzen and Radeon
- 作者／機構：HuggingFace（ggml-org 團隊）
- 連結：https://huggingface.co/blog/ggml-org/llamacpp-amd-bench

#LlamaCpp #AMD #Radeon #LocalInference #Benchmark #Quantization #GGUF #EdgeAI #OpenSource #MoE
