---
title: 调度者+子Agent
type: concept
tags:
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/1c79544c1fea40ecabb3d7cfdc678afb
notion_id: 1c79544c-1fea-40ec-abb3-d7cfdc678afb
---

## 定义

调度者+子Agent是一种由中心调度者负责拆分任务、分派工作、汇总结果的协作模式，适合把一个大问题拆成多个相对独立的小任务并行处理。

## 关键要点

- 适合代码审查、资料搜集、问题排查这类“可拆分、弱依赖、可汇总”的任务

- 优势是协调成本低、上手快，通常是多 Agent 系统最稳妥的起点

- 主要风险是调度者成为信息瓶颈，跨子任务的关键上下文可能在层层汇报中丢失

## 来源引用

- [原文链接](https://x.com/KKaWSB/status/2043883512168886387)｜《轻松掌握Anthropic官方给的五种"多Agent协作"模式》｜源文章：Anthropic 五种多 Agent 协作模式全解析：别上来就选最复杂的架构

## 关联概念

- 生成者+验证者

- Agent团队

- 消息总线

- 共享状态

- Claude Managed Agents
