---
title: 'Xiaomi’s MiLM Plus Releases PROVE: Perception-Aligned Object Removal Metrics
  RC-S and RC-T With a Real-World Video Benchmark'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/11/xiaomis-milm-plus-releases-prove-perception-aligned-object-removal-metrics-rc-s-and-rc-t-with-a-real-world-video-benchmark/
model: claude-code/sonnet
generated_at: '2026-08-12T07:33:24.655214'
score: 93
---

📌 【Xiaomi MiLM Plus】物件移除模型評分不準？PROVE 提出免參考新指標

TL;DR：Xiaomi 提出 RC-S／RC-T 免參考指標，人類評分相關性遠超既有 PSNR、LPIPS 等指標。

一段影片把路人從畫面中抹除，陰影、倒影、被遮擋的結構都重建得天衣無縫——但拿現有指標一評分，結果卻經常把好壞排反。這不是指標算錯了，而是問題本身沒有標準答案。

🤔 物件移除是「一對多」問題，沒有唯一正解

Diffusion 系的物件移除（object removal）模型近年進步很快，能合理重建陰影、倒影與被遮蔽結構，但 PSNR、SSIM、LPIPS、ReMOVE、CFD 這類常用指標經常把輸出的優劣順序判斷錯誤。根本原因是結構性的：物件抹除是一個 ill-posed（不適定）、一對多的任務——同一個「洞」可能有多種合理的填補方式，因此不存在單一的 ground truth 可供比對。Xiaomi Inc. 旗下的 MiLM Plus 團隊針對這個落差，發表了已被 ACM MM 2026 接受的 PROVE（Perceptual RemOVal cohErence）。

🧩 兩個免參考指標，靠局部特徵分布比對

PROVE 提出兩個感知對齊（perception-aligned）指標：RC-S 衡量空間一致性（spatial coherence），RC-T 衡量時間一致性（temporal consistency）。兩者都只對被編輯區域做局部評分，採用滑動視窗（sliding-window）Maximum Mean Discrepancy（MMD）在 DINOv2 特徵空間上計算，且都不需要參考影片。核心概念相同：用深度特徵空間中的局部分布比對，取代傳統的全域聚合評分。

RC-S（空間）：先用連通元件分析（connected-component analysis）把遮罩拆成獨立目標，每個 bounding box 向外擴張其邊長的三分之一後送入 DINOv2，遮罩則下採樣到特徵解析度；接著讓一個 w×w 視窗在特徵圖上滑動，用 Gaussian RBF 核計算被遮罩區域與局部背景特徵之間的平方 MMD，先在每個目標內平均，再跨目標平均。

RC-T（時間）：相鄰兩幀先在兩者遮罩聯集下聯合裁切以避免錯位，再只在兩幀遮罩的交集（也就是兩幀都被修復的區域）內計算 MMD。消融實驗顯示，若拿掉這道裁切步驟，RC-T 會對人為注入的破壞失去敏感度。

PROVE 同時釋出兩層式真實世界影片 benchmark：PROVE-Bench，包含 PROVE-M（80 組配對影片，以腳架拍攝輸入畫面與兩分鐘內拍攝的無目標對照畫面，SAM3 遮罩逐幀精修，經三階段品質控管，並同步套用 Ken Burns 式運鏡增強，每段 81 幀、1080p）以及 PROVE-H（100 段無 ground truth 的高難度影片，涵蓋人群、流水、火焰、紋理地形、多水窪倒影、快速運動等場景，刻意使用未精修的 SAM3 遮罩）。

📊 與人類評分相關性大幅領先，速度也更快

團隊找來 20 位受試者以 Borda count 彙整人類評分排名進行比對：RC-S 的平均 Kendall's τ 為 0.59、Spearman's ρ 為 0.66，相較之下 ReMOVE 僅 0.26／0.29，CFD 僅 0.16／0.18；RC-S 在六個 benchmark 中的五個排名第一，而只看背景區域的 full-reference 變體則在多數資料集上出現負相關。在 RORD-Val 上，RC-S 有 100% 的情況會偏好乾淨影像而非模糊或區域互換的變體，ReMOVE 僅 60.06%，CFD 在模糊條件下僅 49.27%。RC-T 對逐漸增加的破壞程度呈單調反應，而既有的 TC、TF 指標則沒有這個特性。

消融實驗也拆解了各設計選擇的貢獻：使用 DINOv2（平均 τ 0.59）優於 DINOv3（0.51）與 SAM（0.44）；拿掉滑動視窗會損失 0.11；把 MMD 換成餘弦相似度會損失 0.07。效能上，RC-S 也是測試過最便宜的空間指標，比 CFD 快 13.7 倍。在公開排行榜上，SVOR（1.3B）以 0.5197 的綜合 RC-S 領先，EffectErase 則以 0.2525 在 RC-T 上領先。

🎯 實務啟示

PROVE 以 Apache 2.0 授權釋出 PyTorch 程式碼庫，提供單一 CLI 入口 run_prove_metrics.py，需要 Python 3.10+、PyTorch 2.6+、Transformers 4.51+ 與 DINOv2-giant 權重，且遮罩（白色像素標示被移除物件）為必要輸入。對正在開發或評估影片物件移除、修復（inpainting）模型的團隊而言，與其繼續依賴會誤判優劣的 PSNR／LPIPS 類指標，不如直接把 RC-S／RC-T 接入評估流程，並用 PROVE-Bench 的高難度子集（PROVE-H）壓力測試模型在複雜真實場景下的表現。

🔗 來源
- 標題：Xiaomi's MiLM Plus Releases PROVE: Perception-Aligned Object Removal Metrics RC-S and RC-T With a Real-World Video Benchmark
- 作者／機構：Michal Sutter（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/08/11/xiaomis-milm-plus-releases-prove-perception-aligned-object-removal-metrics-rc-s-and-rc-t-with-a-real-world-video-benchmark/

#Xiaomi #VideoInpainting #ObjectRemoval #EvaluationMetrics #DINOv2 #ComputerVision #ACMMM2026 #NoReferenceMetric #VideoBenchmark #GenerativeAI
