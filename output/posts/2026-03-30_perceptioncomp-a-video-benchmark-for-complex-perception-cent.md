---
title: "PerceptionComp: A Video Benchmark for Complex Perception-Centric Reasoning"
source: ChatPaper/AI
url: https://arxiv.org/abs/2603.26653
score: 106
model: gpt-4o-free
generated_at: 2026-03-31T00:33:10.210381
---

📌 【Tsinghua 等最新研究】PerceptionComp：挑戰 MLLM 的長時程感知推理  

你以為現在的多模態大模型已經能看懂長視頻？PerceptionComp 說不：單幀不夠，得跨時間拼湊才能答對。  

🤔 **現有基準無法檢驗長時程、多步驟的感知推理**  
現行視頻理解基準多聚焦於單幀或短片段的識別，無法考察模型是否需要同時利用多個時間點的視覺線索、以及在合取或序列邏輯下進行概念組合。這留下了一個重要的評估空白：當任務要求跨多個瞬間、結合物件、屬性、關係、位置、動作與事件時，模型的表現究竟如何？  🧪 **手動標註的 1,114 個複雜問題覆蓋 279 部多領域視頻**  PerceptionComp 由人工逐題標註，包含 1,114 個高度複雜的選擇題，對應 279 部來自城市步行、室內別墅、遊戲及極限戶外運動等領域的視頻。每個問題設計為必須同時利用多個時間點的視覺證據，並滿足合取或序列的組合約束，涵蓋物件、屬性、關係、位置、動作、事件等感知子任務，同時考慮語義識別、視覺對應、時間推理與空間推理等能力。  

📊 **人類受試者需更長思考時間，禁止回放時準確率降至近隨機水準**  
人類研究顯示，答題所需時間顯著高於既有基準；當禁止重複觀看視頻時，人類準確率驟降至 18.97%，幾乎等於隨機猜測。這說明該基準確實考驗了需要多次感知步驟與較長思考的推理能力。  

🤖 **最先進的多模態大語言模型在該基準上表現顯著落後**  
在五選一設定下，評估中的最佳模型 Gemini-3-Flash 僅達到 45.96% 準確率；開源模型則普遍低於 40%。與現有基準相比，這些模型在 PerceptionComp 上的差距凸顯了當前在長時程、組合式感知推理方面的不足。  

⚠️ **基準設計聚焦於感知推理，未涵蓋更高層次的認知任務**  
PerceptionComp 專門測試跨時間的視覺識別與關係組合，不包含需要外部知識、常識推理或語言生成等更高層次的認知挑戰。因此，模型在此基準上的弱點主要反映在感知與時間空間推理上，而非其他認知維度。  

🎯 **未來研究可從強化時間感知與概念組合入手**  
結果表明，提升模型在多幀視覺對應、時間序列建模以及合取/序列約束下的概念組合能力，將是縮小與人類表現差距的關鍵方向。將此基準作為評估工具，有助於引導社群朝向更具感知推理韌性的多模態系統發展。  

🔗 **論文連結**  
📝 PerceptionComp: A Video Benchmark for Complex Perception-Centric Reasoning  
👤 Shaoxuan Li, Zhixuan Zhao, Hanze Deng, Zirun Ma, Shulin Tian (Tsinghua University; University of Washington; Nanyang Technological University)  
🔗 https://arxiv.org/abs/2603.26653  

你在使用多模態模型處理長視頻時，是否也遇到過需要來回翻幀才能確認細節的情況？歡迎在留言區分享你的經驗與看法 👇  

#AI #VideoUnderstanding #MultimodalMLLM #PerceptionReasoning #Tsinghua #NanyangTU #UW #Benchmark #Gemini #MLLM #ARXIV
