---
title: From the creator of Redis; run LLM locally with ds4
source: Hacker News
url: https://dwarfstar.sh/
model: claude-code/sonnet
generated_at: '2026-10-03T19:54:48.779922'
score: 106
---

📌 Redis 作者出手，用 C 語言寫本地 LLM 推理引擎

TL;DR：antirez 推出 ds4，用純 C 打造的本地推理引擎，專攻高記憶體機器跑大型 MoE 模型。

當多數人還在討論要租哪家雲端 GPU 跑大模型時，Redis 的創造者 antirez 選擇了完全相反的方向:把 2840 億參數的 MoE 大模型,直接塞進你自己的 Mac 或工作站裡跑。

🤔 **為什麼要在本地跑這麼大的模型**

DS4(DwarfStar 4)是一個專為高記憶體 Mac、CUDA 與 ROCm 機器設計的「narrow」C 語言推理引擎。它支援 DeepSeek V4 與 V4.1 Flash、GLM 5.x 以及 Qwen3.8 Flash Next,同時涵蓋文字與視覺模型,並在同一套工具鏈中整合本地 API、CLI 與一個原生 agent。專案以 MIT 授權發布,原始碼為 C 語言,搭配 Metal、CUDA、ROCm 作為後端。

🧩 **三階段設計：巨人、壓縮、矮星**

README 把整個設計分成三個階段。第一階段是「the giant」:DeepSeek V4 Flash 是一個 2840 億參數的 mixture-of-experts 模型,一般做法是透過遠端伺服器服務,ds4 則是從完全相反的限制條件出發,直接面對本地硬體的侷限。第二階段是「the collapse」,也就是壓縮而非閹割:採用非對稱量化(asymmetric quantization),針對被路由到的專家(routed experts)進行壓縮,同時保留關鍵路徑的精度,讓模型得以在高記憶體機器上實際運作。第三階段是「the dwarf star」:本地引擎同時對外暴露 CLI、HTTP API 與一個原生 agent,三者共享同一份模型狀態與快取。

核心技術分成三塊:第一是非對稱 2-bit 量化,壓縮路由專家、保留共享關鍵路徑的精度;第二是把 KV 快取視為磁碟的一等公民,把長 prefix 存到 SSD,依 prompt hash 復原,重啟不必整個重新跑一次 prefill;第三是「一套引擎、三種介面」:`./ds4` 提供互動式聊天,`./ds4-server` 提供本地 API,`./ds4-agent` 則是長駐的程式設計 agent。專案同時列出 SSD streaming、tensor parallelism、session batching、DSPARK + MTP 與 vision input 等能力,模型格式僅支援 GGUF,載入方式為非對稱 2-bit 加 imatrix。

🧩 **怎麼上手**

安裝流程很直接:先 `git clone https://github.com/antirez/ds4`,進入目錄後執行 `./download_model.sh ds4f-q2` 下載權重;接著依平臺編譯,macOS 上用 `make`(走 Metal),Linux 的 DGX Spark 則用 `make cuda-spark`;最後用 `./ds4` 進入互動模式,或是用 `./ds4-server --ctx 100000` 啟動 API 服務。相容的客戶端包含 OpenCode、Claude Code、Codex CLI 與 Pi,並提供 `/v1/chat/completions`、`/v1/messages`、`/v1/responses` 三種端點。

📊 **硬體門檻與實測數字**

README 列出的硬體記憶體等級從 32GB 一路到 512GB,甚至雙機 2×512GB 的配置。V4 Flash Q2 是最基本的門檻;在 128GB 的機器上,GLM 5.3 Q2 與 Qwen Q4 也能跑起來,V4.1 Q2 則需要從 SSD 串流讀取。官方基準測試以 M5 Max 128GB、32K context 為參考點,生成速度為每秒 34.4 token,prefill 速度為每秒 557 token。細看完整表格:M5 Max 128GB 在 2,048 token 時 prefill 790.2 t/s、生成 39.4 t/s,拉長到 65,536 token 時 prefill 降為 398.5 t/s、生成 27.6 t/s;DGX Spark 128GB 在 2,048 token 時 prefill 825.8 t/s、生成 18.1 t/s,65,536 token 時 prefill 823.0 t/s、生成 13.8 t/s。

⚠️ **適用邊界**

這個專案的定位很明確:不是追求泛用性的推理框架,而是針對特定幾款 MoE 大模型,在高記憶體的消費級與工作站硬體上做深度最佳化。這也意味著支援的模型清單相對有限,換模型或換硬體平臺前,得先確認是否落在官方列出的記憶體與平臺矩陣內。

🎯 **對工程師的意義**

如果你本來就擁有一臺高記憶體的 Mac 或工作站,且想在不依賴雲端 API 的情況下跑前沿開源權重模型,ds4 提供了一條具體可行的路徑,從下載腳本到基準測試數字都公開在 GitHub 上,值得實際跑一輪驗證在自己硬體上的真實表現。

🔗 **來源**
- 標題：From the creator of Redis; run LLM locally with ds4
- 作者／機構：fibo（Hacker News 發文者）
- 連結：https://dwarfstar.sh/

#LocalLLM #OpenSource #DeepSeek #Quantization #Inference #Redis #Metal #CUDA #ROCm #MoE
