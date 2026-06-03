---
title: 'NVIDIA Releases Cosmos 3: A Two-Tower Mixture-of-Transformers Foundation Model
  Unifying Physical Reasoning, World Generation, and Action Generation'
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/03/nvidia-releases-cosmos-3-a-two-tower-mixture-of-transformers-foundation-model-unifying-physical-reasoning-world-generation-and-action-generation/
score: 108
model: tencent/hy3-preview:free
generated_at: '2026-06-03T21:31:15.528263'
---

📌 【NVIDIA 最新發布】Cosmos 3：統一物理推理、世界生成與動作生成的雙塔 MoT 模型  

你以為機器人只需要「看」和「動」？實際上，它得先「理解」世界才能正確行動。  
Cosmos 3 把推理與生成緊密結合，單一模型就能完成感知、預測與決策。  
這意味著機器人、自動駕駛與倉儲監控系統未來可用更少的模型實現端到端的物理 AI。  

🤔 **統一三大能力，避免模型分裂**  
早期 Cosmos 版本將物理推理、世界生成與動作生成拆分成獨立模型，導致資源重複與介面複雜。Cosmos 3 透過一個開放的基礎模型，將這三項功能納入同一架構，讓系統在感知環境後直接產生未來觀測與動作序列。  

🧪 **雙塔 Mixture‑of‑Transformers 架構**  
模型由兩個塔組成：  
- **Reasoner 塔**：基於 Qwen3‑VL 的視覺語言模型，採用自回歸架構，負責解讀圖像、影像與文字，理解運動、物體互動等物理語境，被團隊稱為模型的「大腦」。  
- **Generator 塔**：採用擴散（diffusion）過程，生成物理感知的未來影像與動作序列，其輸出完全條件於 Reasoner 塔的理解。  
資訊單向流動：Reasoner → Generator；Reasoner 可單獨運行，而 Generator 必須同時啟動兩塔以進行引導生成。  

🚀 **三種規模，適配不同硬體需求**  
NVIDIA 提供 Edge、Nano 與 Super 三個尺度，皆採用相同的雙塔 Mixture‑of‑Transformers 設計：  
- **Cosmos3‑Nano**：16B 參數，建立在密集 8B Transformer 上（源自 Qwen3‑VL 8B），適合工作站 GPU（如 NVIDIA RTX PRO 6000）進行即時推理。  
- **Cosmos3‑Super**：64B 參數，建立在密集 32B Transformer 上，提供更高的推理與生成能力。  
具體 Edge 規模細節未在摘要中說明，但同樣採用相同架構。  

💡 **開源即用，降低實體 AI 開發門檻**  
NVIDIA 同時開放了模型檢查點、訓練腳本、部署工具與訓練資料集。這意味著機器人、自動駕駛與倉儲監控團隊可以直接在本地或雲端環境中載入、微調並部署統一的物理 AI 系統，無需自行拆解與對接多個模型。  

⚠️ **目前僅說明架構與開放資源，實測效能尚未公開**  
摘要未提供基準測試結果（如推理延遲、生成品質或下游任務準確率），因此無法評估其在真實場景中的具體表現；此外，模型大小仍屬於大規模範疇，對資源受限的邊緣設備可能需要進一步壓縮或蒸餾。  

🎯 **工程師可先從 Nano 版本開始實驗**  
- 若目標是即時機器人控制或邊緣推理，優先測試 Cosmos3‑Nano 在 RTX PRO 6000 上的延遲與功耗。  
- 若需要更高品質的世界生成或長 horizion 動作規劃，可嘗試 Cosmos3‑Super 並參考提供的訓練腳本進行域適配。  
- 利用開源的資料集與腳本，先在模擬環境驗證 Reasoner 塔的物理理解能力，再觀察 Generator 塔是否能產生符合物理約束的影像與動作序列。  

🔗 **論文連結**  
📝 NVIDIA Releases Cosmos 3: A Two-Tower Mixture-of-Transformers Foundation Model Unifying Physical Reasoning, World Generation, and Action Generation  
👤 Asif Razzaq (MarkTechPost 報導)  
🔗 https://www.marktechpost.com/2026/06/03/nvidia-releases-cosmos-3-a-two-tower-mixture-of-transformers-foundation-model-unifying-physical-reasoning-world-generation-and-action-generation/  

你認為統一推理與生成的單一模型，會如何改變機器人與自動駕駛的開發流程？歡迎在留言區分享你的看法 👇  

#NVIDIA #Cosmos3 #MixtureofTransformers #PhysicalAI #Robotics #AutonomousVehicles #WarehouseAI #OpenSource #AI研究 #深度學習
