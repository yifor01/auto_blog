---
title: How NVIDIA Groq 3 LPX Deterministic Execution Drives Power-Efficient High-Interactivity
  Inference on NVIDIA Vera Rubin
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/how-nvidia-groq-3-lpx-deterministic-execution-drives-power-efficient-high-interactivity-inference-on-nvidia-vera-rubin/
model: claude-code/sonnet
generated_at: '2026-09-15T20:43:25.583159'
score: 78
---

📌 【NVIDIA】用「決定論」幫 AI 晶片省下浪費的電

TL;DR：Groq 3 LPX 靠可預測的執行排程，縮小電壓安全邊際，換取更省電的高互動性推論。

AI 工廠裡最稀缺的資源不是晶片，而是電。當效能與電力預算掛鉤，工程師開始意識到一件反直覺的事：晶片有相當一部分電力，其實花在「以防萬一」的安全邊際上，而不是真正的運算。

🤔 **為什麼電壓會突然掉下去**

晶片執行 AI 工作負載時，會在簡單的資料重排與高耗電的矩陣乘法之間動態切換，這種切換會在極短時間內造成電流需求的劇烈變化。晶片會先從緊鄰的去耦電容（decoupling capacitor）抽取額外電流，導致電壓瞬間下降；電壓調節器雖然負責把供電拉回目標值，但受限於電感效應無法立即反應，因此會出現「電壓驟降」（voltage droop）。一旦電壓跌破晶片能正常運作的最低值（Vmin），就會產生錯誤結果。為了避免這種最壞情況，晶片必須持續預留一段「電壓安全邊際」，但由於功率與電壓的平方成正比，多提供 10% 的電壓，代價是持續多消耗 21% 的功率——而這些功率大多數時間都是白白浪費的。

🧩 **把排程算死，電流需求就能提前算出來**

NVIDIA Vera Rubin 平臺從工廠與機櫃兩個層級同時處理這個問題：在工廠層級，DSX MaxLPS 軟體能依工作負載動態在機櫃間調度電力，回收原本被閒置浪費的電力額度；在機櫃內部，機櫃層級電容搭配具備電量感知能力的 Intelligent Power Smoothing 軟體，吸收訓練與推論工作負載忽高忽低的電力尖峰。

而針對延遲要求最高的互動層級，平臺加入了低延遲加速器 Groq 3 LPX。它的核心是決定性執行模型：LPU 編譯器會在工作負載開始執行前，就把每一筆資料何時搬到哪個運算單元、每個運算何時執行,精確排到時脈週期的等級，而且這套排程延伸到機櫃內全部 256 顆 LPU 晶片。

支撐這套決定論的硬體設計包括：負責矩陣乘法的 MXM、負責向量運算的 VXM、負責轉置與重排的 SXM，這些運算單元彼此以時脈週期同步；每顆晶片配有無階層架構的晶片內 SRAM；LPU 之間更是直接互連而非透過中介裝置，讓資料傳輸時間本身也變得可預測。因為每次執行所需的時脈週期數固定不變，編譯器可以提前規劃資料搬移的時間表，甚至能事先解決像是兩個運算單元同時寫入同一個記憶體庫這類資源衝突。

💡 **從電流曲線到主動供電**

由於整套排程在執行前就已確定，編譯器也能據此推算出整個工作負載在每個時脈週期的電流需求曲線。這條曲線催生了兩項互補技術：Preemptive Power（PEP）讓晶片提前命令供電網路（PDN）在需求變化來臨前先做好準備；Clock Period Synthesis（CPS）則負責把需求上升與下降的曲線變得更平緩。兩者合力縮小了原本必須持續預留的電壓安全邊際，讓省下來的電力可以轉而投入真正的運算。相較於動態排程的加速器在執行當下才決定資源分配、導致電流需求難以預測、必須預留更大安全邊際，Groq 3 LPX 等於是把一個電力工程問題，提前轉化成編譯期就能解決的排程問題。

📊 **具體效益**

- DSX MaxLPS 讓同樣的機房電力額度內可多部署最多 40% 的 GPU，並帶來 35% 更高的 token 產出量。
- 電壓與功率的平方關係意味著：多 10% 電壓安全邊際，就是持續多花 21% 的電力。

🎯 **實務啟示**

對評估高互動性、低延遲推論硬體的基礎設施工程師來說，決定性執行架構因為能讓電力系統的容錯邊際更緊繃，理論上能在同樣的功耗預算下擠出更多有效算力，這在規劃 AI 工廠電力配置時是值得納入考量的變數。

🔗 **來源**
- 標題：How NVIDIA Groq 3 LPX Deterministic Execution Drives Power-Efficient High-Interactivity Inference on NVIDIA Vera Rubin
- 作者／機構：Tanya Lenz（NVIDIA Developer）
- 連結：https://developer.nvidia.com/blog/how-nvidia-groq-3-lpx-deterministic-execution-drives-power-efficient-high-interactivity-inference-on-nvidia-vera-rubin/

#NVIDIA #Groq #VeraRubin #AIInfrastructure #Inference #PowerEfficiency #LPU #DataCenter #AIFactory #HardwareEngineering
