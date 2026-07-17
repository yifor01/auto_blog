---
title: Introducing Grok on Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/introducing-grok-on-amazon-bedrock/
score: 98
model: tencent/hy3:free
generated_at: '2026-07-17T08:08:28.460932'
---

📌 【AWS ML】xAI Grok 4.3 登陸 Amazon Bedrock

TL;DR：Grok 4.3 上架 Bedrock，具百萬 token 上下文與可調推理力度，適合 agent 與企業工作負載。

當多數團隊還在為 agent 的長上下文與穩定工具呼叫頭痛時，xAI 直接把 Grok 4.3 搬上了 Amazon Bedrock。

🤔 **xAI 成為 Bedrock 模型供應商，Grok 4.3 正式可用**

xAI 的 Grok 4.3 已在 Amazon Bedrock 全面開放（generally available）。這代表 xAI 正式以模型供應商身分加入 Bedrock，提供給建置 agent 與 AI 工作流程的團隊使用。官方描述此模型能針對長輸入穩定推理（reasons reliably over long inputs）。

🧩 **為 agent 與企業場景設計的核心能力**

README 指出，Grok 4.3 具備以下特性：
- 可配置推理力度（configurable reasoning effort），單一模型可透過每個請求設定 effort level（none、low、medium、high）來服務從輕量到重度的各種任務。
- 強工具使用（tool use）與指令遵循（instruction following）能力，適合建置 agent。
- token 效率（token efficiency），有利高用量推論。
- 接受文字與圖片輸入，並擁有 100 萬 token 上下文視窗，可處理長檔案與多輪對話。
- 模型執行於 Mantle，即 Amazon Bedrock 的新世代推論引擎。

📊 **xAI 自述的評測表現**

根據 xAI 宣稱，Grok 4.3 鎖定準確度攸關的企業工作。在其自身發布時的基準測試中：
- 於 Artificial Analysis Omniscience 基準拿下第 1，且在前沿模型中幻覺率最低。
- 於 Artificial Analysis Tau2 Telecom 基準（客服場景工具呼叫）排名第 1。
- 於 Vals AI Case Law 與 Corporate Finance 基準（檔案理解）均排名第 1。
- xAI 稱該模型位於「智慧對成本」的 Pareto 前沿，描述為每美元智慧程度比其他前沿模型高 2 到 10 倍。

🎯 **實務啟示**

對在 Bedrock 上建系統的 ML 工程師來說，Grok 4.3 提供單一模型透過 per-request effort 切換輕重任務的彈性：例如分類呼叫可用 none 力度壓低延遲，需要深度推理時再拉高。長上下文與圖片輸入也讓多輪 agent、長檔案理解可直接在同一模型上跑，減少管線拼接。

🔗 **來源**
- 標題：Introducing Grok on Amazon Bedrock
- 作者／機構：Melanie Li（AWS ML，與 xAI 的 Eric Jiang 合寫）
- 連結：https://aws.amazon.com/blogs/machine-learning/introducing-grok-on-amazon-bedrock/

#AmazonBedrock #xAI #Grok4 #LLM #AgenticAI #LongContext #ToolUse #ModelProvider #EnterpriseAI #InferenceEngine
