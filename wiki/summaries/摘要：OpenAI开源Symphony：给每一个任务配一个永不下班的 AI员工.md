---
title: 摘要：OpenAI开源Symphony：给每一个任务配一个永不下班的 AI员工
type: summary
tags:
- Harness 工程
- Agent 协作模式
- 代码生成
status: 已审核
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: https://www.notion.so/352701074b688144930df341e42e8c1d
notion_url: https://www.notion.so/Tizer/16eb061b9b8349629c0ebabfc8f5e738
notion_id: 16eb061b-9b83-4962-9c0e-babfc8f5e738
---

**一句话摘要**：Symphony 是 OpenAI 开源的 AI 编程任务编排系统，将项目管理看板（Linear）变成 AI 编码代理的控制中枢，让工程师从「监督 Agent」转向「管理任务」，部分团队三周内 PR 合并量增长 500%。

**关键洞察**

- Symphony 的核心洞察：AI 编程的瓶颈不是代码生成速度，而是人类的注意力和上下文切换成本；解法是把编排层从「管理 Agent 会话」上移到「管理任务看板」

- 使用 Linear 状态机驱动工作流（Todo → In Progress → Human Review → Done），人类只在 Human Review 节点介入

- Agent 能自主创建子任务、识别依赖关系（DAG），支持大粒度任务（如先迁移 Webpack→Vite 再升级 React）

- 架构核心是一份 [SPEC.md](http://spec.md/) 规范文档，官方用 Elixir 实现但已被社区用 Go/Rust/TypeScript/Python 等多语言复现，验证了「规范驱动开发」的可行性

- Codex App Server 模式（JSON-RPC 无头模式）是底层执行引擎，通过动态工具调用封装外部 API 而不暴露凭证

- 工作流显式化：将团队隐性工程规范写入 [WORKFLOW.md](http://workflow.md/)，支持热重载，让 AI 遵循人类工程流程

**提取的概念**

- [Symphony](entities/Symphony.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Codex](entities/Codex.md)

- [Codex App Server](concepts/Codex App Server.md)

- [规范驱动开发 SDD](concepts/规范驱动开发 SDD.md)

- [任务 DAG 调度](concepts/任务 DAG 调度.md)

**原始文章信息**

- 作者：@vista8（向阳乔木）｜ 来源：X书签 ｜ 发布时间：2026-04-29

- 链接：[https://x.com/vista8/status/2049484504444834126](https://x.com/vista8/status/2049484504444834126)

- GitHub 仓库：[openai/symphony](https://github.com/openai/symphony)（19,640 ⭐，Apache-2.0，Elixir）

- 官方博文：[https://openai.com/index/open-source-codex-orchestration-symphony/](https://openai.com/index/open-source-codex-orchestration-symphony/)

**个人评注**

Symphony 的「管理任务而非管理 Agent」理念与 Tizer 的 HITL 工作流高度一致。Proof of Work 机制（CI 结果 + PR review + 复杂度分析 + 演示视频）为异步审批提供了具体依据。[WORKFLOW.md](http://workflow.md/) 热重载的设计可借鉴到 OpenClaw 的 skill 配置更新流程中。值得关注的是 Symphony 不打算做成产品，而是定位为协议/规范——这种「[SPEC.md](http://spec.md/) + 让 AI 实现」的模式可能成为 Agent 基础设施的新分发方式。
