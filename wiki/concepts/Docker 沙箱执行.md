---
title: Docker 沙箱执行
type: concept
tags:
- Harness 工程
- Agent 安全
- 算力基础设施
status: 审核中
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/eb22bc39f46d4156b772955d122c45ca
notion_id: eb22bc39-f46d-4156-b772-955d122c45ca
---

## 定义

Docker 沙箱执行是让 Agent 在独立容器中运行代码、读写文件和调用命令的一种隔离执行方式。

## 关键要点

- 它把真实执行能力和宿主机风险做了一层边界隔离。

- 对 Agent 系统来说，沙箱不是附属品，而是把建议变成可执行操作的关键基础设施。

- 冷启动、资源开销和权限治理是这类方案的主要工程代价。

## 来源引用

- [原文链接](https://x.com/heynavtoor/status/2030904551424074107)｜《DeerFlow 2.0：字节跳动开源的 SuperAgent 框架，给 AI 一台真正的电脑》｜来源条目：DeerFlow 2.0：字节跳动开源的 SuperAgent 框架，给 AI 一台真正的电脑

- [原文链接](https://x.com/Gorden_Sun/status/2033941005368774953)｜《阿里开源 OpenSandbox：让 AI Agent 不再「裸奔」的沙箱基础设施》｜来源条目：[摘要：阿里开源 OpenSandbox：让 AI Agent 不再「裸奔」的沙箱基础设施](summaries/摘要：阿里开源 OpenSandbox：让 AI Agent 不再「裸奔」的沙箱基础设施.md)
