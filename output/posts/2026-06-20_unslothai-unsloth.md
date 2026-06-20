---
title: unslothai/unsloth
source: GitHub Trending
url: https://github.com/unslothai/unsloth
score: 99
model: google/gemma-4-31b-it:free
generated_at: '2026-06-20T19:36:22.660677'
---

📌 Unsloth Studio：在本機上快速跑、訓練多模態模型的全功能套件

TL;DR：Unsloth Studio 讓 Windows、macOS、Linux 使用者可在本機跑、訓練文字、語音、影像等模型，支援多種格式、LoRA、工具呼叫，且訓練速度最高可達 2 倍、VRAM 用量減少 70%。

🎣 **為什麼現在的開發者都在關注本機模型？**  
隨著大型語言模型 (LLM) 越來越大，雲端 API 成本與延遲成為瓶頸。Unsloth 直接在個人電腦上提供「跑、訓練、部署」全流程，讓研發團隊可以在不依賴雲端的情況下完成實驗與原型開發。

🤔 **核心功能一覽**  
- **跨平台支援**：macOS、Linux（含 WSL）以及 Windows 都能一鍵安裝。  
- **多模態模型支援**：文字、語音、Embedding、視覺模型皆可在同一環境中運行。  
- **模型格式與下載**：內建搜尋、下載、執行 GGUF、LoRA adapters、safetensors 等常見格式。  
- **模型匯出**：支援將模型保存或匯出為 GGUF、16‑bit safetensors 等格式，方便搬移與部署。  
- **工具呼叫與程式碼執行**：提供自我修復的 tool calling、網路搜尋功能，並能在 Claude 產出或沙箱環境中測試程式碼。  
- **API 推理端點**：可將本機 LLM 部署為 API，與 OpenAI、Anthropic 等服務或 vLLM、Ollama 伺服器整合。  
- **自訂聊天模板**：自動設定推理參數，支援圖片、音訊、PDF、DOCX、程式碼等多種輸入。  

🧩 **訓練效能亮點**  
- 宣稱可將 500+ 模型的訓練速度提升至 2 倍，且 VRAM 使用量降低最高 70%，且「無精度損失」。  
- 內建自訂 Triton 與數學 kernel，與 PyTorch、Hugging Face 合作開發。  
- 提供 Data Recipes：自動從 PDF、CSV、DOCX 等檔案產生資料集，並支援視覺化節點式編輯工作流。  
- Reinforcement Learning (RL) 模組被描述為「最有效率的 RL 函式庫」，可直接於本機執行。

⚡ **快速上手**  
- macOS / Linux / WSL：`curl -fsSL https://unsloth.ai/install.sh | sh`  
- Windows：`irm https://unsloth.ai/install.ps1 | iex`  

💡 **實務啟示**  
- **省錢又降低延遲**：開發團隊可在本機跑完整的模型推理與微調，省去雲端 API 的高額費用與網路延遲。  
- **快速迭代**：支援 LoRA、safetensors 等輕量化微調方式，讓模型調整僅需少量顯示卡資源即可完成。  
- **多模態原型**：同一環境即支援文字、聲音、影像等輸入，適合開發跨領域 AI 產品（如聊天機器人＋圖片辨識）。  
- **社群與支援**：提供 Discord、X（Twitter）與 Reddit 社群，方便取得即時支援與範例。  

🔗 來源  
- 標題：unslothai/unsloth  
- 作者／機構：unslothai  
- 連結：https://github.com/unslothai/unsloth  

#Unsloth #LLM #LocalInference #ModelTraining #LoRA #GGUF #safetensors #Triton #RL #MultimodalAI #OpenSource  
