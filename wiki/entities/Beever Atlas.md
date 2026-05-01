---
title: Beever Atlas
type: entity
tags:
- RAG/检索
- 长期记忆
- 知识管理
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/037a80d87b2c46719b7c0bbda12f67b3
notion_id: 037a80d8-7b2c-4671-9b7c-0bbda12f67b3
---

## 定义

Beever Atlas 是一个开源的 LLM-Wiki 对话知识库系统，能自动将 Slack、Discord、Teams、Mattermost 等聊天内容提取为结构化 Wiki。项目开源于 [Beever-AI/beever-atlas](https://github.com/Beever-AI/beever-atlas)，Apache 2.0 许可。

## 关键要点

- **Wiki-first RAG**：不同于传统 RAG 直接检索原始消息片段，Beever Atlas 先将对话蒸馏为结构化 Wiki（主题页、实体图、决策、引用），再在干净的知识上做检索

- 灵感来自 Andrej Karpathy 的观点：LLM 更擅长推理经过整理的百科式内容，而非原始对话记录

- **双记忆架构**：三层语义存储（频道/主题/原子事实）+ Neo4j 图存储（实体与关系）

- 6 阶段 ADK 管线：消息提取原子事实、去重、聚类为主题页并附引用

- 智能查询路由器按问题类型选择语义检索或图检索

- 通过 MCP 接入 Claude Code / Cursor 等外部 AI Agent

- 111 GitHub Stars，使用 Google ADK 构建

## 技术栈

- 后端：FastAPI + MongoDB + Redis

- 图存储：Neo4j（typed Neo4j with provenance + temporal props）

- 向量存储：Weaviate

- 嵌入：Jina v4（2048-dim）

- LLM：Gemini

## 来源引用

- [摘要：hybrid GraphRAG memory system](summaries/摘要：hybrid GraphRAG memory system.md)（[原文](https://x.com/garrytan/status/2048503081911128119)）
