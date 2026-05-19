---
title: "Semantic Generative Tuning for Unified Multimodal Models"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.18714
score: 118
model: tencent/hy3-preview:free
generated_at: 2026-05-19T20:27:21.627102
---

📌 **分割驅動的統一多模態模型**  

你以為多模態模型只要把理解和生成拼在一起就夠了？實際上，它們的表示空間常常各自為政，導致兩者無法互相促進。這篇論文提出了一種新思路——利用圖像分割作為生成代理，來對齊這兩個功能。  

🤔 **理解與生成的表示空間彼此脫節，限制了多模態模型的協同效應**  
現有統一多模態模型（UMMs）在訓練時，理解任務依賴稀疏的文本信號，而生成任務則透過密集的像素目標進行優化。這種脫耦的策略使得理解與生成的特徵空間難以對齊，進而阻礙了兩者的互相強化。  

🧪 **以圖像分割作為生成代理的階層式後訓練策略**  
研究團隊系統地探討了生成式後訓練，將不同的視覺任務視為生成的代理。經驗發現，高層語義任務——特別是圖像分割——能提供結構化的語義資訊，而不會被低層紋理細節干擾，因而同時提升視覺感知與生成布局的忠實度。  

💡 **分割作為代理顯著提升感知與生成的表現**  
基於此觀察，作者提出語義生成調整（Semantic Generative Tuning, SGT），以分割作為生成代理來對齊和協同多模態能力。機制分析顯示，SGT 能根本性地提升特徵的線性可分性，並優化視覺‑文本注意力的分配模式。在多個主流基準上，該方法持續改善多模態理解與生成保真度。  

🔍 **特徵線性可分性與注意力分配的機制改善**  
進一步的機制研究表明，SGT 不僅讓視覺特徵在語義空間中更易線性分離，還引導模型在跨模態注意力上更有效地分配資源，從而使理解與生成兩端的表示更加協調。  

⚠️ **作者未在摘要中詳細說明限制，需參考全文了解更多**  
摘要未具體列出實驗的樣本規模、訓練時長或特定架構的適用範圍，完整的限制討論請參閱論文全文。  

🎯 **將分割任務納入後訓練流程，可直接提升現有統一多模態模型的性能**  
對於工程師而言，SGT 提供了一種可直接插入的後訓練範式：只需要在現有 UMM 上加入圖像分割作為生成代理的訓練目標，即可在不重新設計架構的情況下，同時提升理解與生成的表現。代碼已於 https://song2yu.github.io/SGT/ 開源，便於快速驗證與部署。  

🔗 **論文連結**  
📝 Semantic Generative Tuning for Unified Multimodal Models  
👤 Songsong Yu, Yuxin Chen, Ying Shan, Yanwei Li (Shanghai Jiao Tong University; Tencent ARCLab)  
📄 論文：https://arxiv.org/abs/2605.18714  
💻 代碼：https://song2yu.github.io/SGT/  

#AI #Multimodal #CVPR #SemanticGenerativeTuning #ImageSegmentation #Tencent #ShanghaiJiaoTong #深度學習
