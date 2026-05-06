---
title: "Workspace-Bench 1.0: Benchmarking AI Agents on Workspace Tasks with Large-Scale File Dependencies"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.03596
score: 123
model: tencent/hy3-preview:free
generated_at: 2026-05-06T20:03:55.462381
---

📌 【上海交大/字节跳动/MIT/清华联合研究】推出Agent工作空间评估基准

現有AI Agent評測多採用預指定或合成文件，真實依賴關係有限，難以反映實際工作場景能力。最新基準測試顯示，當前最佳Agent在工作空間任務的準確率僅68.7%，遠低於人類的80.7%。

🤔 **现有Agent评测缺真实文件依赖，落地参考价值低**
Workspace learning要求AI代理能夠識別、推理、利用並更新工作者工作空間中異構文件間的顯式與隱式依賴，才能有效完成常規與進階任務。但現有相關基準大多基於預指定或合成文件構建，真實世界依賴關係有限，針對工作空間層級的評估長期處於空白。

🧪 **覆盖5类工作者、2万+文件、388项真实任务**
研究團隊構建了貼近真實場景的工作空間
