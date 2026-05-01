---
title: 摘要：AI 编程三大 SDD 工具深度对比（OpenSpec vs Superpowers vs GSD）
type: summary
tags:
- 代码生成
- 上下文管理
- 多Agent协作
- IDE 集成
- Agent 协作模式
status: 已审核
confidence: high
last_compiled: '2026-04-10'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c6043734a27f43f98556587155652d92
notion_id: c6043734-a27f-43f9-8556-587155652d92
---

## 一句话摘要

三个合计超 11 万 GitHub Stars 的开源项目（OpenSpec、Superpowers、GSD）标志着规范驱动开发（SDD）的兴起——在 AI 写代码之前先明确规范，分别解决「写什么」「怎么写」「怎么一直写好」三个不同层次的问题。

## 关键洞察

- **SDD 四阶段演进**：Copilot 补全 → Vibe Coding 一句话需求 → 质量危机 → SDD 用规范约束 AI，在自由和纪律间找平衡

- **三个工具定位**：OpenSpec（~27K⭐，轻量规范对齐层，解决「写什么」）、Superpowers（~61K⭐，完整方法论框架含强制 TDD，解决「怎么写」）、GSD（~23K⭐，子代理隔离解决上下文腐烂，解决「怎么一直写好」）

- **关键差异**：TDD 执行力（Superpowers 唯一强制，会删除测试前代码）、上下文管理（GSD 子代理隔离最优雅）、Spec Delta（OpenSpec 独有，无需看代码即可审查变更意图）

- **行业信号密集**：Martin Fowler 背书、GitHub 推 Spec Kit、AWS 发布 Kiro IDE

- **趋势判断**：SDD 将成 AI 编程标配；上下文工程是下一个基础设施瓶颈；第三方工具窗口期有限但先发者有标准制定权

## 提取的概念

- 规范驱动开发 SDD（新建 Wiki 条目）

## 原始文章信息

- **作者**：机智流 AI Insight 研究组

- **来源**：微信公众号

- **发布时间**：2026-03-02

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDgzMA%3D%3D&mid=2247555220&idx=2&sn=0f3bf03627bb2178e8ec7b3c93efd292)

## 个人评注

SDD 的核心理念「AI 代码的质量上限取决于输入的规范质量」与 Wiki Compiler 的 Schema 驱动编译完全对应。上下文腐烂问题在长对话场景中普遍存在，GSD 的子代理隔离思路可借鉴到多 Agent 协作架构中。三个工具可组合使用的设计理念值得参考。
