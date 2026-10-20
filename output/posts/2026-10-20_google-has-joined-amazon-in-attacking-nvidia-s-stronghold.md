---
title: Google has joined Amazon in attacking Nvidia’s stronghold with AI app developers
source: TechCrunch AI
url: https://techcrunch.com/2026/10/20/google-has-joined-amazon-in-attacking-nvidias-stronghold-with-ai-app-developers/
model: claude-code/sonnet
generated_at: '2026-10-20T20:52:57.077031'
score: 91
---

📌 Google 加入 Amazon，PyTorch 正在鬆動 Nvidia 的預設地位

TL;DR：Google 開源 TorchTPU，跟進 Amazon TorchNeuron，讓 PyTorch 應用免改碼就能跑上非 Nvidia 晶片。

多數 AI 應用在寫程式碼的那一刻，就已經預設只能跑在 Nvidia 的 GPU 上。這週，Google 和 Amazon 相繼出手，試圖打破這個「預設」。

🤔 PyTorch 為何幾乎等於 Nvidia

PyTorch 是 AI 開發者用來建構、訓練與執行模型最流行的開源工具，據報導，約有 85% 的 AI 應用使用它。PyTorch 最早由 Meta（當時是 Facebook）於 2016 年開發，那時 LLM 尚未改變世界，而 Nvidia 的 GPU 早已是 AI 研究的標準硬體，因此 PyTorch 的許多功能原生就是為 Nvidia 晶片打造的。2022 年，Meta 把 PyTorch 交棒給非營利組織 Linux Foundation 管理。

🧩 Google 的 TorchTPU 與 Amazon 的 TorchNeuron

本週二，Google 宣布旗下醞釀已久的 PyTorch 版本 TorchTPU 正式開源，讓 AI 應用能跑在自家的 AI 晶片 Tensor Processing Units（TPU）上。報導指出，開發者只需做簡單的設定變更，不需要重寫應用程式碼，就能把現有的 PyTorch 應用搬到 TPU，進而搬上 Google Cloud。

這跟進的是 Amazon 週一的動作：Amazon 發布自己的 PyTorch 版本 TorchNeuron，讓 AI 應用同樣免改碼搬到自家 AI 晶片 Trainium 與 AWS 上。Amazon 更進一步，向 PyTorch 主專案提交程式碼，把多項原本綁定 Nvidia 晶片的功能解耦，讓專案預設就對任何硬體更開放。

💡 Google 這次多做了什麼

報導提到，Google 在幾個地方可能更勝一籌：它表示已直接與 Meta、Hugging Face，以及 vLLM 開發商 Inferact、SGLang 開發商 RadixArk 等合作，確保 TorchTPU 的功能與程式庫能像原生 PyTorch 一樣，順暢搭配這些主流 AI 開發工具。Google 另外推出專屬的 TPU agent suite，協助開發者把應用搬到自家晶片與雲端的過程中排查、修正錯誤；同時更新了讓 AI 跑在手機、筆電與嵌入式裝置上的 LiteRT 工具，使其更好地配合 PyTorch 應用。

⚠️ 不代表開發者會立刻出走

報導也提醒，即便現在能更輕鬆地把應用搬到替代晶片與雲端，並不意味 AI 應用開發者會因此大舉拋棄 Nvidia 硬體。但 Amazon 與 Google 顯然都在持續削弱 Nvidia 在這個生態中的既有優勢。

🎯 對工程師的實務影響

如果你的 AI 應用是用 PyTorch 開發，現在理論上多了「免改碼」就能測試 TPU 或 Trainium 的選項，值得在新專案或成本優化時納入評估；但在正式遷移前，仍應實測效能、相容性與工具鏈（如 vLLM、SGLang）在非 Nvidia 硬體上的實際表現，而不是只看「可以搬」就直接決定搬。

🔗 來源
- 標題：Google has joined Amazon in attacking Nvidia's stronghold with AI app developers
- 作者／機構：Julie Bort（TechCrunch AI）
- 連結：https://techcrunch.com/2026/10/20/google-has-joined-amazon-in-attacking-nvidias-stronghold-with-ai-app-developers/

#PyTorch #TPU #Nvidia #Trainium #GoogleCloud #AWS #AIInfrastructure #MachineLearning #CloudComputing #OpenSource
