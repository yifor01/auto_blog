---
title: mvanhorn/last30days-skill
source: GitHub Trending
url: https://github.com/mvanhorn/last30days-skill
score: 74
model: google/gemma-4-31b-it:free
generated_at: '2026-07-05T19:36:52.178907'
---

📌 用真實資料定義熱門：mvanhorn 開源 AI 驅動的 /last30days 搜尋引擎

TL;DR：一個 AI Agent 外掛，透過整合 Reddit、X、TikTok 等社群互動資料，取代編輯推薦來定義「最近 30 天」的熱門趨勢。

當我們在 Google 或 ChatGPT 搜尋趨勢時，結果往往是由演算法、編輯權重或特定的合作協議決定。但真正的「熱門」應該是什麼？是數百萬人的點讚、推文互動，或是真金白銀的投注。

🧩 **以「注意力」與「金錢」作為權重指標**

`last30days-skill` 提出了一種不同的搜尋邏輯：不依賴編輯篩選，而是直接抓取真實使用者的參與度作為評分標準。

- **資料來源**：平行搜尋 Reddit（Upvotes）、X（Likes）、YouTube（轉錄內容）、TikTok（參與度）以及 Polymarket（由真金白銀支援的賠率與內部資訊）。
- **運作流程**：搜尋所有平臺 → 根據真實互動量評分 → 由 AI Agent 裁判將碎片化資訊合成一份簡報。
- **核心差異**：相較於 Google 聚合編輯觀點，或 ChatGPT 與 Gemini 僅能存取部分平臺（如 ChatGPT 僅有 Reddit 合作，Gemini 有 YouTube），此工具旨在打破單一 AI 的存取限制，同步獲取多平臺資料。

🛠️ **快速整合至 AI 開發環境**

該專案設計為一個「Skill」，可無縫整合進多種 AI Agent 主機（Agent Skills hosts），且標榜零設定（Zero config）。

- **推薦安裝（Claude Code）**：透過 marketplace 自動更新
  ` /plugin marketplace add mvanhorn/last30days-skill`
- **通用安裝（Codex, Cursor, Copilot, Gemini CLI 等 50+ 主機）**：
  `npx skills add mvanhorn/last30days-skill -g`（-g 為全域安裝，可用於所有專案）
- **初始化**：Reddit、HN、Polymarket 與 GitHub 可立即使用；執行一次設定精靈後，可在 30 秒內解鎖 X、YouTube 與 TikTok。

🎯 **實務啟示**

對於需要快速掌握市場脈動、社群情緒或即時趨勢的工程師與分析師，這個工具提供了一種「去中心化」的資訊獲取方式。它將搜尋目標從「官方答案」轉移到「群眾行為」，適合用來追蹤那些尚未被主流媒體或官方檔案記錄，但在社群中已爆發的技術趨勢或爭議議題。

🔗 **來源**
- 標題：mvanhorn/last30days-skill
- 作者／機構：mvanhorn
- 連結：https://github.com/mvanhorn/last30days-skill

#AI #AIAgent #SearchEngine #OpenSource #ClaudeCode #Cursor #SocialListening #DataAggregation #TrendAnalysis #DeveloperTools
