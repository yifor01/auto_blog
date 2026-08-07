---
title: Locking Pretrained Weights via Deep Low-Rank Residual Distillation
source: Apple ML
url: https://machinelearning.apple.com/research/locking-pretrained-weights
model: tencent/hy3:free
generated_at: '2026-08-07T07:32:34.929436'
score: 99
---

📌 Locking Pretrained Weights via Deep Low-Rank Residual Distillation  
TL;DR：DLR-Lock 用深層低秩殘差網路鎖住預訓練權重，提升反向傳播開銷以防未授權微調。  

🎣 當開放權重模型讓誰都能微調時，安全與開放似乎成了零和博弈；如果防護機制本身就能被攻擊者輕易繞過，那麼鎖住模型的意義又在哪裡？  

🤔 背景或問題  
開放權重的語言模型（LLM）便於跨平臺使用與開放研究，但同時也使未授權的修改成為可能。簡易的結構性防禦易被具備完整模型知識的攻擊者逆向破解，因而需要一種能在攻擊者完全了解防禦策略的情況下仍舊有效的方法。  

🧩 方法或架構  
本文提出 DLR-Lock，其核心是將模型中每個預訓練的 MLP 替換為參數量相近的深層低秩殘差網路（DLR‑Net）。這樣的設計在反向傳播期間會使激活記憶體隨著網路深度線性增長。DLR‑Net 的訓練採用逐模組蒸餾（module‑wise distillation），以保持原始模型的前向傳播行為。  

📊 數據或結果  
作者在 LLM 上進行實驗，證實 DLR‑Lock 能夠抵禦具有完整防禦策略知識的適應性攻擊者，同時未顯著降低原始模型的能力。具體的評估指標或基準數據未在摘要中說明。  

💡 深入分析  
防禦利用了自動微分在推理與訓練階段的不對稱性：透過在反向傳播中增加額外的記憶體與計算開銷，使標準微調的最佳化變得更加困難。架構上的不匹配進一步加劇了這種效應，導致反向傳播的開銷顯著高於前向傳播。  

⚠️ 限制  
摘要未詳細討論 DLR‑Lock 的潛在限制，例如在特定硬體上的實際記憶體負擔、對不同模型架構的適用性，或是在極端規模模型上的行為。  

🎯 實務啟示  
對於希望在開放權重的同時保護智慧財產權的模型提供者，DLR‑Lock 提供一種可行的途徑：透過增加反向傳播的資源消耗，提升未授權微調的成本，而不影響模型在正常推理時的表現。實際部署時需評估額外的記憶體與計算開銷是否可接受。  

🔗 來源  
- 標題：Locking Pretrained Weights via Deep Low-Rank Residual Distillation  
- 作者／機構：Keitaro Sakamoto†**, Pierre Ablin, Federico Danieli, Marco Cuturi @ Apple ML  
- 連結：https://machinelearning.apple.com/research/locking-pretrained-weights  

#AI #LLM #ModelSecurity #DeepLearning #Distillation #AppleML #ICML #DefenseMechanism #OpenWeights #FineTuning
