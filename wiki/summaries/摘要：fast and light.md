---
title: 摘要：fast and light
type: summary
tags:
- 开发工具
- Agent 技能
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b6881bf8a7cd3e77067de5c
notion_url: https://www.notion.so/1bbbc73d09e7473891ec6faafdfee3c5
notion_id: 1bbbc73d-09e7-4738-91ec-6faafdfee3c5
---

## 一句话摘要

LiteParse 是一个面向 Agent 场景的开源文档解析器，通过 **Grid Projection Algorithm** 在不依赖 VLM 或其他机器学习模型的前提下，把复杂 PDF 的文本与表格快速投影成保留版式关系的结构化输出。

## 关键洞察

- 它的核心不是“更大的模型”，而是基于启发式规则的版式重建：先按相近 Y 坐标组织文本行，再抽取左右/中锚点，并将文本投影到网格列中。

- 这种 **Heuristics-first Parsing** 路线让 LiteParse 在速度、成本和本地部署灵活性上更有优势，尤其适合作为 Agent 的前置解析层。

- LiteParse 的重点是保留布局结构，而不仅仅抽取纯文本，因此对多栏排版、表格和空间关系敏感的 PDF 更有价值。

- 它既可以作为 CLI 或库独立使用，也可以作为 Skill 接入 coding agent / agent workflow，适合嵌入自动化内容处理链路。

- 官方同时明确了分层定位：LiteParse 适合 fast and light 的本地解析场景，而面对超复杂文档时，更重的 LlamaParse 仍然可能更合适。

## 提取的概念

- [LiteParse](entities/LiteParse.md)

- [Grid Projection Algorithm](concepts/Grid Projection Algorithm.md)

- [Heuristics-first Parsing](concepts/Heuristics-first Parsing.md)

- [Layout-aware PDF Parsing](concepts/Layout-aware PDF Parsing.md)

## 原始文章信息

- 作者：@jerryjliu0

- 来源：X书签

- 发布时间：2026-04-22

- 原文链接：[https://x.com/jerryjliu0/status/2047041129326194882](https://x.com/jerryjliu0/status/2047041129326194882)

## 个人评注

LiteParse 很适合放进 Tizer 的内容编译链路里做“先快后重”的本地解析层：先低成本拿到尽量保留结构的文本与表格，再决定是否升级到更重的解析器或进入 HITL 复核，这和 OpenClaw / 工作流自动化里的分层处理思路非常一致。
