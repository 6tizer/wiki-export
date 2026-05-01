---
title: HTTP Hooks
type: concept
tags:
- 内容自动化
- AI 产品
- 上下文管理
status: 审核中
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/9912d7adebad4d80a30f19d7c6509d90
notion_id: 9912d7ad-ebad-4d80-a30f-19d7c6509d90
---

## 定义

HTTP Hooks 是 Claude Code Hooks 中面向外部系统集成的执行类型，会把事件上下文以 JSON 形式发送到指定 URL，再依据响应内容影响 Claude 的后续行为。

## 核心要点

- 适合接入 Slack、Discord、PagerDuty、自建审计服务或审批服务，把本地工作流扩展到外部系统。

- 是否真正拦截不取决于 HTTP 状态码本身，而取决于返回的结构化 JSON 决策内容。

- 它把 Claude Code 从单机助手扩展为可接入企业基础设施的事件节点。

## 来源引用

- [摘要：打造可靠的 AI 编程环境：Claude Code Hooks 完整开发者指南](summaries/摘要：打造可靠的 AI 编程环境：Claude Code Hooks 完整开发者指南.md)（[原文](https://mp.weixin.qq.com/s?__biz=MjM5NzA1NzMyOQ%3D%3D&mid=2247486947&idx=1&sn=92ca2b4f44cadd181eb6b40087a2531b&chksm=a7e11bb1d385c29bce1587e79207574fba3835086a7fbed287fbf12e86194e37111fb2982d78#rd)）

## 关联概念

- [Claude Code Hooks](concepts/Claude Code Hooks.md)

- [Command Hooks](concepts/Command Hooks.md)

- [Agent Hooks](concepts/Agent Hooks.md)
