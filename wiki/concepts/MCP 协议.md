---
title: MCP 协议
type: concept
tags:
- MCP 协议
status: 已审核
confidence: high
last_compiled: '2026-04-22'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/842a872c175b40e389fb91a964f18530
notion_id: 842a872c-175b-40e3-89fb-91a964f18530
---

## 定义

MCP（Model Context Protocol，模型上下文协议）是 Anthropic 于 2024 年底发布的开放协议，规定了 AI 模型与外部工具（数据库、API、文件系统等）之间的标准化通信格式。类似于 USB 接口之于外设，MCP 解决了 AI 工具连接的碎片化问题。

## 关键要点

- **核心价值**：统一 AI 与外部工具的连接格式，解决各家（OpenAI Function Calling、LangChain Tool 等）各自一套的碎片化问题

- **架构**：AI 客户端 → MCP 服务器（工具适配层）→ 实际服务

- **在演进路线中的位置**：MCP 解决「连通性」（AI 能连接什么），是 Skills 和 Plugin 的基础层

- **局限性**：只解决连通性，不解决「AI 知不知道怎么用工具」的问题

## 来源引用

- [摘要：我研究了Anthropic这个金融服务Plugin仓库，发现AI正在做一件比写代码更可怕的事](summaries/摘要：我研究了Anthropic这个金融服务Plugin仓库，发现AI正在做一件比写代码更可怕的事.md)（老码小张, 2026-02-28）— MCP → Skills → Plugin 演进分析

- [摘要：Claude Code + Apify，无障碍抓取全网数据](summaries/摘要：Claude Code + Apify，无障碍抓取全网数据.md)（AI编程实验室，2026-03-02）— Apify MCP Server 通过 MCP 协议接入 15000+ Actor 实现灵活数据采集

- [摘要：mcp-use——Agent MCP 服务全栈开发框架](summaries/摘要：mcp-use——Agent MCP 服务全栈开发框架.md)（王鹏LLM，2026-03-03）— 全栈跨语言 MCP 开发框架，支持 TS/Python 双语言 SDK

- [摘要：Gate MCP Skills：让 AI Agent 直接操盘加密交易的新基础设施](summaries/摘要：Gate MCP Skills：让 AI Agent 直接操盘加密交易的新基础设施.md)

- [摘要：Chrome DevTools MCP：让 AI 助手直接操控你正在用的浏览器](summaries/摘要：Chrome DevTools MCP：让 AI 助手直接操控你正在用的浏览器.md)（X书签，2026-03-16）— 展示 MCP 在浏览器调试与当前会话接管中的落地

- [摘要：PANews 推出官方 AI Skills 工具集：让 AI 直接读懂加密新闻](summaries/摘要：PANews 推出官方 AI Skills 工具集：让 AI 直接读懂加密新闻.md)（X书签，2026-03-17）— 体现垂直媒体把内容能力封装为 Agent 技能接口的路线

- [摘要：DailyNews：6551Team 推出的永久免费加密新闻日报 MCP Server](summaries/摘要：DailyNews：6551Team 推出的永久免费加密新闻日报 MCP Server.md)（X书签，2026-03）— 展示 MCP 在加密情报分发中的轻量接入方式

