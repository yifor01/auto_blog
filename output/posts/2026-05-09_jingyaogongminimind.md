---
title: "jingyaogong/minimind"
source: GitHub Trending
url: https://github.com/jingyaogong/minimind
score: 38
model: tencent/hy3-preview:free
generated_at: 2026-05-09T19:45:48.451732
---

📌 【開源專案】僅 3 元、2 小時訓練 64M 參數的 MiniMind LLM  

你以為訓練大語言模型需要超級電腦？這個開源專案證明，只需一張消費級顯卡和不到三塊台幣，就能從零開始訓練出自己的 64M 參數語言模型。  

🤔 **LLM 的學習門檻仍然很高**  
現行的大型語言模型動輒數十億甚至上千億參數，訓練與部署對個人開發者來說成本高、門檻深。雖然現成的 API 和微調工具讓使用變得容易，但卻讓人難以窺見模型內部運作的細節，失去「從零理解」的學習機會。  

🧪 **從 0 開始的完整訓練鏈路**  
MiniMind 專案採用純 PyTorch 原生實作，不依賴 transformers、trl、peft 等高階庫，提供以下完整流程的程式碼：  
- Tokenizer 與分詞器訓練  
- Dense 與 MoE 兩種主線架構（對齊 Qwen3 / Qwen3‑MoE 生態）  
- 預訓練（Pretrain）  
- 監督微調（SFT）  
- LoRA 微調  
- RLHF（DPO）  
- RLAIF（PPO / GRPO / CISPO）  
- Tool Use、Agentic RL、自適應思考與模型蒸餾  
- 視覺模態 MiniMind‑V、多模態 Omni 模型 MiniMind‑O、擴散語言模型 MiniMind‑dLM 與線性模型 MiniMind‑Linear  

所有核心算法皆從零撰寫，旨在讓開發者能逐行閱讀、修改與實驗。  

💡 **核心成果：低成本、快速復現**  
- 在單張 NVIDIA RTX 3090 上，SFT 階段跑完 1 epoch 大約需 2 小時。  
- 對應的 GPU 雲端租用成本約為 3 美元（約 3 元台幣）。  
- 得到的模型參數量約為 64M，相當於 GPT-3 的 1/2700，可在一般個人電腦上進行推理與進一步微調。  

這些數據來自專案頁面所說明的實測耗時與成本說明，未進行任何基準測試或性能比較。  

⚠️ **專案的使用情境與限制**  
- MiniMind 主要作為教學與實驗工具，模型規模故意設計得極小，不適合直接用於生產環境或需要高精度任務的場景。  
- 目前所述的訓練時間僅包含 SFT 階段的一個 epoch，未涵蓋完整的預訓練或多輪強化學習的長期穩定性。  
- 所有程式碼均以研究與學習為目的，使用時請參考專案附帶的 Apache 2.0 授權條款。  

🎯 **適合誰？適合做什麼？**  
- 想要從頭了解 LLM 內部運作的學生、開發者或研究者。  
- 想在低成本環境下嘗試 MoE、RLHF、Tool Use 等進階技術的實驗平台。  
- 作為課程或工作坊的教材，讓學員親手體驗「從 0 到 1」的模型建造過程。  

🔗 **專案連結**  
📂 GitHub：https://github.com/jingyaogong/minimind  
（專案頁面亦提供線上體驗與影片介紹的連結，詳見 README）  

#MiniMind #LLM #開源 #PyTorch #MoE #RLHF #AI學習 #GitHubTrending #深度學習 #AI教育
