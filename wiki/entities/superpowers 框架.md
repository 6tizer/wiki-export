---
title: superpowers 框架
type: entity
tags:
- Agent 框架
- Agent 技能
- Coding Agent
- 工作流
status: 审核中
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/3dc1f1f67b884a08b4b76283952f086c
notion_id: 3dc1f1f6-7b88-4a08-b4b7-6283952f086c
---

## 定义

superpowers 是由 Jesse Vincent（obra）主导开发的**代理技能框架（Agentic Skills Framework）**，专为 Claude Code、Cursor、Codex、OpenCode 等 AI 编码代理设计，通过一系列可组合的 Markdown 格式「技能」文件，强制 AI 代理在每次操作前先检查并遵循工程规范。

GitHub：[https://github.com/obra/superpowers](https://github.com/obra/superpowers)

## 核心哲学

- **TDD 永不妥协**：先写失败的测试（RED），再写最小实现（GREEN），最后重构（REFACTOR）

- **系统化优先于随意性**：遵循严谨流程，而非依靠猜测和「感觉」

- **证据优先**：所有「已修复」「已完成」的声明，必须附上测试通过的实际证据

## 核心工作流：Brainstorm → Plan → Implement

1. **Brainstorming**：AI 发起苏格拉底式追问，形成架构文档存入 `/docs/plans/`，等待批准

1. **Writing-plans**：批准后开启新 git worktree 分支，拆分 8-12 个微观任务

1. **Subagent-Driven Execution**：每个微任务由新鲜子代理承接，严格遵循 TDD → Spec 审查 → Code Review → 自动进入下一微任务

## 项目数据

- GitHub Stars：128,000+（截至 2026 年初）

- License：MIT

- 作者：Jesse Vincent（Keyboardio 联合创始人、RT 创建者、K-9 Mail 创建者、Perl 项目负责人）

## 安装注意（重要！）

- 正确：`/plugin marketplace add obra/superpowers-marketplace` + `/plugin install superpowers@superpowers-marketplace`

- 错误：`npx skills add https://github.com/obra/superpowers.git`（会导致关键 hook 丢失）

- 需确保网络能访问 `github.com:443`，否则 slash commands 全部失败

## 已知问题

- 权限提示过于频繁，需要 auto-approve 模式才比较流畅

- 长任务可见性差，中途只能靠观察 git worktree 的 commit 了解进度

## 来源引用

- [摘要：Superpowers：给你的 AI 编码代理装上一套严格的开发方法论](summaries/摘要：Superpowers：给你的 AI 编码代理装上一套严格的开发方法论.md)

- [摘要：Claude Superpowers：开发者的纪律框架，营销人的效率利器](summaries/摘要：Claude Superpowers：开发者的纪律框架，营销人的效率利器.md)

- [原文链接](https://x.com/shannholmberg/status/2032892199751528486)｜《Claude Superpowers：开发者的纪律框架，营销人的效率利器》｜来源条目：[摘要：Claude Superpowers：开发者的纪律框架，营销人的效率利器](summaries/摘要：Claude Superpowers：开发者的纪律框架，营销人的效率利器.md)

- [原文链接](https://x.com/BTCqzy1/status/2033116943712993717)｜《SuperPowers：给 AI 编程装上七阶段软件工程流水线》｜来源条目：[摘要：SuperPowers：给 AI 编程装上七阶段软件工程流水线](summaries/摘要：SuperPowers：给 AI 编程装上七阶段软件工程流水线.md)

- [原文链接](https://x.com/vikingmute/status/2036043855594975485)｜《Superpowers：给你的 AI 编码代理装上一套严格的开发方法论》｜来源条目：[摘要：Superpowers：给你的 AI 编码代理装上一套严格的开发方法论](summaries/摘要：Superpowers：给你的 AI 编码代理装上一套严格的开发方法论.md)

- [摘要：superpowers is still the simplest way to level up any project you're running in Claude](summaries/摘要：superpowers is still the simplest way to level up any project you're running in Claude.md)（[原文](https://x.com/shannholmberg/status/2047722364415459463)）

- [摘要：GPT5.5 + Codex 如何跑一整夜，编程的下一步，不是辅助编程，是可托管执行单元](summaries/摘要：GPT5.5 + Codex 如何跑一整夜，编程的下一步，不是辅助编程，是可托管执行单元.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkyMzY1NTM0Mw%3D%3D&mid=2247515158&idx=1&sn=a656396814f65b8053981d852d11bb54&chksm=c0ba44de9a9054cf724edaed2a5cda4d44ea80568c1c43a3b3d2de3699534f4295bfaf69ba91#rd)）

## 关联概念

- [Git Worktree](concepts/Git Worktree.md)

- [测试驱动开发](concepts/测试驱动开发.md)

- [Claude Code](entities/Claude Code.md)
