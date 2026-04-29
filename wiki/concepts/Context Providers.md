---
title: Context Providers
type: concept
tags:
- 上下文管理
- 多Agent协作
status: 草稿
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/0f24483985aa4f71bd03a77221fed016
notion_id: 0f244839-85aa-4f71-bd03-a77221fed016
---

## 定义

Context Providers 是一种 Agent 架构模式，在主 Agent 和底层工具之间引入一层薄代理层。每个信息源（Slack、Drive、CRM 等）被封装为一个 Context Provider，仅向主 Agent 暴露两个标准化工具：`query_<source>`（自然语言读取）和 `update_<source>`（自然语言写入）。

## 关键要点

- **解决三大问题**：上下文污染（context pollution）、工具作用域重叠导致的性能退化、主 Agent 上下文被工具细节占据

- 每个 Context Provider 背后是一个子 Agent，该子 Agent 负责处理具体工具的所有细节（如 Slack 的用户查找、游标分页、thread 回复等）

- 主 Agent 的上下文不会被中间工具调用结果污染——这是相对 Skills 方案的核心优势

- Skills 方案的局限：虽然将任务知识按需加载，但工具和中间结果仍落在主 Agent 上下文中，加载 2 个带搜索能力的 Skill 就会导致 Agent 失效

- 支持多个 Context Provider 协作：query_slack 找讨论 + query_gdrive 找文档

- 路由逻辑极简，添加新工具不会引起回归

## 与 Skills 的区别

| 维度 | Context Providers | Skills |

| --- | --- | --- |

| 工具暴露 | 仅 query/update 两个 | 全部底层工具 |

| 中间结果 | 留在子 Agent | 污染主 Agent |

| 扩展性 | 添加不影响现有 | 2+ 模块冲突 |

## 来源引用

- [摘要：Meet Scout. The open-source company brain](summaries/摘要：Meet Scout. The open-source company brain.md)（[原文](https://x.com/ashpreetbedi/status/2049180168200106150)）
