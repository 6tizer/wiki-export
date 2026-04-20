---
title: just-bash
type: entity
tags:
- 开发工具
- Agent 技能
status: 草稿
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/20d08c49e5ad4126b245e52c7c6b0b80
notion_id: 20d08c49-e5ad-4126-b245-e52c7c6b0b80
---

## 定义

just-bash 是 Vercel Labs 提供的一个 TypeScript Bash 子集实现，可解析常见 shell 命令、管道与参数。在 Mintlify 的方案中，它充当 Agent 与虚拟文件系统之间的命令解释层。

## 核心要点

- 让 Agent 可以继续用 shell 风格的工作方式思考与调用工具，而不必直接面向底层数据库接口。

- 通过暴露文件系统接口，支持把命令执行重定向到自定义后端。

- 在文档助手场景中，它的价值不在“执行真实系统命令”，而在提供一种自然的命令式检索交互面。

## 来源引用

- [摘要：RAG真被“替换”了？Mintlify造出ChromaFs假文件系统：冷启动46秒砍到100ms！](summaries/摘要：RAG真被“替换”了？Mintlify造出ChromaFs假文件系统：冷启动46秒砍到100ms！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkyODY4MjMxNw%3D%3D&mid=2247486957&idx=1&sn=a138c5f63d7a073cb6a379cd5b4f4228&chksm=c3d4c35bbb262a84c381bbe93326cfa84b8bdac9410335dacfe4aec68823c600edf420e857e6#rd)）

## 关联概念

- [RAG](concepts/RAG.md)

- [ChromaDB](entities/ChromaDB.md)
