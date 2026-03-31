---
title: "Beyond Language: Grounding Referring Expressions with Hand Pointing in Egocentric Vision"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.26646
score: 118
model: gpt-4o-free
generated_at: 2026-03-31T00:20:43.708435
---

📌 【Apple 等機構最新研究】手勢+語音：EgoPoint‑Ground 讓 AI 看懂指向

你以為 AI 只靠文字就能找到物體？在第一人稱視角中，手指點動才是最自然的指示方式——但現有模型卻常忽略這個關鍵線索。

🤔 **手勢與語音結合的指涉表達在真實互動中司空見慣，但傳統視覺定位（VG）幾乎只依賴文字描述，導致語義歧義難以克服**

🧪 **研究團隊構建了 EgoPoint‑Ground，首個大規模以第一人稱視角為基礎的多模態數據集，包含超過 15k 個互動樣本，提供手標Bounding Box 配對與密集語義標註**

 **在該基準上，提出的 SV-CoT 框架將定位問題轉換為結構化的 Visual Chain‑of‑Thought 推理，相較於現有主流 MLLM 與 SOTA VG 模型，取得 11.7% 的絕對提升**

💡 **SV-CoT 透過先解析手勢幾何資訊，再結合語義描述進行逐步推理，有效減少純文字模型在複雜場景中的語義混淆，使代理能更準確理解多模態實體意圖**

⚠️ **目前僅報告基準結果，未涉及長時程自我驅動環境中的泛化表現，數據集雖大但仍聚焦於特定手勢與語音模式**

🎯 **對於構建手勢感知的具身代理、AR/VR 互動或機器人協作系統，該方法提供了一種可直接適用的結構化推理範式，且數據與程式碼將開放供社區使用**

🔗 **論文連結**  📝 Beyond Language: Grounding Referring Expressions with Hand Pointing in Egocentric Vision  
👤 Ling Li, Bowen Liu, Zinuo Zhan, Peng Jie, Jianhui Zhong (Tsinghua University; Dalian University of Technology; Northwestern Polytechnical University; Apple)  
🔗 https://arxiv.org/abs/2603.26646  

你在開發手勢或多模態交互系統時，會如何結合語言與手勢資訊？歡迎留言討論 👇  

#AI #ComputerVision #EgocentricVision #VisualGrounding #Multimodal #Apple #Tsinghua #GestureRecognition #MLLM
