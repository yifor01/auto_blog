---
title: "LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2604.20796
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-04-23T20:00:34.347958
---

📌 【Inclusion AI】統一多模態理解與生成擴散LLM

你用過的多模態模型，是不是要麼擅長看圖答題，要麼擅長生圖修圖？
幾乎沒有模型能原生同時搞定這兩件事，更別說用統一框架處理交錯的多模態任務。
這篇新論文把離散擴散和LLM結合，給出了一個可落地的開源方案。

🤔 **多模態模型長期面臨理解與生成割裂痛點**
現有研究多將多模態理解與生成任務交由不同專用模型處理，缺乏原生統一架構同時支援兩類任務，也難以實現交錯的多模態生成與推理需求。本論文提出的LLaDA2.0-Uni即針對此問題設計，目標是構建原生集成、同時支援多模態理解與生成的統一框架。

🧪 **基於離散擴散LLM的三層統一架構**
LLaDA2.0-Uni是統一離散擴散大語言模型（dLLM），核心架構包含三個組件：
1. 全語義離散Tokenizer：透過SigLIP-VQ將連續視覺輸入離散化，實現文本與視覺輸入的統一離散表示
2. 基於MoE的dLLM骨幹：對文本與視覺輸入均採用塊級掩碼擴散（block-level masked diffusion）處理
3. 擴散解碼器：將視覺Token重建為高保真圖像

推理效率優化方面，骨幹採用前綴感知優化提升並行解碼效率，解碼器採用少步蒸餾減少生成所需步數。訓練階段使用精心整理的大規模數據集，搭配定制的多階段訓練流程。

💡 **統一框架兼顧理解與生成性能**
實驗結果顯示：
- 多模態理解性能與專用視覺語言模型（VLM）相當
- 圖像生成與編輯任務表現優異
- 原生支援交錯生成與推理，可同時處理文本與圖像的混合輸入輸出，為下一代統一多模態基礎模型提供可擴展範式

團隊已開源完整代碼與模型，可供研究者與工程師直接試用。

🔍 **離散擴散架構適配統一多模態需求**
本架構的核心創新在於將離散擴散與大語言模型結合，透過統一的離散Token表示，讓文本與視覺輸入能在同一骨幹中處理，原生集成架構避免了拼接不同模型帶來的兼容性問題。MoE骨幹設計可靈活分配不同模態的計算資源，前綴感知優化與少步蒸餾則提升了整體推理效率，讓統一架構具備實際應用可行性。

該架構對多模態基礎模型的未來走向具啟發性，契合當前對統一多模態模型與擴散生成的熱議方向。

⚠️ **公開摘要未披露具體研究限制**
目前公開的論文摘要未提及本研究的具体限制，相關實驗細節、數據集範圍、跨場景泛化能力等内容，可參考論文全文獲取。

🎯 **開源資源可直接用於多模態任務驗證**
1. 團隊已開源完整代碼與模型，工程師可直接部署試用，驗證統一多模態架構的實際效果
2. 架構設計中的離散Tokenizer、MoE骨幹、推理優化技巧，可作為多模態相關研究的參考
3. 原生支援交錯生成與推理的特性，適用於需要混合文本、圖像輸出的多模態應用場景

🔗 **論文連結**
📝 論文標題：LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model
👤 作者：Tiwei Bie, Haoxing Chen, Tieyuan Chen, Zhenglin Cheng（AGI Research Center; Inclusion AI）
📚 來源：Computer Vision and Pattern Recognition (arXiv)
🔗 論文：https://arxiv.org/abs/2604.20796
💻 開源代碼與模型：https://github.com/inclusionAI/LLaDA2.0-Uni

歡迎討論：你認為統一多模態模型會是下一代基礎模型的發展方向嗎？👇

#多模態 #擴散模型 #大語言模型 #LLaDA #InclusionAI #AI研究 #開源模型
