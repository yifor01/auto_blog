---
title: 'Glyph: A Multi-Strategy Agentic System for Column Description and Sensitivity-Ontology
  Tagging of Enterprise Data Catalogs'
source: Apple ML
url: https://machinelearning.apple.com/research/glyph-column-description-tagging
model: claude-code/sonnet
generated_at: '2026-09-16T20:17:41.507039'
score: 94
---

📌 Apple Glyph：用多智能體聯手治理企業資料表的欄位標籤

TL;DR：Apple提出生產級系統Glyph，用協作式LLM agent自動生成欄位描述並標註敏感性分類，微調編碼器讓同標籤檢索的NDCG@10從0.55衝到0.92。

企業資料湖的資料表增長速度，早已超過人類資料治理團隊手動撰寫描述、標註分類標籤的能力。結果就是大量欄位既沒有說明文字，也沒有治理標籤，資料探索、存取控制與法規遵循全部受到拖累。Apple ML團隊發表的Glyph，正是針對這個「文件債」問題設計的生產系統。

🤔 兩個耦合問題，一套多智能體架構

Glyph把「欄位描述生成」與「欄位類型標註（資料分類）」這兩個原本分開處理的問題，框架成一組以狀態圖（stateful graph）協同運作的LLM agent。系統核心分成兩大模組：Descriptor負責生成描述，Tagger負責分類標籤。

🧩 Descriptor：從產生該欄位的Pipeline原始碼找答案

不同於憑欄位名稱和樣本值猜測用途，Descriptor會透過reasoning–acting的工具呼叫迴圈（主動式RAG），即時從企業內部的GitHub檢索出真正產生這個欄位的pipeline原始碼，再據此生成描述。這種「有憑有據」的作法，讓描述文字有明確的程式碼來源可追溯。

🧩 Tagger：三種策略並行，再用RRF融合排序

Tagger要從一套治理過的275個葉節點的資料分類本體（Data Classification Ontology）中挑出正確標籤。它並行執行三種互補策略：
- 描述標籤器（description tagger）
- 依業務線規則的正則標籤器（line-of-business regex tagger）
- 後端接一個微調過的對比式編碼器、搭配向量資料庫的metadata標籤器

三者各自輸出排序結果後，再以Reciprocal Rank Fusion（RRF）融合成最終標籤。

📊 微調6層MiniLM編碼器，同標籤檢索大幅提升

團隊針對metadata標籤器，用in-batch對比學習目標微調了一個6層的MiniLM編碼器。在同分佈的held-out測試集上，同標籤檢索表現相較原始base編碼器有顯著提升：

| 指標 | 原始base編碼器 | 微調後 |
|---|---|---|
| NDCG@10 | 0.55 | 0.92 |
| MAP@100 | 0.19 | 0.90 |

整體端到端多標籤標註品質，Apple團隊採用recall-weighted F2作為目標指標，在三組評估資料上報告結果，並透過ablation實驗逐一拆解每種策略與RRF融合各自的貢獻。

💡 與既有方案的差異：不看值、看程式碼、有出處

Apple團隊特別強調Glyph與過往column-type-annotation研究、以及商用的value-based／regex敏感性掃描工具的差異：Glyph採用value-free且code-grounded的設計（不需讀取實際資料值即可判斷欄位語意），每個標籤都附帶可追溯的出處（per-tag provenance），並且在部分模組失效時仍能優雅降級（graceful degradation）運作。這些工程決策，是讓多智能體LLM資料編目系統能被稽核、能在生產環境穩定運作的關鍵。

🎯 實務啟示

對正在處理資料治理債務的工程團隊而言，Glyph示範了一個可行的方向：與其單靠一個LLM硬猜欄位語意，不如把描述生成與分類標註拆成專職agent，各自用最合適的檢索與比對策略（程式碼溯源、規則比對、向量檢索），再用RRF這類簡單有效的排序融合方法整合結果。value-free設計也值得注意，對敏感資料場景而言，「不需要讀取實際數值」本身就是一種隱私友善的架構選擇。

🔗 來源
- 標題：Glyph: A Multi-Strategy Agentic System for Column Description and Sensitivity-Ontology Tagging of Enterprise Data Catalogs
- 作者／機構：Kostia Kudriavtsev, Parvez Rafi, Sha Sundaram（Apple ML）
- 連結：https://machinelearning.apple.com/research/glyph-column-description-tagging

#DataGovernance #LLMAgents #RAG #DataCatalog #ContrastiveLearning #AppleML #DataClassification #EnterpriseAI #InformationRetrieval #Privacy
