---
title: 摘要：Here's a fun skill you can teach your OpenClaw/Hermes — Book Mirror
type: summary
tags:
- 知识管理
- 提示工程
- OpenClaw
status: 已审核
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: https://www.notion.so/351701074b6881559ae8ef9ad0973049
notion_url: https://www.notion.so/Tizer/776de0f5b87a43ae82de16660095c563
notion_id: 776de0f5-b87a-43ae-82de-16660095c563
---

## 一句话摘要

Book Mirror 是一种 OpenClaw/Hermes Skill，通过将书籍内容与 AI 对读者的长期记忆交叉映射，生成逐章双栏个性化分析——左栏保留原书核心内容，右栏用读者自己的真实经历做镜像映射。

## 关键洞察

- **双栏结构是质量检验器**：左栏要详尽到可以替代原书，右栏要具体到使用读者自己的话、真实人名和日期——这种结构让 AI 是否真正了解读者一目了然

- **上下文决定一切**：对陌生人执行 Book Mirror 只是书摘，对拥有多年对话记录、治疗笔记和关系模式的用户执行才是「镜像」——长期记忆是核心壁垒

- **Pipeline 设计**：获取书籍 → 按章拆分 → 构建 Context Pack（读者档案） → 逐章双栏分析 → 事实核查 → 输出 PDF，每一步都有明确质量标准

- **禁止泛化建议**：不允许「consider reflecting on...」式的空洞建议，无关章节直接标注不适用，宁缺毋滥

- **社区反馈积极**：评论中有人将其与 Obsidian 二脑、Readwise 等工具结合使用，也有人指出冷启动问题——新账号缺乏上下文时退化为普通摘要

## 提取的概念

- [Book Mirror](concepts/Book Mirror.md)：核心概念，个性化书籍分析技术

- [OpenClaw](entities/OpenClaw.md)：执行平台，作为 Skill 宿主

- [Hermes Agent](entities/Hermes Agent.md)：执行平台，与 OpenClaw 并列支持该 Skill

## 原始文章信息

- **作者**：@garrytan（Garry Tan，Y Combinator CEO）

- **来源**：X 书签

- **发布时间**：2026-04-28

- **原文链接**：[https://x.com/garrytan/status/2049059060427952164](https://x.com/garrytan/status/2049059060427952164)

## 个人评注

Book Mirror 的核心洞察——「右栏质量取决于上下文深度」——与 OpenClaw 的长期记忆生态高度契合。对 Tizer 的知识管理工作流而言，这种模式可以延伸到技术文档阅读场景：将书籍替换为论文或技术 spec，将个人上下文替换为项目背景和代码库状态，实现「读一篇论文就自动映射到当前项目」的效果。值得关注的是评论中提到的 llm-wiki-compiler 作为「inner infra」的思路，与当前 Wiki Compiler Agent 的设计理念一致。
