---
title: Localcode, open source agentic coding on your Mac with one command
source: Hacker News
url: https://github.com/mjwsolo/localcode
model: gpt-6.1-terra
generated_at: '2026-11-28T05:52:32.850280'
score: 76
---

📌 LocalCode：Mac 本機編碼代理

TL;DR：LocalCode 在 Mac 執行本機模型，協助讀寫專案並執行開發任務。

🎣 編碼代理可以幫忙修改檔案、執行測試，但這些工作一定要交給遠端模型嗎？LocalCode 提供另一種選擇：在 Apple Silicon Mac 上執行模型，並讓代理操作本機專案。

🤔 **代理能操作專案，範圍外的動作會先詢問**

LocalCode 是採用 Apache 2.0 授權的開源編碼代理。依專案說明，它可以：

- 讀取、編輯專案檔案，並依名稱、內容或結構搜尋程式碼。
- 自行在專案內執行測試、建置、Git 與 shell 指令；操作專案範圍外的內容前會先詢問。
- 建立並啟動應用程式，再檢查應用程式是否有回應。
- 在多則訊息之間記住任務內容。

🧩 **安裝後在專案目錄啟動**

使用需求包括 Apple Silicon Mac、macOS 13 以上、至少 16 GB 統一記憶體，以及 Python 3.10 以上；也需要足夠的磁碟空間存放 LocalCode 和所選模型。

```bash
uv pip install localcode
cd your-project
localcode
```

更新則使用：

```bash
uv pip install -U localcode
```

若要讓其他本機應用程式使用執行中的模型，可開啟 `/server`，或執行 `localcode api`，使用相容 OpenAI 的端點。

🧩 **12 個模型與 169 種量化選項**

專案列出 12 個模型、169 種量化選項，涵蓋程式碼、圖片輸入與結構化決策用途。模型從 Hugging Face 下載，可透過 `/models` 切換；LocalCode 會根據 Mac 的記憶體，推薦能容納的最強模型。

下載大小依模型與量化選項而異。例如 Gemma 4 12B 為 4.7 GB 至 24.3 GB，DeepSeek V4 Flash 284B-A13B 則為 82.4 GB 至 161.9 GB。下載支援平行處理與中斷後續傳。

💡 **推測式解碼與快取針對本機推論最佳化**

LocalCode 說明，它在模型伺服器之上加入多項最佳化：

- **推測式草稿生成（speculative drafting）**：使用模型供應商提供的草稿模型預先猜測 token。專案宣稱，部分支援的模型回覆速度約提升 2 倍。
- **複製式草稿生成（copy drafting）**：重寫已讀取的檔案時，以複製取代生成。專案宣稱重寫速度提升 3.5 至 4 倍。
- **提示快取（prompt cache）重用**：保持系統提示不變，讓模型只需讀取新增內容。
- **記憶體管理**：預設使用 8-bit KV cache，讓較長的上下文能放入記憶體；Inkling 2 則使用 16-bit cache。
- **預先編譯的 GPU 核心**：減少安裝後首次啟動的等待時間。

這些速度數字來自專案說明；所提供素材未列出測試條件。

⚠️ **推論在本機執行，但部分功能會連網**

LocalCode 指出，推論在本機執行；模型下載、`web_search` 與 `web_fetch` 工具，以及使用者加入的 MCP 伺服器會使用網路。

🎯 **先依記憶體與磁碟空間選模型**

想評估本機編碼代理的工程師，可以先確認 Mac 符合需求，再參考 `/models` 的記憶體推薦與模型下載大小。若要整合其他本機應用程式，則可試用相容 OpenAI 的端點；涉及網路使用時，也應留意上述功能的連線範圍。

🔗 **來源**
- 標題：Localcode, open source agentic coding on your Mac with one command
- 作者／機構：mjwsolo
- 連結：https://github.com/mjwsolo/localcode

#LocalCode #AgenticCoding #LocalModels #AppleSilicon #CodingAgent #LLM #ModelQuantization #SpeculativeDecoding #PromptCache #OpenSource
