---
title: Prompt Thinning
type: concept
tags:
- Coding Agent
status: 审核中
confidence: medium
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/40b798bbce044acd831ebdffcc9a72c3
notion_id: 40b798bb-ce04-4acd-831e-bdffcc9a72c3
---

## 定义

Prompt Thinning 是一种上下文瘦身策略，指在上下文窗口接近拥挤时，有选择地删除低价值噪声、保留关键决策与约束，以维持后续生成的稳定性。

## 关键要点

- 核心不是简单删减文字，而是按任务阶段保留最重要的决策框架

- 适合长任务、多轮返工和代码执行日志较多的 AI 编程场景

- 属于 context-window-aware 上下文管理方法，可直接缓解 Context Rot

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzk0MjcxOTM2Nw%3D%3D&mid=2247502908&idx=1&sn=781cf89e36526cf2ced56337406ae43c&chksm=c2ee5c17dbde042bf7dbe3e5b84da84512262606a3d3b9259740ab2613aab4fcde99397b23c2#rd)｜《GSD框架解析：解决AI编程工具Context Rot的工程化方案》｜源文章：GSD框架解析：解决AI编程工具Context Rot的工程化方案
