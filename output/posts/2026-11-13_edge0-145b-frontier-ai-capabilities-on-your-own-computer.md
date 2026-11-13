---
title: 'Edge0-145B: Frontier AI Capabilities on Your Own Computer'
source: Hacker News
url: https://edge0.ai/blog/introducing-edge0-145b-frontier-ai-capabilities-on-your-own-computer
model: claude-code/sonnet
generated_at: '2026-11-13T22:44:52.288332'
score: 110
---

📌 145B 參數模型塞進筆電：Edge0-145B 挑戰雲端前沿模型的地端答案

TL;DR：開源 145B 參數模型可在筆電離線執行，記憶體峰值僅 29GB，效能逼近多款雲端前沿模型。

一直以來，on-device AI 都被困在一個死結裡：模型做得夠大才夠聰明，但做得夠大就塞不進手機或筆電的記憶體。Edge0 團隊這次開源的 Edge0-145B，宣稱是全球第一個 1450 億參數規模的開源地端模型，試圖同時拿到「夠聰明」和「跑得動」。

🤔 **地端模型為什麼一直長不大**

素材指出，在 2026 年 9 月之前，多數 on-device 模型都卡在 100 億參數以下：Apple Intelligence 的地端基礎模型約 30 億參數，Google Gemini Nano 有 18 億與 32.5 億兩個版本。即使是 70 億參數的模型，也可能吃掉約 4GB 記憶體；一個經過大幅壓縮的 350 億參數模型，記憶體需求甚至逼近 20GB，遠超手機可用的空間。模型權重要佔儲存空間、生成時又要被持續讀取，與作業系統和其他 App 搶記憶體頻寬,這道「記憶體牆」讓廠商長期只能用縮小模型規模來換取可用性,但代價就是能力受限。即便是隱私優勢明顯的 Apple Intelligence，Apple 自己也承認其地端模型並非為需要通用世界知識的 agentic 應用設計。

🧩 **四層設計：架構、訓練、載入、排程一起改**

Edge0 團隊表示，Edge0-145B 的模型與推理引擎是「一起設計」的，目的是減少大模型執行時的記憶體佔用與資料搬動量。具體做法拆成四層：

- **架構層**：在 MoE（混合專家）架構中，每 64 個 專家共享兩個大矩陣，各專家只保留一組捕捉差異的小參數，取代過去「每個專家各自存一整套矩陣」的做法。145B 總參數中，每一步推理實際只有約 10B 參數參與運算。
- **訓練層**：模型從一開始就以地端架構訓練，而不是先訓練一個雲端模型再事後壓縮或剪枝。
- **載入層**：GPU 記憶體、系統記憶體與 SSD 三層儲存的讀取與運算彼此重疊,常用的「熱門專家」留在 GPU 記憶體;約 40GB 的專家庫放在系統記憶體,依需求載入 GPU;約 48GB 的詞彙表資料留在 SSD,按需讀取。
- **排程層**：GPU 負責運算已快取的專家，CPU 同時平行處理其餘工作；並透過 speculative decoding 一次驗證多個候選 token，把讀取權重的成本分攤到更多輸出 token 上。

📊 **筆電上的實測數字**

| 項目 | 數字 | 意義 |
|---|---|---|
| 記憶體峰值 | 29GB | 可在相容筆電（如 MacBook Pro）上執行，不需伺服器 |
| Prefill 速度 | 1,100+ tokens/s | 可處理數十頁程式碼等長提示 |
| Decode 速度 | 80+ tokens/s | 比人類閱讀速度更快 |
| 功耗 | 約 120W | 在測試環境下可持續運作不降頻 |
| 上下文長度 | 128K–256K | 長輸入下速度基本不降 |

作為對照，團隊早前發布的 Edge0-35B 手機版在 iPhone 18 Pro Max 上，用約 2.5GB 記憶體跑出 37+ tokens/s；Edge0-145B 參數量是其四倍，但換到筆電規格後反而跑出更高的 80+ tokens/s。不過兩者測試機型與模型不同,不能直接類比。

在基準測試方面，Edge0-145B 在 DeepSWE 1.1 拿下 64.6 分，優於 Qwen3.8-Flash-Next（58.7）與 DeepSeek-V4-Flash-0731（54.4）；GPQA-Diamond 拿下 90.4 分，接近 DeepSeek-V4-Flash-0731（90.8）與 Claude-Opus-4.6 Max（91.3）；IFBench 拿下 80.6 分，優於 DeepSeek-V4-Flash-0731（79.2）與 Claude-Opus-4.6 Max（62.5）；Terminal-Bench 2.1 拿下 86.52 分，高於 Qwen3.8-Flash-Next（83.3）、DeepSeek-V4-Flash-0731（82.7）與 Claude（78.2）；AA-LCR 則以 79.3 分略高於 Claude 的 78.0。

⚠️ **別忘了，硬體和電費還是要花錢**

素材也坦言，雲端的 API 費用、資料限制和網路依賴問題解決了,但「相容筆電」本身與電力成本仍是真實支出。團隊將模型權重、推理框架與 App 一併開源，方便開發者自行重現數字、評估或微調。

🎯 **實務啟示**

如果你的工作場景重視資料不落地、離線可用、沒有 per-token 費用，Edge0-145B 提供了一個新的評估基準點：先確認手上的硬體是否落在「相容筆電」範圍內，再比對你實際任務的 benchmark 落點,而非只看參數量。

🔗 **來源**
- 標題：Edge0-145B: Frontier AI Capabilities on Your Own Computer
- 作者／機構：sroussey（Hacker News）
- 連結：https://edge0.ai/blog/introducing-edge0-145b-frontier-ai-capabilities-on-your-own-computer

#OnDeviceAI #LLM #OpenSource #MoE #EdgeComputing #Edge0 #LocalInference #AIAgents #MachineLearning #Coding
