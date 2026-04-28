---
title: AI Agent 权限隔离
type: concept
tags:
- Agent 安全
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/b5cc9d5b5b3e4455a9fbbb505ed6fa76
notion_id: b5cc9d5b-5b3e-4455-a9fb-bb505ed6fa76
---

## 定义

AI Agent 权限隔离指在 AI 编程助手或自动化 Agent 接入生产环境时，通过 RBAC（基于角色的访问控制）、环境隔离、破坏性操作确认机制等手段，防止 Agent 因误判或指令歧义执行不可逆的破坏性操作（如删除生产数据库）。

## 关键要点

- AI Agent（如 Cursor + Claude）天然需要数据库、代码库的读写权限，但不应拥有生产环境的 Root 权限

- 云平台 API 应对破坏性操作（DELETE、DROP）要求二次确认，而非静默执行

- 备份必须与原始数据物理隔离（不同卷、不同区域），否则形同虚设

- 最小权限原则：Token 权限应严格限定为任务所需的最小范围

- 环境隔离：Staging 和 Production 使用完全独立的凭证和网络段

## 来源引用

- [摘要：9秒，公司没了！Claude「删库跑路」，Anthropic封杀110人公司，却还在扣钱](summaries/摘要：9秒，公司没了！Claude「删库跑路」，Anthropic封杀110人公司，却还在扣钱.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652695870&idx=1&sn=90f71bfc3f6091269c543b91368b22ee&chksm=f0e8f6e20c4403138c01e736a3c07cd72c780fe55c94401be3d215aa64fd7e8e3adce1d273e2#rd)）
