---
title: 摘要：How I built harness for my agent using Claude Code leaks
type: summary
tags:
- Harness 工程
- 上下文管理
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: https://www.notion.so/348701074b688116b591f390ee17a5d1
notion_url: https://www.notion.so/Tizer/2edc95bc0f9142a5b2757c4fb1a6af72
notion_id: 2edc95bc-0f91-42a5-b275-7c4fb1a6af72
---

## 一句话摘要

这篇长文把 Claude Code 的公开源码拆成一套可复用的生产级 Agent 蓝图，核心观点是：真正决定 Agent 能否长期稳定工作的，不只是模型和提示词，而是 harness 与其背后的基础设施层。

## 关键洞察

- 作者把主流的“模型权重—上下文—harness”三层框架扩展为“四层”：模型权重、上下文、harness、基础设施，强调多租户、权限、隔离、状态持久化和分布式协调才是产品级 Agent 的生死线。

- Claude Code 的核心循环不是普通 while loop，而是可流式输出、可取消、可组合且自带背压能力的异步生成器；这让长时任务、UI 流式反馈与中途打断都成为一等公民。

- 工具执行的关键优化不只是“能调工具”，而是把工具按读写风险做并发分类，并在模型流式生成过程中提前启动工具，从而同时拿到速度和安全性。

- 长上下文管理并不依赖单一摘要，而是通过微压缩、截断压缩、自动总结、上下文折叠等分层策略，把成本控制、连续执行和高保真尾部上下文结合起来。

- 这套架构对 Tizer 的启发很直接：知识编译、OpenClaw 工作流、内容管线等系统若想从“能跑”进化到“可托管、可扩展、可并行”，需要把权限、隔离、记忆压缩和任务协调当成系统设计，而不是提示词补丁。

## 提取的概念

- [Harness Engineering](concepts/Harness Engineering.md)

- [异步生成器](concepts/异步生成器.md)

- [流式工具执行](concepts/流式工具执行.md)

- [工具并发分类](concepts/工具并发分类.md)

- [权限管线](concepts/权限管线.md)

- [Git Worktree](concepts/Git Worktree.md)

- [上下文压缩](concepts/上下文压缩.md)

## 原始文章信息

- 作者：@rohit4verse

- 来源：X书签

- 发布时间：2026-04-07

- 原文链接：[https://x.com/rohit4verse/status/2041548810804211936](https://x.com/rohit4verse/status/2041548810804211936)

- 源文章：从 Claude Code 源码泄露看：如何构建真正能抗住生产环境的 Agent Harness

## 个人评注

这篇文章的价值不在于“Claude Code 很强”，而在于它把 Coding Agent 从提示词工程拉回到了系统工程：循环、权限、压缩、隔离、重试、并行与扩展点，才是可复制的竞争力。对 Tizer 的知识 Wiki 与 Agent 体系来说，它适合作为一篇“Agent 基础设施方法论”母材料，后续可以持续吸收进 OpenClaw、编译器 Agent 与多 Agent 内容生产链路。
