---
title: 'Anthropic Releases Claude Fable 5.1 and Claude Mythos 5.1: 52.6% on Terminal-Bench-Science
  and 75% Cheaper Cache Reads'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/01/anthropic-releases-claude-fable-5-1-and-claude-mythos-5-1-52-6-on-terminal-bench-science-and-75-cheaper-cache-reads/
model: nvidia/nemotron-3-ultra-550b-a55b:free
generated_at: '2026-09-02T10:15:34.712141'
score: 95
---

📌 Fable 5.1 基準與價格  
TL;DR：Claude Fable 5.1 基準達 52.6%，快取讀取成本降 75%。  

就在三個月前，Fable 5 才剛發布，現在同一底層模型卻在科學代理基準上躍升近兩倍。這種效能跳躍伴隨著快取讀取費用的大幅下降，到底是怎麼做到的？  

🤔 背景或問題  
Anthropic 在六月發布 Fable 5 系列，三個月後推出 Claude Fable 5.1 與 Claude Mythos 5.1。兩款模型共用同一底層模型，僅在防護層（safeguard layers）上有所不同。Fable 5.1 於 Claude API、Amazon Bedrock、Claude Platform on AWS、Google Cloud、Microsoft Foundry 公開提供；Mythos 5.1 僅限對經審核的美國組織（Project Glasswing）開放。  

🧩 方法或架構  
兩模型均提供 1M token 上下文視窗與 128K 最大輸
