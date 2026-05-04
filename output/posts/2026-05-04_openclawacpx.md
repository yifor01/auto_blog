---
title: "openclaw/acpx"
source: GitHub Trending
url: https://github.com/openclaw/acpx
score: 112
model: tencent/hy3-preview:free
generated_at: 2026-05-04T20:12:08.089758
---

📌 【openclaw 开源】acpx：Agent通讯结构化CLI工具

AI 编程Agent还在靠抓伪终端（PTY）的字符流通讯？
这种方式解析容错率低，无法支持多轮会话、并行任务等场景。
openclaw 新开源的 acpx 用结构化协议替代 PTY 抓取，直接解决这个痛点。

🤔 **PTY scraping 是Agent通讯的老大难问题**
当前AI agents、编排器（orchestrators）要与编程Agent（coding agents）通讯，主流方式是从伪终端（PTY）会话中抓取字符流。这种方式不仅解析麻烦、容错性低，还难以支持多轮对话、并行任务等复杂协调需求，连Agent本身都抵触这种通讯方式（项目描述提到「They hate having to scrape characters from a PTY session 😤」，而使用acpx的Agent则「love acpx! 🤖❤️」）。
acpx 的核心定位是 Agent Client Protocol（ACP）的 headless CLI 客户端，用结构化协议替代非结构化的 PTY 抓取，专门服务于 agent-to-agent 的命令行通讯场景。

🧪 **兼容多主流Agent的ACP统一客户端**
acpx 提供统一的命令界面，支持 Pi、OpenClaw ACP、Codex、Claude 以及所有ACP兼容的Agent，无需为不同Agent适配不同的通讯逻辑。
目前项目处于 Alpha 阶段，CLI 与运行时接口仍可能变动，基于 acpx 构建的下游项目在稳定前可能出现兼容性问题。ACP 协议的覆盖进度可参考官方发布的 ACP Spec Coverage Roadmap。

💡 **持久会话与队列机制解决协调痛点**
acpx 针对编程Agent工作流的协调需求，内置了多项实用特性：
- 持久会话：多轮对话可跨调用存活，按仓库（repo）维度划分作用域
- 命名会话：同一仓库内可运行并行工作流，通过 `-s backend`、`-s frontend` 等参数区分
- 提示排队：当前提示运行中可提交新提示，按提交顺序依次执行
- 协作取消：取消操作会发送 ACP session/cancel 指令，不会破坏现有会话状态
- 软关闭生命周期：关闭会话但不会删除磁盘上的历史记录
- 队列所有者TTL：通过 `--ttl` 参数可短暂保持队列所有者存活，等待后续提示
- 即发即忘：添加 `--no-wait` 参数可排队提示后立即返回，无需等待执行结果
- 优雅取消：按下 Ctrl+C 会先发送 ACP session/cancel 指令，再 fallback 到强制终止进程
- 会话控制：支持 `set-mode`、`set <key> <value>` 操作，对应 session/set_mode 与 session/set_config_option 功能
- 崩溃重连：检测到 Agent 进程异常死亡时，会自动重载会话恢复状态

⚠️ **Alpha阶段接口变动风险需注意**
acpx 目前仍处于 Alpha 开发阶段，CLI 命令与运行时接口大概率会发生变更，任何基于当前版本构建的下游应用都可能遇到兼容性问题，建议仅在测试环境使用，等待版本稳定后再投入生产。

🎯 **编程Agent工作流构建的落地工具**
对于正在搭建编程代理工作流程的工程师与研究者，acpx 提供了开箱即用的开源实现，直接解决多轮编程代理协调的实际痛点。项目已登上 GitHub Trending，社群关注度高，有Agent间通讯需求的开发者可以尝试适配。

🔗 **项目链接**
📝 项目名称：openclaw/acpx
👤 作者：openclaw
🔗 GitHub地址：https://github.com/openclaw/acpx
📌 备注：当前为Alpha版本，接口可能变动，下游项目请注意兼容性

你正在构建编程Agent相关的工作流吗？有没有遇到过Agent间通讯的痛点？欢迎在评论区分享你的经验👇

#AI #Agent #编程 #开源 #GitHub #ACP #openclaw #AI编程
