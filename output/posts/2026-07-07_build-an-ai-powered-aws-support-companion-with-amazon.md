---
title: Build an AI-powered AWS support companion with Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-an-ai-powered-aws-support-companion-with-amazon-bedrock-agentcore/
score: 96
model: google/gemma-4-31b-it:free
generated_at: '2026-07-07T21:14:11.751399'
---

**使用 Amazon Bedrock AgentCore 建構 AI 驅動的 AWS 支援伴侶**  
*作者：Jose Soto*（AWS ML）  
*來源：https://aws.amazon.com/blogs/machine-learning/build-an-ai-powered-aws-support-companion-with-amazon-bedrock-agentcore/*

---

## TL;DR  
- 現行的 AWS 故障排除需要在主控臺、CloudWatch、檔案、社群貼文與開 case 之間切換，平均每起事件耗時 30–45 分鐘。  
- 本文示範如何使用 **Amazon Bedrock AgentCore** 搭配 **Strands Agents**、**Model Context Protocol (MCP)** 與 **Amazon Nova Pro（透過 Amazon Bedrock）** 建立一個單一對話介面的 AWS 支援伴侶。  
- 該伴侶能夠分析 CloudWatch 日誌、搜尋 AWS 檔案、查詢 AWS re:Post 社群知識並直接建立支援案件。  
- 解決方案透過 **AWS CloudFormation** 一鍵部署，隨附以 **AWS Amplify** 建置的網頁前端，讓開發與運維團隊能在同一介面內完成所有調查步驟。  
- AgentCore 負責執行階段的作業複雜度（工作階段隔離、自動擴充、安全性與可觀測性），讓開發者只需專注於代理的行為，而無需管理基礎設施。

---

## 為何需要 AI 驅動的 AWS 支援伴侶  

在處理 AWS 基礎設施事件時，工程師通常需要：

1. 開啟 AWS Management Console 檢視資源狀態。  
2. 檢視 Amazon CloudWatch 日誌尋找異常。  
3. 搜尋 AWS 官方檔案尋找相關操作說明。  
4. 瀏覽 AWS re:Post 社群尋找類似案例。  
5. 手動建立支援案件等待後續處理。

這些步驟分散在不同的介面與工具之間，導致每起事件在真正開始修復前就已耗費 30–45 分鐘，嚴重影響團隊的響應速度，且取得的資訊無法在各工具間自然流動。

---

## 解決方案概覽  

本文介紹的 **AWS 支援伴侶** 利用以下元件將上述步驟整合為單一的對話式介面：

- **Amazon Bedrock AgentCore** – 負責代理的執行階段，提供工作階段隔離、自動擴充、安全性與可觀測性，讓開發者只需專注於代理的行為。  
- **Strands Agents** – 作為協調框架的 Python 應用程式，以 Docker 容器形式打包並部署至 AgentCore 執行階段。  
- **Model Context Protocol (MCP)** – 三個 MCP 伺服器分別提供對 AWS 檔案、AWS re:Post 社群知識、支援案件建立以及 CloudWatch 日誌查詢的存取。  
- **基礎模型 (FM)** – 透過 Amazon Bedrock 存取 **Amazon Nova Pro**，可依需求換成其他支援的模型而無需修改代理程式碼。  
- **AWS CloudFormation** – 一鍵部署所有後端資源。  
- **AWS Amplify** – 提供網頁前端，讓使用者透過網頁與代理進行互動。

---

## 架構元件說明  

### 代理執行階段（Agent Runtime）  
- 以 **Strands Agents** 編寫的 Python 應用程式，打包成 Docker 容器。  
- 部署至 **Amazon Bedrock AgentCore 執行階段**，由 AgentCore 負責容器的生命週期、擴縮容、安全隔離與日誌收集。  

