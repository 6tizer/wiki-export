---
title: 摘要：Claude Code Memory 记忆功能
type: summary
tags:
- LLM
- 记忆系统
- 开发工具
status: 已审核
confidence: high
last_compiled: '2026-04-10'
source_tags: Agent, LLM, 自动化, Claude
source_article_url: ''
notion_url: https://www.notion.so/a860e3f3819247328f9f8e9e85f56b48
notion_id: a860e3f3-8192-4732-8f9f-8e9e85f56b48
---

## 一句话摘要

Claude Code 推出全新 Memory 记忆功能，通过自动记忆和文档记忆两种机制以及层级化管理方案，解决 AI 在长期对话中的记忆管理难题。

## 关键洞察

- **双记忆机制**：分为自动记忆（AI 自动捕获对话中的关键偏好和模式）和文档记忆（用户以纯文本格式主动记录偏好和项目说明）

- **按需读取优化**：不是加载全部记忆，而是仅加载核心记忆以提高对话效率，避免上下文窗口浪费

- **层级化记忆管理**：提供多层级的规则和约定管理方案，确保不同场景下灵活应用适当的记忆内容

- **纯文本格式**：记忆以纯文本存储，简化管理同时保持灵活性和可编辑性

- **潜在风险**：自动记忆可能捕获不准确或过时的信息，用户需谨慎对待

## 提取的概念

- Claude Code Memory

- 自动记忆

- 层级化记忆管理

## 原始文章信息

- **作者**：字节笔记本

- **来源**：微信公众号

- **发布时间**：2026-02-27

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=MzIzMzQyMzUzNw%3D%3D&mid=2247513823&idx=1&sn=8fe0a5296f51f06fa0b901bb706fd32e)

## 个人评注

与现有 Wiki 中的记忆系统概念（Auto Memory、Memory Folder、记忆分层架构）高度相关。Claude Code 的双记忆机制（自动 + 手动）可直接参考用于 Tizer 的知识编译系统——自动记忆对应 Agent 自动提取知识，文档记忆对应人工编辑的 Wiki 条目。层级化管理方案也与本 Wiki 的分层知识架构不谋而合。
