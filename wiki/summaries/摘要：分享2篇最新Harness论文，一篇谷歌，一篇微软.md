---
title: 摘要：分享2篇最新Harness论文，一篇谷歌，一篇微软
type: summary
tags:
- Harness 工程
- 长期记忆
status: 已审核
confidence: high
last_compiled: '2026-04-25'
source_tags: ''
source_article_url: https://www.notion.so/34d701074b6881cfa4e7fcacf5fb0535
notion_url: https://www.notion.so/Tizer/ebf393d9facb4844bcc859b7a0bddf4b
notion_id: ebf393d9-facb-4844-bcc8-59b7a0bddf4b
---

## 一句话摘要

这篇文章以微软的 M⋆ 和谷歌的 AutoHarness 为例，说明 Agent 研究正在从单纯提升模型能力，转向为不同任务自动进化更合适的 Harness，包括记忆结构与动作约束两类系统层设计。

## 关键洞察

- M⋆ 将记忆 Harness 表达为可执行的 Python 记忆程序，把记忆结构的设计问题转成可迭代优化的程序搜索问题。

- 不同任务需要不同的记忆结构，跨任务迁移效果不佳，说明记忆 Harness 必须与任务协同优化。

- AutoHarness 把动作约束的生成视为代码搜索问题，用树搜索和 Thompson 采样自动生成、修复并优化合法动作验证器。

- 专用 Harness 不只是“防错层”，还会直接影响任务表现，甚至能让较小模型在部分场景击败更大模型。

- 自进化 Agent 的关键正在从“把模型做得更聪明”转向“把系统层的记忆、验证与修复循环做得更合适”。

## 提取的概念

- [Harness Engineering](concepts/Harness Engineering.md)

- [M⋆](concepts/M⋆.md)

- [AutoHarness](concepts/AutoHarness.md)

- [Reflective Code Evolution](concepts/Reflective Code Evolution.md)

- [Population-based Search](concepts/Population-based Search.md)

- [Harness-as-Policy](concepts/Harness-as-Policy.md)

## 原始文章信息

- 作者：数据派THU

- 来源：微信 / PaperAgent

- 发布时间：2026-04-25 17:02（Asia/Shanghai）

- 原文链接：[查看原文](https://mp.weixin.qq.com/s?__biz=MzI1MjQ2OTQ3Ng%3D%3D&mid=2247665936&idx=1&sn=3a22066240ebfea5f456ecfaa39e9892&chksm=e8c800edc26b20940eeca6d9cd263fa15ef276abf030f9a15cb64f86fb2ee59005c2588a8a9d#rd)

- 源文章页：分享2篇最新Harness论文，一篇谷歌，一篇微软

## 个人评注

- 对 Tizer 的启发是，OpenClaw 或内容流水线里的 Agent 不应追求单一通用记忆或约束方案，而应把任务记忆结构、验证器和修复循环做成可演化的 Harness 层。

- 这也说明 HITL 与自动验证并不冲突：先让系统层约束兜底，再把人工审核放在高价值节点。
