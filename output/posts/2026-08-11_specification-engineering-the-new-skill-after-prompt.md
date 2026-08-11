---
title: 'Specification Engineering: The New Skill After Prompt Engineering'
source: KDnuggets
url: https://www.kdnuggets.com/specification-engineering-the-new-skill-after-prompt-engineering
model: tencent/hy3:free
generated_at: '2026-08-11T07:08:39.867667'
score: 93
---

📌 【趨勢預警】Prompt Engineering 已經不夠用了，Specification Engineering 才是下一波核心技能

TL;DR：從「如何提問」轉向「如何定義工作」，Specification Engineering 正在成為開發 AI Agent 與自動化流程的關鍵。

隨著 AI 從單純的聊天機器人（Chatbots）演進為編碼代理（Coding Agents）、研究助理與數據科學副駕駛（Copilots），單純寫出「好的提示詞（Prompt）」已不足以應付複雜任務。現在，工程師需要掌握的是「規格工程（Specification Engineering）」：這不僅是關於如何提問，更是關於如何定義什麼才叫做「正確完成」。

🤔 **為什麼 Prompt Engineering 已經不夠用了？**

一個好的 Prompt 可能會產生看起來很漂亮的答案，但 Specification（規格）則是用來定義這個答案是否真的「可以被接受」。

當 AI 開始處理 SQL 查詢、修改程式碼庫、分析試算表或進行多步驟決策時，核心問題不再只是「模型會不會回答」，而是：
- 它是否滿足了所有需求？
- 它是否遵守了限制條件？
- 它處理邊緣案例（Edge cases）了嗎？
- 輸出結果是否可以被其他系統消費？
- 它是否優化了錯誤的目標（Specification gaming）？

例如，要求 AI 「修復這個 Bug」，它可能提供一個能通過視覺測試的補丁，卻破壞了隱藏的系統假設。這就是「提示詞成功了，但規格失敗了」的典型場景。

🧩 **從「隨機提問」轉向「可執行指令集」**

Specification Engineering 的實踐，是將模糊的任務轉化為可執行、可測試、可審核的指令集。

| 弱提示詞 (Weak Prompt) | 強規格 (Better Specification) |
| :--- | :--- |
| 「分析這個客戶流失數據集並給我洞察。」 | 「分析此數據集。識別缺失值、類別不平衡、洩漏風險與關鍵特徵。在預處理前先進行訓練/測試集分割。對比 Logistic Regression、Random Forest 與 XGBoost。報告 Accuracy、F1 與 ROC-AUC。不要宣稱因果關係。提供三個基於相關性的業務建議。」 |

一個完整的規格通常包含：
- **目標 (Objective)**：模型應達成什麼？
- **內容 (Context)**：模型需要知道什麼？
- **輸入 (Inputs)**：允許使用哪些資料、工具或假設？
- **輸出格式 (Output format)**：最終答案長什麼樣？
- **限制 (Constraints)**：模型應該避免什麼？
- **評估準則 (Evaluation criteria)**：如何判斷正確性？
- **邊緣案例 (Edge cases)**：可能出錯的地方？
- **驗證步驟 (Verification steps)**：必須通過哪些測試？

📊 **研究顯示：需求導向的訓練效果更顯著**

目前的 AI 產業正從「提示詞」轉向「規格化」。研究與產業實踐皆支持此趨勢：

- **訓練成效差異**：一項關於「需求導向提示工程 (ROPE)」的研究顯示，針對 30 位初學者的隨機對照實驗發現，ROPE 訓練能將需求撰寫能力提升 20%，而傳統的 Prompt Engineering 訓練僅提升 1%。
- **結構化輸出 (Structured Outputs)**：OpenAI 的功能讓開發者能強制模型符合 JSON Schema，這本質上就是 API 形式的規格工程。
- **模型行為規範**：OpenAI 的 Model Spec 與 Anthropic 的 Constitutional AI，皆是透過書面原則來規範模型的行為。

💡 **從「感覺開發」到「規格驅動開發」**

在 AI 編碼領域，這種差異尤為明顯。傳統做法可能是「幫我做一個簡單的記帳 App」，而規格驅動的做法則會明確要求：React 架構、特定功能模組（新增/編輯/刪除/分類篩選）、資料持久化方式（Local storage）、各項功能單元測試，以及禁止使用外部付費 API。

這也解釋了為什麼目前的軟體工程評測（如 SWE-bench）越來越強調解決真實 GitHub Issue 的能力，而非僅僅生成孤立的程式碼片段。

🎯 **新的工作流程：從「Prompt → Output」到「Spec → Audit」**

未來的 AI 工作流將不再是簡單的「提問 → 輸出 → 手動修正」，而是：
**撰寫規格 → 生成 → 驗證 → 修訂 → 審核**

例如，你可以先寫下任務規格，接著要求 AI 找出規格中缺失的部分，再讓它生成解法，最後針對失敗的檢查點進行迭代，並記錄最終的假設與限制。

這也對組織提出了警示：Google DORA 的研究指出，AI 是組織強項與弱點的放大器。強大的流程能讓 AI 發揮更大價值，而混亂的流程則會讓錯誤被無限放大。

🔗 **來源**
- 標題：Specification Engineering: The New Skill After Prompt Engineering
- 作者／機構：Kanwal Mehreen @ KDnuggets
- 連結：https://www.kdnuggets.com/specification-engineering-the-new-skill-after-prompt-engineering

#AI #LLM #PromptEngineering #SpecificationEngineering #SoftwareEngineering #AIAgent #MachineLearning #DeveloperProductivity #OpenAI #Anthropic
