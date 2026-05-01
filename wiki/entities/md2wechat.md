---
title: md2wechat
type: entity
tags:
- 社交媒体
- 内容自动化
- CLI 工具
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/839c9cbd8a954c95968d98e652d1f62b
notion_id: 839c9cbd-8a95-4c95-968d-98e652d1f62b
---

## 定义

md2wechat 是一个面向微信公众号内容发布的 CLI / API / Skill 工具，核心目标是把 Markdown 写作、排版转换、图片处理与草稿投递串成一条可自动化的发布链路。

## 关键要点

- 以 Markdown 作为内容源，降低在微信编辑器中重复排版的成本

- 同时提供 API 模式与 AI 模式，既能快速生成 HTML，也能生成交给外部模型继续处理的排版请求

- 支持预览、inspect、图片上传、草稿推送、humanize 等围绕发布的完整能力

- 可通过 `npx skills add` 接入 Claude Code、Codex、OpenCode 等 Coding Agent，也兼容 OpenClaw 与 Obsidian / Claudian 场景

## 适用场景

- 技术博主或内容团队用 Markdown 维护公众号文章

- 将 AI 生成内容接入微信发布流程

- 在 Agent 工作流中把“写作—排版—发稿”封装为可重复调用的工具能力

## 关联概念

- [Markdown 转公众号工作流](concepts/Markdown 转公众号工作流.md)

- [微信草稿箱自动上传](concepts/微信草稿箱自动上传.md)

- [AI 模式排版请求](concepts/AI 模式排版请求.md)

## 来源引用

- [摘要：用 Markdown 写公众号文章，像发朋友圈一样简单](summaries/摘要：用 Markdown 写公众号文章，像发朋友圈一样简单.md)（[原文](https://x.com/seekjourney/status/2045056409457549784)）

- [摘要：43 个排版模块，Agent 帮你一键完成公众号排版](summaries/摘要：43 个排版模块，Agent 帮你一键完成公众号排版.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA5Njg4Mzk0NQ%3D%3D&mid=2649825377&idx=1&sn=d46eacb27a67c81f02021d2fa4532fcc&chksm=891a78112ba45aa1feae298ec0b1ac9ba014041b538b5d374588d8f75336ead4aa9a9a1d7c32#rd)）
