---
title: zubair-trabzada/geo-seo-claude
source: GitHub Trending
url: https://github.com/zubair-trabzada/geo-seo-claude
score: 72
model: google/gemma-4-31b-it:free
generated_at: '2026-06-20T19:45:28.205583'
---

📌 GEO‑first SEO 工具「geo‑seo‑claude」：讓網站適配 AI 搜尋流量  

TL;DR：一鍵腳本優化網站，針對 ChatGPT、Claude 等 AI 搜尋引擎的 GEO‑first 排名，同時保留傳統 SEO 基礎。

🧩 為何需要 GEO‑first、AI‑supported SEO  

隨著 AI 產生的搜尋結果（ChatGPT、Claude、Perplexity、Gemini、Google AI Overviews）逐漸取代傳統關鍵字搜尋，流量來源正從「過去的關鍵字」轉向「即時 AI 推薦」。README 中指出 AI‑referenced 流量年增長率高達 527%，且 AI 流量的轉換率是一般自然搜尋的 4.4 倍。Gartner 甚至預測到 2028 年傳統搜尋流量會下降 50%。因此，網站若僅依賴舊有 SEO 做法，將錯失快速成長的 AI 流量。

🧩 專案核心功能與設計理念  

- **GEO‑first、AI‑supported**：工具以地理位置（GEO）為優先，針對 AI 搜尋引擎的地區化回應進行優化，同時不拋棄傳統 SEO（如 meta 標籤、結構化資料）。  
- **單指令安裝**：提供 macOS、Linux 以及 Windows（Git Bash）的一鍵安裝腳本，使用 `curl … | bash` 直接下載並執行 `install.sh`（或 `install-win.sh`）。  
- **手動安裝選項**：若不願使用一鍵腳本，可自行 `git clone` 專案並執行安裝腳本。  
- **執行環境**：需要 Python 3.8+，在 Debian/Ubuntu 系統上建議安裝 `python3-venv`，並依賴 Claude Code CLI 與 Git。可選擇安裝 `uv` 以加速 Python 環境管理。  

📊 快速上手步驟（macOS / Linux）  

```
curl -fsSL https://raw.githubusercontent.com/zubair-trabzada/geo-seo-claude/main/install.sh | bash
```

📊 Windows (Git Bash) 安裝流程  

1. 以 Git Bash 開啟目標資料夾（不要使用 PowerShell 或 CMD）。  
2. 執行一鍵指令：  
   ```
   curl -fsSL https://raw.githubusercontent.com/zubair-trabzada/geo-seo-claude/main/install-win.sh | bash
   ```
   或手動 clone 後執行 `./install-win.sh`。  

⚠️ 使用限制與注意事項  

- 只能在支援 Git Bash 的 Windows 環境下執行，PowerShell 或 CMD 會導致腳本失效。  
- 需要自行安裝 Claude Code CLI，README 僅列出為「Optional」項目，未說明安裝方式。  
- 目前未提供圖形化介面或即時排程功能，適合有基礎 CLI 操作經驗的使用者。  

🎯 實務啟示  

對於已經在執行傳統 SEO 的網站，導入此工具可快速加入 AI 搜尋的 GEO 優化層面，尤其在以下情境下有明顯收益：  

1. **品牌想搶佔 AI 流量**：根據專案摘要，AI 流量的轉換率遠高於一般搜尋，適合電商或服務型網站。  
2. **地區化內容需求**：若產品或服務在不同國家有差異化策略，GEO‑first 的優化有助於在 AI 搜尋中取得更精準的曝光。  
3. **開發資源有限**：一鍵腳本免除繁雜設定，適合小型團隊或個人部落客快速測試。  

🔗 來源  
- 標題：geo-seo-claude  
- 作者／機構：zubair-trabzada  
- 連結：https://github.com/zubair-trabzada/geo-seo-claude  

#AI #SEO #GeoSEO #Claude #ChatGPT #WebOptimization #Python #CLI #OpenSource #SearchEngineOptimization
