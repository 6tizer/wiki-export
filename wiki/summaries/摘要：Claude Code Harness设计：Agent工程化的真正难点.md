---
title: 摘要：Claude Code Harness设计：Agent工程化的真正难点
type: summary
tags:
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/b4b725e3a67642688aa8ea97786eb06b
notion_id: b4b725e3-a676-4268-8aa8-ea97786eb06b
---

**一句话摘脁**：Founder Park 混度剖析 Claude Code 的成熟 Harness 设计，涵盖 TAOR 循环哲学、Context 管理三层防御、六层记忆架构、五档权限信任光谱和多 Agent 编排。

---

## 关键洞察

- **TAOR 循环**：Think-Act-Observe-Repeat，Orchestrator 越笨架构越稳定；所有推理、决策、停止判断全部交给模型

- **Context 三层防御**：Auto-Compaction（Context 达 50% 自动压缩）+ Sub-Agent 隔离（派遣子 Agent 处理重型任务）+ Prompt Cache 经测学（追踪 14 个 cache-break 向量）

- **六层记忆**：组织级策略 → 项目 [CLAUDE.md](http://claude.md/) → 用户偏好 → Auto-Memory → 会话 → 子 Agent 记忆

- **五档权限**：plan/default/acceptEdits/dontAsk/bypassPermissions，权限设计像 UX 设计

- **TAOR 循环核心逻辑只有 50 行**，但给了模型无限的操作空间

## 提取的概念

- [TAOR 循环](concepts/TAOR 循环.md)

## 原始文章信息

- **作者**：Founder Park

- **来源**：微信公众号

- **发布日期**：2026-04-01

- **链接**：[https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw==&mid=2247523594](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw%3D%3D&mid=2247523594)

## 个人评注

这篇是整个 Claude Code 泳露事件中对架构剖析最全面、最有工程价值的文章。TAOR 循环和五档权限设计是 Tizer 构建自己 Agent 系统的重要参考。
