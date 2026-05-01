---
title: 摘要：昨天才开源的浏览器扩展：一键获取任意网站 DESIGN.md
type: summary
tags:
- 知识管理
status: 已审核
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: https://www.notion.so/346701074b688192ab8bde73c8c37d27
notion_url: https://www.notion.so/Tizer/d15ea6c0695b49ce9eb3e7b150c1775b
notion_id: d15ea6c0-695b-49ce-9eb3-e7b150c1775b
---

## 一句话摘要

这篇文章介绍了一个刚开源的 Chrome 扩展，它能从任意网页自动提取设计样式并生成 [DESIGN.md](http://design.md/) 或 [SKILL.md](http://skill.md/)，帮助开发者把网站设计系统转成可被 AI 编程工具直接消费的结构化规范。

## 关键洞察

- 插件的核心价值不是“截图”或“复制页面”，而是把网页中的排版、颜色、间距、圆角、阴影和动效等设计信号结构化提取出来。

- 输出目标是 [DESIGN.md](http://design.md/) 与 [SKILL.md](http://skill.md/) 这类 Agent 可读文件，让 Google Stitch、Claude Code、Codex 等工具能够基于统一设计蓝图生成或改写页面。

- 该项目基于 TypeUI 的 [DESIGN.md](http://design.md/) 格式，说明设计系统正在从设计工具内部资料转向可版本化、可复用、可被 LLM 直接读取的文本接口。

- design-md-chrome 的开源意味着团队可以直接 fork 并按自己的工作流改造提取流程、生成规范和输出模板。

- 这类“从真实网页反向生成设计规范”的工具，为前端重构、竞品拆解、设计迁移和 AI 辅助开发提供了新的切入口。

## 提取的概念

- [DESIGN.md](concepts/DESIGN.md.md)

- [SKILL.md](concepts/SKILL.md.md)

- [TypeUI](entities/TypeUI.md)

- [design-md-chrome](entities/design-md-chrome.md)

## 原始文章信息

- 作者：Rico的设计漫想

- 来源：微信

- 发布时间：2026-04-16 10:23（Asia/Shanghai）

- 原文链接：[https://mp.weixin.qq.com/s?__biz=MzA3MDc2OTQwMw==&mid=2456446097&idx=1&sn=3af45a46ce3ee45352e8dd2f7ee413c3&chksm=8943077d2f9183c84189f4fd3139c21b605914b6c441ce81f1a33e60da1a82bf67439eb3a916#rd](https://mp.weixin.qq.com/s?__biz=MzA3MDc2OTQwMw%3D%3D&mid=2456446097&idx=1&sn=3af45a46ce3ee45352e8dd2f7ee413c3&chksm=8943077d2f9183c84189f4fd3139c21b605914b6c441ce81f1a33e60da1a82bf67439eb3a916#rd)

## 个人评注

这类工具对 Tizer 的价值不只是在“提取网页样式”，更在于把外部网站的视觉与交互规范沉淀成 Markdown 资产，再接到 Claude Code、OpenClaw 或内容生产流水线里，形成从参考站点 → 规范文档 → 生成实现的闭环。
