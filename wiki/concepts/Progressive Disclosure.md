---
title: Progressive Disclosure
type: concept
tags:
- Coding Agent
- 知识管理
status: 草稿
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/cb3919aad18b4688b0a4721087bb5496
notion_id: cb3919aa-d18b-4688-b0a4-721087bb5496
---

## 定义

Progressive Disclosure（渐进式披露）是一种上下文加载策略：先只向 Agent 暴露低成本的元数据或概要描述，只有在任务真正需要时，再按需加载完整说明、示例或更深层状态。

## 关键要点

- 它通过“先少后多”的信息分发方式，降低上下文窗口被一次性填满的风险。

- 与一股脑返回整套 schema、文档或配置相比，渐进式披露更适合 Agent 在多步骤任务中动态取用知识。

- 在 Skills 场景里，常见实现方式是先加载 name、description 等短元数据，命中任务后再展开完整技能内容。

- 它本质上是一种上下文压缩与按需展开机制，适合控制 Token 成本并减少无关干扰。

## 关联概念

- [Context Engineering](concepts/Context Engineering.md)

- [Agent Skills](concepts/Agent Skills.md)

## 来源引用

- [摘要：How to cut Claude Code costs by 3x (using Karpathy's context engineering principles)](summaries/摘要：How to cut Claude Code costs by 3x (using Karpathy's context engineering principles).md)（[原文](https://x.com/_avichawla/status/2046500537584218438)）

- [摘要：How to Give Claude Perfect Memory (complete guide)](summaries/摘要：How to Give Claude Perfect Memory (complete guide).md)（[原文](https://x.com/aiedge_/status/2046966170868486512)）
