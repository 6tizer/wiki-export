---
title: 摘要：开源的Chrome 浏览器插件，一键扒光网站设计，让 AI 帮你复刻
type: summary
tags:
- Coding Agent
- 开发工具
status: 已审核
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b688130ac75fa1a31ec347a
notion_url: https://www.notion.so/71fe6f9968dd445280cc4234f88766df
notion_id: 71fe6f99-68dd-4452-80cc-4234f88766df
---

## 一句话摘要

这篇文章介绍了一个开源的 Chrome 扩展 design-md-chrome，它能从任意网站自动提取设计样式并生成 `DESIGN.md` 或 `SKILL.md` 文件，让 Claude、Cursor、Codex 等 AI 工具按目标网站的视觉风格进行复刻与实现。

## 关键洞察

- 这个工具不是简单截图或抄页面，而是把字体、颜色、间距、圆角、阴影、动画等设计信号结构化抽取出来。

- 它把网页设计直接转成 `DESIGN.md` / `SKILL.md` 这样的 Agent 可读资产，降低了把参考站点风格喂给 AI 编程工具的门槛。

- 插件同时覆盖本地开发安装与 Chrome 商店安装，说明它已经具备较低的试用成本与较强的传播性。

- 这类工具把“竞品拆解 → 设计规范沉淀 → AI 生成实现”连成一条链路，适合前端重构、套壳复刻和内容生产场景。

## 提取的概念

- [design-md-chrome](entities/design-md-chrome.md)

- [DESIGN.md](concepts/DESIGN.md.md)

- [SKILL.md](concepts/SKILL.md.md)

- [TypeUI](entities/TypeUI.md)

## 原始文章信息

- 作者：github淘金

- 来源：微信

- 发布时间：2026-04-21 08:48（Asia/Shanghai）

- 原文链接：[https://mp.weixin.qq.com/s?__biz=Mzg2MjY1NDIzNg==&mid=2247499291&idx=1&sn=e594d6f818da6cf6f862cb91bbefa3d8&chksm=cf669d5aca8d3d26ae43d2adca0d6a522314fa1e06aeef38d7a215e02fbbcd22bcbf5cd4f70f#rd](https://mp.weixin.qq.com/s?__biz=Mzg2MjY1NDIzNg%3D%3D&mid=2247499291&idx=1&sn=e594d6f818da6cf6f862cb91bbefa3d8&chksm=cf669d5aca8d3d26ae43d2adca0d6a522314fa1e06aeef38d7a215e02fbbcd22bcbf5cd4f70f#rd)

## 个人评注

对 Tizer 的工作流来说，这类工具的价值在于把外部优秀站点的视觉规范直接沉淀成 Markdown 资产，再交给 Claude Code、Codex 或其他 Coding Agent 使用，形成“参考网站 → 设计规范 → AI 落地实现”的高效闭环。
