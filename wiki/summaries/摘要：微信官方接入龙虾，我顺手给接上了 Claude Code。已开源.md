---
title: 摘要：微信官方接入龙虾，我顺手给接上了 Claude Code。已开源
type: summary
tags:
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: 微信生态, OpenClaw, Claude Code
source_article_url: ''
notion_url: https://www.notion.so/647373e795f342d69e99398db8c9e6c4
notion_id: 647373e7-95f3-42d6-9e99-398db8c9e6c4
---

**一句话摘要**：微信官方推出 ClawBot 插件，通过 iLink 协议提供安全的官方管道；作者通过读取官方源码并应用 Claude Code Channels，5 分钟实现了将微信接入 Claude Code 的开源方案。

**关键洞察**

- 微信官方 ClawBot 插件适用 iLink 协议：长轮询撤息 + Token 认证 + context_token 关联对话

- 这套接口和接的是什么 AI 没有关系，它只是一个消息通道：微信把用户消息送过来，你把回复送回去

- 作者读了官方 npm 包源码，应用 Claude Code Channels MCP 调通微信和 Claude Code，300 行代码

- 实现效果：微信发消息→Claude Code 处理→微信收到回复，彻底跨设备遊控

- 定位：微信给 OpenClaw 开了一扇门，这个项目就是让 Claude Code 秉着虎皮从同一扇门走进去

**提取的概念**

- ClawBot（微信官方 AI Agent 接入插件。iLink 协议）

- Claude Code Channels（已创建词条）

**原始文章信息**

- 作者：AGI Hunt | 来源：微信公众号 | 发布时间：2026-03-22

- 链接：[https://mp.weixin.qq.com/s?__biz=MzA4NzgzMjA4MQ==&mid=2453481779](https://mp.weixin.qq.com/s?__biz=MzA4NzgzMjA4MQ%3D%3D&mid=2453481779)

**个人评注**

展示了如何通过逐开官方插件源码快速实现开发的过程。对 Tizer 跨平台工作流有参考价值：手机遊控本地 Agent 局域内可能是最配序完备的方案。
