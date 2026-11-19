---
title: Build Tool-Calling Parsers in Rust with AI Agents
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/build-tool-calling-parsers-in-rust-with-ai-agents/
model: claude-code/sonnet
generated_at: '2026-11-19T23:52:26.067683'
score: 87
---

📌 NVIDIA教你用AI Agent打造Rust工具呼叫解析器

TL;DR：NVIDIA工程師示範如何用AI agent搭配共用的Conformance Corpus測試集，替新模型打造Dynamo的工具呼叫（tool-calling）解析器。

🎣 **半個城市名就能讓整個agent迴圈卡住**

想像你問模型「巴黎的天氣如何」，模型先生成一段推理，再呼叫get_weather並帶上city參數。但如果串流到一半，模型只吐出「Par」就斷了，或是呼叫了一個根本沒被提供的工具，負責把token拆成「可見文字、推理內容、工具呼叫」三部分的parser，稍有不慎就會讓資料遺失、呼叫重複，或讓模型專屬的標記語法洩漏到最終答案裡。

🤔 **解析器要擋住哪兩種壞輸出**

NVIDIA Developer部落格作者Keiven Chang以NVIDIA Nemotron為例，列出兩種典型失敗：

- 語法錯誤：參數與工具呼叫框架沒有正常收尾，city參數值被截斷成「Par」，整段呼叫無法被完整解析。
- 語意錯誤：呼叫框架格式正確，但指名的工具（unknown_tool）根本不在可用工具清單中。

兩種錯誤處理方式不同：面對語意錯誤，parser應原樣回報模型實際生成的呼叫，再交由serving層去驗證工具是否存在、授權與schema是否吻合；擅自改寫工具名稱等於掩蓋了模型真正輸出的內容。至於語法錯誤，難處在串流尚未結束時無法判斷——城市名的其餘部分可能在下一個chunk才送達，連標記符號本身都可能被切成兩半。parser必須有一套一致規則，決定什麼時候該輸出、什麼時候該先緩衝，以及串流結束時該如何收尾。

🧩 **從token到回應的完整流程**

整條管線是：前端準備並tokenize提示詞 → 推理引擎執行LLM生成token → parser消費token ID或解碼後文字，依序拆出推理內容、可見文字與工具呼叫 → 協定adapter再把這些事件轉成OpenAI相容的回應，批次JSON與串流更新走的是同一條解析路徑。

為了驗證解析器行為是否正確，frontend-crates（NVIDIA Dynamo工具呼叫解析器背後可重用的Rust元件）維護一份共用的Conformance Corpus：用語言無關的YAML fixture，把固定輸入與預期輸出（稱為GOLDEN）配對起來，讓Rust解析器與Python參考實作可以跑同一組測試案例。

📊 **同一個行為，四種模型標記語法**

Conformance Corpus裡的UNIFIED.1-tool_only案例示範了這個概念：四個不同模型家族各自用完全不同的原生標記語法，但都應該解析出同一個GOLDEN結果——get_weather({"city": "Paris"})：

- Beam：`<|start|>assistant to=get_weather<|channel|>analysis<|constrain|>xml<|message|><rfl:parameter name="city">Paris</rfl:parameter><|call|>`
- GPT-OSS：`<|start|>assistant<|channel|>commentary to=functions.get_weather<|constrain|>json<|message|>{"city": "Paris"}<|call|>`
- Muse Spark：`<|start|>assistant to=get_weather<|message|><atem:function_calls><atem:invoke name="get_weather"><atem:parameter name="city">Paris</atem:parameter></atem:invoke></atem:function_calls><|eom|>`
- NVIDIA Nemotron 3：`</think><tool_call><function=get_weather><parameter=city>Paris</parameter></function></tool_call>`

標記語法各不相同，測的卻是同一個行為。新parser要支援的模型，只要把UNIFIED.*案例的輸入格式改寫成該模型的語法，就能重複利用既有的行為測試，不必從零設計。

💡 **讓AI agent照著SKILL.md自己寫parser**

文章提供一套具體工作流程，讓AI agent在frontend-crates checkout裡依照`.agents/skills/tool-parser-generator/SKILL.md`為新模型建立v2 Unified parser：

1. 下指令：請agent研究目標模型的grammar，準備GOLDEN測試集（調整適用的UNIFIED.*案例），完成後先暫停等人工審查，核准後才實作、驗證，並附上本地conformance報告連結供人工檢查。
2. 定義GOLDEN測試集：agent會在`conformance/fixtures-unified-v2/families/<name>/inputs_and_golden.yaml`中獨立產出初始測試案例，每筆案例把輸入與預期輸出配對。例如nemotron_v3家族的一筆案例，輸入是帶有`<tool_call>`標記的文字，GOLDEN則是`kind: tool_call, name: get_weather, arguments: {city: Paris}`。
3. 反覆迭代：agent撰寫或修正parser、跑測試，再用失敗案例引導下一步修改；若agent建議更動預期行為，人必須先審查再採用。

整個單元測試流程只需CPU與固定測試fixture即可執行，不需要GPU；但要做端到端測試，仍需要一套能運作的Dynamo runtime、discovery服務，以及對應模型的硬體。

⚠️ **AI生成的測試集，也可能是錯的**

作者特別提醒：GOLDEN測試集定義了parser應被驗證的行為，如果這些期望值本身是錯的，parser即使通過測試也可能行為不正確。agent產生的初始測試集可能帶有錯誤，因為預期行為往往取決於agent不一定掌握的上下文。建議先讓agent做一次對抗性審查，再逐案人工檢查；部署前也務必用真實模型與GPU跑過端到端測試，不能只靠單元測試就宣稱支援到位。

🎯 **實務啟示**

對維護LLM serving層的工程師來說，這是一種務實的AI輔助開發模式：讓agent先生成假設（測試案例與實作），但保留人工審查這一關，尤其是「預期結果」這個環節。善用跨模型共用的Conformance Corpus，也能把過去為某個模型寫的迴歸測試，低成本複用到新模型的parser開發上。

🔗 **來源**
- 標題：Build Tool-Calling Parsers in Rust with AI Agents
- 作者／機構：Keiven Chang，NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/build-tool-calling-parsers-in-rust-with-ai-agents/

#NVIDIA #Rust #ToolCalling #LLMInference #AIAgents #Dynamo #StreamingParser #OpenSource #LLMOps #AgenticEngineering
