---
title: MemPalace/mempalace
source: GitHub Trending
url: https://github.com/MemPalace/mempalace
score: 98
model: google/gemma-4-31b-it:free
generated_at: '2026-06-06T19:56:21.358172'
---

📌 【GitHub Trending】本地化 AI 記憶庫 MemPalace：零 API、結構化檢索、R@5 96.6%

你以為 AI 記憶只能靠雲端服務、API 金鑰才能實現？MemPalace 直接把對話原文存本機，搭配可插拔的語意檢索，讓隱私與效能同時兼得。  

🤔 **本地 AI 記憶的痛點：隱私、成本與長期檢索**  
在多數生成式 AI 應用中，對話歷史往往被外部服務持久化，或僅保留摘要。這樣不僅暴露敏感資訊，亦無法支援「原文」檢索。開發者需要一個 **完全本地**、**結構化**、且 **高效** 的記憶層，才能在不依賴外部 API 的前提下，快速定位過往對話。

🧪 **MemPalace 的核心設計：結構化語意檢索 + 可插拔後端**  
- **原文存儲**：所有對話以 verbatim 純文字寫入磁碟，絕不做摘要或改寫。  
- **層級結構**：人員與專案 → *wings*，主題 → *rooms*，具體內容 → *drawers*，使搜尋可以限定在特定子集合，避免平面檢索的噪聲。  
- **檢索層**：預設使用 **ChromaDB**，接口定義於 `mempalace/backends/base.py`，開發者可自行替換為其他向量資料庫（如 FAISS、Weaviate）而不改動其餘程式碼。  
- **純本機運行**：除非使用者主動授權，資料永遠不會離開本機；因此可在高度受限或離線環境下部署。  

📈 **實驗結果：LongMemEval 上 96.6% R@5**  
在 LongMemEval 基準測試中，MemPalace 以 **96.6% 的 Recall@5** 成績領先，同時保持零 API 呼叫的純本機特性，證明結構化索引與高品質向量化的組合在長文本檢索上具備實用性。

⚙️ **安裝與使用注意**  
- 透過 `pip install mempalace` 安裝，或直接克隆 GitHub 倉庫。  
- 建議在 **isolated environment**（virtualenv/conda）中安裝，以避免 Debian/Ubuntu/Homebrew 系統 Python 的 PEP 668 衝突。  
- 安裝同時提供 CLI，便於快速建立、管理 *wings/rooms/drawers*。  

⚠️ **安全提醒：僅信任官方來源**  
MemPalace 目前唯一的官方渠道是：  
1. GitHub repository — https://github.com/MemPalace/mempalace  
2. PyPI 套件 — `pip install mempalace`  
3. 官方文件 — https://mempalaceofficial.com  

任何其他域名（包括 *.tech、*.net、或其他 .com 變體）均為冒牌站，可能夾帶惡意程式。下載或執行前請務必核對來源。

🔧 **快速上手檢查清單**  
- 下載官方 repo → 建立虛擬環境 → `pip install -e .`  
- 確認 ChromaDB 依賴已安裝 (`pip install chromadb`)  
- 使用 CLI 建立第一個 *wing*（例如 `mempalace create-wing my_project`）  
- 開始對話，所有文字自動寫入對應 *drawer*，之後可用 `mempalace search "關鍵詞"` 進行語意檢索。

🧭 **未來方向與限制**  
- 目前僅支援文字對話的 verbatim 存儲，對多模態（圖像、音訊）尚未提供原生支援。  
- 長期保存依賴本機磁碟，未內建自動備份機制；使用者需自行規劃備份策略。  
- Claude Code 等外部會話若未手動保存，30 天後會過期，未與 MemPalace 自動掛鉤。

🎯 **實務建議**  
- **隱私敏感的企業內部聊天**：部署 MemPalace 作為本地知識庫，避免將機密對話外流。  
- **研究與原型開發**：利用其可插拔後端測試不同向量資料庫的效能差異。  
- **長期對話分析**：結構化的 *wing/room/drawer* 讓團隊能以主題維度快速回顧歷史討論。

🔗 **論文/說明文件**  
- GitHub repo： https://github.com/MemPalace/mempalace  
- PyPI 套件： https://pypi.org/project/mempalace/  
- 官方概念說明： https://mempalaceofficial.com/concepts/the-palace  
- 更新紀錄： https://github.com/MemPalace/mempalace/blob/main/docs/HISTORY.md  

你有在本機部署 AI 記憶的需求嗎？或是對可插拔檢索有其他想法？歡迎在下方留言分享你的實作經驗 👇  

#AI #LocalFirst #Memory #SemanticSearch #ChromaDB #OpenSource #GitHubTrending #PrivacyFirst
