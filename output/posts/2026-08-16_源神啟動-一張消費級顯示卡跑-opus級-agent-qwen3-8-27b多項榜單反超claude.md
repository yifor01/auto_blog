---
title: 源神啟動！一張消費級顯示卡跑“Opus級”Agent，Qwen3.8-27B多項榜單反超Claude
source: 量子位
url: https://www.qbitai.com/2026/08/473669.html
model: claude-code/sonnet
generated_at: '2026-08-16T06:07:53.687737'
score: 96
---

📌 270億參數 Qwen3.8-27B：一張消費級顯卡跑贏 Claude Opus

TL;DR：Qwen3.8-27B 在多項程式碼與 Agent 榜單超越 Claude Opus 4.6 Max，且能塞進單張消費級顯卡。

開發者苦等已久的 Qwen3.8-27B 終於開源。270 億的總參數量，卻在官方多項軟體工程與 Agent 評測中壓過體型大得多的 Claude Opus 4.6 Max，這個反差正是它引爆討論的原因。

🤔 270億參數，為什麼讓 Claude 有點緊張

社群之所以持續催更這個型號，一個很現實的原因是：這回自家電腦真有機會帶得動。270 億參數經過量化後，24GB VRAM 的 RTX 3090、4090 這類消費級顯卡就有機會把整個模型裝下。尺寸縮小的同時，上下文長度完全沒有妥協，原生支援 262K token，還可以繼續擴展到 100 萬 token。這一代重點強化的方向是程式設計、專業工作、研究與長程 Agent 任務。

📊 SWE-bench Pro 領先 Opus 4.6 Max 8.3 分

官方 benchmark 給出的對比相當直接：

| 評測項目 | Qwen3.8-27B | Claude Opus 4.6 Max |
|---|---|---|
| SWE-bench Pro（Agent 程式設計） | 領先 8.3 分 | — |
| QwenSWEBench（軟體工程） | 領先 15.2 分 | — |
| CoWorkBench（電腦／金融／法律／醫療長任務 Agent） | 70.7 | 68.2 |
| OSWorld-Verified（電腦操作） | 84.3 | 72.7 |
| AndroidWorld（手機操作） | 81.9 | 62.0 |
| WebArena-Verified（瀏覽器操作） | 64.8（前代 48.8） | — |

多模態能力方面，官方數據顯示 Qwen3.8-27B 在開啟 CI 後，視覺數學問題解決拿到 94.6 分，是同排可見模型中的最高成績；通用視覺推理開啟 CI 後為 85.6 分，相較不開 CI 的 65.7 分有明顯提升。

🧩 64 層裡 48 層線性注意力，撐起 262K 原生上下文

要在小尺寸下扛住長任務，底層架構也得下功夫。Qwen3.8-27B 一共 64 層，其中 48 層採用 Gated DeltaNet 線性注意力，16 層保留完整 attention，大致按照「三層線性注意力＋一層完整 attention」的節奏循環。線性注意力負責降低長序列下的計算與快取壓力，完整 attention 則每隔幾層做一次更充分的資訊互動，這也是它能把原生上下文做到 262K、還能擴展到 100 萬 token 的關鍵。

💡 推理檔位、preserve_thinking，開發者已經開始暴力測試

模型預設開啟 Thinking 模式，並支援 reasoning_effort 調節推理深度，分成 xhigh、medium、low 三檔：複雜程式碼或長程 Agent 任務可拉高檔位，簡單問答、摘要則可降檔換取速度與成本；Thinking 本身也能直接關閉。另外預設開啟 preserve_thinking，讓 Agent 前幾輪的推理過程能留在後續上下文裡，例如 Coding Agent 連續改十幾個檔案時，可以沿著先前的決策繼續走，也更利於 KV cache 重複使用。

社群已經開始各種實測：有人用 3.8-27B 與前代 3.6-27B 分別做像素風寶塔，3.8-27B 在色彩細節與結構上明顯更好；有人做出俄羅斯方塊，模型還自行加上了掉落震動與消除行時的獎勵倍增器效果。有網友把 Qwen3.8-27B-FP8 放上一張 NVIDIA GH200，同時跑 10 個真實請求，每個最高輸出 16K token、上下文拉到 262K，結果首批串流 token 幾乎都在 10 毫秒內返回，10 個請求全數正常完成。也有人丟給模型一部 1935 年的 11 分鐘電影，讓它辨識 96 個帶時間戳的事件並逐字引用畫面文字，157 秒完成，時間點誤差約 2 秒，且整個過程只用單張 GPU。官方已經接上 Transformers、vLLM、SGLang 與 TokenSpeed，生產環境建議用 SGLang、vLLM 這類 serving 引擎，Hugging Face 也提供了量化版本供本地部署。

🎯 實務啟示

如果手上有高階消費級顯卡或大記憶體 Mac，這是少數能在本地跑出「Opus 級」Agent 體驗的開源選項；reasoning_effort 檔位與 preserve_thinking 這類細節，也值得其他框架在設計長程 Agent 時參考。

🔗 來源
- 標題：源神啟動！一張消費級顯示卡跑"Opus級"Agent，Qwen3.8-27B多項榜單反超Claude
- 作者／機構：夢瑤 @ 量子位
- 連結：https://www.qbitai.com/2026/08/473669.html

#Qwen #OpenSource #LLM #AIAgent #Coding #SWEBench #LocalLLM #Multimodal #LongContext #ConsumerGPU
