---
title: "Models.dev: open-source database of AI model specs, pricing, and capabilities"
source: Hacker News
url: https://github.com/anomalyco/models.dev
score: 88
model: tencent/hy3-preview:free
generated_at: 2026-05-23T19:39:36.940744
---

📌 Models.dev Hub  

你有花費時間在各家 AI 模型的定價與特性表格間來回切換嗎？一個開源資料庫正試圖把這些資訊集中在一起。  
社群正在維護這個專案，讓任何人都能快速查詢與貢獻模型資料。  

🤔 **缺乏統一的 AI 模型資訊來源**  
目前市面上散落在不同供應商文件、部落格或商業目錄中的模型規格、定價與能力資訊，缺乏一個統一、易於程式化查詢的來源。這使得工程師在選型或成本評估時，需要手動蒐集與交叉比對。  

🧪 **社群維護的 TOML 資料與公開 API**  
Models.dev 將所有資料儲存為 TOML 檔案，依供應商（provider）分目錄管理。任何人都可以透過 Pull Request 貢獻或更新模型條目。資料可經公開 API 取得：`curl https://models.dev/api.json`，供應商的 Logo 也可透過 `https://models.dev/logos/{provider}.svg` 直接下載（若無則回傳預設 Logo）。  

📊 **核心發現：提供模型規格、定價與能力的集中目錄**  
該專案旨在成為一個開源、社群驅動的資料庫，收錄各家 AI 模型的參數規模、定價結構、支援的功能（例如多模態、工具使用等），並以統一的 Model ID 作為查詢鍵，方便與 AI SDK 等工具整合。  

💡 **深入分析：實用但與現有平台有重疊**  
Models.dev 提供即時、可程式化存取的模型目錄，對需要快速比較或自動化工作流程的工程師而言，具備實用價值。然而，其功能與既有的模型中心（如 Hugging Face Model Hub）在資料覆蓋上有所重疊，因此在創新程度上屬於補充式而非顛覆性的貢獻。  

⚠️ **研究限制：尚未突破現有生態系統的創新點**  
作為社群專案，其資料深度與及時性依賴貢獻者的積極程度；目前尚未顯示出明確的獨家資料或功能，能顯著區別於現有成熟平台。  

🎯 **實務啟示：適合工程師快速比較與引用**  
對於需要在多個供應商間進行成本效益評估、自動化選型或產生模型卡片的開發者，Models.dev 提供了一個簡單且開放的資料來源，可直接透過 API 整合到腳本或內部工具中。  

🔗 **論文連結**  
📝 Models.dev: open-source database of AI model specs, pricing, and capabilities  
👤 由 maxloh 維護（社群貢獻）  
🔗 GitHub：https://github.com/anomalyco/models.dev  
🔗 API 範例：`curl https://models.dev/api.json`  
🔗 Logo 範例：`curl https://models.dev/logos/openai.svg`  

Hacker News：149 點，27 則留言  

#AI #ModelsDev #OpenSource #機器學習 #模型選型 #API #GitHub #HackerNews
