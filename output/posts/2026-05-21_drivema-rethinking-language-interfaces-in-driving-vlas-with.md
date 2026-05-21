---
title: "DriveMA: Rethinking Language Interfaces in Driving VLAs with One-Step Meta-Actions"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.21273
score: 116
model: tencent/hy3-preview:free
generated_at: 2026-05-21T20:36:43.687764
---

📌 【上海智源等最新研究】用「一步 Meta‑Action」取代冗長語言推理，DriveMA 在 Waymo 挑戰賽上創新 SOTA  

🎣 你以為讓自駕模型「說出」推理過程就一定更智慧？實際上，這樣的語言介面可能卻成為效能的瓶頸。  

🤔 **語言推理介面的三個實務瓶頸**  
當前 Driving VLAs 常以自然語言作為中間推理步驟，但取得高品質標註困難、緊湊模型難以產生與理解長鏈推理、以及推理延遲顯著增加，限制了實際部署。  

🧪 **以專家軌跡自動導出的一步 Meta‑Action**  
研究團隊提出一種低熵的語義決策標記——one‑step meta‑action。它能直接從專家軌跡中自動產生，提供決策 grounding 同時保持簡浒，因而具備可擴展的監督訊號與可靠的軌跡條件。  

🔬 **DriveMA：監督學習 + 信用分配強化學習**  
基於此介面，DriveMA 結合動作導向的監督訓練與逐輪信用分配 RL 框架，同時優化 meta‑action 正確性、軌跡品質以及軌跡‑meta‑action 一致性。實驗使用 2B 與 4B 參數規模模型在 Waymo End‑to‑End Driving Challenge 上評估。  

💡 **核心發現：新 SOTA 與更佳的實務權衡**  
- 2B 版 DriveMA 達到 Rater Feedback Score (RFS) 8.060，創下該挑戰賽新紀錄。  
- 4B 版進一步提升至 8.079 RFS。  
- 在 NAVSIM 上亦獲得具競爭力的表現。  
消融實驗顯示，相較於冗長語言推理或更細粒度的動作序列，one‑step meta‑action 在表達力、可預測性與推理效率間提供了更佳的實務取捨。  

⚠️ **研究限制**  
- 本工作主要基於 Waymo 與 NAVSIM 數據集，其他真實駛入環境的適用性尚需驗證。  
- 未探討不同 meta‑action 設計空間的極限。  
- 代碼與模型將於論文發佈後開放，目前仍屬預公開狀態。  

🎯 **實務啟示：為端到端自駕系統提供更輕量的語言介面**  
對於工程師而言，採用一步 meta‑action 可在不犧牲決策解釋性的前提下降低標註成本與推理延遲，適合資源受限的車載平台。未來可探索將此介面擴展至多任務或跨場景的決策規劃。  

🔗 **論文連結**  
📝 DriveMA: Rethinking Language Interfaces in Driving VLAs with One-Step Meta-Actions  
👤 Weicheng Zheng, Yixin Huang, Qiao Sun, Derun Li, Hang Zhao (Shanghai Qi Zhi Institute; Tsinghua University; Tongji University)  
🔗 https://arxiv.org/abs/2605.21273  

你認為在自駕系統中，「說少做多」的介面是否是未來趨勢？歡迎在留言區分享你的看法 👇  

#AI #自駕 #端到端 #DriveMA #Waymo #CVPR #上海智源 #清華大學 #同濟大學 #機器學習 #視覺語言行動模型
