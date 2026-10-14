---
title: Build self-improving document processing using Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-self-improving-document-processing-using-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-10-14T21:00:26.101852'
score: 86
---

📌 發票格式年年變？AgentCore 做自學習文件處理

TL;DR：AWS 示範用 8 個協作 agent 打造能自動學習新發票／採購單格式的文件處理系統。

IDC 研究指出，文件相關問題每年讓每位資訊工作者多花 19,732 美元成本，生產力下降 21.3%——問題往往不是文件難懂，而是每換一個供應商的版面，整套樣板就要重新設定一次。

🤔 **樣板一改版面就壞，發票越多維護越痛**

企業同時收來自數百家供應商的發票時，版面會依發行者而異，而且常常毫無預警地更動。傳統的智慧文件處理（IDP）系統需要替每一種文件格式預先設定樣板、擷取規則與驗證邏輯，一旦版面跑掉就會整套失效。素材指出，員工最多可花 30% 的工時處理文件相關工作，而人工輸入的錯誤率落在 1–4%。

🧩 **8 個 agent 分兩條流程線，從分類到學習**

這套方案用 Strands Agents（一套開源 agent SDK）建構多 agent workflow graph，跑在 Amazon Bedrock AgentCore 之上，由 8 個專責 agent 分別負責分類、擷取、驗證與學習。部署會建立六個 CloudFormation stack：Core（S3、Cognito、DynamoDB）、Gateway（Lambda 工具、AgentCore Gateway）、Aurora（Amazon Aurora DSQL）、Agent（AgentCore runtime、容器）、UI Orchestrator（API 端點），以及 Modern UI（跑在 CloudFront 上的 React 應用），整個部署約需 15–20 分鐘。

文件素材給出一個具體案例：新供應商 Two Wheel Store 寄來第一張採購單時，流程是這樣走的：
- Step 1：Matcher agent 在向量庫中搜尋，找不到相似文件，於是把工作導向訓練流程。
- Step 2：Analyzer agent 用 Amazon Textract 擷取文件的原始文字。
- Step 3：Instructions agent 依 schema 產生擷取用的 prompt，Extractor agent 據此產出結構化 JSON。
- Step 4：Validator agent 比對 schema 後驗證失敗——供應商的 SKU 格式（SB-004）和內部格式（AB-SB-004）不一致。
- Step 5：Instructions Fixer agent 診斷出問題，在擷取 prompt 中加入明確規則：把供應商 SKU 加上 AB- 前綴。
- Step 6：第二次嘗試，七筆品項全數通過驗證，Save Instructions agent 把修正後的 prompt 存回向量庫。

第一次處理這張單子，從頭到尾耗時 3 分 49 秒。等 Two Wheel Store 的第二張採購單進來，Matcher agent 以 confidence score 3.946（門檻為 3.7）直接比對到先前存下的擷取指令，這次就改走自動化流程，不需要再重新訓練。

📊 **一個月處理 1000 份文件，成本估算約 58 美元**

以每月 10 份訓練文件、1,000 份處理文件計算（美國東部維吉尼亞區域），估計月成本約 58 美元，其中基礎模型推論約佔整體成本的 85%，平均每份文件約 0.055 美元。各 agent 使用的模型集中設定在設定檔中，可以針對簡單任務選用較便宜的模型。更換模型後，可用 AgentCore Evaluations 確認擷取品質是否仍維持在可接受水準。

⚠️ **範例資料是假的，schema 與規則要自己換**

範例使用的是合成的腳踏車公司資料集與模擬 ERP 資料庫，要套用到自己的文件類型，必須自行建立 JSON schema（定義欄位名稱、資料型別，以及每個欄位是文件上明寫還是需要從上下文推斷），也要替換驗證邏輯——寫一個接受擷取 JSON、回傳通過／失敗與錯誤訊息的 Lambda function，再註冊成 AgentCore Gateway 的工具。此外，Orchestrator、Validator、Instructions 等 agent 的 prompt 都寫死了採購單相關用語，換文件類型也要一併調整。

🎯 **自動化的是學習迴圈，不是免設定**

這套系統真正的價值在於把「遇到新格式 → 驗證失敗 → 修正擷取規則 → 記住」這個迴圈自動化，而不是讓你完全不用設定。對想導入的團隊來說，schema、驗證規則與 prompt 仍需要工程師依據自己的業務邏輯重新打造。

🔗 **來源**
- 標題：Build self-improving document processing using Amazon Bedrock AgentCore
- 作者／機構：Erik Cordsen，AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/build-self-improving-document-processing-using-amazon-bedrock-agentcore/

#AWS #AmazonBedrock #AgentCore #IDP #DocumentProcessing #AIAgents #StrandsAgents #Automation #MachineLearning #CloudComputing
