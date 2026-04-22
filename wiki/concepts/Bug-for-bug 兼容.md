---
title: Bug-for-bug 兼容
type: concept
tags:
- Coding Agent
- 开发工具
status: 草稿
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/c4b8057b8fbf45b5a12d4ca9637732f3
notion_id: c4b8057b-8fbf-45b5-a12d-4ca9637732f3
---

## 定义

Bug-for-bug 兼容是一种迁移与重写策略，要求新实现不仅复现旧系统的正常行为，也刻意保留旧实现中会影响用户工作流的既有瑕疵，从而避免兼容性在“修 bug”的名义下被悄悄打破。

## 关键要点

- 优先保证行为稳定，而不是立刻追求实现层面的完美

- 特别适合命令行工具、Agent 工作流与复杂工具链迁移

- 可以降低重写阶段对用户脚本、习惯与自动化流程的破坏

- 往往与回归测试、行为快照和 Parity Harness 搭配使用

## 关联概念

- [净室重写](concepts/净室重写.md)

- [Agent Harness](concepts/Agent Harness.md)

- [Claw Code](entities/Claw Code.md)

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493153&idx=1&sn=72c2e68a8f7d0643e26798536ebdcddf&chksm=c0f2fc5aeb871deb50d997025e1dec3f07677e1f3f1fa9185c61aca0e43ef4093d44ff6ec270#rd)｜《用 Rust 重写的 Claw Code ,已经178K Star !有些东西看了后，睡不着觉》｜源文章：用 Rust 重写的 Claw Code ,已经178K Star !有些东西看了后，睡不着觉
