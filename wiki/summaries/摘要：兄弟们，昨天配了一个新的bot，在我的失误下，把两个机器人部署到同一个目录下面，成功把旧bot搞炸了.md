---
title: 摘要：兄弟们，昨天配了一个新的bot，在我的失误下，把两个机器人部署到同一个目录下面，成功把旧bot搞炸了
type: summary
tags: []
status: 已审核
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b68814ca7a3c8abf9e11ab4
notion_url: https://www.notion.so/Tizer/7ec2c327e93a4d078367f4ec205ab883
notion_id: 7ec2c327-e93a-4d07-8367-f4ec205ab883
---

### 一句话摘要

这篇文章通过一次 Hermes + Telegram Bot + Codex 部署翻车案例，总结出一套更可靠的链路排障方法：不要迷信配置或模型自报，而要通过进程清理、token 重置、假模型注错和真实任务测试来验证整条调用链。

### 关键洞察

- 真正的问题往往不在模型配置本身，而在消息是否真的被目标服务接管

- 多个旧进程共用同一目录或同一 token，会让排障出现“看起来改了但始终不生效”的假象

- `getWebhookInfo` 返回空 webhook 也不能排除后台 polling 进程在抢消息

- 当怀疑 token 已被旧环境污染时，最省时间的办法通常不是继续排查，而是直接 `/revoke` 后更换新 token

- 判断模型是否切换成功，应该看端到端错误与任务输出，而不是问 Bot “你现在是什么模型”

### 提取的概念

- [Hermes Agent](entities/Hermes Agent.md)

- [Codex](entities/Codex.md)

- [OpenRouter](entities/OpenRouter.md)

- [调用链验证](concepts/调用链验证.md)

- [假模型测试](concepts/假模型测试.md)

- [Token 污染](concepts/Token 污染.md)

- [Polling 抢消息](concepts/Polling 抢消息.md)

### 原始文章信息

- 作者：@AnchorNode

- 来源：X书签

- 发布时间：2026-04-16

- 原文链接：[https://x.com/AnchorNode/status/2044675901775126986](https://x.com/AnchorNode/status/2044675901775126986)

### 个人评注

这篇内容对 Tizer 的 Agent 工作流很有参考价值。它本质上不是在讲单点配置，而是在讲 **生产环境里的链路验收方法**。对于 Hermes、OpenClaw、Telegram Bot 这类多组件串联系统，部署后的第一件事不该是“问模型是谁”，而应该是验证消息入口、token 占用、provider 路由和真实任务输出是否一致。这个思路很适合沉淀为后续内容管线或 HITL 发布前的排障清单。
