---
title: Snapshot 引用机制
type: concept
tags:
- Agent 技能
- 开发工具
status: 草稿
confidence: medium
last_compiled: '2026-04-25'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/81c6e1a591ff404f939705eb7bceecd0
notion_id: 81c6e1a5-91ff-404f-9397-05eb7bceecd0
---

## 定义

Snapshot 引用机制是一种把页面中的按钮、输入框、链接等交互元素映射为短引用标识（如 @e1、@e2）的表示方法，使 Agent 能直接引用这些标识继续执行操作。

## 关键要点

- 它把“重新查找元素”转成“复用稳定引用”，减少选择器依赖。

- 对连续多步操作尤其有价值，因为 Agent 可以沿用上一步的元素引用。

- 本质上属于面向 Agent 的交互状态压缩与动作寻址机制。

## 来源引用

- [摘要：agent-browser：为AI Agent 写的浏览器CLI](summaries/摘要：agent-browser：为AI Agent 写的浏览器CLI.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIwNzU5MzY4OQ%3D%3D&mid=2247486082&idx=1&sn=68860cb626f874e6753331df42a06452&chksm=96b464c960e585a7580e8b47dab3d5957471c51e820dc9014909b4afcba510e60109f7838c82#rd)）
