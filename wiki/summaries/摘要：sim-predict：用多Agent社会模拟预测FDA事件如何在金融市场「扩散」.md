---
title: 摘要：sim-predict：用多Agent社会模拟预测FDA事件如何在金融市场「扩散」
type: summary
tags:
- 量化交易
- 多Agent协作
- Agent 协作模式
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/06aad9b416ed45bc8a1c875dbdf5ca59
notion_id: 06aad9b4-16ed-45bc-8a1c-875dbdf5ca59
---

### 一句话摘要

sim-predict 试图用多 Agent 社会模拟去预测 FDA 事件在金融市场中被逐步消化的速度，而不仅仅是价格方向。

### 关键洞察

- 项目把“alpha 来自信息扩散速度”作为核心问题，而不是传统的涨跌预测。

- 它以 [OASIS](concepts/OASIS.md) 做社会模拟引擎，再用 [autoresearch](entities/autoresearch.md) 式循环持续调参。

- 当前结果里，传播曲线形状匹配度高，但绝对时间预测仍有明显提升空间。

- 这种方法的价值在于把市场参与者的信息传导过程显式建模，而不是只做事件分类与情绪打分。

### 提取的概念

- [sim-predict](entities/sim-predict.md)

- [OASIS](concepts/OASIS.md)

- [autoresearch](entities/autoresearch.md)

### 原始文章信息

- 作者：wangray

- 来源：X书签

- 发布时间：未明确

- 链接：[原文](https://x.com/wangray/status/2031312140788023421)

### 个人评注

这类“先模拟传播机制，再评估结果”的思路，对 Tizer 后续做 Agent 投研、叙事扩散追踪和内容信号排序都很有启发，尤其适合接到 OpenClaw 的自动研究流水线中。
