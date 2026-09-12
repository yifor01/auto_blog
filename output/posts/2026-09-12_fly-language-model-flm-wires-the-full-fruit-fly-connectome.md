---
title: Fly Language Model (FLM) Wires the Full Fruit Fly Connectome Into a Frozen
  1.2B LLM, and Its Own Controls Show the Wiring Does Not Help
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/12/fly-language-model-flm-wires-the-full-fruit-fly-connectome-into-a-frozen-1-2b-llm-and-its-own-controls-show-the-wiring-does-not-help/
model: claude-code/sonnet
generated_at: '2026-09-12T19:34:52.879669'
score: 79
---

📌 果蠅腦接上 1.2B LLM，作者自證這套生物線路沒用

TL;DR：開發者把完整果蠅連接體焊進凍結的 1.2B 語言模型，但論文自己的對照實驗顯示，拿掉果蠅腦、只留隨機線路，表現反而更好。

如果你聽到「把一整隻果蠅的腦神經連接圖，接進一個十幾億參數的語言模型」，第一反應大概是某種行銷噱頭。但這次特別的是，做出來的人自己拿數據打了自己的臉，而且還老實寫進報告裡。

🤔 **這是什麼：把果蠅神經圖當成儲備池，接在凍結 LLM 上**

Fly Language Model（FLM）是一個可公開試用的 chatbot，核心是把完整保留下來的 MaleCNS v1.0 果蠅連接體（connectome），接到凍結不動的 LiquidAI LFM2.5-1.2B-Instruct 骨幹模型上。專案作者在對外宣傳時稱它是「世界第一個 Fly Language Model」，並使用了一個叫 GPF（Generative Pre-trained Fly）的架構稱呼；不過報告本身並未採用 GPF 這個標籤，也明確澄清自己並非第一個「以連接體為基礎」的語言模型，報告中還提到一份更早的原型 ngxson/fly-hf，是用 MaleCNS 裡 49,393 顆神經元的中央腦子集當儲備池，在 TinyStories 上訓練、且沒有預訓練骨幹。FLM 的差異點在於用了完整保留的連接體規模，以及「骨幹凍結」的設計，方便追蹤語言能力究竟從哪來。

🧩 **架構：166,700 個神經元、2,558 萬條邊，只訓練一個很小的讀出層**

整套系統可以理解為「在語言模型上焊了一顆生物儲備計算器（reservoir computer）」。完整保留下來的 MaleCNS 圖，有 166,700 個節點與 25,582,938 條有向邊，全部參與運算；連接圖本身、LLM 骨幹、以及輸入輸出的隨機投影矩陣全部凍結不訓練，唯一會訓練的是一個 278,528 參數的讀出層，佔骨幹總參數 1,170,340,608 的比例約 0.0238%。

流程大致是這樣：每個 token 先經過一個固定的高斯投影，把 2,048 維的 token embedding 壓縮成 128 個通道；果蠅圖裡的每個神經元隨機分配到其中一個通道（帶隨機正負號）；接著整張圖依照 x = tanh(W(0.6x + 0.4Bc)) 更新狀態，其中 W 存放的是按輸入正規化過的解剖學接觸次數；最後把所有神經元狀態分箱成 128 維，經過兩個不帶偏置的訓練矩陣（U 是 128×128，V 是 2,048×128），再投影回凍結的詞彙頭，變成加在骨幹 logits 上、RMS 上限被限制在 0.25 的一個有界殘差項。

📊 **對照組贏了：果蠅圖沒有帶來額外好處**

作者用 SmolTalk 裡新切出的 32 段日常對話（共 1,236 個目標 token）做評估，跑了三個訓練種子，結果如下：

| 設定 | 表現 |
|---|---|
| 果蠅讀出層 vs 骨幹原始表現 | 每 token 進步 0.0222 nats（困惑度從 3.98 降到 3.90）|
| 直接輸入對照組（同樣 128 通道投影，但跳過連接圖，直接接同結構讀出層）| 三個種子全部贏過果蠅版本，平均每 token 領先 0.000488 nats |
| 配對 bootstrap 信賴區間 | +0.00000502 至 +0.00104，不支持「果蠅圖有特殊貢獻」的結論 |

報告另外做了兩個關鍵驗證：把 W 設為零可以精確重現骨幹本身的逐 token loss，證明果蠅圖確實有參與運算；而在不重新訓練的情況下打亂節點身份標籤，NLL 又會回到接近基準線，說明讀出層學到的其實是「介面對齊」，而不是果蠅拓撲本身比隨機線路更優越。報告還證明這套遞迴機制每個 token 最多把初始狀態差異壓縮 0.6 倍，10 個 token 後這個界限只剩 0.00605，20 個 token 後只剩 0.0000366，換句話說堆進 166,700 顆神經元並沒有換來長記憶，上下文能力終究來自 LLM 骨幹本身。

⚠️ **限制**

作者自己給出的證據鏈相當完整且誠實：果蠅連接圖確實有參與計算，但沒有證據顯示它比隨機線路更適合語言建模；長程記憶的來源仍是凍結骨幹，而非生物連接圖。

🎯 **實務啟示**

這是一個值得工程師學習的「陰性結果也要老實報告」的案例：專案本身 MIT 授權，nftechie/flm 這個 repo 可在 Python 3.12（macOS/Linux，支援 MPS、CUDA 或 CPU）本地跑，不需要 API key，適合對 reservoir computing 或生物啟發架構好奇的人拿來把玩，但不建議把「連接體」當成效能賣點來包裝。

🔗 **來源**
- 標題：Fly Language Model (FLM) Wires the Full Fruit Fly Connectome Into a Frozen 1.2B LLM, and Its Own Controls Show the Wiring Does Not Help
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/12/fly-language-model-flm-wires-the-full-fruit-fly-connectome-into-a-frozen-1-2b-llm-and-its-own-controls-show-the-wiring-does-not-help/

#ReservoirComputing #Connectome #LLM #NeuroAI #OpenSource #MachineLearning #LanguageModel #AIResearch #BioinspiredAI #Benchmarking
