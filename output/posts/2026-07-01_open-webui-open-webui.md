---
title: open-webui/open-webui
source: GitHub Trending
url: https://github.com/open-webui/open-webui
score: 91
model: google/gemma-4-31b-it:free
generated_at: '2026-07-01T20:36:39.259282'
---

📌 【開源專案】Open WebUI：支援完全離線執行的全功能 AI 部署平臺

TL;DR：一個可自託管、支援 Ollama 與 OpenAI API 並內建 RAG 推論引擎的 extensible AI 介面。

對於追求隱私或需要在封閉環境部署 AI 的工程師來說，最頭痛的往往不是模型本身，而是如何快速搭建一個功能完備、且能管理多個使用者的前端介面。

🧩 **支援多種推論後端與 API 整合**

Open WebUI 的設計核心在於其高度的靈活性，允許開發者自由組合不同的模型提供者：
- 本地端整合：原生支援 Ollama。
- 外部 API：只要符合 OpenAI-compatible API 規範即可接接，包括 LMStudio、GroqCloud、Mistral、OpenRouter 及 vLLM 等。
- 內建 RAG：平臺內建了推論引擎以支援 RAG (Retrieval-Augmented Generation)，讓部署方案更完整。

🚀 **從 Docker 到 Kubernetes 的快速部署**

針對不同環境的部署需求，Open WebUI 提供了多種安裝路徑：
- 快速安裝：可透過 pip 或 uv 直接安裝。
- 容器化部署：支援 Docker（提供 :ollama 與 :cuda 標記的映像檔）以及 Kubernetes（支援 kubectl, kustomize 或 helm）。

🔐 **企業級的許可權管理與擴充套件能力**

為了滿足組織內部的管理需求，該專案不僅僅是一個對話視窗，還包含了：
- 細粒度 RBAC：管理員可以定義詳細的角色 (Roles)、群組 (Groups) 與許可權，確保使用者僅能存取其所需的資源。
- 外掛系統：透過 Filters、Actions、Pipes、Tools 與 Skills 擴充套件功能。
- 外部服務連線：支援透過 MCP、MCPO 以及 OpenAPI tool servers 連線外部服務，可用於建立自定義整合、速率限制 (rate limits)、審核流程或資料連線。

🎯 **實務啟示**

對於需要快速搭建「私有 AI 聊天室」的團隊，Open WebUI 提供了一個從許可權管理到 RAG 整合的完整套件。工程師不再需要自行撰寫前端與 API 轉接層，即可將本地模型（如 Ollama）與雲端 API 混合使用，並透過其外掛系統將 AI 串接至公司內部的 OpenAPI 服務。

🔗 **來源**
- 標題：open-webui/open-webui
- 作者／機構：open-webui
- 連結：https://github.com/open-webui/open-webui

#AI #OpenSource #SelfHosted #LLM #Ollama #RAG #Kubernetes #Docker #RBAC #OpenAPI
