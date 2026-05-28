---
title: "Sakana AI Proposes DiffusionBlocks: a Block-wise Training Framework That Converts Residual Networks into Independently Trainable Denoising Modules"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/27/sakana-ai-proposes-diffusionblocks-a-block-wise-training-framework-that-converts-residual-networks-into-independently-trainable-denoising-modules/
score: 86
model: tencent/hy3-preview:free
generated_at: 2026-05-28T21:43:00.910569
---

**區塊訓練降低記憶體**  
【Sakana AI】  

你是否曾為訓練巨大的 diffusion model 而記憶體爆炸發愁？一種新的區塊訓練方式聲稱，只要把網路切成塊，記憶體需求就能降至原本的 1/B，而不犧牲效能。  

🤔 **殘差網路的訓練記憶體瓶頸**  
現有的 end-to-end 反向傳播需要在每一層儲存中間激活值，隨著網路深度線性增長記憶體消耗。即使使用 activation checkpointing 也只能節省激活值的記憶體，參數、梯度與優化器狀態（例如 Adam 的動量與變異數）仍佔每層約四倍參數大小，這成為深度模型訓練的主要限制。  

🧪 **區塊式訓練框架 DiffusionBlocks**  
研究團隊提出將 transformer‑based 殘差網路分割為 B 個區塊，每個區塊獨立進行訓練。理論上，這樣的做法可把所需記憶體降至約 1/B，因為每次只需要載入當前區塊的參數與對應的優化器狀態。他們進一步指出，殘差更新  
\(z_\ell = z_{\ell-1} + f_{\theta_\ell}(z_{\ell-1})\)  
對應於常微分方程的 Euler 離散形式，而在 score‑based diffusion model 的 Variance Exploding (VE)  formulation 中，這正是 probability flow ODE 的反向擴散過程。因此，區塊訓練不僅是一種工程技巧，更與擴散模型的理論基礎直接對應。  

💡 **關鍵洞察：區塊目標與全域一致性**  
先前的區塊式或逐層貪婪訓練多依賴 ad‑hoc 的局部目標，導致在端到端任務上表現不佳，且多局限於分類問題。DiffusionBlocks 透過將殘差網路的更新視為 probability flow ODE，提供了一種 principled 的局部目標，使得獨立訓練的區塊仍能組合成在生成任務上與 end-to-end 訓練相當的全域模型。  

⚠️ **研究限制**  
該研究主要闡述理論關聯與記憶體減少的潛力，尚未提供大規模擴散模型的實際基準數據。具體的區塊數 B、不同架構上的具體效能數據以及最佳區塊劃分策略仍需後續實驗進一步探討。  

🎯 **實務啟示**  
對於受記憶體限制的 diffusion model 訓練，可嘗試將網路劃合為多個區塊並分別更新，這樣既能顯著降低顯卡顯存需求，又不必犧牲模型的生成品質。在實作時，建議先以小規模實驗驗證區塊劃分對收穩度與樣本品質的影響，再逐步擴大至完整模型。  

🔗 **論文連結**  
📝 Sakana AI & University of Tokyo – DiffusionBlocks: a Block-wise Training Framework That Converts Residual Networks into Independently Trainable Denoising Modules  
🔗 https://www.marktechpost.com/2026/05/27/sakana-ai-proposes-diffusionblocks-a-block-wise-training-framework-that-converts-residual-networks-into-independently-trainable-denoising-modules/  

你認為區塊訓練在未來的擴散模型或其他深度生成模型中會有什麼潛力？歡迎在留言區分享你的看法 👇  

#AI #DiffusionModel #機器學習 #SakanaAI #深度學習 #記憶體優化 #Transformer #研究分享
