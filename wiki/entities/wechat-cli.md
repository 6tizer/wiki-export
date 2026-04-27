---
title: wechat-cli
type: entity
tags:
- MCP 协议
status: 草稿
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/519c296747d74826a0ea29b68b2d9703
notion_id: 519c2967-47d7-4826-a0ea-29b68b2d9703
---

## 定义

wechat-cli是一个开源的微信命令行工具，允许用户通过命令操作本地微信数据。全程本地运行，输出JSON格式，专为AI Agent集成设计。

## 11个内置命令

- `init`：一键初始化，提取密鑰

- `sessions`：列出最近会话

- `history`：查看聊天记录，支持分页和时间过滤

- `search`：全局搜索消息

- `stats`：聊天统计，谁最活跃、消息类型分布

- `export`：导出聊天记录为Markdown或纯文本

- `new-messages`：增量获取新消息

## WeSight

WeSight是基于wechat-cli和OpenClaw引擎的桌面端Agent产品，提供群聊分析/监控预警/聊天记录导出和AI精华总结。

**四维度AI精华总结：**核心议题、关键决策/结论、争议/待跟进、精华内容

## GitHub

[https://github.com/freestylefly/wechat-cli](https://github.com/freestylefly/wechat-cli)

## 关联概念

- [Graphify](entities/Graphify.md)

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [暗知识编译](concepts/暗知识编译.md)

- [SQLCipher 4](concepts/SQLCipher 4.md)

## 来源引用

- 摘要：我把微信 cli 开源了，群消息终于不用爬楼了！（苍何，2026-04-08）

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzI2MzA5NjA4MQ%3D%3D&mid=2665365507&idx=1&sn=8efb2e3bb093dcbda21aed892627d696&chksm=f0cdf306ccc0b7fcbef97f62e290b698001da1676e7ee11075b3dbb2b100e3c12bea51b047c6#rd)｜《Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki》｜源文章：Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki
