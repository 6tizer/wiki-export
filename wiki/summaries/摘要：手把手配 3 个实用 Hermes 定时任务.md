---
title: 摘要：手把手配 3 个实用 Hermes 定时任务
type: summary
tags:
- 内容自动化
- CLI 工具
status: 已审核
confidence: medium
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: https://www.notion.so/354701074b6881bdbb29f706c90691d6
notion_url: https://www.notion.so/Tizer/f6d35b1137f24762be322a9de20375cf
notion_id: f6d35b11-37f2-4762-be32-2a9de20375cf
---

## 一句话摘要

手把手演示在 Hermes Agent 中配置三个 Cron 定时任务（每日 GitHub Issue 整理、每周周报生成、定时服务状态检查），让 Agent 从被动应答转为主动执行。

## 关键洞察

- **Cron 三件套**：每日 Issue 整理（`0 9 * * *`）、每周五周报生成（`0 17 * * 5`）、每 30 分钟服务健康检查（`*/30 * * * *`），覆盖了日常运维自动化的核心场景

- **Prompt 自包含原则**：定时任务无对话上下文，所有信息（仓库地址、检查规则、输出格式、通知渠道）必须写入 Prompt 本身；建议先在普通对话中测试 Prompt 再放入 Cron

- **静默告警模式**：监控任务应正常时静默、异常时才通知，避免通知疲劳导致用户关闭告警

- **自然语言创建**：除命令行 `hermes cron create` 外，也可在对话中直接用自然语言描述定时任务，Hermes 自动解析为 Cron Job

- **Gateway 依赖**：Cron 任务依赖 Hermes Gateway 调度，Gateway 停止则任务不触发，需用 systemd 等保证常驻

## 提取的概念

- [Hermes Agent](entities/Hermes Agent.md)

- [Cron 自动化](concepts/Cron 自动化.md)

- [自然语言定时任务](concepts/自然语言定时任务.md)

- [Prompt 自包含原则](concepts/Prompt 自包含原则.md)

## 原始文章信息

- **作者**：AI赋能说

- **来源**：微信公众号

- **发布时间**：2026-05-02

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=MzI3NjE4OTAyMg%3D%3D&mid=2247488709&idx=1&sn=e97ce62f2ff99e390c8fe93ad45c9413&chksm=ea0a5ab955dc7bb8b88b30460b5318465cae31892d997d3ffd88defb44bcd9dbdcc620ef7241#rd)

## 个人评注

本文是 Hermes Agent Cron 功能的实操教程，对 Tizer 的内容自动化流水线有直接参考价值：文中的 GitHub Issue 整理和周报生成模式可类比到 OpenClaw 的定时编译/巡检场景；Prompt 自包含原则是所有无状态自动化任务的通用设计准则，与 Wiki Compiler 的触发逻辑设计理念一致。
