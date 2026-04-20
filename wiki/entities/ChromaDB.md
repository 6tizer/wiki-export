---
title: ChromaDB
type: entity
tags:
- 开发工具
- 记忆系统
status: 草稿
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/392c64d3898640639c48b70699176c08
notion_id: 392c64d3-8986-4063-9c48-b70699176c08
---

## 定义

ChromaDB 是面向 AI 应用的开源向量数据库与检索存储组件，常被用作本地优先记忆系统的语义检索层。本文场景里，它承担 MemPalace 的向量记忆存储底座。

## 关键要点

- 与 SQLite 知识图谱配合，形成“语义检索 + 结构化关系”的双层记忆架构。

- 支持本地运行，不依赖外部 API 即可完成基础记忆检索。

- 在 MemPalace 体系里，ChromaDB 更偏向原始对话与召回层，而不是完整的知识表达层。

## 来源引用

- [摘要：Claude-Mem：让AI编程助手拥有跨会话持久记忆](summaries/摘要：Claude-Mem：让AI编程助手拥有跨会话持久记忆.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg2MjIwODc3Mw%3D%3D&mid=2247518172&idx=1&sn=867250666fc5c9f4a7ca9c84f243b970&chksm=cf5ea8e68aca9ab2d4c501de00f8682baffb9866b120a678223699ba9024ea0b302de2a35158#rd)）

- [摘要：RAG真被“替换”了？Mintlify造出ChromaFs假文件系统：冷启动46秒砍到100ms！](summaries/摘要：RAG真被“替换”了？Mintlify造出ChromaFs假文件系统：冷启动46秒砍到100ms！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkyODY4MjMxNw%3D%3D&mid=2247486957&idx=1&sn=a138c5f63d7a073cb6a379cd5b4f4228&chksm=c3d4c35bbb262a84c381bbe93326cfa84b8bdac9410335dacfe4aec68823c600edf420e857e6#rd)）——在该方案中，Chroma 充当虚拟文件系统背后的文档分块与查询存储层

- [原文链接](https://mp.weixin.qq.com/s/1rY6qMBqSELEm83MbhDzLA)｜源文章：96.6%召回率，0美元成本：这款开源AI记忆系统凭什么超越一切付费方案

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ%3D%3D&mid=2247505903&idx=1&sn=d9f6ab8c463b8d5e883f51ffcf133c45&chksm=c121bbb7f887f2a99a0cc4e1ce630437181d622f5c30a1064e566c02e77a5f7082ea79d11ab1#rd)｜源文章：[摘要：刚刚开源就斩获 46K+ Star！生化危机女主在 GitHub 开源了一个本地 AI 记忆系统！](summaries/摘要：刚刚开源就斩获 46K+ Star！生化危机女主在 GitHub 开源了一个本地 AI 记忆系统！.md)

## 关联概念

- [Mintlify](entities/Mintlify.md)

- [ChromaFs](concepts/ChromaFs.md)

- [just-bash](entities/just-bash.md)

- [MemPalace](entities/MemPalace.md)

- [LongMemEval](concepts/LongMemEval.md)

- [AAAK 方言](concepts/AAAK 方言.md)

- [本地优先知识库](concepts/本地优先知识库.md)

- [知识图谱层](concepts/知识图谱层.md)
