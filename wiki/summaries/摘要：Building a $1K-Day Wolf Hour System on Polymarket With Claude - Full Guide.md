---
title: 摘要：Building a $1K/Day Wolf Hour System on Polymarket With Claude - Full Guide
type: summary
tags:
- Crypto/DeFi
- 工作流
status: 已审核
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: https://www.notion.so/348701074b6881798763fb9fc8b6dd04
notion_url: https://www.notion.so/636972bb615845799c71fffda19b9fc5
notion_id: 636972bb-6158-4579-9c71-fffda19b9fc5
---

## 一句话摘要

这篇文章提出一种“Wolf Hour”夜间交易框架：白天先用 Claude 辅助做 Polymarket 合约的公允价值研究与目标价设定，凌晨只让系统监控是否出现极端价差，等到流动性恢复后再退出，以捕捉结构性错价。

## 关键洞察

- 真正的优势不在凌晨做被动做市，而在白天先建模、夜间只执行预设条件的方向性入场。

- “Wolf Hour”的机会来自 02:30–04:00 UTC 的流动性真空：零售交易者休息、做市机器人收窄活跃度、个人套利系统停机，导致中等热度合约的价差显著放大。

- 宽价差并不等于安全收益；在薄市场里，逆向选择风险更高，任何主动成交都可能是在和掌握新信息的一方交易。

- 策略依赖三件事同时成立：白天得出可信的公允价值估计、只监控既定观察名单、并把仓位控制在正常规模的 30–50%。

- 退出必须在伦敦开盘或美盘活跃时段完成；策略赚的不只是基本面判断，还包括流动性恢复带来的价差压缩。

## 提取的概念

- [Polymarket](entities/Polymarket.md)

- [预测市场](concepts/预测市场.md)

- [Wolf Hour](concepts/Wolf Hour.md)

- [逆向选择](concepts/逆向选择.md)

## 原始文章信息

- 作者：@SolSt1ne

- 来源：X书签

- 发布时间：2026-04-13

- 原文链接：[https://x.com/SolSt1ne/status/2043685450070831212](https://x.com/SolSt1ne/status/2043685450070831212)

- 源文章页：Wolf Hour：用 Claude 在 Polymarket 凌晨流动性真空中抓取结构性套利机会

## 个人评注

这类方法最值得借鉴的不是“Claude 帮你交易”，而是把研究、监控、执行拆成不同阶段：白天由人和模型一起做判断，夜间只让自动化系统检查阈值并执行既定剧本。对 Tizer 的内容/Agent 工作流来说，这种“先定义边界，再自动执行”的 HITL 思路，比追求 Agent 临场自主判断更稳健。
