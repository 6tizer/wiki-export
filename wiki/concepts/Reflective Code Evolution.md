---
title: Reflective Code Evolution
type: concept
tags:
- Agent 编排
- Coding Agent
status: 草稿
confidence: high
last_compiled: '2026-04-25'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/fb3b304543784fa49f5dbae06a33545d
notion_id: fb3b3045-4378-4fa4-9f5d-bae06a33545d
---

## 定义

Reflective Code Evolution 是一种让模型基于执行轨迹、失败案例和评估结果反思现有程序，再生成代码补丁并持续改进系统行为的迭代优化机制。

## 关键要点

- 先执行与评估，再根据失败原因生成补丁

- 强调反思、变异、验证和自动修复的闭环

- 适合用于优化 Agent 的记忆程序、约束器与工具链逻辑

- 是自进化 Harness 的关键实现方式之一

## 来源引用

- [摘要：分享2篇最新Harness论文，一篇谷歌，一篇微软](summaries/摘要：分享2篇最新Harness论文，一篇谷歌，一篇微软.md)

## 关联概念

- [Harness Engineering](concepts/Harness Engineering.md)
