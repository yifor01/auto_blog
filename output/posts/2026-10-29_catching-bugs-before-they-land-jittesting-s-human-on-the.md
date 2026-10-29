---
title: 'Catching Bugs Before They Land: JiTTesting’s Human-on-the-Loop Approach at
  Full Scale'
source: Meta AI Research
url: https://engineering.fb.com/2026/10/29/security/catching-bugs-before-they-land-jittestings-human-on-the-loop-approach-at-full-scale/
model: claude-code/sonnet
generated_at: '2026-10-29T22:00:06.356052'
score: 102
---

📌 Meta 大規模部署五個月：AI 生成測試揪出 74 個隱私重大錯誤

TL;DR：Meta 把 JiTTests 從研究原型轉正為正式基礎設施，用 AI 生成「會失敗的測試」在上線前抓 Bug。

程式碼審查再快，終究是人在讀程式碼找問題；但當一個平臺的程式碼有數億行、每天都在變動，審查速度跟規模根本不成比例。Meta 給出的答案不是「審查得更快」，而是換一種抓錯方式：讓 AI 直接生成可執行的測試，用測試結果說話。

🤔 傳統審查追不上規模，那就別審查，讓測試說話

多數業界的 AI 抓錯手法，本質上是用 LLM 或 agent 模仿人類審查員讀程式碼、憑經驗判斷有沒有問題，只是做得比人快。Meta 的 Just-in-Time Tests（JiTTests）走的是不同路線：針對每個程式碼異動（diff），自動生成能展示「這次改動確實改變了行為」的可執行測試，測試被設計成應該失敗，藉此在異動上線前揪出問題。這類方法運算步驟更多，但能抓到 LLM 審查可能漏掉的錯誤類型。

🧩 五階段流程：從「可疑異動」到「人類只需確認一句話」

系統每晚利用閒置運算資源運作，目標是前一天送出、透過類似 Diff Risk Score 機制判定為「高風險」的異動，確保測試生成的力氣花在最可能出大問題的改動上。接下來分兩條工作流並行：

- Dodgy diff 工作流：把每個異動當成一個「突變」，用 mutation-guided 的 LLM 測試生成法，寫出能區分異動與原始版本行為差異的測試，目的是盡量擴大「弱捕獲」（weak catch，可能的 false positive）的候選池。
- Intent-aware 工作流：讓 LLM 根據程式碼改動、diff 標題與摘要推斷「這次改動想做什麼」，再描述實作過程中可能出錯的「風險」，依此構造出一系列代表潛在 Bug 的突變，生成測試去「殺死」這些突變，並拿這些測試實際跑在真正的異動上，失敗的就收進弱捕獲池。

有了弱捕獲之後，系統要判斷哪些是真的抓到 Bug（強捕獲）、哪些只是誤報。這裡用了兩套機制互補：一是 LLM-as-Judge，集合多個 SOTA LLM 分別評判弱捕獲的真偽；二是基於規則的 RubFake（Rule-Based False-Positive Killing Environment），提供確定性、可驗證的判斷。兩者的排序結果共同決定哪些弱捕獲值得進一步處理，以及是否要把工程師拉進來。關鍵是 Meta 採用「human-on-the-loop」而非「human-in-the-loop」：工程師不用逐一審查每個輸出，而是設定判斷準則、在整體層級檢視結果。

📊 589 位工程師參與，上半年攔下 74 個隱私重大錯誤

截至發文時，589 位工程師（佔 Meta 主動接觸對象的 64%）已實際使用過 Catching JiTTests，回報真正可行動的發現比例（true positive rate）達 60%。2026 年上半年，Catching JiTTests 在 diff 階段攔下 74 個嚴重（SEV）隱私錯誤，使同期隱私類 SEV 的整體發生率下降 20%。

⚠️ 判斷真偽的拉鋸：語意豐富但不確定，規則確定但受限

LLM-as-Judge 的判斷語意豐富，卻帶有非確定性、難以驗證的特性；RubFake 的規則判斷確定可驗證，但相對死板。Meta 選擇讓兩者並行互補，而不是只依賴單一機制，反映出目前 AI 判讀仍需要搭配確定性機制做校驗。

🎯 讓 AI 執行、人類定策略而非逐件把關

這套系統給其他工程團隊的啟示是：先把成功標準定義清楚,讓 AI 去執行測試生成與初步篩選，在整體層級監控結果，只在政策層級介入,而不是每一件都要人工確認。對工程師而言，理想狀態是幾乎不用去讀測試程式碼,只需要確認「這個行為變化是不是故意的」。

🔗 來源
- 標題：Catching Bugs Before They Land: JiTTesting's Human-on-the-Loop Approach at Full Scale
- 連結：https://engineering.fb.com/2026/10/29/security/catching-bugs-before-they-land-jittestings-human-on-the-loop-approach-at-full-scale/

#SoftwareTesting #LLM #Meta #BugDetection #AgenticAI #CodeQuality #CI #SoftwareEngineering #AIforSoftwareEngineering #TestGeneration
