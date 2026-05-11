---
title: "Flow-OPD: On-Policy Distillation for Flow Matching Models"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.08063
score: 111
model: tencent/hy3-preview:free
generated_at: 2026-05-11T20:32:17.848016
---

📌 **Flow-OPD：On‑Policy Distillation 提升 Flow Matching 多任務對齊**  

你以為只要把多個獎勵函數塞進 Flow Matching 模型就能得到全能圖像生成器？實際上，獎勵稀疏與梯度衝突會讓模型在各項指標上來回拉扯，甚至學會「獎勵駭客」。  

🤔 **多任務對齊的兩大瓶頸：獎勵稀疏與梯度干擾**  
現有的 Flow Matching (FM) 文本到圖像模型在同時滿足多個目標時，會遇到兩個問題：一是標量獎勵導致的稀疏回饋，使得強化學習難以獲得有效梯度；二是異質目標聯合優化時產生的梯度干擾，使得各項指標互相拖累，出現「跷跷板效應」並容易產生獎勵駭客現象。這些問題限制了模型在通用任務上的表現。  

🧪 **兩階段對齊策略：先養師後融學**  
Flow-OPD 採用 On‑Policy Distillation 的思想，分為兩個階段進行對齊。首先，針對每個單一任務使用 GRPO 進行微調，培養出領域專家教師模型，讓每位專家在獨立環境下能達到其性能上限。其次，透過 Flow‑based Cold‑Start 構建一個穩健的初始策略，然後以三步驟的方式將多位教師的知識蒸餾到單一學生模型中：(1) on‑policy 採樣產生軌跡，（2) 根據任務進行路由標註，（3) 以密集的軌跡層級監督進行學習。  

🚀 **核心發現：GenEval 提升 29 點，OCR 提升 35 點**  
在 Stable Diffusion 3.5 Medium 基礎上，Flow-OPD 使 GenEval 分數從 63 提升至 92，OCR 準確率從 59 提升至 94，相較於 vanilla GRPO 大約提升 10 個百分點。值得注意的是，這些提升是在保持圖像保真度與人類偏好對齊的前提下達成的，並出現「教師超越」的現象——學生模型在某些指標上甚至優於其教師。  

💡 **Manifold Anchor Regularization：穩定生成 manifolds**  
為進一步減少純 RL 對齊常見的美學退化，Flow-OPD 引入 Manifold Anchor Regularization (MAR)。MAR 利用一個與任務無關的教師模型，在完整資料上提供監督訊號，將生成過程錨定在高質量的圖像 manifold 上，從而在多任務對齊時維持圖像的視覺品質。  

⚠️ **研究限制：僅在特定基礎模型上驗證，長期效果尚未探討**  
目前的實驗僅基於 Stable Diffusion 3.5 Medium 進行，未涉及其他架構或更大規模的模型。此外，評估主要集中在即時的 GenEval 與 OCR 指標，長期使用中的穩定性與潛在的副作用仍需後續工作檢驗。  

🎯 **實務啟示：採用階段式對齊與 manifold 錨定可提升通用模型**  
對於希望構建通用文本到圖像系統的工程團隊，Flow-OPD 提供了一個可直接套用的後訓練範例：先以單一獎勵訓練專家教師，再以冷啟動與 on‑policy 蒸餾融合知識，最後加入 manifold 正則化以防止美學衰減。這種「先分後合」的流程在保持圖像品質的同時，顯著提升多任務對齊的效果。  

🔗 **論文連結**  
📝 Flow-OPD: On-Policy Distillation for Flow Matching Models  
👤 Zhen Fang, Wenxuan Huang, Yu Zeng, Yiming Zhao, Shuang Chen  
🔗 https://arxiv.org/abs/2605.08063  

你有嘗試過在多任務對齊中使用蒸餾策略嗎？歡迎在留言區分享經驗或疑問 👇  

#AI #FlowMatching #OnPolicyDistillation #TextToImage #StableDiffusion #UCLA #USTC #CUHK #Xiaohongshu #MachineLearning #ComputerVision
