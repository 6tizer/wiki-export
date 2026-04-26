---
title: ECL 管道
type: concept
tags:
- 知识管理
- RAG/检索
- 长期记忆
status: 审核中
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/b3aec1edac7c4ecbb5d9de1189088b06
notion_id: b3aec1ed-ac7c-4ecb-b5d9-de1189088b06
---

## 定义

ECL 管道是 Cognee 用来组织记忆构建流程的核心工作流，把数据处理拆分为 Extract、Cognify、Load 三个阶段，用于将原始资料转成可检索、可推理的记忆结构。

## 关键要点

- Extract 负责从多种数据源摄取原始内容

- Cognify 负责抽取实体、关系与结构化语义

- Load 负责把结果写入图数据库与向量数据库

- 这种分层让每个阶段都能独立扩展或替换

- 相比把全部逻辑塞进单一 RAG 流程，ECL 更适合长期演化的 Agent 记忆系统

## 来源引用

- [摘要：6行代码搞定AI Agent记忆！这个16K Star的开源项目打破了传统RAG痛点！](summaries/摘要：6行代码搞定AI Agent记忆！这个16K Star的开源项目打破了传统RAG痛点！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ%3D%3D&mid=2247505915&idx=1&sn=435f936eea034dc7723fca601ed0dd4b&chksm=c1bafd08562e145ba4f562227b66cba5d99b801b72ca91c78c9b8d092816ecbdb77e941b262d#rd)）
