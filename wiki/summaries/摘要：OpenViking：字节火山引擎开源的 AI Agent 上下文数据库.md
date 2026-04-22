---
title: 摘要：OpenViking：字节火山引擎开源的 AI Agent 上下文数据库
type: summary
tags:
- 记忆系统
- 知识管理
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, OpenClaw, 自动化
source_article_url: https://www.notion.so/335701074b688195a10ef8016f6e7dbf
notion_url: https://www.notion.so/cdbdef8811344156a5f38ef79a0960e7
notion_id: cdbdef88-1134-4156-a5f3-8ef79a0960e7
---

## 一句话摘要

OpenViking 用文件系统范式重构 Agent 记忆管理，把“记忆怎么存、怎么找、怎么按需加载”一起变成可观测、可分层的上下文工程系统。

## 关键洞察

- viking:// 把资源、技能和记忆统一成层级目录，替代扁平向量检索。

- L0/L1/L2 分层加载让 Agent 可以先看摘要、再看概览、最后按需读全文。

- 文章最重要的信息不是 Star 数，而是它把上下文管理从“黑盒召回”推进到“可调度结构”。

- 这条路线尤其适合长程任务、多知识源和长期运行的 Agent。

## 提取的概念

- [OpenViking](entities/OpenViking.md)

- [Agent 上下文数据库](concepts/Agent 上下文数据库.md)

- [viking://](concepts/viking---.md)

- [L0/L1/L2 分层加载](concepts/L0-L1-L2 分层加载.md)

## 原始文章信息

- 作者：berryxia（[Berryxia.AI](http://berryxia.ai/)）

- 来源：X书签

- 发布时间：未注明

- 链接：[原文](https://x.com/berryxia/status/2032838544688034081)

## 个人评注

这和 Tizer 的 Wiki 编译工作高度相关。真正可扩展的知识系统，不只是能搜到内容，而是能控制加载粒度、引用路径和上下文成本。
