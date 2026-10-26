---
title: Can AI help solve the COBOL code crisis?
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/1018434/cobol-migration-legacy-code-openai-anthropic
model: claude-code/sonnet
generated_at: '2026-10-26T21:58:22.747812'
score: 63
---

📌 COBOL 遷移準確率衝上 98%,但離「換系統」還很遠

TL;DR：OpenAI 新模型 COBOL 翻譯測試分數亮眼,專家說離真正現代化差一大截。

IRS、銀行、提款機背後,跑的可能是一段六十多年前寫下、沒人敢動的程式碼。OpenAI 說它的新模型在這件事上有了「實質進展」。專家的回應是：先別急著開香檳。

🤔 **一個拖了七十年都死不掉的語言**

COBOL（common business-oriented language）誕生於 1959 年。根據 IBM 的數據,COBOL 至今仍支撐超過 40% 的線上銀行系統、80% 的實體信用卡交易、95% 的 ATM 交易,也是美國社會安全署、IRS 等政府服務的底層架構。報導引用一項估計,COBOL 造成的低效率每年讓美國 GDP 損失約 1050 億美元。問題是替換它極其困難：系統牽涉的人與知識早已老去或退休,而且「正常人不會用 COBOL 做新專案」,卻沒人敢碰舊系統怕引發連鎖故障。

📊 **OpenAI 的測試數字：低推理強度 87%,拉高到 98%**

10 月 19 日,OpenAI 發布部落格文章,宣稱其模型在將 COBOL 遷移到 C++、Java、Kotlin、Python、Rust 等現代語言時有「實質改善」,並強調「只有所有測試都通過,才算遷移成功」（behavior preservation,行為保留）。官方公布的測試結果：

| 模型 | 低推理強度 | 高推理強度 |
|---|---|---|
| GPT-6.1 Sol | 87% | 98% |
| GPT-6 Astra | 約 86% | — |
| GPT-6 Sol | 21% | — |
| GPT-5.6 Sol | 5% | — |

OpenAI 也表示同步改善了模型用各種語言（包括 COBOL）建置資料庫軟體的能力。Anthropic 方面則在今年 2 月發布一份「程式碼現代化 playbook」,主打用 Claude Code 把 COBOL 搬到 Java 或 Python,但沒有公布具體效能數據,只宣稱「COBOL 現代化的經濟效益已經轉變」。報導提到該公告發布後 IBM 股價下跌（IBM 部分營收來自協助企業維護舊系統)。

💡 **三位學者的共同質疑：改寫程式碼不等於換掉系統**

Twente 大學軟體演化副教授 Vadim Zaytsev 指出,他見過的最大 COBOL 系統有 2.5 億行程式碼,但程式碼量只是問題的一部分：系統可能混用多種語言,資料存在不同格式裡,還有跟其他系統的技術整合與組織期望要考慮,「AI 目前並未在真正替換或遷移 COBOL 系統中扮演主要角色」。

Delft 理工大學軟體工程教授 Arie van Deursen 直言 OpenAI 的部落格內容「流於表面」,對遷移任務本身的細節交代不多,測試的任務也相對簡單、定義明確,跟模型訓練時見過的系統很相似；他強調「維護一個老系統」跟「現代化一個老系統」中間有巨大差距,OpenAI 用來評估模型的任務「差了十萬八千里」,而且這些評測「沒有處理到真正的難點:把複雜的舊系統拆解成能個別替換的小單元」。

倫敦帝國理工學院程式語言教授 Alastair Donaldson 則指出,真正的挑戰往往不是看不懂語法,而是「很少人還懂得怎麼寫 COBOL」導致對系統行為缺乏理解；「在許多情況下,遷移前後即使只有微小的行為差異都是不可接受的」。他建議的驗證方式包括讓新舊系統跑同樣的工作流比對結果,搭配人類審查文件化的翻譯過程。南丹麥大學的 Jacopo Mauro 則提出形式化驗證（formal verification）——用數學方法從計算上證明程式碼行為正確——作為另一條路。

⚠️ **OpenAI 自己也承認還沒解決**

OpenAI 發言人 Oscar Haines 在回覆中坦言,舊程式碼遷移「仍遠遠稱不上是已解決的問題」,公司正在聽取開發者與企業的回饋,探索如何建立更好的測試並持續改善模型對各種程式語言的理解。Anthropic 則未在報導發布前提供回應。

🎯 **實務啟示**

對實際要處理 COBOL 或其他舊語言系統的工程團隊而言,目前 AI 比較現實的定位是輔助理解與記錄舊程式碼行為、產出可供人類審查的翻譯草稿,而不是直接拿來取代系統。真正要落地,仍需要搭配能比對新舊系統行為差異的測試基礎設施,甚至形式化驗證,而拆解系統邊界這件事,目前看起來仍是人類的工作。

🔗 **來源**
- 標題：Can AI help solve the COBOL code crisis?
- 作者／機構：Robert Hart, The Verge
- 連結：https://www.theverge.com/ai-artificial-intelligence/1018434/cobol-migration-legacy-code-openai-anthropic

#COBOL #LegacyCode #OpenAI #Anthropic #CodeMigration #SoftwareModernization #AICoding #EnterpriseIT #FormalVerification #ClaudeCode
