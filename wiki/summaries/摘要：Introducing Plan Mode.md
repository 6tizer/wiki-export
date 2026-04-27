---
title: 摘要：Introducing Plan Mode.
type: summary
tags:
- AI 产品
- Harness 工程
status: 已审核
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b68814098dfe7c73bd34662
notion_url: https://www.notion.so/Tizer/d539696fc1d34271b1b89bb1af05ef66
notion_id: d539696f-c1d3-4271-b1b8-9bb1af05ef66
---

## 一句话摘要

Notion 推出 Plan Mode，Agent 在只读沙箱中展示执行计划，用户审核通过后才执行变更，实现原生 Human-in-the-Loop 工作流。

## 关键洞察

- **Plan → Approve → Execute 三步流程**：Agent 先生成计划、用户审批、最后执行，避免 Agent 直接修改内容带来的风险

- **只读沙箱预览**：Agent 在沙箱环境中「展示工作」，用户可以完整审查计划后再决定是否执行

- **信任构建机制**：社区反馈认为，明确的「不可编辑状态」比单纯的计划更重要——团队在看到清晰的审批边界后更愿意采纳 Agent 工作流

- **高风险场景优先**：Plan Mode 在涉及真实业务运营的自动化场景中价值最大；简单任务中可能引入不必要的摩擦

- **与 Claude Code Plan Mode 类似**：社区将其与 Claude Code 的 Plan Mode 类比，认为「先看计划再执行」是 Agentic AI 的通用最佳实践

## 提取的概念

- [Notion Plan Mode](entities/Notion Plan Mode.md)

- [Human-In-The-Loop](concepts/Human-In-The-Loop.md)

## 原始文章信息

- **作者**：@NotionHQ

- **来源**：X（Twitter）

- **发布时间**：2026-04-23

- **链接**：[原文推文](https://x.com/NotionHQ/status/2047420542454829117)

## 个人评注

Plan Mode 是 HITL 范式在笔记工具/AI 产品中的典型落地。对 Tizer 的 OpenClaw 和 Agent 工作流有直接参考价值——在 Agent 自动编译 Wiki、批量处理文章等场景中，可以借鉴 plan-then-approve 模式为高风险操作（如批量删除、跨库迁移）增加审批层。
