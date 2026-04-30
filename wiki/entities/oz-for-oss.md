---
title: oz-for-oss
type: entity
tags:
- 代码生成
- Agent 协作模式
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/6218718997c94053b7dafd864dba2886
notion_id: 62187189-97c9-4053-b7da-fd864dba2886
---

## 定义

oz-for-oss 是 Warp 开源的一组 GitHub Actions 工作流和 Python 脚本，用于将 Oz Agent 能力引入开源项目的日常维护。它覆盖 issue 分诊、产品/技术 spec 生成、实现 PR 创建、PR review 编排和未就绪任务引导等全流程。

> 仓库地址：[https://github.com/warpdotdev/oz-for-oss](https://github.com/warpdotdev/oz-for-oss)

> 许可证：MIT

> Stars：116（截至 2026-04-29）

> 语言：Python

## 关键要点

- 以 GitHub Actions 可复用工作流为载体，其他开源项目可直接引入

- 需要创建 GitHub App 并配置 `OZ_MGMT_GHA_APP_ID`、`OZ_MGMT_GHA_PRIVATE_KEY`、`WARP_API_KEY` 等密钥

- 核心脚本位于 `.github/scripts/oz_workflows/`，包括 triage、spec 创建、实现、PR review 等入口

- 活跃维护的开源项目可申请 Oz Open Source Partnership 获得免费 Oz credits

- Warp 创始人 Zach Lloyd 表示已将此流程用于 Warp 自身的开源社区贡献管理

## 关联概念

- [Oz](entities/Oz.md)：底层 Agent 基础设施

- [Warp](entities/Warp.md)：母产品

## 来源引用

- [摘要：Repository permissions](summaries/摘要：Repository permissions.md)（[原文](https://x.com/zachlloydtweets/status/2049525301982400763)）

- [摘要：The open agentic development loop](summaries/摘要：The open agentic development loop.md)（[原文](https://x.com/zachlloydtweets/status/2049562997551694113)）
