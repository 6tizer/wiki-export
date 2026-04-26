---
title: ChromaFs
type: concept
tags:
- 开发工具
- 知识管理
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/814baa5de0b74fac835d31973ce3500b
notion_id: 814baa5d-e0b7-4fac-835d-31973ce3500b
---

## 定义

ChromaFs 是 Mintlify 为 AI 文档助手设计的一种虚拟文件系统方案：它把 `ls`、`cat`、`grep`、`find`、`cd` 等文件系统操作翻译成对 Chroma 存储、缓存和目录树结构的查询，让 Agent 在无需真实沙箱的前提下获得“正在浏览文件系统”的工作体验。

## 核心要点

- 核心思想不是提供真实文件系统，而是提供足够逼真的只读文件系统幻觉。

- 目录树会被预处理为路径结构并缓存到内存，使导航类操作接近本地执行。

- `cat` 通过按 chunk 顺序回拼页面内容，`grep` 通过粗筛、预取与内存精筛来保证性能。

- 适合文档站、知识库等天然具备层级结构与只读特征的场景。

## 来源引用

- [摘要：RAG真被“替换”了？Mintlify造出ChromaFs假文件系统：冷启动46秒砍到100ms！](summaries/摘要：RAG真被“替换”了？Mintlify造出ChromaFs假文件系统：冷启动46秒砍到100ms！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkyODY4MjMxNw%3D%3D&mid=2247486957&idx=1&sn=a138c5f63d7a073cb6a379cd5b4f4228&chksm=c3d4c35bbb262a84c381bbe93326cfa84b8bdac9410335dacfe4aec68823c600edf420e857e6#rd)）

## 关联概念

- [RAG](concepts/RAG.md)

- [ChromaDB](entities/ChromaDB.md)
