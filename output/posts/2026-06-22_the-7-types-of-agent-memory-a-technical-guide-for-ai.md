---
title: 'The 7 Types of Agent Memory: A Technical Guide for AI Engineers'
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/21/the-7-types-of-agent-memory-a-technical-guide-for-ai-engineers/
score: 82
model: google/gemma-4-31b-it:free
generated_at: '2026-06-22T21:08:36.271631'
---

📌 **打造 AI Agent 的關鍵：深入解析 7 種記憶機制與其技術分類**

TL;DR：將 LLM 從「無狀態」轉化為具備記憶能力的 Agent，需透過引數化與非引數化記憶來管理不同時效的資訊。

LLM 本質上是 stateless（無狀態）的。每一次 API 呼叫都像是一次全新的開始，一旦回應回傳，模型就會忘記之前的所有對話。對於單次問答這沒問題，但如果你在開發 AI Agent，這種特性將成為致命傷。

當 Agent 需要規劃路徑、呼叫工具或執行多步驟任務時，它必須具備「記憶」能力。記憶是將無狀態模型轉化為能保留上下文、從經驗中學習並隨時間採取行動之系統的核心基礎。

🧩 **記憶的兩個維度：形式（Form）與時間（Time）**

記憶的本質是任何能將資訊在模型推理過程中傳遞的機制。根據素材，記憶可從兩個軸線來定義：
- **形式 (Form)**：分為引數化（Parametric，儲存在模型權重中）與非引數化（Non-parametric，儲存為純文字）。
- **時間 (Time)**：分為短期（Short-term）與長期（Long-term）。

基於這兩個維度，AI Agent 的記憶可細分為以下型別（目前揭露 4 種）：

🧠 **短期記憶：In-Context / Working Memory**
這相當於系統的 RAM。所有目前處於 context window（上下文視窗）內的資訊都屬於此類，包含：
- 系統提示詞 (System Prompt)
- 近期的對話訊息
- 工具執行的輸出結果
- 推理步驟 (Reasoning steps)
其特性是速度快且至關重要，但具有暫時性且空間有限，且所有其他型別的記憶最終都要競爭這個有限的空間。

📚 **長期記憶：三種不同的儲存形式**

- **Semantic Memory（語義記憶）**：一個持久化的事實、偏好與領域知識庫。例如記錄「使用者偏好 Python 而非 JavaScript」。這類知識與學習的時間點脫鉤，像是 Agent 關於使用者或特定主題的組織化百科全書。
- **Episodic Memory（情節記憶）**：記錄特定的過去事件、完整的對話紀錄與任務執行過程。它記錄了哪些方法有效、哪些失敗，讓 Agent 能從經驗中學習。例如 Reflexion 與 ExpeL 等系統會撰寫文字形式的「事後分析 (post-mortems)」並儲存結論供未來使用。
- **Procedural Memory（程式記憶）**：關於「如何操作」的知識。涵蓋了技能、工具使用模式、工作流 (workflows) 以及行為準則。

🎯 **實務啟示**

對於 AI 工程師而言，設計 Agent 時不應將所有資訊都塞進 context window，而應根據資訊的性質選擇儲存策略：
- **即時推理** $\rightarrow$ 使用 Working Memory。
- **使用者偏好與事實** $\rightarrow$ 建立 Semantic Memory 儲存庫。
- **錯誤修正與經驗累積** $\rightarrow$ 實作 Episodic Memory 記錄執行日誌。
- **標準作業程式 (SOP)** $\rightarrow$ 定義 Procedural Memory 規範工具使用路徑。

🔗 **來源**
- 標題：The 7 Types of Agent Memory: A Technical Guide for AI Engineers
- 作者／機構：Asif Razzaq
- 連結：https://www.marktechpost.com/2026/06/21/the-7-types-of-agent-memory-a-technical-guide-for-ai-engineers/

#AI #LLM #AIAgents #Memory #MachineLearning #ContextWindow #SemanticMemory #EpisodicMemory #ProceduralMemory #SoftwareArchitecture
