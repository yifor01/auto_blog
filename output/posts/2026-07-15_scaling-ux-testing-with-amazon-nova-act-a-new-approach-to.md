---
title: 'Scaling UX testing with Amazon Nova Act: A new approach to user flow analysis'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/scaling-ux-testing-with-amazon-nova-act-a-new-approach-to-user-flow-analysis/
score: 104
model: tencent/hy3:free
generated_at: '2026-07-15T07:59:50.320580'
---

📌 【Amazon】Nova Act 視覺導覽 UX 測試

TL;DR：Amazon Nova Act 多模態模型看截圖導覽，讓 UX 測試免於硬編碼指令碼維護。

🎣 開場
傳統自動化工具如 Selenium 遇到介面改版就失效，UX 測試始終難以規模化。Amazon 提出的 Nova Act 選擇讓模型直接「看」網頁截圖來行動，可能翻轉這套邏輯。

🤔 **UX 測試看流程順暢度，但傳統方法覆蓋率受限**
UX 測試評估使用者能否輕鬆完成任務，例如找商品、註冊帳號或結帳，重點在識別導覽摩擦與影響滿意度的介面元素，不同於 QA 測試只找功能 bug。手動測試只能走有限關鍵路徑，邊緣案例常被忽略；硬編碼指令碼工具（如 Selenium、Playwright）一旦介面變動就斷裂，維護負擔限縮測試覆蓋率。跨裝置、多旅程的全面測試對多陣列織仍過於昂貴耗時。

🧩 **Nova Act 處理視覺資訊，像人類測試者分析截圖**
Amazon Nova Act 是多模態基礎模型，能透過視覺與動作理解並操作瀏覽器介面。它不依賴預定義元素選擇器，而是分析網頁截圖：理解頁面佈局、用視覺線索辨識可互動元素、依上下文決定下一步動作。這種視覺理解使其能適應介面變更與動態內容，而傳統自動化工具會在此失效。

💡 **模型推理與思維鏈日誌可提供網站洞察**
作者指出 Nova Act 的 reasoning 與 chain of thought 日誌能提供關於網站設計的有價值洞察，但摘要在此處截斷，確切細節未明。對工程師而言，這代表除自動化操作外，可能還能從日誌反推介面問題。

🎯 **工程師可轉向視覺型自動化，降低維護負擔**
對前端與 QA 團隊，採用此類視覺基礎模型意味著不再需要為每個 UI 調整更新選擇器指令碼。可將有限人力放在邊緣案例與體驗最佳化，讓自動化覆蓋更多裝置與互動模式。

🔗 **來源**
- 標題：Scaling UX testing with Amazon Nova Act: A new approach to user flow analysis
- 作者／機構：Reilly Manton (AWS ML)
- 連結：https://aws.amazon.com/blogs/machine-learning/scaling-ux-testing-with-amazon-nova-act-a-new-approach-to-user-flow-analysis/

#AmazonNovaAct #UXTesting #MultimodalModel #WebAutomation #Selenium #Playwright #AWSMachineLearning #UserFlow #VisualUnderstanding #AITesting
