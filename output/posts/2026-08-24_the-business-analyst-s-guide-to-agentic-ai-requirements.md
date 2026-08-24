---
title: The Business Analyst's Guide to Agentic AI Requirements
source: Modernanalyst.com
url: https://www.modernanalyst.com/Resources/Articles/tabid/115/ID/7213/The-Business-Analysts-Guide-to-Agentic-AI-Requirements.aspx
model: claude-code/sonnet
generated_at: '2026-08-24T06:34:51.683954'
score: 71
---

📌 業務分析師如何寫出 Agentic AI 的需求規格？

TL;DR：一篇文章整理出五種框架，幫助 BA 具體定義 AI agent 的自主邊界與責任歸屬。

當系統不再只是「接收輸入、回傳輸出」，而是會自己判斷、呼叫工具、甚至代表使用者採取行動時，傳統的使用者故事（user story）還寫得出這種系統的需求嗎？

🤔 **傳統需求文件抓不住「自主性」**

Agentic AI 系統與傳統軟體最大的不同，在於它會在執行過程中做決策，而不是單純執行預先寫死的邏輯。這讓 BA 過去慣用的功能規格、驗收條件，很難完整描述一個 agent「能做什麼、不能做什麼、什麼時候該交給人」。

🧩 **五套框架，各自對應一個治理問題**

文章提出五個具名框架，分別是：Agentic Requirements Stack（需求分層架構）、Autonomy Boundary Canvas（自主邊界畫布）、Tool Contract Specification（工具合約規格）、Escalation and Handoff Matrix（升級與交接矩陣），以及 Agentic Traceability Ledger（可追溯性帳本）。每個框架都搭配專案情境做說明，涵蓋從定義 agent 權限範圍、規範它能呼叫哪些工具與介面契約，到出錯時如何升級給人類、以及如何記錄決策軌跡以利事後追查。

💡 **不算全新概念，但把散落的治理拼圖收攏了**

從框架命名就能看出，這些概念其實脫胎於既有的 IT 治理工具：工具合約類似傳統的 API contract，升級矩陣類似客服或維運領域常見的 escalation matrix，可追溯性帳本則接近稽核日誌（audit trail）的概念。對熟悉傳統系統治理的資深 BA 來說，創新度有限；但把這些概念系統化地重新包裝成「agentic 專屬」的一套清單，對第一次面對自主性系統需求的團隊而言仍有實用價值，至少提供了一個可以照著填的起點。

🎯 **實務啟示**

在 agentic 系統專案初期，可以借用這五個框架的骨架，逐一釐清工具呼可邊界、人機交接時機與決策留痕機制，避免專案進行到一半才發現「agent 到底能不能自己下單」這種問題沒人定義清楚。

🔗 **來源**
- 標題：The Business Analyst's Guide to Agentic AI Requirements
- 作者／機構：adrian，Modernanalyst.com
- 連結：https://www.modernanalyst.com/Resources/Articles/tabid/115/ID/7213/The-Business-Analysts-Guide-to-Agentic-AI-Requirements.aspx

#AgenticAI #BusinessAnalysis #RequirementsEngineering #AIGovernance #ToolContracts #AutonomyBoundary #AIAgents #ProductManagement #Traceability #EnterpriseAI
