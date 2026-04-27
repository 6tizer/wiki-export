---
title: 摘要：The Bitter Lesson of Agent Harnesses
type: summary
tags:
- Harness 工程
- 浏览器自动化
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b68814c9384d22a1397f259
notion_url: https://www.notion.so/Tizer/d3c5eac262a146759c385ff9c105744e
notion_id: d3c5eac2-62a1-4675-9c38-5ff9c105744e
---

## 一句话摘要

Browser Use 团队将 Rich Sutton 的 Bitter Lesson 延伸到 Agent 工具层：不要包裹 LLM 的工具，直接给它 CDP 原始接口和可编辑的 helpers，让模型自行编写缺失能力并自我修复。

## 关键洞察

- **工具层也是抽象**：之前 Browser Use 花大量代码封装 click()、type()、scroll() 等浏览器操作，但这些 helper 本身就是对模型的约束——LLM 已经在数百万 token 的 CDP 文档上训练过，直接给它 CDP 比给它抽象更有效

- **~600 行极简 Harness**：整个执行底座仅由 4 个文件组成——[run.py](http://run.py/)（13 行）、[helpers.py](http://helpers.py/)（192 行）、[daemon.py](http://daemon.py/)（220 行）和 [SKILL.md](http://skill.md/)——Agent 写 Python，Python 调 helpers，helpers 说 CDP

- **自修复循环取代 Watchdog**：当工具缺失时，Agent 自动 grep [helpers.py](http://helpers.py/)、补写函数、继续执行；遇到 Chrome 崩溃等异常时也能自主 reattach，无需专门的容错处理器

- **真实案例验证**：Agent 自行编写了 upload_file() 函数，遇到 CDP websocket 10MB 限制后还自主切换到分块上传；还成功完成了 Gusto 员工生日导入 Google Calendar、Azure 管理门户操作等复杂任务

- **核心原则是「最大动作空间」**：先给模型最大自由度，再按需约束，而不是预先决定它需要哪些抽象

## 提取的概念

- [Bitter Lesson 原则](concepts/Bitter Lesson 原则.md)

- [Agent 自修复循环](concepts/Agent 自修复循环.md)

- [Browser Harness](entities/Browser Harness.md)

- [Browser Use](entities/Browser Use.md)

- [Chrome DevTools Protocol](concepts/Chrome DevTools Protocol.md)

- [SKILL.md](concepts/SKILL.md.md)

- [Agent Harness](concepts/Agent Harness.md)

## 原始文章信息

- **作者**：@gregpr07（Gregor Zunic，Browser Use 创始人）

- **来源**：X书签

- **发布时间**：2026-04-23

- **原文链接**：[https://x.com/gregpr07/status/2047358189327520166](https://x.com/gregpr07/status/2047358189327520166)

- **GitHub 仓库**：[browser-use/browser-harness](https://github.com/browser-use/browser-harness)

## 个人评注

这篇文章对 Tizer 的 Harness 工程思路有直接启发。核心洞察与 OpenClaw 的设计理念高度契合——把执行层做薄，让 Agent 自行演化工具链。Browser Harness 的自修复循环是 Agent 可编辑执行环境的典型案例，证明了「让模型写自己需要的工具」比「提前为模型准备所有工具」更具扩展性。对内容管线而言，这意味着 Agent 的 skill 文件不应过度封装底层能力，而应保留足够的原始接口让模型自适应。
