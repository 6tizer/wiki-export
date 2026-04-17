---
title: LLM+Markdown+Wiki 知识库
type: concept
tags:
- 知识管理
- LLM
status: 草稿
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/23c10731c26342c9aa5bf0b45173d695
notion_id: 23c10731-c263-42c9-aa5b-f0b45173d695
---

## 定义

Karpathy 提出的个人知识库构建方法：将原始资料（论文、文章、代码仓库）以 Markdown 形式索引，利用 LLM 算力自动编译为结构化 Wiki，并在其上进行问答、可视化和知识沉淀。

## 核心架构（三层分离）

1. **原始资料层（raw/）**：原始内容，不经 LLM 处理，保持完整性

1. **LLM 编译产物层（wiki/）**：LLM 自动整理的摘要、概念、关联，可迭代更新

1. **宪法文件层（system/）**：定义编译规则和约束的 instructions 文件，类似 Agent 的 system prompt

## 关键操作

- **资料灌入**：Obsidian Web Clipper / 脚本导入

- **提问检索**：在 Wiki 上对 LLM 提问，获取跨文档综合答案

- **输出归档**：将 LLM 生成的分析保存回 Wiki

- **健康检查**：定期审查 Wiki 质量，修复错误条目

## 与传统 RAG 的区别

- RAG：需要向量数据库 + 检索工程，适合大规模精确检索

- LLM+MD+Wiki：依赖 LLM 的上下文理解，适合中小规模个人知识库，无需工程基础

## 产品化实现

- **有道宝库**：低门槛产品，支持多格式导入、引用溯源、播客生成

- **NotebookLM**（Google）：类似功能，对中文支持较弱

- **Obsidian + CacheZero**：开发者自建方案

## 来源引用

- [摘要：Karpathy LLM Wiki 个人知识库方法论](summaries/摘要：Karpathy LLM Wiki 个人知识库方法论.md)

- [摘要：实操指南：如何用 Karpathy 的 LLM + Markdown + Wiki 搭建个人知识库](summaries/摘要：实操指南：如何用 Karpathy 的 LLM + Markdown + Wiki 搭建个人知识库.md)

- [摘要：实操指南：如何用 Karpathy 的 LLM+Markdown+Wiki 搭建个人知识库](summaries/摘要：实操指南：如何用 Karpathy 的 LLM+Markdown+Wiki 搭建个人知识库.md)

- [摘要：Karpathy 开源个人 LLM Wiki ——知识编译而非检索](summaries/摘要：Karpathy 开源个人 LLM Wiki ——知识编译而非检索.md)

@Wiki 引用升级员 测试 3 条
