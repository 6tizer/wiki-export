---
title: 摘要：我只想说一句，这文章太tm牛逼了！
type: summary
tags:
- 量化交易
- 加密资产
status: 已审核
confidence: high
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: https://www.notion.so/355701074b68810ca9aef0f3870d4434
notion_url: https://www.notion.so/Tizer/bec09b7d67864a5ea374c28e39ae2c91
notion_id: bec09b7d-6786-4a5e-a374-c28e39ae2c91
---

## 一句话摘要

通过拆解 $MYX 和 $COAI 两个做市商操盘案例，揭示加密市场做市商从隐蔽建仓到挤仓清算再到反手出货的完整收割五阶段模型及实战检测信号。

## 关键洞察

- **五阶段挤仓模型**：Setup（微型买入+LP注资隐蔽建仓）→ Bait（暴力拉盘诱空）→ Trap（横盘一个月养空，资金费率每4小时-2%）→ Squeeze（连锁清算推动价格飙升）→ Exit（反手做空+转CEX出货）

- **低流通量是操纵前提**：MYX TGE 仅 9.21% 解锁，COAI 19.65%，70-90% 锁仓意味着少量资金即可控盘

- **Binance Futures 是终极武器**：杠杆清算瀑布是做市商的核心收割机制，MYX 单日清算 $1653 万（其中空头 $1368 万）

- **五大挤仓检测信号**：资金费率方向、OI 与价格关系、Taker Ratio、链上大额转 CEX 行为、订单簿异常（bid-ask 失衡 >0.4）

- **协调钱包集群**：Bubblemaps 在 COAI 案例中抓到 60 个钱包被同一地址同时注入 1 BNB 的自动化控盘证据

## 提取的概念

- [做市商挤仓](concepts/做市商挤仓.md)

- [OI Brushing](concepts/OI Brushing.md)

- [Bubblemaps](entities/Bubblemaps.md)

## 原始文章信息

- **作者**：@0xKevin00（整理翻译）；原文作者 @tradinghoex

- **来源**：X 书签

- **发布时间**：2026-05-02

- **链接**：[原文推文](https://x.com/0xKevin00/status/2050478908462805171)

## 个人评注

这篇做市商操盘案例拆解对 Tizer 的量化交易和链上分析工作流有直接参考价值。五阶段模型和挤仓读表五信号可作为跟庄策略的实战框架——特别是资金费率、OI 变化和 Taker Ratio 这三个指标，可以被集成到交易监控工具中做实时预警。Bubblemaps 和 Arkham 等链上分析工具的组合使用方式也值得纳入 OpenClaw 的数据源评估清单。
