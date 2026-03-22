---
title: "用多 Agent 框架做晶片驗證，準確度提升 70%"
date: "2026-03-04"
paper_url: "https://arxiv.org/abs/2603.03175"
paper_title: "Saarthi for AGI: Towards Domain-Specific General Intelligence for Formal Verification"
tags: [Agent, Formal Verification, RAG]
tldr: "多 Agent 框架做晶片驗證準度提升 70%"
---

晶片設計裡有一個環節叫 formal verification（形式驗證），簡單說就是用數學方法證明你的電路設計沒有 bug。這件事極其重要，因為晶片一旦流片就改不了，一個邏輯錯誤可能代表幾百萬美金的損失。問題是，寫 formal verification 的 assertion 需要非常專業的工程師，人力稀缺且昂貴。**Infineon**（英飛凌）的團隊問了一個大膽的問題：能不能讓 AI Agent 來做這件事？

## 🔍 Formal Verification 為什麼這麼難自動化

先講一下背景。Formal verification 不是跑 testbench 看波形那種模擬驗證，而是要寫出 **SystemVerilog Assertion**（SVA），用數學方式窮舉所有可能的狀態去證明設計正確。一個中等複雜度的 IP block 可能需要幾十到上百條 assertion，每一條都要精確描述電路的時序行為。

LLM 在這個領域的挑戰很具體：SVA 的語法很嚴格，時序邏輯的表達容易出錯，而且驗證工程師的 domain knowledge 非常深。之前 Infineon 就做過第一版的 **Saarthi** 框架，用多個 AI Agent 協作來完成從規格到驗證閉合的完整流程，但準確率只有大約 **40%**。在晶片驗證這個領域，40% 基本上不能用。

## 🛠️ 兩個關鍵改進

這次的升級版 Saarthi 做了兩個核心改進：

第一個是「**結構化規則書 + 規格文法**」。他們不是直接讓 LLM 自由生成 SVA，而是定義了一套嚴格的 specification grammar，Agent 必須按照這個文法來組織輸出。同時配上一本 rulebook，裡面記錄了常見的 SVA 寫法規範和錯誤模式。這有點像是給 LLM 戴上了護欄 → Agent 的創造力受限，但犯錯的機會也大幅降低。

我覺得這個設計很務實。晶片驗證不需要 LLM 有多「有創意」，需要的是精確和可控。用結構化的約束來限制輸出空間，比讓 LLM 自由發揮再用後處理修正，效果好得多。

第二個改進是整合 **GraphRAG**。傳統的 RAG 是把文件切 chunk 丟進 vector store，但硬體驗證的知識有很強的結構性 → 信號之間有依賴關係、時序有先後順序、模組之間有層次結構。GraphRAG 用知識圖譜來組織這些關係，讓 Agent 在迭代修正的時候能查到更精準的技術知識和 best practice。

這兩個改進的效果：

- SVA 生成準確率提升 **70%**
- 達到 coverage closure 所需的迭代次數減少 **50%**

他們用 **NVIDIA** 的 CVDP benchmark 來測試，這是業界認可的高難度測試集，所以數字是有說服力的。

## 💡 Domain-Specific AGI 的正確打法

坦白說，論文標題裡的「AGI」用得有點大膽。他們自己也承認離真正的 AGI 還很遠。但我覺得這篇論文展示了一個重要的趨勢：與其追求通用 AGI，不如在特定 domain 把 Agent 做到真的能用。

這篇論文提出的 **STSC**（Short Term, Short Context）概念值得注意。他們認為 formal verification 的子任務大多是「短期記憶、短上下文」的，每一步的推理不需要太長的 context window，但需要精確。這跟寫長篇小說或做多輪對話不同，LLM 目前的能力剛好可以勝任。這個分析框架可以幫助其他領域判斷「AI Agent 在我的場景到底可不可行」。

不過 **40%** → **70%**（經過改進後的推算）雖然進步明顯，離生產級的要求還有距離。晶片驗證需要的準確率接近 **100%**，因為漏掉一個 corner case 的代價太高。所以目前 Saarthi 的定位比較像是「輔助工具」而非「替代方案」→ 幫驗證工程師生成初版 assertion，人再來 review 和修正。

另一個我好奇的點是，GraphRAG 的知識庫怎麼維護？硬體設計的規範會隨著製程和架構演進，如果知識圖譜的更新跟不上，RAG 反而可能提供過時的建議。論文沒有討論這個維運成本。

EDA（電子設計自動化）產業正在快速擁抱 AI，**Synopsys**、**Cadence** 都在做類似的事。Saarthi 的開放式研究提供了一個很好的技術參考點，特別是 **rulebook + GraphRAG** 這個組合，我覺得可以推廣到其他需要高精確度、有嚴格語法規範的 code generation 場景。

