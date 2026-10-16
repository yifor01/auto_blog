---
title: 'Granite Switch 4.1: Chat, Decisions, and Speech from One Endpoint'
source: HuggingFace Blog
url: https://huggingface.co/blog/ibm-granite/granite-switch-4-1
model: claude-code/sonnet
generated_at: '2026-10-16T20:12:47.807617'
score: 91
---

📌 一個端點搞定聊天、決策與語音：IBM Granite Switch 4.1

TL;DR：IBM 用 cache 共享的 aLoRA 把聊天、決策分類與語音轉文字塞進同一個模型端點，省下大量 GPU。

企業導入 AI 時常見的痛點是：聊天要一個模型，內容安全審核要另一個分類器，語音轉文字又要再掛一套 ASR 服務，三套系統各吃各的 GPU 記憶體。IBM Granite Switch 4.1 想解決的正是這個「一個任務一個模型」的資源浪費問題。

🤔 **從模組化專案到三合一端點**

去年春天啟動的 Granite Switch 專案主張模組化的模型開發方式：用輕量的 adapter 疊加在同一個基底模型上，而不是為每個任務各自微調一整個模型。這次的 Granite Switch 4.1（8B 與 30B 兩種尺寸）把三樣能力整合進單一端點：一個通用決策用的 Decision aLoRA（例如對應 v1/systemone）、一個在安全相關決策任務上平均優於 Jev 1.13、Microsoft-Decision-1、GPT-Luna-Decisions 與 Clef-Flash 的專用 Guardian aLoRA，以及內嵌的 Granite-Speech-5.0-Turbo-CTC，也就是 OpenASR Leaderboard 上最快的 ASR 模型。

🧩 **關鍵設計：aLoRA 共享 KV cache**

這三項技術加上底層基底模型被組合成一個模型，所佔用的 GPU VRAM 大約只等同於單獨跑基底模型本身，也就是用更少 GPU 做到更多能力。其技術關鍵是這些 Switch adapter 是用「cache 效率高」的 Activated LoRA（aLoRA）打造的：基底模型產生的 KV cache 可以被後續任何基於 adapter 的決策任務重複利用，再搭配團隊近期對 vLLM 的貢獻（加速低秩 adapter 推理）以及共置的 ASR encoder，模型就能在聊天請求、決策請求與語音請求之間快速切換。IBM 也提供了一個 Speech-to-Decisions 的 HF Space 示範：granite-switch-4.1-8b 可以即時轉錄音訊、生成摘要、篩選有害內容，並同時檢測使用者自訂的 15 項其他標記，全部在同一個端點上完成。

📊 **專用 adapter 打敗通用決策模型**

IBM 先前釋出的 Granite Libraries 提供一系列專用「決策模型」adapter 與其他任務 adapter，可自由組合成客製化的 Granite Switch 模型。摘要指出，雖然 Jev 等閉源決策模型主打通用性，但許多 granitelib 的專用 adapter 在特定分類任務上能超越通用型決策模型，而且因為 adapter 共享基底模型的 KV cache，疊加專用 adapter 的成本幾乎可以忽略，等於同時拿到通用模型的廣泛覆蓋與專用模型的更高準確率。在一場「賽跑」實測中，Granite-Switch-4.1-30B（凍結的 Granite 基底 + 4 個專用 aLoRA）在真實世界的 5 步驟 RAG 工作流程中，完成速度明顯快於對手 Jev-27B（凍結的 Qwen 基底 + 1 個通用決策 LoRA）。

一個更直觀的例子是拿 Doom 遊戲當測試場：一個客製化的 3B 參數 Granite Switch 模型以每秒 60 到 100 次決策的速度在遊戲中導航，相較於 Jev 官方報告的每秒 10 次決策；而且與 Jev 不同，這個 Granite Switch 模型還能在玩遊戲的同時用語音敘述狀況並回答使用者的問題。

🧩 **怎麼用**

Granite-Switch-4.1-8B 與 -30B 是「內建電池」的版本,已經搭配好一組預設的實用 adapter，但使用者不一定要用 IBM 預設的組合，任何人都能用 Granite Libraries 裡的 adapter 自由混搭出客製化的 Granite Switch 模型。模型可在 vLLM 搭配插件執行，也原生支援 llama.cpp 及下游平臺，能無縫替換任何呼叫 /v1/systemone API 的場景，同時仍服務傳統聊天呼叫，並共享同一份 prefix cache。IBM 也預告將釋出 Adapter SDK，讓社群可以在 Mellea 中訓練自己的 adapter，並提供更多教學與 Granite Switch 支援。

🎯 **對企業 AI 架構的實務啟示**

如果你的系統正同時維運聊天模型、內容審核分類器與語音轉文字服務，Granite Switch 的 aLoRA + 共享 KV cache 架構提供了一個值得參考的方向：把多個任務收斂到同一個基底模型上疊加輕量 adapter，而不是為每個任務各自部署一套模型，可能是降低 GPU 成本同時維持甚至提升專項準確率的可行路徑。

🔗 **來源**
- 標題：Granite Switch 4.1: Chat, Decisions, and Speech from One Endpoint
- 作者／機構：Kate Soule, Subhajit Chaudhury, Hendrik Strobelt, Luis A Lastras（IBM Granite）
- 連結：https://huggingface.co/blog/ibm-granite/granite-switch-4-1

#GraniteSwitch #IBM #aLoRA #LoRA #OpenSourceAI #ModelAdapters #ASR #AIInfrastructure #vLLM #EnterpriseAI
