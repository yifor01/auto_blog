---
title: "Flash-GRPO: Efficient Alignment for Video Diffusion via One-Step Policy Optimization"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.15980
score: 129
model: tencent/hy3-preview:free
generated_at: 2026-05-18T20:11:45.575915
---

📌 **Flash‑GRPO：一步搞定視訊擴散模型對齊，訓練成本大幅下降**  

你以為把一個 14B 參數的視訊擴散模型對齊必須花費數百個 GPU 天？最新研究顯示，只要換成正確的單步優化策略，同樣的（甚至更好）對齊品質可以在遠少的算力下達成。

🤔 **視訊擴散對齊的計算瓶頸**  
Group Relative Policy Optimization（GRPO）是目前將視訊擴散模型與人類偏好對齊的主流方法，但直接訓練一個 14B 參數模型通常需要 **數百個 GPU 天** 每次實驗。為了降低成本，現有做法多採用 sliding‑window subsampling（只訓練部分時間步），雖能省資源，卻會引入 **時間步混雜的方差** 以及 **梯度幅度的不一致**，導致訓練不穩定，最終無法達到完整軌跡的性能。

🧪 **Flash‑GRPO：單步策略 + 兩關鍵設計**  
論文提出 **Flash‑GRPO**，一種單步（one‑step）策略優化框架，透過兩個專門設計解決上述問題：  

1. **等時分組（Iso‑temporal grouping）**  
   強制同一個 prompt 在所有時間步上保持時間的一致性，從而消除由時間步造成的混雜方差，使策略表現不再受特定時間步難度的影響。  

2. **時間梯度校正（Temporal gradient rectification）**  
   中和時間步依賴的縮放因子，使得不同時間步的梯度幅度趨於一致，避免因梯度不均導致的訓練不穩。  

實驗覆蓋 **1.3B 到 14B** 參數的視訊擴散模型，結果顯示：在相當低的算力預算下，Flash‑GRPO 不僅訓練速度顯著提升（從數百 GPU 天縮減至只有其分數），而且在對齊品質上**優於**傳統的完整軌跡訓練，且訓練過程保持穩定。

💡 **為何單步就能勝過多步？**  
傳統滑動窗口方法在減少計算時，同時切斷了時間步之間的信息流，導致策略無法學到完整的時序依賴。Flash‑GRPO 透過等時分組讓每個 prompt 在所有時間步上共享相同的策略更新，而時間梯度校正則確保這些更新在各時間步上具有可比的 magnitude。這兩個機制讓單步更新同時具備 **時序一致性** 與 **梯度穩定性**，從而在低算力下仍能達到或超越多步訓練的對齊效果。

⚠️ **已知限制**  
- 實驗僅在 1.3B‑14B 參數範圍內進行，尚未在更大規模（如 70B+）或其他生成任務（圖像、音訊）上驗證。  
- 長期訓練穩定性與對齊效果的持續性仍需後續工作進一步探討。  

🎯 **對研究與產業的啟示**  
- 對於資源有限的實驗室或希望快速迭代的產業團隊，Flash‑GRPO 提供了一種**可直接插入現有 GRPO 流程**的低成本方案。  
- 在部署大型視訊擴散模型時，可顯著縮短對齊階段的時間與能源消耗，同時保持甚至提升模型對人類偏好的貼合度。  

🔗 **論文連結**  
📝 Flash-GRPO: Efficient Alignment for Video Diffusion via One-Step Policy Optimization  
👤 Xiaoxuan He, Siming Fu, Zeyue Xue, Weijie Wang, Ruizhe He  
🏫 Zhejiang University; Joy Future Academy; Independent Researcher; Tsinghua University  
🔗 https://arxiv.org/abs/2605.15980  

如果你正在為視訊生成模型的對齊階段發愁，這或許是值得一試的新思路。歡迎在留言區分享你的看法或實驗經驗！  

#FlashGRPO #VideoDiffusion #PolicyOptimization #AIResearch #ZhejiangUniversity #Tsinghua #MachineLearning #生成式AI
