---
title: Performance per dollar is getting faster and cheaper
source: Hacker News
url: https://www.wafer.ai/blog/glm52-amd
score: 68
model: google/gemma-4-31b-it:free
generated_at: '2026-07-04T19:26:10.008164'
---

📌 **推理成本危機：AMD 雖然硬體更便宜，但軟體鴻溝仍是關鍵**

TL;DR：AMD GPU 價格僅 B300 的 1/2.75，但缺乏 NVIDIA 的 Day-0 軟體支援，導致部署 frontier models 仍有高工程成本。

面對 Claude Fable、GLM5.2 與 Minimax M3 等 frontier models 每兩週就更新一次的快節奏，推理需求已遠超供應量。當 Blackwell GPU 供不應求導致價格攀升時，市場開始重新審視 AMD 的競爭力。

🤔 **硬體價格優勢與供應缺口**

目前 NVIDIA GPU 價格快速上漲，導致 token 成本增加。相比之下，AMD 的 Instinct MI350 系列在矽片層級具有強大競爭力。以 MI355X 對比 B300，其平均每張 GPU 的價格約為前者的 1/2.75，且硬體規格相當，被視為降低推理成本的潛在解法。

🧩 **軟體生態的「Day-0」劣勢**

儘管硬體規格接近，但 NVIDIA 的軟體優勢讓服務供應商能以極低摩擦、極快速度部署推理服務。而 AMD 的 ROCm 堆疊面臨以下挑戰：

- **缺乏開箱即用的效能**：最新的 frontier models 在 MI355X 上很少能直接達到 SOTA 效能。
- **環境部署困難**：即便僅是尋找一個能執行該模型的映像檔（image）都相當困難。
- **工程週期過長**：缺乏 Day-0 支援意味著最佳化新模型可能需要數週的工程與運算時間，導致 AMD 始終在追趕最新模型的發布速度。

💡 **AI Agent 可能成為填補鴻溝的關鍵**

雖然目前 AMD 在軟體端處於劣勢，但 Wafer 指出，隨著 AI Agent 在 kernel 與模型最佳化（model optimization）方面的能力提升，這種軟體差距正在即時縮小。Wafer 宣稱已多次證明透過最佳化能提升效能，例如在 20k 輸入 / 1k 輸出且快取命中率 60% 的工作負載下，能達到較高的聚合吞吐量。

🎯 **實務啟示**

對於追求成本效益的工程師而言，AMD 硬體提供了極高的「每美元效能」潛力，但必須衡量「硬體省下的錢」是否足以抵銷「額外的工程最佳化時間」。在缺乏 Day-0 支援的情況下，部署新模型將面臨較長的開發週期。

🔗 **來源**
- 標題：Performance per dollar is getting faster and cheaper
- 作者／機構：latchkey
- 連結：https://www.wafer.ai/blog/glm52-amd

#AI #Inference #AMD #NVIDIA #ROCm #GPU #LLM #CloudComputing #Hardware #AIInfrastructure
