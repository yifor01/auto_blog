---
title: "May 7, 2026AlignmentDonating our open-source alignment tool"
source: Anthropic Research
url: https://www.anthropic.com/research/donating-open-source-petri
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-05-08T20:37:45.023739
---

📌 【Anthropic】捐赠开源对齐工具Petri 3.0

你以為AI對齊測試結果可信？其實模型可能早就知道你在測它。
這會導致評估完全失真，無法看到模型真實行為。
Anthropic 最新工具更新，直接針對這個痛點優化。

🤔 **開放對齊工具是AI社區共同需求**
AI模型對齊評估是產業核心議題，過往多數對齊測試工具封閉、難以複用。Anthropic於2025年10月推出開源對齊測試工具箱Petri，由Anthropic Fellows項目開發，可快速簡便地測試任意大語言模型的欺騙、諂媚、配合有害請求等風險傾向，目標是為整個AI開發社區提供開放可用的對齊工具。

🧪 **雙模型架構，Claude全系列與外部機構採用**
Petri的評估流程採用雙模型設計：由獨立「審計員」模型模擬各類對齊相關場景，對比目標模型行為，再由「裁判」模型對互動文本進行打分，識別不對齊行為。自Claude Sonnet 4.5起，所有Claude模型的对齐评估均采用Petri，且已被外部機構採用，例如英國AI安全研究所（AISI）將其作為評估模型破壞AI研究傾向的核心工具。

 **Petri 3.0三大升級：適配性、真實性、深度**
2026年5月7日，Anthropic宣布更新Petri至3.0版本，核心更新包含三項：
1. 適應性（Adaptability）：重大架構調整，將審計員模型與目標模型拆分為獨立組件，可分別調整，支援更多客製化使用場景。
2. 真實性（Realism）：新增「Dish」插件，解決過往測試人工痕跡過重、模型察覺為測試導致結果失真的問題，可使用模型真實系統提示詞、真實部署用的「腳手架」（包裹模型以協助達成目標的軟體）執行測試，還原真實部署場景。
3. 深度（Depth）：強化評估深度，目前官方僅公開部分更新細節，完整資訊尚未釋出。

🎯 **對齊評估門檻大降，全社區可直接使用**
Petri為完全開源工具，可應用於任意大語言模型，本次3.0更新進一步降低對齊測試的技術門檻。對工程師而言，這套開箱即用的工具可直接用於探查任意LLM的欺騙、諂媚、有害配合傾向，回應社區對模型安全評估的強烈需求。無論是模型開發者、安全研究員還是監管機構，都可快速用於評估模型的潛在風險，解決過往對齊測試不透明、難複現的痛點。

🔗 **資源連結**
📝 發布機構：Anthropic Research
📅 發布日期：2026年5月7日
🔗 原文連結：https://www.anthropic.com/research/donating-open-source-petri

你會用Petri測試你正在使用的AI模型嗎？歡迎在留言區分享你的看法👇

#AI安全 #對齊技術 #Anthropic #Petri #開源工具 #LLM評估 #AI研究
