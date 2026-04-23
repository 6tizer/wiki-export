---
title: AGENTS.md
type: concept
tags:
- Agent 编排
- 知识管理
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/5da673ca2377484498ec12f5679bfbf3
notion_id: 5da673ca-2377-4844-98ec-12f5679bfbf3
---

**定义**：[AGENTS.md](http://agents.md/) 是 Codex CLI 的行为策略配置文件，需要**手动维护**（非自动生成），类似为 AI Agent 设定行事准则的策略文件。

**设计原则**

- 内容应聚焦于策略、优先级、约束三个维度，而非逐步操作指南

- 遵循"最小干预"原则：从默认配置开始，仅在反复出现同类问题时才添加定向规则

- 过度定制会引入不可预期的副作用

**配置注意事项**

- 绝不在配置中硬编码密钥

- 必须为破坏性操作（删除文件、重写模块）设置明确的升级确认规则

- 任何自动化脚本应在 README 和 PR 中记录来源、触发时机和入口点

**相关工具**

- Codex CLI：使用 [AGENTS.md](http://agents.md/) 的主要工具

- [CLAUDE.md](http://claude.md/)：Claude Code 中类似的配置文件

**来源引用**

- [摘要：「不就是几个 Markdown 文件」：一场关于 Agentic 工程本质的争论](summaries/摘要：「不就是几个 Markdown 文件」：一场关于 Agentic 工程本质的争论.md)（[原文](https://x.com/garrytan/status/2045371983312097409)）

- [摘要：OpenAI Codex CLI 实用最佳实践](summaries/摘要：OpenAI Codex CLI 实用最佳实践.md)

- [摘要：OpenClaw Orchestrator 模式：一条提示词让智能体效率提升 10 倍？](summaries/摘要：OpenClaw Orchestrator 模式：一条提示词让智能体效率提升 10 倍？.md) — 用 [AGENTS.md](http://agents.md/) 与 [SOUL.md](http://soul.md/) 的职责差异讨论调度规则应放在哪里

- [摘要：agency-agents：一个开源的 AI 虚拟团队，144 个专业 Agent 覆盖 12 个职能部门](summaries/摘要：agency-agents：一个开源的 AI 虚拟团队，144 个专业 Agent 覆盖 12 个职能部门.md) — 展示 [AGENTS.md](http://agents.md/) 一类角色规范文件在多工具 Agent 生态中的复用价值

- [摘要：OpenClaw 养虾踩坑实录：如何用 CDP 把浏览器完全交给 AI Agent 控制](summaries/摘要：OpenClaw 养虾踩坑实录：如何用 CDP 把浏览器完全交给 AI Agent 控制.md) — 补充把浏览器配置、Profile 与登录流程沉淀进 [AGENTS.md](http://agents.md/) 的实战做法

- [原文链接](https://x.com/chenchengpro/status/2031347640630165525)｜《OpenAI 用 Codex 维护 Agents SDK 的四层架构：把工程规范变成 Agent 的行为约束》｜来源条目：OpenAI 用 Codex 维护 Agents SDK 的四层架构：把工程规范变成 Agent 的行为约束

- [摘要：OpenClaw 的「睡醒失忆」问题：用 MEMORY.md 和 AGENTS.md 让龙虾记住你](summaries/摘要：OpenClaw 的「睡醒失忆」问题：用 MEMORY.md 和 AGENTS.md 让龙虾记住你.md)

- [摘要：多Agent团队协作才是Hermes Agent的正确打开方式。](summaries/摘要：多Agent团队协作才是Hermes Agent的正确打开方式。.md)

- [摘要：Hermes Agent 从中级到高级进阶指南](summaries/摘要：Hermes Agent 从中级到高级进阶指南.md)

- [原文链接](https://x.com/LufzzLiz/status/2044258384556556743)｜《抽丝剥茧：深度解析 Hermes Agent 万字系统提示词（System Prompt）构成》｜来源条目：[摘要：抽丝剥茧：深度解析 Hermes Agent 万字系统提示词（System Prompt）构成](summaries/摘要：抽丝剥茧：深度解析 Hermes Agent 万字系统提示词（System Prompt）构成.md)

- [原文链接](https://x.com/nyk_builderz/status/2044472463279710344)｜《The Ultimate Hermes Guide - from one agent to a 4-profile team that still feels coherent on day 30》｜来源条目：[摘要：The Ultimate Hermes Guide - from one agent to a 4-profile team that still feels coherent on day 30](summaries/摘要：The Ultimate Hermes Guide - from one agent to a 4-profile team that still feels coherent on day 30.md)

- 《OpenClaw 核心文档架构详尽分析与优化方案指南》｜X书签文章｜源文章：OpenClaw：用 Markdown 文件定义 AI Agent 大脑的「文件即代理」框架深度解析

- 源文章：Hermes Agent 核心文档优化指南：让你的 AI 助手真正「越用越聪明」｜来源条目：[摘要：Hermes 核心文档架构详尽分析与优化方案指南](summaries/摘要：Hermes 核心文档架构详尽分析与优化方案指南.md)

- [摘要：Hermes 多 Agent 深水区：三个高级实战技巧](summaries/摘要：Hermes 多 Agent 深水区：三个高级实战技巧.md)（[原文](https://x.com/BTCqzy1/status/2045720855137903046)）

- [摘要：ziggy-llm](summaries/摘要：ziggy-llm.md)（[原文](https://x.com/zxytim/status/2046255419178500408)）

- [摘要：markdown knowledge bases](summaries/摘要：markdown knowledge bases.md)（[原文](https://x.com/lucaronin/status/2046877445748322418)）

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [多 Agent 协作工作流](concepts/多 Agent 协作工作流.md)

- [SOUL.md](concepts/SOUL.md.md)

- [Agent-Managed Skills](concepts/Agent-Managed Skills.md)

- [MEMORY.md](concepts/MEMORY.md.md)

- [ModelBox](entities/ModelBox.md)

- [Memory KPI](concepts/Memory KPI.md)

- [Policy Gate](concepts/Policy Gate.md)

- [team-agents.md](concepts/team-agents.md.md)

- [STYLE.md](concepts/STYLE.md.md)

- [EVOLUTION.md](concepts/EVOLUTION.md.md)

- [TOOLS.md](concepts/TOOLS.md.md)

- [受控自进化](concepts/受控自进化.md)

- [USER.md](concepts/USER.md.md)

- [SKILL.md](concepts/SKILL.md.md)

- [Subdirectory Hints](concepts/Subdirectory Hints.md)

- [Tolaria](entities/Tolaria.md)

- [YAML frontmatter](concepts/YAML frontmatter.md)

- [Architecture Decision Records](concepts/Architecture Decision Records.md)
