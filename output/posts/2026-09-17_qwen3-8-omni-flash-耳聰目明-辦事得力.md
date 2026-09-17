---
title: Qwen3.8-Omni-Flash：耳聰目明，辦事得力
source: Qwen
url: https://qwen.ai/blog?id=qwen3.8-omni-flash
model: claude-code/sonnet
generated_at: '2026-09-17T20:31:09.521952'
score: 108
---

📌 【阿里通義千問】全模態模型不只會看懂，還要動手做完

TL;DR：Qwen3.8-Omni-Flash 把音影片從「輸入」升級成「Agent 的行動載體」，音影片 API 價格直降九成以上。

當多模態模型還在比拼「看得懂多少」的時候，Qwen3.8-Omni-Flash 已經把賽道換了：它不只要理解一段影片在講什麼，還要親自剪輯、配音、寫會議紀要，甚至修改另一個模型的訓練資料。

🤔 **音影片正在從「感知」變成「行動現場」**

官方指出，音影片 Agent 落地生產環境面臨一組系統性難題：長影片的檔案儲存、網路傳輸與多輪推理成本高昂，現有 Agent Harness 框架也缺乏對音影片的原生支援，從全模態理解走到端到端任務執行的範式仍處於早期階段。Qwen3.8-Omni-Flash 的目標，正是把這條鏈路（素材理解 → 任務規劃 → 工具呼叫 → 結果交付）打通。

🧩 **從按需 Caption 到自主取證的長影片理解**

模型支援文本、影像、音訊、影片輸入與 1M 長上下文。針對長影片，它導入了「Agentic 長音影片理解」：不再逐幀處理整部影片，而是從問題出發，自主決定該看什麼、聽什麼，透過由粗到細的多輪取證定位關鍵資訊。官方在 OmniVideoBench 上做了對照實驗：

| 模式 | 準確率（↑） | 每次查詢 Token 消耗（↓） |
|---|---|---|
| Static Understanding | 63.4 | 145,736 |
| Agentic Understanding | 67.8 | 79,117 |

Agentic 模式在準確率提升的同時，Token 消耗降幅約 45.7%。此外模型還具備多說話人音畫協同識別能力，原生支援最長一小時的音影片輸入，能端到端完成說話人切分、內容轉錄與身份對應，用於處理多人會議場景。圍繞這些能力，官方同步開源了 Qwen-MM-Plugins（音影片生產力入口，含 Video2Note、Omni Skill Creator 等工具）與 Qwen-Live Harness（即時全模態互動的執行環境），並推出面向低延遲互動的 Qwen3.8-Omni-Flash-Realtime，支援空間音訊感知（聽聲辨位）與外部 Skill 注入。

📊 **關鍵評測數據**

官方稱在累計 29 項評測中，相比上一代 Qwen3.5-Omni-Plus 平均得分提升超過 25%；音訊輸入 API 價格降幅超過 98%，音影片輸入降幅超過 93%。部分細分評測對比如下：

| 評測 | 類型 | Qwen3.8-Omni-Flash | Qwen3.5-Omni-Plus | Gemini 3.8 Flash | Seed 2.0 Lite |
|---|---|---|---|---|---|
| WildClawBench-MM | Multimodal tool use | 71.0 | 34.5 | 58.9 | 41.9 |
| UniClawBench | Multimodal tool use | 69.6 | 67.1 | 69.0 | 61.2 |
| AgenticVBench | Multimodal tool use | 36.8 | 14.5 | 45.0 | 10.0 |
| OmniGAIA | Web Search | 74.0 | 57.2 | 78.6 | 64.4 |
| OmniVideoBench | Audio-Visual Reasoning | 63.4 | 53.8 | 65.2 | 58.5 |
| AliMeeting（DER\|cpWER，↓） | Multi-Speaker ASR | 3.4\|17.2 | 88.1\|89.6 | 72.6\|53.1 | 75.1\|76.1 |

官方也提到，音影片能力已接近 Gemini 3.8 Flash，音訊能力整體超過 Gemini 3.8 Flash。

💡 **讓大模型去最佳化小模型：一次 12 小時實驗**

團隊向 Qwen3.8-Omni-Flash 下達任務：在 12 小時內提升 Qwen2.5-Omni-3B 的四川話識別能力。模型自主選定評測集、固定評測標準、完成基線測試，聽取語音樣本診斷問題並構建訓練資料，連續 4 輪實驗累計構建 3,413 條訓練資料，並根據評測反饋保留有效改進、回退無效嘗試。最終 Qwen2.5-Omni-3B 在同一評測集上的字元錯誤率從 25.79% 降至 15.30%，相對下降約 40.7%。這展示了「大模型負責研發、小模型面向業務」的另一種模型演進路徑。

🎯 **實務啟示**

對於正在建置音影片 Agent 工作流的工程師，Agentic Understanding 的多輪取證機制值得參考：與其對長影片做全量處理，不如讓模型先假設、再按需取證，能同時省 Token 又提準確率。而「大模型驅動小模型最佳化」的實驗流程，也提供了一種低人力介入、資料驅動迭代模型能力的範式。

🔗 **來源**
- 標題：Qwen3.8-Omni-Flash：耳聰目明，辦事得力
- 作者／機構：Alibaba（Qwen）
- 連結：https://qwen.ai/blog?id=qwen3.8-omni-flash

#Qwen #Alibaba #MultimodalAI #OmniModel #AIAgent #VideoUnderstanding #LLM #SpeechRecognition #AgenticAI #GenerativeAI
