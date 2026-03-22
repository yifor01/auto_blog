---
title: "Apple 怎麼讓企業搜尋同時找到文字、圖片和影片——AMES 的 late interaction 架構"
date: "2026-03-17"
paper_url: "https://arxiv.org/abs/2603.13537"
paper_title: "AMES: Approximate Multi-modal Enterprise Search via Late Interaction Retrieval"
tags: [Search, Multimodal, Late-Interaction, Apple, Enterprise]
tldr: "Apple 用 late interaction 做多模態企業搜尋"
---

你在公司內部搜「Q3 revenue breakdown」，期望看到的可能是一張圖表，不是一段文字。但大多數企業搜尋引擎只會搜文字，頂多加個 tag 做圖片過濾。想搜影片裡的某個片段？想都不要想。Apple 的研究團隊做了一個叫 AMES 的系統，用 late interaction 把文字、圖片、影片全部拉進同一個搜尋框架，而且直接跑在他們基於 Solr 的生產系統上。不用換搜尋引擎，加一層就能搜多模態。

🔍 問題出在哪

企業內部資料天然就是多模態的，設計稿、投影片截圖、會議錄影、技術文件都有。但搜尋系統是「單模態思維」設計的。想搜圖片？寫一套 image search 邏輯。想搜影片？再寫一套。每多一種模態就多一套維護成本，而且跨模態的結果怎麼合併排序本身就是工程難題：分數來自不同模型，scale 不同，直接比較沒有意義。

根本問題是架構性的。你需要的不是「每種模態各一個搜尋引擎」，而是一個統一框架。

🛠️ AMES 怎麼做

如果你熟悉 ColBERT，概念是類似的，都是 late interaction。query 和 document 各自編碼成一堆 token-level 的向量，檢索時才做 token 之間的交互計算（MaxSim）。AMES 把這個想法推廣到多模態：

→ 文字拆成 text tokens
→ 圖片拆成 image patches
→ 影片拆成 video frames

這三種「token」通過 multi-vector encoder 映射到同一個表示空間。檢索的時候完全不需要知道對面是什麼模態。一個 text query 可以跟 image patches 算 MaxSim，也可以跟 video frames 算 MaxSim，邏輯完全一樣。這就是「backend agnostic」的意思。

但 late interaction 有個老問題：慢。每個 document 不是一個向量而是一堆向量，token-level 交互計算量比 single-vector 方法大很多。企業環境可能有幾百萬份文件，暴力算 MaxSim 不現實。

AMES 的解法是 two-stage pipeline：

第一階段，parallel token-level ANN search。對 query 的每個 token 各跑一次 approximate nearest neighbor 搜尋，然後用 per-document Top-M MaxSim approximation 粗篩。重點是不需要算完整的 MaxSim，只看每個 document 最相關的 M 個 token 交互。

第二階段，accelerator-optimized Exact MaxSim re-ranking。對粗篩出來的少量候選才做精確計算，用 GPU 加速。

兩階段加起來，把 late interaction 從「學術上好但生產上太慢」拉到了可以在 Solr 上跑的程度。

📊 效果

他們在 ViDoRe V3 benchmark 上測試，用的措辭是「competitive」。

這裡我想誠實說，這不是 SOTA。他們沒有宣稱打敗所有 baseline，而是說在接近最好方法的同時，能在生產環境落地。

我覺得這個定位其實很務實。學術論文追 SOTA 是正常的，但企業搜尋在意的不只是 benchmark 上那 0.x% 差距。系統能不能部署在現有架構上？能不能處理千萬級文件？延遲可不可以接受？AMES 的重點不在分數最高，而在證明 late interaction 在生產規模的企業搜尋中能跑得動。

🤔 我怎麼看

Apple 做這件事不意外，他們內部資料天然多模態，Keynote 投影片、設計稿、內部影片，搜尋需求擺在那裡。

幾個我覺得值得關注的點：

統一架構的維護成本優勢是巨大的。少維護幾套 modality-specific 的 pipeline，長期省下的工程時間遠超開發 AMES 本身的成本。這是那種不 sexy 但每個做過企業搜尋的工程師都會心有戚戚焉的痛點。

late interaction 的 token-level 粒度對企業搜尋特別有用。搜一份 30 頁的 PDF，你不需要整份文件跟 query 相關，只要其中某幾段相關就行。Token-level 匹配天然就支援這種局部相關性，比 single-vector 的 document-level 表示強很多。

不過影片搜尋的 frame-level 處理方式算是比較粗暴。把影片拆成 frames 當圖片索引，效果跟影片長度和內容類型有關。一段 10 分鐘的會議錄影和一段 30 秒的 demo 影片，sampling 策略應該不同，但論文沒深入討論這個。

「competitive」而非 SOTA 是一個 honest trade-off。用統一架構換工程簡潔性，每個單一模態上可能都不是最好的。對企業來說，這個 trade-off 通常值得。

如果 late interaction 真的能在生產規模下跑起來，那 ColBERT-style 的 multi-vector retrieval 可能比我們想像的更接近大規模落地。AMES 不是第一個說這件事的，但可能是第一個由 Apple 這種規模的公司在生產環境驗證的。

你們公司的搜尋系統現在怎麼處理多模態內容？還是根本沒有處理？

📄 論文：https://arxiv.org/abs/2603.13537

<!-- fb -->

你在公司搜「Q3 revenue breakdown」，期望的可能是一張圖表而不是一段文字。但大多數企業搜尋只會搜文字。Apple 做了 AMES，用 late interaction 把文字、圖片、影片拉進同一個搜尋框架，直接跑在 Solr 生產系統上。

🛠️ 怎麼做
→ 文字拆 text tokens、圖片拆 image patches、影片拆 video frames
→ 通過 multi-vector encoder 映射到同一個表示空間
→ 檢索時不需要知道對面是什麼模態，邏輯完全統一
→ Two-stage pipeline：ANN 粗篩 + GPU 加速 Exact MaxSim 精排

📊 在 ViDoRe V3 達到「competitive」，不是 SOTA，但重點是在生產規模能跑。

🤔 統一架構的維護成本優勢巨大。少維護幾套 modality-specific pipeline，長期省下的工程時間遠超開發成本。late interaction 的 token-level 粒度對局部相關性特別有用。

如果 ColBERT-style retrieval 真能在生產規模下跑，multi-vector 方法可能比我們想像的更接近大規模落地。

#Apple #MultimodalSearch #LateInteraction #EnterpriseSearch #ColBERT #GenAI
