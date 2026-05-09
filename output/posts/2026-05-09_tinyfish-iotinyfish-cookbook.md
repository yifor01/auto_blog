---
title: "tinyfish-io/tinyfish-cookbook"
source: GitHub Trending
url: https://github.com/tinyfish-io/tinyfish-cookbook
score: 28
model: tencent/hy3-preview:free
generated_at: 2026-05-09T19:46:38.445454
---

📌 **TinyFish 免費搜尋**  

你是否曾為讓 AI agent 讀取網頁內容而煩惱？  
現在，TinyFish 的 Search 與 Fetch 端點全面免費，無需信用卡。  
只需取得金鑰，即可直接驅動你的代理。  

🤔 **為什麼需要 TinyFish**  
AI agent 若要搜尋即時網頁、讀取乾淨內容或執行多步驟瀏覽流程，傳統方式往往需要自行維護爬蟲或依賴付費服務。TinyFish 提供一層專為 agent 設計的 Web 層，讓開發者能專注於任務邏輯，而非基礎設施。  

🧪 **四大端點概覽**  
- **Search** (`api.search.tinyfish.ai`)：快速、結構化的網頁搜尋，JSON 結果， rank‑stable，響應時間 < 0.5s。  
- **Fetch** (`api.fetch.tinyfish.ai`)：任意 URL 轉乾淨 Markdown/JSON/HTML，實測瀏覽器渲染，失敗請求仍免費，可取代 Firecrawl、原生 LLM fetch 或手寫 Playwright。  
- **Agent**：提供 URL 與自然語言目標，代理自動導航、操作並回傳結構化 JSON，適合多步驟流程與資料擷取，計費方式為 Metered（依使用量）。  
- **Browser**：完全受管的雲端瀏覽器租用，適合需要完整瀏覽環境的複雜任務，同樣為 Metered。  

🔍 **核心發現**  
Search 與 Fetch 現在對所有人開放，無需信用卡，並提供慷慨的速率限制。金鑰、儀表板與端點與之前付費版完全相同，可直接用於生產環境工作負載。  

💡 **深入分析**  
免費的 Search 與 Fetch 降低了 agent 取得即時網路資訊的門檻，使開發者能以較低成本實作「讀取網頁 → 喂給 LLM」的管線。至於 Agent 與 Browser，則保留使用量計費模式，適合需要更深度互動或長時間瀏覽的場景。  

⚠️ **研究限制**  
本資訊僅來自官方儲存庫說明，未包含實際效能基準或長期穩定性數據。免費額度的具體上限與 Metered 服務的計費細節需參考官方文件。  

🎯 **實務啟示**  
1. 前往 [tinyfish-io/tinyfish-cookbook](https://github.com/tinyfish-io/tinyfish-cookbook) 取得 API 金鑰。  
2. 將 Search 或 Fetch 整合至現有的 LLM 工作流，即可獲得即時網頁資料。  
3. 若需執行複雜瀏覽任務，可嘗試 Agent 或 Browser，並注意其使用量計費。  

🔗 **論文連結**  
📂 專案：tinyfish-io/tinyfish-cookbook  
🔗 GitHub：https://github.com/tinyfish-io/tinyfish-cookbook  

#TinyFish #AIAgents #WebSearch #Fetch #開發工具 #GitHubTrending
