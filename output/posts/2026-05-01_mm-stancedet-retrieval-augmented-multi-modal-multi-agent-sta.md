---
title: "MM-StanceDet: Retrieval-Augmented Multi-modal Multi-agent Stance Detection"
source: ChatPaper/AI
url: https://arxiv.org/abs/2604.27934
score: 112
model: tencent/hy3-preview:free
generated_at: 2026-05-01T19:48:32.434950
---

📌 多模态立场检测新框架MM-StanceDet

🎣 **折疊區優化 (The Hook)**
图文信号冲突时，现有多模态模型常误判立场。
跨模态歧义、单遍推理脆弱，是长期待解痛点。
北大、百度、布朗大学、亚马逊联合提出的新框架，在五個數據集上顯著超越SOTA。

🤔 **图文信号冲突，多模态立场检测长期卡关**
多模态立场检测（MSD）是理解公共话语的核心任务，需同时融合文本与图像信号判断立场。但现有方法在上下文 grounding、跨模态解释歧义、单遍推理脆弱性上存在明显缺陷，尤其是图文信号冲突时，性能下滑严重。

🧪 **检索增强+多智能体协作的四阶段架构**
研究团队提出MM-StanceDet，一套整合检索增强与多智能体协作的新框架，核心设计包含四个模块：
1. 检索增强模块：解决上下文 grounding 问题，补充任务相关背景信息
2. 专门多模态分析智能体：负责细粒度的跨模态信号解释，减少歧义
3. 推理增强辩论阶段：多智能
