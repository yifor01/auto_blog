---
title: 'Flex-Forcing: Towards a Unified Autoregressive and Bidirectional Video Diffusion
  Model'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.03509
score: 91
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T13:22:22.011534'
---

📌 Flex-Forcing：同時支援自回歸與雙向生成的影片 Diffusion 模型  

TL;DR：Flex-Forcing 透過彈性分塊機制，在時間與去噪步驟上同時支援自回歸與雙向產生，提高影片品質與推論速度。

🤔 統一自回歸與雙向生成的挑戰  
傳統影片 Diffusion 模型要麼以自回歸方式逐幀生成，速度慢但可控制；要麼以雙向方式一次處理全部幀，速度快但缺乏靈活性。Flex-Forcing 針對這兩種生成規則的差異，提出一套「彈性分塊」機制，讓同一模型在不同時間步與去噪階段切換生成模式。

🧩 彈性分塊機制的核心概念  
- **時間分塊**：將影片序列切成可變長度的時間區段；每個區段內可選擇自回歸或雙向去噪。  
- **去噪步驟分塊**：在 Diffusion 的噪聲去除過程中，同樣允許在不同去噪階段切換生成規則。  
- 這樣的設計讓模型在保持全域性一致性的同時，仍能針對區域性細節使用自回歸精細化，提升最終影片的視覺品質。

🎯 實務影響與應用前景  
- **推論速度**：因為可以在大部分時間步使用雙向去噪，只在關鍵區段切換自回歸，減少了逐幀解碼的計算成本。  
- **影片品質**：雙向模式提供全域性一致性，自回歸模式則強化區域性細節，兩者結合有望在複雜動作或快速變化的場景中取得更佳效果。  
- **彈性部署**：開發者可根據硬體資源或應用需求，自行設定分塊策略，兼顧效能與品質。

🔗 來源  
- 標題：Flex-Forcing: Towards a Unified Autoregressive and Bidirectional Video Diffusion Model  
- 連結：https://huggingface.co/papers/2607.03509  

#VideoDiffusion #FlexForcing #Autoregressive #Bidirectional #GenerativeAI #MachineLearning #DeepLearning #ComputerVision #TemporalModeling #AIResearch
