---
title: geo-content-writer
type: concept
tags:
- Agent 技能
- 内容创作
status: 草稿
confidence: medium
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/753eb26622024cceb00b2158befed358
notion_id: 753eb266-2202-4cce-b00b-2158befed358
---

## 定义

geo-content-writer 是一个开源的 GEO 内容生产工作流框架（GitHub: [GEO-SEO/geo-content-writer](https://github.com/GEO-SEO/geo-content-writer)），基于 Python 实现，通过 Dageno 平台的 Prompt 机会数据，将"发现机会→构建 Backlog→生成编辑简报→产出文章"的全流程自动化。

## 核心工作流

1. **机会发现层**：从 Dageno 获取真实用户 Prompt 数据，提取 Fanout 机会

1. **Backlog 层**：将 Fanout 整理为优先级队列，分配 Cluster Role，避免内容重叠

1. **写作层**：生成编辑简报（Editorial Brief）、分段写作合同（Draft Package）、审稿合同（Review Package）

1. **分发层**：支持 WordPress 发布

## 关键设计理念

- **从 Backlog 行出发**，而非直接从关键词生成文章，避免同质化内容

- **机器可读 Payload**：生产产物是结构化 JSON，供外部 Agent 逐段执行

- **质量契约**：发布前必须通过 Final Gate（包含竞争对比、决策引擎、证据要求等）

- **Cluster Role 规划**：为每篇文章分配角色（如 category_article、comparison_article），防止邻近文章重复

## 主要命令

```javascript
build-fanout-backlog → select-backlog-items → publish-ready-article → draft-article-from-payload
```

## 来源引用

- [原文链接](https://x.com/tim_geo_seo/status/2042096325634953260)｜《GEO Content Writer：用 Agent 把 AI 可见度做到行业第一》｜来源条目：[摘要：GEO Content Writer：用 Agent 把 AI 可见度做到行业第一](summaries/摘要：GEO Content Writer：用 Agent 把 AI 可见度做到行业第一.md)

- 推文：[@tim_geo_seo, 2026-04-09](https://x.com/tim_geo_seo/status/2042096325634953260)

- GitHub: [https://github.com/GEO-SEO/geo-content-writer（95★，MIT）](https://github.com/GEO-SEO/geo-content-writer（95★，MIT）)
