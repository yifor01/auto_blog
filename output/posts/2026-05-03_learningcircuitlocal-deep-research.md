---
title: "LearningCircuit/local-deep-research"
source: GitHub Trending
url: https://github.com/LearningCircuit/local-deep-research
score: 92
model: tencent/hy3-preview:free
generated_at: 2026-05-03T19:32:48.562435
---

📌 本地可控开源AI深度研究助理

登上GitHub Trending的AI研究助理，
所有流程本地运行，数据完全归你，
不用担心隐私外泄问题。

🤔 **本地运行+数据自主，主打隐私优先**
这是LearningCircuit开源的本地AI研究助理，主打agentic深度研究能力，可调用多个LLM与搜索引擎，生成带引用的研究结果。核心特点是所有流程本地运行，用户可自选LLM、自建可搜索知识库，完全拥有数据，且运行逻辑透明可查。

🧪 **完整Docker支持，CPU/GPU部署全覆盖**
项目提供完整的容器化部署方案：
- 手动Docker运行：依次启动Ollama（示例拉取gpt-oss:20b模型）、SearXNG搜索服务、Local Deep Research本体，映射对应端口即可
- Docker Compose快速启动：CPU版本支持所有平台，NVIDIA GPU版本仅支持Linux，启动后等待约30秒即可通过http://localhost:5000访问

💡 **整合现有工具，无核心算法创新**
需要明确的是，该项目并非底层技术突破，本质是对现有成熟工具的整合封装：底层依赖LLM提供推理能力、SearXNG负责搜索、agent框架实现研究流程编排，没有自研核心模型或新算法。

🔍 **隐私友好部署简单，适合注重隐私的开发者**
项目的核心价值在于落地性：完整的Docker方案大幅降低了部署门槛，本地运行、数据自主的特性，对重视隐私、不想将研究数据上传云端的工程师或研究者有较高实用价值。目前已有技术博主The Art Of The Terminal发布评测视频，可供参考。

⚠️ **无底层技术突破，定位实作向工具**
由于无核心技术创新，该项目不适合作为前沿技术追踪的案例，更适合需要本地AI研究工具的开发者参考实作，或作为个性化研究助理的搭建基础。

🎯 **注重隐私可尝试，按配置选择部署方案**
如果你需要本地运行的AI研究助理，可按照自身硬件配置选择部署方式：无GPU的设备选CPU版Docker Compose，Linux带NVIDIA显卡的可选GPU加速版。所有代码、部署配置均已开源。

🔗 **项目连结**
📝 项目名称：LearningCircuit/local-deep-research
👤 作者：LearningCircuit
🔗 GitHub地址：https://github.com/LearningCircuit/local-deep-research
📹 评测视频：The Art Of The Terminal

你有没有用过本地部署的AI工具？欢迎分享你的经验👇

#AI #开源工具 #本地部署 #GitHubTrending #研究助理 #隐私保护