- [摘要：Nunchi agent-cli：在 Hyperliquid 上跑 14 个开源量化策略，还能接 Claude Code 和 MCP](summaries/摘要：Nunchi agent-cli：在 Hyperliquid 上跑 14 个开源量化策略，还能接 Claude Code 和 MCP.md)（X书签文章）— 原文链接：[https://x.com/maid_crypto/status/2034493385344765966](https://x.com/maid_crypto/status/2034493385344765966)

- [摘要：Unusual Whales MCP：让 Claude 和 Cursor 直接调用专业美股交易数据](summaries/摘要：Unusual Whales MCP：让 Claude 和 Cursor 直接调用专业美股交易数据.md)（X书签文章）— 原文链接：[https://x.com/oragnes/status/2034570577667850436](https://x.com/oragnes/status/2034570577667850436)

- [原文链接](https://x.com/axiaisacat/status/2036750597622260206)｜摘要：OpenSpace：让 AI Agent 从「会做事」进化到「会学习」的开源引擎（来源条目）

- [原文链接](https://x.com/AYi_AInotes/status/2042970104921542896)｜[摘要：Shopify刚放了个大招，绝大多数人估计半年后才会反应过来。](summaries/摘要：Shopify刚放了个大招，绝大多数人估计半年后才会反应过来。.md)（来源条目）

- [摘要：模型只是引擎，System Prompt 才是底盘：用 Claude 优化自身的迁移实验](summaries/摘要：模型只是引擎，System Prompt 才是底盘：用 Claude 优化自身的迁移实验.md)（X书签文章）— 原文链接：[https://x.com/outsource_/status/2040345259335422463](https://x.com/outsource_/status/2040345259335422463)

- [摘要：Google Stitch 2.0 + Claude Code：独立开发者终于有了自己的设计师](summaries/摘要：Google Stitch 2.0 + Claude Code：独立开发者终于有了自己的设计师.md)（X书签文章）— 原文链接：[https://x.com/0xKingsKuan/status/2040357839714275647](https://x.com/0xKingsKuan/status/2040357839714275647)

- [摘要：96.6%召回率，0美元成本：这款开源AI记忆系统凭什么超越一切付费方案](summaries/摘要：96.6%召回率，0美元成本：这款开源AI记忆系统凭什么超越一切付费方案.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIxNzQwNjM3NA%3D%3D&mid=2247546207&idx=1&sn=772820dba9a7a0a037b4bad24eee51ad&chksm=962fbc784ab760b642a982a17ee1b7a251fc8dd1573eef97759423d6400035677c10ff9ab5ae#rd)｜[摘要：这个 Skill 太硬了，刚开源就斩获 2.8K 星标！Agent 联网能力拉满！](summaries/摘要：这个 Skill 太硬了，刚开源就斩获 2.8K 星标！Agent 联网能力拉满！.md)

- [摘要：code-review-graph：Claude Code 本地知识图谱，减少 6.8 倍代码审查 Token !](summaries/摘要：code-review-graph：Claude Code 本地知识图谱，减少 6.8 倍代码审查 Token !.md)

- [摘要：我是怎么运作的：内观一个自进化 Agent 的 Harness](summaries/摘要：我是怎么运作的：内观一个自进化 Agent 的 Harness.md)

- [摘要：Learn more in the official documentation](summaries/摘要：Learn more in the official documentation.md)

- [摘要：Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比](summaries/摘要：Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比.md)

- [摘要：Hermes Agent 从中级到高级进阶指南](summaries/摘要：Hermes Agent 从中级到高级进阶指南.md)

- [摘要：Notion Custom Agents复盘：三年重写5次，Notion 历史上最成功的新功能之一](summaries/摘要：Notion Custom Agents复盘：三年重写5次，Notion 历史上最成功的新功能之一.md)（源文章）

- [摘要：上手实测小红书评论爬取分析｜开源项目MediaCrawler+NotebookLM洞察选品机会](summaries/摘要：上手实测小红书评论爬取分析｜开源项目MediaCrawler+NotebookLM洞察选品机会.md)（来源条目）

- [摘要：Agent 的"手"长出来了，但为什么还是不可靠？](summaries/摘要：Agent 的手长出来了，但为什么还是不可靠？.md)（来源条目）

- [摘要：刚刚开源就斩获 46K+ Star！生化危机女主在 GitHub 开源了一个本地 AI 记忆系统！](summaries/摘要：刚刚开源就斩获 46K+ Star！生化危机女主在 GitHub 开源了一个本地 AI 记忆系统！.md)（来源条目）

- [摘要：How to Connect Claude to TradingView (FULL GUIDE)](summaries/摘要：How to Connect Claude to TradingView (FULL GUIDE).md)（来源条目）

- [摘要：OpenAI祭出GPT-5.4神装！Codex同款Harness全面开放](summaries/摘要：OpenAI祭出GPT-5.4神装！Codex同款Harness全面开放.md)（源文章）

- [摘要：Hermes Agent新手教程：从入门到精通，附带变现方式](summaries/摘要：Hermes Agent新手教程：从入门到精通，附带变现方式.md)（来源条目）

- [摘要：Creating a Second Brain with Claude Code](summaries/摘要：Creating a Second Brain with Claude Code.md)（来源条目）

- [摘要：真香！这可能是openclaw抓取任何网页的终极解决方案了](summaries/摘要：真香！这可能是openclaw抓取任何网页的终极解决方案了.md)（源文章）

- [摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了"持久大脑"，持续的高质量上下文，这事靠谱了](summaries/摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了持久大脑，持续的高质量上下文，这事靠谱了.md)

- 摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了"持久大脑"，持续的高质量上下文，这事靠谱了

- [摘要：Here are the 3 Core Pillars of Every AI Agent's Context](summaries/摘要：Here are the 3 Core Pillars of Every AI Agent's Context.md)（[原文](https://x.com/Ai_Vaidehi/status/2045050337149513974)）

- [摘要：上交大54页综述讲透Agent认知外部化的演进之路](summaries/摘要：上交大54页综述讲透Agent认知外部化的演进之路.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651029194&idx=2&sn=d468f16ac694682f072e150ac531e5a2&chksm=85cd02c33fc1ca1088db4f4f1a5b2219ed652157b32c004b7ef2cfb994654cfdfdd0d38512e7#rd)）

## 关联概念

- [RAG](concepts/RAG.md)

- Gate MCP Skills

- 《Gate MCP Skills：让 AI Agent 直接操盘加密交易的新基础设施》（NFTCPS，2026-03）— 展示 MCP 协议在交易所原生 Agent 接入中的落地方式

- [OpenSpace](entities/OpenSpace.md)

- 《OpenSpace：让 AI Agent 从「会做事」进化到「会学习」的开源引擎》｜X书签文章｜原文链接：[https://x.com/axiaisacat/status/2036750597622260206](https://x.com/axiaisacat/status/2036750597622260206)｜来源条目：摘要：OpenSpace：让 AI Agent 从「会做事」进化到「会学习」的开源引擎

- [Shopify AI Toolkit](entities/Shopify AI Toolkit.md)

- [Agent 原生电商后台](concepts/Agent 原生电商后台.md)

- [Agent 审计与回滚机制](concepts/Agent 审计与回滚机制.md)

- [MemPalace](entities/MemPalace.md)

- [AAAK 方言](concepts/AAAK 方言.md)

- [web-access](entities/web-access.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Claude Code](entities/Claude Code.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [OpenClaw](entities/OpenClaw.md)

- [ClawShell](entities/ClawShell.md)

- [Gateway](concepts/Gateway.md)

- [Notion Custom Agents](entities/Notion Custom Agents.md)

- [Coding Agent](concepts/Coding Agent.md)

- [软件工厂](concepts/软件工厂.md)

- [MediaCrawler](entities/MediaCrawler.md)

- [NotebookLM](entities/NotebookLM.md)

- [CDP 直连](concepts/CDP 直连.md)

- [Tool Calling 2.0](entities/Tool Calling 2.0.md)

- [CLI-Anything](entities/CLI-Anything.md)

- [AutoSkill](concepts/AutoSkill.md)

- [SKILL.md](concepts/SKILL.md.md)

- [LongMemEval](concepts/LongMemEval.md)

- [ChromaDB](entities/ChromaDB.md)

- [OpenAI Agents SDK](entities/OpenAI Agents SDK.md)

- [Agent Skills](concepts/Agent Skills.md)

- [多智能体编排](concepts/多智能体编排.md)

- [Cron 自动化](concepts/Cron 自动化.md)

- [第二大脑系统](concepts/第二大脑系统.md)

- [code-review-graph](entities/code-review-graph.md)

- [Tree-sitter](entities/Tree-sitter.md)

- 爆炸半径分析

- [增量更新](concepts/增量更新.md)

- [代码知识图谱](concepts/代码知识图谱.md)

- [Dokobot](entities/Dokobot.md)

- [llm-wiki](entities/llm-wiki.md)

- [MemPalace](entities/MemPalace.md)

- [wiki-mempalace-bridge](entities/wiki-mempalace-bridge.md)

- [wake-up 协议](concepts/wake-up 协议.md)

- [wiki-mempalace-bridge](entities/wiki-mempalace-bridge.md)

- [wake-up 协议](concepts/wake-up 协议.md)

- [llm-wiki](entities/llm-wiki.md)

- [A2A 协议](concepts/A2A 协议.md)

- [AG-UI](concepts/AG-UI.md)
