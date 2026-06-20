---
title: 'VibeThinker-3B: A 3B Dense Reasoning Model Built on Qwen2.5-Coder-3B With
  the Spectrum-to-Signal Post-Training Pipeline'
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/19/vibethinker-3b-a-3b-dense-reasoning-model-built-on-qwen2-5-coder-3b-with-the-spectrum-to-signal-post-training-pipeline/
score: 96
model: google/gemma-4-31b-it:free
generated_at: '2026-06-20T19:37:34.051687'
---

📌 【Sina Weibo】VibeThinker-3B：用 3B 參數挑戰 1T 規模的推理效能

TL;DR：基於 Qwen2.5-Coder-3B，透過 SSP 訓練管線在數學與程式碼等可驗證任務上對標超大型模型。

大多數 AI 推理的突破往往依賴於「規模法則」，投入數千億個參數來跨越認知門檻。然而，來自 Sina Weibo Inc 的 VibeThinker-3B 嘗試走一條完全不同的路：證明小型稠密模型（Dense Model）也能在特定領域展現出遠超其體量的推理能力。

🤔 **專攻可驗證任務，而非通用知識**

VibeThinker-3B 並非追求全能的通用模型，而是一個設計精良的「專家」。它專注於那些答案可被驗證（Verifier）確認的任務，如數學、程式碼與 STEM 學科。對於開放域的知識查詢任務，研究團隊建議使用更大規模的通用模型。

🧩 **Spectrum-to-Signal (SSP) 後訓練管線**

VibeThinker-3B 並非從零開始預訓練，而是基於 Qwen2.5-Coder-3B 進行後訓練（Post-training），其核心技術在於延續 VibeThinker-1.5B 的 Spectrum-to-Signal Principle (SSP) 框架：

1. **SFT (Supervised Fine-Tuning)**：建立一個包含大量有效推理路徑的廣泛空間，定義為「光譜 (Spectrum)」。
2. **RL (Reinforcement Learning)**：透過強化學習放大其中正確的路徑，將其轉化為「訊號 (Signal)」。
3. **自我蒸餾 (Self-distillation)**：進一步優化模型推理能力。

📊 **3B 規模對標 671B 與 1T 模型**

在多項可驗證基準測試中，VibeThinker-3B 展現出極高的效率。值得注意的是，其 AIME26 分數甚至能與參數規模大數百倍的模型相媲美：

| 基準測試 (Benchmark) | VibeThinker-3B 分數 | 對比對象/備註 |
| :--- | :--- | :--- |
| **AIME26** | 94.3 | 相當於 DeepSeek V3.2 (671B) 與 Kimi K2.5 (1T) |
| **LiveCodeBench v6** | 80.2 (Pass@1) | 程式碼生成能力 |
| **IMO-AnswerBench** | 76.4 | 400 題 IMO 等級題目集 |
| **BruMO25** | 93.8 | 推理能力測試 |
| **HMMT25** | 89.3 | 推理能力測試 |
| **OJBench** | 38.6 | 低於最大規模模型 |

此外，研究提到使用「+CLR」（Claim-Level Reliability Assessment）的測試時擴展（Test-time scaling）可以進一步影響結果。

🎯 **實務啟示：低門檻部署的高效推理**

對於工程師而言，VibeThinker-3B 的最大價值在於「極低部署成本」與「高專精效能」的平衡。BF16 權重僅約 6 GB，單張 GPU 即可運行。若需要追求更快的推理速度，建議搭配 vLLM 或 SGLang。

**部署環境建議：**
- 基礎依賴：`transformers >= 4.54.0`
- 加速框架：`vLLM == 0.10.1` 或 `SGLang >= 0.4.9.post6`

🔗 **來源**
- 標題：VibeThinker-3B: A 3B Dense Reasoning Model Built on Qwen2.5-Coder-3B With the Spectrum-to-Signal Post-Training Pipeline
- 作者／機構：Asif Razzaq / Sina Weibo Inc
- 連結：https://www.marktechpost.com/2026/06/19/vibethinker-3b-a-3b-dense-reasoning-model-built-on-qwen2-5-coder-3b-with-the-spectrum-to-signal-post-training-pipeline/

#AI #LLM #Reasoning #Qwen #SinaWeibo #OpenSource #STEM #Mathematics #Coding #MachineLearning
