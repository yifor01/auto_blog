---
title: "Draft-OPD: On-Policy Distillation for Speculative Draft Models"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.29343
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-06-02T21:33:51.496975
---

📌 【Draft-OPD】草稿模型的政策蒸餾  

你有沒有想過，讓小模型幫大模型「猜測」下一個詞，其實訓練方式可能讓它越用越笨？  
Draft-OPD 提出一種在線蒸餾方法，讓草稿模型在推理時持續學習，彌合訓練與推理的落差。  
這意味著，我們可以在不犧牲品質的情況下，獲得顯著的延遲減少。  

🤔 **離線訓練與實際推理的落差限制了草稿模型的提升**  
Speculative decoding 依賴輕量的 draft model 先行提出 token 候選，再由大模型驗證。然而，傳統的監督微調是離線進行的，草稿模型在訓練時無法看到目標模型在實際推理中的行為，導致訓練與推理之間的分布落差（offline‑to‑inference mismatch），進而造成效益平台。  

🧪 **透過目標輔助 rollout 與錯誤重播的 on‑policy 蒸餾**  
論文提出 On‑Policy Distillation (OPD)：在訓練階段讓 draft model 參與「目標輔助 rollout」，即在生成過程中偶爾參考目標模型的輸出，使其學習到目標模型的策略；同時引入「錯誤重播」機制，將過去的預測錯誤重新送回訓練，強化模型對自身失誤的校正。這種在線（on‑policy）的蒸餾方式直接縮小了離線訓練與實際推理的間隔。  

🔬 **核心發現：直接提升解碼速度而不犧牲生成品質**  
根據評審指出，該方法能夠在不降低生成質量的前提下，提升 speculative decoding 的解碼速度，並提供可量測的延遲減少。這使得該技術適合當前對高效推理需求日益增長的工程場景。  

💡 **為何 on‑policy 蒸餾能橋接離線‑到‑推理的鴻溝**  
目標輔助讓 draft model 在訓練時直接體驗目標模型的行為分布，減少了因行為偏差導致的錯誤累積；錯誤重播則專注於模型在推理中容易失敗的情境，強化其在實際使用中的穩健性。兩者結合，使得草稿模型在推理階段的表現更接近其訓練目標，從而解除離線‑到‑推理的瓶頸。  

⚠️ **僅提供概念驗證，具體實驗細節尚未公開**  
摘要與評論中未具體說明使用的基準資料集、模型規模或具體速度提升數字，因此實際效益在不同硬體與模型組合上的表現仍需參考論文完整實驗章節。  

🎯 **工程師可直接將此方法納入現有 speculative decoding 流程**  
若你正在部署 LLM 並使用 speculative decoding，可考慮在 draft model 的訓練流程中加入目標輔助 rollout 與錯誤重播的步驟。此方法不需要重新設計解碼架構，僅是訓練策略的調整，預期能帶來可觀的延遲改善。  

🔗 **論文連結**  
📝 Draft-OPD: On-Policy Distillation for Speculative Draft Models  
👤 作者：未註明  
🔗 https://huggingface.co/papers/2605.29343  

#AI #LLM #SpeculativeDecoding #EfficientInference #HuggingFace #DraftOPD #MachineLearning
