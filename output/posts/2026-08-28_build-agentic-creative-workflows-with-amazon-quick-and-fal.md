---
title: Build agentic creative workflows with Amazon Quick and fal
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-agentic-creative-workflows-with-amazon-quick-and-fal/
model: claude-code/sonnet
generated_at: '2026-08-28T18:08:34.428091'
score: 82
---

📌 用 MCP 串起 Amazon Quick 與 fal:讓創意工作流記得住上下文

TL;DR:Amazon Quick 透過 MCP 串接 fal 的生成媒體工具,把分鏡腳本製作變成一個有審核關卡的 agent 迴圈。

78% 的創意主管表示需求已經超過團隊產能,但單純加快生成速度並不能解決問題,因為腳本、參考素材、模型與產出結果散落在不同工具之間,創作者得不斷手動搬運上下文、重新組裝結果。

🤔 **問題不是生成太慢,而是上下文一直斷線**

媒體企業需要的是一個可重複使用的 agent harness:能保留上下文、支援長時間執行的媒體任務,並在關鍵創作節點加入人工審核。這篇文章示範的解法結合了可重用的工作流程指令、共享工具基礎設施與編排能力,並用兩個工作流程(八格分鏡腳本製作、音樂錄影帶概念雛形)來說明。

🧩 **四層架構:Quick 編排、Skills 固化流程、MCP 當介面、fal 出圖出片**

整套架構有四層。Amazon Quick 是 agent 工作區與編排層,負責解讀創作者的請求、規劃工作、保留已核准的決策,並呼叫外部工具、呈現產出供審核。Skills 則是把可重複的流程(例如「產生場景前先確認角色參考」「在指定品質關卡前暫停等待核準」)固化成可重用的工作流程指令,團隊不必每次活動都重新設計流程。fal 是一個生成媒體平臺,提供超過 1,000 個涵蓋圖片、影片、音訊、3D 等生成任務的模型,並以 MCP(Model Context Protocol,一個讓 AI 應用程式透過一致介面連接外部工具與資料來源的開放標準)伺服器的形式對外開放能力;Amazon Quick 則透過其 MCP client 發現並呼叫這些工具。這樣的架構把「工作流程編排」與「媒體生成」分開:Quick 是編排層與 MCP client,fal 是 MCP server 與生成媒體工具的提供者。

連接方式是先在 fal 後臺建立 API key,妥善保存(不放進截圖、原始碼或共享文件),再到 Amazon Quick 設定 MCP 連接器,確認 Quick 能發現 fal 開放的工具後,即可在新對話中開始使用。

🧩 **八格分鏡腳本:從創意方向到最終版面,一次對話搞定**

文章以「為未來感賽車原型發表製作八格分鏡腳本,採用動漫風格與漫畫格線版面」為例,說明整個流程如何在一次互動式對話中完成:

1. 鎖定創意方向:確認畫風、格線版面、長寬比與限制條件。
2. 核准故事計畫:先產出八個故事節點、鏡頭清單與角色描述的文字版本,此階段不生成任何圖片,創作者可以先修改故事節奏或角色設定。
3. 鎖定角色設計:文字計畫核准後,Quick 檢視可用的 fal 模型,產生兩組標示清楚的角色設計供比較(A/B 雙模型比較),創作者選定其中一組後,再產生該角色的多視角參考圖(正面、背面、多姿勢、戴頭盔、特寫臉部),經核准後才會進入分鏡格生成。
4. 生成分鏡格:使用 FLUX.1 Kontext,每次呼叫都附上已核准的角色參考圖,確保跨場景的視覺一致性。

創作者可以在同一段對話中審核並要求修改;八格全部核准後,Quick 依鏡頭清單順序排列並加上說明文字,組成互動式分鏡檢視器,可以呈現為漫畫格線、捲動或投影片形式,且這些版面重複使用已核准的圖片,不需重新生成。若創作者確認這套流程值得重複使用,還能直接請 Quick 把這段對話轉存成一個可分享的「AI Storybuilding」Skill。

🎯 **實務啟示**

這篇文章展示的價值不在生成模型本身,而在「審核關卡 + 上下文保留」的 agent harness 設計:每個關鍵決策點(畫風確認、故事計畫、角色設計、參考圖)都先鎖定再往下一步,避免下游生成因上游變動而報廢重做。對正在設計自家 agentic 創意工具的工程團隊,透過 MCP 做工具介面而非為每個生成服務寫客製整合,再搭配 Skills 把驗證過的流程固化下來,是一個值得參考的分層方式。

🔗 **來源**
- 標題:Build agentic creative workflows with Amazon Quick and fal
- 作者／機構:James Wu / AWS Machine Learning Blog
- 連結:https://aws.amazon.com/blogs/machine-learning/build-agentic-creative-workflows-with-amazon-quick-and-fal/

#AgenticAI #MCP #GenerativeMedia #AmazonQuick #fal #CreativeWorkflow #FLUXKontext #AIAgents #ModelContextProtocol #ContentGeneration
