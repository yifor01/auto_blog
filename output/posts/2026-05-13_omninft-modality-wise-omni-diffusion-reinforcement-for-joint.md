---
title: "OmniNFT: Modality-wise Omni Diffusion Reinforcement for Joint Audio-Video Generation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.12480
score: 121
model: tencent/hy3-preview:free
generated_at: 2026-05-13T20:25:03.464846
---

📌 **OmniNFT：針對音訊‑影像聯合生成的模態感知強化學習框架**

隨著擴散模型在音訊與影像聯合生成上的突破，實際應用卻對單一模態的保真度、跨模態對齊以及細粒度同步提出了更高要求。傳統的強化學習（RL）微調策略在這種多目標、多模態的情境下，常常因為梯度與信用分配的不一致而難以達到理想效果。

🤔 **多目標優勢不一致與梯度洩漏是主要瓶頸**

作者透過深入分析指出，直接把單一全域優勢用於 RL 微調會導致三個問題：  
1. **多目標優勢不一致** – 不同模態的回報優勢在同一批次樣本中可能指向相反方向；  
2. **多模態梯度不平衡** – 影像分支的梯度會流入淺層音訊網路，干擾純音訊生成；  
3. **均等信用分配** – 對音訊‑影像同步關鍵區域的探索不足，導致細節對齊不足。

這些短comings 說明為何 vanilla RL 往往只能得到次佳結果。

🧪 **OmniNFT：三種模態感知設計的線上擴散 RL 框架**

為了對症下藥，研究團隊提出 OmniNFT，包含以下三個創新機制：  
- **模態優勢路由**：為每個模態獨立計算對應的優勢，並將其導向各自的生成分支；  
- **層級梯度手術**：在淺層音訊網路上選擇性斷開影像分支的梯度，同時保留負責跨模態互動的層梯度；  
- **區域損失重加權**：根據音訊‑影像同步與細粒度對齊的重要區域動態調整政策優化的權重。

實驗採用 LTX-2 作為骨幹模型，在 JavisBench 與 VBench 上進行評估，結果顯示 OmniNFT 在音訊感知品質、影像感知品質、跨模態對齊以及音訊‑影像同步方面皆有全面提升。

💡 **關鍵洞察：分離與重新加權才是多模態 RL 的正確途徑**

與其嘗試用單一全域訊號去平衡所有目標，OmniNFT 顯示：先把各模態的訊號分開處理（優勢路由），再針對梯度流動做選擇性保留或切除（梯度手術），最後讓學習過程聚焦在真正影響同步與對齊的區域（損失重加權），才能避免梯度衝突與信用稀釋的問題。

⚠️ **僅在特定骨幹與基準上驗證，長期穩定性尚未探討**

目前的實驗限於 LTX-2 骨幹以及 JavisBench、VBench 兩個基準，未說明在其他擴散架構或更長序列生成中的表現；此外，論文未討論訓練穩定性或在真實產線部署時的計算開銷。

🎯 **對工程師的啟示：在多目標生成任務中，先做模態層面的訊號分離**

如果你正在構建涉及音訊、影像甚至更多模態的生成系統，可參考 OmniNFT 的思路：  
1. 分別為每個模態計算獎勵或優勢；  
2. 在反向傳播時，依照網路層級的功能（純模態 vs. 跨模態）選擇性地保留或切除梯度；  
3. 針對已知對任務目標關鍵的時空區域，搭配動態損失重加權來強化學習焦點。  
這樣的設計能減少梯度干擾，讓每個模態都能在各自的目標上獲得有效的學習訊號。

🔗 **論文連結**  
📝 OmniNFT: Modality-wise Omni Diffusion Reinforcement for Joint Audio-Video Generation  
👤 Guohui Zhang, XiaoXiao Ma, Jie Huang, Hang Xu, Hu Yu (USTC; Peking University; JD Explore Academy)  
🔗 https://arxiv.org/abs/2605.12480  

你在多模態生成中是否也遇過梯度衝突或獎勵不一致的問題？歡迎在留言區分享你的經驗與解決方案 👇

#AI #AudioVideoGeneration #DiffusionModels #ReinforcementLearning #MultimodalAI #USTC #PekingUniversity #JDExploreAcademy #CVPR2026
