---
title: twentyhq/twenty
source: GitHub Trending
url: https://github.com/twentyhq/twenty
score: 78
model: google/gemma-4-31b-it:free
generated_at: '2026-06-20T19:43:25.637334'
---

📌 把 CRM 當成程式碼來維護：開源 CRM 框架 Twenty

TL;DR：Twenty 提供可透過 SDK 定義對象與邏輯的開源 CRM，讓技術團隊能像開發軟體一樣版本化管理 CRM。

大多數企業在面對 CRM 時，往往在「功能太簡單的開源工具」與「設定極其複雜的企業級 SaaS」之間掙扎。當業務需求演進時，調整 CRM 的欄位與流程往往變成一場繁瑣的點擊遊戲，而非工程開發。

🛠️ **像維護技術棧一樣維護 CRM**

Twenty 的核心理念是將 CRM 的建構過程「程式碼化」。它不再僅僅是一個預設的工具，而是一組建構塊（Building Blocks），讓技術團隊能根據複雜的業務需求，快速建構並迭代自定義的 CRM 系統。

🧩 **透過 SDK 定義對象與結構**

開發者可以使用 Twenty CLI 快速初始化專案，並透過 `twenty-sdk` 以程式碼定義資料結構。例如，定義一個「交易 (Deal)」對象的流程如下：

1. 使用 `npx create-twenty-app` 建立新應用。
2. 在程式碼中定義對象名稱、標籤以及對應的欄位類型（如 `TEXT`、`CURRENCY` 或 `DATE_TIME`）。
3. 執行 `npx twenty app:publish` 將定義好的結構發佈到工作區。

這種方式讓 CRM 的定義（對象、視圖、代理人與邏輯函式）可以與其餘技術棧一樣進行版本控制與部署。

🚀 **靈活的部署選項**

針對不同的基礎設施需求，Twenty 提供兩種啟動方式：
- **Cloud 版本**：最快速的啟動方式，無需管理基礎設施，一分鐘內即可建立工作區。
- **Self-hosting**：支持使用 Docker Compose 在自有基礎設施上運行，或透過本地設置指南進行開發貢獻。

🎯 **實務啟示**

對於需要高度自定義 CRM 但不希望被封閉 SaaS 綁架的工程團隊，Twenty 的「以程式碼定義結構」模式能大幅降低維護成本。將 CRM 的變更納入 Git 版本管理，能讓業務邏輯的更迭變得可追蹤且可預測，而非依賴手動配置。

🔗 **來源**
- 標題：twentyhq/twenty
- 作者／機構：twentyhq
- 連結：https://github.com/twentyhq/twenty

#CRM #OpenSource #TypeScript #SDK #DeveloperExperience #SelfHosted #Docker #SoftwareEngineering #Productivity #Twenty
