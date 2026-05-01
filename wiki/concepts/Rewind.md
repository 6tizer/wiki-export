---
title: Rewind
type: concept
tags:
- 上下文管理
- 加密资产
status: 审核中
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/65563cf3325540f0aed6199796b602f9
notion_id: 65563cf3-3255-40f0-aed6-199796b602f9
---

## 定义

Rewind 是 Claude Code 的会话回退机制，允许回到某个历史消息点重新分支，把其后的消息、工具调用和输出从当前上下文中移除，以减少错误路径和上下文污染。

## 关键要点

- 适合在方案走错方向后回退重来，而不是继续在错误分支上叠加修正

- 比直接补一句“这条路不对，改试另一个方案”更干净，因为会明确丢弃失败路径

- 可与 handoff 摘要或重写提示配合，保留教训但不保留噪声

- 在长任务里，每一轮回复都可能成为新的分叉点，因此回退能力本身就是上下文管理工具

## 来源引用

- [摘要：这样用 Opus 4.7，才能发挥实力](summaries/摘要：这样用 Opus 4.7，才能发挥实力.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ%3D%3D&mid=2247515662&idx=1&sn=bfcc64cdceb913aef59f697c1ecbfa8d&chksm=c3914681eabbc4c3c559e95297d8d5b85aebabf0c4c93a5d517e6784d086e7b7ff3aa9abee9e#rd)）

- [原文链接](https://x.com/trq212/status/2044548257058328723)｜《Using Claude Code: Session Management & 1M Context》｜源文章：Claude Code 会话管理指南：如何驾驭 100 万 Token 的上下文窗口

- [原文链接](https://x.com/AYi_AInotes/status/2044625894556230013)｜《说实话，这才是Anthropic今年最有价值的更新啊，没有之一！！！》｜来源条目：[摘要：说实话，这才是Anthropic今年最有价值的更新啊，没有之一！！！](summaries/摘要：说实话，这才是Anthropic今年最有价值的更新啊，没有之一！！！.md)

- [摘要：1M 上下文时代太费 Token，告诉你我的 Coding Agent 省钱方法](summaries/摘要：1M 上下文时代太费 Token，告诉你我的 Coding Agent 省钱方法.md)（[原文](https://mp.weixin.qq.com/s?__biz=MjM5ODQ2MDIyMA%3D%3D&mid=2650734353&idx=1&sn=ed1c3514623d29bffc28e1856c920dd8&chksm=bf1f3acf64e4e5b746803a7ac4aaf8bfc0f5d216e8dcbdb8f89d5f6d4d961af981b37393dba6#rd)）

## 关联概念

- [Claude Code 上下文管理](concepts/Claude Code 上下文管理.md)

- [Context Rot](concepts/Context Rot.md)

- [Context Compaction](concepts/Context Compaction.md)

- [Subagents 并行](concepts/Subagents 并行.md)

- [Claude Code](entities/Claude Code.md)
