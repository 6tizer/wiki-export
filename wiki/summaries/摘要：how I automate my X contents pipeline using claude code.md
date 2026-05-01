---
title: 摘要：how I automate my X contents pipeline using claude code.
type: summary
tags:
- 内容自动化
- 代码生成
- 图像生成
status: 已审核
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b68818c96fcec842accdacc
notion_url: https://www.notion.so/Tizer/4408d5c80fc4452a9a1f4c68f5072dbf
notion_id: 4408d5c8-0fc4-452a-9a1f-4c68f5072dbf
---

## 一句话摘要

这篇文章展示了如何把 Claude Code 作为内容运营的编排中枢，用 [CLAUDE.md](http://claude.md/)、抓热点脚本、研究执行脚本和图像/视频技能，把 X 内容生产压缩成“选题—起稿—设计—剪辑—人工定稿”的半自动流水线。

## 关键洞察

- 先用 [CLAUDE.md](http://claude.md/) 固化系统边界，而不是每次临时提示。

- 通过脚本抓取 X 热门内容并按互动排序，选题从凭感觉变成数据驱动。

- 写作环节先产出结构，再补研究材料和转写，AI 负责底稿，人负责风格校正。

- 横幅、信息图和视频处理被拆进可调用的技能或脚本里，减少在多个工具之间来回切换。

- 这套流程的核心不是“完全自动发帖”，而是把 80% 重复劳动自动化，同时保留人工终审。

## 提取的概念

- [Claude Code](entities/Claude Code.md)

- [CLAUDE.md](concepts/CLAUDE.md.md)

- [规划/检索/执行三层隔离](concepts/规划-检索-执行三层隔离.md)

- [内容创作工程化](concepts/内容创作工程化.md)

- [数据驱动内容选题](concepts/数据驱动内容选题.md)

- [自退火循环](concepts/自退火循环.md)

## 原始文章信息

- 作者：@exploraX_

- 来源：X书签

- 发布时间：2026-04-22

- 原文链接：[https://x.com/exploraX_/status/2046950874237337808](https://x.com/exploraX_/status/2046950874237337808)

## 个人评注

这套方法对 Tizer 的价值在于，它把内容生产拆成了可编排步骤：热点抓取、资料研究、草稿生成、视觉资产生成、人工审校。对 HITL 和 OpenClaw 类工作流来说，最值得借鉴的不是单个 prompt，而是用配置文件 + 脚本 + 人工复核构成稳定流水线的思路。
