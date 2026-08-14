---
title: 'Securing the frontier: How JetBrains evaluates and deploys Claude Fable 5'
source: Claude Blog
url: https://claude.com/blog/how-jetbrains-evaluates-and-deploys-claude-fable-5
model: claude-code/sonnet
generated_at: '2026-08-14T07:20:18.091373'
pinned: true
---

📌 JetBrains 用私有程式碼庫實測 Claude Fable 5

TL;DR：JetBrains CTO 揭露內部評測方法，Fable 5 的 Python 通過率大增 16 個百分點。

當一家服務全球 1,250 萬活躍使用者、88 家財星全球 100 大企業的公司，決定用自家 monorepo 來測試新模型，得到的答案往往比公開 benchmark 更誠實。JetBrains Agent Systems CTO Vladislav Tankov 在受訪時，說明了團隊如何評測、何時選用 Claude Fable 5，以及如何看待資料保留與安全防護的取捨。

🤔 **十年老兵，從懷疑到全面轉向**

Tankov 在 JetBrains 任職十年，公司是最早一批 LLM 供應商客戶。他形容過去一年是關鍵轉折：公司內外原本存在的 AI 懷疑論者，如今幾乎全數改觀，「這是科技產業一次根本性的變化」。

🧩 **不只看公開榜單，用自家 monorepo 驗證**

作為一家開發工具公司，JetBrains 建立了大規模評測流程：在私有程式碼庫（包含公司 monorepo）上跑大型 eval set。Tankov 指出，部分模型會針對公開 benchmark 調校而在實際任務上失準，用私有程式碼庫測試更容易抓出這種落差。團隊同時維護三份排行榜：最佳品質、每項任務最低成本、最快速度。他也提到 Claude Fable 5 雖然每個 token 的價格較高，但在較複雜的長時間任務上，每個任務的總成本反而更低。

📊 **Python 通過率大增 16 個百分點**

依 Tankov 分享的實測數據：

| 指標 | Claude Fable 5 | Opus 4.8 |
|---|---|---|
| Python 通過率 | 44.3% | 28.2% |
| 頭對頭比較（各自獨贏題數） | 贏 18 題 | 僅贏 2 題 |
| 平均所需步驟 | 較 Opus 4.8 少約 22% | 基準 |

他特別強調，程式碼「能跑」和「答案正確」是兩回事，而 Fable 5 產出的程式碼一旦執行，通過測試的比例明顯高於兩款 Opus 模型，這類錯誤原本是最昂貴、最難察覺的失敗類型。在 Java 任務上，Opus 4.8 常反覆嘗試拉取外部資源（在 JetBrains 環境中幾乎沒有幫助），Fable 5 則完全略過，直接處理眼前的程式碼，展現出更好的工程習慣。

💡 **什麼時候該選 Fable 5，而不是 Opus？**

Tankov 將 Opus 定位為「工作馬」：能確保任務被完成。而當團隊需要更強的推理能力、近乎一個合作夥伴、甚至自己也還不確定該怎麼做時，才會轉向 Claude Fable 5。他舉例，一位技術主管用 Fable 5 幾乎一次到位地實作出團隊嘗試多年都沒成功的富文本編輯器元件。另一個常見用法是長時間的 agentic coding 實驗：讓 agent 依據文字與圖片規格，實作出複雜的類 IDE 應用程式，甚至規格本身也可由 agent 依據既有應用程式反向生成，形成近乎黑箱的框架／語言／執行環境改寫流程。

⚠️ **資料保留是一場拉鋸戰**

JetBrains 並不打算自行成為「最安全模型」的打造者，而是信任 Anthropic 端的紅隊測試與安全工作，自身則著重在部署層面的安全網。安全性是 Fable 5 目前最大宗的用途之一，JetBrains 用它對自家產品做白箱測試找漏洞，同時預期未來會有外部人士用同等級模型來探測其產品弱點。Tankov 坦言團隊其實更偏好零資料保留，但為了理解分類器何時誤判，仍需要一定程度的資料回溯；只要審查僅限於被標記的最嚴重案例，他認為這是換取前沿智慧的合理取捨。

🎯 **實務啟示**

對正在評估前沿模型的工程團隊，這次分享提供了一個可複製的方法論：用私有程式碼庫而非公開榜單驗證模型真實能力，同時建立品質、成本、速度三個維度的排行榜，依任務複雜度而非單一模型「全面最強」的迷思來決定該用哪個模型。

🔗 **來源**
- 標題：Securing the frontier: How JetBrains evaluates and deploys Claude Fable 5
- 作者／機構：Anthropic
- 連結：https://claude.com/blog/how-jetbrains-evaluates-and-deploys-claude-fable-5

#Anthropic #ClaudeFable5 #JetBrains #AICoding #LLMEvaluation #AgenticCoding #SoftwareEngineering #AIatWork #ModelBenchmark #EnterpriseAI
