---
title: NVIDIA Vera Rubin and Blackwell Set a New Standard for Agentic AI Performance
  per Watt
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/nvidia-vera-rubin-and-blackwell-set-a-new-standard-for-agentic-ai-performance-per-watt/
model: claude-code/sonnet
generated_at: '2026-08-25T06:20:11.570488'
score: 106
---

📌 【NVIDIA】Vera Rubin 對 Blackwell：Agentic AI 每瓦效能新標竿

TL;DR：SemiAnalysis AgentX 基準測試顯示，Vera Rubin NVL72 每百萬瓦吞吐量最高比 GB300 NVL72 高 30 倍。

當一個 coding agent 開始工作，它不再只是回答一句話，而是不斷推理、呼叫工具、協調子任務，並把愈滾愈大的上下文一路帶到下一輪。OpenRouter 的 State of AI 報告分析了 100 兆個 token 的真實使用量，發現平均每次請求的 prompt token 數成長了約四倍，而單一 agentic 請求消耗的 token 量，是一般對話請求的 15 倍。這種轉變讓「怎麼評測硬體效能」變成一個新問題。

🤔 舊基準測不出真實 agent 流量

過去 InferenceX 套件慣用的靜態 8K/1K（輸入 8K、輸出 1K）序列長度測試，在 DeepSeek-R1-0528 上顯示 GB300 NVL72 每百萬瓦 token 吞吐量最高領先 H200 達 40 倍。但這種固定長度情境代表的是受控、規律的服務模式，而非真實 agent 產生的流量：請求長度逐輪變化、上下文不斷累積、部分 token 可被重複利用、模型呼叫還會被工具執行或子任務中斷。隨著 agentic AI 成為主流工作負載，這類固定序列長度的測試已被降格為 InferenceX 套件中的「維護模式」。

🧩 AgentX：用真實 Claude Code 對話重播測效能

AgentX 是 SemiAnalysis 開源基準套件 InferenceX 中，專門針對 agentic coding 推理設計的基準測試。它會用 AIPerf 客戶端逐輪重播預先錄製的 Claude Code 對話 session，保留原始 session 的上下文、輸入輸出序列長度，以及推理與工具呼叫的實際延遲間隔，藉此重現真實情境下 KV cache 容量的壓力。由於每套系統都收到相同的重播流量，觀察到的差異反映的是服務堆疊（serving stack）本身的效能，而非針對基準測試的特調。

AgentX 會在不同並發量下量測「每百萬瓦吞吐量」（tokens per megawatt），並同時報告四項使用者體驗指標：

| 指標 | 定義 | 用途 |
|---|---|---|
| E2E Normalized Interactivity | 總輸出 token 數除以從請求送出到最後一個 token 送達的時間 | 反映含首字延遲在內的整體每瓦可用輸出量，越高越好 |
| Standard Interactivity | 生成階段的每使用者 token 速率（首字後到末字的輸出 token 數） | 反映開始生成後的每瓦串流輸出量，越高越好 |
| E2E Latency | 單一請求從送出到最後輸出 token 送達的總耗時 | 檢驗高效能是否仍在可接受時間內完成，越低越好 |
| TTFT | 從送出請求到第一個輸出 token 送達的時間 | 反映首次回應速度，對重複開啟長上下文對話的 agent 尤其關鍵，越低越好 |

📊 Vera Rubin 30 倍、GB300 最高 80 倍於 H200

以下數據為 NVIDIA 使用 SemiAnalysis AgentX 工作負載測得，尚待 SemiAnalysis 審核：

- 在 AgentX 的 DeepSeek V4-Pro 工作負載、每使用者每秒 160 個 token 的互動水準下，Vera Rubin NVL72 每百萬瓦吞吐量最高比 GB300 NVL72 高 30 倍。
- 在 DeepSeek V4 Pro 1.6T 上，GB300 NVL72 每百萬瓦吞吐量最高比 H200 NVL8 高 15 倍，換算成單位經濟效益，GB300 NVL72 每百萬 token 成本最高比 H200 NVL8 低 10 倍。
- 模型規模愈大，優勢愈明顯：在 Kimi K3 2.8T 上，GB300 NVL72 每百萬瓦吞吐量約為 H200 NVL8 的 80 倍，並把互動水準的上限從 H200 NVL8 的範圍延伸到約每使用者每秒 215 個 token。

💡 效能背後是整套服務堆疊的協同工作

文章指出，GB300 NVL72 的這些結果來自服務執行時期（serving runtime）、模型 kernel 與 scale-up fabric 的系統級整合，這些層面共同讓大型 MoE 模型在 agent session 累積上下文、並發量上升、解碼需求增強時，仍能維持有回應力的吞吐量。SGLang、TensorRT-LLM、vLLM 等 MoE 服務執行框架，都能把專家（expert）運算分散到 NVL72 的運算網域中執行。

🎯 實務啟示

對正在規劃 agentic 推理基礎設施的團隊來說，這份基準提醒了一件事：評估硬體不能只看靜態、固定長度的傳統跑分，而要看它在真實 agent 流量下，能否在給定的功耗與電力預算內維持可接受的互動體驗。這直接關係到單位 token 成本與整體服務容量的規劃。

🔗 來源
- 標題：NVIDIA Vera Rubin and Blackwell Set a New Standard for Agentic AI Performance per Watt
- 作者／機構：Elizabeth Goodman（NVIDIA Developer）
- 連結：https://developer.nvidia.com/blog/nvidia-vera-rubin-and-blackwell-set-a-new-standard-for-agentic-ai-performance-per-watt/

#NVIDIA #VeraRubin #Blackwell #AgenticAI #InferenceX #AgentX #MoE #GPU #AIInfrastructure #PerformancePerWatt
