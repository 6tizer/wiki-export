---
title: Dreaming 记忆机制
type: concept
tags:
- 知识管理
- 长期记忆
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-24'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/622354f2354244b2a32d3eb457e0d095
notion_id: 622354f2-3542-44b2-a32d-3eb457e0d095
---

## 定义

Dreaming 记忆机制是 OpenClaw 2026.4.5 版本引入的后台记忆巩固机制，也常被称为 OpenClaw Dreaming，模拟人类睡眠的三阶段（浅睡/REM/深睡）对 AI 的短期记忆进行自动整理和提炼，将「持久真相」写入长期记忆文件。

## 核心机制

三阶段循环：

1. **浅睡眠（Light）**：筛选和整理近期短期记忆

1. **REM阶段**：提取主题和反思性信号

1. **深度睡眠（Deep）**：决定哪些记忆值得永久保留，[写入MEMORY.md](http://xn--memory-2l2jmn.md/)

六个加权评分信号（权重从高到低）：

- 相关性（0.30）> 频率（0.24）> 查询多样性 > 时效性 > 复现强度 > 概念丰富度

**设计理念**：相关性高于频率——更看重「在不同场景下被反复检索」，而非简单出现次数。

## 使用方式

```javascript
/dreaming on   开启
/dreaming off  关闭
/dreaming status  查看状态
```

默认每天凌晨3点自动执行完整扫描。Gateway Dreams标签页可查看短期/长期记忆数量、本日提升数、下次扫描时间。

## 技术来源

灵感来源于Claude Code泄露源码（51.2万行TypeScript）中隐藏的KAIROS/autoDream机制，其三门触发机制为：时间门（距上次24小时+）→ 会话门（5次会话+）→ 锁门（排他锁防并发）。

## 关键要点

- 多语言支持：中文对话产生的记忆无需翻译即可参与评分

- 命令行用户可手动触发：`openclaw memory promote --apply`

- 支持查询记忆未被提升的原因（`promote-explain`）

- 与 MemBrain1.5、MemPalace 等方案相比，Dreaming 更强调定时触发、透明可查的三阶段记忆巩固流程

## 与竞品对比

| 系统 | 触发方式 | 架构 | 特点 |

| --- | --- | --- | --- |

| OpenClaw Dreaming | 定时 + 命令 | 三阶段 | 透明可查 |

| MemBrain1.5 | 实时 | 实体树 | 召回优先 |

| MemPalace | 被动 | 五层 | 完整性优先 |

## 来源引用

- [摘要：Anthropic 封杀 48 小时，逼出 OpenClaw 最强反击！龙虾首次会生视频了](summaries/摘要：Anthropic 封杀 48 小时，逼出 OpenClaw 最强反击！龙虾首次会生视频了.md)（新智元，2026-04-07）

- [摘要：Openclaw 龙虾五天五连，24小时两更，火力全开！到底更新了些什么？](summaries/摘要：Openclaw 龙虾五天五连，24小时两更，火力全开！到底更新了些什么？.md)

- [摘要：OpenClaw 2026.4.5：被 Anthropic 断供后，这只龙虾进化得更猛了](summaries/摘要：OpenClaw 2026.4.5：被 Anthropic 断供后，这只龙虾进化得更猛了.md)

- 摘要：I Went Through Every AI Memory Tool I Could Find. There Are Two Camps.

## 关联概念

- [grounded REM backfill](concepts/grounded REM backfill.md)

- [Active Memory 插件](entities/Active Memory 插件.md)

- [Memory Wiki](concepts/Memory Wiki.md)

- [OpenClaw](entities/OpenClaw.md)

- [上下文基底](concepts/上下文基底.md)

- [Context Engineering](concepts/Context Engineering.md)
