---
title: 摘要：Meeting Minutes 本地 AI 会议助手
type: summary
tags:
- LLM
- 开发工具
status: 已审核
confidence: medium
last_compiled: '2026-04-10'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/8f632cead0eb4b0486ca265499135328
notion_id: 8f632cea-d0eb-4b04-86ca-265499135328
---

## 一句话摘要

Meeting Minutes 是一款完全本地运行的开源 AI 会议助手，实时捕获音频、转录文本并生成摘要，所有数据处理均在本地设备完成以保障隐私。

## 关键洞察

- **隐私优先架构**：音频捕获、转录、摘要生成全部在本地设备完成，不依赖外部服务器

- **Whisper.cpp 本地转录**：使用 Whisper.cpp 进行本地语音转录，支持多种模型尺寸（tiny→large）和 GPU 加速

- **多 LLM 提供商支持**：统一接口支持 Anthropic、Groq、Ollama 等多个 LLM 后端，支持本地模型

- **内置知识图谱**：使用 ChromaDB 向量存储实现跨会议的语义搜索

- **Rust 实验性实现**：提供 Rust 版本的实时音频捕获和转录，面向高性能场景

## 提取的概念

- Whisper.cpp

- 本地音频转录

- 知识图谱（会议场景）

## 原始文章信息

- **作者**：CTOLib码库

- **来源**：微信公众号

- **发布时间**：2025-03-04

- **链接**：[原文链接](http://mp.weixin.qq.com/s?__biz=MzI4NjM0NjA3Ng%3D%3D&mid=2247487232&idx=1&sn=8a861fd65d971fc99ec8aadfbd0949e3)

## 个人评注

本地化的会议转录和摘要生成方案，隐私保障做得很到位。其 ChromaDB + 知识图谱的方案可作为 Tizer 知识管理流水线中「会议记录 → 知识提取」环节的参考。技术栈（FastAPI + Tauri + Next.js）也值得作为全栈本地应用的架构模板。
