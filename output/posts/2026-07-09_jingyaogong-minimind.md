---
title: jingyaogong/minimind
source: GitHub Trending
url: https://github.com/jingyaogong/minimind
score: 106
model: google/gemma-4-31b-it:free
generated_at: '2026-07-09T09:51:42.558389'
---

📌 MiniMind：只用 3 塊錢與 2 小時即可在個人 GPU 上訓練 64M 超小語言模型  

TL;DR：MiniMind 以 64M 參數、約 GPT‑3 1/2700 體積的模型，於單張 NVIDIA 3090 上完成 1 epoch SFT 只需 2 小時，成本低於 3 塊錢，全部程式碼從零用 PyTorch 實作，提供完整 LLM 訓練鏈路與多模態擴展。  

🎣 你是否曾因模型太大、資源太貴而只能在「推理」階段玩玩？MiniMind 把整個 LLM 從資料清洗、預訓練、微調到 RLHF 全流程，以極簡、低成本的方式公開，讓每個人都能在自己的 GPU 上親手打造一個可執行的語言模型。  

🧩 **從 0 開始的完整 LLM 教程**  
- 專案以 PyTorch 原生 API 撰寫，沒有依賴 transformers、peft 等高階抽象，所有核心演算法（MoE、LoRA、DPO、PPO/GRPO/CISPO、Tool Use、Agentic RL、模型蒸餾）均從頭實作。  
- 完整訓練鏈路涵蓋：  
  1. 資料清洗與 Tokenizer 訓練  
  2. 預訓練（Pretrain）  
  3. 監督微調（SFT）  
  4. LoRA 微調  
  5. RLHF（DPO）與 RLAIF（PPO/GRPO/CISPO）  
  6. Tool Use、Agentic RL、適應性思考等進階應用  

📊 **模型規模與效能**  
- MiniMind 主線最小版本參數量約 64M，體積僅為 GPT‑3 的 1/2700。  
- 在單張 NVIDIA 3090 上完成 SFT 階段 1 epoch 的實測耗時 2 小時，對應的 GPU 租用成本不到 3 塊錢（依當時市場價格計算）。  

💡 **多模態與衍生模型**  
- 除了 MiniMind‑LLM，專案還提供：  
  - MiniMind‑V：視覺模態模型  
  - MiniMind‑O：多模態 Omni 模型  
  - MiniMind‑dLM：結合擴散的語言模型  
  - MiniMind‑Linear：線性模型  
- 相關說明與討論可在專案的 Discussion 區檢視。  

⚠️ **限制與適用物件**  
- 目標是「普通個人 GPU」的可訓練與可復現，模型規模極小，適合作為 LLM 入門與教學示範；若需商業級或大規模應用，仍須考慮更大型的模型與資源。  
- 所有程式碼皆以 Apache 2.0 授權釋出，免費使用，但僅提供訓練與基礎推理流程，未包含商業化支援。  

🎯 **實務啟示**  
- 想要快速驗證 LLM 訓練流程或教學時，可直接克隆此專案，在本地 GPU 上跑完整的 Pretrain → SFT → RLHF 迴路，省去購買雲端大模型的高額成本。  
- 由於使用純 PyTorch 實作，開發者可以輕鬆讀取每個模組的實作細節，作為自行設計新演算法或改寫現有流程的參考基礎。  

🔗 來源  
- 標題：jingyaogong/minimind  
- 作者／機構：jingyaogong  
- 連結：https://github.com/jingyaogong/minimind  

#MiniMind #LLM #PyTorch #OpenSource #LowCostAI #ModelTraining #MoE #LoRA #RLHF #Multimodal #AIEducation #Apache2.0
