---
title: 'Llama.cpp on a jailbroken PS5: run any GGUF model natively on the console'
source: Hacker News
url: https://github.com/cobanov/PS5LM
model: claude-code/sonnet
generated_at: '2026-10-17T19:35:05.718734'
score: 85
---

📌 有人把 PS5 改裝成區域網路的私人 LLM 伺服器

TL;DR：開源專案 PS5LM 讓一臺破解過的 PS5 跑 llama.cpp，變成全家共用、不用雲端的推理伺服器。

你家的 PS5 在不玩遊戲的時候,GPU 其實是閒置的。有人想到一個點子：既然 llama.cpp 能跑在各種 GPU 上,為什麼不讓它跑在客廳電視下的那臺主機裡?PS5LM 這個 GitHub 專案把這個念頭變成了真的可用的東西。

🤔 **想要一臺不用雲端、不用帳號的私人模型伺服器**

PS5LM 的目標使用者很明確：擁有破解版 PS5、想要在家架一臺私人模型伺服器的人。它把 GGUF 模型載入主機的 GPU，提供服務給筆電、手機與各種程式開發工具使用，整個過程不需要額外的 PC、不需要雲端、也不需要帳號。

🧩 **用 llama.cpp 的 Vulkan backend 吃滿主機 GPU**

核心架構是 llama.cpp 的 Vulkan backend，跑在 PS5 的 RDNA 2 GPU 上，用共享記憶體裡的 11.4 GB 空間存放模型與 context，llama.cpp 支援的每一種架構與量化格式都能直接搭配使用。

對外服務的部分做得相當完整：
- 相容 OpenAI 的 `/v1/chat/completions` 與 Anthropic 的 `/v1/messages`（Claude Code 可以直接指向它），外加一個瀏覽器內建的聊天頁面。只要把用戶端指向 `http://<console>:8081`,帶任何模型名稱,載入中的模型就會回應。
- 支援決策模型（decision models），透過與 Ollaya 相同的 `/v1/systemone` API，載入像 d1、Clef、OpenJev 這類模型後,可以回傳帶校準機率的分類結果、分數或是非題答案,而不是生成文字。
- 具備視覺能力：搭配 Gemma 4、MiniCPM-V、d1 這類有影像投影層的模型,可以在聊天與決策任務中直接吃圖片輸入。
- 介面本身投影在電視上,每一個請求都會以聊天形式即時串流顯示：哪個裝置發出請求、問了什麼、回答逐字跳出。按下 Square 可以送出示範請求,Triangle 則打開鍵盤輸入,整套體驗是設計給「坐在沙發上操作」的場景。
- 內建 Console 監控頁面,顯示過去兩分鐘或一小時的溫度、功耗、GPU 與 CPU 使用率曲線。
- 模型管理上有自動規劃機制：讀取每個 GGUF 檔案,依照剩餘記憶體配置最長的 context 與最佳的 cache,並提供一份在主機上實測過的建議模型清單,可直接從 Hugging Face 下載到內部儲存、M.2 硬碟或 USB 隨身碟。

📊 **幾組官方實測的推理速度**

README 公布的 benchmark 數字如下：

| 模型 | 大小 | PS5 Slim 上的表現 |
|---|---|---|
| Qwen 3.5 0.8B, Q4_K_M | 0.5 GB | 每秒 207 tokens |
| Qwen 3.5 9B, Q4_K_M | 5.3 GB | 每秒 55 tokens |
| Qwen 3.8 27B, UD-Q2_K_XL | 9.2 GB | 約每秒 20 tokens，64k context |
| d1 Omni 600M（決策模型） | 1.1 GB | 3 個問題 0.3 秒；一張 720p 圖加 7 個問題 2.9 秒 |

🧩 **怎麼跑起來**

前提是一臺韌體版本在 7.00 到 13.60 之間、已破解的 PS5，並安裝 kstuff-lite、etaHEN、ShadowMountPlus 三個必要的 payload（分別負責核心修補、homebrew 支援、把 PS5LM 加到主畫面），elfldr 與 ftpsrv 則是建議安裝，用於溫度監控與透過 FTP 安裝模型。安裝流程是下載發布包、透過 FTP 複製資料夾到 `/data/homebrew`，之後就能從主畫面啟動，到 Models > Suggested 下載模型，或自行把 `.gguf` 檔案丟進模型資料夾。整套操作用搖桿完成：D-pad 選單、Cross 載入、Square/Triangle 送出示範或打字。

⚠️ **這終究是一個小眾的 homebrew 玩具**

專案本身採 GPL-3.0-or-later，依賴的 llama.cpp 保留 MIT 授權，字體 Manrope 用 OFL。README 特別聲明不包含任何 Sony SDK 檔案、金鑰、韌體或模型權重，且專案與 Sony Interactive Entertainment 無任何關係。要玩這個東西，前提是你已經接受了破解主機的風險與法律灰色地帶，這注定只適合願意動手的 homebrew 愛好者，而非一般企業部署場景。

🎯 **實務啟示**

拋開「拿 PS5 跑 AI」的噱頭,這個專案真正展示的是 llama.cpp 生態的可移植性有多強：只要有 Vulkan backend 與足夠的記憶體,幾乎任何消費級 GPU 裝置都能被改裝成本地推理節點,而且決策模型的 `/v1/systemone` API 也證明小型、校準過機率輸出的模型同樣能在邊緣硬體上即時運作。對做邊緣推理或自架模型伺服器的工程師來說,這是個有趣的設計參考案例。

🔗 **來源**
- 標題：Llama.cpp on a jailbroken PS5: run any GGUF model natively on the console
- 連結：https://github.com/cobanov/PS5LM

#PS5 #LlamaCpp #LocalLLM #GGUF #EdgeAI #Homebrew #Jailbreak #SelfHosted #OpenSource #AIHardware
