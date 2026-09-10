---
title: Qwen 3.8 follows GPT-5.5 Pro reasoning prefills
source: Hacker News
url: https://gist.github.com/wsxiaoys/e0286dc6bb624ff5fdf49e7f4c528ba3
model: claude-code/sonnet
generated_at: '2026-09-10T20:05:31.492198'
score: 89
---

📌 讓 Qwen3.8 讀一口 GPT-5.5 Pro 的思路，答案就洩了 18 個百分點

TL;DR：一個「reasoning prefill」實驗發現，塞入 GPT-5.5 Pro 前 1% 的推理內容後，Qwen3.8 A95B 的回答與該模型的重疊度暴增，暗示其訓練資料可能與 GPT-5.5 Pro 系有關。

同一批開源模型，換一個「老師」模型做前綴注入，得到的結果卻天差地遠：先前用 Opus 4.8 幾乎測不出效果的 Qwen，這次換上 GPT-5.5 Pro 當老師，重疊度直接跳升 18 個百分點以上。這篇貼上 Hacker News 後拿下 232 分、93 則留言，顯然戳中了不少人對「模型蒸餾來源」的好奇心。

🤔 能不能從「思路重疊度」反推訓練資料？

這是一份 Hacker News 上發布的後續實驗（v1.1），延續作者先前「reasoning prefill」與「Stolen Thoughts」系列的方法論：如果目標模型曾用某個教師模型的輸出做過蒸餾（distillation）訓練，那麼把教師的推理過程餵給目標模型的推理通道（reasoning channel）之後，目標模型接下來生成的可見答案，理論上會更貼近教師的用詞與表達方式。

🧩 實驗設計：只餵 1% 的思路，看後面 100 個 token 抄了多少

作者針對 45 道題目（15 題 STEM、15 題非 STEM、15 題合成謎題）分別讓每個目標模型產生兩種回答：一種是完全不加提示的普通回答，另一種是在目標模型的推理通道開頭，插入教師模型 GPT-5.5 Pro 推理內容的前 1%，可見答案部分仍由模型自由生成。接著比對目標模型答案的前 100 個 token，與教師模型可見答案之間的重疊程度，分數取 unigram、bigram、trigram 三種 source recall 的平均值。

📊 數據：Qwen 的變化最劇烈

| 模型 | 樣本數 | 未加前綴 | 加入 GPT-5.5 Pro 推理前綴 | 差值 |
|---|---|---|---|---|
| DeepSeek V4 Flash | 45 | 27.30% | 26.13% | −1.17 pp |
| Inkling | 45 | 19.99% | 20.45% | +0.46 pp |
| Kimi K3 | 45 | 31.11% | 35.65% | +4.54 pp |
| Qwen3.8 A95B | 45 | 16.79% | 34.97% | +18.18 pp |

若再拆解 Qwen3.8 A95B 按題目類別的表現：

| 類別 | 樣本數 | 未加前綴 | 加入前綴 | 差值 |
|---|---|---|---|---|
| STEM | 15 | 19.26% | 46.24% | +26.99 pp |
| 非 STEM | 15 | 20.62% | 33.42% | +12.80 pp |
| 合成謎題 | 15 | 10.49% | 25.23% | +14.75 pp |
| 全部 | 45 | 16.79% | 34.97% | +18.18 pp |

💡 Qwen 對 GPT-5.5 Pro「有反應」，對 Opus 卻沒有

作者指出，Qwen 在先前以 Opus 4.8 為教師的實驗中幾乎沒有移動，但這次換成 GPT-5.5 Pro 後卻大幅偏移 18.18 個百分點，尤其在私有的合成謎題類別上效果顯著（+14.75 pp）。作者認為這些數據暗示 Qwen 可能學習自 GPT-5.5 Pro，或是與其密切相關的某個 GPT 系模型，而非 Opus。另一個有趣的對照是 Kimi K3：無論加不加前綴，它與 GPT-5.5 Pro 的重疊度本來就是四者中最高的（31.11% 與 35.65%），但前綴帶來的增量只有 +4.54 pp，遠低於 Qwen 的變化幅度。

⚠️ 重疊度不等於因果證據

需要留意的是，這類 n-gram 重疊度量的是「用詞與表達方式的相似性」，作者的措辭也是「suggest（暗示）」而非斷言，這代表結果只能作為一種間接訊號，並不能直接證明特定模型之間存在蒸餾關係。

🎯 實務啟示

對於想要評估開源模型「血統」的工程師，reasoning prefill 提供了一種不需要拿到訓練資料、只靠輸出行為就能做初步側寫的低成本方法；但在下結論前，仍應把它當作統計訊號而非鐵證，尤其在對外討論模型來源時，用詞要跟原作者一樣保守。

🔗 來源
- 標題：Qwen 3.8 follows GPT-5.5 Pro reasoning prefills
- 作者／機構：wsxiaoys（Hacker News）
- 連結：https://gist.github.com/wsxiaoys/e0286dc6bb624ff5fdf49e7f4c528ba3

#LLM #ModelDistillation #Qwen #GPT #ReasoningModels #AIResearch #OpenSourceAI #MachineLearning #KimiK3 #DeepSeek
