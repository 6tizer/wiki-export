---
title: ai-gradio
type: entity
tags:
- AI 产品
- 多Agent协作
- 浏览器自动化
status: 审核中
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1bdda8786b644d33b318ce8c83b91d96
notion_id: 1bdda878-6b64-4d33-b318-ce8c83b91d96
---

## 定义

ai-gradio 是基于 Gradio 构建的 Python 包，提供统一的多模型 AI 应用开发接口，支持 15+ 个 AI 提供商（OpenAI、Anthropic、Gemini、Groq、DeepSeek、Qwen 等）的快速搭建交互界面。作者为 Ahsen Khaliq（AK391），曾参与 Gradio 团队。

**GitHub**：AK391/ai-gradio | ⭐ 1600+ Stars | 创建于 2024 年 12 月

## 核心优势

- **极低接入成本**：换模型只需改一行 `name` 参数

- **语音对话**：基于 WebRTC 的实时语音交互

- **视频理解**：通过 Gemini 支持摄像头实时输入

- **Agent 团队**：集成 CrewAI。支持多 Agent 协作

- **浏览器自动化**：内置 browser-use-agent

- **Computer-Use**：接入 OpenAI Computer-Use Preview

## 快速上手

```python
import gradio as gr
import ai_gradio

gr.load(
    name='openai:gpt-4-turbo',
    src=ai_gradio.registry,
    title='AI Chat',
).launch()
```

## 与同类工具对比

- vs Streamlit：ai-gradio 接入 AI 提供商更多；Streamlit UI 更灵活

- vs Chainlit：Chainlit 适合做持久化会话产品；ai-gradio 弹素更快

## 来源引用

- [摘要：ai-gradio：用几行 Python 代码，接入 15+ AI 大模型并搭建可视化应用](summaries/摘要：ai-gradio：用几行 Python 代码，接入 15+ AI 大模型并搭建可视化应用.md)