### 基礎模型與工具協調  
- 代理透過 Strands Agents 呼叫 **Amazon Nova Pro**（經 Amazon Bedrock 取得），根據使用者的自然語言指令決定要呼叫哪些工具。  
- 透過 **Model Context Protocol (MCP)**，代理能夠存取三個後端服務：  
  1. **AWS 檔案伺服器** – 檢索官方操作手冊與最佳實踐。  
  2. **AWS re:Post 社群伺服器** – 搜尋社群討論與已知解決方案。  
  3. **支援案件與 CloudWatch 伺服器** – 建立支援工單以及查詢最近的日誌與指標。  

### 部署與前端  
- 全部後端資源（AgentCore 執行階段、MCP 伺服器、必要的 IAM 角色等）透過單一 **AWS CloudFormation** 指令碼完成佈署。  
- 前端採用 **AWS Amplify** 建置的單頁應用程式，提供簡易的聊天視窗，使用者只要輸入問題或描述症狀，代理即會自動 orchestrate 所需的工具與模型，回傳整合後的答案或直接建立支援案件。  

---

## 運作流程（簡化說明）  

1. **使用者在網頁介面輸入**：例如 “我的 EC2 Instance 在過去 10 分鐘內 CPU  utilisation 持續超過 90%，請幫我診斷”。  
2. **代理接收輸後**，透過 Strands Agents 決定需要哪些工具：  
   - 呼叫 CloudWatch MCP 伺服器抓取相關指標與日誌。  
   - 查詢 AWS 檔案 MCP 伺服器尋找高 CPU 可能原因與處理步驟。  
   - 搜尋 re:Post MCP 伺服器尋找類似案例的社群解答。  
3. **取得資訊後**，代理將結果送往 Amazon Nova Pro 進行摘要與建議生成。  
4. 根據摘要內容，代理可以：  
   - 直接回覆可能的根本原因與修復步驟。  
   - 在使用者確認後，透過支援案件 MCP 伺服器自動建立支援工單。  
5. 整個過程在同一個對話視窗內完成，免除切換多個主控臺與工具的需求。  

---

## 解決方案的主要優勢  

- **減少上下文切換時間**：所有調查步驟透過單一介面完成，可縮小原本 30–45 分鐘的準備階段。  
- **操作簡化**：開發與運維團隊不需要學習多種工具，只需熟悉對話介面。  
- **作業複雜度由 AgentCore 負載**：工作階段隔離、自動擴容、安全控制與觀測性皆由代理執行階段處理，開發者專注於代理的邏輯與工具整合。  
- **模型彈性**：只要在 Amazon Bedrock 中有可用的模型，即可透過設定變更 FM，無需改動代理程式碼。  
- **快速部署**：單一 CloudFormation 指令碼即可完成後端佈署，前端則由 Amplify 提供即時更新的網頁介面。  

---

## 部署步驟概覽（僅概述）  

1. 下載隨文附帶的 CloudFormation 範本與 Amplify 前端原始碼。  
2. 透過 AWS CLI 或 Console 執行該 CloudFormation 堆疊，系統會自動建立：  
   - AgentCore 執行階段（含 Docker 容器）  
   - 三個 MCP 伺服器（檔案、re:Post、支援/CloudWatch）  
   - 必要的 IAM 角色與政策  
3. 部署完成後，啟動 Amplify 應用程式，取得網頁網址。  
4. 在網頁介面中開始與代理對話，即可體驗完整的 AWS 支援流程進行問題診斷與案件建立。  

> **完整部署指令碼與原始碼請參考原文連結**：https://aws.amazon.com/blogs/machine-learning/build-an-ai-powered-aws-support-companion-with-amazon-bedrock-agentcore/

---

## 結論  

透過將 **Amazon Bedrock AgentCore**、**Strands Agents**、**Model Context Protocol** 與 **Amazon Nova Pro**（經 Amazon Bedrock）結合，並以 **AWS CloudFormation** 與 **AWS Amplify** 完成一鍵部署，本文展示了如何將原本分散在多個主控臺與工具中的 AWS 故障排除流程，縮減為單一的對話式體驗。此做法不只減少了上下文切換所帶來的時間浪費，也讓團隊能將更多精力放在真正的問題解決上，而非工具切換與資訊搜尋的雜務上。  

如需完整的程式碼與部署說明，請參考上述原始文章連結。祝您開發順利！
