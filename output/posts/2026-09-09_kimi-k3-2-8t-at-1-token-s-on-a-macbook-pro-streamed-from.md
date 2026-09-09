---
title: Kimi K3 (2.8T) at 1 token/s on a MacBook Pro, streamed from four SSDs
source: Hacker News
url: https://github.com/argonautlabsai/deltafin
model: claude-code/sonnet
generated_at: '2026-09-09T20:01:24.913388'
score: 91
---

📌 M5 Max筆電跑2.8T參數模型,代價是1 token要等一秒

TL;DR：Deltafin用四顆SSD串流專家權重,在一臺128GB筆電上「原汁原味」跑滿Kimi K3的2.8T參數,速度換來的是超慢的prefill。

一款2.8兆參數、目標運行在16節點、約4.8TB總顯存基礎設施上的模型,要塞進一臺消費級MacBook Pro——聽起來像不可能的任務,但Deltafin這個開源專案硬是做到了,只是代價相當寫實:512 token的prompt,光是等到第一個輸出token就要6.3分鐘。

🤔 **不刪、不縮、不妥協的「原始尺寸」目標**

市面上已經有其他專案能在消費硬體上跑Kimi K3,但做法是把專家權重重新編碼壓到約3-bit,換取「差不多能用」的速度。Deltafin選擇了另一條路：每一個專家的每一個byte都完全照Moonshot釋出的原樣保留,16個路由專家、全部token都由K3本尊決定,不做任何量化縮水,只在「怎麼把物理上的I/O瓶頸榨到極限」這件事上下功夫。專案作者(fork自gavamedia/deltafin,原始引擎由該作者打造)將此定位為一場關於消費硬體極限的實驗,而非急著討好創投的產品原型。

🧩 **從四顆SSD即時串流專家權重**

Deltafin是一個單一原生執行檔,核心設計是把1.45TB的專家權重存放在SSD上,依照路由結果即時串流讀取,而不是一次全部載入記憶體。README提供了兩種安裝方式:一種先把完整1.7TB模型下載到硬碟(`deltafin setup --full`),追求最快的執行速度;另一種是邊用邊串流(`deltafin setup --stream`),只需215GB起始空間,隨著使用逐步建立本地快取。

專案還內建了推測解碼(speculative decoding)機制:預設搭配Inferact的Kimi-K3-DSpark小模型負責「先猜」,K3本尊負責逐一核對每個猜測是否正確,只有通過確認的內容才會真正輸出;另外有可選的Qwen模組專門加速純文字續寫(如程式碼自動完成),在一次17-token的測試中讓速度提升2.7倍,且輸出token ID完全相同。

📊 **實測數據:多顆SSD疊加的效益遞減**

以下是這個fork在M5 Max、128GB記憶體、四顆SSD串流設定下,於2026年9月8日測得的數字(每個數字都是單次冷啟動、使用同一組prompt跑出的結果):

| 情境 | 關閉draft模型 | 開啟draft模型 |
|---|---|---|
| 穩定解碼,512-token答案 | 0.92 tok/s | 1.00 tok/s |
| 穩定解碼,128-token答案 | 0.93 tok/s | 1.13 tok/s |
| 公開17-token prompt(median of 3) | — | 0.96 tok/s(上游回報為0.68) |
| 首token延遲(512-token prompt) | 6.3分鐘 | 6.3分鐘 |

另外還有一項關於SSD數量的擴展性測試：單顆SSD約可達到四顆時速度的52%,兩顆約73%,三顆約90%。原因是每一層16次專家讀取中,速度最慢的那一次讀取決定了整層的步調,而非單純看總頻寬疊加。相較之下,上游gavamedia/deltafin在M1 Max筆電上的官方數據僅0.29 tok/s左右,顯示這個fork在同代硬體限制下確實有明顯進步。

⚠️ **已知的瓶頸:prefill比解碼慢得多**

專案作者誠實列出目前的限制:512-token的prompt要等6.3分鐘才出現第一個token,原因已被定位為prefill階段會把每一層的專家權重重複讀取8次,但修復方案目前「已規劃、尚未實作」。這代表Deltafin現階段更適合短prompt、長輸出的場景,若丟進去的是長文件或大量上下文,等待時間會相當可觀。

🎯 **實務啟示**

對想在自架硬體上碰觸超大模型的工程師來說,Deltafin提供了一個誠實的參照系:它證明了「用SSD當顯存的延伸來跑2.8T模型」在物理上可行,但也清楚標示出目前的天花板在prefill而非解碼。如果你的應用場景是短prompt、可以忍受秒級吞吐量,同時堅持不能犧牲模型精度,這類「不砍質量、只榨I/O」的路線值得關注;但若需要處理長上下文,目前仍應等待prefill重複讀取的修復,或選擇量化壓縮的替代方案。

🔗 **來源**
- 標題：Kimi K3 (2.8T) at 1 token/s on a MacBook Pro, streamed from four SSDs
- 作者／機構：Argonautlabs(fork自gavamedia/deltafin)
- 連結：https://github.com/argonautlabsai/deltafin

#KimiK3 #MoE #LocalLLM #SSDStreaming #SpeculativeDecoding #EdgeInference #OpenSource #ConsumerHardware #LLMInference #AppleSilicon
