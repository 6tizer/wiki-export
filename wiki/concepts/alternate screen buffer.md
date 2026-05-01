---
title: alternate screen buffer
type: concept
tags:
- CLI 工具
- 加密资产
status: 审核中
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c60dbfa4f630459e83b0d14d692a4432
notion_id: c60dbfa4-f630-459e-83b0-d14d692a4432
---

## 定义

alternate screen buffer 是终端程序常用的一种全屏界面机制。像 vim、htop 这类 TUI 程序会在备用缓冲区里绘制界面，从而把实时界面刷新与主滚动历史分开。

## 关键要点

- 适合构建全屏交互式终端界面

- 可以避免在主终端历史中反复重绘整段内容

- 有助于降低界面闪烁，提升长会话场景下的可读性

- Claude Code 的 Fullscreen rendering 就利用了这一机制来优化长对话体验

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzYyMzc4NjU0Mg%3D%3D&mid=2247485518&idx=1&sn=32379f84dd600df7b002ea9070cc38fd&chksm=feee7cfd7f2988db5205c021092c341fa9b97c0c0d9c8d02c4394af0d93862d6e968ab042e31#rd)｜《Claude Code 全屏渲染来了：长对话不再闪烁，还能用鼠标！》｜源页面：Claude Code 全屏渲染来了：长对话不再闪烁，还能用鼠标！

## 关联概念

- [Claude Code](entities/Claude Code.md)
