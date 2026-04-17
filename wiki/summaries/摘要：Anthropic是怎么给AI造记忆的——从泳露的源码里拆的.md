---
title: 摘要：Anthropic是怎么给AI造记忆的——从泳露的源码里拆的
type: summary
tags:
- OpenClaw
- 记忆系统
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化, Claude
source_article_url: ''
notion_url: https://www.notion.so/18673a96176848c388f2661078087831
notion_id: 18673a96-1768-48c3-88f2-661078087831
---

**一句话摘脁**：作者专业拆解 Claude Code 泳露源码中的记忆系统，揭示其互斥锁的后台记忆提取、"Cheapest First" 三重门控、Microcompact 缓存「骗”层和 Prompt 标题对模型行为的巨大影响。

---

## 关键洞察

- **互斥锁的后台记忆提取**：`extractMemories` 子 Agent 在每轮对话后异步运行；主 Agent 已写记忆则后台自动跳过（互斥，不是去重）

- **确认信号同样重要**：只记纠正导致模型过度谨慎，记录 "perfect"、"yes exactly" 等确认信号同样重要

- **三重门控（Cheapest First）**：Gate1时间 → Gate1.5 扫描节流 → Gate2 Session数 → Gate3 锁，99% turn 在第一关就返回

- **Microcompact 缓存「骗”**：通过 `cache_edits` API 指令告诉服务端将旧工具输出当作空处理，不修改本地消息保留缓存热

- **Prompt 标题对分数的巨大影响**：同一段规则，标题改成行动时刻提示（"Before recommending"）得 3/3；改成抽象概念（"Trusting what you recall"）得 0/3

## 原始文章信息

- **作者**：AI比我快

- **来源**：微信公众号

- **发布日期**：2026-03-31

- **链接**：[https://mp.weixin.qq.com/s?__biz=MzcwMDE2MTQ3NA==&mid=2247483877](https://mp.weixin.qq.com/s?__biz=MzcwMDE2MTQ3NA%3D%3D&mid=2247483877)

## 个人评注

这篇文章是整个 Claude Code 泳露事件中对记忆系统拆解最详细、最有工程价值的文章。Cheapest First 和 Microcompact 设计可直接应用于 Tizer 的 Agent 成本控制。
