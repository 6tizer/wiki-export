---
title: 摘要：AI Agent的"海姆达尔计划"：让大模型看见代码的双眼
type: summary
tags:
- Coding Agent
- Agent 技能
status: 已审核
confidence: high
last_compiled: '2026-04-25'
source_tags: ''
source_article_url: https://www.notion.so/34d701074b68811aa8b1cf4203f7a261
notion_url: https://www.notion.so/2fd03487a75d40da9941ea242ebf9e77
notion_id: 2fd03487-a75d-40da-9941-ea242ebf9e77
---

## 一句话摘要

MCP 正在把代码知识图谱、本地检索与自动化 Hook 接到 Coding Agent 身上，让大模型不再依赖超长上下文硬塞整个代码库，而是通过结构化检索真正“看见”代码。

## 关键洞察

- 代码理解的瓶颈不是上下文窗口不够大，而是 **上下文选择机制** 不够好；把无关代码塞进窗口，只会让 Agent 在盲人摸象。

- **MCP 协议** 像 AI 世界的 USB-C，把 Tools、Resources、Prompts 统一成可插拔接口，让外部知识源和工具链能稳定接入 Agent。

- **GitNexus** 提供代码知识图谱与依赖/调用链分析，帮助 Agent 在修改前先看清调用关系、影响范围和执行流。

- **QMD** 通过 BM25、向量检索与重排组合，补上文档与代码片段的高质量召回能力，让局部上下文更准确。

- **Claude Code Hooks** 让图谱增强、提交后重索引等流程自动发生，意味着“上下文工程”开始从人工喂料走向系统化流水线。

## 提取的概念

- [MCP 协议](concepts/MCP 协议.md)

- [GitNexus](entities/GitNexus.md)

- [QMD](entities/QMD.md)

- [代码知识图谱](concepts/代码知识图谱.md)

- [AST 感知分块](concepts/AST 感知分块.md)

- [Claude Code Hooks](concepts/Claude Code Hooks.md)

## 原始文章信息

- 作者：智物社

- 来源：微信

- 发布时间：2026-04-08 09:23

- 原文链接：[查看原文](https://mp.weixin.qq.com/s?__biz=MzI4MTc1Njg0MA%3D%3D&mid=2247486027&idx=1&sn=5044a57bef3d70a570db55273e382056&chksm=ea4fee508bee3d6d05240803fd1567e72c1dcc6d4a527b35a60dbca6b604e8a90021341f6c90#rd)

- 源文章页：AI Agent的"海姆达尔计划"：让大模型看见代码的双眼

## 个人评注

这篇内容对 Tizer 当前工作流的启发很直接：下一代 Coding Agent 的关键，不是继续追求更大的上下文窗口，而是把代码结构、项目知识、检索能力和执行 Hook 组织成一条稳定的 context pipeline。无论是 OpenClaw、Claude Code 还是后续内容工厂里的工程 Agent，真正的壁垒都会落在“怎么把对的信息在对的时刻送进模型”上。
