---
title: "OpenAI Adds Chrome Extension to Codex, Letting Its AI Agent Access LinkedIn, Salesforce, Gmail, and Internal Tools via Signed-In Sessions"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/08/openai-adds-chrome-extension-to-codex-letting-its-ai-agent-access-linkedin-salesforce-gmail-and-internal-tools-via-signed-in-sessions/
score: 98
model: tencent/hy3-preview:free
generated_at: 2026-05-09T19:28:23.844749
---

📌 【OpenAI 新功能】Codex 加入 Chrome 擴充套件，可直接使用已登入的瀏覽器存取 LinkedIn、Salesforce、Gmail 與內部工具  

🎣 你是否曾希望 AI 能直接操作你已登入的工作頁面，而不必複製貼上或手動切換？OpenAI 最近的更新讓這成為可能。  

🤔 **為何此功能必要**  
在 Codex 推出後，使用者多半選擇在瀏覽器中完成工作，因為此時可以直接呼叫「Computer Use」等功能。然而，早期的 Codex 只有兩種方式：內建的沙盒瀏覽器（適用於本地預覽）以及針對 GitHub、Slack、Figma、Notion 等服務的專用插件。這兩種方式無法覆蓋需要真實、已登入瀏覽器狀態的情境，例如讀取或修改 LinkedIn 個人資料、更新 Salesforce 紀錄、操作公司內部工具等。  

🧪 **擴充套件如何運作**  
OpenAI 現在提供了一個適用於 Mac 與 PC 的 Codex Chrome 擴充套件。當 Codex 需要執行必須使用使用者已登入的瀏覽器狀態時，它會呼叫此擴充套件，讓 Chrome 成為其操作環境。對於不需要登入的任務——如本地開發伺服器、檔案預覽或公開網頁——Codex 仍會使用內建的沙盒瀏覽器，以避免干擾使用者的 Chrome 設定。  

Codex 現在會根據任務自動選擇三種工具層級：  
- **插件**：當有專門整合時使用；  
- **Chrome**：當需要已登入瀏覽器內容時使用；  
- **內建瀏覽器**：適用於 localhost 預覽。  

使用者也可以在提示中直接呼叫 Chrome，例如 `@Chrome open Salesforce and update the account from these call notes`。若 Chrome 尚未開啟，Codex 會自行啟動它。  

📊 **核心發現**  
此擴充套件讓 Codex 能夠：  
- 直接測試網頁應用程式；  
- 在多個開啟的標籤頁中收集上下文資訊；  
- 在使用者進行其他作業時，同時呼叫 Chrome DevTools 進行偵錯或檢查。  

更重要的是，Codex 會在任務專用的標籤群組中運作，因而能夠蒐集資訊與執行動作而不會佔用或干擾使用者目前的瀏覽器視窗。  

💡 **為何這是重要的一步**  
此更新填補了先前插件與沙盒瀏覽器無法覆蓋的實際工作流程缺口。對於需要頻繁與 CRM、郵件或內部管理系統互動的工程師而言，AI 現在可以在不離開對話介面的情況下，讀取最新的客戶紀錄、根據郵件內容更新任務狀態，或直接在公司內部工具上執行例行操作。這種「登入瀏覽器情境」的支援，使得 Codex 從純粹的程式輔助工具向更完整的網頁工作流程助理邁進。  

⚠️ **目前的限制與注意事項**  
- 該擴充套件僅支援 Chrome（Mac 與 PC 版），其他瀏覽器暫未提及支援計畫。  
- 功能依賴使用者已登入的瀏覽器狀態；若使用者未登入或使用隱私模式，相應操作將無法執行。  
- 作為新發布的功能，尚未公開詳細的使用量或長期穩測資料，實際表現仍需社群回饋驗證。  

🎯 **開發者如何善用**  
- 在需要快速查看或更新客戶資訊時，使用 `@Chrome open LinkedIn` 讀取個人檔案，再由 Codex 甄別後續行動。  
- 撰寫或測試內部工具時，讓 Codex 在同一個標籤群組中執行操作，減少視窗切換帶來的認知負擔。  
- 結合 DevTools 功能，讓 Codex 在背景偵錯時，您專注於程式碼撰寫或設計工作。  

🔗 **文章連結**  
📝 OpenAI Adds Chrome Extension to Codex, Letting Its AI Agent Access LinkedIn, Salesforce, Gmail, and Internal Tools via Signed-In Sessions  
👤 作者：Asif Razzaq（MarkTechPost）  
🔗 https://www.marktechpost.com/2026/05/08/openai-adds-chrome-extension-to-codex-letting-its-ai-agent-access-linkedin-salesforce-gmail-and-internal-tools-via-signed-in-sessions/  

你已經試著讓 Codex 操作你的工作頁面了嗎？歡迎在留言區分享你的使用心得或遇到的挑戰 👇  

#OpenAI #Codex #AI Agent #Chrome Extension #生產力工具 #軟體工程 #LinkedIn #Salesforce #Gmail #內部工具
