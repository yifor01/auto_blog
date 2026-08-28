---
title: AI Engineer Notebooks – free, framework-free RAG/agents/evals on Colab
source: Hacker News
url: https://github.com/calmrocks/ai-engineer-notebooks
model: claude-code/sonnet
generated_at: '2026-08-28T18:08:34.428196'
score: 82
---

📌 免框架學 LLM 全端:13 本免費 Colab Notebook 練 RAG、Agent 與 Evals

TL;DR:一套從 raw API 到微調、serving 全部框架外撰寫的免費 AI Engineer 練功筆記,在 Hacker News 拿下 111 分。

LangChain、LlamaIndex 幫你把 agent loop、RAG 都包好了,但如果你從沒用 raw API 親手寫過一次,要判斷「什麼時候該用框架、什麼時候不該用」其實很難。這套 AI Engineer Notebooks 反其道而行,堅持先用最原始的 API 呼叫把整個 applied-LLM stack 走過一遍。

🤔 **寫給正在轉職 AI Engineer / FDE 的後端工程師**

作者將受眾定義為「能寫生產程式碼、想補齊 applied-model 這一層」的後端或全端工程師,目標角色包括 AI Engineer、Forward Deployed Engineer(FDE)、Applied AI 或 Solutions Engineer(AI),作者認為這些職稱不同,但實際工作內容大致相同。整套筆記被定位為「Plan: Transitioning to Forward Deployed Engineer / AI Engineer」這份學習計畫的實作搭配教材。

🧩 **框架外優先、Evals 是主幹、全程免費可跑**

三個設計理念貫穿全系列。第一,框架外優先:agent loop、RAG、evals 都先用原始 API 呼叫寫過一遍,理由是「模式是耐久的,框架的包裝會過時」。第二,evals 是主幹:「先量測再調整」的習慣從第 02 章就安裝進去,之後每一章都會回頭用到,作者將其形容為「區分出只是做出 demo,還是真正交付系統的工程師」的關鍵習慣。第三,全程可在免費的 Groq API 上執行,不需信用卡;唯二無法在 Groq 上完成的主題是 LoRA 微調(第 06 章)與自架 serving(第 09 章),這兩章採概念優先講解,並附上已在 Colab 免費 T4 GPU 上驗證過的選用附錄。此外全系列採 OpenAI 相容介面,換個 base URL 就能把同一套 pattern 用在 OpenAI,稍加修改也能搬到 Anthropic。

🧩 **13 本筆記,由淺到深走完整條 applied-LLM 技能樹**

學習順序從 00 到 12,每本筆記獨立成冊(自行安裝依賴、從 Colab secrets 讀取 API key)並在結尾附練習題:

- 00 環境設定:API key 管理、成本控管、模型選型
- 01 Model APIs:提示工程、結構化輸出、tool calling、streaming、context 與 caching
- 02 Evals I:在第 01 章的任務上建立 golden set 與量測指標
- 03 RAG:retrieve → augment → generate 迴圈、embedding 與檢索、混合檢索與 reranking、chunking 策略、RAG 失效診斷
- 04 Evals II:golden set、LLM as judge、回歸型 evals(當成 CI 用)
- 05 Agents:從零寫 agent loop、工具設計、guardrails 與預算控制、MCP 概念、Skills 與漸進式揭露、harness engineering
- 06 模型調適:fine-tune vs RAG vs prompt 的取捨、LoRA/QLoRA 概念,附選用的真實 LoRA 微調
- 07 安全性:prompt injection、OWASP LLM Top 10
- 08 維運:observability、可靠性與 fallback 機制、用 MLflow 做實驗追蹤與模型註冊
- 09 Serving 與推論效能:vLLM、TGI、Triton、TensorRT-LLM 的取捨,continuous batching、KV cache、量化
- 10 ML 系統設計:QPS/VRAM/延遲/成本估算、複本擴展、佇列與快取的權衡
- 11 客戶溝通(FDE 差異化技能):把模糊需求收斂成可評估系統的 scoping 與 discovery
- 12 案例研究與 Capstone:一個「客服助理」案例(從模糊需求到部署、上線後遭遇索引過期的品質回歸並除錯),以及自建部署專案的 Capstone

🎯 **實務啟示**

這套筆記最大的價值不是教新技術,而是強迫你在碰框架之前先理解框架在做什麼。對正在準備 AI Engineer / FDE 面試,或想系統性補齊 RAG、evals、agent、fine-tuning、serving 這條技能鏈的工程師,可以把它當成一份可動手驗證的自我檢核清單:每一章的練習題都是檢驗自己是否真的理解,而非只是跑過範例程式碼。

🔗 **來源**
- 標題:AI Engineer Notebooks – free, framework-free RAG/agents/evals on Colab
- 作者／機構:calmrocks / Hacker News
- 連結:https://github.com/calmrocks/ai-engineer-notebooks

#AIEngineer #LLM #RAG #AIAgents #Evals #PromptEngineering #LoRA #MCP #MLOps #ForwardDeployedEngineer
