---
title: 摘要：1M 上下文时代太费 Token，告诉你我的 Coding Agent 省钱方法
type: summary
tags:
- 上下文管理
- CLI 工具
status: 已审核
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: https://www.notion.so/351701074b688156a5eac571ae58f2b8
notion_url: https://www.notion.so/Tizer/d70e98c22f2e40839a6086af1c7b3fe6
notion_id: d70e98c2-2f2e-4083-9a60-86af1c7b3fe6
---

## 一句话摘要

1M 上下文窗口虽大，但噪音和成本问题依然严峻——通过会话管理（新开会话、主动压缩、Sub Agent 委派、Rewind 回退）才能真正提效省钱。

## 关键洞察

- **1M 上下文 ≠ 无限记忆**：上下文越长，无关信息越多，模型越容易被旧路径和失败尝试干扰，导致「越聊越笨」

- **新任务新会话**：不同任务之间的上下文互相污染，切换任务时应果断清空会话，只手动携带关键结论

- **主动压缩优于被动触发**：在上下文混乱前用 `/compact` 并附带方向提示，避免系统自动压缩时丢失关键信息

- **Sub Agent 是省 Token 大杀器**：将检索、验证等产生大量中间输出的任务委派给子 Agent，主会话只接收最终结论

- **Rewind 比 PUA 更有效**：Agent 走错路时回退到关键分叉点重新开始，比在错误上下文里继续修正更省 token 且效果更好

## 提取的概念

- [Claude Code 上下文管理](concepts/Claude Code 上下文管理.md)

- [Sub agent 上下文隔离](concepts/Sub agent 上下文隔离.md)

- [Context Compaction](concepts/Context Compaction.md)

- [Rewind](concepts/Rewind.md)

- [Claude Code](entities/Claude Code.md)

## 原始文章信息

- **作者**：MacTalk

- **来源**：微信公众号

- **发布时间**：2026-04-29

- **链接**：[原文](https://mp.weixin.qq.com/s?__biz=MjM5ODQ2MDIyMA%3D%3D&mid=2650734353&idx=1&sn=ed1c3514623d29bffc28e1856c920dd8&chksm=bf1f3acf64e4e5b746803a7ac4aaf8bfc0f5d216e8dcbdb8f89d5f6d4d961af981b37393dba6#rd)

## 个人评注

本文是面向 Coding Agent 用户的实操省钱指南，核心观点与 Tizer 的 Harness Engineering 实践高度相关：会话管理本质上就是上下文工程的用户侧实践。对 OpenClaw 和内容自动化流水线的启示在于——长时程 Agent 任务同样需要内置「阶段切分 → 压缩 → 子任务委派」的管理策略，避免单一会话累积过多噪音导致质量下降和成本失控。
