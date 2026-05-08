---
title: "OpenAI Releases Three Realtime Audio Models: GPT-Realtime-2, GPT-Realtime-Translate, and GPT-Realtime-Whisper in the Realtime API"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/08/openai-releases-three-realtime-audio-models-gpt-realtime-2-gpt-realtime-translate-and-gpt-realtime-whisper-in-the-realtime-api/
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-08T20:27:12.215710
---

📌 【OpenAI 发布三款实时音频模型】

你以为实时语音AI的核心瓶颈是识别准确率？实际上，部署中最常收到的用户投诉是「突然不说话」和「聊半小时就忘事」。

🤔 **实时语音API正式GA，生产部署门槛消失**
OpenAI近日通过Realtime API发布三款全新音频模型，同时宣布Realtime API结束测试版，正式进入通用可用（GA）阶段。此前不少开发者因API处于测试阶段，迟迟未将其用于生产系统，此次GA是重要的生产级落地信号。这三款模型覆盖实时语音应用的完整链路，推动语音应用从基础问答，升级为可监听、推理、翻译、转录、执行操作的全流程对话系统。

🧪 **三款模型各司其职，覆盖推理、翻译、转录场景**
三款模型分别对应不同的实时语音能力：
- GPT-Realtime-2：旗舰款，面向具备推理能力的语音代理，是OpenAI首款达到GPT-5级推理能力的语音模型
- GPT-Realtime-Translate：专注实时语音翻译场景
- GPT-Realtime-Whisper：负责流式转录任务
所有模型已通过OpenAI API即时上线，开发者可在Playground直接测试。

💡 **旗舰模型上下文扩至128k，支持GPT-5级推理**
本次发布的核心亮点是旗舰模型GPT-Realtime-2的能力升级：
- 推理能力：首次搭载GPT-5级推理，可处理更复杂的请求，支持自然中断与对话延续
- 上下文窗口：从过往的32k token扩展至128k token，支持更长会话与复杂任务，避免长对话丢上下文的问题
- 多工具调用：可同时调用多个工具，执行过程中实时播报进展，避免用户等待时的死寂感
- 可调推理强度：提供5档推理强度调节，包含minimal、low、medium等级别，方便开发者按场景调优
- 前置语功能：可启用「让我查一下」「稍等我确认」等短提示语，让用户明确感知代理正在处理请求

🔍 **可调推理+实时播报，解决语音代理核心痛点**
过往的语音模型常出现多步请求卡顿、长会话丢失上下文、处理请求时无反馈的死寂等问题，导致用户体验极差。GPT-Realtime-2的升级直接针对这些落地痛点：128k上下文解决长会话记忆问题，实时播报进展加前置语功能消除等待时的死寂感，可调推理强度让开发者在性能与成本间灵活平衡。
根据本次发布的评价，这些生产级能力直接解决了语音代理的延迟与静默问题，对构建实时对话系统的工程师而言是值得关注的更新。虽然实时语音模型的核心概念并非全新，但具体的功能落地与GA的API，让实时语音应用的规模化部署成为可能。

⚠️ **实时语音模型概念非全新，属能力迭代**
根据公开评价，本次发布的核心概念并非行业首创，属于现有实时语音模型方向的能力升级，其生产级API与具体功能优化是主要价值点。

🎯 **生产环境可放心接入，Playground即刻测试**
对于开发者而言，本次更新的直接行动建议非常明确：
1. 此前因Realtime API处于测试版而观望的团队，现在可启动生产级系统的构建
2. 三款模型已全量上线，可直接在OpenAI Playground测试效果
3. 构建语音代理时，可优先启用GPT-Realtime-2的实时播报与前置语功能，避免用户等待时的不良体验
4. 按需调整推理强度，在响应速度与处理能力间找到平衡

🔗 **相關連結**
📝 报道标题：OpenAI Releases Three Realtime Audio Models: GPT-Realtime-2, GPT-Realtime-Translate, and GPT-Realtime-Whisper in the Realtime API
👤 来源：Asif Razzaq @ MarkTechPost
🔗 链接：https://www.marktechpost.com/2026/05/08/openai-releases-three-realtime-audio-models-gpt-realtime-2-gpt-realtime-translate-and-gpt-realtime-whisper-in-the-realtime-api/

你最近在构建实时语音应用吗？最期待哪款模型的能力？歡迎留言分享👇

#OpenAI #实时语音 #AI #语音代理 #API #GPT #技术更新 #MarkTechPost
