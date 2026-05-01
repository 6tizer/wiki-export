---
title: 摘要：Vibe Coding规范工作流
type: summary
tags:
- 加密资产
- 代码生成
- 提示工程
status: 已审核
confidence: high
last_compiled: '2026-04-26'
source_tags: NewStuff
source_article_url: ''
notion_url: https://www.notion.so/Tizer/7f5e71a97f1d4a8f928081bd676742c3
notion_id: 7f5e71a9-7f1d-4a8f-9280-81bd676742c3
---

## 一句话摘要

清华大学团队总结了氛围编程（Vibe Coding）的五阶段规范工作流，强调 AI 是执行者、人是决策者的协作原则。

## 关键洞察

- **五阶段循环**：需求描述 → 架构设计 → 代码生成 → 调试优化 → 持续迭代，不是直线而是持续运转的循环

- **需求描述三步走**：模糊需求澄清 → 技术选型 → 结构化确认，防止「假结构化」

- **逐模块生成**：代码生成不应一次性丢给 AI，而是每次只生成一个模块，确保上下文精准

- **三轮规则**：同一问题与 AI 讨论超过 3 轮未解决，立刻开新对话重头描述

- **阶段产物留存**：需求文档、架构图、调试日志是资产，下次迭代直接复用

## 提取的概念

- Vibe Coding

- 结构化需求描述

- 逐模块代码生成

## 原始文章信息

- **作者**：清新研究（清华大学沈阳教授团队）

- **来源**：微信公众号

- **发布时间**：2026-02-27

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=MzkyMDU4ODUwMw%3D%3D&mid=2247490779&idx=1&sn=7e9c3a5736a6de3279614468ce51612d)

## 个人评注

这套工作流对 Tizer 使用 Cursor/Claude Code 的日常开发非常实用。核心原则「AI 是执行者、你是决策者」与 HITL 理念完全一致。三轮规则和阶段产物留存可以直接应用到 OpenClaw 的 Skill 开发中。
