---
title: Parity Harness
type: concept
tags:
- Agent 编排
- Coding Agent
status: 审核中
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/e8fa17c9be064c5e807b84d288fd447c
notion_id: e8fa17c9-be06-4c5e-807b-84d288fd447c
---

## 定义

Parity Harness 是一种在系统重写或跨语言迁移过程中，用行为一致性来约束新旧实现的验证机制，核心目标不是复刻源码，而是确保用户可感知的工作流与执行结果保持一致。

## 关键要点

- 适用于 TypeScript → Python → Rust 这类多阶段重写与迁移

- 通过文件映射、目录映射与统一测试场景校验行为对齐

- 关注命令系统、工具调用、查询引擎等高组合复杂度模块

- 是让大规模重写可以持续推进而不破坏既有体验的工程护栏

## 关联概念

- [Agent Harness](concepts/Agent Harness.md)

- [净室重写](concepts/净室重写.md)

- [Claw Code](entities/Claw Code.md)

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493153&idx=1&sn=72c2e68a8f7d0643e26798536ebdcddf&chksm=c0f2fc5aeb871deb50d997025e1dec3f07677e1f3f1fa9185c61aca0e43ef4093d44ff6ec270#rd)｜《用 Rust 重写的 Claw Code ,已经178K Star !有些东西看了后，睡不着觉》｜源文章：用 Rust 重写的 Claw Code ,已经178K Star !有些东西看了后，睡不着觉
