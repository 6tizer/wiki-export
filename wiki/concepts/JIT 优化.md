---
title: JIT 优化
type: concept
tags:
- 推理优化
status: 草稿
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1fc7cfc4a3b04cbfa808e7d65c0c5b80
notion_id: 1fc7cfc4-a3b0-4cbf-a808-e7d65c0c5b80
---

## 定义

JIT 优化（Just-in-Time Optimization）指在 Skill 实际运行过程中，根据失败日志、重复模式与资源状态，对执行策略进行动态优化与重编译。

## 关键要点

- 它处理的是静态编译阶段难以提前预见的运行时问题。

- 在 SkVM 中，JIT 包括自适应重编译、代码固化验证与资源感知调度等机制。

- 目标是减少重试、回避系统性失败，并让 Skill 随真实任务反馈持续进化。

## 来源引用

- [摘要：SkVM：优化你的Skills能够跨模型、跨Harness、跨环境稳定运行 ｜SJTU最新](summaries/摘要：SkVM：优化你的Skills能够跨模型、跨Harness、跨环境稳定运行 ｜SJTU最新.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg4MzYxODkzMg%3D%3D&mid=2247508119&idx=1&sn=8576b881967cee0b33dc2c424c9853a5&chksm=ce7a42ad8a773a9cdc3297389c1915b62ee8ee06d86ae09cbf47c11c9141230f4f6a7f8916f7#rd)）
