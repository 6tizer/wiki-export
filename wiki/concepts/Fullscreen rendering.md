---
title: Fullscreen rendering
type: concept
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1c1b047f256647e6a902a434557bca69
notion_id: 1c1b047f-2566-47e6-a902-a434557bca69
---

## 定义

Fullscreen rendering 是 Claude Code 引入的一种终端全屏渲染模式。它通过使用终端的 alternate screen buffer，并只重绘当前可见区域，来减少长对话中的闪烁、卡顿和内存压力。

## 关键要点

- 输入框固定在终端底部，不再随着输出持续跳动

- 渲染范围限制在当前可见消息，避免每次更新都重绘整段会话

- 长对话时内存占用更稳定，更适合持续的人机协作和长链路编程任务

- 在 VS Code 内置终端、tmux、iTerm2、Ghostty 这类环境里体感提升最明显

- 可与鼠标交互能力一起开启，也可以只保留无闪烁渲染

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzYyMzc4NjU0Mg%3D%3D&mid=2247485518&idx=1&sn=32379f84dd600df7b002ea9070cc38fd&chksm=feee7cfd7f2988db5205c021092c341fa9b97c0c0d9c8d02c4394af0d93862d6e968ab042e31#rd)｜《Claude Code 全屏渲染来了：长对话不再闪烁，还能用鼠标！》｜源页面：Claude Code 全屏渲染来了：长对话不再闪烁，还能用鼠标！

## 关联概念

- [Claude Code](entities/Claude Code.md)
