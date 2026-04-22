---
title: 摘要：无需任何 API 费用，这个Agent 拥有"看遍全网"的超能力
type: summary
tags:
- 开发工具
status: 已审核
confidence: medium
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/ed65d3b47a7e45dd9040caf93a6782fd
notion_id: ed65d3b4-7a7e-45dd-9040-caf93a6782fd
---

**一句话摘要**：Agent Reach 是一个开源脚手架工具，一行命令让 AI Agent 获得访问 Twitter/YouTube/Reddit/小红书等 12+ 平台的能力，完全免费且隐私安全。

**关键洞察**

- 定位是"脚手架"而非"框架"——安装后 Agent 直接调用上游工具（xreach/yt-dlp/gh CLI 等），不经过包装层

- 支持 12+ 平台：网页（Jina Reader）、YouTube（yt-dlp）、Twitter（xreach）、GitHub（gh CLI）、小红书、Reddit、B站、抖音、LinkedIn 等

- 每个渠道对应独立上游工具，可插拔替换，不满意直接换掉对应 channel 文件

- Cookie 只存本地（~/.agent-reach/config.yaml，权限 600），完全开源可审查

- 兼容所有 Agent：Claude Code、OpenClaw、Cursor、Windsurf 等任何能跑命令行的 Agent

**提取的概念**

- [Agent Reach](concepts/Agent Reach.md)（面向 AI Agent 的多平台访问脚手架）

- Jina Reader（已有词条）

**原始文章信息**

- 作者：GitHubStore

- 来源：微信公众号

- 发布时间：2026-03-04

- 链接：[https://mp.weixin.qq.com/s?__biz=MzkxNjQ4MzMyOA==&mid=2247494861&idx=1&sn=783b49fbac8a52fa070fb8d2ca00e581](https://mp.weixin.qq.com/s?__biz=MzkxNjQ4MzMyOA%3D%3D&mid=2247494861&idx=1&sn=783b49fbac8a52fa070fb8d2ca00e581)

**个人评注**

可以作为 OpenClaw Skill 的上游工具层使用，补充 Scrapling/Apify 无法覆盖的平台（Twitter、YouTube 字幕、RSS 等）。与 Tizer 的内容监控和情报收集需求直接契合。
