---
title: 'Polymorphic Inference: self-tuning inference for open models'
source: Together AI
url: https://www.together.ai/blog/polymorphic-inference
model: claude-code/sonnet
generated_at: '2026-11-04T22:54:31.647733'
score: 87
---

📌 讓推理引擎自己進化：Together AI 的「多型推理」戰略

TL;DR：Together AI 提出多型推理概念，用 AI agent 自動找出推理設定的最佳解，應對模型與硬體的快速變化。

如果你還在用一份寫死的 vLLM 或 SGLang 設定檔跑所有流量，Together AI 想告訴你：這個做法已經過時了。

🤔 **為什麼一份設定檔不再夠用**

Together AI 觀察到幾個同時發生的趨勢正在把推理這件事變得更複雜。首先是模型釋出速度暴增且架構愈來愈分散，他們引用的數據是 OpenRouter 上有 80% 的流量來自過去三個月內釋出的模型，而目前最熱門的十個開源模型彼此用的架構都不一樣。其次是流量形態持續在變,新使用者、新產品、新的 post-train（例如讓模型多花 token 思考以換取更高品質）都會改變實際的 serving 負載。最後是硬體本身也在快速迭代，從 B200 到 GB300，甚至已經站在 Vera Rubin 部署的門口。Together AI 把這種「無數種形狀同時存在」的現況稱為 Polymorphic Inference（多型推理），用來對照過去封閉模型、單一 Transformer 架構、單一硬體平臺的「靜態推理」時代。

🧩 **Together Compiler：把最佳化問題變成 agent 搜尋問題**

Together AI 承認自己過去也是「靜態思維」的一部分：像 FlashAttention 這類核心成果仍適用於訓練與許多 prefill 場景,但他們在把 megakernel（把整個推理流程融合成單一 kernel）真正推上生產環境後,得到一個反直覺的結論——megakernel 融合其實不是多型推理時代該追求的目標,因為架構(如 MoE)與負載(動態批次大小)的每一種變化都需要不同的技術解法。

他們的應對方案是 Together Compiler：由 Frontier Performance 團隊(文中點名 Reyna Abhyankar 與 Dylan Lim)打造的 agent 群體，搭配一套高擬真、可快速迭代的持久化引擎，把傳統「編譯器轉譯」問題重新定義成「agentic 搜尋」問題，找出核心最佳化模式並持續套用。這套機制驅動的流程被稱為 Continuous Compilation（持續編譯），讓系統能自動適應新的流量形態與工作負載，而不必每次都重寫一組 kernel。

📊 **已經在生產環境裡跑**

Together Compiler 目前已經在 Together AI 多個最熱門的 serverless endpoint 上線，並在原本就高度最佳化的程式碼之上再找到額外的效能空間。文中也提到一個規模背書：Together AI 每天服務的 token 量已達兆級(trillions of tokens per day),十月時甚至首次在 OpenRouter 上服務的 token 量超過了閉源模型廠商。

🎯 **對工程師的意義**

如果你在自架或選用開源模型推理服務，這篇文章的訊號是：未來評估推理供應商時，「能否快速適應新模型、新流量、新硬體」會比「這一刻的 benchmark 數字」更關鍵。對自己維運 vLLM/SGLang 的團隊而言，也值得重新檢視目前的設定是否只是針對某個特定流量形態調過的「靜態最優」，而不是真正能隨負載演進的方案。

🔗 **來源**
- 標題：Polymorphic Inference: self-tuning inference for open models
- 作者／機構：Together AI
- 連結：https://www.together.ai/blog/polymorphic-inference

#InferenceOptimization #OpenSourceAI #LLMServing #TogetherAI #AgenticAI #MoE #GPUComputing #AIInfrastructure #ContinuousCompilation #MLSystems
