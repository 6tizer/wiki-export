---
title: MemPalace
type: entity
tags:
- 记忆系统
status: 草稿
confidence: high
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/88975eec5a264d5d954cd49e28efee97
notion_id: 88975eec-5a26-4d5d-954c-d49e28efee97
---

## 定义

MemPalace将古希腌记忆宫段法（Method of Loci）映射为代码中的五层数据结构，采用完整性优先策略（不对对话进行摘要压缩），在LongMemEval基准测试500题中达到96.6%召回率。

## 五层数据结构

1. **Wings（侧厅）**：按人或项目划分记忆

1. **Halls（大殿）**：按记忆类型分类

1. **Rooms（房间）**：按具体话题组织

1. **Closets（衣柜）**：存放摘要

1. **Drawers（抽屉）**：存放原始文件

## 技术实现

- **ChromaDB**：向量存储，存原始对话不压缩

- **SQLite**：时序知识图谱，支持时间感知查询

- **MCP Server**：19个工具，支持Claude/ChatGPT/Cursor/Gemini

- **L0-L3分层**：每次唤醒AI只加载约170 tokens

## 完整性优先策略

> 宁可检索慢一点，不要丢失细节

随着语境窗口越来越大、存储成本越来越低，完整存储洺益越来越内删消摘要压缩的必要性。

## 争议与局限

- AAAK压缩声称「30倍无损压缩」不成立

- 「矛盾检测」功能尚未完全实现

- 维护者主动承认这些过度营销，开源社区信任建设的典范

## 与竞品对比

| 特性 | MemPalace | MemBrain1.5 | OpenClaw Dreaming |

| --- | --- | --- | --- |

| 设计哲学 | 完整性优先 | 自适应实体树 | 相关性优先 |

| 召回率 | 96.6% | SOTA | 未公开 |

| 触发 | 被动 | 实时 | 定时 |

## GitHub

[https://github.com/milla-jovovich/mempalace](https://github.com/milla-jovovich/mempalace)

## 来源引用

- 摘要：太抽象了，Alice都来了。（cxuanAI，2026-04-08）

- [原文链接](https://x.com/blackanger/status/2043063705324392585)｜源文章：mempal：用 Rust 重铸 AI 记忆宫殿，Coding Agent 的项目记忆工具

- [原文链接](https://mp.weixin.qq.com/s/1rY6qMBqSELEm83MbhDzLA)｜源文章：96.6%召回率，0美元成本：这款开源AI记忆系统凭什么超越一切付费方案

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ%3D%3D&mid=2247505903&idx=1&sn=d9f6ab8c463b8d5e883f51ffcf133c45&chksm=c121bbb7f887f2a99a0cc4e1ce630437181d622f5c30a1064e566c02e77a5f7082ea79d11ab1#rd)｜源文章：[摘要：刚刚开源就斩获 46K+ Star！生化危机女主在 GitHub 开源了一个本地 AI 记忆系统！](summaries/摘要：刚刚开源就斩获 46K+ Star！生化危机女主在 GitHub 开源了一个本地 AI 记忆系统！.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493206&idx=1&sn=7080809308368860641fd4df6601bef9&chksm=c0a8ea2ad24191e6e6e084a08eacab4b318f12dd484d75fe35bb554e96c6e9906e407e998911#rd)｜《Karpathy 提出了 LLM Wiki，我用 Rust 把它造出来了，还打通了 MemPalace 知识图谱》｜来源条目：[摘要：Karpathy 提出了 LLM Wiki，我用 Rust 把它造出来了，还打通了 MemPalace 知识图谱](summaries/摘要：Karpathy 提出了 LLM Wiki，我用 Rust 把它造出来了，还打通了 MemPalace 知识图谱.md)

- [原文链接](https://x.com/witcheer/status/2044456778843238689)｜《I Went Through Every AI Memory Tool I Could Find. There Are Two Camps.》｜来源条目：[摘要：I Went Through Every AI Memory Tool I Could Find. There Are Two Camps.](summaries/摘要：I Went Through Every AI Memory Tool I Could Find. There Are Two Camps.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493215&idx=1&sn=7cc67138b3f4025466cb3a64a55c8109&chksm=c0ccfbe465f303ae41c71f66e977f5051c02fda3d0eb7a62327f390e017b04181fb0fcbff59e#rd)｜《Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了"持久大脑"，持续的高质量上下文，这事靠谱了》｜来源条目：[摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了"持久大脑"，持续的高质量上下文，这事靠谱了](summaries/摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了持久大脑，持续的高质量上下文，这事靠谱了.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493215&idx=1&sn=7cc67138b3f4025466cb3a64a55c8109&chksm=c0ccfbe465f303ae41c71f66e977f5051c02fda3d0eb7a62327f390e017b04181fb0fcbff59e#rd)｜来源条目：[摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了"持久大脑"，持续的高质量上下文，这事靠谱了](summaries/摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了持久大脑，持续的高质量上下文，这事靠谱了.md)

- [摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了"持久大脑"，持续的高质量上下文，这事靠谱了](summaries/摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了持久大脑，持续的高质量上下文，这事靠谱了.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493215&idx=1&sn=7cc67138b3f4025466cb3a64a55c8109&chksm=c0ccfbe465f303ae41c71f66e977f5051c02fda3d0eb7a62327f390e017b04181fb0fcbff59e#rd)）

## 关联概念

- [mempal](entities/mempal.md)

- [AAAK 方言](concepts/AAAK 方言.md)

- [混合检索](concepts/混合检索.md)

- [知识图谱层](concepts/知识图谱层.md)

- [自描述协议](concepts/自描述协议.md)

- [跨项目隧道](concepts/跨项目隧道.md)

- [LongMemEval](concepts/LongMemEval.md)

- [ChromaDB](entities/ChromaDB.md)

- [MCP 协议](concepts/MCP 协议.md)

- [本地优先知识库](concepts/本地优先知识库.md)

- [llm-wiki](entities/llm-wiki.md)

- [Claim 断言模型](concepts/Claim 断言模型.md)

- [wiki-mempalace-bridge](entities/wiki-mempalace-bridge.md)

- [FTS5 全文检索](concepts/FTS5 全文检索.md)

- [时序知识图谱](concepts/时序知识图谱.md)

- [wake-up 协议](concepts/wake-up 协议.md)

- [wiki-mempalace-bridge](entities/wiki-mempalace-bridge.md)

- [FTS5 全文检索](concepts/FTS5 全文检索.md)

- [时序知识图谱](concepts/时序知识图谱.md)

- [wake-up 协议](concepts/wake-up 协议.md)

- [MCP Server](concepts/MCP Server.md)

- [知识生命周期](concepts/知识生命周期.md)

- [wiki-mempalace-bridge](entities/wiki-mempalace-bridge.md)

- [FTS5 全文检索](concepts/FTS5 全文检索.md)

- [时序知识图谱](concepts/时序知识图谱.md)

- [wake-up 协议](concepts/wake-up 协议.md)
