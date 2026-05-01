---
title: "DPN-LE: Dual Personality Neuron Localization and Editing for Large Language Models"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2604.27929
score: 107
model: tencent/hy3-preview:free
generated_at: 2026-05-01T20:02:57.868401
---

📌 DPN-LE：干預 0.5% 神經元，LLM 性格可控且推理不崩

你以為要精準控制大型語言模型的性格，就必須犧牲推理能力？最新研究顯示，修改不到百分之一的神經元，不僅能穩固性格表現，還能大幅壓縮能力損失。

🤔 **性格可編輯，但通用能力常被連坐**

隨著 LLM 被廣泛部署，如何安全、可控地調整其「性格」與價值傾向已成關鍵議題。現有的人格編輯方法多數依賴神經元級干預，但往往牽涉大量神經元修改，並導致模型整體表現顯著下滑。這引發一個根本問題：被修改的神經元，確實都負責性格表現嗎？

🧪 **對比 MLP 激活的雙重人格神經元定位法**

本研究提出 DPN-LE（Dual Personality Neuron Localization and Editing），針對 LLaMA-3-8B-Instruct 與 Qwen2.5-7B-Insect 進行實驗。核心設計包含：

- 以高特質與低特質樣本對比 MLP 激活，定位人格相關神經元  
- 層級化構建引導向量，並以 Cohen’s d 與激活強度雙閾值過濾  
- 僅選取互斥性最強的神經元子集，進行稀疏線性干預  

全程僅需約 1,000 對比樣本，即可在推論階段動態調控性格。

📉 **干預 ~0.5% 神經元，推理表現大幅保留**

- 現有方法可改變性格，但普遍損害通用能力  
- DPN-LE 僅干預約 0.5% 神經元，達到具競爭力的人格控制  
- 推理任務的能力損失顯著低於基線方法  

結果顯示，神經元具有多功能性，且對立性格特質呈現高度互斥的表示模式；盲目修改易觸及知識與推理相關區域。

💡 **用性格對比定位，而非用干預取代理解**

DPN-LE 的關鍵在於「分離」：透過高/低特質激活差異，將混雜在多功能神經元中的性格訊號萃取過濾。這讓干預可以更精準，避免層級間的表示相互干擾，並保留模型原有的知識與推理結構。

⚠️ **目前限於中階模型與短期效果**

- 實驗對象為 7B–8B 規模模型  
- 長期穩定性與跨任務泛化仍需驗證  
- 方法聚焦 MLP 層，干預粒度與擴展性存在工程取捨  

🎯 **可控對齊的輕量路徑，值得納入微調流程**

- 人格控制不必等價於大範圍權重更新  
- 稀疏線性干預適合部署在推論時期的對齊階段  
- 可結合 RLHF 或安全微調，進一步壓縮副作用  

🔗 **論文連結**  
📝 DPN-LE: Dual Personality Neuron Localization and Editing for Large Language Models  
👤 Lifan Zheng, Xue Yang, Jiawei Chen, Chenyan Wu, Jingyuan Zhang et al.  
🏫 Southeast University; Shanghai Jiao Tong University; Tsinghua University; Kuaishou Technology; Northeastern University; others  
🔗 https://arxiv.org/abs/2604.27929  

你會願意用極少神經元干預來換取可控性格嗎？歡迎留言討論實務應用與風險 🧠

#AI #LLM #可控對齊 #神經網絡可解釋性 #模型微調 #AI安全 #人格編輯
