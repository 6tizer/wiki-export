---
title: 摘要：Claude Code 官方远程连接 Telegram 和 Discord 的操作流程。
type: summary
tags:
- 社交媒体
- OpenClaw
- AI 产品
status: 已审核
confidence: medium
last_compiled: '2026-04-11'
source_tags: Claude Code, 教程/实战
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f15b191f67444e4a955d07acdf7152de
notion_id: f15b191f-6744-4e4a-955d-07acdf7152de
---

**一句话摘要**：官方操作流程：创建机器人并配置 Token → 安装插件 → 启动命令 → 扫码/发配对码 → 锁定访问权限。

**关键洞察**

- **Telegram**: BotFather 创建机器人 Token → `/plugin install telegram@claude-plugins-official` → `/telegram:configure <token>` → 启动命令 → 发配对码 → 锁定访问决策

- **Discord**: 创建 Bot 获取 Token → 开启 Message Content Intent → 邀请 Bot 入服务器 → 安装插件 → 连接配对

- Claude Code Channels 提供官方支持的双向消息通道，是将 AI Agent 接入即时通讯的标准方案

**提取的概念**

- Claude Code Channels（Claude Code 官方远程消息层插件框架）

**原始文章信息**

- 作者：歸藏的AI工具筱 | 来源：微信公众号 | 发布时间：2026-03-20

- 链接：[https://mp.weixin.qq.com/s?__biz=MzU0MDk3NTUxMA==&mid=2247496189](https://mp.weixin.qq.com/s?__biz=MzU0MDk3NTUxMA%3D%3D&mid=2247496189)

**个人评注**

官方接入方案比社区野路子安全。对于 Tizer 将 OpenClaw/Claude Code 接入 Telegram/飞书等工作平台有直接实用价值。
