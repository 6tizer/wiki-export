---
title: 摘要：Codex 刚刚上线了一个重磅新功能——自带“评论模式”的应用内浏览器
type: summary
tags:
- Coding Agent
- Agent 技能
status: 已审核
confidence: medium
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: https://www.notion.so/345701074b6881de996bea06f416f788
notion_url: https://www.notion.so/8f92a62227fc4a23899f861b9bc5d09b
notion_id: 8f92a622-27fc-4a23-899f-861b9bc5d09b
---

## 一句话摘要

Codex 新增了带评论模式的应用内浏览器，让用户可以在编辑器内直接浏览网页、点选页面元素，并把截图与 DOM 上下文无缝交给 Agent 继续迭代。

## 关键洞察

- 这次更新把网页查看、元素定位和对话迭代合并到同一个编码界面里，减少了频繁切换窗口的摩擦

- 评论模式的核心价值在于把“这里有问题”变成可定位的页面上下文，比手工描述 UI 问题更精确

- 截图与 DOM 元素同时进入上下文后，Agent 对页面状态的理解会更具体，适合前端调试和页面微调

- 除了做应用前端迭代，这种能力也适合一边看文档一边向 Agent 追问细节

## 提取的概念

- [Codex](entities/Codex.md)

- [应用内浏览器](concepts/应用内浏览器.md)

- [浏览器评论模式](concepts/浏览器评论模式.md)

- [DOM 代理自动化](concepts/DOM 代理自动化.md)

## 原始文章信息

- 作者：@dotey

- 来源：X书签

- 发布时间：2026-04-16

- 原文链接：[https://x.com/dotey/status/2044879703698526617](https://x.com/dotey/status/2044879703698526617)

## 个人评注

这类能力和 Tizer 的 HITL 工作流很契合。它把“指出网页哪里要改”变成结构化上下文输入，能够明显降低前端改版、落地页优化和文档辅助问答里的沟通损耗，也为 OpenClaw 风格的页面协作提供了更顺滑的交互层。
