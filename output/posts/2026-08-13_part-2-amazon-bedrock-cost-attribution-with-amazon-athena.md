---
title: 'Part 2: Amazon Bedrock cost attribution with Amazon Athena and CUDOS'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/part-2-amazon-bedrock-cost-attribution-with-amazon-athena-and-cudos/
model: claude-code/sonnet
generated_at: '2026-08-13T07:38:21.729658'
score: 75
---

📌 誰在燒你的 Bedrock 帳單?用 Athena 把成本歸因到每個人

TL;DR：用 CUR 2.0 的 IAM principal 資料 + Athena + CUDOS 儀表板,把 Amazon Bedrock 花費精確追蹤到每個呼叫者與專案。

「這個月 Bedrock 帳單多了兩成,是哪個團隊、哪個應用造成的?」如果答不出這個問題,代表你的成本歸因還停留在「猜」的階段。

🤔 **Bedrock 帳單的老問題:知道花多少,不知道誰花的**

AWS 這篇文章接續 Part 1 介紹的粒度成本歸因功能:每一次 Bedrock 推論請求都會自動溯源到發出呼叫的 IAM principal。搭配可選的成本分配標籤(cost allocation tags),就能用 team、project、tenant 等維度彙總花費。這篇 Part 2 要解決的是下一步:如何把這些資料實際視覺化、查詢與分析。

🧩 **從 CUR 2.0 到 Athena,再到 CUDOS 儀表板**

整個流程分三層。首先要開啟 Cost and Usage Report(CUR)2.0 的 Data Export,並在設定中啟用 IAM principal 資料,這樣 line_item_iam_principal 欄位與相關 IAM principal 標籤才會被填入。文中特別提醒,啟用這項功能後 CUR 檔案會變大,因為原本一筆用量的紀錄,現在會依貢獻的每個 IAM principal 展開成多筆,高流量且 principal 數量多的工作負載要留意 S3 儲存空間規劃,並考慮搭配 S3 生命週期政策。

CUR 2.0 交付第一份報表到 S3 bucket 可能要等 24 小時。接著用 Amazon Athena 以標準 SQL 查詢這份資料,不需要額外管理任何基礎設施。文章也提到有一個選用的 agent.md skill 套件,可以搭配 Claude Code、Kiro-CLI 或 Codex 等 AI 助手,自動化把 Athena 環境串接到 CUR 資料的流程;想部署視覺化儀表板的話,CUDOS 也提供 CloudFormation 範本可以直接佈署,同時會一併建立 Athena 查詢資料庫。

📊 **一條 SQL,看出誰在用哪個模型、花多少錢**

文章給出三種漸進的查詢模式:第一種按呼叫者身分與模型用量拆解花費,回答「誰在呼叫哪個模型、花了多少」;第二種依照 IAM principal 上標記的 team、project、costcenter 等標籤彙總,回答「這個月工程團隊在 Bedrock 上花了多少」這類問題(前提是標籤已被啟用為成本分配標籤);第三種用 Athena 的 UNNEST 函式動態探索所有出現過的 IAM principal 標籤組合,適合在不確定各團隊究竟用了哪些標籤時使用。

文中舉了一個平臺團隊的例子:同時跑著文件摘要管線(DocProcessor)與客服聊天機器人(ChatApp),兩者各自綁定獨立的 IAM 角色。查詢結果顯示,ChatApp 用 Claude 4.6 Sonnet 的花費超過 80 美元,DocProcessor 用 Nova Lite 花費不到 5 美元。這讓團隊能直接追問:ChatApp 裡 72 美元的輸出 token 成本,是否有部分互動可以改用更輕量的模型來降低。

至於查詢本身的成本,Athena 依掃描資料量計費,每 TB 5 美元、單次查詢最低收費對應 10 MB。由於資料表採用 hive partition projection 按 billing_period 分區,只要查詢時鎖定單一月份,掃描量通常遠低於 10 MB,單次查詢成本約 0.00005 美元。文章建議務必加上 WHERE billing_period = ... 篩選條件,並只選取需要的欄位而非 SELECT *。

CUDOS 儀表板則是開源 Cloud Intelligence Dashboards(CID)框架的一部分,5.8 版在 AI/ML 分頁新增了完整的 Amazon Bedrock 區塊,支援依 IAM principal 分組查看花費與每百萬 token 成本趨勢,也能切換到依專案標籤分組,篩選出單一專案(例如文中的 chatbot-v2)後,其餘視覺化圖表會連動只顯示該專案的模型別、用量類型與單位成本趨勢。

🎯 **實務啟示**

對管理多團隊、多應用共用 Bedrock 的組織來說,這套做法把「成本歸因」從月底對帳的事後工作,變成可以隨時查詢的即時能力。啟用 IAM principal 資料前務必評估儲存成本,並提早規劃好標籤命名規範,否則到了要跨團隊彙總時容易發現各自標籤不一致。

🔗 **來源**
- 標題:Part 2: Amazon Bedrock cost attribution with Amazon Athena and CUDOS
- 作者／機構:Abhi Shivaditya
- 連結:https://aws.amazon.com/blogs/machine-learning/part-2-amazon-bedrock-cost-attribution-with-amazon-athena-and-cudos/

#AmazonBedrock #AWS #Athena #CUDOS #CostOptimization #FinOps #CloudCost #LLMOps #IAM #DataEngineering
