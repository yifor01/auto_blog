---
title: "ZhuLinsen/daily_stock_analysis"
source: GitHub Trending
url: https://github.com/ZhuLinsen/daily_stock_analysis
score: 83
model: tencent/hy3-preview:free
generated_at: 2026-05-10T19:29:19.345229
---

📌 【開源專案】AI 驅動的每日股票決策儀表板  

每天早上花半小時看盤、寫報告，是否其實可以交給 AI？這個開源專案主張：只要 Fork 一下，設定 API Key，就能自動產出多市場決策報告並推送到你常用的通訊軟體。  

🤔 **個人投資者常被資訊淹沒，卻缺乏系統化的決策工具**  
散戶在面對 A股、港股、美盤時，常需同時查詢行情、技術指標、資金流、新聞與基本面，手動彙整耗時且易遺漏關鍵訊號。缺乏一套能自動產出「決策儀表盤」的工具，使得資訊處理成為投資決策的瓶頸。  

🧪 **基於 LLM 的多代理工作流與多來源數據聚合**  
系統核心透過大語言模型（支援 Anspire、AIHubMix、Gemini、OpenAI‑相容、DeepSeek、通義千問、Claude、Ollama 本地模型等）生成 AI 決策報告，內容包含核心結論、評分、趨勢、買賣點位、風險警報、催化因素與操作檢查清單。同時，它整合了 TickFlow、AkShare、Tushare、Pytdx、Baostock、YFinance、Longbridge 等行情資料源，以及 Anspire、SerpAPI、Tavily、Bocha、Brave、MiniMax、SearXNG 新聞搜尋與 Stock Sentiment API（Reddit/X/Polymarket，僅美股可選）社交舆情，實現多市場（A股、港股、美股、ETF）的全方位數據聚合。  

📊 **功能清單：從決策儀表盤到跨平台自動推送**  
- **Web / 桌面工作台**：手動分析、任務進度、歷史報告、完整 Markdown、回測、持倉、配置管理、淺色／深色主題  
- **Agent 策略問股**：多輪追問，內建 11 種策略（均線、缠论、波浪、趨勢等），支援 Web/Bot/API  
- **智能導入與補全**：圖片、CSV/Excel、剪貼板導入；股票代碼／名稱／拼音／別名自動補全  
- **自動化與推送**：GitHub Actions、Docker、本地定時任務、FastAPI 服務；可推送至企業微信、飛書、Telegram、Discord、Slack、郵件  
- **快速開始**：透過 GitHub Actions 5 分鐘完成部署，零伺服器成本；只需 Fork 專案並設定相應的 API Key 秘密（如 ANSPIRE_API_KEYS、AIHUBMIX_KEY、GEMINI_API_KEY 等）  

💡 **開源與可擴充的設計讓使用者可自行換模型、加策略**  
因為所有模型與數據源皆透過環境變數或設定檔注入，開發者可以依需求切換至其他 LLM（例如自行部署的 Ollama 模型）或增加新的技術指標與策略模組。這種「插件式」架構不僅降低了使用門檻，也提供了學習 LLM 與金融數據整合的實作平台。  

⚠️ **依賴外部 API 金鑰與數據源，離線使用需自行部署本地模型**  
該專案本身並未提出新理論或演算法，而是將現有開源資料庫與 LLM 服務結合。若在無法連線的環境中使用，必須自行架構本地模型（如 Ollama）並準備相應的行情與新聞數據源，否則部分功能將受限。此外，因為它是社群維護的工具，文件與穩定度可能隨貢獻者變動而有所波動。  

🎯 **工程師可快速搭建自己的 AI 金融助手，或作為學習 LLM 與金融數據整合的練習項目**  
- 直接 fork 後透過 GitHub Actions 實現每日自動報告，適合想要省時的個人投資者  
- 修改 `llm_config.yaml` 或 `data_source.yaml` 可快速實驗不同模型與數據源的組合  
- 參考 `agent/` 目錄內建的 11 種策略，擴充自選的技術指標或基本面模型  

🔗 **資源連結**  
📂 專案：https://github.com/ZhuLinsen/daily_stock_analysis  
📖 文件中心：同倉庫內的 `docs/` 目錄  
💡 快速開始：參考倉庫 README 中的「方式一：GitHub Actions（推薦）」章節  

你是否已經嘗試過讓 AI 幫你產出投資報告？歡迎在留言區分享你的設定經驗或改進想法 👇  

#AI #股票分析 #開源專案 #LLM #FinTech #GitHubTrending #ZhuLinsen #日常自動化 #投資工具 #量化交易 #決策儀表盤 #多市場 #自動推送 #工程實作 #學習資源
