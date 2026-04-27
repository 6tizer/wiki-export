---
title: Single Source of Truth
type: concept
tags:
- Agent 协作模式
status: 审核中
confidence: medium
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/6017c73e7f88443eac1a2b64aa061d47
notion_id: 6017c73e-7f88-443e-ac1a-2b64aa061d47
---

## 定义

Single Source of Truth 指系统只保留一个权威状态源，其他界面与工具都围绕这份唯一状态进行读取和操作，避免出现多份副本彼此漂移。

## 关键要点

- **避免状态分叉**：减少本地副本、缓存和同步链路带来的冲突

- **降低协作摩擦**：所有操作都围绕同一份远程工作流状态展开

- **适合远程工作流**：尤其适用于服务器端才是真实运行环境的场景

- **强调一致性优先**：宁可牺牲部分离线便利，也要保证状态一致

## 来源引用

- [原文链接](https://x.com/billtheinvestor/status/2042946398124150891)｜X书签｜来源条目：Hermes Desktop：用原生 macOS 应用直连远程 AI 工作流，彻底告别浏览器壳
