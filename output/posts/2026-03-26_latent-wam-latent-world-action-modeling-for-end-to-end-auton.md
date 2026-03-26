---
title: "Latent-WAM: Latent World Action Modeling for End-to-End Autonomous Driving"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.24581
score: 114
model: gpt-4o-free
generated_at: 2026-03-26T19:37:41.353276
---

📌 【中科院等最新研究】Latent‑WAM：緊湊模型也能達到 SOTA 自動駕駛規劃  

你以為只有龐大模型才能在自動駕駛中領先？最新研究顯示，只有 1 億參數的 Latent‑WAM 就能超越現有感知‑自由方法。  

🤔 **感知‑自由規劃受限於表示方式**  
現有基於世界模型的規劃器常面臨表示壓縮不足、空間理解不足以及時間動態利用不足的問題。在資源與計算預算有限的情況下，這些限制導致規劃品質難以達到理想水準，尤其在需要即時決策的駕駛場景中表現尤為顯著。  

🧪 **SCWE 與 DLWM 兩核心模組設計**  
研究團隊提出 Latent‑WAM 框架，包含兩個關鍵組件：一是 Spatial‑Aware Compressive World Encoder (SCVE)，它從基礎模型中提取幾何知識，並透過可學習的查詢將多視角影像壓縮為緊湊的場景標記；二是 Dynamic Latent World Model (DLWM)，採用因果 Transformer 自回歸預測未來世界狀態，條件依賴歷史視覺與運動表示。該設計在 NAVSIM v2 與 HUGSIM 兩個基準上進行了廣泛實驗。  

 **新狀態：89.3 EPDMS 與 28.9 HD-Score**  
在 NAVSIM v2 上，Latent‑WAM 達成 89.3 的 EPDMS，比之前最佳的感知‑自由方法高出 3.2 分；在 HUGSIM 上取得 28.9 的 HD-Score。這些成績是在顯著減少訓練資料量且僅使用 104M 參數的緊湊模型下得到的。  

💡 **空間感知與動態建模的協同效應**  
SCVE 能夠保留幾何結構的細節同時大幅降維，使得後續的 DLWM 能在較小的標記序列上建模時空動態。因果 Transformer 的自回歸特性確保預測符合時間因果關係，從而在規劃階段提供更準確的未來軌跡。這種「先壓縮再動態建模」的鏈條被視為在資源受限環境下提升規劃品質的關鍵。  

⚠️ **實驗基準限制與模型泛化需觀察**  
目前結果主要基於 NAVSIM v2 與 HUGSIM 兩個模擬基準，真實車輛與複雜天氣條件下的表現尚未驗證。此外，模型雖然參數量小，但其訓練仍依賴於基礎模型的預訓練權重，這在部署時可能帶來額外的依賴成本。  🎯 **適合資源受限的邊緣部署與進一步研究**  
Latent‑WAM 表明，透過更好的表示壓縮與動態建模，緊湊端到端規劃器可以在不依賴耗費資訊的感知管線下達成競爭力表現。對於自動駕駛系統的邊緣裝置或計算預算嚴格的應用，這種方法提供了一條可行的技術路線；未來工作可探索在真實車輛平台上的遷移學習與更廣泛的場景適應能力。  

🔗 **論文連結**  
📝 Latent-WAM: Latent World Action Modeling for End-to-End Autonomous Driving  
👤 Linbo Wang, Yupeng Zheng, Qiang Chen, Shiwei Li, Yichen Zhang  
🏢 Chinese Academy of Sciences; Chongqing Chang’an Technology Co., Ltd; University of Chinese Academy of Sciences; Tsinghua University; Zhongguancun Academy  
🔗 https://arxiv.org/abs/2603.24581  

你認為這種「小模型+智慧表示」的趨勢會在哪些自動駕駛子領域先開花？歡迎留言討論 👇  

#自動駕駛 #端到端 #世界模型 #中科院 #清華大學 #CVPR2025 #AI #機器學習
