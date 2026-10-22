---
title: Recursive Releases Flint, an Open-Weight 40B MoE Local Coding Model for Agents
  with 2.5B Active Params
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/21/recursive-flint-local-coding-model/
model: claude-code/sonnet
generated_at: '2026-10-22T20:44:10.928853'
score: 104
---

📌 開源 40B MoE 編碼模型 Flint：2.5B 活躍參數主打本機速度

TL;DR：Recursive 推出開源 MoE 編碼模型 Flint，40B 總參數僅 2.5B 活躍，強調本機端高速推理。

多數編碼模型這幾年都在往「更大」的方向堆參數，Recursive Superintelligence 這次卻反過來打：用遠小於對手的活躍參數量，搶佔本機端推理速度這個戰場。

🤔 **Recursive 的第一個模型，由自家自動化研究系統打造**

Recursive Superintelligence 發布了公司首個模型 Flint，官方表示幾乎整套技術堆疊都是靠自家的自動化研究系統「Eureka Machine」協助打造完成，權重已以 Apache 2.0 授權上架 Hugging Face。Flint 定位是給編碼 agent 用的本機模型，可以探查程式碼庫、修 bug、實作功能、寫測試，純文字輸入輸出，支援推理（reasoning）與 OpenAI 相容的 tool call。

🧩 **49 層 Transformer，256 個路由專家，兩種 attention 混搭**

Flint 是 decoder-only 的 MoE Transformer，共 49 層：前 2 層是 dense 層，其餘 47 層是 MoE 層。每個 MoE 層有 256 個路由專家（routed experts），router 每個 token 會選 6 個，再加上 1 個永遠啟用的共享專家（shared expert）。

Attention 機制混用兩種型態：35 層採用 513-token 的滑動視窗（sliding window）注意力，另外 14 層則是不帶位置編碼（no positional encoding）的全注意力。架構上使用 32 個 query head、4 個 key/value head。官方標示的 2.5B 活躍參數已包含輸出層，若只算活躍的模型主體，大約是 2.2B 參數。

Eureka Machine 的運作方式是提出想法、實作、測試，再根據結果決定下一步要嘗試什麼，官方表示這套流程貢獻了 3 項主要技術特性（原文未展開列出具體內容）。

📊 **官方宣稱本機推理速度最高快 2 倍**

根據 Recursive 公布的數據，Flint 在 Apple M4 Pro MacBook Pro 上超過 125 tokens/秒，在 64GB NVIDIA RTX Spark 上超過 150 tokens/秒，兩者皆為短上下文（short-context）情境下的數字，官方稱比同量級模型最高快 2 倍，並宣稱比效能相近的 25B 至 40B dense 模型快超過 5 倍。

在 Recursive 自製的比較圖表中，另一款模型 Qwen3.6 在 SWE-bench Verified 拿下 73.4%，dense 模型 Qwen3.8 在 Terminal-Bench 2.1 拿下 73.0%，根據原文敘述明顯高於 Flint 的對應成績。需要注意的是，報導特別說明：對手模型的數字部分來自各自官方的 model card，並非全部出自 Recursive 的比較圖表，兩者口徑不完全一致。

⚠️ **測試條件與口徑落差**

所有分數均為 Recursive 自行回報，採樣設定為 temperature 1.0、top-p 0.95、top-k 20；Terminal-Bench 使用 Terminus 2 harness，透過網路檢索找到答案的解法算失敗；SWE-bench 則用 mini-swe-agent、不連網測試；agentic 分數是至少 5 次嘗試的 pass@1 平均。這些細節意味著跨模型比較時仍需留意評測條件是否對齊。

🎯 **實務啟示**

Flint 官方表示相容 llama.cpp、Ollama、Unsloth、LM Studio、vLLM 與 SGLang，對想在本機或邊緣裝置跑編碼 agent 的團隊，這種高 MoE 稀疏度、低活躍參數的設計路線，值得關注其實際落地後的速度與品質表現。

🔗 **來源**
- 標題：Recursive Releases Flint, an Open-Weight 40B MoE Local Coding Model for Agents with 2.5B Active Params
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/10/21/recursive-flint-local-coding-model/

#OpenSourceAI #MoE #CodingAgent #LLM #LocalInference #Transformer #HuggingFace #AgenticAI #SWEBench #AIModelRelease
