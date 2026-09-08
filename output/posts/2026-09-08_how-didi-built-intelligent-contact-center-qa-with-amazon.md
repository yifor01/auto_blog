---
title: How DiDi built intelligent contact center QA with Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-didi-built-intelligent-contact-center-qa-with-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-09-08T20:18:00.478714'
score: 80
---

📌 DiDi用Amazon Bedrock重建客服QA,意圖辨識準確率從38%衝上86%

TL;DR: DiDi海外業務用Amazon Bedrock取代不透明的第三方QA工具,靠精準的上下文管理大幅提升準確率。

一套客服QA系統要同時服務三個事業體、兩種語言,意圖辨識準確率卻只有38%,你會怎麼修?DiDi海外業務集團(IBG)給出的答案不是換一個更強的模型,而是重新設計「模型每一次到底該看到什麼」。

🤔 意圖辨識準確率只有38%,問題出在哪裡

DiDi IBG的業務橫跨14個國家與地區,涵蓋叫車、外送、金融服務三大業務線,服務數千萬用戶。客服部門每月要處理大量西班牙語與葡萄牙語的即時聊天與電話工單,原本仰賴的第三方QA方案不透明、缺乏彈性,難以跟上快速變動的QA標準與業務規模成長。DiDi IBG的CX團隊因此與AWS合作,在Amazon Bedrock上打造自有的智慧QA系統。團隊選擇Bedrock的理由有三:一是model-agnostic的單一API可依pipeline需求選用不同基礎模型,不必重新架構;二是內建治理與安全控制,包括透過AWS PrivateLink的VPC私有連線、傳輸與靜態加密、以及IAM細粒度存取控制,把敏感客服資料留在DiDi網路邊界內;三是Amazon Bedrock Guardrails提供內容過濾與敏感資訊遮罩等可配置防護機制。

🧩 三條pipeline,外加一層負責任AI控制

系統核心由三條pipeline組成:意圖驗證(intent verification)、合規評分(compliance evaluation)、以及顧客之聲分析(VOC,Voice of Customer)。前處理層負責接收雙通道(聊天與電話)資料,正規化成統一schema後,分流進入三條平行pipeline,每個判斷都會產出完整的推理鏈供人工複核。系統並未把模型輸出視為最終答案:針對規則明確的評分項目,會有一層程式化的後驗證機制,依原始對話重新核對模型判斷(例如拼字錯誤只會針對客服人員自己的訊息做二次驗證);而像回覆等待時間這類可計算的事實,則直接由程式碼確定性算出並注入提示詞,而非交由模型推斷。系統也用Bedrock Guardrails在資料進入模型前先遮罩個資等敏感資訊,並套用contextual grounding檢查,標記缺乏依據的回應以降低幻覺判斷。

💡 問題不是prompt寫得不好,是模型看到的東西太多

DiDi的來電原因分類體系(CR Tree)從大分類逐層細分到許多層級的子分類,層級越深,語意差異越細微,大規模標註時誤標在所難免。團隊一開始的做法很直覺:把完整的CR Tree加上對話內容,一次丟給LLM判斷,結果準確率遠低於預期。追查後發現根本原因:當LLM看到完整選項清單時,會自動逐一比對,即使原本的標籤已經合理,只要找到一個「稍微更精確」的替代選項,就會判定原標籤是錯的。團隊試了多輪prompt調整都無法改變這個行為——問題根本不在提示詞寫法,而在於上下文管理本身。團隊因此把pipeline重新設計成兩層架構,將意圖驗證準確率從38%提升到86%。

合規評分pipeline則面對另一個問題:語言、業務線組合眾多,QA標準又頻繁變動,為每個組合維護獨立prompt並不可持續。團隊改用統一的prompt模板搭配動態變數注入,語言情境、業務線情境與各評分項目的定義規則都存放為外部設定,呼叫當下依工單metadata組裝成完整prompt,新增評分項目、語言或業務線只需更新設定即可,一個模板就能涵蓋所有組合。系統同時運用Bedrock的Tool Use能力,強制模型回傳符合schema的結構化JSON,每一項評分都同時包含判斷結果與推理鏈。

📊 準確率38%衝上86%,合規評分超過九成

在DiDi的正式環境驗證中,意圖驗證準確率從38%提升到86%,合規評分準確率超過90%,VOC分析則把過去需要數小時的人工彙整,壓縮到數分鐘內完成。

🎯 給正在處理大型分類體系任務的工程師的啟示

當任務涉及龐大且層級深的分類體系(像DiDi的CR Tree)時,把完整選項一次性丟給LLM很容易誘發模型「自動逐一比較」的傾向,即便原答案合理也會被判定有更優解而翻案。與其花力氣調整prompt措辭,不如檢視「模型每次呼叫實際看到多少上下文」,並把確定性可算的事實(如等待時間)搬出模型判斷之外,直接以程式碼算好注入。

🔗 來源
- 標題: How DiDi built intelligent contact center QA with Amazon Bedrock
- 作者／機構: Fei Huang, Raphael Hua
- 連結: https://aws.amazon.com/blogs/machine-learning/how-didi-built-intelligent-contact-center-qa-with-amazon-bedrock/

#AmazonBedrock #LLM #ContactCenterAI #AWS #PromptEngineering #ContextManagement #AIGovernance #CustomerExperience #GenerativeAI #Guardrails
