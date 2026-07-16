---
title: Tracing Agentic Failure from the Flow of Success
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.12747
score: 109
model: tencent/hy3:free
generated_at: '2026-07-16T08:09:23.301266'
---

📌 【HuggingFace Daily Papers】只用成功軌跡，就能找出 Agent 在哪一步失敗？

TL;DR：OAT 僅用成功軌跡做無監督失敗歸因，比提示法快 200–5000 倍且 F1 更高。

當 LLM-based agentic 系統在任務中失敗，要定位「到底是哪一步出錯」往往耗時又燒錢。現有方法不是靠昂貴的 prompting 管線，就是得收集帶步驟級錯誤標註的失敗資料——而這類資料既難收又難擴充套件。

🤔 **現有失敗歸因方法的三大痛點**

Failure attribution（失敗歸因）旨在從失敗軌跡中找出導致任務失敗的步驟，對除錯與改進 agentic 系統至關重要。但既有的兩類做法都有明顯限制：
- Prompting-based 管線：運算成本高。
- 基於失敗軌跡做 post-training 的方法：需要步驟級錯誤標註，收整合本昂貴且難以規模化。

作者主張，一個實用的失敗歸因模型應該要輕量、且不必依賴失敗資料的步驟級監督就能訓練。

🧩 **OAT：把成功軌跡當成一類學習問題**

這篇論文提出 OAT，處理的是 unsupervised failure attribution——只用在成功軌跡上訓練，推論時給定一條失敗軌跡，就能標出錯誤步驟。

OAT 將此問題形式化為 one-class learning（一類學習），並採用 neural controlled differential equations（神經控制微分方程）來建模成功軌跡在 latent space 中的動態模式。

推論流程可描述為：
- 輸入：一條失敗軌跡（步驟序列）。
- 每一步計算 anomaly score：依據該步偏離「從成功軌跡學到的動態」的程度。
- 彙整 anomaly score → 產出一組被判定為錯誤的步驟（error steps）。

📊 **僅 100 條成功軌跡訓練，速度與準確率雙贏**

實驗設定上，OAT 僅使用 100 條成功軌跡進行訓練。結果顯示：
- 速度：比 prompting-based baseline 快 200–5000 倍。
- 準確率：在 in-domain 與 out-of-distribution（OOD）資料集上，F1 分數分別提升 +20% 與 +7%，且一致優於 baseline。

| 比較專案 | OAT | Prompting-based baseline |
| --- | --- | --- |
| 訓練資料 | 僅 100 條成功軌跡 | 未提及 |
| 推論速度 | 快 200–5000 倍 | 基準 |
| In-domain F1 | +20% 優於 baseline | 基準 |
| OOD F1 | +7% 優於 baseline | 基準 |

🎯 **輕量歸因可成為 Agent 除錯標配**

對工程師而言，OAT 展示了一條務實路線：不需要大規模標註失敗案例，也能建立高效的失敗診斷機制。在 agentic 系統上線後，用少量成功紀錄訓練歸因模型，就有機會在低運算開銷下持續定位失敗步驟。

🔗 **來源**
- 標題：Tracing Agentic Failure from the Flow of Success
- 連結：https://huggingface.co/papers/2607.12747

#LLM #AgenticSystems #FailureAttribution #OneClassLearning #NeuralCDE #OAT #AnomalyDetection #Debugging #HuggingFacePapers #UnsupervisedLearning
