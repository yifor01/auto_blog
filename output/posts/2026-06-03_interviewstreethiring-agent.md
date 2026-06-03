---
title: interviewstreet/hiring-agent
source: GitHub Trending
url: https://github.com/interviewstreet/hiring-agent
score: 98
model: tencent/hy3-preview:free
generated_at: '2026-06-03T21:40:33.326918'
---

📌 【開源】Hiring Agent：AI 履歷評分  

你是否曾為堆積如山的履歷感到頭痛？傳統篩選不只耗時，也易受主觀偏見影響。這個剛上 GitHub Trending 的開源專案，試圖讓 AI 來幫忙「讀履歷、打分數、說明理由」。  

🤔 **履歷篩選的痛點與自動化的可能**  
面對大量應徵者，人力資源或技術面試官常需花費數小時手動閱讀 PDF，同時難以確保每份履歷都被同樣的標準衡量。若能讓模型自動抽取關鍵資訊、補充 GitHub 公開資料，並給出可解釋的分數，不只能提升效率，還能讓評比過程更透明。  

🧪 **端到端的 LLM 驅動管線**  
專案的核心是一套「Resume‑to‑Score」流程，主要步驟如下：  
1. **pymupdf_rag.py** 將 PDF 頁面轉換為類 Markdown 文字。  
2. **pdf.py** 依照 section 使用 Jinja 模板（位於 prompts/templates）呼叫 LLM，抽取結構化 JSON。  
3. **github.py** 抓取應徵者的 GitHub 個人資料與倉庫，對專案進行分類，並請 LLM 選出前 7 個最具代表性的作品。  
4. **evaluator.py** 在公平性約束下執行嚴格的評分，產出類別分數、證據、加分與扣分項目。  
5. **score.py** 統籌上述步驟，開發模式下會輸出 CSV 方便後續分析。  

關鍵模組還包括：  
- **models.py**：Pydantic 結構與 LLM 提供者介面。  
- **llm_utils.py**：提供者初始化與回應清理。  
- **transform.py**：將鬆散的 LLM JSON 轉為 JSON Resume 標準格式。  

整個流程可以完全在本地運行（透過 Ollama），也可切換至 Google Gemini 作為後端。  

💡 **可解釋的評分與 GitHub 訊號增強**  
與單纯依賴 LLM 直接給分不同，Hiring Agent 會：  
- 把履歷內容切分為教育、經驗、技能等區塊，分別讓模型抽取。  
- 透過 GitHub 訊號（專案語言、星星數、貢獻度等）補充程式實力的客觀證據。  
- 在評分階段明確列出每項分數的依據（例如「證據：GitHub 上有 3 個 Python 專案，總星星數 1.2k」），讓使用者能追溯為何會得到這樣的分數。  

這種「抽取 → 增強 → 評分」的設計，不只提供數字結果，更附帶可閱讀的說明，有助於面試官快速了解分數背後的理由。  

⚠️ **已知的限制與使用注意**  
- 依賴外部 LLM 的品質：抽取與評分的準確度會隨所選模型（Ollama 本地模型或 Google Gemini）而異。  
- GitHub 訊號的取得需網路連線，且僅能處理公開的個人資料與倉庫。  
- 目前的文件與範例主要示範基本流程，尚未提供大規模基準測試或與現有 ATS 系統的對比實驗。  
- 安裝前需確保 Python 3.11+（repository 已鎖定 .python-version 為 3.11.13），並自行準備一個可用的 LLM 後端。  

🎯 **實務上的啟示與建議**  
- 若你正在尋找可自行部署、透明度高的履歷初篩工具，這個專案提供了完整的程式碼與設定範本，可直接 clone 後依照 README 安裝。  
- 在實際使用時，建議先以小批量履歷跑通流程，觀察 LLM 抽取的 JSON 是否符合預期，再逐步調整 prompts/templates 中的 Jinja 模板以貼合貴公司的職缺描述。  
- 由於評分過程是可解釋的，面試官可以將產出的 CSV 與證據欄位一起閱讀，既提升效率又保留人工複核的空間。  

🔗 **專案連結**  
📂 Hiring Agent – interviewstreet/hiring-agent  
🔗 https://github.com/interviewstreet/hiring-agent  

你有試過用 AI 協助履歷篩選嗎？歡迎在留言區分享你的經驗或對這種「抽取＋增強＋評分」流程的看法 👇  

#AI #履歷篩選 #HiringAgent #Ollama #GitHub #開源工具 #TechTrend
