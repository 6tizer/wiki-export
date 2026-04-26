---
title: Batching & Yielding
type: concept
tags:
- 前端开发
- 浏览器自动化
status: 草稿
confidence: medium
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/9388664845ca4644a7bc085b381763ad
notion_id: 93886648-45ca-4644-a7bc-085b381763ad
---

### 定义

Batching & Yielding 是一种前端长任务处理策略，即把大规模计算拆成多个小批次执行，并在批次间主动把控制权交还给浏览器，以减少界面冻结。

### 关键要点

- 适用于浏览器内做静态分析、可视化计算或大数据处理时的性能优化。

- “Batching” 负责分块处理，“Yielding” 负责在块与块之间让出主线程。

- 常见实现方式包括 setTimeout、requestIdleCallback 或调度器分片。

- 在文章示例里，这种策略用于避免大仓库分析时 UI 卡死。

### 来源引用

- 2026/04/16｜《codeflow: github上最被低估的黑科技，仅用一个html文件，浏览器直接“透视”整个项目架构，自动计算代码变更的爆炸半径！》

  - 来源：微信

  - 原文链接：[查看原文](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ%3D%3D&mid=2247484493&idx=1&sn=a5ee52c8f58f8da657f54f32976bf1dd&chksm=f56db0775eab013c92bc978ab53e6fa4ac8d49e227f35e3313e988b7b0735bcc7310ae8ce2f6#rd)

  - 源文章页：codeflow:  github上最被低估的黑科技，仅用一个html文件，浏览器直接"透视"整个项目架构，自动计算代码变更的爆炸半径！
