---
title: Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s
source: Hacker News
url: https://github.com/Niko1221/Strata
model: claude-code/sonnet
generated_at: '2026-10-04T20:14:55.885148'
score: 100
---

📌 家用顯卡能跑 1250 億參數模型？Strata 實測效能曝光

TL;DR：開源工具 Strata 讓一張 12GB 顯卡在本機跑 Qwen3.8-Flash-Next（125B），完全不用上傳雲端。

通常一個千億參數等級的模型，想都別想塞進一張遊戲顯卡。但 Strata 這個開源專案宣稱，只要有一張 12GB 以上的 NVIDIA 或 AMD 顯卡，就能在自己的電腦上跑 Qwen3.8-Flash-Next，聊天、寫程式、讀圖片、接你的 coding agent，而且資料完全不離開本機。

🤔 **為什麼千億模型能塞進消費級顯卡**

關鍵在於 Qwen3.8-Flash-Next 本身是稀疏（MoE）架構加上大量量化。Strata 提供多種壓縮程度的模型版本（Q2_0、IQ2_XS、IQ3_XXS、IQ3_S 等），壓縮越多檔案越小、跑越快，但相對「聰明程度」會打折。安裝程式會自動偵測你的顯卡型號與記憶體，挑選對應的推理引擎（NVIDIA 與 AMD 走不同引擎路徑），並依照你的 RAM 容量推薦合適的版本。

🧩 **怎麼用：一鍵安裝、OpenAI 相容 API**

Windows 用戶雙擊 `START-HERE.bat`，Linux 用戶執行 `./setup.sh`，安裝程式會問幾個問題（選哪個模型、多大的 context、要不要讀圖），全部按 Enter 選預設即可。下載約 70GB 模型後自動啟動，瀏覽器會打開 `http://127.0.0.1:8080` 的 Strata 介面，裡面有 Chat 頁面和即時顯示 GPU/CPU/RAM 用量的 Monitor。

若要接到自己的 App 或 coding agent，把 Base URL 設成 `http://127.0.0.1:8080/v1`（OpenAI 相容格式）即可，API Key 和模型名稱可以隨便填。Claude Code 之類用 Anthropic API 格式的工具，則改用 `http://127.0.0.1:8080/v1/messages`。工具也提供 MCP server，讓 AI 助手自己操作安裝、啟動、停止 Strata。

📊 **實測速度：RTX 5070 與 RX 9070 XT**

社群在兩臺一般遊戲電腦上實測，數字代表「生成速度」（每秒輸出幾個 token）與「讀取速度」（吃進 prompt 的速度）：

NVIDIA RTX 5070（12GB VRAM）：

| 量化版本 | 生成速度 | 讀取速度 |
|---|---|---|
| Q2_0 | 94 tokens/s | 2,650 tokens/s |
| IQ2_XS | 79 tokens/s | 2,090 tokens/s |
| IQ3_XXS | 62 tokens/s | 1,750 tokens/s |
| IQ3_S | 53 tokens/s | 1,620 tokens/s |
| Coder | 55 tokens/s | 2,180 tokens/s |

AMD RX 9070 XT（16GB VRAM）：

| 量化版本 | 生成速度 | 讀取速度 |
|---|---|---|
| Q2_0 | 60 tokens/s | 1,160 tokens/s |
| IQ2_XS | 52 tokens/s | 1,110 tokens/s |
| Coder | 44 tokens/s | 1,420 tokens/s |

官方表示，VRAM 更大的卡會更快，例如 RTX 3090（24GB）「應該」能跑到每秒 100-140 token。60 tokens/s 已經比一般人閱讀速度還快。

⚠️ **限制與取捨**

Coder 版本移除了一半的 expert，體積縮到 32GB RAM 就能跑，SWE-bench Verified 分數達到完整模型的 91%，但在程式碼以外的任務（包含中文等 CJK 文字）表現較弱。較舊的顯卡（Tesla P40、GTX 10 系列等）與 Intel Arc 需要社群自行編譯測試，屬實驗性支援；AMD 顯卡在 Windows 上目前還不能讀圖片，需切到 Linux 才能用處理器跑圖片辨識。首次啟動模型載入期間，電腦可能會卡頓 1-3 分鐘，這是正常現象。

🎯 **實務啟示**

如果你在意資料隱私、不想把 prompt 送上雲端 API，或單純想在本機測試大模型的可行性，Strata 把「裝引擎、選量化版本、接 API」這整套流程打包成一鍵安裝，對於沒有時間研究 llama.cpp 參數的工程師是直接可用的起點。但要清楚量化等級與效能是一條光譜，選版本前先衡量自己真正需要的是速度還是推理品質。

🔗 **來源**
- 標題：Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s
- 作者／機構：snehesht（Hacker News）
- 連結：https://github.com/Niko1221/Strata

#Strata #Qwen3 #LocalLLM #OpenSource #MoE #Quantization #LLMInference #ConsumerGPU #AIEngineering #SelfHosted
