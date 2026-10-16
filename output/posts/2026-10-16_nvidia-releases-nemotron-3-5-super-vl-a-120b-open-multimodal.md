---
title: NVIDIA Releases Nemotron 3.5 Super VL, a 120B Open Multimodal Agent Model
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/15/nvidia-nemotron-3-5-super-vl-release/
model: claude-code/sonnet
generated_at: '2026-10-16T20:09:57.606710'
score: 114
---

📌 【NVIDIA 最新釋出】Nemotron 3.5 Super VL：一個 checkpoint 扛起文字、影像與 Agent

TL;DR：NVIDIA 開源 1200 億參數多模態 MoE 模型,單一 checkpoint 同時處理文字、影像、影片與工具呼叫,免除企業維護雙模型的麻煩。

過去要做一個「永遠在線」的企業 agent,得同時維護一個文字模型和一個視覺模型,串接起來還得處理介面不一致的問題。NVIDIA 這次直接把答案寫進模型架構裡:一個開源 checkpoint,讀文字、圖片、文件、影片,然後推理、呼叫工具、寫程式碼,一次到位。

🤔 **為什麼企業需要「單一模型」**

Nemotron 3.5 Super VL 是一個 1200 億參數的 Mixture-of-Experts(MoE)模型,每個 token 只啟動 120 億參數。對開發者而言,這代表原本要分開部署的文字模型與視覺模型,現在可以用同一份開源權重取代。

🧩 **Mamba-2、MoE、Attention 交錯的混合架構**

模型骨幹交錯疊放 Mamba-2、MoE 與 attention 層,每個 MoE 層內有 512 個 routed experts。視覺輸入則靠一個 C-RADIO 視覺編碼器搭配 connector,把圖片、文件頁面與影片幀餵進語言骨幹。影片輸入限制在 2 分鐘以內的 MP4 片段,推理模式可透過 chat template 開關切換。

這個模型是從 Nemotron 3 Ultra 蒸餾而來。NVIDIA 團隊表示訓練用了約 26 兆 tokens,後訓練階段用了約 380 萬筆樣本,並在數十個環境中進行強化學習;持續預訓練階段又加入了 100 億 Indic tokens。

📊 **參數少了 4.6 倍,分數反而更高**

在 agent harness 評測中,Super VL 的表現超越參數量約為其 4.6 倍的 Nemotron 3 Ultra:Hermes Bench 拿下 63.44% 對比 Ultra 的 56.33%,LangChain evals 則是 87.05% 對比 84.3%。

速度方面,NVIDIA 透過 Baseten 端點在 Artificial Analysis 的 agentic 任務測試中,回報每秒超過 600 個輸出 token,圖表顯示比「Inkling Small」快上 5 倍。在 16 張 B200 GPU、每使用者每秒 50 token 的條件下,NVIDIA 宣稱能多服務 8 倍使用者,首個 token 延遲則下降 85%。這些分數皆為 NVIDIA 自行回報,不同廠商的 harness 與 benchmark 版本不一,幾分之差應謹慎看待。

💡 **邊緣端也有對應版本**

NVIDIA 同步推出兩個邊緣模型:Nemotron 3.5 Bolt 74B-A9B 與 Bolt E4B,同屬開源多模態 agent 模型家族。Bolt 74B-A9B 鎖定本地端 agent 應用,發布說明指出它是從 Super VL 蒸餾而來,原生 2-bit 量化後可塞進 RTX 與 DGX Spark 系統的 24GB 記憶體。NVIDIA 表示它在 PinchBench 上於同級開源模型中排名第一,在 BrowseComp 上排名第二。Bolt E4B 僅 4GB,鎖定語音助理與嵌入式 agent,預計 10 月 23 日於 GeForce RTX、Jetson 與 RTX/DGX Spark 平臺上線。

權重以 OpenMDW-1.1 授權釋出,NVIDIA 同時開源了資料集、訓練配方與 NeMo Gym 中的 RL 環境。模型可在 Hugging Face、OpenRouter、ModelScope 取得,也可用 NVIDIA NIM 部署,支援 vLLM、SGLang、TensorRT-LLM(Blackwell 與 Hopper)、llama.cpp 與 Unsloth。正式環境可搭配 Dynamo recipes 做 KV-aware routing;客製化則透過 NeMo AutoModel(SFT、LoRA)與 NeMo RL 進行。

⚠️ **分數比較需要保留懷疑**

所有評測分數皆為 NVIDIA 自行回報,且來自 NVFP4 checkpoint,不同 harness 與版本差異可能影響比較結果。

🎯 **實務啟示**

如果你的團隊正維護一套「文字模型 + 視覺模型」的拼接架構,Super VL 提供了單一 checkpoint 的替代路線;而 Bolt 系列則讓本地端、低記憶體的 agent 部署變得可行,值得評估是否能簡化現有的多模型 pipeline。

🔗 **來源**
- 標題:NVIDIA Releases Nemotron 3.5 Super VL, a 120B Open Multimodal Agent Model
- 作者／機構:Asif Razzaq,MarkTechPost
- 連結:https://www.marktechpost.com/2026/10/15/nvidia-nemotron-3-5-super-vl-release/

#NVIDIA #Nemotron #OpenSource #MultimodalAI #MixtureOfExperts #AIAgent #Mamba2 #LLM #EdgeAI #VisionLanguageModel
