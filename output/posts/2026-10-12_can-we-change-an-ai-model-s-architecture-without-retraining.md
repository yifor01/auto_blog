---
title: Can we change an AI model’s architecture without retraining it from scratch?
source: Amazon Science
url: https://www.amazon.science/blog/can-we-change-an-ai-models-architecture-without-retraining-it-from-scratch
model: claude-code/sonnet
generated_at: '2026-10-12T23:46:59.438376'
score: 127
---

📌 【Amazon 新研究】免重新訓練，Transformer 也能換心臟變混合架構

TL;DR：AWS 團隊提出 Priming 方法，用不到源模型 0.5% 的預訓練 token 預算，把 Transformer 的 attention 層轉換成更省記憶體的 state space 層。

🎣 當 AI agent 的任務越拉越長、推理鏈越疊越深，Transformer 底層那筆隨 token 數成長的「記憶體稅」也跟著水漲船高。過去想換一套更省記憶體的架構，唯一辦法是從零開始，燒掉數萬 GPU 小時重新訓練——直到現在。

🤔 **Transformer 的「過目不忘」是怎麼來的**

Transformer 的 attention 機制靠 query、key、value 三個向量判斷每個 token 與歷史 token 的關聯性：query 代表這個 token 在「找什麼」，key 代表其他 token「提供什麼」，兩者越match，該 token 的 value 就越大程度被納入輸出。因為每個新輸出的 token 會再被丟回去當輸入，Transformer 必須把每個新輸入的 key、value 投影存進「KV cache」，而這個 cache 會隨 context 長度線性成長。

Amazon 團隊把這種能逐字精確回憶所有歷史 token 的能力稱為 eidetic memory（過目不忘式記憶）。它讓 in-context learning、長文件推理、RAG 成為可能，但代價隨輸入 token 數增加。不過研究團隊觀察到，不是每個 attention 層都在做同一件事：有些層負責橫跨數萬 token 的長距離檢索，有些層只在處理鄰近子句或複製附近 token。後者其實不需要不斷長大的 cache，一個固定大小、「有點失真但夠用」的摘要，也就是 fading memory（漸退式記憶），就足夠勝任。

🧩 **Priming 三步驟：舊權重直接接上新架構**

Priming 可行的關鍵，在於一個數學上的巧合：Transformer 本質上也是 state space 模型的一種特例。無論是 attention 層還是 SSM 層，輸出都能寫成「value 序列乘上一個決定每個過去 token 對當前 token 貢獻多少的 mixing matrix」。attention 是用 query 和 key 矩陣相乘算出這個 mixing matrix；SSM 則是讓所有過去資訊都流經一個固定維度的 recurrent state，間接產生類似效果。

因此，如果一個固定維度的 SSM 能產生出足夠接近 attention 層的 mixing matrix，源 Transformer 的 query、key、value 投影權重就能直接拿來當 SSM 的輸入投影，只需額外學習 SSM 專屬的參數。團隊用一個便宜的實驗代理指標判斷某層是否適合轉換：把該層換成 sliding-window attention（只保留部分 context），觀察效能掉多少。掉得少的層代表它本來就不需要長距離的 mixing matrix，適合轉成 SSM；這個指標也對應到動態系統理論中的 Hankel rank，衡量多少資訊必須經過 state 這個「瓶頸」。

Priming 實際執行分三步：
1. 層選擇：找出哪些層可以被忠實壓縮進固定大小的 state，其餘保留為 attention。
2. 權重轉移與對齊：用對應的 attention 權重初始化 SSM 層，再用短時間的蒸餾（distillation）讓 SSM 對齊被取代層的行為。
3. 端到端調適：對整個混合模型做 next-token prediction 微調，讓所有層重新協調。

整條 pipeline 消耗的 token 量，不到源模型預訓練 token 預算的 0.5%，且可跨 Transformer 家族（Qwen、Llama、Mistral）、模型類型（dense 或 MoE）、規模（80 億到 320 億甚至更大）通用。

📊 **GKA 表現最好，SSM 甚至打敗雙倍記憶體的 SWA**

研究團隊比較了三種 state space 層：Gated KalmaNet（GKA）、Gated DeltaNet（GDN）、Mamba-2。在可控條件下，GKA 表現最好，其次是 GDN，再來是 Mamba-2。GKA 還有一項獨特優勢：不用重新訓練就能做變動長度的推理計算，讓使用者能直接控制速度與準確度的取捨位置。

另一個反直覺的發現是：一份好的、有損的完整摘要，勝過一份只記錄最近片段但完美精確的記錄。state space 模型即使只用固定大小的狀態，表現仍持續優於 sliding-window attention，即便後者拿到兩倍的記憶體預算。團隊也展示了一個 320 億參數、以 GKA 為基礎的混合模型：在推理類 benchmark 上追平源 Transformer，在 128,000 token 的 context 下解碼速度最高快上兩倍，得出正確答案所需的實際時間最低只要三分之二。

🎯 **實務啟示**

團隊已把 80 億與 320 億參數規模的「已 Priming 混合模型動物園」，連同訓練程式碼、最佳化 kernel 及 vLLM serving plugin，以 Apache 2.0 授權開源。對做架構研究或想替既有 Transformer 減重的工程團隊來說，過去「哪一層能換成 SSM、換幾層最划算、哪種 SSM 最適合」這類問題，終於能在合理成本下系統性測試，不必每次都從零開始燒 GPU 小時。

🔗 **來源**
- 標題：Can we change an AI model's architecture without retraining it from scratch?
- 作者／機構：Amazon
- 連結：https://www.amazon.science/blog/can-we-change-an-ai-models-architecture-without-retraining-it-from-scratch

#Transformer #StateSpaceModels #HybridArchitecture #AmazonScience #LLM #AIAgents #Mamba #Attention #ModelEfficiency #DeepLearning
