---
title: Kog is going deeper to squeeze more inference out of GPUs
source: TechCrunch AI
url: https://techcrunch.com/2026/08/14/kog-is-going-deeper-to-squeeze-more-inference-out-of-gpus/
model: nvidia/nemotron-3-ultra-550b-a55b:free
generated_at: '2026-08-15T06:19:45.164847'
score: 84
---

📌 法國新創 Kog 深度優化 GPU，誓言既有晶片跑出 30 倍推論速度

TL;DR：Kog 以軟體深度優化現有 GPU（如 MI300X、H200），目標為大型模型達 30 倍推論加速，首鎖定程式碼生成場景。

當市場熱捧 Cerebras 等專用推論晶片上市，法國新創 Kog 卻反其道而行：與其買新鐵，不如把手邊的 H200、MI300X 「榨乾」。創辦人從白帽駭客出身，帶著逆向工程組合語言的心態，要在現有硬體上把 LLM 推論速度推高 30 倍。

🤔 **專用晶片熱潮下，既有 GPU 還有多少油水可榨？**

Cerebras 五月成功上市，證明市場對極速推論的渴求。但企業數據中心早已佈署大量 AMD MI300X 與 Nvidia H200。Kog CEO Gaël Delalleau 認為：較新一代 GPU 擁有極高記憶體頻寬，這些頻寬「只待被解鎖」。他賭注軟體層面仍有巨大空間，能在企業既有資產上榨出更多推論產能。

🧩 **Kog Inference Engine (KIE)：從組合語言層級逆向工程 GPU**

核心產品 KIE 的設計哲學源自 Delalleau 的雙重背景：固態物理博士（École Polytechnique）與四度 DEFCON CTF 決賽白帽駭客。  
- **物理思維**：理解 GPU 的物理定律與架構極限，以此為邊界條件進行最佳化。  
- **駭客思維**：逆向工程至組合語言與二進制碼層級，搞清楚硬體「實際如何運作」，再將其用於非原設計意圖的目標。  

技術預覽版用開源小模型 Laneformer 2B 實測，單請求達 3,000 tokens/秒（TPS）。但 Delalleau 承認：小模型易優化，真正挑戰在大模型。目前團隊 11 人，每支援一顆新 GPU 就需投入數週至數月進行「GPU 工程研究」，這極度依賴人工、難以快速擴展晶片支援清單。長期規劃是將方法論餵入 Agent 管線自動化，以支援更多晶片與模型。

📊 **200 條商業線索鎖定程式碼生成，9 月驗證大模型 10 倍加速**

Hacker News 曝光後帶來 200 條具體商業線索。首要用例直指軟體工程痛點：Claude Code 用戶常需等待數小時，Anthropic 甚至推出收費的 Fast Mode。Kog 瞄準因延遲而卻步的專業 AI 工作流客戶。設計合作夥伴還包含提示詞生成遊戲/應用的工具，推論加速對他們直接轉化為營收。  
關鍵洞察：潛在客戶不願微調小模型，迫使 Kog 全力攻克大模型加速。Delalleau 訂下里程碑：9 月實現首個主流大模型 10 倍加速，作為啟動 Series A 募資的關鍵證明。

💡 **區隔 ZML 與 Hazy Research：更深層的「GPU 工程研究」，賭注歐洲算力主權**

同樣來自法國的 ZML 選擇繞過 CUDA 支援異構晶片；Stanford Hazy Research 則專注深度加速演算法。Delalleau 定位 Kog 更接近 Hazy Research，但下探至更底層的硬體工程細節。若方法論能自動化，將受惠於歐洲建立自主算力能力的主權順風——已獲 Scaleway 支持、法國 Bpifrance 與 French Tech 2030 補助背書。

⚠️ **手工調校極耗時，11 人小團隊難支援多晶片，大模型驗證仍待證明**

深度優化的代價是極高的人力成本：每顆新 GPU 需數週至數月人工鑽研。11 人團隊在可見未來只能支援極少數晶片。目前僅在 2B 參數小模型展示 3,000 TPS，大模型能否複製此效能、以及能否在 9 月兌現 10 倍加速承諾，仍是最大風險。市場尚未成熟、客戶拒絕小模型，反倒逼迫 Kog 必須啃最硬的骨頭。

🎯 **別只盯著新鐵：既有叢集若能靠軟體榨出 10 倍吞吐，ROI 遠超換硬體**

對管理 GPU 叢集的工程師，Kog 案例提醒：在等待下一代晶片或專用 ASIC 前，既有硬體（H200/MI300X）的記憶體頻寬利用率往往遠未達滿。若這類「GPU 工程研究」方法論能產品化、自動化，將大幅降低推論成本門檻。短期可關注其 9 月大模型基準測試結果，評估是否納入推論優化選項。

🔗 **來源**
- 標題：Kog is going deeper to squeeze more inference out of GPUs
- 作者／機構：Anna Heim @ TechCrunch
- 連結：https://techcrunch.com/2026/08/14/kog-is-going-deeper-to-squeeze-more-inference-out-of-gpus/

#Kog #GPUInference #LLMOptimization #AIInfrastructure #FrenchTech #TechCrunch #InferenceEngine #HardwareAcceleration #DeepTech #SeriesA
