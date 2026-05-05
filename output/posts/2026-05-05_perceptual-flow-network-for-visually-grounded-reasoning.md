---
title: "Perceptual Flow Network for Visually Grounded Reasoning"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.02730
score: 123
model: tencent/hy3-preview:free
generated_at: 2026-05-05T19:37:40.299682
---

📌 【多機構聯合發表】解耦感知與推理，PFlowNet 緩解 LVLM 幻覺

大型視覺語言模型（LVLMs）雖然能力驚人，但有一個頑疾始終困擾著開發者：模型往往過度依賴語言慣性，導致「看圖說故事」時出現幻覺（Hallucination）。明明圖片裡沒有某個物體，模型卻可能因為文本語境而堅稱它存在。

🤔 **標準訓練目標無法約束視覺軌跡，導致語言偏見**

目前的 LVLMs 多採用標準最大似然估計（MLE）進行優化，這種方式缺乏對視覺推理路徑的強約束。為了解決這個問題，許多研究引入了外部視覺專家（如目標檢測模型）的幾何先驗作為監督訊號。然而，這種做法存在一個顯著的 trade-off：過度追求幾何精確度，卻忽略了這些特徵對高層次推理的實際效用。

🧪 **來自華東師大、上海交大與螞蟻集團的技術突破**

這篇由華東師範大學、四川大學、上海交通大學、香港科技大學、螞蟻集團及上海人工智能實驗室共同發表的研究，提出了一種全新的架構：Perceptual Flow Network (PFlowNet)。

 **解耦感知與推理，建立自條件生成過程**

PFlowNet 的核心設計在於將「感知」與「推理」進行解耦。不同於以往強行對齊專家先驗的做法，PFlowNet 透過變分強化學習（Variational Reinforcement Learning），整合多維度獎勵與鄰近幾何塑形（Vicinal Geometric Shaping）。這使得模型能夠在保持視覺可靠性的同時，學習到真正服務於推理目標的感知行為，而非單純的幾何匹配。

💡 **推理導向的感知行為，效能與可解釋性兼得**

這種設計不僅讓模型的視覺推理過程更具可解釋性，更在實證數據上取得了顯著突破。PFlowNet 在具挑戰性的 V* Bench 上達到了 90.6% 的準確率，並在 MME-RealWorld-lite 上取得 67.0% 的成績，雙雙刷新了當前的 SOTA（State-of-the-Art）紀錄。

⚠️ **學術研究階段，實際部署需考量計算成本**

雖然論文提供了具備理論保證的性能分析，但作為一篇學術論文，其實際落地到工業級應用時，變分強化學習所需的計算資源以及多維度獎勵函數的設計細節，仍需進一步的工程優化與驗證。

🎯 **從「看圖說話」走向「看圖思考」**

對於致力於解決 LVLM 幻覺問題的工程師來說，PFlowNet 提供了一個重要的啟示：單純堆疊視覺特徵並不夠，透過強化學習將感知過程與推理目標對齊，才是提升模型可信度的關鍵路徑。

🔗 **論文連結**
📝 Perceptual Flow Network for Visually Grounded Reasoning
👤 Yangfu Li, Yuning Gong, Hongjian Zhan, Teng Li, Yuanhuiyi Lyu
🏫 EAST CHINA NORMAL UNIVERSITY; SCU; HKUST; SJTU; Ant Group; Shanghai AI Laboratory
🔗 論文：https://arxiv.org/abs/2605.02730

你認為解耦感知與推理是解決 LVLM 幻覺的最佳路徑嗎？歡迎在留言區分享你的看法 👇

#AI #ComputerVision #LVLM #Hallucination #強化學習 #技術論文 #PFlowNet #上海交大 #螞蟻集團
