---
title: Learning more about Claude's mathematical capabilities
source: Anthropic Research
url: https://www.anthropic.com/research/riemann-zeta
model: tencent/hy3:free
generated_at: '2026-08-11T06:59:32.615462'
score: 109
---

📌 【Anthropic 研究】挑戰黎曼猜想未果，卻意外突破零點比例下限：從 41.6% 提升至 67.2%

TL;DR：Claude 在嘗試解決黎曼猜想時，意外將黎曼 zeta 函數零點的比例下限從 41.6% 提升至 67.2%。

面對數學史上最著名的未解難題之一——黎曼猜想（Riemann hypothesis），即便是最強大的 AI 也難以一舉攻克。然而，Anthropic 的研究發現，當 Claude 被要求「認真嘗試」解決這個問題時，它在嘗試過程中意外取得了一項數學進展：大幅提升了滿足黎曼猜想的 zeta 函數零點比例的下限。

🤔 **黎曼猜想與零點比例的意義**

黎曼 zeta 函數描述了質數的分布；函數中每一個取值為零的位置，都對質數序列提供了更精細的細節。黎曼猜想主張，所有決定質數分布的零點都位於某條特定的垂直線上。

在數學界，研究方向之一是量化「位於該線上的零點所佔的最小比例」。過去數十年來，數學家們透過研究不斷提高這個常數比例，目前的已知下限為 41.6%。

🧩 **Claude 如何達成數學突破**

這次的進展並非直接證明了黎曼猜想，而是透過結合前人的研究成果，突破了現有的比例下限。

- **研究方法**：Claude 結合了 Baluyot、Goldston、Suriajaya 與 Turnage-Butterbaugh 的研究成果，以及 Bombieri 在 2000 年發表的論文。
- **技術細節**：Claude 建立了一個適當的函式空間，該空間具有由 Weil 誘導的二次型（quadratic form），以及由線上的零點與線外零點所產生的正定與負定子空間。接著，Claude 針對二次型秩（rank）的性質，結合一階與二階矩（moment）資訊，寫出了一個不等式。
- **關鍵突破點**：Claude 敢於同時處理整個空間（同時考慮正定與負定性），並允許二次型為非對角矩陣（non-diagonal），這被認為是達成此結論的關鍵步驟。

📊 **透過大量計算與子代理人協作**

這次研究並非單次對話完成，而是發生在一個未發布的研究版本 Claude 中，其過程極具工程規模：

- **運算規模**：使用了 Claude Code 進行兩次對話，總共產生了 3100 萬個輸出 token。
- **協作架構**：Claude 協調了約 60 個子代理人（subagents），在一天半的時間內執行了 2,400 個 shell 指令並撰寫了數百個 Python 腳本。
- **驗證流程**：子代理人之間進行互審，並進行了數千次針對已知 zeta 零點的數值檢查。此外，Claude 還下載了 54 篇 arXiv 論文以確認該發現是否已被發表，並嘗試從頭重新證明該結果。
- **形式化驗證**：Claude 還與人員合作，產出了該結果的 Lean 形式化證明（formalization），並通過了標準的驗證工具比對。

💡 **AI 在數學推理上的新範式**

雖然這次嘗試並未解決黎曼猜想本身，但這展現了 AI 在數學研究中的新潛力：

1. **非預期產出**：這個突破是 Claude 在嘗試解決「不可能的任務」時產生的意外副產品。
2. **協作與驗證**：透過大量子代理人的協作、數值檢查與形式化證明，AI 展現了處理複雜邏輯與驗證的能力。
3. **突破認知限制**：研究人員指出，Claude 似乎低估了 AI 進步的速度；在面對難題時，AI 有能力從龐大的前人研究中，尋找到結合新路徑的可能性。

🎯 **實務啟示**

對於 AI 工程師與研究者而言，這顯示了「多代理人系統（Multi-agent systems）」與「形式化驗證（Formal verification）」在處理高度邏輯問題時的巨大價值。AI 不僅僅是生成內容，更能在複雜的協作框架下，透過大規模的計算與自我驗證，輔助人類突破學術研究的邊界。

🔗 **來源**
- 標題：Learning more about Claude's mathematical capabilities
- 機構／作者：Anthropic
- 連結：https://www.anthropic.com/research/riemann-zeta

#AI #Mathematics #RiemannZeta #Claude #Anthropic #MachineLearning #Research #FormalVerification #Subagents #MathematicalDiscovery
