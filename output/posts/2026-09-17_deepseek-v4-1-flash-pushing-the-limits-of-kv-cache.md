---
title: 'DeepSeek-v4.1 Flash: Pushing the Limits of KV Cache Compression'
source: Hacker News
url: https://zartbot.github.io/blog/model_arch/dsv41flash_arch/en.html
model: claude-code/sonnet
generated_at: '2026-09-17T20:31:09.522142'
score: 103
---

📌 DeepSeek-V4.1 Flash：把 KV Cache 壓到極限的架構

TL;DR：技術報告顯示，DeepSeek-V4.1 Flash 靠 Encoder-Decoder 分離與跨層 KV 壓縮，把長上下文推理成本大幅壓低。

一款號稱「後訓練迭代版」的模型，跑起來卻接近 420 Tokens/s，還伴隨舊版模型陸續下線的消息——這篇部落格作者的觀察，揭開了 DeepSeek-V4.1 Flash 背後其實是一次架構級的重新設計。

🤔 **長程 Agent 把 KV Cache 逼到牆角**

技術報告指出，近年 Long-horizon Agent 讓超長上下文處理成為越來越重要的工作負載，這類任務不只需要高效處理長序列，還需要 KV Cache 的持久化儲存、複用與傳輸。DeepSeek-V4 原本結合能覆蓋全上下文的 Sparse Attention 與覆蓋局部視窗的 Sliding Window Attention（SWA），雖然降低了計算成本，但持久化儲存與資料搬移逐漸成為更突出的瓶頸：長上下文下 Global KV Cache 的用量會主導記憶體與 SSD 佔用，也對 KV Cache 搬移的互連頻寬提出很高要求，最終限制服務吞吐、推高部署成本。

🧩 **Causal Encoder-Decoder 架構：Prefill 只走一半的層**

DeepSeek-V4.1-Flash 是一個多模態 MoE 模型，參數規模 552B，原生支援多模態輸入，最長支援 1M token 上下文。核心設計是 Causal Encoder-Decoder（CED）架構：Decoder 的 Global KV Cache 由 Encoder 最終隱藏狀態投影而來，這意味著長 prompt 的大部分位置只需經過模型 40 層中的前 20 層。這一設計借鑑了 YOCO 的思路，使模型在 Prefill 階段每 token 只啟用 8B 參數，Decode 階段啟用 16B 參數，作者認為這種設計對「輸入主導」的 Agent 場景特別划算。

在 KV Cache 壓縮上，報告描述的是名為 CSA2 的跨層壓縮方案，從三個維度同時下手：通道維度上，用一個 512 維的潛在向量共享每個 attention head 所需的 key 與 value 表示；序列維度上，Encoder 透過通道級學習權重把相鄰 2 個位置合併為 1 個快取條目，Decoder 則保留逐位置的快取；層維度上，多層共享同一份 Global KV，整個網路僅保留 3 份 Encoder 快取與 1 份 Decoder 快取。搭配 FP4 量化後，Global 主 KV 與 Indexer 的儲存增長約為每 token 890 位元組。作者將這種設計類比為一種「遞迴 Transformer」架構——透過修改 Q 並在遞迴過程中重複使用 KV，並引用了另一篇論文〈On the Future Transformer: Loops Are Not What You Need〉作為相關參照。

💡 **這其實該叫 V5，而不是 V4.1**

作者在文中直言，起初以為 V4.1 Flash 只是一次後訓練迭代，直到看完完整技術報告才意識到「應該被稱為 DeepSeek-V5 Flash」。報告給出的比較數據顯示：在相同序列長度下，DeepSeek-V4.1-Flash 所需的運行時 KV Cache 儲存僅約 DeepSeek-V4-Flash 的四分之一，持久化 KV Cache 儲存僅約其八分之一，同時整體效能優於 DeepSeek-V4-Flash——儘管前者的參數規模明顯更大。作者也提到，原始論文對 CED 的敘述較為複雜，但若改以「圍繞 KV Cache、結合電腦架構視角」重新繪圖，設計脈絡會清晰許多。

🎯 **實務啟示**

對於正在做長上下文 Agent 部署的工程師，這篇分析點出一個值得關注的方向：與其單純堆疊 Sparse Attention 降計算量，不如同時從通道、序列、層三個維度壓縮 KV Cache 本身，才能真正緩解長上下文服務的儲存與頻寬瓶頸。Prefill/Decode 分離啟用參數的設計，也提示了「輸入密集型 Agent 工作負載」在架構層面仍有專門最佳化的空間。

🔗 **來源**
- 標題：DeepSeek-v4.1 Flash: Pushing the Limits of KV Cache Compression
- 作者／機構：mfiguiere（Hacker News 提交）
- 連結：https://zartbot.github.io/blog/model_arch/dsv41flash_arch/en.html

#DeepSeek #KVCache #LLMInference #ModelArchitecture #LongContext #TransformerArchitecture #MoE #AIInfrastructure #EfficientInference #AgenticAI
