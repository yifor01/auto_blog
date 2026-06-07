---
title: twentyhq/twenty
source: GitHub Trending
url: https://github.com/twentyhq/twenty
score: 59
model: google/gemma-4-31b-it:free
generated_at: '2026-06-07T19:37:29.307370'
---

📌 **【開源 CRM 新選擇】Twenty：把 CRM 當成軟體產品來開發與版本管理**

對於許多技術團隊來說，市面上的 CRM（客戶關係管理系統）往往陷入兩個極端：要麼是功能太簡單無法滿足複雜業務，要麼是像 Salesforce 那樣龐大且封閉，客製化成本極高且缺乏開發者的掌控感。

如果 CRM 能像我們開發後端服務一樣，透過程式碼定義、版本管理，並能快速部署，會是什麼樣子？

🤔 **CRM 的客製化不該是「點擊設定」，而應該是「編寫程式碼」**

傳統 CRM 的配置通常依賴於複雜的後台 UI 點擊，這導致開發者無法使用 Git 進行版本控制，也難以將變更整合進 CI/CD 流程。Twenty 試圖打破這個僵局，將 CRM 的構建過程「開發化」。

它的核心理念是提供一套「建構塊 (Building Blocks)」，讓技術團隊能根據業務演進快速調整，而不是被軟體供應商的設定介面所限制。

🧪 **透過 SDK 與 CLI 實現「CRM as Code」**

Twenty 的設計亮點在於將 CRM 的定義從 UI 移到了程式碼層級。開發者可以使用 `twenty-sdk` 直接定義業務邏輯，而非在後台手動新增欄位。

例如，透過 `defineObject` 函式，你可以直接在程式碼中定義物件（如：Deal）、欄位（如：Amount, Close Date）及其類型。定義完成後，利用 `npx twenty app:publish` 即可將這些定義發佈到工作區。這種方式讓 CRM 的定義變得可追蹤、可審核，且能像管理其餘技術棧 (Tech Stack) 一樣進行版本管理。

🛠️ **從雲端快速啟動到完全自主託管**

Twenty 在部署靈活性上提供了兩種路徑：
- **Cloud 版本**：適合追求速度的團隊，一分鐘內即可建立工作區，無需管理基礎設施。
- **Self-hosting**：針對對數據主權有高度要求的企業，支援透過 Docker Compose 在自有基礎設施上運行。

這讓團隊能根據公司發展階段，從快速驗證 (MVP) 平滑過渡到完全自主掌控的私有部署。

💡 **將 CRM 整合進開發工作流的實務價值**

對於 AI 工程師或後端開發者來說，Twenty 的價值在於它將 CRM 從一個「管理工具」轉變為一個「可擴展的框架」。當你需要將 AI Agent 整合進 CRM 流程時，透過其提供的 Objects、Views 與 Logic Functions 接口，開發者能更直覺地將 AI 邏輯注入到業務流程中，而非受限於第三方平台的 API 限制。

⚠️ **定位於框架而非成品，學習曲線與維護成本存在**

需要注意的是，Twenty 定位為提供「建構塊」的框架。這意味著它不像傳統 SaaS CRM 那樣「開箱即用」，開發者需要投入時間編寫定義並管理自己的配置。對於沒有開發能力的小型團隊，這可能增加運維負擔；但對於技術導向的團隊，這換來的是極高的靈活性。

🎯 **適合追求「開發掌控感」的技術團隊**

如果你正厭倦於在 CRM 後台進行繁瑣的點擊設定，或者希望 CRM 的變更能同步在 Git 提交記錄中，Twenty 提供了一種更符合工程師直覺的替代方案：

- 將業務物件定義為程式碼 $\rightarrow$ 實現版本控制
- 使用 CLI 快速發佈 $\rightarrow$ 加速迭代速度
- 自主託管 $\rightarrow$ 確保數據安全與隱私

🔗 **專案連結**
📝 Twenty: The Open-Source CRM
👤 twentyhq
🔗 GitHub: https://github.com/twentyhq/twenty

你傾向於使用設定簡單的 SaaS CRM，還是願意花時間建構一個完全掌控的開源 CRM？歡迎在下方分享你的看法 👇

#OpenSource #CRM #SoftwareEngineering #DeveloperExperience #Twenty #SelfHosted #GitHubTrending
