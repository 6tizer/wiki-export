---
title: 摘要：DeepSeek V4永久降价！缓存命中再打1折，实测编程成本骤降83%
type: summary
tags:
- 推理优化
- 商业/生态
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b68813cb72ad6c486d33b37
notion_url: https://www.notion.so/Tizer/ee99b710736a4322a024e6c3ae9940ff
notion_id: ee99b710-736a-4322-a024-e6c3ae9940ff
---

## 一句话摘要

DeepSeek V4 在输入输出 2.5 折基础上，对缓存命中的输入 token 永久再打 1 折，实测 Agent 编程场景整体成本骤降 83%，开启新一轮 Token 价格战。

## 关键洞察

- **缓存命中永久降价**：输入缓存折扣无时限，研究员陈德里确认为永久降价，标记 #AGIforEveryone

- **实测成本骤降**：Agent 编程场景下 V4-Pro 缓存命中率约 95%–96%，3500 万 token 任务从 31.73 元降至约 5.34 元，整体节省 83%

- **输入远大于输出**：Agent 编程任务中输入 token 比例远高于输出，缓存命中定价使真实花费的绝大部分 token 享受最低价

- **V4-Pro 与 V4-Flash 差距极小**：缓存命中价格下，V4-Pro 每百万 token 只比 V4-Flash 贵 0.5 分钱

- **价格战三部曲**：2024 年 V3 降价引发第一轮 → R1 夜间折扣升温 → V4 折上折开启第三轮，对海外市场冲击力更大

## 提取的概念

- [DeepSeek V4](entities/DeepSeek V4.md)

- [缓存命中定价](concepts/缓存命中定价.md)

- [Token 价格战](concepts/Token 价格战.md)

## 原始文章信息

- **作者**：梦晨（量子位）

- **来源**：微信公众号 QbitAI

- **发布时间**：2026-04-27

- **链接**：[原文](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw%3D%3D&mid=2247886631&idx=2&sn=2678881a031fa59bfb08c1d237d2d98e&chksm=e9755c5e4b3a8ec6ed5dd523f8a8db6cc979f1e9a4acbef1e10d97b99a1c71f70532207be1e1#rd)

## 个人评注

缓存命中定价对 OpenClaw 等长上下文 Agent 系统的成本影响巨大。Agent 编程的多轮对话天然产生大量可复用前缀，95%+ 的缓存命中率意味着切换到 V4-Pro 几乎不增加成本却能获得更强模型。可据此优化 prompt 架构——将固定系统指令和上下文放在前缀、将变化部分后置——最大化缓存命中率。此外，华为算力部署后的进一步降价值得关注。
