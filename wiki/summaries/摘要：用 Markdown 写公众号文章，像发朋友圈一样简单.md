---
title: 摘要：用 Markdown 写公众号文章，像发朋友圈一样简单
type: summary
tags:
- 内容自动化
- CLI 工具
status: 已审核
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: https://www.notion.so/348701074b6881b2b6eac1e04371232d
notion_url: https://www.notion.so/Tizer/320286d1fe9c444a9df58b9b0f69ca4a
notion_id: 320286d1-fe9c-444a-9df5-8b9b0f69ca4a
---

## 一句话摘要

md2wechat 把 Markdown 写作、排版转换、图片处理与微信草稿箱投递整合成一条可自动化的公众号内容生产链路，让公众号写作接近“像发朋友圈一样简单”。

## 关键洞察

- 这不是单点排版工具，而是一条从写作、检查、预览到发稿的完整内容流水线

- 以 Markdown 作为统一内容源，能显著降低在微信编辑器里重复整理格式的成本

- 工具同时支持 API 模式与 AI 模式：前者偏稳定快速，后者偏样式灵活与模型接力

- 通过 CLI + Skill 的组合，md2wechat 可以被 Claude Code、Codex、OpenCode、OpenClaw、Claudian 等 Agent 环境直接调用

- `inspect`、`preview`、`humanize`、图片上传与草稿推送等能力，说明它覆盖了内容团队真正需要的“最后一公里”发布环节

## 提取的概念

- [md2wechat](entities/md2wechat.md)

- [Markdown 转公众号工作流](concepts/Markdown 转公众号工作流.md)

- [微信草稿箱自动上传](concepts/微信草稿箱自动上传.md)

- [AI 模式排版请求](concepts/AI 模式排版请求.md)

## 原始文章信息

- 作者：@seekjourney

- 来源：X书签

- 发布时间：2026-04-17

- 原文链接：[https://x.com/seekjourney/status/2045056409457549784](https://x.com/seekjourney/status/2045056409457549784)

- 源文章页面：md2wechat：用 Markdown 写公众号文章，一键推送到微信草稿箱

## 个人评注

这类工具很适合 Tizer 当前的内容流水线思路：先让 Agent 或人类用 Markdown 产出，再通过标准化命令做检查、排版和草稿投递，最后保留 HITL 审核。它的价值不只是“发公众号”，而是把内容生产过程拆成可复用、可组合、可被 Agent 接管的若干能力模块。
