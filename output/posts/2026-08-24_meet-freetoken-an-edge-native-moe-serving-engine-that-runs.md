---
title: 'Meet FreeToken: An Edge-Native MoE Serving Engine that Runs 753B GLM-5.2 on
  a Single Workstation GPU'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/23/meet-freetoken-an-edge-native-moe-serving-engine-that-runs-753b-glm-5-2-on-a-single-workstation-gpu/
model: claude-code/sonnet
generated_at: '2026-08-24T06:32:03.357449'
score: 115
---

📌 UC Berkeley與UT Austin新解法：讓753B模型跑在單張工作站GPU上

TL;DR：開源推理引擎FreeToken把個人電腦當成彈性運算平臺，讓消費級GPU也能服務千億參數MoE模型。

隨著Kimi-K3、GLM-5.2、DeepSeek-V4-Flash等開源權重模型陸續逼近閉源系統的能力，一個現實問題浮上檯面：能拿到模型權重，不代表跑得起這個模型。當agentic workload把推理需求繼續往上推，成本壓力最終落在個人開發者與小團隊身上，而不是那些本來就負擔得起資料中心GPU叢集的大型企業。

🤔 問題不在硬體，而在服務系統

素材指出，全球已有超過一億臺消費級機器搭載獨立GPU，但主流推理引擎的設計仍假設使用者擁有資料中心等級的叢集。來自UC Berkeley與UT Austin的研究團隊提出FreeToken，主張缺的不是硬體，而是一套服務系統：把個人電腦當成一個統一、彈性的推理平臺，而非單純把它視為「一張小GPU」，並持續把運算與模型狀態動態映射到機器上實際可用的GPU、CPU、記憶體與互連頻寬。

🧩 用MoE的稀疏性換取本地可行性

Mixture-of-Experts架構是讓本地跑得起前沿模型的算術基礎。以DeepSeek-V4-Flash為例，43層中每層僅從256個路由專家啟用6個，因此單一token實際只動用284B參數中的13B。但稀疏性不等於專家池變小：以FP4精度計算，完整專家集合仍約140GB，未啟用的專家平時留在主機記憶體，需要時才被拉進執行路徑。研究團隊指出，現有引擎（llama.cpp、KTransformers、Ollama、MoE-Infinity）在處理這種「按需載入」情境時存在三種失效模式，這也是FreeToken要解決的核心問題。

FreeToken以Apache-2.0授權開源於GitHub，並以freetoken v0.1.2上架PyPI（`uv pip install "freetoken[accel]"`），另提供Windows與Linux的一鍵桌面應用（flashml.ai）。CLI目前鎖定搭載NVIDIA GPU、驅動r580以上（CUDA 13）的Linux x86_64環境；`ft serve`會在1919埠開出OpenAI與Anthropic相容的端點，`ft launch claude`則可直接接上Claude Code、Codex、OpenCode或OpenClaw等agent客戶端。

📊 實測數據：延遲與快取命中率雙雙勝出

在RTX 5090上，FreeToken於Qwen3.6-35B-A3B（BF16）維持77–83 tok/s，DeepSeek-V4-Flash（MXFP4）則有22–25 tok/s，是最強基準線的1.5–2.3倍，且在三種agentic工作負載下，decode速度都維持在單輪對話速度的12%以內。

| 指標 | FreeToken | 對照基準 |
|---|---|---|
| 最差情況TTFT | 全矩陣皆低於44秒 | llama.cpp最高232秒、Ollama 179秒、KTransformers 946秒（部分情境已超過agent客戶端逾時上限） |
| 專家快取未命中率（相同37%快取容量） | 16% | KTransformers 41%、llama.cpp 62% |
| 8GB RTX 4060筆電，NVFP4，35B模型 | 39.3 tok/s | 高於Codex生產環境實測中位數33 tok/s |
| 單張RTX PRO 6000，GLM-5.2（753B，啟用40B） | 14.9 tok/s | llama.cpp為7.3 tok/s |

⚠️ 企業別拿它取代資料中心

素材明確指出，FreeToken更適合token帳單已經超過自購GPU成本的獨立開發者、新創與中小型工程團隊；對企業而言，這套系統應被視為「離線／受監管場景」的替代路徑，而不是資料中心的取代品。CLI目前也僅支援搭載NVIDIA GPU的Linux x86_64環境。

🎯 實務啟示

對經常被agent token帳單壓垮的個人與小團隊而言，FreeToken提供了一條把既有消費級GPU升級成「私有推理伺服器」的路徑，尤其適合本地coding agent、私有程式碼審查、離線合約分析、合成資料生成與批次評測等資料不能離開機器的場景。

🔗 來源
- 標題：Meet FreeToken: An Edge-Native MoE Serving Engine that Runs 753B GLM-5.2 on a Single Workstation GPU
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/23/meet-freetoken-an-edge-native-moe-serving-engine-that-runs-753b-glm-5-2-on-a-single-workstation-gpu/

#MoE #EdgeAI #LLMInference #OpenSource #GPU #LocalLLM #AgenticAI #ModelServing #Quantization #MachineLearning
