---
title: OpenViking
type: entity
tags:
- 记忆系统
status: 审核中
confidence: medium
last_compiled: '2026-04-19'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/cce5707add6c4188968ca407dd16b49b
notion_id: cce5707a-dd6c-4188-968c-a407dd16b49b
---

## 定义

OpenViking 是字节跳动火山引擎（Volcengine）Viking 团队开源的 Agent 记忆管理框架，将传统 RAG 的平面向量检索升级为「文件系统范式」的层级归纳检索，显著提升 Token 效率和检索精度。

**GitHub**：volcengine/OpenViking | ⭐ 约 2900 Stars | 开源库台项目 | Apache 式许可证

## 核心创新：文件系统范式

引入 `viking://` 协议，将 Agent 的记忆（Memory）、资源（Resources）、技能（Skills）统一组织为虚拟文件系统。每个目录下有两个特殊文件：

- **`.abstract.md`****（L0，约 100 tokens）**：目录极简摘要（文件夹标签）

- **`.overview.md`****（L1，约 2k tokens）**：目录详细大纲（章节导读）

检索时递归下骻：先读 L0 摘要判断相关目录，确认后读 L1 概览定位具体文件，最后才加载全文。

## 与传统 RAG 的对比

- 传统 RAG：平面向量检索，海量碎片中「捩针」，Token 消耗大

- OpenViking：层级目录递归定位，最小化无关内容加载，Token 高效

## 应用场景

- 大规模结构化知识库的 Agent 记忆管理

- 项目代码库、文档、邮件全量上下文的结构化第二大脑

## 与其他记忆系统对比

- vs Mem0：图谱+向量混合，简单容易应用

- vs OpenViking：大规模结构化场景下最为突出

## 来源引用

- [摘要：OpenViking：字节跳动用「文件系统范式」重构 Agent 记忆，终结扁平 RAG 时代](summaries/摘要：OpenViking：字节跳动用「文件系统范式」重构 Agent 记忆，终结扁平 RAG 时代.md)

- 摘要：memory-lancedb-pro：给你的 OpenClaw Agent 装上真正会记忆的大脑

- 摘要：OpenClaw 长期记忆终极方案：memory-lancedb-pro vs total-recall 深度对比

- [原文链接](https://x.com/berryxia/status/2032838544688034081)｜《OpenViking：字节火山引擎开源的 AI Agent 上下文数据库》｜来源条目：[摘要：OpenViking：字节火山引擎开源的 AI Agent 上下文数据库](summaries/摘要：OpenViking：字节火山引擎开源的 AI Agent 上下文数据库.md)

## 关联概念

- memory-lancedb-pro

- [智能遗忘](concepts/智能遗忘.md)

- total-recall

- [Agent 上下文数据库](concepts/Agent 上下文数据库.md)

- [viking://](concepts/viking---.md)

- [L0/L1/L2 分层加载](concepts/L0-L1-L2 分层加载.md)

- [MiroFish](entities/MiroFish.md)

- [多智能体社会仿真](concepts/多智能体社会仿真.md)

- 《memory-lancedb-pro：给你的 OpenClaw Agent 装上真正会记忆的大脑》（axiaisacat，2026-03-07）— 文章将 OpenViking 作为对照，强调其在 Token 效率上的优势

- [摘要：一周暴涨 8.4k Star：GitHub Coding AI 开源项目周榜 Top 20 深度解析](summaries/摘要：一周暴涨 8.4k Star：GitHub Coding AI 开源项目周榜 Top 20 深度解析.md)— 将 OpenViking 视为 Agent 上下文数据库与文件系统范式代表

- [原文链接](https://x.com/ResearchWang/status/2034161775797801206)｜《OpenClaw 省钱五剑法：节省 90% Token 消耗的完整插件指南》｜来源条目：[摘要：OpenClaw 省钱五剑法：节省 90% Token 消耗的完整插件指南](summaries/摘要：OpenClaw 省钱五剑法：节省 90% Token 消耗的完整插件指南.md)

- [原文链接](https://x.com/qkl2058/status/2035396930587787650)｜《MiroFish × OpenViking：让几千个 AI 代理拥有完美长期记忆，重新定义事件预测》｜来源条目：[摘要：MiroFish × OpenViking：让几千个 AI 代理拥有完美长期记忆，重新定义事件预测](summaries/摘要：MiroFish × OpenViking：让几千个 AI 代理拥有完美长期记忆，重新定义事件预测.md)
