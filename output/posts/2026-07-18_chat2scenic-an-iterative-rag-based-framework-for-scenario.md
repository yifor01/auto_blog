---
title: 'Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous
  Driving'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.14387
score: 111
model: tencent/hy3:free
generated_at: '2026-07-18T07:31:12.792035'
---

📌 【HuggingFace Papers】Chat2Scenic：用迭代 RAG 框架生成自駕測試場景指令碼

TL;DR：迭代式 RAG 框架將自駕場景指令碼編譯成功率拉到 76.42%，並開源 benchmark。

自動駕駛系統的驗證需要大量符合法規的測試場景，但在模擬測試中，這些場景其實是可執行的指令碼。如何從法規文字自動生成這類指令碼，一直是未解難題——現有方法不是難以擴充，就是編譯成功率慘不忍睹。

🤔 **現有方法在擴充性與編譯率之間二選一**

在模擬測試裡，場景是用 Domain Specific Language（DSL，領域特定語言）寫成的可執行指令碼。過去做法有兩條路：retrieval-assemble 方法能達到還算合理的編譯率，但缺乏擴充性；retrieval-based full-script generation 雖然直接生成整份指令碼，編譯成功率卻很低。兩者都卡在根本的 trade-off 上。

🧩 **Chat2Scenic：第一個迭代式 RAG 場景生成框架**

作者提出 Chat2Scenic，這是首個基於 iterative retrieval-augmented generation（迭代式檢索增強生成）的框架，專門用來生成 DSL 場景指令碼。它提供 chatbot 介面，支援互動式的場景修正（interactive scenario refinement），並整合 RAG 將生成過程 grounding 在法規知識與 DSL 語法之上，讓產出的指令碼既合規又可編譯。

📊 **編譯成功率與框架準確度都大幅領先**

作者以 SOTA LLM 進行評估，並與兩種現有方法對比，關鍵資料如下：

| 方法 | Compilation Success Rate (CSR) | Framework Accuracy (FA) |
|------|-------------------------------|--------------------------|
| Retrieval Assemble | 30.08% | 11.03% |
| Retrieval full-script generation | 16.26% | 10.86% |
| Chat2Scenic | 76.42% | 58.17% |

Chat2Scenic 在 CSR 與 FA 兩項指標上都明顯優於既有方法。

🤔 **附帶釋出 123 筆開源 Benchmark**

除了框架本身，作者也提出一個開放 benchmark，包含來自多種法規的 123 個場景，涵蓋 NHTSA、United Nations Vehicle Regulations 以及其他來源，供後續研究使用。

🎯 **實務啟示**

對自駕模擬與測試團隊來說，Chat2Scenic 把「法規文字 → 可執行 DSL 指令碼」這條路徑變得可行，且支援互動式修正，能減少手刻場景指令碼的人力。其開源程式碼與 benchmark 也已釋出，適合直接拿來做內部測試流程的基線或對比實驗。

🔗 **來源**
- 標題：Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving
- 連結：https://huggingface.co/papers/2607.14387

#AutonomousDriving #RAG #ScenarioGeneration #DSL #Benchmark #LLM #SimulationTesting #Chat2Scenic #RetrievalAugmentedGeneration #OpenSource
