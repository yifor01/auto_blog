---
title: 'When One GPU Isn’t Enough: Serving GLM-5.3 Across Two NVIDIA DGX Stations
  with vLLM'
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/
model: claude-code/sonnet
generated_at: '2026-11-13T22:47:57.183194'
score: 98
---

📌 單GPU塞不下753B模型，NVIDIA示範雙DGX Station跨機serving GLM-5.3

TL;DR：當模型大到一張GPU HBM放不下，NVIDIA用兩臺DGX Station透過RDMA以vLLM張量並行，把753B MoE模型serving成一個API端點。

前沿模型的參數規模已經跨過了單機硬體的物理天花板。GLM-5.3 NVFP4量化後的checkpoint仍有約464 GB，比一張GB300 GPU的252 GB HBM3e記憶體還大，這代表就算關掉CPU weight offload也裝不進去。NVIDIA Developer部落格這篇教學示範的作法很直接：別讓模型瘦身，而是把兩臺DGX Station接起來，當成一張「虛擬大GPU」用。

🤔 **MoE模型為什麼不能靠稀疏啟用解套**

GLM-5.3 NVFP4是Z.ai的mixture-of-experts模型，雖然每個token只啟用400億參數（總參數753億），但稀疏啟用只省計算量，省不了記憶體。因為每個token可能被路由到不同的expert，所有權重都得隨時待命在GPU記憶體裡，這也是為什麼MoE模型的記憶體需求往往跟不上參數規模的直覺縮水。

🧩 **跨機張量並行：兩臺機器各算一半，答案從同一個門出去**

作法是用ConnectX-8 RDMA連接兩臺GB300 DGX Station，以vLLM設定TP=2（tensor parallelism），把模型的張量運算拆成兩份，分別交給兩張GB300 GPU。兩臺機器的記憶體仍是獨立的，但運算時彼此協作：Station A擔任rank 0，對外提供唯一的OpenAI相容API；Station B擔任rank 1，只跑worker、不開API。每一筆請求都會同時用到兩臺機器的運算資源，再由Station A把結果回傳給呼叫端。

🧩 **實際動手的七步：從網路校驗到下載整份checkpoint**

教學的前置作業頗為扎實：先用`ibdev2netdev`和`ip -br addr`確認RDMA rail與IPv4位址，再用jumbo frame ping和`timedatectl`驗證連線延遲與時間同步，避免之後NCCL timeout找不到原因。接著兩臺機器都要pull同一個vLLM容器映像檔（`vllm/vllm-openai:v0.30.0-aarch64`），在Station A用`hf download`抓取官方指定版本的GLM-5.3-NVFP4 checkpoint（約1小時於1 Gb/s，10 Gb/s下約6分鐘），再用`rsync`把整份464 GB的權重複製到Station B——兩邊各自保留完整一份,vLLM載入時才會動態切分給各自的GPU。文中強調下載與拷貝完成後要逐一比對檔案清單，確保兩份checkpoint一致。

📊 **後續步驟：推論、壓力測試與SPEED-Bench**

教學後段會啟動推論服務、送出請求、並在併發負載下測量行為，同時用SPEED-Bench（取自需要申請存取權限的`cais/hle`資料集）跑基準測試作為效能基線。這部分屬於後置步驟，文中沒有完整展開細節，但足以說明這套流程的終點是一個可量測、可重現的雙機serving端點。

🎯 **對工程團隊的啟示**

這份教學等於給出一套「模型大於單機記憶體時」的標準參考動作：先驗證硬體與網路，再用張量並行跨機拆權重，而不是急著降精度或犧牲模型完整性。對正在規劃本地部署超大MoE模型的團隊，這是少見的、步驟完整到可以照抄的雙機serving範例。

🔗 **來源**
- 標題：When One GPU Isn't Enough: Serving GLM-5.3 Across Two NVIDIA DGX Stations with vLLM
- 作者／機構：Fatima Fall，NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/

#vLLM #NVIDIA #DGXStation #TensorParallelism #MoE #GLM #LLMInference #RDMA #GPUComputing #LocalDeployment
