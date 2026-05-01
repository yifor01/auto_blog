---
title: "PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2604.28123
score: 125
model: tencent/hy3-preview:free
generated_at: 2026-05-01T19:33:32.133509
---

📌 【港科大廣州/清華等團隊】PRISM 緩解多模態 RL 分佈漂移問題

現行多模態大模型後訓練標準流程，藏著被忽視的隱形成本。
監督微調（SFT）帶來的分佈漂移，會雙殺模型原有能力與後續強化學習效果。
新框架PRISM插入對齊階段，8B模型準確率最高提升6個百分點。

🤔 **標準後訓練流程的隱形成本：SFT帶來的分佈漂移**
大型多模態模型（LMMs）的標準後訓練流程為「監督微調（SFT）→ 帶可驗證獎勵的強化學習（RLVR）」，但SFT會引入分佈漂移，既無法保留模型原有能力，也無法忠實貼合監督數據分佈。這個問題在多模態推理任務中會被放大：感知錯誤與推理失敗會產生不同的漂移模式，在後續RL階段疊加，進一步拉低最終效果。

🧪 **三階段 Pipeline + 黑箱對抗蒸餾，解耦感知與推理訊號**
團隊提出PRISM三階段後訓練框架，核心是在SFT與RLVR之間插入顯式分佈對齊階段，緩解漂移問題。對齊階段基於線上策略蒸餾（OPD）原則，將對齊任務轉化為策略模型與混合專家（MoE）判別器的黑箱、響應級對抗遊戲：MoE判別器包含專門的感知專家與推理專家，可輸出解耦的矯正訊號，引導策略模型貼近監督分佈，且全程不需要存取教師模型的內部輸出概率（logits）。
數據層面，團隊先用1.26M公開示範數據完成SFT初始化，再從Gemini 3 Flash整理出113K針對最難未解問題的高質量示範數據，包含密集視覺定位與逐步推理內容，專門用於分佈對齊階段。

 **Qwen3-VL 4B/8B 準確率分別提升4.4/6.0個百分點**
實驗基於Qwen3-VL模型驗證，PRISM相比SFT到RLVR的基線，平均準確率提升顯著：4B模型提升+4.4個百分點，8B模型提升+6.0個百分點。效果具備通用性，兼容GRPO、DAPO、GSPO等多種RL算法，在多個多模態基準測試中均保持穩定提升。

💡 **解耦感知與推理訊號是對齊有效的核心原因**
PRISM針對多模態任務的特性，將感知與推理的錯誤漂移分開處理：MoE判別器的專門專家可針對視覺感知錯誤、邏輯推理錯誤分別給出針對性矯正訊號，避免兩類錯誤的漂移在後續RL中疊加放大。黑箱對抗蒸餾的設計不需要教師模型內部logits，也降低了對齊階段的部署門檻。

⚠️ **公開資訊未提及明確研究限制**
目前公開的論文摘要與相關資訊中，未明確列出本研究的方法限制或實驗邊界。團隊已開源全部程式碼、113K高質量示範數據與模型檢查點，可供社群進一步驗證與擴展。

🎯 **多模態後訓練可直接復用開源資源**
對於多模態大模型研發團隊，PRISM的三階段Pipeline可直接復用，在SFT與RLVR之間插入分佈對齊階段，能有效緩解漂移問題、提升最終效果。團隊開源的113K高質量示範數據也可作為多模態任務的優質訓練素材，降低資料整理成本。

🔗 **論文連結**
📝 論文標題：PRISM: Pre-alignment via Black-box On-policy Distillation for Multimodal Reinforcement Learning
👤 作者：Sudong Wang, Weiquan Huang, Xiaomin Yu, Zuhao Yang, Hehai Lin
🏫 所屬機構
