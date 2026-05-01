---
title: 摘要：ClawWork AI 经济压力测试框架
type: summary
tags:
- 商业/生态
- OpenClaw
- 多Agent协作
- Agent 协作模式
status: 已审核
confidence: high
last_compiled: '2026-04-10'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/76f75a966cb042d093533a677fe5c862
notion_id: 76f75a96-6cb0-42d0-9353-3a677fe5c862
---

## 一句话摘要

ClawWork 是港大开源的 AI 经济压力测试框架，让 AI 以 10 美元启动资金在真实职业任务中「打工赚钱」，用经济指标衡量 AI 的实际工作能力。

## 关键洞察

- **经济压力测试范式**：AI 初始资金仅 10 美元，每次 API 调用都扣钱，必须通过完成真实工作任务赚回报酬，入不敷出即「破产」淘汰

- **GDPVal 真实职业任务**：基于 GDPVal 数据集的 220 个任务覆盖 44 个行业领域，报酬按美国劳工统计局时薪标准计算（$82.78-$5004/任务）

- **惊人的经济效率**：最顶尖 AI 员工时薪达 $1500+，7 小时赚 $10K，超越典型白领生产力

- **基于 Nanobot 的轻量架构**：继承 Nanobot 的 4000 行代码极简设计，pip install + 配置文件即可部署，支持 9 个通讯渠道集成

- **战略性工作/学习权衡**：Agent 每天需在「赚钱工作」和「投资学习」之间做出决策，模拟真实职业权衡

## 提取的概念

- ClawWork

- [GDPVal](concepts/GDPVal.md)

- Nanobot

- AI 经济压力测试

## 原始文章信息

- **作者**：开源星探

- **来源**：微信公众号

- **发布时间**：2026-02-18

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ%3D%3D&mid=2247505338&idx=1&sn=c879c8df8a497a8092dc8a68b5d8f7e0)

## 个人评注

与 OpenClaw 直接相关——ClawWork 基于 Nanobot 构建，而 Nanobot 正是复刻 OpenClaw 核心能力的项目。经济压力测试的范式为评估 Agent 实际价值提供了量化方法。ClawMode 集成器可将任意 Nanobot 实例变为「能赚钱的 AI 同事」，这对 OpenClaw 生态的商业化探索有直接启示。
