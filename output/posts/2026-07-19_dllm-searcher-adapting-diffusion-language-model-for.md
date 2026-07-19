---
title: 'DLLM-Searcher: Adapting Diffusion Language Model for Efficient Search Agents'
source: Semantic Scholar
url: https://www.semanticscholar.org/paper/f053acd7135df48fc65a45cb62848dddd2131928
score: 89
model: tencent/hy3:free
generated_at: '2026-07-19T08:04:49.696386'
---

📌 【Semantic Scholar 論文】用擴散語言模型打造更高效的搜尋代理

TL;DR：DLLM-Searcher 結合 dLLM 與並行推理，搜尋代理推論加速約 15%。

搜尋代理在 ReAct 框架下，每一輪都要「想 → 呼叫工具 → 等回傳」串列執行，端對端延遲相當可觀。但擴散式大型語言模型（diffusion LLM, dLLM）天生支援平行解碼，能不能拿來解這個痛點？

🤔 **兩道關卡：延遲與代理能力都不容忽視**

作者指出，現有搜尋代理受制於兩個核心限制。其一是 Latency Challenge：在 ReAct 代理架構下，多輪推理、工具呼叫與等待工具回應是序列執行，造成嚴重的端對端延遲。其二是 Agent Ability Challenge：現有 dLLM 主幹模型的推理與工具呼叫能力偏弱，導致 dLLM 的效率優勢難以真正落地。

🧩 **兩階段後訓練補強代理能力**

為解決 Agent Ability Challenge，論文提出 DLLM-Searcher 這個針對 dLLM 搜尋代理的最佳化框架，設計了一套兩階段後訓練流程：
- Agentic Supervised Fine-Tuning（Agentic SFT）：透過監督式微調強化主幹模型。
- Agentic Variance-Reduced Preference Optimization（Agentic VRPO）：以降低變異的偏好最佳化進一步提升資訊搜尋與推理能力。

🧩 **P-ReAct：邊等工具回傳邊思考**

為緩解 Latency Challenge，作者利用 dLLM 彈性的生成機制，提出新的代理範式 Parallel-Reasoning and Acting（P-ReAct）。P-ReAct 引導模型優先解碼 tool_call 指令，使模型能在等待工具回傳的同時持續推理，而非單純阻塞等待。

📊 **效能持平主流，推論快約 15%**

實驗結果顯示，DLLM-Searcher 的表現可與主流基於 LLM 的搜尋代理相當；而 P-ReAct 帶來約 15% 的推論加速。作者也指出專案程式碼已開放於 GitHub（github.com/bubble65/DLLM-Searcher）。

🎯 **平行解碼不只是生成快，還能重構代理流程**

對工程師來說，這篇工作的實務啟示在於：若採用 dLLM 作為代理主幹，可透過調整解碼順序（優先 tool_call）把等待時間重疊到推理中，降低端對端延遲；同時需搭配針對代理任務的後訓練，才有辦法補上原生 dLLM 在工具呼叫上的短板。

🔗 **來源**
- 標題：DLLM-Searcher: Adapting Diffusion Language Model for Efficient Search Agents
- 作者／機構：Jiahao Zhao, Shaoxuan Xu, ZhongXiang Sun, Fengqi Zhu, Jingyang Ou
- 連結：https://www.semanticscholar.org/paper/f053acd7135df48fc65a45cb62848dddd2131928

#DiffusionLLM #dLLM #SearchAgent #ReAct #PReAct #AgentSFT #VRPO #InferenceAcceleration #ToolCalling #LLMagent
