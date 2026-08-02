---
title: LMCache/LMCache
source: GitHub Trending
url: https://github.com/LMCache/LMCache
score: 113
model: google/gemma-4-31b-it:free
generated_at: '2026-07-09T09:50:18.887439'
---

**LMCache：將 KV Cache 轉換為可持久化與共享的 LLM 推理層**  
*來源：GitHub Trending – https://github.com/LMCache/LMCache*  

---

### TL;DR  
LMCache 是一個開源的 KV Cache 管理層，將原本臨時的 KV Cache 轉換為可持久化、可跨多個推理引擎重複使用的 AI‑native 知識。透過可觀測性堆疊與生成品質轉換，它能降低 Time‑To‑First‑Token（TTFT）並提升吞吐量，特別適用於長上下文代理、多輪對話及 k（依原文說明）場景。專案自 2025 年起持續在 GitHub 上獲得關注，已獲得 5,000+ 個星星，並獲得 CoreWeave、PyTorch Foundation、TensorMesh、NVIDIA Dynamo、AMD MI300X、Arm、Ascend、Redis 等生態夥伴的支援。

---

## 簡介  
LMCache 定位為 **KV Cache Management Layer for Scalable LLM Inference**。它的核心目標是將原本只在單次推理中臨時存在的 KV Cache 轉換為可以持久化儲存、跨不同推理引擎重複使用的資產。這樣的設計不僅提供可觀測性（observability stack），還能對生成品質進行轉換，進而在長上下文代理、多輪對話及 k（依原文說明）等場景中降低 TTFT、提升吞吐量。

---

## 核心功能（根據敘述）|
|---|
| **持久化與共享**：將 KV Cache 從暫存資產為可持久化、可跨多個推理引擎重用知識 **可觀測\n**可觀測性堆疊**：提供完整的觀測堆疊，使開發者能監控與診斷 KV Cache 的使用狀況。\n**生成品質轉換**：透過特定的轉換機制，提升生成文字的品質表現。\n**降低 TTFT、提升吞吐量**：特別適合長上下文代理（agentic）、多輪對話以及文中提到的 k 場景，能顯著減少首個 token 的延遲並提升整體吞吐量。\n\n## 重要里程碑（依時間順序）\n- **2026/05** – Agentic 工作負載基準在 AMD MI300X 上發表（部落格）。\n- **2026/04** – LMCache 發布多處理程序（MP）架構版本（部落格）。\n- **2026/03** – LMCache 在 GTC 2026 發表（貼文）。\n- **2026/01** – LMCache 多節點 P2P CPU 記憶體共享從實驗功能進入生產階段（部落格）。\n- **2025/11** – LMCache 與 CoreWeave 合作，加速 Cohere 的高效 LLM 推理（部落格）。\n- **2025/10** – LMCache 加入 PyTorch 基金會，並發布 TensorMesh（部落格、PyTorch）。\n- **2025/09** – NVIDIA Dynamo 整合 LMCache，加速 LLM 推理（部落格）。\n- **2025/08** – LMCache 在 GitHub 獲得 5,000+ 個星星（部落格）。\n- **2025/08** – LMCache 首日支援 gpt-oss（20B/120B）模型（部落格）。\n- **2025/07** – 與 Redis 合作提供更快的 LLM 推理與更低的回應成本（Redis 部落格）。\n- **2025/07** – LMCache 將 turbo‑boost 擴展至多模態模型，支援 vLLM V1（部落格）。\n- **2025/06** – LLM 生產堆疊實現跨硬體支援：AMD、Arm 與 Ascend（部落格）。\n\n## 技術亮點（依摘要敘述）\n- 將 KV Cache 轉換為**可持久化與共享**的層。\n- 支援**跨多個推理引擎重複使用**。\n- 提供**可觀測性堆疊**，方便監控與除錯。\n- 能夠**轉換以提升生成品質**。\n- 因而**降低 TTFT（特別適用於長上文、多輪對話輪對話及 k**低 TTFT**、**提升吞吐量**，特別適用於**長上下文代理、多輪對話及 k**（依原文說明）。\n\n## 社群與生態\n- 專案於 GitHub 取得 **5,000+ 個星星**（2025/08 公佈）。\n- 提供 **Slack 社群**、**社群會議**與 **路線圖更新**，方便開發者即時交流。\n- 已獲得以下生態夥伴的公開支援或合作：\n  - CoreWeave（與 Cohere 合作加速 LLM 推理）\n  - PyTorch 基金會 & TensorMesh（2025/10）\n  - NVIDIA Dynamo（2025/09）\n  - AMD MI300X（2026/05 基準測試）\n  - AMD、Arm、Ascend（跨硬體 LLM 生產堆疊，2025/06）\n  - Redis（提供更快的 LLM 推理與更低迴應成本，2025/07）\n\n## 結語\nLMCache 透過將傳統的短暫 KV Cache 轉換為可持久化、可共享的 AI‑native 知識層，成功在長上下文代理、多輪對話以及特定 k 場景中降低首 token 延遲、提升系統吞吐量。專案自 2025 年起在 GitHub 上快速累積星星，並獲得來自硬體廠商、雲端平臺與開源基金會的廣泛支援。若您正在尋找一種讓 LLM 推理更具擴展性與經濟性的方案，LMCache 值得進一步評估與貢獻。\n\n## 來源連結\n- GitHub 倉庫：https://github.com/LMCache/LMCache\n- 部落格與公告（依時間順序）：\n  - 2026/05 – Agentic workload benchmark on AMD MI300X\n  - 2026/04 – LMCache's new multiprocess (MP) architecture release\n  - 2026/03 – LMCache at GTC 2026\n  - 2026/01 – LMCache multi-node P2P CPU memory sharing, from experimental feature to production\n  - 2025/11 – LMCache x CoreWeave accelerate efficient LLM inference for Cohere\n  - 2025/10 – LMCache joins the PyTorch Foundation and Tensormesh unveiled\n  - 2025/09 – NVIDIA Dynamo integrates LMCache, accelerating LLM inference\n  - 2025/08 – LMCache hits 5,000+ GitHub stars\n  - 2025/08 – LMCache supports gpt-oss (20B/120B) on day 1\n  - 2025/07 – Get faster LLM inference and cheaper responses with LMCache and Redis\n  - 2025/07 – LMCache extends its turbo-boost to multimodal models in vLLM V1\n  - 2025/06 – LLM Production Stack goes cross-hardware: AMD, Arm and Ascend\n\n*本文僅基於上述公開資訊撰寫，未新增任何未在來源中出現的細節。*
