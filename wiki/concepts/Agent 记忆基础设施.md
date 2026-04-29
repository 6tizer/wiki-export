---
title: Agent 记忆基础设施
type: concept
tags:
- 长期记忆
- 上下文管理
status: 草稿
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/6935bd11c034482aa8534cbe69475440
notion_id: 6935bd11-c034-482a-a853-4cbe69475440
---

## 定义

Agent 记忆基础设施是一种设计理念：当记忆系统的用户从人类变为自主运行的 Agent 时，记忆不再是「笔记本」，而是需要按基础设施级别工程化设计的系统组件。人类第二大脑优化可读性、浏览和反思，而 Agent 记忆优化快速检索、持久状态、低 Token 开销、冲突解决和可靠更新——两者是不同的工作负载。

## 核心原则

- **选择性注入（Selective Injection）**：只有相关记忆进入上下文，其余留在存储层

- **结构化检索（Structured Retrieval）**：Agent 应能查询最新偏好、任务状态、相关决策，而非「读笔记后推断」

- **记忆评分（Scoring）**：每条记忆需元数据——置信度、新鲜度、重要性、强化次数

- **冲突解决（Conflict Resolution）**：两条事实矛盾时需规则：更新优先 / 高置信优先 / 询问用户

- **记忆衰减（Decay）**：部分记忆应弱化、过期或归档；全部等权记忆最终导致检索质量下降

## 与人类知识库的区别

| 维度 | 人类第二大脑 | Agent 记忆基础设施 |

| 优化目标 | 可读性、浏览、反思 | 快速检索、低 Token、持久状态 |

| 更新频率 | 偶尔手动 | 每次任务/对话/工具调用后 |

| 格式 | Markdown / 笔记 | 结构化事实、实体、关系、时间戳 |

| 检索粒度 | 整页文档 | 单条事实 |

| 冲突处理 | 人工判断 | 自动规则 |

## 最佳实践：混合架构

- **Markdown 面向人类**：笔记、报告、身份文件、日志

- **结构化存储面向 Agent**：事实、实体、关系、偏好、任务状态、索引、时间戳、评分

- Markdown 作为界面，结构化记忆作为底层——这是实用方向

## 关联概念

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [Mercury](entities/Mercury.md)

- [CerebroCortex](entities/CerebroCortex.md)

- [ACT-R 激活模型](concepts/ACT-R 激活模型.md)

- [FSRS-6](concepts/FSRS-6.md)

## 来源引用

- [摘要：Why Karpathy's Second Brain Breaks at Agent Scale. How Mercury Solves It.](summaries/摘要：Why Karpathy's Second Brain Breaks at Agent Scale. How Mercury Solves It.md)（[原文](https://x.com/Ctrl_Alt_Zaid/status/2049082538686382397)）

- [摘要：Mercury asks first — and remembers what matters.](summaries/摘要：Mercury asks first — and remembers what matters.md)（[原文](https://x.com/AYi_AInotes/status/2049318687065174449)）
