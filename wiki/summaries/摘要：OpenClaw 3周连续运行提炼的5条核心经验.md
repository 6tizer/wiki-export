---
title: 摘要：OpenClaw 3周连续运行提炼的5条核心经验
type: summary
tags:
- OpenClaw
- 长期记忆
- Agent 协作模式
status: 已审核
confidence: medium
last_compiled: '2026-04-10'
source_tags: OpenClaw, Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/fbf0f34efff9480f9c05cd60522562a7
notion_id: fbf0f34e-fff9-480f-9c05-cd60522562a7
---

## 一句话摘要

结构化记忆 + 成本分层 + 规则工程 + 主动调度 + 防御性架构，是 OpenClaw 长期运行的五条核心经验。

## 关键洞察

- **结构化记忆**：Projects→Areas→Resources→Archives + 语义搜索，一下午从混乱升级到结构化召回

- **成本分层**：廉价模型做监控/调度，顶级模型留给写作/研究/判断

- **规则工程**：“Be helpful”无效，必须写具体可验证规则，每次失误转化为新规则

- **主动调度**：13 个 cron 定时任务，Agent 主动推送而非被动等待

- **防御性架构**：不“请求”AI不泄露密钥，而是让泄露在技术上不可能（Keychain + pre-commit hook + sed 脱敏）

## 原始文章信息

- **作者**：AI 启蒙小伙伴

- **发布时间**：2026-03-03

- **链接**：[原文](https://mp.weixin.qq.com/s?__biz=MzkwNDExODE4Nw%3D%3D&mid=2247495730&idx=1&sn=f4009641060dee3c56ebb1da657d24db)

## 个人评注

五条经验与已有概念高度对应：记忆分层架构、Agent 成本控制、Cron 自动化、Agent 可观测性。「希望不是安全策略」这一点与 22 万实例暴露文章相呼应。
