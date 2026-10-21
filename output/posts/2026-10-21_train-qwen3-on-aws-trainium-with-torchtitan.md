---
title: Train Qwen3 on AWS Trainium with torchtitan
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/train-qwen3-on-aws-trainium-with-torchtitan/
model: claude-code/sonnet
generated_at: '2026-10-21T21:02:35.011902'
score: 89
---

📌 在 AWS Trainium 上用 torchtitan 訓練 Qwen3：三種路徑實測

TL;DR：同一張 trn2.48xlarge，三種設定跑通 Qwen3，含可複現的 loss 數字。

當你習慣在 NVIDIA GPU 上用 torchtitan 訓練模型，換到 AWS Trainium 需要改多少程式碼？AWS 這篇教學給出的答案是：幾乎不用改——因為 TorchNeuron 把 Trainium 註冊成標準的 PyTorch device，torchtitan 透過原生介面就能直接使用。

🤔 同一套工具，換一顆加速器

torchtitan 在 Trainium 上的用法，和在其他裝置上一樣：裝好 torch_neuronx 後，TorchNeuron 會把 Trainium 註冊為 neuron device，torchtitan 啟動時自動偵測。eager 模式下 Neuron 逐個算子即時編譯；開啟 torch.compile 後，則是編譯捕捉到的計算圖(graph)。整篇教學都在單臺 trn2.48xlarge 上完成，使用 AWS Deep Learning AMI for Neuron 或 Neuron PyTorch 訓練容器，兩者都內建 Neuron 所需的 driver、runtime 與 compiler。

🧩 三種設定，三種整合深度

第一種設定直接用 Transformers v5 當 modeling backend：透過 AutoModelForCausalLM 載入 Hugging Face Hub 上的模型定義，並直接讀寫已發布的 safetensors。設定檔中不特別指定架構欄位，讓 AutoConfig.from_pretrained() 從 Hub 載入架構，再用 torchrun 啟動 64 個訓練行程(對應 64 個 logical NeuronCore)，資料並行(data parallel)切分到全部 64 個 rank。若要微調已發布的權重，只需啟用 checkpoint 載入並指向本地的模型目錄；state-dictionary adapter 會自動處理前綴與 tied embedding，訓練完成後也會存成標準的 Hugging Face safetensors。

第二種設定改用 torchtitan 原生的 Qwen3Model，只需把 config.model_spec 換成 model_registry("4B", attn_backend="sdpa")，選擇原生 Qwen3 實作搭配 scaled dot product attention(SDPA)。因為測試用的 torchtitan 版本沒有現成的 qwen3_4b() config builder，教學是從 qwen3_32b() 出發，再把模型規格換成 4B。

第三種設定更進一步，把 mixture-of-experts(MoE)層換成用 Neuron Kernel Interface(NKI)寫的 kernel。設定上用資料並行切分 64 個 rank，tensor parallel 度數為 1，不使用 expert parallelism；num_experts=64 只是模型裡的專家數量，不等於 expert parallel 的切分度。教學把 Qwen3-30B-A3B 縮減成 4 層、64 個專家以塞進單臺機器，每個 token 路由給 4 個專家(top_k=4)。文中也示範如何用 wrap_nki 把 NKI kernel 包成可被 PyTorch 呼叫的算子、用 nki_op 註冊，再用 register_autograd 搭配前向傳播儲存的路由資訊(routing metadata)接上反向傳播。範例進一步示範如何引入 nkilib 裡的 rope_hf kernel，取代原本的 CosSinRoPE，並透過 torchtitan 的 override 註冊機制(--override.imports)載入自訂的 NKIRoPE。

📊 用 loss 數字驗證權重真的載對了

對 Qwen/Qwen3-4B-Instruct-2507，教學給出一個很實用的驗證技巧：用第一個訓練 step 的 loss 快速檢查權重是否正確載入。從已發布權重啟動的第一步 loss 為 6.54，而從隨機初始化啟動則是 12.43——兩者差距明顯，可以當作快速的 sanity check。訓練結束後，用 AutoModelForCausalLM 搭配 load_state_dict 重新載入匯出的 checkpoint，除了 Qwen3-4B 將 lm_head.weight 與 token embedding 綁定(tied)而缺少的那一個 key 外，不應該出現其他 missing 或 unexpected 的 key，這代表匯出的檔案仍是標準的 Hugging Face checkpoint。

💡 自訂 kernel 的關鍵在於資料佈局與自動微分

文中特別提到，torchtitan 內部的 query/key 張量佈局是 [batch, seq, heads, head_dim]，而 rope_hf 期望的佈局是 [batch, heads, seq, head_dim]，所以自訂算子要在呼叫 kernel 前先轉換佈局，並用 torch.empty_like() 配置輸出張量。反向傳播需要另外註冊一個 backward=True 的算子版本，並把前向傳播算出的 rotary cache 存下來供反向使用（cache 本身不可微分，梯度回傳 None）。

⚠️ 這個範例證明可行，不是效能優化

作者明確說明，這段自訂 kernel 的範例是在示範 kernel 註冊與自動微分整合的流程，而不是效能優化；序列長度需設為 128 * LNC 的倍數（LNC=2 時為 256），rotary cache 也要重塑成 [seq, head_dim * 2] 的形狀。另外，torchtitan 的 Transformers v5 整合與 Trainium 專用的 override 模組會隨版本變動，教學建議照文中版本表釋出的版本固定依賴，才能重現結果。

🎯 實務啟示

如果你的訓練基礎設施已經在往 Trainium 遷移，這篇教學提供了一條漸進路徑：先用 Transformers v5 backend 零改動跑通模型，再切到 torchtitan 原生實作做效能調校，最後才進到 NKI 自訂 kernel。三種設定共用同一套 torchrun 啟動模式與 config 結構，意味著遷移成本主要集中在 kernel 層，而不是整個訓練框架。

🔗 來源
- 標題：Train Qwen3 on AWS Trainium with torchtitan
- 作者／機構：Josh Longenecker, AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/train-qwen3-on-aws-trainium-with-torchtitan/

#AWSTrainium #torchtitan #Qwen3 #PyTorch #NeuronSDK #MoE #LLMTraining #NKI #Transformers #MLInfra
