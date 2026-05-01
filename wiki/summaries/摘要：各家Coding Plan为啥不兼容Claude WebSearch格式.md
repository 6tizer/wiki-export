---
title: 摘要：各家Coding Plan为啥不兼容Claude WebSearch格式
type: summary
tags:
- IDE 集成
- MCP 协议
- 浏览器自动化
status: 已审核
confidence: medium
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: https://www.notion.so/346701074b688126a403e7eb4c7198e3
notion_url: https://www.notion.so/Tizer/02ede0dc76994dd89ea88f2b54b0cce1
notion_id: 02ede0dc-7699-4dd8-9ea8-8f2b54b0cce1
---

## 一句话摘要

这篇文章的核心观点是：不少宣称兼容 Anthropic API 的 Coding Plan，只兼容了通用 Tools 外壳，却没有兼容 Claude Code 对内置联网工具的真实调用语义，因此在 WebSearch 上报 422、在 WebFetch 链路上报 403。

## 关键洞察

- WebSearch 的报错重点不是“没搜到内容”，而是后端把 Anthropic 的内置搜索工具当成普通自定义工具处理，强行要求 `input_schema`。

- WebFetch 的失败发生在本地抓取网页成功之后，说明问题更可能出在后端 Coding Plan 的能力支持，而不是抓取动作本身。

- “兼容 Anthropic API”并不自动等于“兼容 Claude Code”，因为 Claude Code 会依赖 Anthropic 体系下更细粒度的工具协议和内置工具语义。

- [z.ai](http://z.ai/) 官方 API 虽然提供搜索能力，但接口形态更接近自家风格，也没有在 Coding Plan API 层面完整兼容 Claude Code 的 WebSearch。

- OpenClaw 这类强调模型中立与多模型适配的系统，反而更重视把不同模型与搜索能力接成统一执行链。

## 提取的概念

- [Claude Code](entities/Claude Code.md)

- [Anthropic API](entities/Anthropic API.md)

- [WebSearch](concepts/WebSearch.md)

- [WebFetch](concepts/WebFetch.md)

- [GLM-5.1](entities/GLM-5.1.md)

- [OpenClaw](entities/OpenClaw.md)

## 原始文章信息

- 作者：aigcrepo

- 来源：微信

- 发布时间：2026-04-18 19:11

- 原文链接：[查看原文](https://mp.weixin.qq.com/s?__biz=MzkyOTY1NzMzNg%3D%3D&mid=2247489376&idx=1&sn=722c4f2ba5f82432e7abff79079f8bef&chksm=c3cb3b3b7b865b2b1cf89b3ea79ebe2a03d32fb1e8749f2f334e444c518356d58f2af2b2561f#rd)

## 个人评注

这篇文章对 Tizer 的启发是：做模型接入、Agent 编排或内容流水线时，不能只看“兼容某家 API”这类市场口径，还要拆到工具协议、内置工具类型、错误码语义与客户端行为层去验证。对需要同时接 Claude Code、OpenClaw 或自建 Agent 的工作流来说，真正关键的是 **tool dialect compatibility**，否则看似可用，到了搜索、抓取、委托执行这些高价值环节就会暴露断层。
