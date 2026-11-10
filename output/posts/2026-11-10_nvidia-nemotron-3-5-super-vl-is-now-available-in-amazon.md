---
title: NVIDIA Nemotron 3.5 Super VL is now available in Amazon SageMaker JumpStart
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/nvidia-nemotron-3-5-super-vl-is-now-available-in-amazon-sagemaker-jumpstart/
model: claude-code/sonnet
generated_at: '2026-11-10T00:57:50.955133'
score: 90
---

📌 120B 視覺語言模型上架 SageMaker JumpStart，NVFP4／BF16 任你選

TL;DR：Nemotron 3.5 Super VL 登上 JumpStart，NVFP4 或 BF16 皆可一鍵部署。

當你要同時餵模型看圖片、看影片又要讀文件時，多數 VLM 只能被動接受裁好的小圖；但這次上架 SageMaker 的 NVIDIA Nemotron 3.5 Super VL，把 context window 拉到最多 100 萬 token，還內建推測解碼用的 MTP head，只是 JumpStart 目前還沒把它打開。

🧩 架構：120B MoE 語言骨幹＋C-RADIO 視覺編碼器
Super VL 是 NVIDIA Nemotron 3.5 家族中的 vision-language 模型（VLM），接受 image、video 與 text 輸入，輸出文字。模型把一個 120B 參數、12B active 參數的 hybrid Mixture-of-Experts（MoE）語言骨幹，與一個 C-RADIO 視覺編碼器搭配使用，支援最長 100 萬 token 的 context length，並內建 Multi-Token Prediction（MTP）head，可用於推測解碼（speculative decoding）。使用時可針對每個請求個別設定 reasoning 開關。NVIDIA 表示這個模型是為 document intelligence、GUI 理解（適合 computer-use agent）、video question answering 與多模態 agentic 應用而設計。

JumpStart 提供兩種版本：NVFP4，由 BF16 透過 quantization-aware distillation 量化而來，針對推理最佳化；以及 BF16 全精度參考權重。

📊 量化後精度幾乎不掉
NVIDIA 的 model card 在 reasoning 開啟的設定下，比較了兩個版本在多模態基準上的表現。文中指出，NVFP4（JumpStart 預設版本）在 MMLongBench-Doc 上與 BF16 打平，其他基準差距約在 1 分以內，甚至在 OCRBench v2 與 OSWorld-Verified 上略高於 BF16。完整對比與評測設定請參考 NVIDIA Nemotron 3.5 Super VL and Lightning Technical Report。

實際推理效能方面，AWS 用 generate workload profile（250 input tokens、1,500 output tokens、5 個 concurrent streaming requests）測試：BF16 版本在 ml.p5en.48xlarge 上達到每個請求每秒 140.85 個 output tokens，三種配置下 time to first token 都約 0.5 秒左右。但提示變長後數字會明顯不同：在 summarize profile（10,000 input tokens）下，ml.g7.24xlarge 的 time to first token 拉長到 12.62 秒。由於 NVFP4 與 BF16 跑在不同 GPU 系統與配置上，這些數字並非單純的精度對比。

🧩 部署怎麼選：G7 配 NVFP4，P5en 配 BF16
SageMaker JumpStart 支援的硬體組合是：NVFP4 跑在搭載 NVIDIA RTX PRO 4500 Blackwell Server Edition GPU 的 G7 實例上，BF16 跑在搭載 NVIDIA H200 GPU 的 P5en 實例上。NVFP4 的 JumpStart 預設實例是 ml.g7.24xlarge，是 generate profile 的建議起點；BF16 則用 ml.p5en.48xlarge。部署可以從 SageMaker Studio、SageMaker Python SDK，或直接從 Hugging Face 模型頁面選擇 Deploy → Amazon SageMaker AI 完成。用 SDK 時要留意把 instance type 放進 Compute 參數，因為少了它 SDK 會預設退回 ml.m5.large，導致 build 失敗；部署完成到端點狀態轉為 InService，在 ml.g7.24xlarge 上大約需要 10 分鐘。

inference_config_name 參數用來選擇 serving 設定，每種設定對應不同的 context length：預設的 generate 設定服務 2,275 個 token 的短提示情境，summarize 設定服務 13,650 個 token，modify 設定則服務 15,600 個 token。文章中的 image、video 與 reasoning 範例都需要用到 modify 設定才夠用。

⚠️ 使用限制：圖片輸入與網路隔離
端點以 vLLM-powered chat completions API 對外提供服務，可用熟悉的 chat-message 格式送請求。NVIDIA 建議文字請求用 temperature 1.0、top_p 0.95，圖片與影片請求則用 temperature 0.6、top_p 0.95。由於端點執行在網路隔離環境下，無法抓取外部 URL，所有媒體都必須以 base64 data URL 的形式 inline 送入。模型只接受 image 而非原始 PDF 檔案，要處理 PDF 得先把每一頁都轉成 PNG 之類的圖片格式；一頁 1,536×1,024 的圖片大約佔用 1,536 個 token 的 context，且一個請求只能帶一張圖片。影片輸入建議使用短、經過壓縮的片段，並留意編碼後的 payload 是否超出端點支援的大小限制；若影片請求需要大量 reasoning，記得把 max_tokens 設高一些，同時兼顧回應長度與端點呼叫限制。另外，雖然 checkpoint 內建了 MTP head，但 JumpStart 目前的 serving 設定並未啟用推測解碼。

🎯 實務啟示
如果你的應用場景是文件理解、GUI 操作型 agent 或影片問答，NVFP4 在 G7 實例上提供了接近 BF16 品質但成本更低的選項，適合當作預設起點；需要全精度參考權重時再切到 BF16 與 P5en。實際整合前要先確認：輸入是否都能轉成 base64 inline 的 image／video、PDF 是否已經轉成圖片、以及你的提示長度該對應哪一種 inference_config_name，否則容易因 context 不足或實例設定錯誤而部署失敗。測試結束記得刪除端點、端點設定與模型，避免持續產生費用。

🔗 來源
- 標題：NVIDIA Nemotron 3.5 Super VL is now available in Amazon SageMaker JumpStart
- 作者／機構：Venu Kanamatareddy, AWS ML Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/nvidia-nemotron-3-5-super-vl-is-now-available-in-amazon-sagemaker-jumpstart/

#NVIDIA #Nemotron #VisionLanguageModel #AmazonSageMaker #JumpStart #MoE #MultimodalAI #EdgeInference #NVFP4 #AgenticAI
