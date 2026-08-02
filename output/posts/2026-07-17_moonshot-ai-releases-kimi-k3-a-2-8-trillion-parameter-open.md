---
title: 'Moonshot AI Releases Kimi K3: A 2.8 Trillion Parameter Open MoE Model With
  Kimi Delta Attention and 1M Context'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/16/moonshot-ai-releases-kimi-k3-a-2-8-trillion-parameter-open-moe-model-with-kimi-delta-attention-and-1m-context/
score: 99
model: tencent/hy3:free
generated_at: '2026-07-17T08:07:29.679672'
---

📌 【Moonshot AI 釋出 Kimi K3】2.8 兆參數開源 MoE，首見 3T 級模型

TL;DR：Kimi K3 為首個開源 2.8 兆參數 MoE，含 KDA 與 1M 上下文，效能仍落後頂尖閉源模型。

當多數開源模型還在千億參數級別競爭，Moonshot AI 直接把門檻推到 2.8 兆——這是該公司宣稱的全球第一個開放權重的 3T-class 模型。

🤔 **開源模型規模的天花板被再度拉高**

Moonshot AI 發布 Kimi K3，一個具備原生視覺能力（native vision）與 100 萬 token 上下文視窗（context window）的稀疏 Mixture-of-Experts (MoE) 模型。Moonshot 表示，在過去十二個月當中有九個月，Kimi 系列模型持續設定開源模型參數規模的上限；K3 則是首個達到 2.8 兆參數的開源模型。

🧩 **KDA 與 AttnRes：從序列長度與深度兩軸改造資訊流**

K3 建立在兩項架構更新之上。Kimi Delta Attention (KDA) 是一種混合線性注意力機制（hybrid linear attention），改變資訊跨序列長度的流動方式；Moonshot 宣稱在百萬 token 上下文中，KDA 可帶來最高 6.3 倍更快的解碼速度。Attention Residuals (AttnRes) 則作用在模型深度軸，選擇性地從不同深度檢索表示（representations），而非均勻累積；據稱能以低於 2% 的額外成本換取約 25% 更高的訓練效率。

⚠️ **整體效能仍落後最強閉源模型**

Moonshot 坦言 K3 的整體表現仍落後目前最強的專有模型 Claude Fable 5 與 GPT 5.6 Sol。不過在 Moonshot 自身的評估套件中，K3 一致地優於其他受測模型。

🧩 **稀疏化與路由：896 個專家中只啟動 16 個**

K3 採用 Stable LatentMoE，實際上只啟用 896 個專家中的 16 個。在此稀疏度下，路由（routing）與最佳化成為首要挑戰。Quantile Balancing 直接從路由器分數的分位數推導專家分配，省去啟發式更新與敏感的平衡超參數；Per-Head Muon 獨立最佳化各 attention head；Sigmoid Tanh Unit (SiTU) 與 Gated MLA 分別改善啟用控制與注意力選擇性。配合精煉的訓練與資料配方，整體擴展效率較 Kimi K2 約提升 2.5 倍。這些設計也延續到推論服務端，K3 套用了量化（quantization，摘要於此處截斷，細節未提及）。

🎯 **實務啟示**

對工程師而言，K3 代表了開源模型在長上下文與超大規模 MoE 架構上的新基準：若你需要百萬 token 級的長程編碼或知識工作，可關注其 KDA 帶來的解碼加速與開源權重可用性；但部署前應留意其整體能力仍不及頂尖閉源模型，且摘要未提供量化後的具體服務成本與細節。

🔗 **來源**
- 標題：Moonshot AI Releases Kimi K3: A 2.8 Trillion Parameter Open MoE Model With Kimi Delta Attention and 1M Context
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/16/moonshot-ai-releases-kimi-k3-a-2-8-trillion-parameter-open-moe-model-with-kimi-delta-attention-and-1m-context/

#KimiK3 #MoonshotAI #MoE #OpenModel #KDA #AttnRes #LongContext #LLM #MixtureOfExperts #QuantileBalancing
