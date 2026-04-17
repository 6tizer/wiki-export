---
title: LangChain
type: entity
tags:
- Agent 编排
- LLM
status: 草稿
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/51899a21209143d19b0bd28657508e92
notion_id: 51899a21-2091-43d1-9b0b-d28657508e92
---

## 定义

LangChain 是由 Harrison Chase 于 2022 年 10 月创建的开源 LLM 应用开发框架，提供连接大语言模型与各种工具、数据源的标准化接口，已成为 AI 应用开发的事实标准之一。核心语言为 Python 和 JavaScript（LangChain.js）。

**GitHub**：langchain-ai/langchain | ⭐ 129k+ Stars | License: MIT

## 核心能力

- **LLM Provider 抽象**：统一接口调用 OpenAI、Anthropic、Google 等所有主流模型

- **Chain/Pipeline 编排**：将多个 LLM 调用、工具调用链接成工作流

- **RAG 支持**：内置文档加载、分块、向量检索的完整管道

- **Agent 工具**：支持 Tool 定义和 Agent 循环

- **LangSmith**：配套的链路追踪和调试平台

- **LangGraph**：专门的有状态 Agent 编排子框架（另见词条）

## 主要局限

- 抽象层过多，部分场景调试困难（「过度封装」批评）

- JS 版本 bundle 体积较大（gzip 后约 101 KB），不支持 Edge Runtime

- 迭代频繁，API 有时不向后兼容

## 来源引用

- LangChain + Qdrant S3 语义检索流水线教程

- Agent Service Toolkit：LangGraph + FastAPI + Streamlit

- Browser Use 开源浏览器自动化

- LangGraph AI 金融分析师 Agent

- ai-gradio 多模型统一接口

- LLM Graph Transformer 知识图谱

- Nexus AI 学术研究助手

- Web3 AI Agent 的真相：Vercel AI SDK vs LangChain
