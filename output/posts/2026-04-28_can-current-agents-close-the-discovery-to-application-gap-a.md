---
title: "Can Current Agents Close the Discovery-to-Application Gap? A Case Study in Minecraft"
source: ChatPaper/AI
url: https://arxiv.org/abs/2604.24697
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-04-28T20:34:52.301942
---

📌 【UCLA/北大/Amazon 研究】SciCrafter：測Agent發現應用能力

你以為前沿AI Agent已能搞定複雜工程任務？
最新研究顯示，它們在Minecraft紅石電路任務的成功率僅26%。
瓶頸甚至不是「做不對」，而是「不知道要解決什麼問題」。

🤔 **評估通用智能的「發現到應用循環」缺乏合適基準**
發現因果規律並將其應用於構建功能系統的「發現到應用循環」，是通用智能的核心標誌。但過去評估AI這項能力時，始終面臨科學發現與現實工程之間的巨大複雜度鴻溝：任務太簡單無法測出真實能力，太複雜又難以標準化評估，導致相關研究難以推進。

🧪 **基於Minecraft紅石電路的參數化可擴縮基準**
本研究提出SciCrafter基準，以Minecraft中的紅石電路任務為載體，要求Agent按指定模式點亮燈具，例如同時點亮、定時序列點亮。當目標參數放大時，構建複雜度與所需知識會大幅上升，強迫Agent真正通過實驗發現規律，而非依賴記憶中的現成解決方案。

實驗採用通用代碼Agent框架，評估了GPT-5.2、Gemini-3-Pro、Claude-Opus-4.5等前沿模型。研究將「發現到應用循環」拆解為四項核心能力：知識缺口識別、實驗發現、知識鞏固、知識應用，並設計針對性干預實驗，以干預的邊際貢獻作為對應能力缺口的代理指標。

 **所有前沿模型成功率均卡在26%左右**
實驗結果顯示，所有被測模型的成功率均停滯在約26%，未出現明顯的性能差異。

進一步分析四項能力的缺口後發現：通用知識應用能力仍是所有模型的最大短板；但對於前沿模型而言，知識缺口識別能力開始成為主要障礙，這代表當前AI的能力瓶頸，正從「把問題解決對」轉向「提出正確的問題」。

💡 **AI能力瓶頸從解決問題轉向提出問題**
過去AI研究的重點多放在提升模型解決給定問題的能力，但SciCrafter的診斷結果顯示，前沿模型已具備一定的問題解決能力，卻缺乏主動識別自身知識缺口、設計實驗發現新規律的能力。這項發現為後續Agent研究指明了新的突破方向，除了優化問題解決能力，更要強化主動探索與問題定義能力。

⚠️ **論文未明確提及研究限制**
本次提供的公開資料未包含論文所述的研究限制說明，讀者可自行查閱原文獲取完整資訊。

🎯 **為Agent能力評估提供診斷性新框架**
SciCrafter的價值不在於給出模型的分數排名，而在於提供可拆解的能力診斷工具。對AI研究者而言，可針對知識缺口識別等短板設計優化方案；對工程師而言，在設計實際場景的Agent時，需重點強化其主動探索、識別自身知識邊界的能力，而非僅關注問題解決效率。

🔗 **論文連結**
📝 标题：Can Current Agents Close the Discovery-to-Application Gap? A Case Study in Minecraft
👤 作者：Zhou Ziheng, Huacong Tang, Jinyuan Zhang, Haowei Lin, Bangcheng Yang
🏫 机构：University of California, Los Angeles; Peking University; Amazon
🔗 链接：https://arxiv.org/abs/2604.24697

你認為目前AI Agent最大的能力缺口是什麼？歡迎留言分享你的觀察👇

#AI #Agent #MachineLearning #Minecraft #UCLA #PekingUniversity #Amazon #人工智能 #基准测试 #通用智能
