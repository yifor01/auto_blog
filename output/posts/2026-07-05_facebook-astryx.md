---
title: facebook/astryx
source: GitHub Trending
url: https://github.com/facebook/astryx
score: 74
model: google/gemma-4-31b-it:free
generated_at: '2026-07-05T19:37:20.605711'
---

📌 【Meta 開源】Astryx：支撐 13,000 個 App 的大規模設計系統正式公開

TL;DR：Meta 開源其內部最大設計系統 Astryx，提供 150+ 元件，強調對 AI Agent 與開發者的共同友善。

當一個設計系統需要同時支撐超過 13,000 個應用程式時，它不能只是一個元件庫，而必須成為一套能讓數千名工程師與設計師協作的基礎設施。Meta 近期將在內部執行八年的設計系統 Astryx 正式開源。

🧩 **從 Meta 內部實踐轉化為開源工具**

Astryx 是 Meta 內部使用率最高且規模最大的設計系統。它不僅提供 150 個以上符合無障礙標準（accessible）的元件，還整合了品牌級主題設定（brand-level theming）、深色模式、可直接部署的模板以及一套 CLI 工具。

在技術實作上，Astryx 基於 React 與 StyleX 構建。開發者只需匯入預建的 CSS 並使用強型別（typed）的 React 元件即可快速上手，無需安裝額外的建構外掛或強制採取特定的樣式庫。

💡 **打破封閉 API 的三項核心設計**

Astryx 與傳統設計系統的不同之處在於其「開放性」：

- **開放內部結構**：元件設計允許在任何層級進行組合，而非將功能鎖在頂層 API 之後。若需要更深度的自定義，可透過 swizzle 功能將元件的完整原始碼直接匯出至專案中由開發者完全掌控。
- **無樣式鎖定（No styling lock-in）**：雖然 Astryx 內部使用 StyleX 撰寫樣式，但對使用者而言這是透明的。開發者可以使用 Tailwind、CSS modules 或純 CSS 透過 className 進行覆寫，無需更換既有的樣式工具。
- **無需封裝的自定義**：主題設定透過 CSS 自定義屬性（custom properties）的覆寫來實現。設計師可以直接調整主題，而不需要為了修改風格而對元件原始碼進行 fork 或撰寫複雜的封裝層。

🤖 **為「人與 AI Agent」共同設計**

Astryx 在設計 API、檔案與 CLI 時，特別考慮到了現代的開發模式：不僅要讓人類工程師好用，也要讓與開發者協作的 AI 助手（agents）能使用同一套工具鏈高效地構建介面。

🎯 **實務啟示**

對於需要建構大規模、高度可擴充套件 UI 的團隊，Astryx 提供了一個極佳的參考範本：如何在高一致性（Design System）與高靈活性（Swizzle/CSS Overrides）之間取得平衡，並在設計之初就將 AI 自動化開發納入考量。

🔗 **來源**
- 標題：facebook/astryx
- 作者／機構：facebook
- 連結：https://github.com/facebook/astryx

#Meta #DesignSystem #React #StyleX #OpenSource #Frontend #UIUX #WebDevelopment #AI #DeveloperExperience
