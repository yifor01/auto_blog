---
title: Use prompt caching with open-weight models on Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/use-prompt-caching-with-open-weight-models-on-amazon-bedrock/
model: nvidia/nemotron-3-ultra-550b-a55b:free
generated_at: '2026-11-17T01:06:46.751761'
score: 87
---

📌 **Amazon Bedrock 開放權重模型新支援 Prompt Caching，長文脈應用可大幅降本增效**

TL;DR：AWS 釋出開放權重模型的 Prompt Caching 功能，支援隱式與顯式兩種模式，重複前綴只需計算一次，輸入成本與延遲雙雙下降。

隨著系統提示、RAG 參考文件、工具定義動輒上萬 tokens，每次請求都把同一段長文脈丟給模型重跑，不僅燒錢也拖慢回應。Amazon Bedrock 近期為開放權重模型（Open-weight models）啟用 Prompt Caching，讓重複的 Prompt 前綴在首次計算後直接從快取讀取，對於多輪對話、編碼代理、文件問答等「前段固定、後段變動」的場景，效益立竿見影。

🤔 **為何現在才需要 Prompt Caching？**

過去模型上下文窗口較短，系統提示佔比有限；現在動輒 128k–1M tokens，若每輪都重算固定前綴，GPU 算力與網路頻寬都在做無意義重複運算。Bedrock 此次在 Chat Completions API（OpenAI 相容端點）上線此功能，且資料不會外洩給模型提供者或用於訓練，符合企業資安合規。

🧩 **兩種快取模式：隱式自動 vs. 顯式可控**

文章以虛構產品「AnyCompany AquaPure 500」濾水器說明書（約 4,000 tokens Markdown）為共享前綴，示範兩種模式差異：

**隱式快取 —— 免程式碼修改，適合對話流**
- 原理：Bedrock 自動偵測請求開頭是否符合既有快取前綴，採最佳努力復用。
- 關鍵排序原則：**靜態內容放前面、動態內容放後面**。系統提示 → 參考文件 → 對話歷史 → 當下問題。
- 行為：第 1 輪寫入快取；第 2、3 輪讀取系統提示與說明書，但會把新問題也延伸寫入快取（導致少量額外寫入費用）。
- 缺點：若每輪問題都不同，隱式模式會持續寫入「永不被再次讀取」的內容，若模型對快取寫入計費較高，反而增加成本。

**顯式快取 —— 開發者標記斷點，精準控制層級**
- 原理：在訊息內容中插入 `cache_breakpoint`，標示可復用前綴的結束位置。可設多個斷點（視模型上限），實現分層快取：指令 → 工具定義 → 客戶專屬文件 → 即時問題。
- 行為：僅第 1 輪寫入斷點前內容；後續請求全讀取、零寫入。動態問題段按標準輸入費率計費，避免為「一次性內容」支付較貴的快取寫入費。
- 適用：RAG 固定知識庫、多租戶系統提示、編碼代理的工具定義與對話歷史。

🛠 **實作三步走：從認證到讀取快取指標**

1. **認證**：使用 `aws-bedrock-token-generator` 套件，將 AWS 憑證換成最長 12 小時的短期 Bedrock API Key，無需管理長期金鑰。
2. **隱式範例 (`implicit.py`)**：將說明書放入 `system` 角色，問題放 `user` 角色。**注意**：若將兩者合併為單一 `user` 訊息，隱式快取將完全失效。
3. **顯式範例 (`explicit.py`)**：在系統提示結尾加入 `"cache_breakpoint": {"type": "ephemeral"}`（或依模型支援的欄位名），並可選設定 `ttl` 秒數。
4. **觀測指標**：回應物件 `usage.prompt_tokens_details` 回傳 `cached_tokens`、`cache_read_input_tokens`、`cache_write_input_tokens` 三欄，直接量化命中率與成本結構。

💡 **實戰驗證：OpenCode 編碼代理無縫接入**

OpenCode 為開源編碼代理，支援自訂 OpenAI 相容 Provider。實測中，其每輪請求包含系統提示、工具定義、完整對話歷史，極適合隱式快取。Bedrock 自動將前 N-1 輪對話作為第 N 輂的快取前綴，無需修改 Agent 程式碼即可獲得加速與省錢效果。

🎯 **工程師可執行的最佳化清單**

1. **檢查 Model Card**：確認模型支援的模式、最小前綴長度、最大斷點數、TTL 秒數與讀寫費率（讀取通常較便宜，寫入可能較貴）。
2. **Prompt 重構**：將不變的指令、文件、Schema 前置；使用者輸入、檢索結果、即時狀態後置。
3. **模式選擇**：
   - 純多輪對話、代理迴圈 → 隱式最省事。
   - 固定知識庫 + 高頻異質查詢 → 顯式斷點鎖定共享層，避免為一次性查詢付快取寫入費。
4. **冷啟動測試**：若需測量冷啟動效能，在系統提示最前加入唯一 Run ID（如 `uuid.uuid4()`）強制快取未命中。
5. **成本監控**：將 `prompt_tokens_details` 三欄寫入可觀測性系統，追蹤快取命中率與實際省下金額。

🔗 **來源**
- 標題：Use prompt caching with open-weight models on Amazon Bedrock
- 作者／機構：Dustin Liu @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/use-prompt-caching-with-open-weight-models-on-amazon-bedrock/

#AWS #AmazonBedrock #PromptCaching #LLM #OpenWeightModels #GenerativeAI #CostOptimization #LatencyReduction #ChatCompletionsAPI #OpenCode
