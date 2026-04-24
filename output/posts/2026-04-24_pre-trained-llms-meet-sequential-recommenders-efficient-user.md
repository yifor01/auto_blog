---
title: "Pre-trained LLMs Meet Sequential Recommenders: Efficient User-Centric Knowledge Distillation"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2604.21536
score: 101
model: tencent/hy3-preview:free
generated_at: 2026-04-24T20:08:31.562376
---

📌 【Sber AI Lab 新研究】LLM 強化推薦系統，線上推論零成本

推薦系統追求精準度，LLM 擁有強大的語意理解能力，但將兩者結合的常見做法往往導致線上推論成本過高，讓許多工程團隊在落地時面臨兩難。這篇來自 Sber AI Lab 與俄羅斯頂尖學府的合作研究，提出了一個不需要在線跑 LLM 的知識蒸餾方案。

🤔 **序列推薦懂時間，卻不懂語意**

序列推薦系統（Sequential Recommenders）在捕捉使用者點擊、購買的時間序列行為上表現出色，但往往只能看到「互動模式」，難以理解背後豐富的「使用者語意」。雖然大型語言模型（LLM）具備強大的推理能力，能生成深度的使用者理解，但直接將 LLM 部署在推薦系統的即時推論端，其運算成本與延遲往往是現有架構難以承受的。

🧪 **用 LLM 生成文字 Profile，再蒸餾進輕量模型**

這項研究提出了一種創新的知識蒸餾（Knowledge Distillation）方法。首先，利用預訓練好的 LLM 離線生成文字化的使用者 Profile，接著將這些文字蘊含的知識注入到傳統的序列推薦模型中。關鍵在於，這個過程不需要對 LLM 進行微調（Fine-tuning），也不需要修改現有的推薦模型架構。

 **維持傳統模型效率，補足語意理解短板**

實驗結果顯示，這種方法成功保留了傳統序列推薦模型的高效率推論特性。在服務上線時，完全不需要呼叫 LLM 進行推論，卻能讓模型具備 LLM 等級的語意理解能力。這解決了過往「要效果就得犧牲速度」的痛點，實現了效率與效果的平衡。

💡 **解耦離線生成與線上推論，降低落地門檻**

這項技術的核心價值在於其工程可行性。由於不需要架構修改，現有的推薦系統只需透過離線處理，就能獲得 LLM 的知識加持。這種「知識蒸餾」而非「聯合推論」的設計，讓推薦系統能專注於處理高併發的線上請求，同時享受 LLM 帶來的語意紅利。

⚠️ **依賴預訓練 LLM 的離線生成品質**

研究的主要限制與依賴點在於預訓練 LLM 生成 Profile 的品質。此外，由於是在離線階段生成知識，對於使用者行為發生劇烈變化的即時反應能力，可能會受到 Profile 更新頻率的限制。

🎯 **產品化推薦系統的務實選擇**

對於正在探索 LLM 落地的推薦團隊，這提供了一個極具參考價值的範式。不需要昂貴的線上 GPU 資源來跑 LLM，也不需要重訓複雜的推薦模型，只需專注於如何設計更好的 Prompt 來生成高品質的使用者 Profile，並透過蒸餾讓輕量模型學會這些知識。

🔗 **論文連結**
📝 Pre-trained LLMs Meet Sequential Recommenders: Efficient User-Centric Knowledge Distillation
👤 Nikita Severin, Danil Kartushov, Vladislav Urzhumov, Vladislav Kulikov, Oksana Konovalova
🏛️ Independent researcher; Sber AI Lab; Innopolis University; HSE University; ITMO University; AIRI
🔗 論文：https://arxiv.org/abs/2604.21536

你們團隊在推薦系統中引入 LLM 時，遇到最大的效能瓶頸是什麼？歡迎在留言區交流 👇

#推薦系統 #LLM #KnowledgeDistillation #SberAI #資訊檢索 #MachineLearning #AI工程
