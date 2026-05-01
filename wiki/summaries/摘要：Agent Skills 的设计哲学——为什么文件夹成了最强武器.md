---
title: 摘要：Agent Skills 的设计哲学——为什么文件夹成了最强武器
type: summary
tags:
- Agent 协作模式
- 上下文管理
- 提示工程
status: 已审核
confidence: high
last_compiled: '2026-04-10'
source_tags: Agent, LLM, 自动化, skills
source_article_url: ''
notion_url: https://www.notion.so/Tizer/bc3546c88fec462495f67dbdbc9bdcc0
notion_id: bc3546c8-8fec-4624-95f6-7dbdbc9bdcc0
---

## 一句话摘要

OpenAI 开发者体验工程师 Gabriel Chua 解释 Agent Skills 的设计哲学：Skills 本质是可重复使用的提示词文件夹，通过渐进式披露、结构化和额外资源访问三大机制，将隐性流程显性化为可共享、可一致执行的标准工作流。

## 关键洞察

- **Skills = 可重复使用的提示词**：核心是 [skill.md](http://skill.md/) 文件 + 示例/模板/脚本，打包成 Agent 可反复用的流程

- **三大差异化机制**：① 渐进式披露（先看简短说明，相关时才加载完整指令）② 结构（文件系统本身提供上下文）③ 额外资源访问（附录、MCP 服务器、CLI 脚本等）

- **团队价值**：将口口相传的程序性知识编码固化，新成员不用从头反推，更新一次 Skill 即可全局生效

- **核心判断标准**：如果同一个流程重复超过几次，它就应该变成一个 Skill

- **本质**：不是新能力，而是把隐性流程变成显性、可共享、可一致执行的方法

## 提取的概念

- 渐进式披露（Agent Skills 上下文管理策略，与 Obsidian Skills 三层加载一致）

## 原始文章信息

- **作者**：机智流（翻译自 Gabriel Chua/OpenAI）

- **来源**：微信公众号

- **发布时间**：2026-03-02

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDgzMA%3D%3D&mid=2247555220&idx=1&sn=e95a600d4b08122c98def85c7ec6f05a)

## 个人评注

「渐进式披露」是 Skills 设计最优雅的地方——与 Wiki Compiler 的按需加载策略完全对应。「隐性流程显性化」的理念直接适用于 Tizer 的 HITL 工作流标准化。Gabriel 提出的「重复超过几次就该变成 Skill」是一条非常实用的判断标准。
