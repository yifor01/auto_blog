---
title: "[AINews] DeepSeek V4 Pro (1.6T-A49B) and Flash (284B-A13B), Base and Instruct — runnable on Huawei Ascend chips"
source: Latent Space
url: https://www.latent.space/p/ainews-deepseek-v4-pro-16t-a49b-and
score: 111
model: tencent/hy3-preview:free
generated_at: 2026-04-25T19:02:15.898986
---

📌 【DeepSeek V4 發布】1M Context、華為昇騰原生支援，開源模型新標竿

千呼萬喚始出來，DeepSeek 終於在萬眾矚目下推出了 V4 系列。這不僅是繼 V3 和 R1 之後的重大架構更新，更是一個明確的信號：頂級開源模型的競爭焦點，正從純粹的參數規模轉向極致的推理效率與硬體自主權。

🤔 **擺脫 CUDA 依賴，DeepSeek 的算力自主之路**

過去幾個月，產業界一直在等待 DeepSeek V4。這次發布意義重大，不僅因為它是對標 Gemini 3.1 與 GPT 5.4 級別的模型，更因為它展示了在出口管制背景下，中國 AI 產業如何透過華為昇騰 (Ascend) 芯片實現技術獨立。這是首個原生支援華為 CANN 架構的頂級開源模型，雖然昇騰供應鏈目前僅為 H100 的四分之一，但戰略意義非凡。

🧪 **雙版本策略：Pro 與 Flash 的精準定位**

DeepSeek 首次採用清晰的高低搭配策略，滿足不同場景需求：
- **DeepSeek V4 Pro (1.6T-A49B)**：旗艦級模型，採用 FP4 訓練，預訓練數據量達 32T tokens。
- **DeepSeek V4 Flash (284B-A13B)**：輕量化版本，兼顧效率與效能。
兩者均支援混合推理模式 (Reasoning/Non-reasoning)，並同時釋出 Base 與 Instruct 版本，為後續可能推出的 R2 鋪路。

 **1M Context 的極致效率：僅需 10% 的 KV Cache**

長上下文一直是資源消耗的大戶，但 V4 透過技術創新打破了瓶頸。藉由全新的 **Compressed Sparse Attention (CSA)** 與 **Heavily Compressed Attention (HCA)** 技術，V4 在處理 1M token 上下文時，相比 V3.2 僅需 **27% 的 FLOPs** 與 **10% 的 KV Cache 記憶體**。這意味著在同等硬體條件下，處理長文本的成本大幅降低。

💡 **技術底蘊：從 Manifold 到 Muon 的延續與創新**

這份長達 58 頁的技術報告揭示了 V4 的技術血統：
- **mHC 架構**：繼承自 1 月發布的 Manifold Constrained Hyper-Connections，優化模型連接效率。
- **Muon 優化器**：持續沿用 Moonshot 的 Muon 優化演算法，顯示其在訓練穩定性上的價值。
- **MIT 授權**：完全開源，讓開發者與企業能無後顧之憂地進行部署與二次開發。

⚠️ **供應鏈現實與實測驗證**

雖然技術報告詳盡（甚至紅迪討論區已有多篇分析），但必須面對的現實是：華為昇騰芯片的產能目前仍有限。此外，模型雖已達到 Kimi K2.6 等開源領導者的水準，但在實際複雜任務中的表現，仍需社群進一步的壓力測試。

🎯 **開發者與管理者的行動指南**

- **部署考量**：如果你的基礎設施受限於非 NVIDIA 環境，V4 的昇騰原生支援是關鍵破局點。
- **長文本應用**：利用 CSA/HCA 技術，重新評估你的 RAG 或長文摘要架構，成本可能會有驚喜。
- **開源生態**：Base 版本的釋出意味著針對特定領域的客製化訓練有更多可能性。

🔗 **相關連結**
📝 DeepSeek V4 Pro and Flash: Base and Instruct — runnable on Huawei Ascend
📰 來源：Latent Space (AINews)
🔗 https://www.latent.space/p/ainews-deepseek-v4-pro-16t-a49b-and

你會考慮將 V4 部署在華為昇騰環境上，還是繼續觀望？歡迎在留言區分享你的技術選型看法 👇

#DeepSeek #AI #LLM #開源模型 #華為昇騰 #TechNews #MachineLearning #NVIDIA替代
