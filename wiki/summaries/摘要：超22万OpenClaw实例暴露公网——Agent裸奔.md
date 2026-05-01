---
title: 摘要：超22万OpenClaw实例暴露公网——Agent裸奔
type: summary
tags:
- Agent 安全
- OpenClaw
status: 已审核
confidence: medium
last_compiled: '2026-04-10'
source_tags: OpenClaw, Agent, 自动化, 安全
source_article_url: ''
notion_url: https://www.notion.so/Tizer/b32a4002141443a39516ff1807497170
notion_id: b32a4002-1414-43a3-9516-ff1807497170
---

## 一句话摘要

超 22 万个 OpenClaw 实例暴露公网且多数未启用认证，凸显 Agent 快速部署与安全治理的严重脱节。

## 关键洞察

- **22万+ 实例暴露**：多数未启用认证，部分存在明文凭证泄露

- **涉及企业云**：托管在腾讯、甲骨文、百度、阿里、华为等，可能涉及生产环境

- **Agent 风险远高于 Web 服务**：具备调用工具、访问数据库、执行代码能力，未鉴权可导致远程操控

- 部署量爆炸但安全治理未成熟

## 原始文章信息

- **作者**：AI前线

- **发布时间**：2026-03-03

- **链接**：[原文](https://mp.weixin.qq.com/s?__biz=MzU1NDA4NjU2MA%3D%3D&mid=2247657627&idx=1&sn=23a81a95a9aacddd538df297704e51fb)

## 个人评注

Agent 安全暴露的重要警示。与 OpenFang 16 层安全机制形成对比。
