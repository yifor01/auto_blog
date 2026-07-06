---
title: 'Structured PDF-to-JSON: A Guide to Open-Source Extraction Models in 2026'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/04/structured-pdf-to-json-a-guide-to-open-source-extraction-models-in-2026/
score: 89
model: google/gemma-4-31b-it:free
generated_at: '2026-07-06T20:32:35.347666'
---

📌 Structured PDF-to-JSON：2026 年開源抽取模型指南  

TL;DR：開源模型可在本地將 PDF 轉為結構化 JSON，適合發票、表單與 RAG 資料前處理，成本與隱私優於專有 API。  

🎣 開場鉤子  
企業資料大量鎖在 PDF、掃描件與投影片內，但大型語言模型與代理只能使用結構化 JSON。若每頁都要付費傳送至雲端 API，成本與資安風險都會急速上升。  

🧩 方法或架構  
文章指出「PDF to JSON」實際上涵蓋兩種不同任務：  

1. ** schema‑driven extraction**（結構化抽取**：使用者先給定 JSON schema，模型根據該 schema 抽取對應欄位的數值。適用於欄位已知的檔案，如發票、表單、合約與收據。  
2. ** document parsing檔案解析**：模型不依賴預先定義的 schema，而是重建頁面版面、閱讀順序、表格、公式與程式碼，最後輸出 JSON 或 Markdown。適合製作乾淨語料庫，供 RAG 與代理使用。  

開源模型的關鍵優勢在於「open weights」：模型權重可下載至本地硬體執行，避免將敏感檔案上傳至第三方服務，同時省除每百萬頁數千美元的 API 費用。  

📊 資料或結果  
文中重點介紹了一個名為 **lift** 的開源模型：  

- 來源：Datalab（Marker 與 Surya 團隊）  
- 模型規模：9B 視覺模型，基礎架構為 Qwen 3.5  
- 部署方式：可透過 Hugging Face 在本地執行，或透過 vLLM 伺服器遠端呼叫  
- 功能特色：  
  - 接收 JSON schema，輸出符合該 schema 的 JSON（schema‑constrained decoding 確保輸出合法）  
  - 支援多頁檔案單通過處理，包括跨頁的數值  
  - 提供 CLI、Python API 與 Streamlit「Schema Studio」（用於建構與測試 schema）  
- 基準測試：在 Datalab 自建的 225 份檔案基準上，lift 達到 **90.2%** 欄位準確率，中位數延遲 **9.5 秒**  
- 對比結果：  
  - 優於 NuExtract3（81.5%）與 Qwen3.5‑9B（76.3%）  
  - 落後於 Gemini Flash 3.5（91.3%）以及文中未完整列出的某個宿主模型  

💡 深入分析  
lift 的設計將視覺理解與結構化輸出緊密結合：先利用 9B 視覺 backbone 讀取頁面影像，再透過 schema‑constrained decoding 直接產生合法 JSON，避免後處理步驟可能導致的格式錯誤。單通過多頁處理減少了模型載入與特徵重複計算的開銷，這在處理大量掃描檔案時顯著降低延遲。然而，基準資料僅來自單一內部測試集，未見公開的跨域或長尾檔案評估，因此在真實雜錯版面或低品質掃描上的表現仍需進一步驗證。  

⚠️ 限制  
- 文章未提供 lift 在極端長檔案（超過數百頁）或極低解析度掃描上的實測資料。  
- 基準結果僅針對「欄位準確率」單一指標，未涵蓋結構完整度（例如層級正確度）或 Markdown 輸出品質。  
- 文中提到 lift 「落後於 Gemini Flash 3.5 以及某個宿主模型」，但該宿主模型名稱未完整給出，無法直接比較。  

🎯 實務啟示  
對於需要在本機處理敏感檔案、控制成本或避免網路傳輸的團隊，lift 提供了一個可直接下載的開源選擇。若主要目標是從固定格式的表單或發票中抽取已知欄位，可先使用其 schema‑driven extraction 功能；若目標是製備乾淨的語料庫供 RAG 或代理消費，則可嘗試其 document parsing 功能輸出 JSON/Markdown。在實際部署前，建議先在內部樣本上跑一下基準，確認準確率與延遲符合業務容忍度後再擴大使用。  

🔗 來源  
- 標題：Structured PDF-to-JSON: A Guide to Open-Source Extraction Models in 2026  
- 作者／機構：Michal Sutter @ MarkTechPost  
- 連結：https://www.marktechpost.com/2026/07/04/structured-pdf-to-json-a-guide-to-open-source-extraction-models-in-2026/  

#PDF #JSON #OpenSource #DocumentExtraction #LLM #RAG #DataEngineering #AI #MarkTechPost #Datalab
