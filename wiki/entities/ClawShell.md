---
title: ClawShell
type: entity
tags:
- OpenClaw
- Agent 安全
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/9120ca5814d74e288f4e034dc486e7d7
notion_id: 9120ca58-14d7-4e28-8f4e-034dc486e7d7
---

## 定义

ClawShell 是 OpenClaw 生态中的安全执行层，用于拦截包含敏感信息或高风险操作的命令，并配合显式审批机制降低高权限 Agent 的越权风险。

## 核心要点

- 在本文中，ClawShell 被描述为一个以 Rust 实现的第三方安全层，位于命令执行路径上。

- 它与 Red Lines、审批机制一起构成 OpenClaw 的安全护栏，特别适合本地高权限 Agent 场景。

- 其核心价值不在于提升模型能力，而在于把 Shell 执行、隐私保护和人工确认串成一条可审计的控制链。

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzE5ODM0MDIyNg%3D%3D&mid=2247484011&idx=1&sn=588c8c9f5f8a8e56cb1d32c5ba91947a&chksm=976d338b09e0fcd9565bdfc1728262bd18a93f1408aecb26a19ba94a31968423d172955f1a51#rd)｜[摘要：Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比](summaries/摘要：Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比.md)｜源文章：Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比

## 关联概念

- [OpenClaw](entities/OpenClaw.md)

- [Hermes Agent](entities/Hermes Agent.md)
