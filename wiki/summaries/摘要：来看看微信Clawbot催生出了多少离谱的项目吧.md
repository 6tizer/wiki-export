---
title: 摘要：来看看微信Clawbot催生出了多少离谱的项目吧
type: summary
tags:
- OpenClaw
status: 已审核
confidence: medium
last_compiled: '2026-04-11'
source_tags: 微信生态, OpenClaw, 开源项目
source_article_url: ''
notion_url: https://www.notion.so/d6f143df32ba4bdaa298842c5aa3c40c
notion_id: d6f143df-32ba-4bda-a298-842c5aa3c40c
---

**一句话摘要**：微信 ClawBot 推出一天内就炸出三个增强项目（weclaw/vibe-remote/wechatbot），加上已有上千万用户体量的各龙虾变体，微信正在成为最大 AI Agent 入口。

**关键洞察**

- weclaw：支持图片、语音、主动推送消息，可接 OpenClaw/Claude Code/Codex/Cursor 等终端 Agent，通过子命令 (/cc /gm /oc) 指定应用

- ACP 协议： Claude Code、Codex 等终端 Agent 已实现 ACP，只需部署一个桥接服务就可接入微信

- 理论上可以调度任何 Agent：让 Manus 出调研报告、让美团 Agent 点外卖、让携程 Agent 订机票

- 前提：被接入的 Agent 实现 ACP 协议或开放接口

**原始文章信息**

- 作者：卡尔的AI沃茨 | 来源：微信公众号 | 发布时间：2026-03-23

- 链接：[https://mp.weixin.qq.com/s?__biz=Mzg3MTk3NzYzNw==&mid=2247505794](https://mp.weixin.qq.com/s?__biz=Mzg3MTk3NzYzNw%3D%3D&mid=2247505794)

**个人评注**

这篇文章展示了开源社区的快速迭代能力。ACP 协议是关键：如果 Tizer 能将所有工具都按照 ACP 协议封装，就能通过微信 ClawBot 统一调度。
