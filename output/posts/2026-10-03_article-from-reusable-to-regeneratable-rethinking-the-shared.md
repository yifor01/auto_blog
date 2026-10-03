---
title: 'Article: From Reusable to Regeneratable: Rethinking the Shared UI Component
  Library'
source: InfoQ.com
url: https://www.infoq.com/articles/regeneratable-ui-component-library/
model: claude-code/sonnet
generated_at: '2026-10-03T20:02:24.614443'
score: 64
---

📌 當 AI 能現場生成 UI，共用元件庫還值多少？

TL;DR：模型能依設計系統即時生成多數標準 UI，讓維護共用元件套件的理由越來越薄弱。

多年來，前端團隊把「不要重複造輪子」當作鐵律，砸重本建立共用元件庫、設計系統、版本治理流程。但如果現在造一個輪子的成本，已經低於維護一座輪子倉庫的成本，這套鐵律還站得住嗎？

🤔 **共用元件庫曾經解決的問題**

InfoQ 作者 Daniel Curtis 指出，過去共用 UI 元件套件存在的理由很單純：重複寫同樣的 Button、Modal、Table 太浪費工程資源，所以把它們包裝成可重用的套件，讓多個團隊共享、統一維護。

🧩 **「生成」改變了重用的經濟帳**

文章的核心論點是，regeneration（現場重新生成）已經改變了重用的成本結構。當一個模型被指向一套完整的設計系統（design system）時，它可以依需求現場生成絕大多數標準化 UI，而不需要仰賴事先打包好的元件套件。換句話說，過去「寫一次、到處重用」的經濟學，正在被「隨時可以重新生成」取代，這讓繼續花人力維護一個版本化、要相容性測試的共用元件套件，變得更難被證明值得。

💡 **該留下的，是設計系統本身**

作者建議的方向並非放棄整套設計規範，而是保留設計系統、設計代幣（tokens）與使用指引（guidelines）這些「決策規則」本身，因為這些才是讓模型能生成出一致、符合品牌規範 UI 的基礎；真正該被重新檢視的，是那個需要持續發版、修 bug、處理相依性的「元件套件」這個實體產物。

🎯 **實務啟示**

如果你的團隊正在評估是否要繼續投資維護一套內部元件庫，這篇文章提供了一個值得思考的切角：與其問「這個元件還要不要維護」，不如先問「我們的設計系統與 tokens 是否完整、清晰到可以讓模型現場生成出可用的 UI」。把治理重心從「元件程式碼」移到「設計規則」，可能才是因應生成式工具普及後更划算的投資方向。

🔗 **來源**
- 標題：From Reusable to Regeneratable: Rethinking the Shared UI Component Library
- 作者／機構：Daniel Curtis @ InfoQ.com
- 連結：https://www.infoq.com/articles/regeneratable-ui-component-library/

#UIComponents #DesignSystems #FrontendEngineering #AIGeneratedUI #DesignTokens #SoftwareArchitecture #DeveloperTooling #CodeReuse #WebDevelopment #GenerativeAI
