---
title: 'Beyond the Single Camera: Agentic Multi-View Reasoning in Sports Video Understanding'
source: arXiv
url: http://arxiv.org/abs/2607.11844v1
score: 100
model: tencent/hy3:free
generated_at: '2026-07-14T07:55:38.882176'
---

📌 多視角體育影片理解基準與 Agent

TL;DR：SportMV-Bench 暴露 MLLM 多視角弱點，SportMV-Agent 相對提升 14.46%。

🎣 單一鏡頭下，球員掩護與快攻讓 AI 看不清犯規瞬間。但真實賽事有多機位錄影，現有影片理解基準卻從未考驗模型整合多視角的能力。

🤔 單視角 MLLM 難解體育影片的遮蔽與混戰
近期多模態大型語言模型（MLLM）在單視角影片理解基準表現強健，然而體育影片包含密集遮蔽、快速運動與複雜互動，單一觀點難以釐清。實務上賽事以多鏡頭拍攝，提供互補證據給裁判，但既無基準評估 MLLM 的多視角體育影片理解能力。

🧩 從官方錄影建出 787 組多視角包與三類任務
作者提出 SportMV-Bench，從官方比賽錄影出發，透過結合 LLM 生成、MLLM 驗證與人工過濾的專屬管線，確保品質與一致性。資料集含 787 個多視角影片包（multi-view video bundles）與 2592 個問答對，涵蓋三類：感知覺察辨識（Perception-Aware Recognition, PAR）、規則覺察事件詮釋（Rule-aware Event Interpretation, REI）、裁決決策推理（Adjudicative Decision Reasoning, ADR）。

同時提出 SportMV-Agent，一個代理式（agentic）框架，協調迭代迴圈：主動視角選擇（active view selection） → 感知工具執行（perception tool execution） → 證據奠基推理（evidence-grounded reasoning），反覆精煉答案。

📊 瓶頸在細節感知與選視角，Agent 相對漲 14.46%
分析顯示，當前 MLLM 未能有效利用多視角資訊，瓶頸在於細粒度視覺感知與視角選擇，而非邏輯推理或領域知識。SportMV-Agent 相較最強 MLLM 基準線，達成 14.46% 的相對效能提升。

🎯 多視角融合與主動選視角才是實戰重點
對工程師而言，若要在體育或監控等需多機位的場景部署 MLLM，不應只堆疊單視角模型；可參考代理式架構，讓模型主動挑選關鍵鏡頭並呼叫感知工具，才能補足遮蔽與快速動作的資訊缺口。

🔗 來源
- 標題：Beyond the Single Camera: Agentic Multi-View Reasoning in Sports Video Understanding
- 作者：Kerui Chen, Jinglu Wang, Xiaoyi Zhang, Yan Lu
- 連結：http://arxiv.org/abs/2607.11844v1

#MultiView #SportsVideo #MLLM #Benchmark #Agent #VideoUnderstanding #SportMVBench #Reasoning #ComputerVision #arXiv
