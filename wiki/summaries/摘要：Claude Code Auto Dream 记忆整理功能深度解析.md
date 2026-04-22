---
title: 摘要：Claude Code Auto Dream 记忆整理功能深度解析
type: summary
tags:
- LLM
status: 已审核
confidence: high
last_compiled: '2026-04-10'
source_tags: Agent, LLM, 自动化, Claude
source_article_url: ''
notion_url: https://www.notion.so/1c208833e63547ef94562d62b81a61a7
notion_id: 1c208833-e635-47ef-9456-2d62b81a61a7
---

## 一句话摘要

AI Agent 的长期记忆会积累「技术债」，Claude Code 通过 Auto Memory 自动记录 + Auto Dream 后台整理的双机制，实现记忆系统的自我维护与持续优化。

## 关键洞察

- **记忆也有技术债**：旧决策与新决策矛盾、相对日期过时、已完结项目笔记残留，不清理反而让 Agent 变笨

- **Auto Dream 四步循环**：扫描现有记忆 → 识别问题（过时/矛盾/重复）→ 优化整理 → 写回文件，可作为通用记忆维护范式

- **记忆分层架构**：Claude Code 按项目隔离记忆，分为 [MEMORY.md](http://memory.md/)（索引）、user/（用户信息）、feedback/（反馈）、project/（项目进展）、reference/（外部资源）五层

- **「选择记什么」决定任务上限**：宝可梦案例中，Opus 4.6 精选 10 个记忆文件拿到 3 个道馆徽章，Sonnet 3.5 堆了 31 个文件仍卡在第二个城镇

- **Compaction + Memory Folder**：Anthropic Harness 指南推荐的两种记忆策略，Sonnet 4.5 使用 Memory Folder 后 BrowseComp-Plus 准确率从 60.4% 升至 67.2%

## 提取的概念

- Auto Dream

- [Auto Memory](concepts/Auto Memory.md)

- Compaction

- Memory Folder

- 记忆技术债

## 原始文章信息

- **作者**：数字生命卡兹克

- **来源**：微信公众号

- **发布时间**：未标注

- **链接**：未提供

## 个人评注

Auto Dream 的「扫描→识别→优化→写回」四步循环，与 Tizer 正在构建的 Wiki Lint Agent 高度契合——本质上都是对非结构化知识的定期清理与结构化维护。Claude Code 的记忆分层设计（索引 + 分类子目录）也可作为 OpenClaw 记忆分区方案的参考。文章提到的 mem0 记忆分区共享系统，正是 HITL 内容管线中记忆层的候选方案之一。
