---
title: Offloaded inference for real-world physical AI robotics
source: Microsoft Research
url: https://www.microsoft.com/en-us/research/blog/offloaded-inference-for-real-world-physical-ai-robotics/
model: claude-code/sonnet
generated_at: '2026-09-23T20:30:34.044021'
score: 110
---

📌 機載 GPU 拖累機器人？微軟實測推理卸載效益

TL;DR：微軟研究首度系統性實測機器人推理卸載，證實把運算搬離機身能同時提升準確率與電池續航。

多數人假設機器人要「聰明」，就得在機身上塞一顆 GPU。但當 physical AI 模型越來越大，機載 GPU 反而可能是拖累效能、吃掉電池的元兇。微軟研究團隊決定把這個假設攤開來實測。

🤔 背景：機載 GPU 是理所當然的選擇嗎

目前 physical AI 的主流做法，是在機器人身上直接配置一顆 GPU（例如直接把 GPU 接上機器人），讓推理工作侷限在這顆機載 GPU 上，由它產生機器人執行任務所需的動作序列。高層次的規劃或許在雲端進行，但任務執行通常仍綁在機器人本體。微軟研究團隊質疑這個預設，理由是隨著 physical AI 模型越來越大、越來越複雜，機載運算的限制也越來越明顯：GPU 耗電量大、降低電池續航、增加成本與重量，還可能讓機器人無法運行最新一代的 AI 模型。

🧩 研究方法：以「廚房撿垃圾」任務系統性測試

為了理解 physical AI 在系統層面的影響，團隊進行了第一個針對機器人 workload 的系統性研究，聚焦於移動式機器人操作（mobile robotic manipulation），以「檢查廚房裡的垃圾並丟進垃圾桶」這類任務作為代表案例。這個任務涉及規劃前往廚房的路徑、感知環境找出垃圾、導航到垃圾所在位置、撿起垃圾，再導航回垃圾桶丟棄。團隊針對三項核心能力挑選具代表性的模型進行評測：語意地圖與規劃（semantic mapping and planning）、導航（navigation），以及操作（manipulation），並在機載、邊緣、雲端等不同運算配置下逐一評估。

團隊也基於研究結果打造了一套工具，用於簡化機器人推理卸載，並在邊緣 GPU 與雲端之間分配推理工作。這套工具以 Kubernetes 作為統一抽象層，在機器人本體運算、邊緣 GPU 與雲端之間分配 physical AI 工作負載，支援用宣告式規格自動容器化與卸載工作負載，並整合機器人模擬器、LeRobot 與 ROS2，方便開發者使用。

📊 數據：卸載推理如何改善效能與電池續航

| 項目 | 現象 | 數據 |
|---|---|---|
| 語意地圖與規劃 | 在記憶體足夠但運算力較弱的 GPU 上明顯變慢 | 相較 A100 最慢達 383% |
| 導航 | 較弱 GPU 上障礙物即時偵測能力下降 | 偵測率下降 30% |
| VLA 操作模型 | 雖未大幅變慢，但準確率明顯受影響 | 換用較小 GPU 時準確率下降 50% |
| 電池續航 | 機載 GPU 大量耗電 | Jetson Thor 機載 GPU 使電池續航縮短達 160%（僅剩數小時） |

團隊也發現，部分較小的 GPU 甚至無法承載完整的移動操作技術堆疊。整體而言，機載 GPU 限制了機器人的表現，而把推理卸載到機外的 GPU 則能提升其運作表現。團隊也比較了以 Raspberry Pi 5 板取代機載 GPU、並把所有資料傳送到卸載 GPU 處理的方案，證實這種做法能提升電池續航。

💡 深入分析：卸載不是免費午餐

團隊強調，把推理卸載到機身之外涉及效能、網路延遲與頻寬，以及可用 GPU 資源之間複雜的權衡取捨，代表卸載並非在所有場景下都是最佳解，而是需要依具體部署環境權衡。隨著 physical AI 模型持續成長、變得更複雜，團隊預期卸載帶來的效益只會更加明顯。

⚠️ 限制

素材並未提供更完整的網路延遲、頻寬需求或成本量化數據，這些權衡細節需參考團隊發布的技術報告。目前公開的範例僅涵蓋 SO-101 與 UR10e 等特定機型，尚不清楚結論在其他機器人硬體組合上的普適程度。

🎯 實務啟示

這套推理卸載工具已納入微軟近期發布的開源框架 Physical AI Toolchain，整合 Azure 雲端服務與 NVIDIA 的 physical AI 技術堆疊，用於資料整理、擴增與評估等 pipeline。文章展示的示範案例，是把微軟鎖定雙臂機器人的 Rho 模型卸載到 Jetson Thor GPU，控制 Mobile Aloha 機器人運作。對於正在設計機器人推理架構的工程團隊而言，這項研究提供了具體的量化依據：與其預設機載 GPU 是唯一選項，不如把它視為效能、電池續航、成本與網路條件之間的一種權衡，並評估邊緣或雲端卸載是否更符合實際部署需求。

🔗 來源
- 標題：Offloaded inference for real-world physical AI robotics
- 作者／機構：Ganesh Ananthanarayanan, Matthew Balkwill, Xenofon Foukas, Sanjeev Mehrotra, Bozidar Radunovic, Connor Settle, Ankit Verma, David White, Shawn Cicoria, Mark Martin, Rachel Johnson, Mayur Patel（Microsoft Research）
- 連結：https://www.microsoft.com/en-us/research/blog/offloaded-inference-for-real-world-physical-ai-robotics/

#PhysicalAI #Robotics #EdgeComputing #InferenceOffloading #MicrosoftResearch #Kubernetes #VLA #JetsonThor #ROS2 #RoboticsAI
