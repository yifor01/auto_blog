---
title: 'AlphaGenome Atlas: A predictive map of every possible DNA letter change in
  the human genome'
source: Google DeepMind
url: https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/
model: claude-code/sonnet
generated_at: '2026-09-08T20:04:29.281744'
score: 121
---

📌 【Google DeepMind】90億種DNA變異，一次預測到位

TL;DR：DeepMind 釋出全基因組單點變異預測圖譜，助研究者秒速鎖定致病突變。

人類基因組裡，任何一個位置的 DNA 字母都可能發生突變，理論上組合數高達 90 億種。要在實驗室裡逐一驗證每一種變異對生物學的影響，幾乎是不可能的任務。Google DeepMind 這次選擇用運算硬碰硬地把答案先算出來。

🤔 **9 億種可能突變，實驗室測不完的難題**

DNA 是生命的語言，但要解讀基因變異如何在分子層級影響生物功能，一直是個根本性瓶頸。人類基因組中存在約 90 億種可能的單一核苷酸變異（single-nucleotide variant），逐一在實驗室中測試效果並不現實。DeepMind 先前推出的 AlphaGenome 模型已能預測特定變異對生物過程的影響，並在研究界獲得廣泛使用，但研究者仍缺乏一個能綜覽整個基因組變異全貌的工具。

🧩 **AlphaGenome Atlas：把預測結果先算好、擺出來**

AlphaGenome Atlas 是一個包含 90 億個單核苷酸變異預測結果的平臺，透過學術研究免費使用的網站入口、AlphaGenome API，以及 Google Antigravity 中的技能開放使用。整個資料集規模達 1 PB，比 AlphaFold Database 大 30 倍以上。

為了幫助研究者快速排序變異的重要性，DeepMind 同時推出 AlphaGenome Variant Impact（AVI）分數，結合 AlphaGenome（基因調控預測）與 AlphaMissense（蛋白質影響預測）兩個模型的結果，把預測濃縮成單一數值。AVI 分數同時涵蓋編碼區（佔基因組約 2%）與非編碼區（其餘 98%，掌管基因調控活性、也是多數性狀相關變異所在之處）。

每個 AVI 分數還會拆解成「AVI feature attributions」，指出該變異究竟主要影響哪些分子機制，例如 RNA 剪接（splicing）或基因表現量。Atlas 也額外收錄超過 2,500 個反覆出現的 DNA 序列模體（motif），可視為基因組中的「詞彙」。

📊 **從罕見疾病到族群遺傳學的初步應用**

DeepMind 表示，AVI 分數在多項變異致病性與罕見疾病基準測試中，展現出業界領先的表現。在與 GREGoR Consortium 的合作中，Broad Institute 的研究團隊 Laura Covill 與 Anne O'Donnell-Luria 等人利用 AVI 分數，在先前研究中被忽略的候選變異裡，找到了一個影響 DNM1 基因、與癲癇性腦病變密切相關的變異。AlphaGenome 的預測進一步顯示，該變異形成了一個錯誤的剪接位點，導致蛋白質異常延長，隨後的實驗篩選也驗證了這項預測。

💡 **對照 AlphaFold Database 的擴張經驗**

DeepMind 提到，2022 年擴充 AlphaFold Database 時，結構資訊從約 19 萬個實驗結構暴增到超過 2 億個預測結構，並提供無需寫程式即可使用的視覺化介面，成為推動生命科學研究的重要基礎設施。AlphaGenome Atlas 走的是同一條路：把海量預測結果轉化為直覺易用的探索工具。

⚠️ **目前定位為研究資源**

AlphaGenome Atlas 目前是透過免費入口開放給學術研究使用，其核心價值建立在 AlphaGenome 與 AlphaMissense 模型的預測之上；文中提及的 DNM1 案例雖經實驗驗證，但整個資料集規模龐大，多數變異預測本質上仍是模型推論結果。

🎯 **實務啟示**

對於從事罕見疾病或族群遺傳學研究的工程師與研究者，AVI 分數提供了一種先篩選、後聚焦的工作流程：先用 Atlas 快速為海量候選變異排序，再針對高分變異搭配 feature attributions 深入理解其分子機制，最後才投入實驗驗證資源。透過 API 或 Google Antigravity 技能整合，也讓這套流程更容易嵌入既有的生資分析管線。

🔗 **來源**
- 標題：AlphaGenome Atlas: A predictive map of every possible DNA letter change in the human genome
- 作者／機構：Google DeepMind
- 連結：https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/

#AlphaGenome #GoogleDeepMind #Genomics #AIforScience #RareDisease #Bioinformatics #DNA #VariantAnalysis #MachineLearning #PrecisionMedicine
