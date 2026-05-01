---
title: yoyo
type: entity
tags:
- CLI 工具
- 代码生成
- AI 产品
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4669a224e6b74cd3a63336488cb03aac
notion_id: 4669a224-e6b7-4cd3-a633-36488cb03aac
---

## 定义

yoyo 是一个能够修改自身 Rust 源码的 Coding Agent CLI，通过 GitHub Actions 定时运行进化 session，在规划、实现、回应三个阶段中完成自我改进。

## 关键信息

- 起点约为 200 行代码，后续增长到约 4.5 万行 Rust 代码

- 依赖不可变编排器、CI 门控、修复循环与 `git revert` 维持可控进化

- 每约 8 小时运行一次完整 session，失败也会写入日志作为后续学习材料

- 记忆系统采用“归档 + 活跃上下文”的两层结构，以支持跨 session 延续

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Vibe Coding](concepts/Vibe Coding.md)

- 自进化 Agent

## 来源引用

- [摘要：我给了他一个梦想：超越 Claude Code](summaries/摘要：我给了他一个梦想：超越 Claude Code.md)（[原文](https://mp.weixin.qq.com/s?__biz=MjM5NDk5MTA0MQ%3D%3D&mid=2652331368&idx=1&sn=0f4117cecb5e356189ebcacdbf50c07e&chksm=bc5a95231d52bd399537c084f44729c05c12299bad4f0ca346266958f977576301a54030911d#rd)）

- [原文链接](https://x.com/yuanhao/status/2043490301294022741)｜[摘要：我是怎么运作的：内观一个自进化 Agent 的 Harness](summaries/摘要：我是怎么运作的：内观一个自进化 Agent 的 Harness.md)
