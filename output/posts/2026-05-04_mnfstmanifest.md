---
title: "mnfst/manifest"
source: GitHub Trending
url: https://github.com/mnfst/manifest
score: 107
model: tencent/hy3-preview:free
generated_at: 2026-05-04T20:24:12.132720
---

📌 **Manifest 智能路由省 70% AI 成本**

AI 應用、Agent 的模型調用成本越來越高？
接了多家供應商還想跑本地模型，管理混亂到崩潰？
這款 GitHub Trending 工具號稱最高可省 70% 支出。

🤔 **多模型 AI 應用成本飆漲，供應商管理碎片化**
當前 Agent 與 AI 應用團隊若需調用多個模型供應商，往往面臨成本失控、管理介面碎片化的問題：既要維護不同供應商的 API 金鑰，可能還要管理訂閱方案、本地部署模型，成本優化難度極高。

🧩 **智能路由按查詢特性匹配最適模型，降本最高 70%**
Manifest 是專為 Agent 與 AI 應用設計的智能模型路由器，會根據每個查詢的複雜度、特異性與自訂 HTTP 標頭，自動將請求導向最合適的模型，官方宣稱最高可節省 70% 的 AI 支出。

🔧 **支援 16 家供應商 300+ 模型，混搭本地與訂閱方案**
核心功能完全基於實務需求設計：
- 路由邏輯：基於查詢複雜度、特異性、自訂 HTTP 標頭導流
- 供應商混搭：支援 API 金鑰、已付訂閱、本地模型、自訂供應商（相容 OpenAI/Anthropic 格式）
- 成本管控：追蹤每筆支出，可設定通知與限額
- 容錯機制：查詢失敗時自動 fallback 至其他模型
- 統一端點：所有模型均透過同一 /auto 端點調用，可自帶 API 金鑰、復用既有付費訂閱或運行本地模型

🚀 **雲端版即開即用，自託管僅需一條 Docker 指令**
Manifest 提供兩種部署方式：
1. 雲端版：直接前往 app.manifest.build 依指引操作即可使用
2. 自託管：以 Docker 映像檔提供，執行單一指令即可部署：
`bash <( curl -sSL https://raw.githubusercontent.com/mnfst/manifest/main/docker/install.sh )`
部署後開啟 http://localhost:2099 註冊，首個註冊帳號將自動成為管理員，完整自託管指南可參考 docker/DOCKER_README.md。

📋 **支援復用 ChatGPT/Claude 訂閱，覆蓋主流大模型**
Manifest 目前連接 16 家供應商共 300+ 模型，也支援任何自訂供應商（需相容 OpenAI/Anthropic 格式），已確認支援的供應商包含：
- OpenAI：支援 API 金鑰、ChatGPT Plus/Pro/Team 訂閱，對應模型 gpt-5、gpt-5-mini、o4、o4-mini
- Anthropic：支援 API 金鑰、Claude Max/Pro 訂閱，對應模型 claude-opus-4-7、claude-sonnet-4-6、claude-haiku-4-5
- Google：支援 API 金鑰，對應模型 gemini-2.5-pro、gemini-2.5-flash、gemini-2.0-flash
- xAI：支援 API 金鑰，對應模型 grok-4、grok-3、grok-code-fast
- DeepSeek：支援 API 金鑰，對應模型 deepseek-v3.2、deepseek-r1
- Mistral：支援 API 金鑰，對應模型 mistral-large、codestra

⚠️ **舊版 npm 套件已棄用，路由概念非全新**
需注意兩點客觀限制：
1. 舊版 manifest npm 套件已正式棄用，不再發布更新
2. 模型路由與 fallback 機制並非全新概念，本專案的優勢在於整合多項實用功能

🎯 **擴展多模型生態的團隊可立即降本，簡化開發**
對於正在擴展多模型生態的 AI 工程團隊，Manifest 的統一 /auto 端點可大幅簡化開發流程，結合成本追蹤與自動路由，能快速實現 AI 成本優化，具備明確的實務應用價值。

🔗 **專案連結**
- 專案名稱：mnfst/manifest
- 來源：GitHub Trending
- GitHub 連結：https://github.com/mnfst/manifest
- 雲端版入口：app.manifest.build

你們團隊目前有 AI 成本優化的需求嗎？歡迎分享你的解法 👇

#GitHub #AI開發 #成本優化 #模型路由 #Manifest #AI應用 #Agent #多模型
