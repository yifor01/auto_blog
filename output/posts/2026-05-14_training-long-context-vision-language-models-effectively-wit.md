---
title: "Training Long-Context Vision-Language Models Effectively with Generalization Beyond 128K Context"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.13831
score: 123
model: tencent/hy3-preview:free
generated_at: 2026-05-14T20:22:29.204911
---

📌 長上下文 VLMs 訓練新法  
你以為只需要更長的文字就能讓模型看懂長文檔？實際上，資料如何混合才是關鍵。  

🤔 **長文檔理解需求激增，但訓練食譜仍缺乏系統指引**  
現代視覺語言模型被期望處理長文檔、長影片與多輪工具使用，然而長情境續訓的具體做法缺乏系統化探索，特別是如何設計與平衡長情境資料混合。  

🧪 **從 32K 到 128K 的續訓消融實驗，聚焦長文檔 VQA 與 OCR 轉錄**  
研究以 Qwen2.5‑VL‑7B 為基礎，將情境長度從 32K 延伸至 128K，針對長文檔資料進行大規模消融。實驗首次證實，長文檔視覺問答（VQA）在提升長情境能力上遠勝於純 OCR 轉錄資料。  

🔑 **平衡長度分布勝過針對性長文資料，檢索是主要瓶頸，純長文 VQA 能保留短文能力**  
三個主要發現如下：  
1. 在序列長度分布上，資料長度的均衡混合比僅聚焦於目標長度（例如 128K）的資料更有效，說明長情境能力需要在不同長度與位置上進行通用的關鍵資訊擷取。  
2. 檢索任務仍是效能瓶頸，因此資料混合應該偏向檢索導向，並適量加入推理資料以增加任務多樣性。  
3. 使用純長文檔 VQA 進行續訓，在不額外混合短情境資料的情況下，仍能保留原本的短情境表現。  

💡 **為何平衡混合與檢索導向資料能提升可泛化的關鍵資訊擷取**  
當資料涵蓋多種長度時，模型學會的不是死記特定位置的 token，而是一種能在任意長度中定位關鍵訊息的檢索策略。這種策略同時受益於少量推理資料所帶來的任務多樣性，使得模型在未見過的更長情境（256K、512K）以及網頁多模態針尖檢索、視覺文本壓縮與長影片理解等任務上仍能保持強效能，而無需額外任務特定訓練。  

⚠️ **僅在 7B 模型上驗證，資料規模與實際多模態任務覆蓋仍有待擴充**  
本研究的結論基於單一 7B 參數模型與 5B 權杖的續訓預算，尚未在更大規模模型或更多樣化的多模資料集上進行驗證，長期使用效果與更複雜代理工作流的適用性仍需後續工作補充。  

🎯 **使用僅 5B 權杖的 MMProLong 食譜，即可在 256K/512K 長文檔上保持強效能**  
根據上述發現，團隊提出 MMProLong：在僅 5B 權杖的預算下，對 Qwen2.5‑VL‑7B 進行長情境續訓。該模型在長文檔 VQA 上提升 7.1%，並在未見過的 256K 與 512K 情境下依舊表現優秀，同時能泛化至網頁多模態針尖檢索、視覺文本壓縮與長影片理解等任務，無需額外監督訓練。  

🔗 **論文連結**  
📝 Training Long-Context Vision-Language Models Effectively with Generalization Beyond 128K Context  
👤 Zhaowei Wang, Lishu Luo, Haodong Duan, Weiwei Liu, Sijin Wu (HKUST; ByteDance Seed)  
🔗 https://arxiv.org/abs/2605.13831  

你的長情境訓練策略是否已經檢視資料混合的平衡？歡迎在留言區分享經驗與疑問 👇  

#AI #VisionLanguage #LongContext #MMProLong #HKUST #ByteDance #MachineLearning #CVPR #模型訓練 #資料混合
