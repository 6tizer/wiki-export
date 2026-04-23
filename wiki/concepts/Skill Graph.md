---
title: Skill Graph
type: concept
tags:
- 知识管理
status: 草稿
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/65d235b8d2094ed2b075ed2f4daf2b6a
notion_id: 65d235b8-d209-4ed2-b075-ed2f4daf2b6a
---

**定义**：Skill Graph 是一种将知识拆分为多个 markdown 文件并用 wikilinks 连成网络的知识组织模式，允许 Agent 像专家一样按需导航知识体系，而非一次注入全部内容。

**与 **[**SKILL.md**](http://skill.md/)** 的差异**

|  | 单一 [SKILL.md](http://skill.md/) | Skill Graph |

| --- | --- | --- |

| 容量 | 有限 | 无限 |

| 读取方式 | 全量注入 | 渐进式导航 |

| 适用场景 | 简单技能 | 复杂领域 |

**三个核心要素**

- **wikilinks**：嵌入正文告知 Agent 何时深入

- **YAML frontmatter**：扫一眼描述判断是否读全文

- **MOC（Map of Content）**：导航索引，在图谱变大时提供子话题导航

**渐进式披露工作流程**

1. Agent 先读 index 了解全局

1. 扫描 YAML frontmatter 筛选相关文件

1. 沿 wikilinks 跳转到具体内容

1. 只展开需要的章节

结果：10 万字知识库可能只需读 3000 字

**arscontexta**

该理念的具体实现，一个 249 个文件的 Claude Code 插件，教 Agent 怎么构建知识体系的知识体系。

**来源引用**

- [摘要：Skill Graph > SKILL.md 渐进式披露典范](summaries/摘要：Skill Graph  SKILL.md 渐进式披露典范.md)

- [摘要：A new way to think about composing skills to increase leverage: Skill Graphs 2.0](summaries/摘要：A new way to think about composing skills to increase leverage- Skill Graphs 2.0.md)（[原文](https://x.com/shivsakhuja/status/2047124337191444844)）

- [摘要：skills](summaries/摘要：skills.md)（[原文](https://x.com/garrytan/status/2047183884266402275)）

**关联概念**

- [原子-分子-化合物技能分层](concepts/原子-分子-化合物技能分层.md)

- [Sub agent 上下文隔离](concepts/Sub agent 上下文隔离.md)

- [Brain RAM 杠杆模型](concepts/Brain RAM 杠杆模型.md)
