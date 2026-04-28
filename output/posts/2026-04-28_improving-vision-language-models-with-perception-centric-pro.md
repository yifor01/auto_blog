---
title: "Improving Vision-language Models with Perception-centric Process Reward Models"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2604.24583
score: 120
model: tencent/hy3-preview:free
generated_at: 2026-04-28T20:08:57.222906
---

📌 【人大&字節】用 Perceval 揪出 VLM 幻覺

現有的 VLM 強化學習只看結果對錯，卻不管中間推理哪裡出錯。這種「只看分數不看過程」的訓練方式，讓模型很容易在細節上產生幻覺。

🤔 **現有 RLVR 只看結果，無法診斷推理過程中的感知錯誤**

強化學習結合可驗證獎勵（RLVR）雖然提升了視覺語言模型（VLM）的推理能力，但這種「結果級（Outcome-level）」的監督太過粗糙。當模型看圖說故事時，如果答案最後是錯的，我們很難知道它是哪一句話、哪一個 token 開始產生視覺幻覺。這就像只管考試分數，不管錯題原因，自然難以修正。

🧪 **Perceval：逐句比對文字聲明與視覺證據的 PRM**

由中國人民大學、Bytedance、UCSD 與港科大團隊提出的 Perceval，是一個以「感知為中心」的過程獎勵模型（PRM）。它的運作邏輯相當直觀但技術上很精細：

1. **提取聲明**：從模型的回應中提取出與圖像相關的具體聲明。
2. **視覺比對**：將這些聲明與圖像中的視覺證據進行逐一比對。
3. **Token 級定位**：找出包含感知錯誤的具體區段（Spans），實現 Token 級別的錯誤定位。

 **Token 級別的細粒度監督，顯著提升多個 VLM 基準表現**

Perceval 不僅是一個評測工具，更被整合進 RL 訓練流程。相較於傳統 GRPO 演算法使用序列級的優勢（Sequence-level advantages），Perceval 能針對被識別出的幻覺區段施加 Token 級別的懲罰。

實驗結果顯示，這種細粒度監督在多個領域的基準測試中，都為經過 RL 訓練的推理型 VLM 帶來了顯著的性能提升。

💡 **從訓練到推理：Perceval 實現測試時擴展**

除了改進訓練，Perceval 在推理階段（Inference）也展現了強大的實用性：

- **錯誤截斷**：當檢測到回應中有錯誤部分，直接截斷。
- **自我修正**：讓模型直接重新生成，或是引導模型反思先前的錯誤。
- **測試時擴展**：這個「檢測-修正」的過程可以重複多次，效果優於傳統的多數投票（Major Voting）策略。

⚠️ **依賴高品質感知數據，跨領域泛化能力待驗證**

論文雖然展示了強大的效果，但仍需注意其限制。Perceval 的訓練依賴「感知密集型」的監督數據，這意味著數據的品質與覆蓋範圍將直接影響模型表現。此外，雖然在跨領域基準上有效，但在極端場景或全新領域的泛化能力仍需更多實證。

🎯 **針對性懲罰幻覺區段，結合反思機制提升準確率**

對於正在做 VLM 後訓練（Post-training）的工程師來說，這提供了一個明確的技術路徑：

- 不要只依賴最終答案的對錯來回饋模型，嘗試引入過程獎勵。
- 在推理部署時，可以設計「檢測-反思」的循環架構，利用 PRM 提升輸出的可靠性。
- 團隊已承諾開源代碼與數據，這對於想要復現或改進 RLVR 流程的開發者來說是極佳的資源。

🔗 **論文連結**
📝 Improving Vision-language Models with Perception-centric Process Reward Models
👤 Yingqian Min, Kun Zhou, Yifan Li, Yuhuan Wu, Han Peng
🏫 Renmin University of China; Bytedance; UC San Diego; HKUST
🔗 論文：https://arxiv.org/abs/2604.24583
💻 GitHub：https://github.com/RUCAIBox/Perceval

你覺得 VLM 的幻覺問題，是靠更好的訓練數據解決，還是靠這種過程監督的機制更有效？歡迎討論 👇

#VLM #ComputerVision #ReinforcementLearning #AI研究 #Bytedance #多模態 #幻覺問題
