---
title: How well do agents use test/verification techniques?
source: Hacker News
url: https://danluu.com/agentic-testing/
model: claude-code/sonnet
generated_at: '2026-09-08T20:04:29.281852'
score: 101
---

📌 叫 Agent 用 TDD、QuickCheck，結果沒差很多

TL;DR：實測 26 種測試技巧＋4 款技能，發現指定技巧對 AI 寫程式碼的正確率影響有限。

如果你在 prompt 裡加一句「請用 property-based testing」或「請用形式化驗證」，是不是就能讓 coding agent 寫出更可靠的程式碼？Dan Luu 用一套嚴謹的實測告訴你：沒那麼簡單。

🤔 **測試技巧變好用了，軟體品質卻沒變好**

作者在先前的觀察中指出，雖然現在讓 coding agent 使用有效的測試技巧比以前容易，但軟體品質看起來反而在變差，暗示開發者預設採用的做法可能沒什麼用。這次的實驗想驗證：對一個沒有測試專業知識、只是「聽說該用某技巧」的人來說，單純在 prompt 裡加上技巧或函式庫名稱，能否改善 agent 實作正確性。

🧩 **26 種條件 × 80 次重跑的實驗設計**

實驗沿用先前比較程式語言效果時用過的 Zstd 實作評測，這次改成比較不同測試技巧與函式庫，全部以 Rust 實作。共測試 26 種 prompt 條件，涵蓋形式化方法（ACL2、Alloy、Creusot、Kani、Lean 4、SMT solver、Spin、TLA+、Verus）、傳統測試技巧（TDD、Fuzzing、Mutation testing、Metamorphic testing、Differential testing、Property-based testing）、特定函式庫（Proptest、QuickCheck、Insta、rstest、Rust 內建測試框架），以及一些對照組（Default 無額外指示、「Make no mistakes」、「Judgement」讓 agent 自行判斷最佳技巧）。另外測試 4 款技能：Hegel 官方技能、擁有 25 萬星、3.8 萬 fork 的 ECC Rust 測試技能、Trail of Bits 的 property test 技能，以及作者自己寫的技能。

測試使用 codex 搭配 GPT-5.6 Sol，分別在 medium 與 xhigh 兩種推理強度下執行，每個條件與強度各跑 80 次，另外在 IMAP RFC 上也各跑了 40 次驗證。

📊 **Default 反而表現在平均之上**

整體結果顯示，沒有任何條件明顯大幅勝出。值得注意的是，完全不加額外指示的 Default 條件表現反而在平均之上。在 xhigh 強度下，fuzzing 與 property-based testing 相關條件平均略優於形式化方法，但在 medium 強度下情況更為混雜。作者事先推薦的測試技能整體表現不佳，唯獨作者自己寫的技能表現尚可；TDD 一如預測地表現不好，其中一款技能因為引導 agent 使用 TDD，也連帶表現不佳。IMAP RFC 與其他隨機挑選的 RFC 上，結果與 Zstd 評測沒有本質差異。

💡 **Agent 不是真的懂這些技巧，只是套了個殼**

深入檢視 agent 實際的行為後發現，多數情況下 agent 並不真正理解該如何運用這些工具或技巧。作者引用 Gary Bernhardt 的評論：AI agent 對測試的做法，大致上是把十五年前反對 mocking 的人幻想出的病態案例，當成自己測試策略的骨幹，卻從沒真正用過 mocking。實測也印證了類似模式：被指定用某技巧時，agent 大多只是把原本會寫的測試包進對應框架的外殼；用形式化方法時常常證明一些無關緊要的性質；用 property-based testing 時則過度依賴純隨機輸入，大量落在無效或會被拒絕的案例，或是只驗證一個瑣碎性質後跑一堆低價值的隨機案例。

⚠️ **範圍侷限**

這次結果主要建立在 Zstd 實作與 IMAP RFC 等少數評測任務上，且集中測試單一 agent（codex + GPT-5.6 Sol）。作者本人自陳並非測試領域專家，實驗設計也帶有其個人事先設定的信心水準（例如預期 TDD 表現不佳、形式化方法不會過度突出），這些預測雖多數應驗，但仍是作者主觀假設下的驗證框架。

🎯 **實務啟示**

單純在 prompt 裡點名一種測試技巧或塞進一份看起來很完整的技能文件，未必能讓 agent 寫出更可靠的程式碼；效果較好的自製技能，關鍵在於刻意引導 agent 遠離其預設的低品質行為模式，而不是像教學文件一樣堆砌技巧說明。與其迷信特定方法論的名號，不如檢視 agent 實際產出的測試內容是否真的觸及風險路徑。

🔗 **來源**
- 標題：How well do agents use test/verification techniques?
- 作者／機構：vinhnx（Hacker News）
- 連結：https://danluu.com/agentic-testing/

#AICoding #SoftwareTesting #CodingAgents #TDD #PropertyBasedTesting #FormalMethods #Rust #LLMEval #DeveloperTools #QualityAssurance
