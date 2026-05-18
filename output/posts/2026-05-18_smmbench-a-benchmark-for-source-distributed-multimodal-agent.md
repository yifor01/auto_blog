---
title: "SMMBench: A Benchmark for Source-Distributed Multimodal Agent Memory"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.15710
score: 98
model: tencent/hy3-preview:free
generated_at: 2026-05-18T20:43:30.834973
---

📌 SMMBench：多模態記憶的跨來源挑戰  

你以為 AI 已經能『記住』所有線索？事實上，當證據散落在對話、截圖、表格與文件等獨立來源時，現有模型卻常常找不出關鍵拼圖。  

**記憶基準多聚焦單一情境，卻忽略跨來源證據整合**  
現有多模態記憶基準多半將所有線索預先組裝在單一、經過篩選的情境中評估模型。這種設計無法檢測模型在面對獨立產生、異質構成的證據時，是否能進行有效的檢索、對齊與組合。  

**建構 264 個獨立來源、1877 個樣本的 SMMBench**  
為彰顯此缺口，研究團隊提出 Source‑distributed Multimodal Memory Benchmark（SMMBench）。該基準包含 264 個獨立來源（如對話紀錄、使用者畫面截圖、表格、圖片與文件），衍生出 1877 個測試樣本，專門考察模型在多個來源之間進行多模態推理的能力。  

**實驗顯示現有記憶與檢索模型在此基準上仍有明顯不足**  
在 SMMBench 上測試了若干代表性的記憶式與檢索式基線。結果顯示，這些模型在跨來源多模態推理、衝突解決、偏好推理以及記憶導向的動作預測四項核心能力上，均未達到理想表現，凸顯來源分散記憶仍是未被充分評估的挑戰。  

**問題出在證據對齊與衝突解決的能力缺口**  
進一步分析發現，模型主要困難在於如何將來自不同模態與來源的線索正確對齊，以及在出現互相矛盾資訊時進行有效的衝突解決。這兩個環節直接影響後續的偏好判斷與動作預測。  

**基準規模與任務設計尚未覆蓋長期記憶與真實Agent互動**  
目前的 SMMBench 主要聚焦於單次任務中的證據組合，未涵蓋長期記憶的保存與更新，亦未模擬真實Agent在互動過程中持續累積與使用記憶的情境。這意味著基準仍有擴充的空間。  

**研究者可直接使用此基準檢視與改進多模態記憶系統**  
基準已於 HuggingFace 公開（https://huggingface.co/datasets/HuacanChai/SMMBench），研究團隊鼓勢將其作為評估新架構、新訓練策略或新檢索方法的標準工具，以針對性提升模型在來源分散多模記憶上的表現。  

🔗 論文連結  
📝 SMMBench: A Benchmark for Source-Distributed Multimodal Agent Memory  
👤 Huacan Chai, Yukai Wang, Yingxuan Yang, Dan Peng, Yuanyi Song (Shanghai Jiao Tong University; OPPO)  
🔗 https://arxiv.org/abs/2605.15710  

你在開發多模態 Agent 時，是否曾遇過「明明有線索卻找不齊」的困境？歡迎在留言區分享你的經驗與看法 👇  

#AI #Multimodal #AgentMemory #Benchmark #SMMBench #ShanghaiJiaoTong #OPPO #Research #MachineLearning
