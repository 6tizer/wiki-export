---
title: Lint Report 2026-04-14
type: lint-report
tags:
- 知识管理
- 笔记工具
status: 草稿
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/b61d063fd584430fa36ba310c63dfc47
notion_id: b61d063f-d584-430f-a36b-a310c63dfc47
---

## 检查日期

2026-04-14

## 总体健康度

**80/100** 🟢

- 近似重复 2 对，共扣 20 分。

- 本轮未确认孤岛、过期草稿、过时内容、状态异常、缺失标签或弃用标签。

- 抽样 25 页中有 3 页存在纯文本来源引用，未达到额外扣分阈值。

## 孤岛条目

- 本轮未确认明确孤岛。

- 已反向检索验证：[记忆技术债](concepts/记忆技术债.md)、[GDPVal](concepts/GDPVal.md) 可在 summary 正文中被命中。

- 风险提示：summary 正文中的结构化引用覆盖仍不一致，当前孤岛检测采用保守判定。

## 过期草稿

- 无。当前未发现创建超过 7 天且仍为草稿的 concept / entity。

## 过时内容

- 无。当前未发现最后编译时间超过 30 天或为空的 concept / entity / summary。

## 重复疑似

### A. 完全同名重复

- 无。

### B. 规范化后近似重复

- [AI Hedge Fund](entities/AI Hedge Fund.md) ↔ ai-hedge-fund

  - 原因：大小写与连字符规范化后同名，且类型与标签不一致。

- [Everything Claude Code](entities/Everything Claude Code.md) ↔ everything-claude-code

  - 原因：大小写规范化后同名，疑似重复入库。

### summary 同名重复

- 无。

## 状态异常

- 无。当前未发现状态为空的 concept / entity。

## 标签异常

- 缺失标签：无。

- 弃用标签：无。

- 可能误分标签：

  - [Generative UI](concepts/Generative UI.md) 当前标签为 `内容创作`，更接近交互式 UI / Agent 能力概念，建议复核。

  - [A2UI 协议](concepts/A2UI 协议.md)、[Server-Driven UI](concepts/Server-Driven UI.md) 当前标签为 `开发工具`，更接近协议 / 方法论概念，建议复核。

## 标签分布统计

| 标签 | 数量 |

| --- | --- |

| LLM | 167 |

| Coding Agent | 153 |

| 商业/生态 | 127 |

| 工作流 | 118 |

| 记忆系统 | 111 |

| 知识管理 | 84 |

| 内容创作 | 49 |

## 引用结构化检查

| 指标 | 结果 | 抽样页数 | 25 |

| --- | --- | --- | --- |

| 含结构化引用的页面 | 23 | 含纯文本引用的页面 | 3 |

| 结构化页面占比 | 92% | 含纯文本页面占比 | 12% |

### 待修复页面

- [Deep Research](entities/Deep Research.md)：来源引用区块混用了纯文本摘要名与结构化页面引用。

- [多步骤研究规划](concepts/多步骤研究规划.md)：来源引用区块仅为纯文本摘要名。

- [AI 自修改代码](concepts/AI 自修改代码.md)：来源引用区块仅为纯文本文章标题。

## 状态晋升建议

| 页面 | 当前状态 | 建议状态 | 原因 | — | — | — | 本轮未发现满足晋升条件的条目。summary 已全部为“已审核”，草稿 concept / entity 也未出现创建满 7 天且内容完整的页面。 |

| --- | --- | --- | --- | --- | --- | --- | --- |

## 改进建议

1. **优先处理近似重复**

  - 统一裁决 [AI Hedge Fund](entities/AI Hedge Fund.md) 与 ai-hedge-fund 的保留页、类型与标签。

  - 合并 [Everything Claude Code](entities/Everything Claude Code.md) 与 everything-claude-code，避免重复维护。

1. **修复来源引用结构化断层**

  - 优先补齐 [Deep Research](entities/Deep Research.md)、[多步骤研究规划](concepts/多步骤研究规划.md)、[AI 自修改代码](concepts/AI 自修改代码.md) 的 `<mention-page>` 来源链接。

1. **复核标签分类**

  - 优先检查 Generative UI、A2UI 协议、Server-Driven UI 的标签是否与方法论 / 协议属性一致。

>  请根据以上报告执行自动修复。
