---
title: 摘要：Claude Code 全屏渲染来了：长对话不再闪烁，还能用鼠标！
type: summary
tags:
- CLI 工具
- IDE 集成
- Harness 工程
status: 已审核
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: https://www.notion.so/343701074b6881f4bcf5e5ee8e7352ab
notion_url: https://www.notion.so/Tizer/3170edf7c2eb47e89494e6e6775eee7d
notion_id: 3170edf7-c2eb-47e8-9494-e6e6775eee7d
---

## 一句话摘要

这篇文章介绍了 Claude Code 新增的 Fullscreen rendering，全屏渲染通过 alternate screen buffer 和按需可见区域渲染，显著改善长对话中的闪烁、卡顿与内存占用，同时带来鼠标交互和 transcript 模式下更顺滑的会话检索体验。

## 关键洞察

- Fullscreen rendering 把输入框固定在底部，并只渲染当前可见内容，直接改善了长对话中的界面闪烁问题

- alternate screen buffer 这一终端机制，是 Claude Code 本次界面优化的底层关键

- 鼠标支持让终端式编程 Agent 更接近日常图形界面的操作体验，包括定位光标、展开输出、打开链接和滚轮翻页

- transcript 模式把历史对话搜索、跳转和导出能力做得更接近 less，降低了长会话回溯成本

- 对重度使用 VS Code 内置终端、tmux、iTerm2、Ghostty 的 Claude Code 用户来说，这是一次偏基础设施层的体验升级

## 提取的概念

- [Claude Code](entities/Claude Code.md)

- [Fullscreen rendering](concepts/Fullscreen rendering.md)

- [alternate screen buffer](concepts/alternate screen buffer.md)

- [CC Switch](entities/CC Switch.md)

- [transcript 模式](concepts/transcript 模式.md)

## 原始文章信息

- 作者：老罗聊 AI

- 来源：微信

- 发布时间：2026-04-02 19:47

- 原文链接：[https://mp.weixin.qq.com/s?__biz=MzYyMzc4NjU0Mg==&mid=2247485518&idx=1&sn=32379f84dd600df7b002ea9070cc38fd&chksm=feee7cfd7f2988db5205c021092c341fa9b97c0c0d9c8d02c4394af0d93862d6e968ab042e31#rd](https://mp.weixin.qq.com/s?__biz=MzYyMzc4NjU0Mg%3D%3D&mid=2247485518&idx=1&sn=32379f84dd600df7b002ea9070cc38fd&chksm=feee7cfd7f2988db5205c021092c341fa9b97c0c0d9c8d02c4394af0d93862d6e968ab042e31#rd)

- 源页面：Claude Code 全屏渲染来了：长对话不再闪烁，还能用鼠标！

## 个人评注

这类更新虽然不是模型能力升级，但对 Tizer 当前偏终端化、长链路、HITL 的编程工作流价值很高。它减少了 Claude Code 在真实使用中的交互摩擦，能让内容整理、脚本改写、Agent 协作这些长时任务更稳定地跑下去。
