---
title: 'Introducing CARE-X: Towards Clinically Useful Radiology VLMs with Auxiliary
  Supervision, Reward-Aligned Learning, and Tool-Augmented Measurement'
source: Microsoft Research
url: https://www.microsoft.com/en-us/research/blog/introducing-care-x-towards-clinically-useful-radiology-vlms-with-auxiliary-supervision-reward-aligned-learning-and-tool-augmented-measurement/
model: claude-code/sonnet
generated_at: '2026-08-12T07:29:35.279052'
score: 112
---

📌 【Microsoft Research】CARE-X:用一個模型讀懂胸腔 X 光的所有臨床任務

TL;DR:研究模型 CARE-X 以生成加判別雙路推理統一報告、分類與定位任務,尚未用於臨床。

一份報告寫得再流暢,只要漏掉一個發現、寫反一個否定詞、講錯一個位置,就是臨床上的錯誤答案。這正是目前生成式放射學 VLM 難以跨過的門檻:語言流暢不等於臨床正確。

🤔 **放射科的任務有多雜,模型就要有多雜**

放射科醫師使用胸腔 X 光的情境很多樣:寫出詳細發現與精簡的 impression、回答某個發現是否存在或位於何處、辨識醫療器材並評估放置位置、指出異常在影像中的確切位置。這些任務需要的輸出形式也不同,有的要敘述式報告,有的要校準過的診斷分數。Microsoft Research 團隊指出,一個臨床有用的放射學 AI 系統,必須同時涵蓋這些不同任務、適應不同工作流程,而且輸出必須醫學上準確。

需要特別說明:根據 Microsoft 官方的研究說明,CARE-X 是研究模型,並非 Microsoft 的產品或醫療器材,未經任何主管機關核准,不適用於臨床診斷、篩檢或病患照護。文中提及的潛在工作流程,是未來研究方向,不是現有可用的功能。

🧩 **雙路推理:同一次前向傳播,同時給文字答案與結構化預測**

CARE-X 建立在 SigLIP2-so400M 視覺編碼器與 Phi-4-mini-instruct(3.8B)語言模型之上,透過輕量 adapter 串接。為了同時支援自由文字生成與結構化臨床預測,模型在共享的語言骨幹上疊加了任務專屬的輔助頭(auxiliary heads),分別負責分類與視覺定位(grounding)。

這些輔助頭並非獨立訓練,而是與語言建模目標共同訓練(co-trained),讓結構化監督訊號豐富共享表徵,進而提升同一任務上的生成表現。這就是論文所稱的「雙路推理」(dual inference):一次前向傳播同時產生自迴歸文字回應,以及帶信心分數的結構化輔助頭預測,兼顧自由文字的彈性與可調整閾值的輸出。

訓練流程分為三階段監督式微調(視覺預訓練、adapter/輔助頭訓練、LoRA 調適),再接上以 DAPO 為基礎的強化學習,針對臨床報告、診斷準確度與空間定位品質最佳化任務專屬獎勵。

📊 **定位任務漲最多,生成式輸出逼近甚至超越結構化預測頭**

在解剖定位任務(Chest ImaGenome)上,輔助定位頭讓 mAP 提升 28.2 個百分點、mIoU 提升 6.2 個百分點;在片語定位(PadChest)上漲幅更大,mAP 提升 24.6 個百分點、mIoU 提升 14.1 個百分點。

更值得注意的是,經過 DAPO 訓練後的生成式輸出,已經逼近甚至超越 SFT 階段的輔助偵測頭:在解剖定位任務上,CARE-X 生成式推理達到 0.868 mAP,略高於 SFT 偵測頭的 0.865 mAP。這代表獎勵對齊學習(reward-aligned learning)可以讓自迴歸式空間解碼追平結構化預測,讓臨床端只需要單一生成式推理模式,測試時不必額外呼叫輔助頭。

在論文比較的基準中,CARE-X 在 MIMIC-CXR、IU-Xray、CheXpert-Plus、ReXGradient 上的多數指標都取得最佳表現。另外用來評估異常發現、並依臨床嚴重度加權誤差的 held-out 指標 CRIMSON 顯示,這些提升反映的是臨床上有意義的改善,而非單純針對獎勵函式的過度最佳化。

在 ReXVQA 基準(涵蓋五個臨床相關類別、共 41,007 組問答)上,CARE-X 整體準確率達 94%,比目前公開報告的次佳模型高出 6 個百分點,並在 2026 年 8 月的 ReXrank RexVQA 排行榜上排名第一。

在 Narayana Health 的 1,047 張去識別化胸腔 X 光片(標註五種盛行率介於 2.6% 至 5.2% 的罕見高風險病灶)上,CARE-X 在五種病灶中的三種取得最高敏感度,同時維持合理的特異度,顯示模型在低盛行率的真實臨床分布下仍具泛化能力。

💡 **當視覺無法給出答案,就交給計算工具**

部分放射學發現依賴的是量測數值而非視覺型態。研究團隊另外做了一個獨立於 CARE-X 主體之外的推理時實驗:結合 Qwen3-VL-4B-Instruct 與確定性量測工具,讓模型在影像理解與精確計算之間交替。模型在整個推理過程中保有對影像的視覺存取權,並依需要呼叫工具辨識解剖標記、計算量測值、評估診斷閾值,形成一個交錯感知與量測的多輪推理迴圈。

即使沒有針對任務做特別訓練,這個做法在所有評估的量測型情境中,都明顯優於單純依賴視覺判斷的推理。作者舉例,主動脈擴張(aortic dilation)在胸腔 X 光上通常不會被量化,往往只在為其他目的做的 CT 掃描中被偶然發現;若能可靠地在胸腔 X 光上篩檢,或有機會讓延遲偵測導致的心血管風險提早被發現與追蹤。

⚠️ **仍是研究階段,結果來自回溯性研究**

必須再次強調,CARE-X 目前描述的成果都是回溯性研究發現,不代表模型在安全性、有效性或臨床適用性上已獲驗證,也不是目前可用的能力。

🎯 **對工程師的啟示**

CARE-X 的核心設計思路值得借鏡:讓判別式輔助頭與生成式語言模型共享表徵、共同訓練,而不是分開建模,可以同時獲得結構化、可調閾值的輸出以及更強的生成表現。搭配確定性工具處理量測型任務的做法,也提供了一個把 VLM 感知能力與精確計算結合的通用範式,值得延伸到其他需要量化判讀的多模態任務。

🔗 **來源**
- 標題:Introducing CARE-X: Towards Clinically Useful Radiology VLMs with Auxiliary Supervision, Reward-Aligned Learning, and Tool-Augmented Measurement
- 作者／機構:Microsoft — Mercy Ranjit, Nikhilesh E, Dr. Abhyuday Kumara Swamy, Tanuja Ganu
- 連結:https://www.microsoft.com/en-us/research/blog/introducing-care-x-towards-clinically-useful-radiology-vlms-with-auxiliary-supervision-reward-aligned-learning-and-tool-augmented-measurement/

#CARE-X #RadiologyAI #VLM #MedicalImaging #MicrosoftResearch #ChestXray #ReinforcementLearning #ToolAugmentedLLM #ClinicalAI #MultimodalAI
