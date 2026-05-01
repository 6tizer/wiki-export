---
title: 摘要：AI开发范式——Spec Kit、OpenSpec、BMAD 全解析
type: summary
tags: []
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a9f4a95709784fa6bb4b6f6150df79c6
notion_id: a9f4a957-0978-4fa6-bb4b-6f6150df79c6
---

## 一句话摘要

Vibe Coding 在大型项目中暴露上下文丢失和技术债问题，Spec-Driven Development（SDD）提供了结构化解法，但真正的范式转移在于 Context Engineering（管理 AI 认知）和 Compound Engineering（经验复利）。

## 关键洞察

- **Vibe Coding 三大问题**：上下文丢失（跨对话遗忘架构决策）、文档-代码脱节（代码暴涨但无人知全貌）、技术债加速（局部打补丁成缝合体）

- **三大 SDD 框架各有定位**：Spec Kit（GitHub 官方，「宪法+门禁」全流程，重但严谨）、OpenSpec（增量 Delta Spec，轻量适合迭代）、BMAD（模拟敏捷团队多角色，覆盖全但复杂）

- **Spec Kit 企业落地失败**：腾讯工程师实践 3 个月后放弃——需求非线性、80% 是改旧代码、多人并行冲突、无知识复利

- **Context Engineering 是内功**：系统性管理 AI 每次交互能「看到」的信息（Memory Bank + Delta Spec + 代码上下文 + 历史经验），而非靠手动 prompt

- **Compound Engineering 实现经验复利**：规划→执行→审查→沉淀，每次任务完成自动提取经验写入 experience-index，下次类似任务成本递减（45min→15min→5min）

## 提取的概念

- Spec Kit

- OpenSpec

- BMAD Method

- Context Engineering

- Compound Engineering

- Vibe Coding（已有概念，追加引用）

- 规范驱动开发 SDD（已有概念，追加引用）

## 原始文章信息

- **作者**：娄晨

- **来源**：微信公众号

- **发布时间**：2026-03-03

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=MzIxOTgzNTE3Ng%3D%3D&mid=2247484008&idx=1&sn=c6a05ebe7dd44cb6701b7b85eff4073a)

## 个人评注

Compound Engineering 的「经验沉淀→自动加载」模式与 Tizer 的知识 Wiki 编译流程异曲同工——都是将非结构化经验转化为可检索的结构化知识。Context Engineering 的思路可以直接应用到 HITL 工作流设计中：为 Agent 预装好正确的上下文，而非依赖用户手动输入。
