---
title: Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things
source: Simon Willison
url: https://simonwillison.net/2026/Aug/16/qwen-38-27b/
model: claude-code/sonnet
generated_at: '2026-08-25T06:23:14.516708'
score: 93
---

📌 【實測筆記】Qwen 3.8 27B 很能打，但預設「想太多」

TL;DR：Qwen 3.8 27B 效能亮眼，但預設 reasoning 設定會讓簡單任務也想過頭。

請 AI 畫一個圓形，它想了好幾分鐘，最後端出一個你根本沒要求的動畫版本——這是 Simon Willison 實測 Qwen 3.8 27B 時真實遇到的狀況。

🤔 **一顆適合筆電跑的 27B 模型**

Qwen 3.8 27B 是 Alibaba Qwen 研究團隊釋出的 Apache 2 授權、27B 參數、具視覺能力的 LLM。作者指出 27B 是在一般規格筆電上跑模型的理想大小，前代 Qwen 3.6 27B 表現就已經令人印象深刻。Qwen 官方自報的 benchmark 顯示，這次不只贏過 Qwen 3.6 27B，也贏過今年五月時仍是 Qwen 最強模型之一的閉權重版本 Qwen 3.7-Plus（作者宣稱，尚待獨立 benchmark 驗證）。

🧩 **預設 xhigh：一個「很好笑」的設定**

作者分別在 128GB M5 Max MacBook Pro 與 NVIDIA DGX Spark 上，透過 LM Studio 執行 17GB 的 Q4_K_M 量化版本，也在 Spark 上直接用 llama-server 測試。Qwen 官方文件說明模型支援 reasoning_effort 參數可調整推理深度，而作者使用的 LM Studio GGUF 建置版本保留了官方預設的 xhigh（超高）設定。作者形容這是「hilarious default（很好笑的預設值）」，並直言這絕對不是在消費級硬體上執行模型的好方式。

一開始作者就遇到 LM Studio 預設 8,192 tokens context 上限的問題：Qwen 光是思考最普通的問題就會把額度用光，把 context 拉到 262,144 tokens 上限後問題才解決。

📊 **同一個提示，21 分鐘 vs 2 分鐘**

以「畫一隻騎腳踏車的鵜鶘」SVG 為例，xhigh 預設下第一次嘗試花了 21 分鐘，用掉 22,276 個 reasoning tokens 才產出 3,223 tokens 的輸出，作者評價這是他在本地機器上生成過最好的鵜鶘 SVG。同一提示詞若關閉 reasoning，則只花 137 秒（約兩分多鐘）就產出 3,715 tokens 的結果。

換成單純「畫一個圓形」的簡單提示，reasoning trace 卻自行決定加上同心引導圓、刻度、漸層填色與旋轉動畫等額外設計，最終產出一個「美麗的動畫圓形」，完全不是作者原本要的東西。

在 bounding box 視覺任務上，作者要求以 0–1000 尺度標出照片中鵜鶘的位置，模型給出的框選結果相當精準。作者接著用這個模型離線建置了一個自訂視覺化工具，能讀入圖片與 JSON 座標、依實際圖片尺寸換算並畫出標註框；雖然忘記調低思考程度導致工具被過度工程化，模型仍一次性（one-shot）產出完整介面，甚至自行加上一個未被要求的「demo 場景」功能，用 canvas 畫出示意用的鵜鶘輪廓（純粹因為範例 JSON 裡用了「pelicans」這個標籤）。若關閉 reasoning 重試，模型沒能一次做對，標註框位置出現偏差。

在 coding agent 測試中，作者用系統提示較短、適合小模型的 Pi，透過 tailscale serve 分享 Spark 上 LM Studio 執行的 Qwen 3.8 27B，在自己的 datasette 專案資料夾中提出需求。模型經過多輪推理與工具呼叫、存取多個檔案後，給出的回覆被作者評為「相當紮實」。作者接著請它寫一段 Python 程式，把 Pi 的 JSONL 對話紀錄轉成 Markdown，模型也順利完成並通過測試。

💡 **想太多，到底值不值得**

作者的結論是「或許至少有一部分是必要的」：在 bounding box 視覺化工具的案例中，關閉 reasoning 後模型沒能一次做對，顯示對需要多步驟規劃與工具建置的任務，reasoning 確實帶來實質差異；但對單純的 SVG 繪圖或畫圓形這類簡單請求，過度思考反而導致離題、浪費大量時間。

⚠️ **仍是初步、單人測試**

以上結果都是作者個人在有限任務上的實測觀察，尚未有獨立第三方 benchmark 驗證 Qwen 官方宣稱的效能提升，coding agent 的測試也僅止於單一 session 的初步嘗試。

🎯 **實務啟示**

若要在消費級硬體本地部署 Qwen 3.8 27B，第一步就該手動調整 reasoning_effort（或直接關閉），並將 context window 開到接近上限，否則連簡單任務都可能等上 20 分鐘。對需要長 context、程式碼生成與 tool-calling 的 coding agent 場景，這次初步測試結果偏向正面，值得工程師進一步評估其在本地 agent loop 中的實用性。

🔗 **來源**
- 標題：Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Aug/16/qwen-38-27b/

#Qwen #LocalLLM #OpenSourceAI #ReasoningModels #LLMOps #CodingAgent #VisionLanguageModel #Alibaba #OnDeviceAI #PromptEngineering
