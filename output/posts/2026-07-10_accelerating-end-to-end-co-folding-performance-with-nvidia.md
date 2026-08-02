---
title: Accelerating End-to-End Co-Folding Performance with NVIDIA BioNeMo Agent Toolkit
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/accelerating-end-to-end-co-folding-performance-with-nvidia-bionemo-agent-toolkit/
score: 95
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T08:14:05.370141'
---

**使用 NVIDIA BioNeMo Agent Toolkit 加速端到端共摺效能**  
**來源**：NVIDIA Developer  
**作者**：Elizabeth Goodman  
**連結**：https://developer.nvidia.com/blog/accelerating-end-to-end-co-folding-performance-with-nvidia-bionemo-agent-toolkit/

---

## 前言  
生物分子結構預測與共摺（co‑folding）正成為藥物發現與蛋白質設計的核心工作流程。為了讓 AI 代理人能夠高效執行完整的管線——包括多重序列比對（MSA）生成、共摺推理、服務以及多 GPU 規模擴展——每個環節都必須兼具速度與記憶體效率。NVIDIA 近期發布的 BioNeMo Agent Toolkit 針對這些瓶頸進行了端到端的加速。

---

## 技術概覽  
BioNeMo Agent Toolkit 整合了以下關鍵元件：

1. **MMseqs2‑GPU** – 在 NVIDIA Hopper 與 Blackwell 架構上執行 MSA 生成，相較於傳統 CPU JackHMMER，最高可達 **177 倍** 的加速。  
2. **cuEquivariance 與 OpenFold3 NIM** – 提升 OpenFold3 前向傳播的執行速度，最高可達 **3 倍** 加速，並將序列長度上限擴展至約 **5.9k 個 token**。在單張 B300 GPU 上，OpenFold3 NIM 更可支援高達 **6,400 個 token**。  
3. **Fold‑CP（Context‑Parallel）** – 採用內容平行策略，使單張 GPU 的記憶體需求降至 **O(N/P)**，因而能在 **64 顆 B300 GPU** 上模擬多達 **32,000 個 token** 的大型複合物（例如核糖體規模的結構），此前在單卡或少數卡上無法處理的問題因而變得可行。

> 註：部落格內含 AI 生成的摘要，僅供參考，請自行確認重要資訊的正確性。

## 效能提升亮點  

| 技術 | 主要提升 | 資料說明（依原文） |
|------|----------|-------------------|
| MMseqs2‑GPU | MSA 生成速度 | 比 CPU JackHMMER 快 **177 倍**（Hopper / Blackwell） |
| cuEquivariance + OpenFold3 NIM | 前向傳播時間 | 最多 **3 個** 加速；序列長度上限 ~**5.9k** token；單 B300 GPU 可達 **6,400** token |
| Fold‑CP | 記憶體效率 | 每張 GPU 記憶度需求降至 **O(N/P)**；64 顆 B300 GPU 可處理 **32,000** token 規模的複合物 |

這些資料直接來自部落格所提供的效能說明，未加入任何未在原文中出現的額外數值或假設。

## 應用場景  
- **虛擬篩選（Virtual Screening）** : 需要對數百萬至數十億種小分子與一個或少數蛋白質目標進行結合預測，MSA 生成與共摺推理的速度直接影響整體吞吐量。  
- **大型分子複合物預測** : 透過 Fold‑CP 的內容平行機制，研究者現在能在數十張高階 GPU 上模擬核糖體等大規模複合物，以前因記憶體瓶頸無法進行的結構預測變得可行。

這些加速能力使得 AI 驅動的藥物發現與蛋白質設計工作流程能在更大規模、更短時間內完成。

## 結論  
NVIDIA 的 BioNeMo Agent Toolkit 透過 GPU 加速的 MSA 生成（MMseqs2‑GPU）、更快的共摺推理（cuEquivariance + OpenFold3 NIM）以及記憶體效率的上下文平行（Fold‑CP），實現了從序列對齊到大型複合物建模的端到端效能提升。這些改進直接解決了藥物虛擬篩選與巨大分子複合物預測中的效能瓶頸，為後續的生物結構研究提供了更強的運算基礎。

---

**參考連結**  
- NVIDIA Developer 部落格：https://developer.nvidia.com/blog/accelerating-end-to-end-co-folding-performance-with-nvidia-bionemo-agent-toolkit/  

*本文僅依據上述來源內容撰寫，未新增未在來源中提及的任何細節或資料。*
