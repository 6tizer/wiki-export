---
title: Skill 颗粒度设计
type: concept
tags:
- Coding Agent
- Agent 技能
status: 草稿
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/10812965aaba411e903d471be061af24
notion_id: 10812965-aaba-411e-903d-471be061af24
---

## 定义

Skill 颗粒度设计指的是为 Skill 划定多细的能力边界：哪些需求应该合并进同一个 Skill，哪些差异已经大到需要拆成独立 Skill。

## 关键要点

- 最优颗粒度不是越细越好，而是边界清楚且足够可复用

- 高频且边界明确的场景，更适合沉淀为独立 Skill

- 相近需求可以先在一个总 Skill 中统一承接，再在内部做分支路由

- 颗粒度过细会带来选择困难、性能下降和 Token 成本上升

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA%3D%3D&mid=2647681530&idx=1&sn=d5c714699089e31276c667cda1edefdb&chksm=f153676ae06e0dadad8df80becf797662c0126d74a5c1a314ecac659ebf41da34625aac44a6b#rd)｜源文章：Skill其实就是分类学。