如果你在做 Agent 系統設計，這篇論文的 structured rulebook 思路值得借鏡：不要讓 Agent 自由發揮，給它一套明確的遊戲規則。

📎 [論文連結](https://arxiv.org/abs/2603.03175)

<!-- fb -->

晶片設計裡有一個環節叫 formal verification（形式驗證），簡單說就是用數學方法證明你的電路設計沒有 bug。這件事極其重要，因為晶片一旦流片就改不了，一個邏輯錯誤可能代表幾百萬美金的損失。問題是，寫 formal verification 的 assertion 需要非常專業的工程師，人力稀缺且昂貴。Infineon（英飛凌）的團隊問了一個大膽的問題：能不能讓 AI Agent 來做這件事？

🔍 Formal Verification 為什麼這麼難自動化

先講一下背景。Formal verification 不是跑 testbench 看波形那種模擬驗證，而是要寫出 SystemVerilog Assertion（SVA），用數學方式窮舉所有可能的狀態去證明設計正確。一個中等複雜度的 IP block 可能需要幾十到上百條 assertion，每一條都要精確描述電路的時序行為。

LLM 在這個領域的挑戰很具體：SVA 的語法很嚴格，時序邏輯的表達容易出錯，而且驗證工程師的 domain knowledge 非常深。之前 Infineon 就做過第一版的 Saarthi 框架，用多個 AI Agent 協作來完成從規格到驗證閉合的完整流程，但準確率只有大約 40%。在晶片驗證這個領域，40% 基本上不能用。

🛠️ 兩個關鍵改進

這次的升級版 Saarthi 做了兩個核心改進：

第一個是「結構化規則書 + 規格文法」。他們不是直接讓 LLM 自由生成 SVA，而是定義了一套嚴格的 specification grammar，Agent 必須按照這個文法來組織輸出。同時配上一本 rulebook，裡面記錄了常見的 SVA 寫法規範和錯誤模式。這有點像是給 LLM 戴上了護欄 → Agent 的創造力受限，但犯錯的機會也大幅降低。

我覺得這個設計很務實。晶片驗證不需要 LLM 有多「有創意」，需要的是精確和可控。用結構化的約束來限制輸出空間，比讓 LLM 自由發揮再用後處理修正，效果好得多。

第二個改進是整合 GraphRAG。傳統的 RAG 是把文件切 chunk 丟進 vector store，但硬體驗證的知識有很強的結構性 → 信號之間有依賴關係、時序有先後順序、模組之間有層次結構。GraphRAG 用知識圖譜來組織這些關係，讓 Agent 在迭代修正的時候能查到更精準的技術知識和 best practice。

這兩個改進的效果：

SVA 生成準確率提升 70%
達到 coverage closure 所需的迭代次數減少 50%

他們用 NVIDIA 的 CVDP benchmark 來測試，這是業界認可的高難度測試集，所以數字是有說服力的。

💡 Domain-Specific AGI 的正確打法

坦白說，論文標題裡的「AGI」用得有點大膽。他們自己也承認離真正的 AGI 還很遠。但我覺得這篇論文展示了一個重要的趨勢：與其追求通用 AGI，不如在特定 domain 把 Agent 做到真的能用。

這篇論文提出的 STSC（Short Term, Short Context）概念值得注意。他們認為 formal verification 的子任務大多是「短期記憶、短上下文」的，每一步的推理不需要太長的 context window，但需要精確。這跟寫長篇小說或做多輪對話不同，LLM 目前的能力剛好可以勝任。這個分析框架可以幫助其他領域判斷「AI Agent 在我的場景到底可不可行」。

不過 40% → 70%（經過改進後的推算）雖然進步明顯，離生產級的要求還有距離。晶片驗證需要的準確率接近 100%，因為漏掉一個 corner case 的代價太高。所以目前 Saarthi 的定位比較像是「輔助工具」而非「替代方案」→ 幫驗證工程師生成初版 assertion，人再來 review 和修正。

另一個我好奇的點是，GraphRAG 的知識庫怎麼維護？硬體設計的規範會隨著製程和架構演進，如果知識圖譜的更新跟不上，RAG 反而可能提供過時的建議。論文沒有討論這個維運成本。

EDA（電子設計自動化）產業正在快速擁抱 AI，Synopsys、Cadence 都在做類似的事。Saarthi 的開放式研究提供了一個很好的技術參考點，特別是 rulebook + GraphRAG 這個組合，我覺得可以推廣到其他需要高精確度、有嚴格語法規範的 code generation 場景。

如果你在做 Agent 系統設計，這篇論文的 structured rulebook 思路值得借鏡：不要讓 Agent 自由發揮，給它一套明確的遊戲規則。

📎 論文連結：https://arxiv.org/abs/2603.03175

#Agent #FormalVerification #RAG #GraphRAG #EDA #GenAI #ChipDesign
