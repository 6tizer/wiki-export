---
title: 受控 schema RAG
type: concept
tags:
- RAG/检索
- Harness 工程
status: 草稿
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/fff086d470cb47868c34e89560b3e727
notion_id: fff086d4-70cb-4786-8c34-e89560b3e727
---

## 定义

受控 schema RAG 是一种企业级知识库架构模式：先定义业务 schema（节点类型、关系类型、结构化字段），再让 LLM 按 schema 抽取信息，最后结合向量检索做问答。与自由生成的知识图谱不同，所有关系和字段都由业务规则预先约定，模型只能按规则输出。

## 关键要点

- **核心思想**：能用结构化字段和关系表确定的事情，不交给向量召回猜；需要模型发挥的地方，放在答案组织、解释和引用整合上

- **五层架构**：文件解析 → 结构化字段抽取 → 条款索引与受控图谱 → 权限过滤与混合检索问答 → 评测与审计

- **与自由图谱的区别**：Graphify 等工具让模型自由发现关系，受控 schema 则预先定义允许的节点类型和关系类型，模型只能按规则填充

- **适用场景**：合同知识库、法律文档、工业质检等需要权限控制、原文引用和审计追踪的企业场景

- **局限**：需要前期投入定义 schema，维护成本高于纯向量 RAG

## 关联概念

- LLM 知识编译

- Karpathy LLM Wiki 方法论

- Graphify

- 层级父子分块

## 来源引用

- [摘要：Karpathy的LLM Wiki + 3.5 万Star的Graphify：企业级 RAG 缺的真是知识图谱？](summaries/摘要：Karpathy的LLM Wiki + 3.5 万Star的Graphify：企业级 RAG 缺的真是知识图谱？.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI1ODIxNjk1OQ%3D%3D&mid=2649611293&idx=1&sn=7a85ba26ae5121b0eab159fd98346ff4&chksm=f368a598fd4532f7831bd0cf30ff657fce0d46d85cc880bb29b91c24a504ad1a2e9b01e71d2e#rd)）
