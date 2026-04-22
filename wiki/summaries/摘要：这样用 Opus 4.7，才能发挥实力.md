---
title: 摘要：这样用 Opus 4.7，才能发挥实力
type: summary
tags:
- Coding Agent
- 记忆系统
status: 已审核
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: https://www.notion.so/346701074b6881c6bdf4fc5dc8f499ba
notion_url: https://www.notion.so/e222a86d7e3345bfbd5325287fd05868
notion_id: e222a86d-7e33-45bf-bd53-25287fd05868
---

## 一句话摘要

Opus 4.7 的“手感变化”并不是能力退化，而是 tokenizer、默认 effort、adaptive thinking 与长会话策略一起改变了 Claude Code 的默认行为；真正用好它的关键，是在首轮给足上下文，并主动管理长 session 的分叉、压缩与委派。

## 关键洞察

- Opus 4.7 的 token 计数方式变了，同样文本可能比 4.6 多出约 1 到 1.35 倍 token，但并不等于模型本身突然变贵。

- 默认 effort 从 high 提升到 xhigh 后，长任务和复杂编码场景会更稳，但也更容易出现“更慢、更烧 token”的主观感受。

- 4.7 默认更克制：回答长度更按任务复杂度变化，工具调用更少，spawn subagent 也更谨慎，所以旧的 4.6 prompt 和 harness 不能原样照搬。

- 1M context 不代表可以放任 session 无限变长；continue、rewind、compact、/clear 和 subagent 本质上是不同的上下文治理手段。

- 真正影响长任务体验的，不只是模型智力本身，而是是否及时清掉错误路径、无关调试噪声和不再需要的工具输出。

## 提取的概念

- [Claude Code](entities/Claude Code.md)

- [Claude Opus](entities/Claude Opus.md)

- [自适应思考](concepts/自适应思考.md)

- [Compaction](concepts/Compaction.md)

- [Context Rot](concepts/Context Rot.md)

- [Rewind](concepts/Rewind.md)

- [Subagents 并行](concepts/Subagents 并行.md)

## 原始文章信息

- 作者：赛博禅心

- 来源：微信

- 发布时间：2026-04-18 13:39

- 原文链接：[https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ==&mid=2247515662&idx=1&sn=bfcc64cdceb913aef59f697c1ecbfa8d&chksm=c3914681eabbc4c3c559e95297d8d5b85aebabf0c4c93a5d517e6784d086e7b7ff3aa9abee9e#rd](https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ%3D%3D&mid=2247515662&idx=1&sn=bfcc64cdceb913aef59f697c1ecbfa8d&chksm=c3914681eabbc4c3c559e95297d8d5b85aebabf0c4c93a5d517e6784d086e7b7ff3aa9abee9e#rd)

- 源文章页面：这样用 Opus 4.7，才能发挥实力

## 个人评注

这篇文章对 Tizer 当前的 Agent 使用方式很有参考价值：如果要把 Claude Code、OpenClaw 或内容生产流水线跑成长任务，不能只盯模型本身，而要把 prompt 当作执行合同，把 rewind、compact、subagent 这些机制当作工作流控制面。对 HITL 场景来说，这也意味着“什么时候让 Agent 继续”“什么时候强制换上下文”会直接决定稳定性和 token 成本。
