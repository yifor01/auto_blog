---
title: How to Build a Simple AI Web Scraper with Python
source: KDnuggets
url: https://www.kdnuggets.com/how-to-build-a-simple-ai-web-scraper-with-python
model: nvidia/nemotron-3-ultra-550b-a55b:free
generated_at: '2026-08-15T06:26:24.394064'
score: 71
---

📌 用 Python 打造 AI 網頁爬蟲：清洗 HTML、轉 Markdown、餵給 LLM 只回你要的答案

TL;DR：把整頁 HTML 清洗轉 Markdown 再丟給小模型，省 Token 又能直接拿結構化回答。

網頁爬蟲抓回來的通常是滿屏雜訊——導覽列、腳本、追蹤像素、Cookie 標語。若直接整頁餵給 LLM，不僅浪費 Token，回答也會夾雜無關資訊。KDnuggets 這篇手把手教學，示範用 `requests` + `BeautifulSoup` + `markdownify` 三步驟把網頁「洗乾淨」，再丟給 `gpt-5.4-nano` 只回使用者問的那一段。

🎣 **為什麼不直接丟原始 HTML？**

完整網頁常含導覽、彈窗、表單、Footer、重複區塊。這些雜訊會：
- 佔用大量輸入 Token，推高成本
- 干擾模型注意力，降低回答精準度
- 回傳結果難以在下游流程直接使用

教學採取「先清洗、再轉換、最後問答」的管線，讓 LLM 只看乾淨的 Markdown 內容。

🧩 **核心管線：三個函式串起完整流程**

素材提供完整 Jupyter Notebook 實作，關鍵步驟如下：

1. **抓取網頁** (`fetch_page`)
   - 用 `requests.get` 加上自訂 `User-Agent` 與 15 秒 `timeout`
   - `raise_for_status()` 讓非 2xx 回應直接拋例外

2. **清洗 HTML** (`clean_html`)
   - `ftfy.fix_text` 修復編碼亂碼
   - `BeautifulSoup` 解析後 `decompose()` 移除明顯雜訊標籤：`script`、`style`、`nav`、`header`、`footer`、`form`、`button`、`iframe`、`svg`、`img`、`noscript`、`aside`
   - 再掃描所有標籤的 `class` 與 `id`，含 `popup`、`cookie`、`navbar`、`newsletter`、`modal` 等關鍵字者一併移除
   - 最後回傳 `<body>` 內容（若無則回傳整份 soup）

3. **轉 Markdown** (`html_to_markdown`)
   - `markdownify` 參數 `heading_style="ATX"`、`bullets="-"` 輸出標準 Markdown
   - 正則移除圖片語法 `![...](...)`、多餘空白、超過兩行的連續換行
   - 過濾常見雜訊行（如 "click to try"、"wait..."、"product"、"resources" 等）

清洗後的 Markdown 直接作為 System/Assistant 訊息餵給 OpenAI API，提示詞要求「根據網頁內容以 Markdown 回覆使用者問題」。

💻 **最小可行範例（素材完整程式碼節錄）**

```python
# 安裝套件
!pip install requests beautifulsoup4 markdownify openai ftfy python-dotenv

# 關鍵導入
import os, re, requests
from bs4 import BeautifulSoup, Comment
from ftfy import fix_text
from markdownify import markdownify as markdownify_html
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL_NAME = "gpt-5.4-nano"   # 素材使用的小型模型

# 1. 抓取 → 2. 清洗 → 3. 轉 Markdown → 4. 問答
raw   = fetch_page("https://www.olostep.com/")
clean = clean_html(raw)
md    = html_to_markdown(clean)

resp = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {"role": "system", "content": f"Webpage content:\n{md}"},
        {"role": "user",   "content": "這個網站主要提供什麼服務？"}
    ]
)
print(resp.choices[0].message.content)
```

素材完整定義了 `fetch_page`、`clean_html`、`html_to_markdown` 三個函式，可直接複製到 Notebook 執行。

⚠️ **限制與注意事項（僅依素材整理）**

- 需自備 OpenAI API Key 並已完成帳單設定（新帳號需先儲值）
- `gpt-5.4-nano` 若不可用，需自行換成帳號可用的模型
- 清洗規則以關鍵字比對為主，不同網站可能需調整 `noise_words` 與 `skip_lines`
- 教學環境為 Jupyter Notebook，部署成 API 或應用需自行封裝
- 素材未提及對 JavaScript 渲染頁面、分頁、反爬蟲機制的處理

🎯 **實務啟示：把「清洗→轉換→問答」變成可重複使用的模組**

對工程師而言，這篇教學的價值在於示範一個 **可複製、可擴充的前處理管線**：
1. **可換模型**：只需改 `MODEL_NAME` 即可切換至本地模型或其他供應商
2. **可擴充清洗規則**：`noise_words`、`skip_lines` 以列表維護，新增網站特有雜訊只需加關鍵字
3. **可串接 RAG**：輸出的 Markdown 可直接作為檢索單元或向量化切片來源
4. **Token 成本可控**：清洗後內文通常只有原始 HTML 的 10–30%，大幅降低 API 費用

下次需要「抓網頁→問問題」時，直接把這三個函式包成套件匯入，比起每次重寫正則表達式更易維護。

🔗 **來源**
- 標題：How to Build a Simple AI Web Scraper with Python
- 作者／機構：Abid Ali Awan / KDnuggets
- 連結：https://www.kdnuggets.com/how-to-build-a-simple-ai-web-scraper-with-python

#Python #WebScraping #LLM #OpenAI #BeautifulSoup #Markdown #DataCleaning #AIEngineering #JupyterNotebook #TokenOptimization
