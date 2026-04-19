---
title: MemBrain
type: entity
tags:
- 记忆系统
status: 审核中
confidence: high
last_compiled: '2026-04-19'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/0d1e66971fe643b987b917aef9c1daf5
notion_id: 0d1e6697-1fe6-43b9-87b9-17aef9c1daf5
---

## 定义

MemBrain是Feeling AI开发的Agentic原生记忆系统，在LoCoMo/LongMemEval/PersonaMem-v2等当前主流记忆基准评测中刷新SOTA。其核心是自适应实体树算法，尝试同时保留语义保真和显式关联。

## 与主流方案的对比

| 方案 | 语义保真 | 显式关联 | 缺陷 |

| --- | --- | --- | --- |

| 纯文本（OpenClaw式） | 高 | 少 | 将决策全交给LLM，成本高，无法溯源审计 |

| 图结构（Graphiti） | 低 | 高 | LLM无法深度参与检索，语义损耗 |

| **MemBrain** | **高** | **高** | 自适应实体树，层级结构 |

## 自适应实体树算法

- 以实体为根节点，Agent自动按主题聚类为中间层，原子事实为叶节点

- 每条原子事实含带别名指向实体，内容完整不拆分，可动态替换为实体最新描述（「可渲染模板」）

- 少于阈值时保持平坦结构，积累到阈值后由聚类Agent自动升级为层次结构

- 写入层：事实抽取→实体消解→结构更新（多工作流水线）

- 检索层：渐进式策略——普通查询用并行检索，复杂查询启用多查询扩展，跨实体查询开启Agentic模式

## 分层原则

> Agent的判断力被精确地用在它最擅长的地方——判断信息够不够、缺什么、怎么补——而不是去操心底层的索引和排序。

先验的工程结构承担80%的重活，Agent的智能聚焦在真正需要判断的20%上。

## 性能数据

### MemBrain 1.5（最新版本）

- 召回率达 **96.6%**

- KnowMeBench Level III 比现有结果大幅提升超 300%

- LoCoMo / LongMemEval / PersonaMem-v2 刷新 SOTA，反超 MemOS、Zep 和 EverMemOS

### 配套系统

与 **CodeBrain-1**（任务执行优化）配套，共同构成 Feeling AI 的“最强大脑”组合，目标是让 Agent 从“工程师助手”升级为“可信赖的交付专家”

## 开源地址

[https://github.com/feelingai-team/MemBrain](https://github.com/feelingai-team/MemBrain)

## 来源引用

- [摘要：最强大脑组合！全球SOTA的逻辑和记忆CodeBrain-1&MemBrain1.5同时开源](summaries/摘要：最强大脑组合！全球SOTA的逻辑和记忆CodeBrain-1&MemBrain1.5同时开源.md)（机器之心，2026-04-08）
