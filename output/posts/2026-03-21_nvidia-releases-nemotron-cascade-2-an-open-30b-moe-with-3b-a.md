---
title: "NVIDIA Releases Nemotron-Cascade 2: An Open 30B MoE with 3B Active Parameters, Delivering Better Reasoning and Strong Agentic Capabilities"
source: MarkTechPost
url: https://www.marktechpost.com/2026/03/20/nvidia-releases-nemotron-cascade-2-an-open-30b-moe-with-3b-active-parameters-delivering-better-reasoning-and-strong-agentic-capabilities/
score: 103
model: gpt-4o-free
generated_at: 2026-03-22T18:22:05.256217
---

📌 **【NVIDIA 最新發布】Nemotron‑Cascade 2：30B MoE 僅激活 3B 參數，卻在奧數、程式競賽中奪金**

你以為只有龐大參數才能解奧數題？NVIDIA 的新模型用只有 3B 有效參數就拿下國際奧林匹克金牌，這種「智慧密度」到底是怎麼練成的？

🤔 **只有 3B 有效參數，卻能奪奧數金牌**  
Nemotron‑Cascade 2 是一個開放權重的 30B 參數 Mixture‑of‑Experts (MoE) 模型，實際激活參數僅 3B。NVIDIA 強調其「智慧密度」概念——在遠小於前沿模型的參數規模下，仍能提供先進的推理能力。該模型是繼首個後第二個在 2025 國際數學奧林匹克 (IMO)、國際資訊奧林匹克 (IOI) 與 ICPC 世界決賽中達到金牌水平的開放權重 LLM。

🧪 **後訓練管線：從 SFT 到多階段 Cascade RL**  
模型的推理能力來自於以 Nemotron‑3‑Nano‑30B‑A3B‑B 為基礎的後訓練流程。在有監督微調 (SFT) 階段，研究團隊使用了經過精心挑選的資料集，樣本被組織成最長 256K token 的序列。接著模型經過 Cascade RL，該流程採用逐域（domain‑wise）訓練，包含以下階段：  
- 指令跟隨 (IF‑RL)  
- 多域 RL  
- RLHF  
- 長文脈 RL  
- 專門的 Code 與 SWE RL  

這種設計旨在透過為每個域調整超參數來遵循「不破壞其他域」的原理，因而減少災難性遺忘。

💡 **MOPD：關鍵的蒸餾創新**  
在 Cascade RL 過程中，NVIDIA 引入了 MOPD（Model‑level Output‑level Prediction Distillation）。MOPD 會從同一 SFT 初始化中產出的最佳中間「教師」模型中蒸餾出密集的 token 級別優勢，這被定義為一種數學上的優勢（文中給出的公式）。此機制被指出是模型在推理任務上表現突出的重要因素。

📊 **核心發現：在特定推理基準上表現優異，但非全場勝出**  
- 在數學推理、程式碼生成、對齊與指令遵循等領域，Nemotron‑Cascade 2 達到目前最佳狀態（SOTA）的表現。  
- 該模型是第二個在 2025 IMO、IOI 與 ICPC 世界決賽中拿到金牌的開放權重 LLM。  
- 與最近發布的 Qwen3.5‑35B‑A3B（2026 年 2 月）以及更大的 Nemotron‑3‑Super‑120B‑A12B 相比，它在上述目標類別中展現出更強的推理與代理能力。  
- 然而，作者明確指出這並不是「全場勝出」模型：在其他基準上的表現未必領先，具體細節未在此摘要中展開。

⚠️ **研究限制：評估範圍有限，硬體需求未說明**  
- 所述優勢主要集中在數學、程式與指令遵循等特定任務，未涵蓋所有可能的語言模型基準。  
- 摘要未提供模型在廣泛零樣少樣或多語言情況下的詳細結果。  
- 雖然模型是開放權重，但文中未提及運行該模型所需的具體硬體配置或推理延遲，這對實務部署而言是重要考量。

🎯 **實務啟示：適合專注推理的場景，需評估成效與資源**  
- 對於需要高效數學推理或程式輔助的工程團隊，Nemotron‑Cascade 2 提供了一種在參數激活上極具效率的選擇。  
- 由於其專注於特定領域的訓練 pipeline，使用時應先在目標任務上做小規模驗證，確認其優勢是否轉移到實際案例。  
- 開放權重的特性使得社群能夠在遵守 licence 的前提下進行微調或部署，但仍需自行評估模型在多樣化工作負載上的表現。

🔗 **資訊來源**  📰 MarkTechPost – *NVIDIA Releases Nemotron‑Cascade 2: An Open 30B MoE with 3B Active Parameters, Delivering Better Reasoning and Strong Agentic Capabilities*  
🔗 https://www.marktechpost.com/2026/03/20/nvidia-releases-nemotron-cascade-2-an-open-30b-moe-with-3b-active-parameters-delivering-better-reasoning-and-strong-agentic-capabilities/

你有試過在推理密集型任務中使用這種參數激活極低的 MoE 模型嗎？歡迎在留言區分享你的經驗與觀察 👇

#NVIDIA #NemotronCascade2 #MoE #LLM #推理 #程式輔助 #AI研究 #開放權重 #AgenticAI #MarkTechPost
