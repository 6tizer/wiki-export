---
title: Prompt Cache
type: concept
tags:
- Coding Agent
- 开发工具
status: 草稿
confidence: high
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/3b6f5f03ff834b4d916444bb553bacd6
notion_id: 3b6f5f03-ff83-4b4d-9164-44bb553bacd6
---

## 定义

Prompt Cache 是模型服务对重复 prompt 前缀进行缓存复用的机制，可显著降低长会话下的调用成本与延迟。

## 关键要点

- 关键不只是有缓存，而是保持 prompt 前缀稳定可复用

- 会直接影响长上下文 Agent 的成本曲线

- 因此很多上下文管理设计都会反向围绕缓存命中率展开

## 来源引用

- 《Claude Code 的七层记忆架构：从毫秒级 Token 裁剪到「睡眠整理」系统》｜X书签文章｜原文链接：[https://x.com/troyhua/status/2039052328070734102](https://x.com/troyhua/status/2039052328070734102)
