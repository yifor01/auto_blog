---
title: Fix evaluation bias to unlock better models on Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/fix-evaluation-bias-to-unlock-better-models-on-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-10-27T21:36:49.826062'
score: 86
---

📌 評測集 96.8% 標籤來自現役模型：Property Finder 如何打破循環評測換得 86% 省成本

TL;DR：房地產平臺 Property Finder 發現自家模型比較的「標準答案」幾乎全來自現役模型本身，重建無偏標籤後才找到真正更好更便宜的方案。

想換一個更便宜的視覺模型，結果每次比較都是現役模型贏——這聽起來像是現役模型真的最強，但 Property Finder 的工程團隊發現，問題出在評測集本身就是用現役模型的預測結果做標籤。

🤔 **用自己的答案給自己打分**

Property Finder 是一個在中東與北非（MENA）地區營運的房地產應用，每天要處理數萬張房源圖片，平均每筆新上架房源有 15 張照片，系統要對每張圖片評估 11 項品質屬性，包括浮水印偵測、房間分類、裝潢狀態、照片品質與施工痕跡等。團隊在把視覺 AI 工作負載遷移到 Amazon Bedrock 上更具成本效益的方案時，發現自家的評測資料集裡，96.8% 的標籤直接來自現役視覺語言模型（VLM）的預測結果，而非獨立的人工驗證。這代表任何候選模型在測試前就已經結構性地處於劣勢——評測比較的其實是「跟現役模型像不像」，而不是「對不對」。

隱藏的錯誤也證實了問題的嚴重性：浮水印文字抽取裡,連字元層級的錯誤（包含幻覺出來的品牌名稱和缺漏字元）都被標成正確答案;照片分類則被迫把同時包含多種房間類型的圖片硬塞進單一標籤。即使是另外 3.2% 由人工標註的樣本，標註者也引入了原始規格之外的類別，例如出現了 prompt 裡根本沒有定義過的 "Office" 標籤。

🧩 **重建無偏標準答案，並改用多標籤**

要打破這個循環，團隊找來具備房地產上架品質標準專業知識的策略與分析專家，獨立對 356 張阿聯（UAE）圖片重新標註，完全不參考現役模型過去的預測結果，另外還標註了一組埃及圖片作為跨區域檢查（230 張，本文未報告結果）。前 256 張 UAE 圖片組成用於調參的開發集，最終評測集則是全部 356 張（含開發集之後新增標註的 100 張）。AWS Generative AI Innovation Center 團隊透過專門的釐清會議進行系統性品質審查,處理模糊案例並維持標註一致性。

另一個關鍵修正是把單一標籤分類改成多標籤：房地產照片經常透過門口同時拍到多個房間，或同時具備多種品質特徵，例如透過門口看到臥室的走廊照片本質上就是「兩者皆是」。允許多標籤之後，評測就能真正衡量模型答對了什麼，而不是因為它給出合理的次要預測就被扣分。文章也提到,一種可能的改良方向是混合式作法：讓不同模型家族各自提出候選標籤與分歧點，再由人工專家裁定每一個案例，不直接採用任何模型輸出作為標籤,藉此降低未來擴充資料集時的標註負擔。

📊 **指標選擇與優化迴圈**

Micro F1 被選為主要指標，因為它對每一次預測給予同等權重，符合「整體標籤正確率」這個業務目標；同時搭配 Macro F1，因為 Micro F1 容易被高頻類別主導，可能掩蓋罕見屬性上的弱點。團隊也使用了每個標籤的 precision/recall、以及 per-sample IoU（衡量每張圖片預測標籤與專家標籤的重疊程度）；至於九個單標籤屬性（如圖片旋轉、浮水印偵測），則額外用 exact-match accuracy 衡量。

有了無偏評測，團隊才真正開始優化。優化迴圈的概念類似強化學習：把每個版本的 prompt 看作一個 agent，Micro F1 分數是獎勵訊號，錯誤分析則扮演梯度的角色，這個想法與 GEPA（Genetic-Pareto reflective prompt evolution）類似，透過突變 prompt 元件、評估適應度、篩選存活版本並反覆迭代。初版 prompt（v0）只是泛用的分類指令，例如「把這張圖片分類成客廳、廚房、臥室、浴室其中一類」；在 v21 之前的版本沿用舊的單標籤設定，分數不能直接比較。Property Finder 原本的生產基線模型（文中稱為 proprietary model A）使用針對其模型家族調校過的 v22 prompt，在 256 張圖片的開發集上拿到 0.55 的 Micro F1。整個優化流程從 v0 一路迭代到 v27，期間 AI 助理協助重新改寫 prompt，並在 v27 的照片分類任務上引入 DSPy 函式庫中的自動化 prompt 優化框架 MIPROv2 來補強人工的錯誤分析流程。最終，團隊在 Amazon Bedrock 上找到了準確度更高、成本卻降低 86% 的方案。

💡 **方法學比模型選擇更重要**

這個案例最值得注意的地方,是團隊花最多力氣解決的不是「哪個模型更好」，而是「我們能不能先量出真正的差距」。只要評測集的標準答案本身就是從被比較對象之一衍生出來的，任何後續的模型選型、prompt 優化都會被這個偏差污染，而且這種污染往往不會在日常使用中被發現,因為現役模型的表現「看起來一直都不錯」。

🎯 **實務啟示**

在評估是否要替換現有模型之前，先檢查評測標籤的來源：如果標準答案有相當比例是直接沿用現役模型的輸出，這份評測集本身就需要重建。用獨立領域專家重新標註、適度放寬成多標籤、搭配 Micro/Macro F1 與 IoU 等互補指標，才能得到真正可信的模型比較基礎,再談 prompt 優化或換模型才有意義。

🔗 **來源**
- 標題：Fix evaluation bias to unlock better models on Amazon Bedrock
- 作者／機構：Khaled Thabit, Meriem Boughrara, Mohamed Desouky（Property Finder）與 AWS Generative AI Innovation Center
- 連結：https://aws.amazon.com/blogs/machine-learning/fix-evaluation-bias-to-unlock-better-models-on-amazon-bedrock/

#AmazonBedrock #EvaluationBias #ModelEvaluation #PromptEngineering #VisionLanguageModel #MicroF1 #GEPA #MIPROv2 #MLOps #AWS
