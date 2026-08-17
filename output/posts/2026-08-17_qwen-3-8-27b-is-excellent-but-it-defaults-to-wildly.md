---
title: Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things
source: Simon Willison
url: https://simonwillison.net/2026/Aug/16/qwen-38-27b/
model: claude-code/sonnet
generated_at: '2026-08-17T06:16:40.831481'
score: 96
---

📌 Qwen3.8 27B 效能驚艷，卻預設瘋狂過度思考

TL;DR：Alibaba Qwen 團隊推出 27B 開源視覺模型，效能亮眼但預設推理強度過高，實測 21 分鐘才畫出一張 SVG。

一個只是要求畫圓形 SVG 的簡單請求，模型卻思考了好幾分鐘，最後端出一個帶動畫效果的幾何藝術品——完全不是使用者要的東西。這是 Simon Willison 這週實測 Qwen3.8 27B 的真實體驗。

🤔 一顆「思考過頭」的模型

Alibaba 旗下 Qwen 研究團隊推出的 Qwen3.8 27B，是一款採用 Apache 2 授權、支援視覺輸入（vision-capable）的 27B 參數 LLM。27B 這個大小，剛好適合在規格不錯的筆電上跑，前代 Qwen3.6 27B 表現就已經令人印象深刻。Qwen 官方公布的 benchmark 顯示，這款新模型同時超越了 Qwen3.6 27B，以及今年五月時仍是 Qwen 陣營最強模型之一的閉源版本 Qwen3.7-Plus。

問題出在哪？Qwen 官方文件提到，模型支援 reasoning_effort 參數可調整推理深度與成本，但預設值卻是「xhigh」（超高）。Simon Willison 實測用的 LM Studio GGUF 版本延續了這個預設，結果就是模型會為了最平凡的問題也拉滿思考長度。

🧩 21 分鐘的鵜鶘與意外的動畫圓形

Simon 在兩臺機器上測試：128GB 記憶體的 M5 Max MacBook Pro，以及 NVIDIA DGX Spark，兩邊都用 LM Studio 搭配 17GB 大小的 Q4_K_M 量化版本（也在 Spark 上直接用 llama-server 試過）。他一開始碰到 LM Studio 預設 8,192 tokens 的 context 上限，模型光是思考就把額度用光，把 context 拉到最大的 262,144 tokens 後問題才解決。

他慣用的「畫一隻騎腳踏車的鵜鶘 SVG」測試題，這次花了 21 分鐘，用掉 22,276 個推理 tokens，才產出 3,223 tokens 的最終輸出，但結果是他在本機模型中看過最好的鵜鶘 SVG 之一，而模型檔案只有 17GB。關掉推理功能後，同樣的提示只花 137 秒（約兩分鐘）就產出 3,715 tokens 的結果。

更荒謬的例子是單純要求「畫一個圓形的 SVG」，模型在推理過程中自行決定要做一個「有層次、帶動畫」的幾何藝術作品，加上同心輔助圓、刻度標記、漸層與緩慢旋轉的虛線環，結果完全偏離了使用者的簡單需求。

📊 視覺任務與 coding agent 實測

Qwen 過去幾代模型在物件框選（bounding box）任務上表現不錯，Simon 這次要求模型框出照片中鵜鶘的位置，採用 0-1000 座標縮放格式，結果框選精準度相當高。他甚至讓 Qwen3.8 27B 在離線狀態下，直接寫出一個能視覺化這些 bounding box 的 HTML 小工具。由於忘記關掉高強度推理，這個工具被「過度工程化」，還多做了一個沒被要求的功能：自己畫兩隻鵜鶘剪影作為示範場景，因為提示裡的範例 JSON 用了「pelicans」這個標籤。關掉推理後重試，工具幾乎能動，但框選位置有誤，顯示在這類任務上推理確實帶來實質差異。

Simon 也測試了模型能否勝任 coding agent 迴圈。他選用系統提示較短的 Pi 這款 agent 工具，透過 tailscale serve 把跑在 DGX Spark 上、由 LM Studio 提供服務的 Qwen3.8 27B 接進 Pi，對自己的 datasette 專案下指令，得到一份紮實的回覆。他接著要求模型把 Pi 產生的 JSONL 對話紀錄轉成 Markdown，模型順利寫出並自行測試了一支 pi_jsonl_to_md.py，成功達成任務。

💡 一顆 17GB 的全能小模型

綜合這些測試，Simon 認為這顆僅 17GB 大小的模型，已經具備長 context、可靠的程式碼生成與 tool-calling 能力，足以應付撰寫程式碼、驅動工具、標註影像等日常工作，是目前能在消費級硬體上運作的高手感模型之一。

🎯 實務啟示

若打算在本機部署 Qwen3.8 27B，第一件事就是把 reasoning_effort 調低，並確認 context window 不要卡在工具預設的 8,192 tokens，否則模型會把大把時間花在思考瑣事上。對於需要精準輸出（如視覺定位、結構化工具生成）的任務，適度保留推理能力仍有其價值，但日常對話與簡單請求，關掉高強度推理反而更務實。

🔗 來源
- 標題：Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Aug/16/qwen-38-27b/

#Qwen #LLM #OpenSource #LocalLLM #LLMOps #AIAgents #VisionLanguageModel #AIWeights #EdgeAI #Reasoning
