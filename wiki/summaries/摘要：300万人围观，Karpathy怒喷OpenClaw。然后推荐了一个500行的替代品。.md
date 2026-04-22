---
title: 摘要：300万人围观，Karpathy怒喷OpenClaw。然后推荐了一个500行的替代品。
type: summary
tags:
- OpenClaw
status: 已审核
confidence: medium
last_compiled: '2026-04-10'
source_tags: NewStuff
source_article_url: ''
notion_url: https://www.notion.so/ba09d47dc3fd407187ad33b5f7d83173
notion_id: ba09d47d-c3fd-4071-87ad-33b5f7d83173
---

## 一句话摘要

Karpathy 批评 OpenClaw 为「40 万行代码的怪物」，并推荐仅 500 行核心代码的轻量级替代品 NanoClaw。

## 关键洞察

- **OpenClaw 的臃肿问题**：52 个模块、45 个依赖项、15 个渠道抽象层，所有东西挤在共享内存的 Node 进程中，安全隐患大

- **NanoClaw 的极简设计**：核心代码 500 行，总体约 4000 行，安装 3 行命令，无配置文件概念，所有定制通过 Skills 完成

- **AI 自我修改代码**：NanoClaw 通过 Claude Code 处理安装和配置，AI 直接读 Skill、安装依赖、修改源码

- **三个颠覆性观点**：DRY 原则过时（适度重复是隔离）、严格文件行数限制过时、代码无需经得起时间考验

## 提取的概念

- NanoClaw

- [AI 自修改代码](concepts/AI 自修改代码.md)

## 原始文章信息

- **作者**：探索AGI

- **来源**：微信公众号

- **发布时间**：2026-02-27

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNjcyNTk2NA%3D%3D&mid=2247490420&idx=1&sn=e8b916bac5117aa5debc128dd69251ee)

## 个人评注

NanoClaw 的极简理念和 AI 自修改代码特性值得关注。对 OpenClaw 的 Skill 架构思路有借鉴意义。DRY 原则过时论在 AI 编码时代确实有其道理——AI 修改共享函数时难以考虑下游影响。
