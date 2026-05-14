---
title: "Scaling Retrieval-Augmented Reasoning with Parallel Search and Explicit Merging"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.13534
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-14T20:49:55.135269
---

📌 【USTC & 腾讯】MultiSearch：並行多查詢提升推理

你以為一次檢索就能拿到所有答案？實際上，單一查詢常帶來高雜訊，導致推理走偏。本文提出 MultiSearch，讓模型一次產生多個查詢並行檢索，再透過顯式合併提升訊噪比。

🤔 **單一檢索易產生噪聲，限制推理準確度**  
現有的檢索增強推理方法通常在每一步 reasoning 只產生一個查詢，檢索結果的覆蓋範圍有限，且容易引入無關資訊。訊噪比（SNR）低不僅降低答案正確率，還可能觸發額外的推理步驟，浪費計算資源。

🧪 **多查詢並行檢索＋顯式合併的強化學習框架**  
論文提出 MultiSearch，在每一個 reasoning 步驟中：  
1. 產生來自不同視角的多個查詢；  
2. 並行執行外部檢索，擴大相關資訊的獲取範圍；  
3. 在顯式的合併階段，對檢索結果進行整合與精煉，以提升訊噪比。  
同時設計了一個多過程獎勵的強化學習目標，同步優化多查詢生成與資訊合併兩個環節。

📊 **在七個問答基準上持續優於基線**  
實驗顯示，MultiSearch 能提升檢索的訊噪比，進而在七個問答基準上取得比現有方法更好的推理表現。具體提升幅度未在摘要中給出，但作者指出改進具有統計顯著性。

💡 **訊噪比提升的關鍵在於資訊的廣度與精煉**  
透過並行多查詢，模型不再依賴單一檢索結果，減少了因某個查詢偏誤而導致的錯誤傳播。顯式合併則像是一個「過濾器」，去除噪聲、保留高相關內容，使後續推理步驟能站在更乾淨的知識基礎上。

⚠️ **實驗主要聚焦於問答任務，長期與跨領域效果尚待驗證**  
論文僅報告了七個問答基準的結果，未涉及其他類型的推理任務或長對話情境。此外，強化學習的訓練成本與多查詢的計算開銷在文中未作詳細分析，實務部署時需要評估這些 trade‑off。

🎯 **工程師可直接採納的設計方案**  
- 在現有的 agent‑based retrieval 流程中，加入多查詢生成模組（可用 prompt 工程或小型策略網路）。  
- 檢索後加入一個顯式的資訊合併步驟，例如基於相關性得分的加權平均或簡單的 reranker。  
- 使用獎勵函式同時鼓勵查詢多樣性與合併後的任務準確度，可透過標準的 Policy Gradient 或 PPO 進行優化。

🔗 **論文連結**  
📝 Scaling Retrieval-Augmented Reasoning with Parallel Search and Explicit Merging  
👤 Jiabei Liu, Wenyu Mao, Junfei Tan, Chunxu Shen, Lingling Yi (University of Science and Technology of China; WeChat Technical Architecture Department, Tencent Inc.)  
🔗 https://arxiv.org/abs/2605.13534  

你在開發 RAG 或 Agent 系統時，是否曾嘗試過多查詢策略？歡迎在留言區分享你的經驗與想法 👇

#AI #RetrievalAugmentedGeneration #MultiSearch #强化学习 #腾讯 #USTC #GenAI #问答系统
