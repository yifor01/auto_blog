---
title: 'Show HN: Isometric SF – A pixel-art map of the SF Bay Area'
source: Hacker News
url: https://isometricsf.com/
model: claude-code/sonnet
generated_at: '2026-11-14T21:38:29.540178'
score: 78
---

📌 用LoRA蒸餾砍成本：灣區像素地圖背後的技術故事

TL;DR：用開源小模型LoRA蒸餾大模型風格，把像素地圖生成成本砍到四分之一。

如果要用Nano Banana 2把1300平方英里的舊金山灣區，逐格轉成風格統一的像素地圖，作者估計要燒掉近7000美元。但這篇Show HN的作者，最終只用這個數字的一小部分就做出了整張地圖。

🤔 一張地圖，兩種風格挑戰

開發者juscha1從Google Photorealistic 3D Tiles擷取了舊金山灣區約1300平方英里的3D資料，想把它轉換成一張風格統一的等角（isometric）像素地圖，玩法上可以探索像Apple Park、Palace of Fine Arts、UC Berkeley這些知名地標。這個點子的靈感來自Isometric NYC。

🧩 先用大模型練風格，再蒸餾到小模型上線

技術上分兩階段進行：先用Nano Banana 2訓練一個Qwen-Image-Edit 2511的LoRA，用來快速原型化整體風格與生成方法；確認風格可行後，再用Qwen把這個風格蒸餾進一個Klein 4B的LoRA，最終整張地圖就是用這個Klein 4B LoRA量產出來的。作者也提到，自己很享受微調這些開源小模型的過程。

📊 四分之一是怎麼省下來的

作者表示，若整張地圖直接用Nano Banana 2生成，成本大約落在7000美元；換成蒸餾後的Klein 4B LoRA，重現同樣風格只需要原本的四分之一成本。透過「用大模型練風格、小模型做量產」的分工，大幅壓低了這種大規模像素藝術生成的門檻。

🎯 實務啟示

多數需要套用一致風格的大量生成任務，不必每一筆都呼叫最貴的旗艦模型。這個案例示範了一個實用模式：先用大模型確立風格與生成方法，再把這個能力蒸餾進開源小模型的LoRA，就能用小一截的推論成本大量產出，特別適合像這種要對上千張圖片套用統一風格的專案。

🔗 來源
- 標題：Show HN: Isometric SF – A pixel-art map of the SF Bay Area
- 作者／機構：juscha1（Hacker News）
- 連結：https://isometricsf.com/

#LoRA #ModelDistillation #PixelArt #GenerativeAI #QwenImageEdit #OpenSourceAI #FineTuning #ImageGeneration #ShowHN #AIArt
