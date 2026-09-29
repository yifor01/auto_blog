---
title: Jeff – Jev-compatible 0.8B decision models, trained at home, ~30 ms
source: Hacker News
url: https://github.com/firelex/jeff
model: claude-code/sonnet
generated_at: '2026-09-29T21:40:21.886574'
score: 100
---

📌 Jeff：家用單卡 GPU 就能練出的 0.8B 決策模型

TL;DR：開源專案 Jeff 用一張工作站 GPU 完成訓練，30 毫秒內就能做出多選項的零樣本決策判斷。

談到訓練語言模型，直覺會想到動輒數百張 GPU 的資料中心。但 Jeff 這個獨立開源專案，只用一張 RTX PRO 6000 workstation GPU 就在本地把 0.8B 與 2B 的決策模型練了出來，推論延遲只要 22 毫秒。

🤔 為什麼需要「決策模型」而不是聊天模型

許多正式環境需要的不是生成文字，而是「在幾個選項裡選一個」：客服要分流到哪個 team、語音助理聽到的指令對應哪個動作、遊戲角色該往哪走。這類任務若丟給一般 LLM 生成文字再 parse，既慢又不穩定。Jeff 鎖定的正是這個場景：輸入一段情境描述與任意數量的選項（zero-shot，選項不需要出現在訓練資料裡），模型直接對每個選項回傳一個校準過的機率，單次 forward pass 完成，不用生成文字也不用 parsing。

🧩 與 Jev 相同介面，重點在「小而快」

Jeff 是 Qwen3.5 與 Gemma4 的 fine-tune 版本，採用與 Jev 相同的 request 格式（兩者無關，Jeff 是獨立專案，不隸屬 Jev 開發商 TypeSafe；訓練程式碼則從開源的 AutoJev recipe 起步）。它支援三種問題型態：choice（在最多 254 個選項中選一個，這是 v1.1 版 Qwen 模型才有的上限，Gemma4 版本仍是 26 個）、noul（yes/no 的機率）、score（在自訂量表上打分），而且一次 request 可以同時問多個獨立問題。

最值得注意的是訓練方式完全在本地完成：0.8B 模型約訓練 2 小時、2B 約 3.5 小時，都在一張 RTX PRO 6000 上跑完；訓練資料是由開源模型 Qwen3.8-Flash-Next 在兩臺 DGX Spark 上生成的合成資料，測試則在 MacBook 上進行。作者強調沒有用任何雲端 GPU，訓練資料裡也沒有 closed model 的輸出，closed model 僅用來抽樣檢查合成資料品質。

📊 效能與 benchmark 數據

0.8B 模型在 RTX PRO 6000 上推論約 22 毫秒、在 Apple M4 Max（透過 MLX）約 28 毫秒。在五個公開 benchmark（BBH、Financial PhraseBank、JudgeBench、RAGTruth、WinoGrande）的平均分數上：

| 模型 | 平均分（5 benchmarks） |
|---|---|
| Qwen3.5-0.8B（未訓練） | 45.3 |
| Jeff-Qwen3.5-0.8B | 79.1 |
| Qwen3.5-2B（未訓練） | 46.5 |
| Jeff-Qwen3.5-2B | 82.0 |
| Gemma4 E2B（未訓練） | 62.5 |
| Jeff-Gemma4-E2B | 81.6 |
| Jev（官方公布） | 83.0 |
| AutoJev-27B（官方公布） | 84.9 |

在分類與 grounding 類任務上，Jeff 已經追平甚至打敗更大的 Jev；但在偏推理的 benchmark（BBH、JudgeBench，以及 JevBench 的困難題）上，Jeff 明顯落後，作者也坦言這是小模型的預期結果。v1.1 版本另外做了「長列表測試」，0.8B 模型表現從 40% 大幅提升到 95%，但 2B 模型在原本 benchmark 上分數略降（83.1% 降到 82.0%）。

作者也用 Doom、Frogger、Pac-Man 三款遊戲做 zero-shot 測試，每回合把情境與合法動作都轉成文字描述讓模型選擇。0.8B 版本在 Doom 和 Frogger 上的表現與手寫規則 bot 相當，每步推論僅需 29 到 49 毫秒（M4 Max 上），對照 Jev 在 Doom 上透過 API 呼叫平均 212 毫秒（兩者測試硬體不同，僅供參考）。

如果 zero-shot 準確率不夠用，README 還給出了一個 fine-tune 範例：用 60 萬筆 Lichess 棋局（Stockfish 標註）訓練 Jeff-Qwen3.5-0.8B，3.5 小時內把 1000 題測試棋局的解題率從 zero-shot 的 15.5% 推到 55.8%（未訓練模型僅 6.2%）。作者澄清這不是強棋力（約 1000 Elo、無搜尋），重點是速度：一張 GPU 就能同時跟上約 600 場人類 blitz 對局的節奏。

⚠️ 這是什麼，也不是什麼

作者講得很清楚：這些是很小的模型，擅長在選項之間做出快速、校準良好的判斷，適合嵌進本地程式；但推理能力比不上跑在更大模型上的 Jev。若 zero-shot 準確率不夠，一個小規模的 fine-tune（README 提到的語音導航案例，半小時內把 held-out 準確率從 31.7% 推到 95.8%）通常能帶來更大幅度的提升。

🎯 實務啟示

如果你的系統裡有大量「選 A 或 B 或 C」的判斷邏輯（intent 分類、內容審核、路由決策），與其呼叫大型 LLM 生成文字再 parse，Jeff 這類 zero-shot 決策模型提供了更省資源的選項：單次 forward pass、幾十毫秒延遲，還能用少量自有資料快速 fine-tune。對想在本地或邊緣裝置跑推論、預算有限的團隊，這是值得列入評估清單的開源方案。

🔗 來源
- 標題：Jeff – Jev-compatible 0.8B decision models, trained at home, ~30 ms
- 作者／機構：firelex
- 連結：https://github.com/firelex/jeff

#AI #MachineLearning #OpenSource #LLM #ZeroShot #EdgeAI #ModelFineTuning #DecisionModels #Qwen #GitHub
