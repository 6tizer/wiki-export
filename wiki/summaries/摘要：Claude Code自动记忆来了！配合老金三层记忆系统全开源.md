---
title: 摘要：Claude Code自动记忆来了！配合老金三层记忆系统全开源
type: summary
tags:
- LLM
- 记忆系统
- 开发工具
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: Agent, LLM, 自动化, Claude
source_article_url: ''
notion_url: https://www.notion.so/991a9ff7d9494653a6a6684d362ae95e
notion_id: 991a9ff7-d949-4653-a6a6-684d362ae95e
---

## 一句话摘要

Claude Code v2.1.59 上线自动记忆功能（[MEMORY.md](http://memory.md/)），作者对比官方方案和自研三层记忆系统（Layer 1 知识图谱 + Layer 2 每日笔记 + Layer 3 隐性知识），结论是两套结合才是最优解。

## 关键洞察

- **官方自动记忆核心变化**：从「你写 [CLAUDE.md](http://claude.md/)，Claude 读」变为「Claude 自己写 [MEMORY.md](http://memory.md/)，自己读」。[CLAUDE.md](http://claude.md/) 是用户指令（权威性最高），[MEMORY.md](http://memory.md/) 是 Claude 笔记（自动学习）。

- **三层 DIY 记忆架构**：Layer 1 通过 Hooks 自动积累知识图谱（items.json + status 字段管理生命周期），Layer 2 自动生成每日笔记，Layer 3 手动维护隐性知识。三层合计约 1500 token，占 200K 上下文不到 1%。

- **官方赢在知识发现，DIY 赢在知识管理**：官方用 AI 语义理解判断什么值得记（碾压级别），但缺少过期管理、Git 追踪、团队共享、Token 精确控制。

- **Claude Code Hooks 是关键技术**：SessionStart（加载记忆）、PostToolUse（提取知识）、PreCompact（压缩前保存状态）三个 Hook 实现完全自动化。

- **已知问题**：Token 消耗增加（18 分钟轻度对话消耗 8% 配额）、记忆是影子状态（不可 Git 追踪）、[MEMORY.md](http://memory.md/) 重复加载 Bug。

## 提取的概念

- Claude Code Hooks

- mcp-memory-service

- Claude Code Memory（已有词条）

- [Auto Memory](concepts/Auto Memory.md)（已有词条）

- 记忆分层架构（已有词条）

## 原始文章信息

- **作者**：老金带你玩AI

- **来源**：微信公众号

- **发布时间**：2026-02-28

- **链接**：[https://mp.weixin.qq.com/s?__biz=MzI0NzU2MDgyNA==&mid=2247491498&idx=1&sn=e7728ae976c0773677ffbbe92457ce05](https://mp.weixin.qq.com/s?__biz=MzI0NzU2MDgyNA%3D%3D&mid=2247491498&idx=1&sn=e7728ae976c0773677ffbbe92457ce05)

## 个人评注

对 Tizer 的知识管理工作流极具参考价值。Hooks 机制（SessionStart/PostToolUse/PreCompact）的模式可以类比到 Wiki Compiler 的自动编译流程——本质都是「事件触发 → 知识提取 → 结构化存储」。三层记忆架构的 status 字段设计（active/superseded）也可以借鉴到 Wiki 条目的生命周期管理中。开源项目 claude-memory-3layer 值得关注。
