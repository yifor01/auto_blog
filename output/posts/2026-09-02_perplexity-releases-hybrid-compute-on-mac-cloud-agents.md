---
title: 'Perplexity Releases Hybrid Compute on Mac: Cloud Agents Orchestrate Down to
  a Local Model, Gated On Device'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/01/perplexity-releases-hybrid-compute-on-mac-cloud-agents-orchestrate-down-to-a-local-model-gated-on-device/
model: claude-code/sonnet
generated_at: '2026-09-02T10:08:32.875265'
score: 93
---

📌 Perplexity 推出 Mac 混合運算：雲端 Agent 遇到隱私資料就自動下放本地模型

TL;DR：Perplexity 讓雲端與本地模型協同完成單一任務，隱私閘門分類器已開源可查。

Agentic 助理有個結構性矛盾：讓它真正好用的那些內容，例如合約文件、機密檔案、客戶資料，恰恰是使用者不能傳到雲端端點的東西。Perplexity 這週在 Mac 上給出了自己的解法。

🤔 **能力與隱私的兩難**

Perplexity Computer 這類 agentic 助理若要處理私密檔案，勢必得在雲端能力與資料外洩風險之間做取捨。Perplexity 的做法不是二選一，而是把單一任務拆成雲端與本地兩段執行，並用一個裝置端隱私閘門決定哪些資料可以跨過邊界。

🧩 **雲端起頭、本地接手的編排方向**

Computer 每個任務都從雲端開始，由前沿模型負責網頁搜尋、規劃與長程推理；一旦某個步驟碰到私密檔案或敏感資料，Computer 會把那個步驟下放給 Mac 上的本地模型執行，過程中不會重啟任務或遺失上下文，最後再把兩段結果合併成單一輸出。這個方向剛好與 Perplexity 一週前在 NVIDIA DGX Spark 上推出的本地運算模式相反，那個模式是從本地硬體開始、經授權後才升級到雲端模型，同一套編排邏輯，預設方向卻完全相反。由於 Computer 也能與 iPhone 搭配，任務可以在手機上遠端觸發，敏感步驟則留在桌上的 Mac 執行，Perplexity 也建議把常駐開機的 Mac mini 當成專用的本地推理節點。

在任何受保護檔案的內容送到雲端之前，一個裝置端分類器會先檢查內容，隱私閘門會套用四種處置之一：保留在本地、遮蔽敏感片段、拒絕該動作，或詢問使用者是否同意。憑證、信用卡卡號、政府核發身分證件會受到最嚴格的處理；被遮蔽的數值會在送出雲端前替換成替代符，等雲端答案回來後再還原。

負責這個閘門的模型叫 PII-Tracer，是一個以 Qwen3 為骨幹改造的 0.6B 雙向編碼器，把原本的因果遮罩換成支援 padding 的雙向 attention，涵蓋 4,096 token 的視窗。一個線性標記頭會輸出 37 個標籤，包含一個「範圍外」標籤，加上九種 PII 類型各自的 BIOES 位置標籤，另外還有一個輔助頭用來預測整段對話是否含有敏感內容。訓練在約 714,000 筆樣本上跑了三個 epoch，推論時則用一個限制式 Viterbi 解碼器來決定最終標籤序列。

📊 **PII-TRACE 基準：找到「大部分」PII 不等於找到「每一次」出現**

配套發布的 PII-TRACE 基準包含 13,148 則合成對話，涵蓋 13 種語言與 10 種書寫系統，共 37,431 個字元層級的識別符提及。在 12 個偵測器的比較中，PII-Tracer 拿下最高的字元 F1（0.629），在 span-overlap 與 span-containment F1 上則排名第二，僅次於 GPT-5.6-sol。一致性表現領先幅度更明顯：對於重複出現的識別符，PII-Tracer 能找到每一次出現的比例達 79.4%，跨輪對話中則是 77.6%，相比之下 GPT-5.6-sol 僅有 57.0% 與 55.1%。在最困難的區間（同一識別符出現 6 到 10 次）中，PII-Tracer 得分 0.691，GPT-5.6-sol 為 0.464，GLiNER2-PII 為 0.073，Claude Opus 4.8 僅有 0.045。

值得注意的是，單一視窗的召回率會隨對話長度下滑，從 1,000 字元以內的 0.975 掉到 10,000 字元以上的 0.687。Perplexity 的解法不是重新訓練，而是調整解碼策略：改用重疊 50% 的滑動視窗後，整體字元召回率從 0.830 提升到 0.965，多次提及的一致偵測率也從 0.794 提升到 0.954，且是在同一個模型權重上達成。

💡 **上線即可用的模型清單**

Perplexity 公告中列出三個上線即可用的本地模型：Gemma 4 E4B、Qwen3.6 35B-A3B，以及一個針對 Computer 專門後訓練過的 Perplexity 模型；產品頁的設定流程則指向一鍵下載的 PPLX Qwen 3.8 27B。Perplexity 的 Hugging Face 組織也提供對應的 pplx-computer-qwen-3-8-27b 模型，以及負責隱私閘門的 pplx-pii-masking-vllm（即 0.6B 的 token 分類模型）。

🎯 **實務啟示**

Hybrid compute 目前對 Pro、Max、Enterprise 訂閱用戶開放，需要搭載 Apple silicon、macOS 15 以上、且統一記憶體至少 24GB（建議 32GB）的 Mac。本地模型可透過 Mac app 一鍵安裝，不需要 Ollama、不需要額外執行環境、也不需要 API key，本地運算不會消耗雲端額度。對 Enterprise 客戶而言，管理員可以設定組織層級規則，指定哪些資料必須留在裝置上、哪些可以遮蔽、哪些需要明確核准，並提供資料離開機器時的稽核紀錄，這一點讓法務、醫療、金融這類高度重視資料邊界的團隊有機會真正導入。

🔗 **來源**
- 標題：Perplexity Releases Hybrid Compute on Mac: Cloud Agents Orchestrate Down to a Local Model, Gated On Device
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/01/perplexity-releases-hybrid-compute-on-mac-cloud-agents-orchestrate-down-to-a-local-model-gated-on-device/

#Perplexity #PrivacyTech #OnDeviceAI #HybridAI #AIAgents #DataPrivacy #EdgeAI #MacOS #LLM #PII
