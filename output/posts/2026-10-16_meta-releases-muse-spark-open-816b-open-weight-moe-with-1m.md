---
title: 'Meta Releases Muse Spark Open: 816B Open-Weight MoE With 1M Context'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/15/meta-muse-spark-open-816b-open-weight-model/
model: claude-code/sonnet
generated_at: '2026-10-16T20:09:57.606919'
score: 108
---

📌 【Meta 最新開源】816B 的 Muse Spark,兩臺 Mac Studio 就能跑

TL;DR:Meta 釋出 816B 參數開源多模態 MoE 模型,支援文字/影像/影片/音訊輸入與 1M context,量化後可在兩臺 Mac Studio 運行。

816B 參數的模型通常意味著需要一整個資料中心才能服務,但 Meta 這次把量化版本的部署門檻壓到了兩臺 Apple M5 Ultra Mac Studio——這對「開源旗艦模型」的想像是個不小的轉變。

🤔 **Meta 的開源旗艦**

Meta Superintelligence Labs 釋出了 Muse Spark Open,是其 Muse Spark 模型的開源權重版本。Meta 團隊稱其為目前最強的美國開源權重模型。這是一個原生多模態的 MoE 模型,鎖定程式碼與長流程 agentic 工作,輸入涵蓋文字、影像、影片與音訊,輸出為文字,context window 達 1M tokens。

🧩 **816B 總參數、42B 啟動的架構**

模型卡列出 62 層、hidden dimension 為 8,192。每個 MoE 層有 256 個專家,top-k 路由每個 token 啟動 8 個。Attention 採分組查詢注意力,128 個 query head 對 16 個 KV head。視覺輸入由獨立的 18 億參數 Perception Encoder 處理。詞彙表達 202,048 個 token,訓練資料涵蓋超過 100 種語言。推理深度可透過 reasoning_effort 參數設定為 low、medium、high 或 xhigh,預設為 xhigh。開源版本額外做了安全後訓練,Meta 團隊表示這讓模型在沒有系統層級防護機制的情況下也更穩健。

📊 **美國最強,但編碼仍落後中國開源模型**

Meta 在最高推理強度下,將 Muse Spark Open 與 Kimi K3、GLM 5.3、Qwen3.8-2.4T-A95B 等模型比較。編碼是它的弱項:在 Terminal-Bench 2.1(搭配 Terminus 2 harness)上拿下 76.4 分,落後 Kimi K3 的 85.0、GLM 5.3 的 83.9 與 Qwen3.8 的 82.0。在 Artificial Analysis Intelligence Index 上,Muse Spark Open 得分 39,同樣落後 GLM 5.3(45)、Kimi K3(44)與 Qwen3.8(40)。換句話說,「最強美國開源模型」的說法站得住腳,但中國開源模型在整體能力上仍然領先。部分對手分數為自行回報,評測方法論有列出各數據來源。

💡 **量化讓 816B 變得可部署**

根據 Meta 的開發者指南,BF16 權重約 1.6TB,NVFP4 只量化專家部分,壓到約 530GB。模型卡建議 NVFP4 至少需要 700GB VRAM,BF16 則需要 2TB。Day-one 支援引擎包括 SGLang、vLLM、TensorRT-LLM、Hugging Face Transformers、MLX、llama.cpp 與 Unsloth。Hosted API 已在 Baseten、Fireworks AI、Groq、Modal、Nebius、OpenRouter、Together AI 上線,OpenRouter 標價為每百萬輸入 token 1.25 美元、每百萬輸出 token 4.25 美元。

兩個 draft 模型用於加速解碼:DFlash V2 搭配 SGLang,DSpark 搭配 vLLM。Meta 回報在 AMD MI355X 上,DFlash V2 帶來 3.7 倍的單請求吞吐量提升。微調方面支援 TorchTitan、Hugging Face TRL 與 NVIDIA NeMo AutoModel。授權採用 Muse Model License,允許使用、微調、蒸餾與重新散布;其中內部使用、研究用途以及用於自家產品功能皆豁免於營收條款之外。

⚠️ **編碼能力是明顯短板**

雖然整體 Intelligence Index 與多數評測上標榜「最強美國開源」,但在編碼這個對 agentic 工作極為關鍵的面向上,Muse Spark Open 明顯落後 Kimi K3、GLM 5.3 與 Qwen3.8,且部分對手分數屬自行回報,需謹慎解讀跨廠商比較。

🎯 **實務啟示**

如果你的場景需要處理音訊、影片等多模態輸入並要求長 context,Muse Spark Open 的 1M context 與原生多模態能力值得評估;但若核心需求是程式碼生成與 agentic coding,目前的評測顯示它不是這個面向的最佳選擇。NVFP4 把 816B 模型壓到兩臺 Mac Studio 可跑的規模,也為本地高階部署開了一條新路。

🔗 **來源**
- 標題:Meta Releases Muse Spark Open: 816B Open-Weight MoE With 1M Context
- 作者／機構:Asif Razzaq,MarkTechPost
- 連結:https://www.marktechpost.com/2026/10/15/meta-muse-spark-open-816b-open-weight-model/

#Meta #MuseSpark #OpenWeightLLM #MixtureOfExperts #Multimodal #LongContext #AgenticAI #NVFP4 #OpenSource #AIInfrastructure
