---
title: Lint Report 2026-04-13
type: lint-report
tags:
- Agent 协作模式
- 多Agent协作
- 知识管理
status: 草稿
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/27f4d0bf3ee44158bc7f54df00a5ea0f
notion_id: 27f4d0bf-3ee4-4158-bc7f-54df00a5ea0f
---

## 检查日期

2026-04-13（北京时间）

## 总体健康度

🟢 **86 / 100**

- 扣分明细：

  - 规范化近似重复 1 对：-10

  - 过时内容 1 个：-3

  - 引用结构化抽样中发现纯文本引用 9 个样本页：-1

- 说明：summary 同名重复共 1 组，未达到“每 10 组扣 1 分”的阈值

## 检查范围

| 指标 | 数量 |

| --- | --- |

| concept | 701 |

| entity | 345 |

| summary | 765 |

| synthesis | 43 |

| qa | 1 |

| 本轮跳过 | index、lint-report |

## 孤岛条目

- **高置信孤岛：0 个**

- 说明：本轮先做了标题命中初筛，并对近期候选做了正文搜索验证；未发现明确“未被任何 summary 提及”的高置信 concept / entity。

- 风险提示：旧 summary 正文中的结构化 `<mention-page>` 仍不完全统一，孤岛检测仍可能漏判。

## 过期草稿

- **0 个**

- 当前 concept / entity 中，未发现创建超过 7 天且仍处于「草稿」的条目。

## 过时内容

- [知识 Wiki 双轨系统方案：从 Notion 编译引擎到本地 Markdown 分发层](syntheses/知识 Wiki 双轨系统方案：从 Notion 编译引擎到本地 Markdown 分发层.md)

  - 类型：synthesis

  - 当前状态：草稿

  - 最后编译时间：为空

  - 建议：补齐最后编译时间，或重新编译后再进入后续状态流转

## 重复疑似

### A. 完全同名重复

- concept / entity：**0 对**

### B. 规范化后近似重复

- [Claude Skills](entities/Claude Skills.md) ↔ claude-skills

  - 原因：仅大小写与连字符差异，归一化后同名，属于高置信近似重复

### summary 同名重复检测

- **1 组** summary 完全同名重复

- `摘要：Latent Briefing: Efficient Memory Sharing for Multi-Agent Systems via KV Cache Compaction` × 2

  - [摘要：Latent Briefing: Efficient Memory Sharing for Multi-Agent Systems via KV Cache Compaction](summaries/摘要：Latent Briefing- Efficient Memory Sharing for Multi-Agent Systems via KV Cache Compaction.md)

  - 摘要：Latent Briefing: Efficient Memory Sharing for Multi-Agent Systems via KV Cache Compaction

## 状态异常

- **0 个**

- 未发现状态为空的非系统页面。

## 标签异常

- **缺失标签：0 个**

- **废弃标签命中：0 个**

### 标签分类合理性检查

- [Grok CLI](entities/Grok CLI.md)

  - 当前标签：Coding Agent, 开发工具

  - 问题：更像 AI 编程 Agent，本轮建议弱化或移除「开发工具」，保留「Coding Agent」

- [Page Agent](entities/Page Agent.md)

  - 当前标签：Agent 技能, 开发工具

  - 问题：更接近 Agent 能力层 / GUI Agent 能力，不建议长期放在「开发工具」桶里

## 标签分布统计

| 标签 | concept+entity 数量 |  |  |

| --- | --- | --- | --- |

| Agent 编排 | 168 | LLM | 152 |

| Agent 技能 | 150 | Coding Agent | 141 |

| Crypto/DeFi | 139 | 开发工具 | 124 |

| 商业/生态 | 120 | 工作流 | 115 |

| OpenClaw | 112 | 记忆系统 | 107 |

| 知识管理 | 84 | 安全/隐私 | 75 |

| Agent 框架 | 64 | 内容创作 | 45 |

## 标签分类合理性检查补充

- 当前高体量标签集中在 **Agent 编排 / LLM / Agent 技能 / Coding Agent / Crypto/DeFi / 开发工具**。

- 本轮 spot-check 未发现「缺标签」问题，但发现部分 AI Agent 产品仍混入「开发工具」标签，建议后续持续收敛。

## 类型分类检查

### concept → entity 候选

- [Hysteria 2](entities/Hysteria 2.md)

  - 原因：它是具体协议 / 产品名，更像实体档案而非抽象概念

- [openclaw infer CLI](entities/openclaw infer CLI.md)

  - 原因：它是 OpenClaw 体系中的具体 CLI 组件，更适合作为 entity 管理

### entity → concept 候选

- 本轮抽样未发现高置信 entity → concept 候选。

## 引用结构化检查

- 抽样范围：近期草稿 concept / entity 25 页

- 结构化引用页面：16 / 25（64%）

- 纯文本引用页面：9 / 25（36%）

| 指标 | 数量 | 比例 |

| --- | --- | --- |

| 结构化引用 | 16 | 64% |

| 纯文本引用 | 9 | 36% |

### 待修复页面（纯文本来源引用）

- [共识输出](concepts/共识输出.md)

- [交易员信任分](concepts/交易员信任分.md)

- [锁妖塔 Skill](entities/锁妖塔 Skill.md)

- [量化因子蒸馏](concepts/量化因子蒸馏.md)

- [KOL 交易经验蒸馏](concepts/KOL 交易经验蒸馏.md)

- [Claude Code Monitor 工具](concepts/Claude Code Monitor 工具.md)

- [Claude Code 动态循环](concepts/Claude Code 动态循环.md)

- [delegate_task](concepts/delegate_task.md)

- [Steer 机制](concepts/Steer 机制.md)

## 状态晋升建议

| 页面 | 当前状态 | 建议状态 | 原因 |

| --- | --- | --- | --- |

| 本轮无高置信自动晋升对象 | - | - | summary 已全部为「已审核」；草稿 concept/entity 中未发现创建超过 7 天的对象；旧 summary 的结构化引用尚未完全统一，暂不做批量「≥2 summary 交叉验证」晋升 |

## 改进建议

- **优先合并近似重复**：合并 [Claude Skills](entities/Claude Skills.md) 与 claude-skills，统一保留官方命名写法。

- **修复 summary 同名重复**：检查并合并两篇同名的 Latent Briefing 摘要，避免下游引用分叉。

- **批量升级纯文本引用**：优先修复上述 9 个页面的「来源引用」区块，把纯文本来源升级成 `<mention-page>`，避免知识图谱断链。

- **校正类型分类**：将 [Hysteria 2](entities/Hysteria 2.md)、[openclaw infer CLI](entities/openclaw infer CLI.md) 评估后迁移为 entity。

- **收敛标签体系**：从「开发工具」中逐步剥离 AI coding agent / GUI agent 类条目，避免标签桶继续膨胀。

>  请根据以上报告执行自动修复。
