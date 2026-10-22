---
title: Liquid AI Launches RIPL, a Real-Time Inference Engine for Sub-50 ms LFMs
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/22/liquid-ai-ripl-real-time-inference-engine/
model: claude-code/sonnet
generated_at: '2026-10-22T20:52:29.217918'
score: 96
---

📌 Liquid AI 推出 RIPL，把生成式模型塞進 50 毫秒的即時決策鏈

TL;DR：RIPL 讓 LFM 在尖峰流量下仍能於 50 毫秒內吐出完整回應。

搜尋排序、風控檢查、支付授權,這些路徑向來等不起幾秒鐘的LLM回應,所以團隊多半只能退回用gradient-boosted trees之類的傳統模型。Liquid AI這次想把這個限制拿掉。

🤔 為什麼 LLM 服務進不去毫秒級戰場

Liquid AI指出,大多數serving stack的設計目標是大batch和長時間的agentic任務,一次請求等個幾秒是可以接受的。但搜尋排序、詐欺檢測、支付授權這類路徑需要毫秒級的答案,團隊因此預設改用傳統機器學習模型,因為LLM serving太慢。

🧩 RIPL 做的事：優化整條請求路徑

Liquid RIPL全名Real-time Inference Pipeline,是一套把Liquid Foundation Models(LFM)直接放進live request path裡serving的低延遲引擎。它號稱能端到端完整生成並回傳回應,耗時低於50毫秒,而且即使流量連續湧入到尖峰負載,延遲依然維持。對開發者來說訊息很直接:把gradient boosted tree換成生成式模型,延遲預算不變。Liquid AI強調RIPL優化的是從request到達到response完成的整條路徑,而不只是模型本身。

📊 同一顆模型換引擎，差距看得見

Liquid AI拿同一個模型LFM2.5-350M,分別跑在vLLM和RIPL上做比較,在多個工作負載裡,RIPL的p95延遲線都明顯低於vLLM的那條線,這把效能提升獨立歸因到引擎本身,而不只是模型架構的差異。測量方式是在單張B200上,於open-loop Poisson到達模式下量p95端到端延遲:LFM系列跑在RIPL上,MiniCPM5和Granite 4.2這兩個baseline則跑在vLLM上(資料來源為Liquid AI部落格Figure 2,屬自行回報數字)。Liquid AI也把6個即時工作負載對應到各自的固定延遲預算上做比較。

LFM2.5系列本身是混合架構:LFM2.5-1.2B-Instruct共16層,由10個double-gated convolution blocks與6個GQA blocks組成;LFM2.5-2.6B共30層,由22個convolution blocks與8個GQA blocks組成。

💡 已有真實流量在用

根據Liquid AI部落格,Shopify正把LFM部署到多個延遲敏感的電商工作負載中;在search enhancement場景,LFM在正式生產流量上以低於20毫秒的推論延遲運作。Liquid AI也宣稱,相比替代方案,這些模型使用約少50%的參數,推論速度快2到10倍。

⚠️ 要留意的地方

目前公開的比較數字都是Liquid AI自行回報,尚未看到第三方獨立驗證;素材也沒有提供更大型LFM(如2.6B)在RIPL上的端到端延遲是否能維持同等優勢的數據。

🎯 實務啟示

如果系統裡還有一批因為「LLM太慢」而只能用GBDT、regression頂著的路徑,RIPL的定位值得關注。可以先用Liquid AI提供的latency calculator試算自己場景能否吃進50毫秒預算,再對照LFM2.5的model card規格評估遷移可行性。

🔗 來源
- 標題：Liquid AI Launches RIPL, a Real-Time Inference Engine for Sub-50 ms LFMs
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/22/liquid-ai-ripl-real-time-inference-engine/

#LiquidAI #RIPL #LLMInference #EdgeAI #RealTimeAI #LFM #MachineLearning #Latency #AIInfrastructure #GenerativeAI
