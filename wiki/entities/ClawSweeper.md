---
title: ClawSweeper
type: entity
tags:
- Harness 工程
- OpenClaw
status: 草稿
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f965334c2ac34981bddc8c98eb85c540
notion_id: f965334c-2ac3-4981-bddc-8c98eb85c540
---

## 定义

ClawSweeper 是 OpenClaw 官方的保守型维护机器人，通过并行运行 50 个 Codex 实例全天候扫描 GitHub Issues 和 PRs，自动提出关闭建议并执行清理。项目采用 Review-Apply 双车道架构，确保审核与执行分离。

**别名/关联**：openclaw/clawsweeper

## 档案信息

- **GitHub**：[https://github.com/openclaw/clawsweeper](https://github.com/openclaw/clawsweeper)

- **语言**：JavaScript

- **Stars**：1160+

- **License**：MIT

- **创建时间**：2026-04-23

- **作者**：Peter Steinberger (@steipete)

## 关键特点

- 并行运行 50 个 Codex 实例，24/7 全天候扫描

- 采用 Review-Apply 双车道架构：Review Lane 只提出建议，Apply Lane 才执行关闭

- 使用 gpt-5.5 模型，high reasoning，fast service tier

- 每个 Issue/PR 生成一份独立的 Markdown 报告（`items/<number>.md`）

- README 作为实时运营 Dashboard，自动更新状态

- 严格的 Guardrails：只在证据充分时才关闭（已实现、不可复现、重复、不可操作等）

- Maintainer 提交的 Issue 永远不会被自动关闭

- 单日关闭约 4000 个 Issues

## 架构

### Scheduler

- 热门/新 Issue 每小时检查，最新队列 5 分钟 intake

- 30 天内的 PR/Issue 每日检查

- 更老的 Issue 每周检查

- Apply 每 15 分钟唤醒

### Review Lane（提案层）

- Planner 扫描并分片

- 每个分片 checkout `main` 分支

- Codex 以 10 分钟超时审查每个 Item

- 高置信度的关闭建议标记为 `proposed_close`

### Apply Lane（执行层）

- 读取已有报告，仅在审查仍有效时执行

- 更新 Codex 自动评论

- 只关闭未变更的高置信度提案

- 已关闭/已重开的报告自动迁移归档

## 来源引用

- [摘要：Workflow status](summaries/摘要：Workflow status.md)（[原文](https://x.com/steipete/status/2047982647264059734)）

## 关联概念

- [Review-Apply 双车道架构](concepts/Review-Apply 双车道架构.md)

- [Codex](entities/Codex.md)

- [OpenClaw](entities/OpenClaw.md)
