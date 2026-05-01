---
title: 摘要：用OpenClaw+Obsidian搭建内容工厂
type: summary
tags:
- 内容自动化
- 知识管理
- 多Agent协作
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-10'
source_tags: OpenClaw, Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/ac93d84e08d84eee87f7062c68276cb0
notion_id: ac93d84e-08d8-4eee-87f7-062c68276cb0
---

## 一句话摘要

通过 OpenClaw + Obsidian 的组合构建内容生产系统，利用 Symlink 打通多 Agent 工作区、YAML 元数据管理和 SOP 标准作业程序，形成从灵感捕获到发布归档的全流程自动化内容工厂。

## 关键洞察

- **核心架构**：Obsidian 作为本地知识数据库（双向链接 + YAML 元数据）+ OpenClaw 作为 7×24 后台驱动引擎

- **Symlink 跨 Agent 共享**：将 Obsidian 库建在中立路径，通过软链接映射到多个 Agent 工作区，实现数据共享又不破坏沙盒安全

- **安全防护**：严禁 OpenClaw 直接使用 mv/rm 操作 Obsidian 文件，必须通过 obsidian-cli 保护双向链接拓扑

- **四阶段内容流转**：灵感与素材库 → 选题池 → 内容工厂（大纲/初稿/终稿）→ 已发布归档，YAML 属性作为 AI 识别状态的唯一索引

- **四份核心配置**：[SOUL.md](http://soul.md/)（安全红线）、[USER.md](http://user.md/)（风格设定）、[AGENTS.md](http://agents.md/)（启动必读）、SOP_[GZH.md](http://gzh.md/)（标准作业程序）

## 提取的概念

- Obsidian Skills（已有/新建 Wiki 条目，已追加引用）

## 原始文章信息

- **作者**：饼干哥哥AGI

- **来源**：微信公众号

- **发布时间**：2026-03-01

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=MjM5NDI4MTY3NA%3D%3D&mid=2257498975&idx=1&sn=c035ee9d79ff444ac74d6b8466ff5f1d)

## 个人评注

Symlink 架构解决了多 Agent 共享知识库的核心难题，这个模式可以迁移到 Tizer 的工作流中。SOP 文件的设计思路（触发条件→标准动作）与 Wiki Compiler Agent 的 Ingest Process 异曲同工。YAML 元数据管理是确保 Agent 不迷路的关键——与 Wiki Schema 的规则文件理念一致。
