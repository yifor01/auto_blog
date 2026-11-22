---
title: Google AI Previews Tool Retrieval in the Gemini API for Large Tool Libraries
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/22/google-gemini-api-tool-retrieval/
model: claude-code/sonnet
generated_at: '2026-11-22T22:36:09.377321'
score: 91
---

📌【Google最新功能】Gemini API工具延遲載入，省掉萬級token

TL;DR：Gemini API新增Tool Retrieval，模型用到工具才載入參數schema，省掉多餘token。

當一個 Agent 身上掛了五十幾個工具，光是把所有工具的參數規格塞進 prompt，可能在任務還沒開始之前就先燒掉數萬個 token。

🤔 真實成本：工具定義本身就是一筆開銷

Google 在 Gemini API 的 Interactions API 中預覽了 Tool Retrieval 功能。官方文件直接點出問題：幾十個函式宣告（function declaration）就能在每一次請求中消耗掉數萬個 token。Tool Retrieval 讓 Agent 可以保留一個很大的工具庫，卻不必在每個 prompt 裡都把每個工具的參數 schema 送出去,模型只會在真正需要某個工具時，才載入它的 schema。在延遲載入的狀態下，模型一開始只看得到工具的名稱與一段簡短描述，看不到參數 schema。

🧩 怎麼設定：defer_loading 加 tool_search

做法是在 tools 陣列中加入 {"type": "tool_search"}，再對想要延遲載入的每個函式設定 defer_loading: true。Google 的 @googledevs 發布貼文示範了一個在 gemini-4-hydrogen 上延遲載入的 issue_refund 函式，程式碼註解提到還有 50 多個其他函式同樣被延遲載入。當模型需要用到某個被延遲的工具時，回應會包含三個步驟,其中前兩步由 API 自己處理，開發者的應用程式只需要負責執行 function_call 並回傳 function_result。被延遲的函式還可以額外帶一個 short_description，在檢索時顯示，但只有在 defer_loading 為 true 時才有效。

伺服器端（server-side）是預設模式,搜尋工作由 Gemini 自己完成，不需要額外建立或維護任何索引。客戶端（client-side）模式則透過 "execution": "client" 設定，改由開發者自己的應用程式做查找（例如 embedding 索引、工具註冊表或權限過濾），再把符合條件的函式宣告放進 function_result.result 回傳,這些工具甚至可以在對話中途加入，即使它們一開始沒有出現在 tools 陣列裡。但客戶端每次搜尋都要多一次往返；兩種模式不能在同一次請求中混用，而且一次請求只能放一個 tool_search。

🧩 和MCP、快取之間的關係

這個機制也支援 MCP：在 mcp_server 項目上設定 defer_loading: true，會讓該伺服器曝露的所有工具一併延遲載入，被延遲的 MCP 工具仍然透過 Gemini API 的 MCP 支援在遠端執行。在快取方面，延遲載入的 schema 不會出現在 prompt 的前綴部分；一旦被載入，schema 就會以行內（inline）形式附加，仍適用既有的隱式快取（implicit caching）。文件也提醒了一個反例：延遲載入工具可能讓 prompt 縮小到低於可快取的最小長度門檻。

計費上沒有額外收費，所有 token 仍按模型標準的輸入、快取與輸出費率計算。但每一次伺服器端搜尋，都會對完整上下文觸發一次額外的模型呼叫,這些 token 會算進 total_tool_use_tokens，以輸入費率計費；之後每個被載入的 schema，在整段對話剩餘的時間裡都會持續以輸入 token 計費。文件也指出,對於小型工具庫或每輪都要搜尋的情境，靜態載入（不延遲）反而可能更省錢。

⚠️ 限制：不是萬能節省，也還沒有可比較的數字

Tool Retrieval 並非無條件省錢：工具庫小、或每輪對話都要重新搜尋的情境,靜態載入可能更划算；兩種模式互斥，且每次請求只能用一個 tool_search，限制了彈性。文件也提到 Anthropic 與 OpenAI 已經推出類似的工具搜尋功能，並各自公布了節省幅度的數字,但這些數字都是各家自行測出的結果，彼此之間、以及和 Gemini 之間都不能直接比較。

🎯 實務啟示

對接了幾十個函式或多個 MCP 伺服器的 Agent 開發者，是這個功能的直接受益對象:把工具定義從「每次都送」改成「要用才送」，是一個不需要改變 Agent 邏輯、純粹靠 API 層級設定就能落地的最佳化。評估是否要開啟時，值得先用自己的工具庫大小與對話輪數估一下帳,工具少或搜尋頻繁時，靜態載入可能仍是更省的選項。

🔗 來源
- 標題：Google AI Previews Tool Retrieval in the Gemini API for Large Tool Libraries
- 作者／機構：Michal Sutter @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/22/google-gemini-api-tool-retrieval/

#GeminiAPI #GoogleAI #LLMAgent #ToolUse #MCP #PromptEngineering #TokenOptimization #AIInfrastructure #FunctionCalling #APIDesign
