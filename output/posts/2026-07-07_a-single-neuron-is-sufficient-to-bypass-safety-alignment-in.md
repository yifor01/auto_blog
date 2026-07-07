---
title: A Single Neuron Is Sufficient to Bypass Safety Alignment in Large Language
  Models
source: Apple ML
url: https://machinelearning.apple.com/research/single-neuron-safety-alignment
score: 97
model: google/gemma-4-31b-it:free
generated_at: '2026-07-07T21:09:56.608630'
---

📌 單一神經元即可繞過大型語言模型的安全對齊

TL;DR：研究顯示只要抑制或放大每個安全子系統中的一顆關鍵神經元，就能讓 1.7B‑70B 引數的模型在不經訓練或提示工程的情況下，直接產生或隱匿有害內容。

🧩 **安全對齊的雙重機制**  
Apple ML 的論文將大型語言模型（LLM）的安全機制拆解為兩套獨立的神經元群：  
1. **refusal neurons** – 控制模型是否拒絕回應危險請求；  
2. **concept neurons** – 內部編碼危險知識本身。  

作者指出，這兩種神經元在模型中是機制上分離的，且各自只要被單一神經元「門控」即可決定安全行為。

🧩 **單神經元即能造成兩種失效**  
- **抑制 refusal neuron**：在面對明確的有害請求時，若將辨識到的 refusal neuron 靜音，模型會直接輸出危險內容，等同「繞過」安全拒絕。  
- **放大 concept neuron**：對於原本無害的提示，若強化與危險概念相關的 concept neuron，模型會自行產生有害訊息，形成「從善意輸入到有害輸出」的放大效應。

⚙️ **實驗範圍與設定**  
- **模型族群**：涵蓋兩個不同的模型系列，共七個模型，引數規模從 1.7 B 到 70 B 不等。  
- **操作方式**：僅透過直接幹預（不需額外微調或精心設計提示）對目標神經元進行抑制或放大。  
- **結果**：在所有測試的危險請求與無害提示上，單顆神經元的幹預即可一致導致安全失效，說明安全對齊並未在整體權重上廣泛分散。

💡 **對工程師的啟示**  
- **安全檢測須聚焦微觀層級**：僅靠整體權重正則化或大規模微調可能無法覆蓋關鍵神經元的漏洞。  
- **防禦策略可考慮 neuron‑level 監控**：在部署 LLM 時，可加入對已識別的 refusal / concept 神經元的即時監測與限制，降低單點失效風險。  
- **模型審計需要更細緻的因果分析**：辨識出哪些神經元對安全行為具因果充分性，是未來安全對齊研究的重要方向。

🔗 來源  
- 標題：A Single Neuron Is Sufficient to Bypass Safety Alignment in Large Language Models  
- 連結：https://machinelearning.apple.com/research/single-neuron-safety-alignment  

#LLM #SafetyAlignment #Neuroscience #AIAlignment #MachineLearning #AppleML #NeuralNetwork #ModelSecurity #PromptEngineering #AIResearch
