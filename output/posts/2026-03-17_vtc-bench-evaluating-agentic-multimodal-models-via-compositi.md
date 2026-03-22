---
title: "VTC-Bench: Evaluating Agentic Multimodal Models via Compositional Visual Tool Chaining"
source: ChatPaper/AI
url: https://arxiv.org/abs/2603.15030
score: 108
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-17T18:42:46.900881
---

📌 **AI 視覺工具鍊評測新標竿：VTC-Bench 揭示 MLLM 的關鍵限制**

當 AI 模型能看圖說故事，下一步是讓它們真正「做事」。VTC-Bench 橫空出世，用 32 種視覺工具鍊組合，測試當前最強大的多模態模型，結果令人驚訝。

🤔 **為什麼 AI 看得見，卻做不到？**

過去兩年，MLLM 從單純的圖像問答進化到能使用外部工具。但研究者發現，現有評測標準存在根本缺陷：工具種類太少、使用場景太簡單，無法反映真實世界的複雜需求。

🧪 **32 種 OpenCV 工具，680 個認知層級問題**

VTC-Bench 的設計哲學很簡單：如果 AI 要真正幫人類完成視覺任務，它必須能像專業軟體工程師一樣，組合不同的工具函式。

- 32 種 OpenCV 基礎視覺操作（從圖像濾波到幾何變換）
- 680 個精心設計的問題，橫跨九個認知層級
- 每個問題都有標準答案路徑，確保評測客觀

💡 **Gemini-3.0-Pro 只拿到 51%？**

在 19 個頂尖 MLLM 上的測試結果令人震驚：

- 最佳表現者 Gemini-3.0-Pro 也只達到 51% 正確率
- 多數模型無法適應多樣化的工具組合
- 遇到複雜任務時，模型傾向使用熟悉的少數工具，而非最佳方案

這意味著即使是最先進的模型，在面對真實世界的視覺工具鍊問題時，表現遠不如人類專業人士。

⚠️ **三大關鍵限制被揭露**

1. **工具泛化能力差**：無法將學到的工具使用推廣到未見過的操作
2. **組合能力不足**：無法有效組合多種工具完成複雜任務
3. **計畫執行障礙**：無法制定高效的多步驟執行計畫

🎯 **對開發者的實際意義**

VTC-Bench 不只是一個評測工具，更是一個開發指南。它告訴我們：

- 當前 MLLM 在視覺工具使用上的根本限制
- 開發更強大視覺代理模型需要突破的方向
- 如何設計更實用的多模態 AI 應用

🔗 **論文連結**
📝 VTC-Bench: Evaluating Agentic Multimodal Models via Compositional Visual Tool Chaining
👤 Xuanyu Zhu, Yuhao Dong, Rundong Wang, Yang Shi, Zhipeng Wu
🏢 PKU; NTU; USTC; CQU; NUDT; CASIA; Meituan
🔗 論文：arxiv.org/abs/2603.15030

當 AI 能看懂圖片，下一步就是讓它們真正「動手做事」。VTC-Bench 為這個目標提供了嚴格的評測標準。

你認為多模態 AI 最需要突破的瓶頸是什麼？歡迎討論 👇

#AI #MLLM #ComputerVision #Multimodal #工具使用 #深度學習 #視覺推理 #技術評測
