---
title: 摘要：GhostTrack — 免费开源 OSINT 追踪工具
type: summary
tags:
- CLI 工具
status: 已审核
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: https://www.notion.so/351701074b6881f99c0ad64a2423da56
notion_url: https://www.notion.so/Tizer/9337e63f13ce47ae8f5a34b31f7a2bc7
notion_id: 9337e63f-13ce-47ae-8f5a-34b31f7a2bc7
---

## 一句话摘要

GhostTrack 是一款免费开源的 Python OSINT 工具，集成 IP 地理定位、手机号码情报和社交媒体用户名追踪，可在 Linux 和 Android Termux 上零成本运行，替代 Spokeo、BeenVerified 等年费数百美元的付费服务。

## 关键洞察

- **三合一情报采集**：单一工具覆盖 IP 追踪、电话号码查询和用户名跨平台搜索，无需分别注册多个付费服务

- **极低运行门槛**：纯 Python 实现，支持在 $5 Android 手机 + Termux 上运行，无需桌面环境

- **成本对比悬殊**：Spokeo/BeenVerified/TruthFinder 等同类付费服务年费合计超 $900，GhostTrack 完全免费

- **GitHub 社区验证**：11,300+ Stars、1,535 Forks，自 2023 年活跃至今，说明有持续的社区使用需求

- **实际价值存疑**：评论区指出其 IP 定位基于 ISP 而非真实位置，电话/用户名数据来自公开 API，信息粒度有限

## 提取的概念

- [GhostTrack](entities/GhostTrack.md)

- [OSINT](concepts/OSINT.md)

## 原始文章信息

- **作者**：@sharbel

- **来源**：X 书签

- **发布日期**：2026-04-29

- **原文链接**：[https://x.com/sharbel/status/2049462813727318148](https://x.com/sharbel/status/2049462813727318148)

- **GitHub 仓库**：[HunxByts/GhostTrack](https://github.com/HunxByts/GhostTrack)

## 个人评注

这篇文章本质是一条 X 推广帖，介绍了一款免费 OSINT CLI 工具。对 Tizer 的工作流而言，GhostTrack 本身与 AI/Agent 管线无直接关联，但其「开源替代付费 SaaS」的叙事模式值得关注——类似 OpenClaw 用开源替代闭源 Agent 框架的思路。评论区中关于工具实际数据质量的质疑也提醒：GitHub Stars 不等于产品价值，需实际验证数据源的深度和准确性。
