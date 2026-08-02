---
title: Welcome Inkling by Thinking Machines
source: HuggingFace Blog
url: https://huggingface.co/blog/thinkingmachines-inkling
score: 122
model: tencent/hy3:free
generated_at: '2026-07-16T08:08:52.285354'
---

📌 【HuggingFace 報導】Thinking Machines 開源 Inkling：近 1T 參數原生多模態模型

TL;DR：Inkling 是首個約 1T 參數、1M 上下文且原生支援影像／文字／音訊的開放模型。

當多數開放權重模型還在拚單一模態或千億參數規模，Thinking Machines 直接把一個約 1T 參數、能吃掉影像／文字／音訊、還帶 1M 上下文的模型扔上 Hugging Face。

🤔 **什麼是 Inkling？**

Inkling 是 Thinking Machines 釋出的大型開放模型，總參數約 1T（975B total / 41B active），原生接受影像、文字與音訊輸入。HuggingFace 部落格指出，它是第一個具備約 1T 參數與 1M 上下文視窗、能原生接收這三類輸入的開放模型，並在 45 trillion tokens 的 text、images、audio、video 資料上訓練。

🧩 **Decoder-only 多模態 MoE 架構**

README／部落格說明其架構設計如下：

- Decoder-only：採用因果自回歸生成，與多數現代 LLM 相同。
- Multimodal：可 ingest 文字、音訊與影像。
- Mixture-of-Experts (MoE)：每層的 feed forward network 為稀疏結構，任一時刻僅 41B 參數活化，共有 256 個 experts，推論更快。
- Relative attention：部落格提到 Inkling 使用 relative attention 而非常見的 RoPE 來注入位置資訊，但摘要在此處截斷，細節未明。

💡 **推論與生態系支援亮點**

- 提供完整 BF16 權重，以及校準過的 NVFP4 變體。
- 包含 speculative MTP layers 以加速推論。
- 具備 agentic capabilities，並針對 fine-tuning 做領域適配（domain adaptation）。
- Day-0 支援 transformers、SGLang 與 llama.cpp，方便直接上手。

🎯 **實務啟示**

對想打造跨模態推理應用的工程師，Inkling 的開放權重與原生多模態設計，意味著可用單一模型處理影像／音訊／文字聯合推理，並透過 fine-tuning 做領域落地；1M 上下文也降低長檔案或多輪多模態對話的切分成本。

🔗 **來源**
- 標題：Welcome Inkling by Thinking Machines
- 作者／機構：HuggingFace（ben burtenshaw、merve、Pedro Cuenca、Aritra Roy Gosthipaty）
- 連結：https://huggingface.co/blog/thinkingmachines-inkling

#Inkling #ThinkingMachines #Multimodal #LLM #MixtureOfExperts #OpenModel #HuggingFace #LongContext #AgenticAI #FineTuning
