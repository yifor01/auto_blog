---
title: How ONESTRUCTION built the Ishigaki-IDS foundation model with AWS GenAIIC
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-onestruction-built-the-ishigaki-ids-foundation-model-with-aws-genaiic/
model: claude-code/sonnet
generated_at: '2026-08-12T07:33:24.655112'
score: 93
---

📌 營建 IDS 文件太難寫？ONESTRUCTION 用三階段訓練打造專用基礎模型

TL;DR：Qwen3 三階段訓練出的 Ishigaki-IDS，IDS 結構合規率近 100%，遠勝通用前沿模型。

同一份 IDS 檔案，通用前沿模型能寫出格式正確的 XML，內容一致性卻幾乎掛零；換成專門訓練過的模型，結構與內容兩項合規率雙雙衝上八成以上。這個落差，正是 ONESTRUCTION 打造 Ishigaki-IDS 的起點。

🤔 BIM 推得動，但 IDS 沒人會寫

日本營建業長期缺工，BIM（Building Information Modeling，建築資訊模型）被國家層級大力推廣，讓設計、施工、維運團隊能共用同一份資訊。但採用 BIM 需要專業知識，學習成本拖慢了普及速度。其中一個典型例子是 IDS（Information Delivery Specifications）：一種以 XML 為基礎的標準，用來定義 BIM 模型（IFC，Industry Foundation Classes 模型）需要附加與驗證哪些資訊。撰寫 IDS 檔案需同時精通其語法規則與 IFC 知識，門檻不低。ONESTRUCTION 與 AWS Generative AI Innovation Center（GenAIIC）合作，作為 GENIAC（Generative AI Accelerator Challenge）Phase 3 的一環，打造出 Ishigaki-IDS，讓非 BIM 專家也能審閱與管理屬性資訊。

團隊面對三個障礙。第一是資料稀缺：IDS 標準 2024 年才發布，公開網路資料量少且深度不足，模型難以單靠資料本身建立足夠脈絡。第二是要注入數千個 IFC 詞彙的對應關係，例如「beam（梁）」對應 IfcBeam、「air conditioner（空調）」對應 IfcUnitaryEquipment，這種映射過去仰賴領域專家手動整理。第三是 IDS 特有的文法：標籤結構會依附加或驗證的資訊類型而變化，需要重複模式與專屬標籤，通用模型很難準確產出。

🧩 CPT → SFT → RLVR 的三階段訓練

團隊以 Qwen3（8B／14B／32B，Alibaba Cloud 的開源多語言大型語言模型）為基底，先在較小規模上實驗，再投入 32B 的完整訓練。訓練分三個階段：

第一階段是持續預訓練（CPT），用網路語料加上內部領域專家協助產生的合成資料，注入 IDS 與 IFC 領域知識——團隊大量生成合法的 IDS 檔案，並從多個角度建立解釋 IDS 相關文件的合成資料集，合成資料佔訓練語料的大部分。第二階段是監督式微調（SFT），用 IDS 撰寫指令（CSV 或自然語言）與對應的預期 IDS 輸出成對訓練，但單靠 SFT 仍會出現看似合理卻錯誤的 XML 標籤選擇、錯誤的屬性值等問題。第三階段是可驗證獎勵的強化學習（RLVR），以國際標準組織 buildingSMART 的 IDS-Audit-Tool 作為獎勵函式，檢查 XML 格式正確性、IDS 結構有效性與語意一致性，讓模型能針對機械式的正確性訊號持續迭代。RLVR 特別適合這種資料稀缺領域，因為它不需要大量監督資料就能提升輸出品質。

團隊每兩週與 GenAIIC 進行一次技術諮詢會議，帶著訓練成果與評估資料，共同檢視五個關鍵面向，逐輪確認「哪些改動能提升 IDS 生成準確度與實用性」。

訓練基礎設施採用 Amazon EC2 P5en 執行個體（兩臺 p5en.48xlarge，搭載 NVIDIA H200 Tensor Core GPU），以 AWS ParallelCluster 進行編排，訓練資料、合成資料與 checkpoint 則存放在專為高運算密集工作負載最佳化的 Amazon FSx for Lustre，確保多節點分散式訓練穩定運作，並能平行存取大型資料集。

📊 結構合規率近 100%，通用模型不到 25%

團隊與內部 IDS 專家自建評估基準 IDS-Bench，涵蓋 IFC 版本、營建專業領域（建築、結構、機電、共通項目）、語言（日文與英文）以及 Implement、Structure、Content 三個面向。在 IDS-Bench 評測中，Ishigaki-IDS 在 XML 結構合規率與 IDS 結構合規率上都接近 100%，IDS 內容一致性也超過 80%。相對地，通用前沿模型雖能產出格式正確的 XML，但 IDS 結構合規率不到約 25%，內容一致性更是接近 0%。這個落差顯示，IDS 這類專業且新興的領域，正是專用模型能發揮價值之處。

模型也支援以 YaRN（Yet another RoPE extensioN）技術延伸的上下文長度，團隊確認在輸入輸出總長約 12 萬 token 的情況下，模型仍能正確生成。在與 buildingSMART 合作的概念驗證中，無論是 IDS 專家或非專家，都對模型使用經驗給予正面回饋，即便提示模糊，模型也能產出符合意圖的 IDS，同時也提出了後續開發建議。

🎯 實務啟示

這個案例的核心經驗是：領域專家協作、大量合成資料，加上綁定驗證工具的 RLVR，三者組合能在資料稀缺的專業領域中，於較短時間內打造出可用的專用基礎模型。對正在評估「要不要為特定領域訓練專屬模型」的團隊而言，若該領域存在明確的機械式驗證工具（如本例的 IDS-Audit-Tool），RLVR 會是比堆砌監督資料更划算的路徑。

🔗 來源
- 標題：How ONESTRUCTION built the Ishigaki-IDS foundation model with AWS GenAIIC
- 作者／機構：Koyo Hidaka（ONESTRUCTION, Inc. 與 Amazon Web Services Japan G.K. 共同撰寫）
- 連結：https://aws.amazon.com/blogs/machine-learning/how-onestruction-built-the-ishigaki-ids-foundation-model-with-aws-genaiic/

#BIM #ConstructionTech #FoundationModel #Qwen3 #RLVR #AWSGenAIIC #DomainAdaptation #LLMFineTuning #IFC #SyntheticData
