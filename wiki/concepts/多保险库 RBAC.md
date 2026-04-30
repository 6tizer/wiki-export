---
title: 多保险库 RBAC
type: concept
tags:
- 安全/隐私
- Agent 技能
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/31ee07e024984a48bf4c60963423d766
notion_id: 31ee07e0-2498-4a48-bf4c-60963423d766
---

## 定义

多保险库 RBAC 是一种把不同 Agent、环境或任务划分到不同密钥保险库中，并结合基于角色的访问控制进行授权的安全模式，用来压缩单个 Agent 的权限爆炸半径。

## 关键要点

- 通过把凭证分散到多个保险库，可以避免一个 Agent 获得全局访问能力。

- RBAC 让团队按角色、任务或运行环境分配最小必要权限。

- 这种结构尤其适合多 Agent 并行、多人协作和生产环境调用外部 API 的场景。

- 它把传统企业权限治理方法迁移到了 Agent 基础设施层。

## 来源引用

- [摘要：A dream come true for every human anxious about their agents leaking secrets.](summaries/摘要：A dream come true for every human anxious about their agents leaking secrets.md)（[原文](https://x.com/dangtony98/status/2047036513536622918)）
