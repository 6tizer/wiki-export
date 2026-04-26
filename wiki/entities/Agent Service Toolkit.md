---
title: Agent Service Toolkit
type: entity
tags:
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/1324448195bc4d39adb1fefdd5780050
notion_id: 13244481-95bc-4d39-adb1-fefdd5780050
---

## 定义

Agent Service Toolkit 是一个开源 Python 项目模板，将 LangGraph（Agent 逻辑）、FastAPI（API 服务层）和 Streamlit（演示 UI）三者整合在一起，让开发者可以快速启动完整的 AI Agent 服务，而不必从零搞山标架工作。由 Joshua Carroll（Google PM）于 2024 年 8 月发起。

**GitHub**：JoshuaC215/agent-service-toolkit | ⭐ 4100+ Stars | License: MIT | 贡献者 20+

## 四层架构

1. **Agent 层（LangGraph）**：支持 `interrupt()` HITL、`Command` 流程控制、`Store` 长期记忆、langgraph-supervisor 多 Agent 

1. **服务层（FastAPI）**：同步和流式 API 接口，支持 token 级和消息级双模式流

1. **UI 层（Streamlit）**：开笱即用聊天界面，内置语音输入/输出和 LangSmith 星级反馈

1. **工程化支持**：Docker Compose 一键启动、完整测试套件、ChromaDB RAG 集成、Ollama/VertexAI 支持

## 快速启动

```bash
echo 'OPENAI_API_KEY=your_key' >> .env
docker compose watch
```

## 已知问题

- Nginx 反向代理下流式输出可能断流

- Claude 模型下多系统消息冲突问题

- 默认 InMemoryStore，生产环境需替换为持久化存储

## 价値定位

填补 LangGraph 生态中「从 Agent 逻辑到可运行服务的最后一公里」的空白。社区估计节省 60-70% 的部署搭建时间。

## 来源引用

- [摘要：Agent Service Toolkit：用 LangGraph + FastAPI + Streamlit 快速搭建生产级 AI Agent 服务](summaries/摘要：Agent Service Toolkit：用 LangGraph + FastAPI + Streamlit 快速搭建生产级 AI Agent 服务.md)
