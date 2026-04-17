---
title: 摘要：10,000+ markdown files（GBrain 开源发布）
type: summary
tags:
- 知识管理
- 记忆系统
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, OpenClaw, 自动化
source_article_url: ''
notion_url: https://www.notion.so/51bc8d1b1e7747818573fe99d3c0ca8f
notion_id: 51bc8d1b-1e77-4781-8573-fe99d3c0ca8f
---

## 一句话摘要

YC 总裁 Garry Tan 将自己运行多年的生产级 AI Agent 记忆系统 GBrain 完整开源（MIT 协议），其核心是用 Markdown 文件 + Postgres/pgvector 构建的「编译真相+时间线」知识模型，与 OpenClaw/Hermes Agent 深度集成。

## 关键洞察

- **规模验证可信度高**：Garry 本人已用 GBrain 管理 10,000+ Markdown 文件、3,000+ 人物档案、13 年日历数据、5,800 条 Apple Notes，是真实生产配置而非 Demo

- **知识模型是核心**：编译真相（可重写的最优理解）+ 时间线（只增不改的证据链）分离，使知识既保持简洁又保留溯源

- **从 grep 到向量的门槛**：文件数 < 500 用 grep 足够，超过 1,000-3,000 后必须引入 pgvector + 混合检索（向量 + 关键词 + RRF 融合）

- **Dream Cycle 自动维护**：OpenClaw 的 [DREAMS.md](http://dreams.md/) / Hermes Agent 的 nightly cron 每晚扫描当天对话，自动富化实体、修复引用、整合记忆，实现睡后脑子更聪明

- **GBRAIN_SKILLPACK 是灵魂**：Fat Markdown Skill 文件告诉 Agent **如何**使用 GBrain（脑-Agent 循环、实体检测、富化流水线、会议摄入），而非仅提供命令列表

## 提取的概念

- [GBrain](entities/GBrain.md)

- OpenClaw

- [Hermes Agent](entities/Hermes Agent.md)

- OpenClaw Dreaming（睡眠记忆机制）

- [pgvector](concepts/pgvector.md)

- [编译真相+时间线模式](concepts/编译真相+时间线模式.md)

## 原始文章信息

- **作者**：@AYi_AInotes（阿绎 AYi）/ 引用推文作者：@garrytan（Garry Tan）

- **来源**：X 书签

- **发布时间**：2026-04-10

- **链接**：[https://x.com/AYi_AInotes/status/2042594992393458112](https://x.com/AYi_AInotes/status/2042594992393458112)

- **GitHub**：[garrytan/gbrain](https://github.com/garrytan/gbrain)（Stars: 2789，MIT 协议，TypeScript）

## 个人评注

GBrain 对 Tizer 的 OpenClaw 工作流高度相关：

- **OpenClaw 集成路径已明确**：`openclaw skills install gbrain` 即可接入，与现有 memory_search（运营状态）互补，GBrain 管世界知识，Agent memory 管行为配置

- **Dream Cycle 直接可复用**：OpenClaw 原生支持 [DREAMS.md](http://dreams.md/)，可直接启用 GBrain 的夜间自动富化逻辑，降低 HITL 负担

- **知识编译流水线参考**：GBrain 的「摄入 → 实体检测 → 富化 → 更新编译真相」循环，与本 Wiki Compiler Agent 的理念一致，可互相借鉴 Skill 文件写法

- **规模预判**：当 Notion Wiki 条目超过 1,000 时，应考虑引入 pgvector 做语义检索层，而非仅依赖 Notion 全文搜索
