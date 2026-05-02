---
title: 摘要：code-review-graph：给Claude Code装上代码地图，token直降6.8倍
type: summary
tags:
- 上下文管理
- MCP 协议
- IDE 集成
status: 已审核
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: https://www.notion.so/354701074b688100b9bdc3367caaa5dd
notion_url: https://www.notion.so/Tizer/e864d4096368478d99550bd114bbd0fb
notion_id: e864d409-6368-478d-9955-0bd114bbd0fb
---

## 一句话摘要

code-review-graph 通过 Tree-sitter 将代码库预解析为结构化调用图谱并持久化到 SQLite，再经 MCP 协议暴露给 Claude Code 等 AI 编程工具，实现"按需检索"替代"全文喂养"，平均降低 6.8 倍 token 消耗。

## 关键洞察

- **上下文喂养方式是最大成本浪费**：AI 编程中近一半 token 消耗在"读代码"环节，根因是 grep + 全文读取的粗暴检索方式，代码库越大失控越严重。

- **预计算 + 持久化是关键思路**：一次解析生成完整调用关系图存入 SQLite，后续查询为 O(图遍历) 而非 O(全量扫描)，跨 session 复用。

- **Blast-Radius 影响半径分析**：给定改动点，沿图谱逆向追溯受影响的函数、文件、测试集合并附风险评分，让 AI 精确定位"必读清单"而非盲目扩展上下文。

- **工程化成熟度高**：支持 23+ 语言、增量更新 2 秒内完成、内置 D3.js + Leiden 社区检测可视化、多格式导出（GraphML/Neo4j/Obsidian）。

- **工具生态广**：一条 install 命令自动配置 Claude Code、Codex、Cursor、Windsurf 等 12 家 AI 编程工具，一份图谱多端复用。

## 提取的概念

- [code-review-graph](entities/code-review-graph.md)

- [Tree-sitter](entities/Tree-sitter.md)

- [爆炸半径分析](concepts/爆炸半径分析.md)

- [代码知识图谱](concepts/代码知识图谱.md)

- [Claude Code](entities/Claude Code.md)

- [MCP 协议](concepts/MCP 协议.md)

- [增量更新](concepts/增量更新.md)

- [Leiden 图聚类](concepts/Leiden 图聚类.md)

## 原始文章信息

- 作者：NikoAI编程

- 来源：微信

- 发布时间：2026-04-28

- 原文链接：[https://mp.weixin.qq.com/s?__biz=MzI3MTQ3MjM2OQ==&mid=2247484175&idx=1&sn=c07eb173489d8d59c91de777250cfbfd](https://mp.weixin.qq.com/s?__biz=MzI3MTQ3MjM2OQ%3D%3D&mid=2247484175&idx=1&sn=c07eb173489d8d59c91de777250cfbfd)

- 源页面：code-review-graph：给Claude Code装上代码地图，token直降6.8倍

## 个人评注

本文是同一工具 code-review-graph 的第二篇推荐，与此前 AI开源提效指南 的介绍互补。本文从实际 token 账单痛点切入，补充了更具体的使用场景判断（大型 monorepo vs 小项目）、与 Claude Code 原生工具的差异对比表、以及社区 fork（better-code-review-graph）的信息。对 Tizer 的工作流而言，"预先建图 → 按需检索"的模式可直接类比到 OpenClaw 的代码任务上下文管理，值得在中大型项目中实测 token 节省效果。
