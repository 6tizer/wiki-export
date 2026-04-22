---
title: 摘要：Polymarket 套利圣经：量化团队如何用数学基础设施提取 4000 万美元
type: summary
tags:
- Crypto/DeFi
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/959ea6ec52684792b6a4a595155e029b
notion_id: 959ea6ec-5268-4792-b6a4-a595155e029b
---

### 一句话摘要

Polymarket 套利的真正门槛不在交易动作，而在于用整数规划、Bregman 投影和 Frank-Wolfe 算法搭建可实时求解的数学基础设施。

### 关键洞察

- 预测市场中的套利机会往往来自跨市场逻辑依赖，而不是单个盘口的简单加法错误。

- 整数规划把指数级枚举压缩成可求解约束，是组合套利成立的基础。

- Bregman 投影和 Frank-Wolfe 算法让“理论无套利空间”变成可计算、可执行的交易目标。

- 真正决定收益上限的，除了模型，还有 VWAP、滑点和执行顺序等市场微观结构因素。

### 提取的概念

- [Polymarket](entities/Polymarket.md)

- [整数规划](concepts/整数规划.md)

- [Frank-Wolfe 算法](concepts/Frank-Wolfe 算法.md)

- [Bregman 投影](concepts/Bregman 投影.md)

### 原始文章信息

- 作者：RohOnChain

- 来源：X书签

- 发布时间：2026-03-12

- 链接：[原文](https://x.com/MrRyanChi/status/2031292099384008810)

### 个人评注

- 这类文章对 Tizer 的意义不在跟风交易，而在提醒我们：真正有壁垒的 Agent 工作流，底层通常是数学和执行基础设施，而不是表面自动化。
