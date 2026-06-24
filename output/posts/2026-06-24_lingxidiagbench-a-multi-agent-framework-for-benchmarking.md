---
title: 'LingxiDiagBench: A Multi-Agent Framework for Benchmarking LLMs in Chinese
  Psychiatric Consultation and Diagnosis'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2602.09379
score: 90
model: google/gemma-4-31b-it:free
generated_at: '2026-06-24T20:08:23.735065'
---

📌 LingxiDiagBench：評估 LLM 中文精神科診斷能力的 Multi-Agent 基準框架

TL;DR：推出首個針對中文精神科診斷的大規模多代理基準，揭示諮詢品質與診斷準確率之間的落差。

在醫療 AI 的應用中，診斷精神疾病比一般疾病更複雜，因為它高度依賴動態的對話諮詢而非單一的檢驗數值。當 LLM 扮演精神科醫生時，它能否在對話中精準捕捉症狀並給出正確診斷？

🤔 **精神科診斷中的動態諮詢挑戰**

精神科診斷的核心在於「諮詢過程」，這要求模型必須具備動態調整對話方向的能力。LingxiDiagBench 正是為了填補這一空白而設計，旨在評估 LLM 在中文精神醫療情境下的表現。

🧩 **透過 Multi-Agent 框架模擬診斷流程**

該基準採用多代理（Multi-Agent）框架來模擬現實中的診斷過程，將評估重點放在兩個關鍵維度：
1. 諮詢品質：模型在與患者對話時的引導能力與資訊獲取品質。
2. 診斷準確率：最終給出的診斷結果是否正確。

📊 **諮詢品質與診斷準確率之間存在落差**

研究結果指出一個值得關注的現象：諮詢品質的高低並不直接等同於診斷的準確率。這意味著即便一個模型在對話中表現得像個專業的醫生（諮詢品質高），最終的診斷結果仍可能出錯，顯示出 LLM 在處理精神醫療邏輯推理上的潛在不足。

🎯 **實務啟示**

對於開發醫療 LLM 的工程師而言，這項研究提醒我們：不能僅靠對話的「流暢度」或「共情能力」來評估醫療模型的效能。在精神醫療等高風險領域，必須建立像 LingxiDiagBench 這樣能同時量化「過程（諮詢）」與「結果（診斷）」的評估體系，才能確保模型的安全性與準確性。

🔗 **來源**
- 標題：LingxiDiagBench: A Multi-Agent Framework for Benchmarking LLMs in Chinese Psychiatric Consultation and Diagnosis
- 連結：https://huggingface.co/papers/2602.09379

#LLM #Psychiatry #Benchmarking #MultiAgent #MedicalAI #ChineseNLP #HealthcareAI #Diagnosis #Evaluation #LingxiDiagBench
