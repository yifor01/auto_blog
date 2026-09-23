---
title: Claude discovers a novel enzyme system with CRISPR-like repeats
source: Anthropic News
url: https://www.anthropic.com/news/claude-discovers-novel-enzyme-system
model: claude-code/sonnet
generated_at: '2026-09-23T20:30:34.043711'
score: 121
---

📌 【Anthropic】Claude 21 小時自主發現類 CRISPR 新酶系統

TL;DR：Anthropic 新設立的生命科學實驗室讓 Claude 自主搜尋 DNA 資料庫，發現一套帶有類 CRISPR 重複序列的全新酶系統。

CRISPR、限制酶、Taq polymerase，這些改寫生物醫學史的工具，最初都只是某位科學家在浩瀚基因體資料裡「覺得哪裡怪怪的」。如今，這份「覺得怪」的直覺被交給了一群 AI agent，而且只花了 21 小時。

🤔 背景：從人類直覺到 AI 協作的生物發現

Anthropic 在 2026 年春天成立了新的生命科學研究團隊與實驗室，目標是驗證通用 AI 模型能否系統化並加速生物學發現。文章回顧了幾個歷史案例：限制酶在細菌免疫系統中被發現後催生了整個生技產業；Taq polymerase 在黃石公園溫泉的細菌中被找到，成為 PCR 技術的基礎；CRISPR 最早只是細菌 DNA 中一段不尋常的重複序列，如今已成為基因編輯藥物的基礎。這個團隊想做的，就是把這種「發現」的過程系統化。

🧩 怎麼做的：把探索基因體資料庫的工作交給 Claude

研究團隊給 Claude 的指令很簡單：搜尋龐大的 DNA 序列資料庫，找出反轉錄酶（reverse transcriptase，RT，一種把 RNA 複製成 DNA 的酶）中有趣的新例子。除了最初的 prompt 與後續的實驗室工作，中間的分析過程幾乎全由 Claude agent 自主完成：篩選 RT 家族、調查基因體鄰近序列，並依自己的判斷挑出值得關注的候選對象。

團隊描述的典型工作流程是：Claude 先針對特定蛋白家族做文獻回顧，用公開資料重現既有研究結果以驗證方法；接著搜尋沒有已知功能描述的家族成員或基因體鄰近序列，為每個候選對象寫一份人類可讀的報告，提出可能功能並附上證據；後續分析階段，Claude 會批判性地檢視這些證據，大多數候選對象在這一步就被淘汰。一輪搜尋可能只留下一個值得測試的候選，也可能一個都沒有。能通過篩選的候選，才會進入實驗室，由人類科學家表現蛋白質並做生化與結構分析，Claude 則協助解讀數據。

📊 數據：950 個 agent、210 萬 token，找到一個異常重複序列

這次搜尋動用約 950 個 agent、耗費 210 萬 token，花了 21 小時。其中一個 agent 發現了一個異常之處：某個外觀奇特的 RT 基因旁邊，存在一段重複的 DNA 序列模式。進一步分析與實驗室測試後，團隊確認這是一套先前未被描述過的酶系統，存在於感染細菌的病毒（噬菌體）中，命名為 array-associated reverse transcriptases，簡稱 ART。整體而言，Claude agent 共蒐集超過 20 萬個 RT，篩選出 3,500 個新候選系統，再縮小到 20 個最值得分析的候選對象並產出人類可讀報告。團隊指出，這類分析對一位資深科學家而言，通常需要數週到數月的工作量。

💡 深入分析：為什麼這個發現值得注意

ART 系統的特徵組合（伴隨一段非編碼 DNA 重複序列陣列，加上一個功能未知的附屬蛋白）過去只在少數幾個系統中一起出現過，而這些系統無一例外都具備可編程、能執行切割、複製、貼上 DNA 等操作的能力。值得注意的是，這個 RT 本身在先前的研究中已被鑑定過，但 Claude 似乎是第一個注意到它與重複序列陣列、附屬蛋白共同構成一套完整系統的研究者。CRISPR 基因編輯技術先驅、MIT 暨 Broad Institute 教授 Feng Zhang 在審閱預印本後表示，這是 AI agent 對生物學發現做出貢獻的令人興奮的例子，RNA 重複陣列與反轉錄酶的關聯性確實值得進一步研究。

⚠️ 限制：功能仍未知，這只是起點

團隊坦言，目前仍不清楚 ART 系統的實際功能，相關研究仍在進行中。他們選擇提前公開這項發現，一方面展示 Claude 的能力，另一方面也讓外界了解實驗室正在進行的工作方向。所有實驗室工作僅涉及 BSL-1 與 BSL-2 等較低生物安全等級，不處理會感染人類的病原體，且全數由人類科學家執行。

🎯 實務啟示

這個案例展示了一種新的科研協作模式：AI agent 負責大量、重複性的資料篩選與假說生成，人類科學家則專注於審核候選對象與實驗室驗證。對於處理大規模非結構化資料庫的研究團隊而言，「先讓 AI 寫出可驗證的候選報告，再由人類把關」的工作流程，或許比單純要 AI「給答案」更務實。

🔗 來源
- 標題：Claude discovers a novel enzyme system with CRISPR-like repeats
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/news/claude-discovers-novel-enzyme-system

#AI4Science #Anthropic #Claude #CRISPR #SyntheticBiology #Bioinformatics #EnzymeDiscovery #ReverseTranscriptase #AIAgents #GenomeMining
