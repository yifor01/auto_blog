---
title: 'DeepAmbigQA: Ambiguous Multi-hop Questions for Benchmarking LLM Answer Completeness'
source: Apple ML
url: https://machinelearning.apple.com/research/deepambigqa-multihop-questions
model: tencent/hy3:free
generated_at: '2026-08-07T07:33:57.847492'
score: 98
---

📌 【Apple ML 研究】LLM 難以處理歧義問題，連 GPT-5 的回答完整度也令人擔憂

TL;DR：新數據集 DeepAmbigQA 指出，LLM 在處理需解決「名稱歧義」與「多跳推理」的複雜問題時，回答完整度極低。

🤔 **複雜問題對 LLM 的雙重挑戰**

當問題變得複雜，例如：「哪位《熱血拼搏》(Heat) 的演員曾獲得至少一座奧斯卡獎？」這類問題對 LLM 提出了兩個嚴苛要求：
1. **辨識歧義**：必須從多部同名電影中區分出正確的那一部。
2. **多跳推理 (Multi-hop reasoning)**：必須跨越大量演員資料，整合證據以找出正確答案。

目前的問答 (QA) 基準測試（Benchmarks）鮮少能同時對這兩項挑戰進行評估。

🧩 **DEEPAMBIGQAGEN：自動化生成流水線**

為了應對此問題，研究團隊提出了 DEEPAMBIGQAGEN，這是一個自動化數據生成流水線。該流程以文本語料庫與關聯知識圖譜 (Linked Knowledge Graph) 為基礎，能生成既自然又可驗證的問題，並系統性地將「名稱歧義」與「多步推理」嵌入其中。

📊 **DeepAmbigQA 數據集與實驗結果**

研究團隊基於此流水線構建了 DeepAmbigQA 數據集，其中包含 3,600 個問題，其中一半的問題需要解決顯性的名稱歧義。

實驗發現，即使是目前最頂尖的模型，在處理這類問題時表現依然不佳：

| 問題類型 | 精確匹配 (Exact Match) 分數 |
| :--- | :--- |
| 具備歧義的問題 | 0.13 |
| 非歧義的問題 | 0.21 |

實驗結果顯示，即便是 GPT-5 在處理具備歧義的問題時，其精確匹配分數僅有 0.13，顯示出模型在資訊蒐集與回答完整性方面的不足。

⚠️ **對資訊蒐集與完整性的需求**

這些研究結果強調，未來的問答系統需要更強大的能力，以確保在面對複雜情境時，能夠進行穩健的資訊搜集並提供完整的回答。

🎯 **實務啟示**

對於開發者而言，這提醒我們在設計整合搜尋工具的 LLM 應用時，不能僅依賴模型內建知識，必須加強模型在面對歧義實體時的檢索與推理能力，以確保回答的精準度與完整性。

🔗 **來源**
- 標題：DeepAmbigQA: Ambiguous Multi-hop Questions for Benchmarking LLM Answer Completeness
- 作者／機構：Jiabao Ji, Min Li, Priyanshu Kumar, Shiyu Chang, Saloni Potdar @ Apple / University of California, Santa Barbara
- 連結：https://machinelearning.apple.com/research/deepambigqa-multihop-questions

#AI #LLM #DeepAmbigQA #AppleML #MachineLearning #QuestionAnswering #MultiHopReasoning #NLP #KnowledgeGraph #AIResearch
