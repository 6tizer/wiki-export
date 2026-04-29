---
title: dbskill
type: entity
tags:
- 商业/生态
- 提示工程
- CLI 工具
status: 草稿
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e504dee7cd3640d9bd113e3458a7094f
notion_id: e504dee7-cd36-40d9-bd11-3e3458a7094f
---

## 定义

dbskill（简称 dbs）是 @dontbesilent 基于 gstack 的方法论跨领域迁移而创建的 Claude Code 商业诊断工具箱。它将 gstack 的「多角色工程团队」范式迁移到商业诊断领域，用 80 行纯对话式配置替代了 gstack 的 150+ 行 bash 工程化体系。

别名：dbs、dontbesilent 商业工具箱

## 核心要点

- 入口 skill `/dbs` 只做路由，不做诊断——搞清楚用户需求后分发到正确的专业 skill

- `/dbs-diagnosis` 对应 gstack 的 `/office-hours`，采用「消解漏斗」先瓦解问题再路由

- 极简技术栈：无 bash、无外部依赖、无状态管理，纯 Markdown 对话指令

- 包含多种专业诊断 skill：`/dbs-benchmark`（对标分析）、`/dbs-content`（内容诊断）、`/dbs-hook`（钩子诊断）、`/dbs-xhs-title`（小红书标题）等

- `/dbs-chatroom` 实现多专家并行讨论（芒格、卡尼曼、达里奥等视角）

- `/dbs-agent-migration` 体现自我迭代能力——用自身方法论整理自身 Agent 工作台

## 关联概念

- [gstack](entities/gstack.md)

- [方法论跨领域迁移](concepts/方法论跨领域迁移.md)

- [角色化召唤范式](concepts/角色化召唤范式.md)

- [消解漏斗](concepts/消解漏斗.md)

## 来源引用

- [摘要：我花 3 天逆向 gstack to dbs，发现方法论比代码更值钱](summaries/摘要：我花 3 天逆向 gstack to dbs，发现方法论比代码更值钱.md)（[原文](https://x.com/longdechen12/status/2049161112273539088)）
