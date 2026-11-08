---
title: 'MoE Routing Strategies Explained: Top-K, Expert-Choice, Sigmoid Gating and
  Dynamic Routing (2026 Guide)'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/07/moe-routing-strategies-explained/
model: claude-code/sonnet
generated_at: '2026-11-08T21:19:20.640816'
score: 81
---

📌 從Top-K到Hash Routing:MoE路由七種做法全解析

TL;DR:這份指南把目前生產環境常見的MoE路由策略拆成七類,逐一對應到實際用它的模型。

每個Mixture-of-Experts(MoE)模型在推論時都要為每個token重複做同一件事:決定讓哪些專家處理它。這個決定權全交給路由器(router),而router怎麼設計,直接影響輸出品質、負載是否均衡,以及服務成本。這份指南整理了目前生產環境中常見的路由策略,以及各自被哪些模型採用。

🤔 **路由器到底在做什麼**

MoE路由是把每個token送到一小部分專家網路的機制:router替每個專家打分,保留分數最高的幾個,再用這些分數加權混合它們的輸出,只有被選中的專家會實際運算。舉例來說,Mixtral 8x7B讓每個token可以摸到47B參數,但實際只動用13B的啟用參數。

🧩 **七種主流路由策略**

**Top-K路由**:每個token用一個線性層替所有專家打分,保留分數最高的k個,再對這k個分數做softmax決定混合權重。Mixtral在8個專家裡選2個,gpt-oss-120b在128個裡選4個,Qwen3-235B-A22B在128個裡選8個,通常還會搭配一個輔助損失(auxiliary loss)來維持負載均衡。採用者:Mixtral、gpt-oss、Qwen3。

**Switch式單專家路由**:Switch Transformer證明把每個token只送到1個專家,既能維持品質又能大幅降低router的運算量。每個專家有一個固定的容量緩衝區(批次token數除以專家數,再乘上容量因子),溢出的token會直接透過殘差連接跳過這一層。Llama 4 Maverick也採用類似設計,每個token送到1個路由專家加1個共享專家。採用者:Switch Transformer、Llama 4 Maverick(搭配共享專家)。

**共享加路由專家的切分**:DeepSeekMoE把每一層切成「永遠開著」的共享專家與稀疏路由的專家,共享專家負責吸收通用知識,讓路由專家可以專注在特化任務上。DeepSeek-V3用1個共享專家搭配256個路由專家,實際啟用8個;Kimi K2、GLM-4.5與Qwen3.6-35B-A3B都延續這個模式。Qwen3則反其道而行,把共享專家拿掉了。採用者:DeepSeek-V3與V4、Kimi K2、GLM-4.5、Qwen3.6、Llama 4。

**Sigmoid評分與免損失負載平衡**:DeepSeek-V3不用softmax,改用sigmoid替專家打分,並額外加一個只影響top-k挑選、不影響混合權重的per-expert bias;這個bias每一步都會依照各專家的負載狀況調整,過載的專家bias往下降,閒置的往上升。GLM-4.5則用搭配sigmoid gate的免損失平衡路由。DeepSeek-V4把評分函式換成sqrtsoftplus,但仍保留bias平衡機制。採用者:DeepSeek-V3、DeepSeek-V4、GLM-4.5、Kimi K2。

**節點限制路由**:把一個token送到分散在多個節點上的專家成本很高。DeepSeek-V3的做法是依親和分數把專家分成8組,先保留4組,再從中做最終的top-8挑選,等於把每個token限制在最多4個節點內。DeepSeek表示這個限制讓訓練階段的運算與通訊幾乎能完全重疊。Kimi K2則完全拿掉分組,把n_group設為1。

**Expert-choice路由**:Google的做法把方向反過來,由每個專家主動挑選自己的top-k個token,讓每個專家都有固定大小的處理桶,而每個token拿到的專家數量可能不固定。原始論文報告訓練收斂速度快了超過2倍,但代價是破壞了因果性:一個token該交給哪個專家,可能取決於序列裡之後才出現的token。DeepSeek的研究人員量測到這種資訊洩漏會造成約10%的異常loss下降。目前只用在研究與非因果場景,文章比較的10個生產模型中沒有一個採用。

**Hash routing**:直接用token ID決定專家,完全不經過學習得來的router。DeepSeek-V4在前3層MoE層採用這種做法。

另外,指南也提到動態top-k的概念:每個token啟用的專家數量可以不固定。SMIDT把這個機制做進SGLang,讓P99的首token延遲(time-to-first-token)縮短了1.21到1.26倍,目前主要出現在DeepSeek-V4(搭配hash routing)與一些研究性質的推論伺服器裡。

⚠️ **改動路由等於改動模型**

文章特別提醒,推論時調整top-k並不是單純的效能調校,而是實質上改變了模型本身的行為,應該當成一次品質實驗來對待,而不是隨手調的旋鈕。Expert-choice路由的因果洩漏問題,也是它至今沒有被任何主流生產模型採用的關鍵原因。

🎯 **上線前,先讀四個欄位**

大多數團隊其實沒有「選」路由策略,而是選了一個checkpoint就連帶繼承了它的路由設計。部署前,先打開config.json讀四個欄位:專家數、每token啟用數、是否有共享專家,以及topk_method。文章也指出,對於全新的預訓練專案,sigmoid評分搭配bias平衡目前是業界最常見的預設選擇。

🔗 **來源**
- 標題:MoE Routing Strategies Explained: Top-K, Expert-Choice, Sigmoid Gating and Dynamic Routing (2026 Guide)
- 作者/機構:Asif Razzaq(MarkTechPost)
- 連結:https://www.marktechpost.com/2026/11/07/moe-routing-strategies-explained/

#MixtureOfExperts #MoERouting #TopK #ExpertChoice #SigmoidGating #HashRouting #LLMArchitecture #DeepSeek #ModelServing #MachineLearning
