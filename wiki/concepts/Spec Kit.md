---
title: Spec Kit
type: concept
tags:
- Coding Agent
status: 审核中
confidence: high
last_compiled: '2026-04-19'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/8d902dc11fa94f93b99870410753df78
notion_id: 8d902dc1-1fa9-4f93-b998-70410753df78
---

## 定义

Spec Kit 是 GitHub 官方开源的 Spec-Driven Development 框架，核心概念是「宪法」（Constitution）——项目级的技术栈、代码规范、架构原则、安全底线文档，所有 AI 操作都不能违反宪法约束。

## 关键要点

- 七阶段工作流：用户需求 → Specify → Clarify → Plan → Tasks → Analyze → Implement

- 每个阶段之间有「门禁」（gate），上一阶段审核通过才能进下一阶段

- 适合 0→1 新项目和合规要求高的场景（金融、医疗）

- **局限性**：流程重（完整文档 800+ 行）、假设需求线性推进、不适合改旧代码、无知识复利机制

- 腾讯工程师实践 3 个月后放弃——需求频繁变更、80% 工作是改旧代码、多人并行冲突

## 来源引用

- [摘要：AI开发范式——Spec Kit、OpenSpec、BMAD 全解析](summaries/摘要：AI开发范式——Spec Kit、OpenSpec、BMAD 全解析.md)（娄晨，2026-03-03）— 详细对比三大 SDD 框架，含企业落地失败案例
