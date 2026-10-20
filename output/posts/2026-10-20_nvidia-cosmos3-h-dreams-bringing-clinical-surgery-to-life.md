---
title: 'NVIDIA Cosmos3-H-Dreams: Bringing Clinical Surgery to Life Through Generative
  Simulation'
source: HuggingFace Blog
url: https://huggingface.co/blog/nvidia/cosmos3-h-dreams
model: claude-code/sonnet
generated_at: '2026-10-20T20:52:57.076982'
score: 91
---

📌【NVIDIA 最新發布】首個用真實手術影像訓練的即時生成模擬器

TL;DR：Cosmos3-H-Dreams 用真實膽囊切除術影像，訓練出能即時回應器械動作的生成式手術模擬器。

想像醫師在 VR 頭顯中操作 Cadiere grasper 夾起膽囊、提起組織，眼前的手術場景不是事先錄好的影片，而是模型依據你的動作即時「生成」出來的畫面。NVIDIA 這次把這個設想推進到真實臨床手術的複雜度。

🤔 從桌上縫合到人體內部，難度差在哪

NVIDIA 第一代 Cosmos-H-Dreams 建立在 Cosmos-Predict2.5 之上，驗證了 dVRK 桌上縫合這種相對單純場景的生成式模擬：不用明確建模場景幾何、組織形變與物理交互，而是直接從同步錄製的影片與機器人運動學資料中學出視覺動態。但在人體內部，器械的微小移動可能牽動整個場景：組織會受牽引伸展、反光會改變、結構會被遮擋、煙霧會影響視野。模型必須在生成每一段新影片時維持時間一致性，否則誤差會隨時間累積，逐漸改變器械或解剖結構的外觀。更關鍵的是，生成畫面必須忠實回應平移、旋轉、夾爪等控制指令，看起來合理但不聽指令的畫面，無法作為可互動環境使用。

🧩 Cosmos 3 骨幹加上教師-學生蒸餾訓練

Cosmos3-H-Dreams 建立在 160 億參數、以 Open-H-Embodiment 預訓練的 Cosmos3-H-Embodied-Nano 之上，再用經過篩選的膽囊切除術（cholecystectomy）影片與運動學資料，特化出一個雙向（bidirectional）教師模型。訓練樣本專注於兩支清楚可見且持續參與操作的器械：左手 Cadiere grasper、右手單極電鉤（monopolar hook），並限制相機動作，讓模型聚焦於器械驅動的互動。動作空間共 28 個維度，涵蓋雙臂的姿態與夾爪資訊，加上能量控制、搖桿軸向與按鍵。訓練影片解析度為 832×480，動作資料以 10Hz 對齊。

訓練流程採教師到學生的階段式設計：先讓雙向教師在 24 個未來畫格上學習，再把視野延伸到 72 個畫格（對應 10Hz 下的 2.4 秒與 7.2 秒），讓教師能學到更長的手術動態。接著透過蒸餾，把雙向教師轉為能隨新動作逐段生成影片的因果（causal）學生模型：先用「因果教師強制」在既有紀錄上訓練，再用 Self-Forcing 讓學生在自己生成的內容上訓練，並由教師與一個另外訓練的評論模型（critic）引導，藉此緩解互動式生成過程中誤差累積的問題。第一個發布版本的學生模型每段畫格使用四步 denoising，之後再進一步訓練出兩步版本；作者強調兩步模型是獨立訓練而來，並非直接把四步模型減少取樣步數得到，步數越少推論越快，但畫質也會打折。

⚙️ FlashDreams 串流推論與 Cosmos3-H-Dreams 的部署

即時生成仰賴 NVIDIA 的加速串流推論函式庫 FlashDreams，使 Cosmos3-H-Dreams 能在單張 NVIDIA RTX PRO 6000 GPU 上互動運行。長時間 rollout 也需要管理模型持續增長的 attention 歷史，團隊為此採用改良版的 FadeMem 模組來整併串流生成過程中不斷增加的 key/value 快取；這與 Self-Forcing 互補：蒸餾處理模型如何從自己生成的歷史中學習，快取整併則處理這段歷史在串流生成時如何被儲存。

📊 能否應對訓練時沒見過的操作軌跡

據作者說明，臨床手術過程中可能出現突發狀況，或醫師會做出「訓練資料沒見過」的動作，因此模擬器必須能泛化到這類未知軌跡並生成連貫畫面。文中展示的示範影片以同一張初始畫格為起點，搭配 VR 頭顯錄製的不同器械動作序列，呈現出兩段走向不同、但器械控制與組織形變都連貫一致的場景延續，藉此檢驗器械是否跟隨控制指令、組織是否合理回應互動、解剖與器械外觀是否隨時間保持一致。

⚠️ 定位：視覺逼真不等於生物力學準確

文中明確指出，視覺真實感只是驗證的起點，不是生物力學準確性的證明；作者也坦言目前只涵蓋兩支受控器械，尚未涉及更豐富的多器械協同與遮擋情境。

🎯 下一步方向

作者列出的後續研究方向包括：擴大覆蓋範圍與時間一致性，讓整個手術流程（而非片段）都能被系統化探索；將生成式視覺真實感與具備幾何、接觸力與組織力學的數值模擬結合，讓行為更可被檢驗；邀請外科醫師評估解剖準確性、器械行為與組織反應，建立可重現的基準；支援更多器械的協同操作；以及發展自主手術決策模型。

🔗 來源
- 標題：NVIDIA Cosmos3-H-Dreams: Bringing Clinical Surgery to Life Through Generative Simulation
- 作者／機構：Lukas Zbinden、Javier Gamazo、Nigel Nelson、Mostafa Toloui、Sean Huver（NVIDIA）
- 連結：https://huggingface.co/blog/nvidia/cosmos3-h-dreams

#NVIDIA #GenerativeAI #WorldModel #SurgicalRobotics #MedicalAI #Cosmos #SimulationAI #RoboticSurgery #VideoGeneration #AIinHealthcare
