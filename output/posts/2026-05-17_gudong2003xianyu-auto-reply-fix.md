---
title: "GuDong2003/xianyu-auto-reply-fix"
source: GitHub Trending
url: https://github.com/GuDong2003/xianyu-auto-reply-fix
score: 40
model: tencent/hy3-preview:free
generated_at: 2026-05-17T19:47:29.985265
---

📌 閒魚自動管理開源系統  

你是否曾為了在閒魚上快速回覆訊息、自動發貨而費時費力？這個開源專案提供一鍵部署的解決方案。  

🤔 **問題來源**  
閒魚賣家常需處理大量訊息、訂單與商品上下架，手動操作耗時且易出錯。開發者希望有一套能自動化回覆、發貨與商品管理的工具，以降低人力成本。  

🧪 **系統架構**  
後端採用 FastAPI + Uvicorn，以 Python 3.11+ 進行異步編程；資料庫為 SQLite 並實現多用戶資料隔離與自動遷移。前端使用 Bootstrap 5、Vanilla JavaScript 與 Chart.js，採響應式設計。實時通信透過 WebSocket 與 SSE 完成。瀏覽器自動化依賴 Playwright 與 DrissionPage。部署方式以 Docker + Docker Compose 為主，可選擇加入 Nginx 反向代理。日誌系統採 Loguru 並支援檔案輪流；認證採 Bearer Token、圖形驗證碼與 Email 驗證。  

✨ **核心特性**  
- **多用戶系統**：支援 Email 驗證碼註冊、用戶名/Email 登入、圖形驗證碼保護；每位用戶資料完全隔離，並有嚴格的權限控制。  
- **多帳號管理**：單一用戶可管理多個閒魚帳號，每個帳號可獨立啟用/停用、查看實時狀態，支援 Cookie、帳密與備註維護，並提供一鍵或定時擦亮商品。  
- **智能回覆系統**：基於關鍵字匹配（通用、商品專屬、指定商品）與 AI 回覆（需自行接入相容模型），支援圖片關鍵字與自動發送，並設定優先級策略。  
- **自動發貨功能**：依商品資訊智慧匹配發貨規則，支援多規格、延時發貨、多種觸發條件（付款訊息、小刀卡片等），防重複處理，提供完整發貨記錄與統計。  
- **商品管理**：消息觸發時自動收集商品資訊，支援多規格配置、商品詳情編輯與智能去重。  

⚠️ **使用限制**  
本專案僅供學習與研究使用，嚴禁商業用途。使用前請詳閱版權聲明。  

🎯 **實務啟示**  
若你對瀏覽器自動化、後端 API 設計或 Docker 一鍵部署有興趣，此專案提供了完整的程式碼範例，可作為學習參考或二次開發的起點。  

🔗 **專案連結**  
📂 GuDong2003/xianyu-auto-reply-fix  
🔗 https://github.com/GuDong2003/xianyu-auto-reply-fix  

#開源專案 #閒魚 #自動化 #FastAPI #Playwright #Docker #Python #後端開發 #前端框架 #GitHub Trending
