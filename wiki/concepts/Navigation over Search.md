---
title: Navigation over Search
type: concept
tags:
- RAG/检索
- 上下文管理
status: 草稿
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/9b7da346ab604dbba51721accbc88055
notion_id: 9b7da346-ab60-4dbb-a517-21accbc88055
---

## 定义

Navigation over Search 是一种信息检索范式，主张 Agent 应像人类浏览文件系统一样「导航」信息源（ls 目录、grep 函数名、打开文件、跟踪 import），而非将所有内容嵌入向量数据库后做 top-k 检索。该模式源自 Coding Agent 的实践，被推广到企业知识检索场景。

## 关键要点

- **向量检索的三大缺陷**：索引永远过时、分块边界不准确、引用指向上周的碎片

- Coding Agent 已验证此模式：它们通过 `ls`、`grep`、`cat`、跟踪 import 来理解代码库，而非嵌入整个 repo

- 每个信息源天然具备等价的导航接口（Slack 频道列表、Drive 文件夹、CRM 记录），可直接复用

- **三大优势**：

  1. 实时状态——30 秒前的 Slack 消息即可获取

  1. 真实引用——每个引用都是可打开的路径

  1. 权限原生——Drive、Slack 各自控制访问权限

- **代价**：更多 LLM 调用（向量检索 1 次往返 vs 导航 3-4 次），但换来的数据新鲜度和准确性值得

## 来源引用

- [摘要：Meet Scout. The open-source company brain](summaries/摘要：Meet Scout. The open-source company brain.md)（[原文](https://x.com/ashpreetbedi/status/2049180168200106150)）
