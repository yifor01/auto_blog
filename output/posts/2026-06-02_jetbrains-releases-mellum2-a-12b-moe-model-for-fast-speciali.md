---
title: "JetBrains Releases Mellum2: A 12B MoE Model for Fast, Specialized Tasks in Multi-Model AI Pipelines"
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/02/jetbrains-releases-mellum2-a-12b-moe-model-for-fast-specialized-tasks-in-multi-model-ai-pipelines/
score: 91
model: tencent/hy3-preview:free
generated_at: 2026-06-02T22:01:44.114671
---

📌 **JetBrains 釋出 Mellum2：12B 參數 MoE 模型，專為軟體工程管線設計**  

你以為只有龐大的前沿模型才能勝任代碼生成與除錯？JetBrains 的新作證明，專業化與高效運算可以共存于同一個模型裡。  

🤔 **MoE 架構讓大模型變得更輕盈**  
Mellum2 採用 Mixture‑of‑Experts 設計，總參數達 12B，但在每個 token 上只有 2.5B 參數被激活。具體來說，模型擁有 64 個 experts，每次前向傳遞會呼叫其中的 8 個。這使得單 token 的運算量相當於一個 2.5B 的 dense 模型，同時保留較大的總參數空間以進行專門化學習。  

🧪 **三階段預訓練與延伸的上下文窗口**  
預訓練階段共處理約 10.6T 個 token，資料混合會隨階段逐漸從多樣化網頁內容轉向經過篩選的程式碼與數學內容。訓練使用 Muon 優化器、FP8 混合精度以及 Warmup‑Hold‑Decay 學習率排程（線性衰減至零）。預訓練完成後，團隊採用層選擇式 YaRN 方法將基礎模型的上下文視窗擴展至 128K token，為後續的後訓練奠定基礎。  

📈 **後訓練流程與 Instruct 版本的特色**  
後訓練分為兩階段：首先進行監督式微調（SFT），接著在可驗證回報的強化學習（RLVR）階段，涵蓋數學、可執行程式碼、工具使用、指令遵循、推理與知識等任務。得到的 Instruct 版本能直接給出答案，不需要外部鏈式思考，適合低延遲的場景，例如直接回答、工具呼叫與指令執行。  

🔍 **模型的定位與適用範圍**  
JetBrains 團隊將 Mellum2 描述為「焦點模型」（focal model）：它不是要取代前沿的通用大模型，而是作為更大型 AI 管線中的快速、專業化組件。模型同時處理自然語言與程式碼，但目前不支援多模態（無圖像或影像輸入）。  

⚠️ **已知的限制**  
- 模型僅針對文字與程式碼設計，不具備圖像、影片等多模態能力。  
- 文件中未提供基準測試結果或與其他模型的直接比較。  
- 開源版本遵循 Apache 2.0 授權，但未提及是否包含訓練資料或完整的訓練腳本。  

🎯 **對開發者的實務建議**  
若您的工作流程已經深度依賴 JetBrains 產品（如 IntelliJ、Rider），Mellum2 提供一個可直接下載、在 Apache 2.0 下使用的 12B MoE 模型，適合作為代碼生成、編輯、除錯、工具使用或 Agentic 程式設計的低延遲組件。在將其納入現有管線前，建議先在您的特定任務上進行驗證，以確認其激活參數數量與延遲特性符合實際需求。  

🔗 **論文連結**  
📝 JetBrains Releases Mellum2: A 12B MoE Model for Fast, Specialized Tasks in Multi-Model AI Pipelines  
👤 Asif Razzaq (MarkTechPost 報導)  
🔗 https://www.marktechpost.com/2026/06/02/jetbrains-releases-mellum2-a-12b-moe-model-for-fast-specialized-tasks-in-multi-model-ai-pipelines/  

你會考慮在自己的開發管線中嵌入這種專業化的 MoE 模型嗎？歡迎在留言區分享你的想法與經驗 👇  

#AI #MachineLearning #MoE #JetBrains #Mellum2 #CodeGeneration #LLM #開源 #軟體工程
