---
title: Google DeepMind Releases AlphaGenome Atlas
source: Hacker News
url: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/
model: claude-code/sonnet
generated_at: '2026-09-08T20:14:33.705408'
score: 86
---

📌 【Google DeepMind】AI 算出 90 億種基因突變的影響，一次攤在你眼前

TL;DR：DeepMind 推出 AlphaGenome Atlas，預先算好人類基因組所有可能單一鹼基突變的分子效應，開放免程式碼查詢。

人類基因組有 30 億個鹼基對，但科學家真正看得懂的，只有其中負責製造蛋白質的 2%。剩下的 98%，DeepMind 這次決定用運算蠻力直接算給你看。

🤔 98% 的基因組還是一團迷霧

人類基因組雖然只有約 30 億個鹼基對，但目前科學界對負責編碼蛋白質的 2% 區域理解相對透徹，對其餘 98% 的非編碼區域仍所知有限。DeepMind 先前推出的 AlphaGenome 模型，已經能預測非編碼 DNA 區域的單一變異如何干擾蛋白質製造等分子過程，但缺乏一張完整的全局地圖。

🧩 用 AI 算完所有可能的突變

AlphaGenome Atlas 是一個資料庫，預先計算並收錄了人類基因組中每一個可能的單一核苷酸變異（single nucleotide variant）造成的效應。DeepMind 用 AlphaGenome 模型，把全部 90 億種單一鹼基變化的調控影響都算過一遍，產生了一個高達 1 PB（petabyte）的龐大資料集。

為了讓研究者能快速上手，Atlas 引入了 AlphaGenome Variant Impact（AVI）分數，一個把編碼區與非編碼區的預測結果合併成單一數值的評分，讓研究者不必逐條翻閱成千上萬筆資料，就能快速篩出最值得深入研究的變異。

📊 已經在真實研究中派上用場

| 應用場景 | 使用單位／研究者 | 成果 |
| --- | --- | --- |
| 罕見基因變異 | Broad Institute，Laura Covill 團隊 | 用 AVI 分數篩選罕見疾病候選變異，鎖定 DNM1 基因中一個關鍵變異，預測它會造成錯誤的剪接位（splice site），成為解開懸案的關鍵證據 |
| 複雜性狀 | Gareth Hawkes 博士 | 分析英國 UK Biobank 超過 54,000 名參與者的資料，依預測的分子效應分組變異，多找出 22% 的非編碼基因關聯；聚焦影響力前 1% 的變異，鎖定 19 個與身體質量指數（BMI）相關的基因區域 |

💡 分數的價值在於把預測變成排序

過去研究者面對非編碼區變異時，往往缺乏有效的篩選標準，只能大海撈針；現在有了單一可比較的分數，等於把搜尋範圍從全基因組收斂到少數幾個高機率候選區域，這正是 Hawkes 團隊能在 5 萬多人的資料裡多找出兩成關聯的關鍵。

🎯 實務啟示

DeepMind 把 Atlas 做成免程式碼技能即可操作的網站入口，目標是讓臨床研究者與生物學家都能直接查詢，而不只是限於熟悉生物資訊工具鏈的團隊。對於做基因體學相關研究或藥物標的探索的團隊而言，AVI 分數可以作為變異優先排序的第一道篩子，再搭配既有的濕實驗（wet lab）驗證流程收斂候選名單。

🔗 來源
- 標題：Google DeepMind Releases AlphaGenome Atlas
- 作者／機構：Google DeepMind（原文轉載自 Hacker News，作者 utiiiD）
- 連結：https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/

#GoogleDeepMind #AlphaGenome #Genomics #AIforScience #Bioinformatics #DNA #PrecisionMedicine #MachineLearning #RareDisease #GenomicResearch
