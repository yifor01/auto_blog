---
title: Uncertainty Quantification for LLM Function-Calling
source: Apple ML
url: https://machinelearning.apple.com/research/uncertainty-quantification-function-calling
score: 97
model: tencent/hy3:free
generated_at: '2026-07-16T08:14:59.603685'
---

📌 【Apple ML】LLM Function-Calling 的 Uncertainty Quantification 首評

TL;DR：首份 LLM 函式呼叫 UQ 評估指出，多樣本法未勝單樣本法，且輸出結構可補強。

當 LLM 能自主呼叫函式轉帳或刪除資料，一旦呼叫錯誤就是不可逆的後果。在執行前知道「模型自己有多確信這次呼叫是對的」，不再是錦上添花，而是上線的底線。

🤔 **函式呼叫出錯的代價，讓信心估計成為必要**

LLM Function-Calling（FC）是讓模型具備工具使用能力的常見做法。但模型若不正確地呼叫函式，在影響不可逆的場景（如轉帳、刪除資料）下後果嚴重。因此，在實際執行函式前，量化模型對「這次呼叫能正確解決任務」的信心至關重要，而 Uncertainty Quantification（UQ）方法正是用來量化此信心、擋下可能錯誤呼叫的技術。

🧩 **首份 FC 場景的 UQ 方法評估與兩項發現**

這篇由 Apple ML 發表的論文（2026 年 7 月）宣稱，這是已知第一個針對 LLM Function-Calling 的 UQ 方法評估。作者團隊包含來自 University of Oxford 與 Apple 的研究者（以平等貢獻與共同資深作者標註）。

評估結果指出兩個重點：
- 多樣本 UQ 方法（如 Semantic Entropy）在自然語言問答任務表現強，但在 FC 設定下，相較簡單的單樣本 UQ 方法並未展現明顯優勢。
- FC 輸出的特性可被拿來改進現有 UQ 方法：多樣本法可受益於根據 abstract syntax tree（AST）解析對 FC 輸出做聚類；單樣本法則可在計算基於 logit 的不確定性分數時，只挑選語意上有意義的 token 來提升效能。

⚠️ **素材未提及的評估細節**

摘要未提供具體資料集、評估指標數值、baseline 對比量化結果，也未說明實驗規模與訓練設定，因此無從轉述實驗資料與限制章節。

🎯 **實務啟示**

若你在建置具 FC 能力的 agent，不必急著上多樣本 UQ（如多次抽樣算 Semantic Entropy），簡單的單樣本法可能就夠用。進一步可嘗試：對 FC 輸出做 AST 解析聚類來強化多樣本法，或計算 logit 不確定性時濾掉無語意 token，以提升線上攔截錯誤呼叫的可靠度。

🔗 **來源**
- 標題：Uncertainty Quantification for LLM Function-Calling
- 作者／機構：Apple ML（作者群含 Zihuiwen Ye、Lukas Aichberger、Yarin Gal 等，詳見原文）
- 連結：https://machinelearning.apple.com/research/uncertainty-quantification-function-calling

#LLM #FunctionCalling #UncertaintyQuantification #UQ #SemanticEntropy #AST #Logits #ToolUse #AppleML #AgentSafety
