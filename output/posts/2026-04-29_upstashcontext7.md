---
title: "upstash/context7"
source: GitHub Trending
url: https://github.com/upstash/context7
score: 114
model: tencent/hy3-preview:free
generated_at: 2026-04-29T20:05:05.801202
---

📌 【upstash 开源】Context7 实时注入LLM最新代码文档

用 LLM 辅助编程最常见的痛点是什么？
AI 生成的代码示例基于 1 年前的训练数据，完全过时。
调用的 API 根本不存在，全是模型幻觉。

🤔 **LLM 编程通病：过时文档导致幻觉代码**
目前主流 LLM 依赖训练阶段的静态数据，无法同步获取第三方库的最新更新，辅助编程时普遍存在三类问题：代码示例基于 1 年前的训练数据已经过时，幻觉生成不存在的 API，给出的解答仅适配旧版本包，与当前开发场景完全不匹配。

🧪 **双模式适配，低门槛接入编码工具**
Context7 提供两种接入模式，无需复杂配置即可适配各类编码 agent 与辅助工具：
1. CLI + Skills 模式：安装专属 skill 引导 agent 通过 ctx7 命令行拉取文档，无需支持 MCP 协议
2. MCP 模式：注册 Context7 MCP Server，让 agent 原生调用文档查询工具
工程落地门槛极低，与当前 Agent 工具调用的发展趋势高度契合。

💡 **实时拉取版本专属文档，注入 LLM 提示**
Context7 直接从库的官方源地址拉取最新、版本对应的文档和代码示例，直接注入到用户输入的 LLM 提示中，彻底解决上述三类问题。
使用时只需在提示末尾加上「use context7」即可触发文档拉取，官方给出的参考示例包括：
- 编写 Next.js 中间件校验 JWT：「Create a Next.js middleware that checks for a valid JWT in cookies and redirects unauthenticated users to /login. use context7」
- 配置 Cloudflare Worker 缓存策略：「Configure a Cloudflare Worker script to cache JSON API responses for five minutes. use context7」
- 查询 Supabase 邮箱密码注册 API：「Show me the Supabase auth API for email/password sign-up. use context7」

🔍 **双模式覆盖不同开发需求**
两种模式的设计覆盖了不同开发者的使用场景：若使用轻量编码工具，选 CLI + Skills 模式无需适配 MCP 协议；若工具原生支持 MCP 协议，选 MCP 模式可获得更原生的调用体验。
整个流程无需切换标签页查阅文档，也不会出现 AI 生成过时代码或幻觉 API 的问题。

⚠️ **公开资讯未提及明确功能限制**
目前公开的 GitHub 项目资讯未提及具体功能限制，建议使用者根据自身使用的第三方库、编码工具场景测试适配性，也可关注 GitHub 社区的后续反馈与更新。

🎯 **三步接入，快速用上最新文档**
接入 Context
