---
title: NVIDIA Vera Rubin NVL72 Leads Agentic Inference Performance on MLPerf Endpoints
  v1.0
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/nvidia-vera-rubin-nvl72-leads-agentic-inference-performance-on-mlperf-endpoints-v1-0/
model: claude-code/sonnet
generated_at: '2026-11-17T01:03:12.515408'
score: 91
---

📌 NVIDIA Vera Rubin NVL72 首秀 agentic 推理：每瓦吞吐量看齊 GB300 十倍

TL;DR：MLPerf Endpoints v1.0 顯示 Vera Rubin NVL72 在 agentic 推理每瓦吞吐量可達 GB300 NVL72 十倍以上，直接牽動 agent 部署的硬體成本估算。

AI agent 的對話歷史會隨著回合數不斷累積，一來一回之間混雜著推理、工具呼叫與回覆，這種負載模式對推理系統是全新的考驗：系統要同時服務大量使用者，又不能犧牲回應速度。MLPerf Endpoints v1.0 正是為了評測這種平衡而設計，而 NVIDIA 公布的 Vera Rubin NVL72 provisional 成績，交出了一份相當有份量的答卷。

🤔 Endpoints 怎麼測「agentic」

MLPerf Endpoints v1.0 透過真實 API 端點，用程式設計（coding）與企業工作流（enterprise workflow）兩類資料集進行評測。在效能測試過程中，系統產生的工具呼叫與 workflow 意圖會被拿去跟參考答案核對；另外還有獨立的 SWE-bench Verified 評測，檢驗端到端任務的實際解題能力，確保「服務得更快」沒有犧牲模型品質。資料集本身也反映了真實 agentic 負載的特性：coding 任務會隨著回合累積越來越長的歷史，企業工作流則反覆重複使用共享的指令、工具定義與業務規則，context 長度隨著互動持續拉長。

📊 Kimi K3、DeepSeek-V4.1-Flash、Qwen3.6-35B-A3B 全面領先

在 Kimi K3 的測試中，Vera Rubin NVL72 用 32 顆加速器、併發 1,024 筆查詢，在端到端互動性（E2E interactivity）達到每使用者每秒 50.4 tokens 的情況下，系統總吞吐量達 41,414.2 tokens/秒，運作功耗 100.89 kW；相比之下，GB300 NVL72 用 48 顆加速器、併發 48 筆查詢，互動性 56.2 tokens/秒時，系統吞吐量僅 2,210.4 tokens/秒，功耗 60 kW。換算成每千瓦吞吐量，Vera Rubin 的優勢超過 10 倍。

| 模型 | 每瓦吞吐量提升倍數 | E2E 互動性提升倍數 |
|---|---|---|
| Kimi K3 | 10x | 3x |
| DeepSeek-V4.1-Flash | 9x | 5x |
| Qwen3.6-35B-A3B | 5x | 3x |

三個模型的結果方向一致：在相同功耗預算下，Vera Rubin 能撐起更高的吞吐量；在相同併發數下，使用者感受到的互動速度也明顯更快。

🧩 硬體與軟體怎麼一起發力

硬體層面，Rubin GPU 結合了 HBM4 記憶體、Tensor Core 與第六代 NVLink：HBM4 讓模型權重與對話狀態的存取更快，Tensor Core 加速矩陣運算，NVLink 則負責 GPU 之間的高速通訊。軟體層面，NVIDIA 強調「context-aware serving」：透過 prefix caching（前綴快取）與狀態重用，減少重複計算；NVIDIA Dynamo 負責在多個 worker 之間分配請求、平衡負載；disaggregated serving 則讓 prefill（提示處理）與 decode（逐 token 生成）可以分開獨立最佳化，因為這兩個階段對運算資源的需求本質上不同。

🎯 實務啟示

對要規劃 agent 部署規模的團隊來說，這組數據的意義很直接：同樣的電力預算下可以同時跑更多 agent，而且在併發量較低時，回應延遲也會更短，這對重視即時互動的 agentic 應用特別關鍵。

⚠️ 需要留意的是，文中 Vera Rubin 的所有數字都標註為 provisional（暫定），尚待 MLCommons Association 驗證，正式結果公布前仍可能調整；GB300 的對照數字則已通過驗證。

🔗 來源
- 標題：NVIDIA Vera Rubin NVL72 Leads Agentic Inference Performance on MLPerf Endpoints v1.0
- 作者／機構：Zhihan Jiang, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/nvidia-vera-rubin-nvl72-leads-agentic-inference-performance-on-mlperf-endpoints-v1-0/

#NVIDIA #VeraRubin #MLPerf #AgenticAI #Inference #GPU #LLMServing #AIInfrastructure #NVLink #DataCenter
