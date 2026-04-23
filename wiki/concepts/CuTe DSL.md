---
title: CuTe DSL
type: concept
tags:
- Coding Agent
- 开发工具
status: 审核中
confidence: medium
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/5f14f295adde41da85c823b09dbe8c51
notion_id: 5f14f295-adde-41da-85c8-23b09dbe8c51
---

## 定义

CuTe DSL 是文中用于 GPU 内核实现的高层抽象语言之一。它以更可组合的方式描述内核结构，用来检验多智能体系统能否在公开训练数据较少的 API 体系里，仅凭文档完成学习与优化。

## 关键要点

- 文章用它与接近底层的 CUDA C 加 inline PTX 形成对照，覆盖不同抽象层级

- 它的意义不只是“换一种语法”，而是测试 agent 是否能跨抽象层学习新工具

- 如果 agent 能在 CuTe DSL 里完成优化，说明其能力不局限于熟悉代码模式的复写

## 关联概念

- [Agent Harness](concepts/Agent Harness.md)

- [Cursor](entities/Cursor.md)

## 来源引用

- [原文链接](https://cursor.com/blog/multi-agent-kernels)｜《Speeding up GPU kernels by 38% with a multi-agent system》｜源文章：Cursor × NVIDIA：多智能体系统用 3 周把 CUDA kernel 加速了 38%
