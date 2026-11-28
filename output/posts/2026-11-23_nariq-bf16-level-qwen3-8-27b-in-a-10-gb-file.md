---
title: 'NariQ: BF16-level Qwen3.8-27B in a 10 GB file'
source: Hacker News
url: https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF
model: gpt-6.1-terra
generated_at: '2026-11-28T05:50:19.410919'
score: 90
---

📌 NariQ：10 GB 逼近 BF16 表現

TL;DR：NariQ 以低位元量化縮小模型，部分測試表現接近 BF16。

🎣 **模型縮小後，效能一定大幅下降嗎？**

NariQ 的作者表示，Qwen3.8-27B 經過 3-bit 以下量化後，在代理式任務、數學、多語言推理和影像理解上，仍能保有接近 BF16 的品質。原文標題也指出，模型可放入 10 GB 檔案。

但量化位元數降得越低，結果並不一致：3-bit 在列出的測試中接近 BF16，2-bit 的部分成績則明顯下滑。

🧩 **3-bit 量化瞄準 BF16 等級品質**

NariQ 提供 Qwen3.8-27B 的 3-bit、2.5-bit 和 2-bit 量化（quantization）版本，目標是在縮小模型的同時保留品質。

作者宣稱，據其所知，這是首個在長時程代理式任務（long-horizon agentic tasks）上維持 BF16 等級表現的 3-bit 以下量化方案。不過，現有素材沒有說明量化方法的具體設計。

📊 **3-bit 成績接近 BF16，2-bit 在部分任務下滑**

作者提供的基準測試如下：

| 基準測試 | BF16 | 3-bit | 2.5-bit | 2-bit |
|---|---:|---:|---:|---:|
| DeepSWE | 39.8 | 41.0 | 41.9 | 28.6 |
| Terminal-Bench 2.1 | 62.6 | 63.8 | 60.2 | 52.4 |
| AIME 25+26 | 97.7 | 98.3 | 96.5 | 86.0 |
| MSGM | 94.0 | 93.1 | 91.8 | 90.6 |
| RealWorldQA | 82.4 | 82.4 | 81.3 | 80.9 |

3-bit 在五項測試中都接近 BF16，部分數值甚至更高。相較之下，2-bit 的 DeepSWE 和 Terminal-Bench 2.1 成績下降較明顯；RealWorldQA 則從 BF16 的 82.4 降至 80.9。

📊 **不同上下文長度的解碼結果**

作者表示，在 RTX PRO 6000 上，NariQ 的解碼速度與其他量化版本相近，並提供以下不同上下文長度的結果：

| 上下文長度 | 3-bit | 2.5-bit | 2-bit | Unsloth UD-IQ3_XXS |
|---|---:|---:|---:|---:|
| 4K | 88.9 | 99.2 | 111.7 | 94.7 |
| 16K | 84.5 | 93.8 | 105.1 | 89.8 |
| 64K | 70.7 | 77.5 | 85.0 | 74.8 |

素材未標明這組數值的單位，因此不宜進一步換算或推論實際吞吐量。

⚠️ **目前需要專用 llama.cpp 分支**

作者指出，執行這些量化版本目前需要他們的 llama.cpp 分支（fork）。素材未提供安裝步驟、量化方法細節或完整評測設定，因此上述結果仍應以自身工作負載驗證。

🎯 **先比較品質，再確認執行環境**

對考慮低位元量化的工程師而言，3-bit 的結果提供了一個值得測試的選項；若要使用更低位元版本，應特別留意不同任務的品質差異。同時，導入前需確認是否能使用作者提供的 llama.cpp 分支。

🔗 **來源**
- 標題：NariQ: BF16-level Qwen3.8-27B in a 10 GB file
- 作者／機構：toebee
- 連結：https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF

#NariQ #Quantization #LLM #BF16 #Qwen #GGUF #AgenticAI #MultilingualAI #ImageUnderstanding #Inference
