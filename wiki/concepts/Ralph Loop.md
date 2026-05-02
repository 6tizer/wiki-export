---
title: Ralph Loop
type: concept
tags:
- 上下文管理
- Harness 工程
- Agent 协作模式
status: 审核中
confidence: medium
last_compiled: '2026-05-01'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/5d9fb21bbf3a4873a688f27b40c3d3f7
notion_id: 5d9fb21b-bf3a-4873-a688-f27b40c3d3f7
---

## 定义

Ralph Loop 是一种在 Agent 即将退出或上下文接近极限时，拦截执行流、刷新上下文并重启目标任务的续跑机制。

## 关键要点

- 适合长时程任务的连续推进

- 能降低因上下文用尽导致的任务中断

- 常与规划文件、自验证和压缩策略搭配使用

## 关联概念

- [Harness Engineering](concepts/Harness Engineering.md)

- [PRD 驱动 Vibe Coding](concepts/PRD 驱动 Vibe Coding.md)

- [OpenASE](entities/OpenASE.md)

- [HarnessCode](entities/HarnessCode.md)

## 来源引用

- [摘要：Harness Engineering：决定 AI Agent 能跑 10 分钟还是 10 小时的那层系统](summaries/摘要：Harness Engineering：决定 AI Agent 能跑 10 分钟还是 10 小时的那层系统.md)｜X书签文章｜原文链接：[https://x.com/shao__meng/status/2031532690034606549](https://x.com/shao__meng/status/2031532690034606549)

- [摘要：Ralph Loop：更轻量的 Harness Engineering 循环框架](summaries/摘要：Ralph Loop：更轻量的 Harness Engineering 循环框架.md)（[原文](https://x.com/wayne_zhang0/status/2042874483606983079)）｜X书签文章

- [摘要：用了这么久 Claude Code，很多人都在研究 CLAUDE.md、Hooks、Sub-Agent，但其实它 GitHub 仓库里还藏着一批官方插件，很多人根本没注意到。](summaries/摘要：用了这么久 Claude Code，很多人都在研究 CLAUDE.md、Hooks、Sub-Agent，但其实它 GitHub 仓库里还藏着一批官方插件，很多人根本没注意到。.md)（[原文](https://x.com/sitinme/status/2045127135195439279)）

- [摘要：Codex 推出 /goal 功能，不达目标，不罢休](summaries/摘要：Codex 推出 -goal 功能，不达目标，不罢休.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA4NzgzMjA4MQ%3D%3D&mid=2453483290&idx=1&sn=904eb46992f4d152d712fd963e274f9f&chksm=864bb17a8af07573edffe69e9e5007899c121000987a37dc35d01aae2065033c2c8f9fdc3806#rd)）

- [摘要：Codex推出/pet和/goal，不管是啥我都要学](summaries/摘要：Codex推出-pet和-goal，不管是啥我都要学.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA5MTIxNTY4MQ%3D%3D&mid=2461159607&idx=1&sn=a5b83cb73c3f68c2a272084aba243351&chksm=86423cd650291c6afa26f42686776cc115aa9bea16e70740052fe2c6f25f9fa46d966baf5d22#rd)）
