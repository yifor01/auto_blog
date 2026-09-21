---
title: 'Show HN: jevc – compile policy prompts into deterministic verdict programs'
source: Github.com
url: https://github.com/doronp/jevc
model: claude-code/sonnet
generated_at: '2026-09-21T21:22:24.422481'
score: 72
---

📌 jevc：把 Policy Prompt 編譯成確定性判決程式

TL;DR：jevc 把自然語言寫成的 agent 政策，編譯成由程式碼算出結論的確定性判斷器。

讓 LLM 直接讀一大段政策文字，然後自己下「通過／拒絕」的最終判決，聽起來方便,但每次生成的結論可能因為措辭、順序甚至取樣隨機性而飄移。jevc 的思路是把這個責任拆開：模型只負責回答窄範圍的證據問題,真正的判決邏輯留給確定性的程式碼去算。

🤔 **問題：把判決權完全交給模型並不穩**

當 agent 的「政策」（policy）以自然語言形式存在,並直接要求模型輸出最終裁決時，同樣的輸入在不同次呼叫可能得到不一致的結果，也難以稽核「為什麼」會這樣判。jevc 想解決的正是這種不確定性,讓 policy 的執行結果變得可預期、可重現。

🧩 **設計理念：證據交給模型，判決交給程式碼**

根據 README 的說明，jevc 的核心做法是把政策文字（policy prose）編譯成「確定性判決程式」（deterministic verdict programs）：模型只需要回答一組窄範圍的證據問題,實際的最終判決則由編譯出來的程式碼計算得出。這種「模型負責感知、程式碼負責決策」的分工，與讓模型端到端輸出判決的做法相比,理論上能讓同一套政策在重複執行時得到一致的結果。

🚀 **安裝方式**

目前 README 提供的操作資訊僅止於安裝指令：

```
npm i -g jev-compiler
```

⚠️ **素材有限，細節仍待觀察**

必須說明的是，這次取得的素材非常精簡，只包含一句核心概念描述與安裝指令，並未提供具體的政策撰寫語法、編譯流程範例、輸出格式,或是與其他 guardrail 工具的效能比較。作為一個剛在 Show HN 上亮相的專案，它目前更像是一個值得追蹤的概念驗證，實際能否撐起複雜政策場景，還需要看後續文件與範例補齊之後才能判斷。

🎯 **實務啟示**

如果你的 agent 系統中有需要穩定、可重現輸出的守門邏輯（例如內容審核通過與否、風控放行與否），「把證據蒐集交給 LLM、把最終判決交給確定性程式碼」是一個值得參考的架構方向,能降低生成式模型在關鍵決策點上的不穩定性。在細節文件更完整之前，建議先關注它的專案動態，再評估是否導入生產環境。

🔗 **來源**
- 標題：Show HN: jevc – compile policy prompts into deterministic verdict programs
- 作者／機構：doronp
- 連結：https://github.com/doronp/jevc

#jevc #AIAgents #Guardrails #PolicyAsCode #LLM #DeterministicAI #OpenSource #AgentSafety #PromptEngineering #NodeJS
