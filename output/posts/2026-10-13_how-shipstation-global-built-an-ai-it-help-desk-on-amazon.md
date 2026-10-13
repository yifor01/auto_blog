---
title: How ShipStation Global built an AI IT help desk on Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-shipstation-global-built-an-ai-it-help-desk-on-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-10-13T22:11:41.855881'
score: 73
---

📌 ShipStation用Bedrock AgentCore打造IT客服機器人Deckhand

TL;DR：ShipStation Global在Slack上用Amazon Bedrock AgentCore打造IT help desk agent，三個月內回覆97.5%訊息、正向回饋達96%。

IT team每天被同樣的問題淹沒，答案通常早就存在於某篇Confluence文件或八個月前的某條Slack討論串裡，難的從來不是「有沒有答案」，而是「找不到答案」。ShipStation Global索性讓AI去找。

🤔 **同樣的問題被問一百次，答案卻散落在各處**

ShipStation Global是一個出貨與物流平臺，過去IT支援的痛點很典型：同樣的問題反覆被問、下班後才出現的錯誤訊息截圖、以及需要跨team蒐集資訊才能回覆的請求。這些對話全部堆在一個忙碌的help desk Slack頻道裡，答案常常已經存在於某篇how-to文件、intranet頁面或幾個月前的討論串，但找出來本身就是體力活。

🧩 **Agent跑在AgentCore上，工具透過Gateway用MCP掛載**

Deckhand像團隊成員一樣加入Slack頻道、讀對話、並從使用者的Slack profile取得context來回答問題。整套系統跑在Amazon Bedrock AgentCore上，用AgentCore runtime把agent跑在隔離的session裡，不需要自己管伺服器或容器。流程大致是：員工在頻道發訊息→Slack service組合完整討論串歷史與使用者context→透過AgentCore runtime API呼叫agent→agent搜尋knowledge base並視需要呼叫工具→找到答案就回覆，找不到就提出澄清問題或主動提議建立ticket。

Agent本體用open source的Strands Agents SDK實作：一個agent就是model、一組工具、加上一個system prompt，SDK負責管理reasoning loop讓模型選工具、處理結果、反覆迭代直到產出答案，model ID透過環境變數設定，換模型不用改程式碼。工具整合有兩種方式：Amazon Bedrock Knowledge Bases檢索是Strands內建工具，一行import即可用；其他功能（分類、ticket管理、使用者解析、圖片分析）則由註冊在AgentCore Gateway上的Lambda function處理，Gateway把它們包裝成MCP tools，Lambda依工具名稱分派呼叫，這讓工具邏輯可以獨立更新、也讓agent能直接從Gateway取得新工具而不需要重新部署。

Knowledge base用S3-backed data sources，每份文件帶metadata（標題、來源URL、內容類型、活動日期），讓agent可以依條件過濾內容。最有價值的資料來源是「已解決的Slack支援討論串」歷史存檔，這是多年來員工描述問題、IT team帶著排查的完整紀錄，等於一個由「問題真正被解決的那個人」驗證過的知識庫，但原始匯出資料相當雜訊，混著閒聊、自動警示與從未真正被解決的討論串。團隊用三階段pipeline進行挖礦與萃取，核心採用RLM，因為它能把整個Slack匯出歷史維持在一個持久的sandbox變數空間裡，讓模型對這份匯出資料反覆推理並產出一致的輸出結構，最終效果是員工遇到同事以前解過的問題時，Deckhand能直接給出已驗證過的解法，通常是一組可執行的編號步驟。

在共用頻道裡運作的AI bot，往往是先在社交層面出錯，才輪到技術層面出錯，所以Deckhand也有一套邏輯判斷何時該保持安靜（具體規則素材未揭露）。每則回覆都附上回饋按鈕：按讚直接記錄，按倒讚則會跳出簡短的「哪裡出錯」欄位，評分連同原始問題與機器人回覆一起存進DynamoDB，負面回饋被用來改善system prompt、agent行為，以及修正knowledge base裡不正確的資訊。權限管控也不只靠prompt規則，而是透過程式碼與基礎設施層面落實。

📊 **三個月：1,935則訊息，97.5%回覆率，409張ticket**

Deckhand於2026年4月上線，一開始每天約30則訊息，到初夏增加到最多100則。上線前三個月共處理1,935則訊息、開啟1,221次agent對話、建立409張Jira Service Management ticket，整體回覆了97.5%的訊息。三分之一的問題是下班後提出的，這類問題Deckhand回答了94%，原本要等到第二天早上才有人處理的問題，當晚就有了答案。正向回饋率從4月的82%成長到6月的96%，是團隊根據使用者抱怨調整system prompt與knowledge base後達成的。最明顯的成效是ticket deflection：1,221次agent對話裡只有409次真正變成ticket。

💡 **真正的工程量，在資料清洗而不是架構本身**

從架構上看，Deckhand是典型的「knowledge base檢索＋MCP工具呼叫」客服agent模式，搭配AgentCore runtime做無伺服器部署，設計本身並不特別新穎。真正的工程含金量在於資料工程：把雜訊很重的歷史Slack討論串萃取成可信賴、已驗證的知識庫內容，以及把回饋資料持續接回system prompt與knowledge base的迭代機制，這套負回饋閉環才是支撐97.5%回覆率與96%滿意度背後的實際工作量。

🎯 **實務啟示**

想做類似IT或客服agent的團隊，比起糾結架構要多複雜，更值得投資的是三件事：既有歷史對話資料的清洗與驗證pipeline；把回饋資料接回system prompt與knowledge base的迭代機制；以及用Gateway/MCP把工具邏輯與agent邏輯解耦，方便各自獨立迭代。

🔗 **來源**
- 標題：How ShipStation Global built an AI IT help desk on Amazon Bedrock AgentCore
- 作者／機構：Kenneth Salmon, Edward Boswell, Jack Armstrong, Robert Bahn, Nick Ciubotariu（ShipStation Global）／AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/how-shipstation-global-built-an-ai-it-help-desk-on-amazon-bedrock-agentcore/

#AWS #BedrockAgentCore #AIAgent #RAG #SlackBot #ITHelpDesk #StrandsAgents #MCP #GenAI #CustomerSupport
