---
title: AiPy / Python-Use
type: concept
tags:
- OpenClaw
- 工作流
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/52607b5ac2ca4d35be07374044a63315
notion_id: 52607b5a-c2ca-4d35-be07-374044a63315
---

## 定义

AiPy / Python-Use 是一种 AI Agent 执行架构模式：LLM 负责任务规划和生成 Python 代码，Python 解释器负责实际执行，通过「Task → Plan → Code → Execute → Feedback」循环完成任务。代表实现是 AiPy 项目。

GitHub: [https://github.com/knownsec/aipyapp](https://github.com/knownsec/aipyapp)

## 核心理念：Code is Agent

- 不需要 MCP、Workflow 编排、Tools 注册——Python 本身就是协议和接口

- LLM 做规划和写代码（最擅长的），Python 做执行（精确无幻觉）

- 去中间层：直接用 Python 连接模型和真实世界，避免 MCP 等复杂抽象层

- Python 生态（pandas/beautifulsoup/matplotlib/各厂商 SDK）覆盖几乎所有场景

## 解决的问题

- OpenClaw Skill 高 Token 消耗：Python 执行不消耗 Token

- MD 规则描述导致的幻觉：Python if-else 精确表达，结果确定性高

- 工具覆盖范围限制：Python 生态覆盖几乎所有场景

## 与 OpenClaw Skill MD 文档的对比

|  | MD Skill | Python Skill |

| --- | --- | --- |

| Token 消耗 | 高 | 低 |

| 准确性 | 依赖 LLM 理解 | 确定性代码 |

| 可审计 | 难 | 代码可审查 |

## 执行流程

1. 用户给任务

1. LLM 规划步骤

1. LLM 为每步生成 Python 代码

1. Python 执行，结果反馈给 LLM

1. 如报错，LLM 自修复代码，循环直到完成

1. 可沉淀为 Skill，下次直接用 Python 脚本执行

## 来源引用

- [摘要：终于明白为什么 Skill 不好用了](summaries/摘要：终于明白为什么 Skill 不好用了.md)
