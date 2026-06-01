---
title: "Welcome NVIDIA Cosmos 3: The First Open Omni-model for Physical AI Reasoning and Action"
source: HuggingFace Blog
url: https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai
score: 122
model: tencent/hy3-preview:free
generated_at: 2026-06-01T21:59:03.022149
---

📌 【NVIDIA Cosmos 3】首個開放 omni‑model 統一世界生成、物理推理與動作生成  

你是否曾為了讓機器人「看得見、想得通、動得準」而同時管理數個不同的模型？世界生成、場景理解、動作規劃各自獨立，導致開發流程繁雜且難以維護。  

🤔 **一模型搞定世界生成、物理推理與動作產出**  

NVIDIA 今日在 Hugging Face 釋出 **Cosmos 3**，宣稱是首個開放的 **omni‑model**，採用 **Mixture‑of‑Transformers (MoT)** 架構，將先前分離的 Cosmos Predict（世界生成）、Cosmos Transfer（可控生成）、Cosmos Reason（場景理解）與 Cosmos Policy（動作規劃）四個能力整合進單一前向傳遞中。這意味著，開發者現在只需呼叫同一個模型，即可：  

- 從文字、圖片、影片或動作輸入生成符合物理定律的可信視訊世界；  
- 在同一次推理中對運動、因果關係與空間關係進行推理；  
- 直接產出可執行的動作序列（policy），用於機器人、自駕車或智慧空間的控制。  

🧪 **開放資源與整合工具**  

此次發布同步提供：  

- **Cosmos 3 Super** 與 **Cosmos 3 Nano** 兩種規模的模型權重，附帶模型卡與授權說明；  
- **Diffusers 整合**，讓生成管線能直接呼叫 Cosmos 3 進行影像/視訊產生；  
- **後訓練腳本**（GitHub），支援使用自有資料繼續訓練或微調模型；  
- **開放合成資料集（SDG）**，專為實體 AI 任務設計，可用於預訓練或下游微調。  

💡 **對實體 AI 開發的啟示**  

- **統一介面降低複雜度**：不必在多個模型與對應的推理管線之間切換，開發流程變得更線性且易於除錯。  
- **模態互通性提升**：因為世界生成、推理與動作產出共享同一潛在空間，理論上能讓模型在「看見」與「行動」之間建立更一致的內部表徵。  
- **即時可用**：模型權重與工具已經上傳至 Hugging Face Hub，開發者可直接下載、測試並依需求擴充。  

⚠️ **目前已知的範疇**  

- 此版本專注於影像/視訊世界的生成與基礎物理推理；文件中未提及其他感測模態（如雷達、點雲）的支援情況。  
- 作為首次開放釋出，實際在複雜機械手臂或高速自駕場景中的表現仍需社群進一步驗證與微調。  

🎯 **實務建議**  

1. 若你正在構建需要「視覺理解＋動作規劃」的原型，可先嘗試使用 Cosmos 3 Nano 進行快速概念驗證。  
2. 想要針對特定領域（如倉儲機器人或室內導航）提升表現，可參照提供的後訓練腳本，在自有合成或真實資料上進行微調。  
3. 將 Diffusers 整合視為快速產生訓練資料或視覺化中間結果的管線，減少自行建立生成模型的成本。  

🔗 **論文／資源連結**  
📝 Welcome NVIDIA Cosmos 3: The First Open Omni-model for Physical AI Reasoning and Action  
👤 NVIDIA Research Team  
🔗 https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai  

你認為這種「一模型全能」的設計會如何改變實體 AI 開發的工作流程？歡迎在留言區分享你的看法 👇  

#NVIDIA #Cosmos3 #PhysicalAI #WorldFoundationModel #MixtureOfTransformers #Diffusers #Robotics #AutonomousVehicles #SmartSpaces #HuggingFace #AI開發
