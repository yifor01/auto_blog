---
title: "Meet AntAngelMed: A 103B-Parameter Open-Source Medical Language Model Built on a 1/32 Activation-Ratio MoE Architecture"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/12/meet-antangelmed-a-103b-parameter-open-source-medical-language-model-built-on-a-1-32-activation-ratio-moe-architecture/
score: 109
model: tencent/hy3-preview:free
generated_at: 2026-05-13T20:40:50.862173
---

📌 **AntAngelMed：103B 參數開源醫療 MoE 模型**  

你以為只有龐大的密集模型才能掌握醫學知識？AntAngelMed 卻僅啟用 61 億參數，聲稱可媲美 40B 密集模型的表現，這到底是怎麼做到的？

🤔 **醫療領域需要更大知識容量，但算力成本卻是瓶頸**  
隨著臨床決策支援、醫療報告生成等應用對語言模型的需求增加，研究者希望擁有更廣泛的醫學知識庫。然而，傳統密集模型要提升參數規模就意味著指數級的計算成本，難以在資源有限的環境中部署。

🧪 **基於 1/32 啟用率的 MoE 架構，繼承 Ling‑flash‑2.0 基礎**  
AntAngelMed 總參數達 103B，採用 Mixture‑of‑Experts (MoE) 設計，啟用比例為 1/32，即每次推理僅激活約 6.1B 參數。該模型在 inclusionAI 的 Ling‑flash‑2.0 基礎上進行改進，並參照所謂的 Ling Scaling Laws 進行縮放。文中提到的具體優化包括：專家粒度的細緻調整、共享專家比例的調校、注意力平衡機制、無輔助損失的 Sigmoid 路由、多標記預測 (MTP) 層、QK‑Norm 以及僅對部分注意力頭應用的 Partial‑RoPE。

🚀 **聲稱可達 7× 效率提升，6.1B 活化參數匹配約 40B 密集模型**  
根據研究團隊的說明，上述設計讓小啟用率的 MoE 模型在效率上可較同規模的密集架構最高提升 7×。也就是說，僅有 6.1B 活化參數的 AntAngelMed 在理論上能夠達到約 40B 密集模型的表現；隨著生成長度增加，其速度優勢亦可進一步擴大至 7× 或更高。

💡 **三階段訓練流程旨在逐層註入通用與醫療知識**  
文章指出 AntAngelMed 採用三階段訓練過程，目的是先學習通用語言能力，再逐步引入醫療領域的專業知識，最後進行任務特定的微調。具體的資料規模、訓練時長或每階段的目標未在提供的摘要中說明。

⚠️ **未披露具體醫學基準測試結果，僅提供效率估算**  
目前可見的資訊僅強調模型架構與推理效率的優勢，未給出在公開醫療基準（如 MedQA、MMLU‑clinical 等）上的具體分數，亦未說明訓練資料的規模與來源，因此實際醫療任務表現仍需進一步驗證。

🎯 **對工程師與研究者的啟示：開源高效 MoE 為醫療 AI 提供新選擇**  
- 若你需要在算力受限的環境中部署大規模醫療語言模型，AntAngelMed 的 1/32 啟用率 MoE 設計展示了如何在保持知識容量的同時大幅降低運算成本。  
- 開源特性使社群能夠在現有基礎上進行微調、擴展專家結構或探索其他路由策略。  
- 未來工作可著重於在標準醫療基準上進行評估，以及訪談三階段訓練的細節，以驗證其聲稱的效能與實際臨床適用性。

🔗 **論文連結**  
📝 Meet AntAngelMed: A 103B-Parameter Open-Source Medical Language Model Built on a 1/32 Activation-Ratio MoE Architecture  
👤 Asif Razzaq (MarkTechPost 報告)  
🔗 https://www.marktechpost.com/2026/05/12/meet-antangelmed-a-103b-parameter-open-source-medical-language-model-built-on-a-1-32-activation-ratio-moe-architecture/  

你對這種高啟用率效率的 MoE 模型有什麼看法？歡迎在留言區分享你的想法與經驗 👇  

#AI #醫療AI #MoE #開源模型 #AntAngelMed #大型語言模型 #機器學習 #MarkTechPost
