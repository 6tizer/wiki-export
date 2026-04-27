---
title: 摘要：源码被开源，Claude Code之父回应了：纯内部开发者手滑
type: summary
tags:
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-28'
source_tags: Claude Code, 行业观察
source_article_url: ''
notion_url: https://www.notion.so/aef689f92616486088a4951ffdcf21b0
notion_id: aef689f9-2616-4860-88a4-951ffdcf21b0
---

**一句话摘要**：Anthropic 因工程失误意外泳露 Claude Code 51 万行 TypeScript 源码，社区展开深度解读揭示其内部设计（反蘑馏机制、KAIROS、占卢模式等），并引发开源社区大量改写迭代。

---

## 关键洞察

- **泳露原因**：发布 npm 包时未剪除 source map 文件，导致完整 TypeScript 源码被还原

- **反蘑馏机制**：在模型输出流中注入伪造工具调用+将工具调用简化为类别统计，防止竞争对手利用数据训练

- **KAIROS**：Anthropic 内部代号，即亲生龙虾项目，具备心跳机制、autoDream、主动推送、PR 订阅等全功能

- **Auto Dream**：后台记忆整合流程，复盘历史会话内容压缩整理为结构化 [MEMORY.md](http://memory.md/)

- **Prompt 缓存精细化管理**：`promptCacheBreakDetection.ts` 对每次 API 调用的多项进行哈希对比，驱动缓存复用最大化

- **社区反应**：24 小时内 claw-code（Python 改写）创 GitHub 屯 star 增长速度历史记录（2 小时 50k）

## 提取的概念

- KAIROS

- 反蘑馏机制

## 原始文章信息

- **作者**：机器之心

- **来源**：微信公众号

- **发布日期**：2026-04-01

- **链接**：[https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2651024976&idx=1](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651024976&idx=1)

## 个人评注

KAIROS 的设计与 OpenClaw 的心跳机制高度类似。反蘑馏机制和 Prompt 缓存精细管理对了解 Claude Code 内部设计有重要参考意义。
