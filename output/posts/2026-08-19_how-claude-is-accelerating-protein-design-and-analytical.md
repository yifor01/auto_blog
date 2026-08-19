---
title: How Claude is accelerating protein design and analytical chemistry
source: Anthropic Research
url: https://www.anthropic.com/research/Claude-accelerates-protein-design
model: claude-code/sonnet
generated_at: '2026-08-19T06:27:51.883652'
pinned: true
---

📌 【Anthropic 最新研究】Claude 設計的蛋白質結合物,命中率是業界常態的兩倍

TL;DR：Claude 在 15 個蛋白質標靶上設計出結合物,成功率 22-35%,遠高於業界常見的 10-15%。

一名蛋白質工程師要花上數週甚至數月,才能為單一標靶設計出一個可行的結合物。Claude 用 24 到 48 小時,在 15 個標靶上做到了 14 個成功。

🤔 **藥物設計最耗時的一段:從零設計結合蛋白**

大多數現代藥物的作用機制,是靠一個分子精準附著在目標蛋白質上,進而抑制、活化或遞送某種功能。設計這樣的「minibinder」(迷你結合蛋白,一種能緊密鎖定目標蛋白質的小型蛋白質)屬於 de novo design(從零設計),過去需要蛋白質工程師投入數月時間進行運算、最佳化與篩選。近年雖然已有機器學習模型能加速這個流程,協助設計並排序候選結合物,但仍普遍需要運算專家花費數天甚至數週進行繁瑣的流程調度,而濕實驗室(wet lab,實際以化學與生物方法驗證分子的實驗室)的驗證階段更需要數週時間。

🧩 **實驗設計:兩種模式、15 個標靶、外部實驗室驗證**

Anthropic 使用 Claude Opus 4.8 與 Mythos Preview,針對 15 個蛋白質標靶執行了一次多臂(multi-arm)蛋白質設計實驗。標靶選擇上,多數取自業界常見的蛋白質設計基準測試(包括 Adaptyv Bio 的 BenchBB),另外加入兩個來自 Adaptyv Bio 最新競賽的全新標靶——15-PGDH 與 GDF-8,目的是確保 Claude 無法依賴訓練資料中已有的成功案例或線上搜尋結果,所有設計皆需通過原創性檢查。

實驗採用兩種模式:
- **多標靶模式**:Claude 在單一 Claude Science 工作階段中同時對所有標靶進行設計,Opus 4.8 與 Mythos Preview 各執行 48 小時,動用最多 12,500 個 NVIDIA H100 GPU 小時的運算資源,用於執行專門的蛋白質設計與折疊模型。
- **單標靶模式**:每個標靶各自獨立進行,多個工作階段平行執行,Mythos Preview 針對每個標靶執行 24 小時,動用最多 2,500 個 NVIDIA H100 GPU 小時。

整個過程除了初始提示詞外,幾乎沒有額外的人為介入。設計結果由外部評估機構 Adaptyv Bio 與 Twist Bioscience 獨立進行實際製造與濕實驗室測試。

📊 **命中率 22-35%,是業界常態的兩倍以上**

- 15 個標靶中,Claude 成功設計出結合物的有 14 個
- 至少 6 個標靶產出了高親和力(high-affinity)結合物,至少 4 個標靶的最佳設計達到或超越目前已發表的最佳親和力紀錄
- 多標靶模式下,Mythos Preview 與 Opus 4.8 的整體命中率(designs 中實際成功結合的比例)分別為 26.7% 與 22.6%
- 單標靶模式下,Mythos Preview 的整體命中率提升至 35.1%
- 目前業界常見的蛋白質設計命中率約為 10-15%
- 個別標靶的命中率差異很大,最高達 90%,最低則為 0%

親和力(affinity)代表結合物與標靶結合的緊密程度,高親和力結合物通常是藥效發揮的關鍵,因為它能讓藥物在更低劑量下發揮作用,同時降低副作用風險與製造成本。

💡 **另一個場景:分析化學的例行工作也能交給 Claude**

除了蛋白質設計,Anthropic 也測試了現行可公開使用的 Claude Opus 5 在分析化學任務上的表現。研究人員僅提供某委外檢測實驗室的原始 NMR(核磁共振)與 LC-MS(液相層析質譜)檔案,搭配一段兩句話的提示詞,Claude 便在 23 分鐘與 19 分鐘內完成分析報告,其結果在氫原子數與純度判定上與該實驗室的人工分析結果一致(96.4% 對比 96.33%)。這顯示一般可公開取用的模型,已經能夠承擔部分需要專業化學知識、但流程相對例行化的分析工作。

⚠️ **目前仍是實驗性結果,尚未開放給所有科學家使用**

文中提到,這次分享的成果是由 Mythos 與 Opus 系列模型組合完成,而生命科學研究任務目前在 Anthropic 最強大的模型中仍處於限制狀態,官方表示正在籌備一項針對科學家的存取計畫,但尚未正式推出;現階段一般可公開使用的最強模型仍是 Opus 5。此外,文中也指出,加速藥物開發早期階段只是整體藥物開發流程的一環,許多環節的瓶頸更多來自政策與營運層面,而非核心科學能力本身。

🎯 **實務啟示**

對於關注 AI 在科學研究應用的工程師與研究者而言,這個案例的意義在於:蛋白質設計這類過去高度仰賴專家經驗與濕實驗室反覆試錯的任務,正在被證明可以用生成式模型在遠短於傳統週期的時間內完成,且命中率已經超越人類專家團隊的典型水準。同時,分析化學案例說明了另一種更容易落地的價值路徑:讓通用模型承接科學家日常工作中耗時但相對機械化的分析步驟,直接釋放專家的時間去處理更高階的判斷工作。

🔗 **來源**
- 標題：How Claude is accelerating protein design and analytical chemistry
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/research/Claude-accelerates-protein-design

#Anthropic #Claude #ProteinDesign #DrugDiscovery #AIforScience #ComputationalBiology #LifeSciences #AnalyticalChemistry #MachineLearning #LLM
