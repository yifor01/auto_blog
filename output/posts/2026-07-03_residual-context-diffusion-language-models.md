---
title: Residual Context Diffusion Language Models
source: Apple ML
url: https://machinelearning.apple.com/research/residual-context-diffusion
score: 93
model: google/gemma-4-31b-it:free
generated_at: '2026-07-03T19:53:15.197137'
---

📌 【Apple ML 研究】不再浪費計算量：Residual Context Diffusion 讓 Diffusion LLM 效能大幅提升

TL;DR：透過 RCD 模組回收被捨棄的 token 資訊，讓 Diffusion LLM 在 AIME 任務上準確率近乎翻倍。

目前的 Diffusion Large Language Models (dLLMs) 雖然能透過平行解碼多個 token 來挑戰純自迴歸模型的地位，但其核心的「重新遮蓋 (remasking)」機制卻隱藏著巨大的資源浪費：模型僅保留信心最高的 token，其餘的計算結果直接被丟棄。

🤔 **Block-wise dLLM 的計算浪費問題**

在現有的 block-wise dLLMs 中，模型在每一步解碼時會對所有 token 進行預測，但隨後會透過 remasking 機制，僅保留信心值最高的 token 並將其餘部分捨棄。這意味著那些被丟棄的 token 所攜帶的上下文資訊在下一次迭代時完全消失，導致計算資源被浪費。

🧩 **RCD 模組：將捨棄的資訊轉化為「上下文殘差」**

為了解決上述問題，研究團隊提出 Residual Context Diffusion (RCD) 模組。其核心設計理念如下：

- **資訊回收**：將被捨棄的 token 表示 (representations) 轉換為「上下文殘差 (contextual residuals)」。
- **反饋注入**：將這些殘差重新注入到下一次的去噪 (denoising) 步驟中，讓模型能利用先前保留的上下文資訊。
- **兩階段訓練**：為了避開反向傳播 (backpropagation) 帶來的記憶體瓶頸，RCD 採用了解耦的兩階段訓練管線。

📊 **從 AIME 表現看 RCD 的效能增益**

研究團隊在長 CoT 推理 (SDAR) 與短 CoT 指令遵循 (LLaDA) 模型上驗證了此方法，結果顯示：

- **快速轉換**：標準 dLLM 僅需約 10 億 (1 billion) 個 token 即可高效轉換為 RCD 範式。
- **準確率提升**：在多項基準測試中，RCD 使 frontier dLLMs 的準確率提升 5 到 10 個百分點，且額外計算開銷極低。
- **突破性表現**：在最具挑戰性的 AIME 任務中，RCD 的準確率近乎基準線的兩倍，且在相同準確率下，所需的去噪步驟減少了 4 到 5 倍。

🎯 **實務啟示**

對於開發 Diffusion LLM 的工程師而言，這項研究證明了「中間狀態的資訊回收」能顯著降低推論成本。與其單純追求更強的遮蓋策略，將被捨棄的表示轉化為殘差並回饋給模型，可能是提升平行解碼效率、減少去噪迭代次數的有效路徑。

🔗 **來源**
- 標題：Residual Context Diffusion Language Models
- 作者／機構：Yuezhou Hu, Harman Singh, Monishwaran Maheswaran, Haocheng Xi, Coleman Hooper, Jintao Zhang, Aditya Tomar, Michael W. Mahoney, Sewon Min, Mehrdad Farajtabar, Kurt Keutzer, Amir Gholami, Chenfeng Xu @ University of California, Berkeley
- 連結：https://machinelearning.apple.com/research/residual-context-diffusion

#DiffusionLLM #dLLM #AppleML #NaturalLanguageProcessing #RCD #ContextualResiduals #AIME #CoT #ICML #MachineLearning
