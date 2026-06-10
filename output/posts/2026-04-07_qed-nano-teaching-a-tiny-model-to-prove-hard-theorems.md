---
title: "QED-Nano: Teaching a Tiny Model to Prove Hard Theorems"
source: ChatPaper/AI
url: https://arxiv.org/abs/2604.04898
score: 126
model: gpt-4o-free
generated_at: 2026-04-07T13:07:20.630451
---

📌 【開源 4B 小模型】破解高階數學證明

你以為突破 IMO 金級水準必須依賴千億參數的閉源巨獸？CMU 與 Hugging Face 團隊用僅 4B 參數的模型，給出了一個反直覺的答案。

🤔 **閉源系統壟斷高階推理，開源小模型能否破局？**

近年閉源 AI 在 2025 國際數學奧林匹亞 (IMO) 展現金牌級證明能力，但背後的訓練管線高度保密，且嚴重依賴大型內部模型與複雜脚手架。這不僅讓部署成本居高不下，更使學術界難以複製或針對性改進。研究團隊直接切中產業痛點：能否讓輕量開源模型，在奧數級高難度證明上達到競爭力？

🧪 **三階段微調管線：風格蒸馏、評分規則 RL 與推理快取**

QED-Nano 的訓練並非盲目堆疊資料，而是採用精準的三階段後訓練 (Post-training) 架構：
1. 監督式微調 (SFT)：從 DeepSeek-Math-V2 蒸馏優質的數學證明書寫風格與邏輯結構。
2. 強化學習優化：引入基於評分規則 (Rubric-based rewards) 的 RL，引導模型輸出符合嚴格數學規範的步驟。
3. 推理快取擴展：突破傳統上下文限制，將長證明拆解為迭代式總結與精煉循環，強化測試時推理能力。

📊 **4B 參數效能超越 120B 開源模型，逼近頂級閉源系統**

實驗結果顯示，QED-Nano 在數學證明生成任務上，表現已全面超越 Nomos-1 與 GPT-OSS-120B 等大型開源模型，並成功逼近 Gemini 3 Pro 的水準。更關鍵的是，其推論成本僅為大型模型的一小部分，證明參數規模並非決定高階推理能力的唯一變數。

💡 **「總結與精煉」循環，釋放測試時計算潛力**

本研究最核心的技術洞察在於第三階段的設計。面對冗長且易出錯的數學證明，模型不再依賴單次長上下文生成，而是利用推理快取機制，將解題過程轉化為動態的「總結與精煉」迭代。這種設計巧妙結合了測試時計算 (Test-time Compute) 趨勢，讓小模型能在推論階段動態分配計算資源，逐步修正邏輯漏洞，而非受制於固定權重的單次預測。

⚠️ **聚焦數學證明領域，具體量化分數與泛化邊界待公開**

根據目前提供的摘要資訊，本研究主要針對奧數級數學證明進行優化，尚未探討此管線在其他邏輯推理或代碼生成任務的泛化能力。此外，摘要未列出與對比模型的具體得分差距與錯誤模式分析，推理快取機制在處理極端複雜證明時的計算開銷與效能衰減，仍屬需要後續追蹤的工程細節。

🛠️ **完整開源 Pipeline，低成本高階推理的實戰藍圖**

團隊已完整釋出 QED-Nano 與 SFT 版本模型、FineProofs-SFT 與 FineProofs-RL 資料集，以及全套訓練與評估程式碼。這為工程與研究社群提供了一套高可複製性的微調範本：驗證了「精準風格蒸馏、結構化 RL 獎勵設計，加上測試時擴展策略」的組合拳，足以讓邊緣裝置或低成本伺服器執行高階推理。對於正在評估模型輕量化部署或自研垂直領域推理管線的團隊，此專案的程式碼結構與資料清洗邏輯極具參考價值。

🔗 **論文連結**
📝 QED-Nano: Teaching a Tiny Model to Prove Hard Theorems
👤 Yuxiao Qu, Amrith Setlur, Jasper Dekoninck, Edward Beeching (LM-Provers @ CMU; Hugging Face; ETH Zurich; Project Numina)
🔗 論文：https://arxiv.org/abs/2604.04898

你團隊在推論成本與模型效能之間，通常如何取捨？歡迎分享你的微調經驗或部署觀察 👇

#AI #OpenSource #MachineLearning #ReinforcementLearning #TestTimeCompute #數學推理 #HuggingFace #CMU #模型微調 #QEDNano
