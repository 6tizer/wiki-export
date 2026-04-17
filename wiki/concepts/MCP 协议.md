---
title: MCP 协议
type: concept
tags:
- Agent 技能
status: 已审核
confidence: high
last_compiled: '2026-04-17'
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

- 《我研究了Anthropic金融服务Plugin仓库》（老码小张, 2026-02-28）— MCP → Skills → Plugin 演进分析

- 《Claude Code + Apify，无障碍抓取全网数据》（AI编程实验室，2026-03-02）— Apify MCP Server 通过 MCP 协议接入 15000+ Actor 实现灵活数据采集

- 《mcp-use——Agent MCP 服务全栈开发框架》（王鹏LLM，2026-03-03）— 全栈跨语言 MCP 开发框架，支持 TS/Python 双语言 SDK

- 摘要：Gate MCP Skills：让 AI Agent 直接操盘加密交易的新基础设施

- 《Chrome DevTools MCP：让 AI 助手直接操控你正在用的浏览器》— X书签，2026-03-16：展示 MCP 在浏览器调试与当前会话接管中的落地

- 《PANews 推出官方 AI Skills 工具集：让 AI 直接读懂加密新闻》— X书签，2026-03-17：体现垂直媒体把内容能力封装为 Agent 技能接口的路线

- 《DailyNews：6551Team 推出的永久免费加密新闻日报 MCP Server》— X书签，2026-03：展示 MCP 在加密情报分发中的轻量接入方式

- 《Nunchi agent-cli：让 AI 在 Hyperliquid 上自主交易的开源全栈方案》｜X书签文章｜原文链接：[https://x.com/maid_crypto/status/2034493385344765966](https://x.com/maid_crypto/status/2034493385344765966)

- 《Unusual Whales MCP：让 Claude 和 Cursor 直接调用专业美股交易数据》｜X书签文章｜原文链接：[https://x.com/oragnes/status/2034570577667850436](https://x.com/oragnes/status/2034570577667850436)

- [原文链接](https://x.com/axiaisacat/status/2036750597622260206)｜《OpenSpace：让 AI Agent 从「会做事」进化到「会学习」的开源引擎》｜来源条目：摘要：OpenSpace：让 AI Agent 从「会做事」进化到「会学习」的开源引擎

- [原文链接](https://x.com/AYi_AInotes/status/2042970104921542896)｜《Shopify刚放了个大招，绝大多数人估计半年后才会反应过来。》｜来源条目：Shopify AI Toolkit：把 AI Agent 变成你的电商运营团队

- 《模型只是引擎，System Prompt 才是底盘：用 Claude 优化自身的迁移实验》｜X书签文章｜原文链接：[https://x.com/outsource_/status/2040345259335422463](https://x.com/outsource_/status/2040345259335422463)｜来源条目：[摘要：模型只是引擎，System Prompt 才是底盘：用 Claude 优化自身的迁移实验](summaries/摘要：模型只是引擎，System Prompt 才是底盘：用 Claude 优化自身的迁移实验.md)

- 《Google Stitch 2.0 + Claude Code：独立开发者终于有了自己的设计师》｜X书签文章｜原文链接：[https://x.com/0xKingsKuan/status/2040357839714275647](https://x.com/0xKingsKuan/status/2040357839714275647)｜来源条目：[摘要：Google Stitch 2.0 + Claude Code：独立开发者终于有了自己的设计师](summaries/摘要：Google Stitch 2.0 + Claude Code：独立开发者终于有了自己的设计师.md)

- [原文链接](https://mp.weixin.qq.com/s/1rY6qMBqSELEm83MbhDzLA)｜《96.6%召回率，0美元成本：这款开源AI记忆系统凭什么超越一切付费方案》｜来源条目：[摘要：96.6%召回率，0美元成本：这款开源AI记忆系统凭什么超越一切付费方案](summaries/摘要：96.6%召回率，0美元成本：这款开源AI记忆系统凭什么超越一切付费方案.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIxNzQwNjM3NA%3D%3D&mid=2247546207&idx=1&sn=772820dba9a7a0a037b4bad24eee51ad&chksm=962fbc784ab760b642a982a17ee1b7a251fc8dd1573eef97759423d6400035677c10ff9ab5ae#rd)｜《这个 Skill 太硬了，刚开源就斩获 2.8K 星标！Agent 联网能力拉满！》

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ%3D%3D&mid=2247484353&idx=1&sn=f2ad30ea21fee327daac93a9143a76fb&chksm=f539ae6800aa8066504c6b4ed683e14b501d516a93882ddd92b4c501a2537281c3b85d7d3c8f#rd)｜《code-review-graph：Claude Code 本地知识图谱，减少 6.8 倍代码审查 Token !》｜来源条目：[摘要：code-review-graph：Claude Code 本地知识图谱，减少 6.8 倍代码审查 Token !](summaries/摘要：code-review-graph：Claude Code 本地知识图谱，减少 6.8 倍代码审查 Token !.md)

- [原文链接](https://x.com/yuanhao/status/2043490301294022741)｜《我是怎么运作的：内观一个自进化 Agent 的 Harness》｜来源条目：[摘要：我是怎么运作的：内观一个自进化 Agent 的 Harness](summaries/摘要：我是怎么运作的：内观一个自进化 Agent 的 Harness.md)

- [原文链接](https://x.com/claudeai/status/2044131493966909862)｜《Learn more in the official documentation》｜来源条目：[摘要：Learn more in the official documentation](summaries/摘要：Learn more in the official documentation.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzE5ODM0MDIyNg%3D%3D&mid=2247484011&idx=1&sn=588c8c9f5f8a8e56cb1d32c5ba91947a&chksm=976d338b09e0fcd9565bdfc1728262bd18a93f1408aecb26a19ba94a31968423d172955f1a51#rd)｜《Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比》｜来源条目：[摘要：Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比](summaries/摘要：Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比.md)

- [原文链接](https://x.com/BTCqzy1/status/2044259795499450414)｜《Hermes Agent 从中级到高级进阶指南》｜来源条目：[摘要：Hermes Agent 从中级到高级进阶指南](summaries/摘要：Hermes Agent 从中级到高级进阶指南.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw%3D%3D&mid=2247523808&idx=1&sn=0a6aea0c1f3f9c5c6e86eff9592fd30b&chksm=c17464df982ee29fa92c7272b71d87b2dc6c54287a5fd8e61657920ebeb34565f22f3d893ff4#rd)｜《Notion Custom Agents复盘：三年重写5次，Notion 历史上最成功的新功能之一》｜源文章：Notion Custom Agents复盘：三年重写5次，Notion 历史上最成功的新功能之一

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzE5ODAwODU4Mw%3D%3D&mid=2247488491&idx=1&sn=d8956b196055794081700b920e951cbd&chksm=9794196c6e4419b94a1e1d6ba4dbf929b9b30dd49537839c1c3180ef6219f4455d55bf79eeae#rd)｜《上手实测小红书评论爬取分析｜开源项目MediaCrawler+NotebookLM洞察选品机会》｜来源条目：[摘要：上手实测小红书评论爬取分析｜开源项目MediaCrawler+NotebookLM洞察选品机会](summaries/摘要：上手实测小红书评论爬取分析｜开源项目MediaCrawler+NotebookLM洞察选品机会.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzg2NzQ4MTI5Nw%3D%3D&mid=2247484183&idx=1&sn=19d63da8469d8144bc75d9b5d96eb2a5&chksm=cf51bf7f2bbc808c4595a0b312c5385bc05ec91b701c72f7c3c5849e96e54a8581348a50997b#rd)｜《Agent 的"手"长出来了，但为什么还是不可靠？》｜来源条目：[摘要：Agent 的"手"长出来了，但为什么还是不可靠？](summaries/摘要：Agent 的手长出来了，但为什么还是不可靠？.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ%3D%3D&mid=2247505903&idx=1&sn=d9f6ab8c463b8d5e883f51ffcf133c45&chksm=c121bbb7f887f2a99a0cc4e1ce630437181d622f5c30a1064e566c02e77a5f7082ea79d11ab1#rd)｜《刚刚开源就斩获 46K+ Star！生化危机女主在 GitHub 开源了一个本地 AI 记忆系统！》｜来源条目：[摘要：刚刚开源就斩获 46K+ Star！生化危机女主在 GitHub 开源了一个本地 AI 记忆系统！](summaries/摘要：刚刚开源就斩获 46K+ Star！生化危机女主在 GitHub 开源了一个本地 AI 记忆系统！.md)

- [原文链接](https://x.com/milesdeutscher/status/2044536031991763414)｜《How to Connect Claude to TradingView (FULL GUIDE)》｜来源条目：[摘要：How to Connect Claude to TradingView (FULL GUIDE)](summaries/摘要：How to Connect Claude to TradingView (FULL GUIDE).md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652692712&idx=1&sn=608b9832517125a701a13bfd13a99cb6&chksm=f01e31dc247eca9744e9d6e321351659ba0974b8ddea7e9b635d9eb34363255c700453927790#rd)｜《OpenAI祭出GPT-5.4神装！Codex同款Harness全面开放》｜源文章：OpenAI祭出GPT-5.4神装！Codex同款Harness全面开放

- [原文链接](https://x.com/jiroucaigou/status/2044249069699428665)｜《Hermes Agent新手教程：从入门到精通，附带变现方式》｜来源条目：[摘要：Hermes Agent新手教程：从入门到精通，附带变现方式](summaries/摘要：Hermes Agent新手教程：从入门到精通，附带变现方式.md)

- [原文链接](https://x.com/rywiggs/status/2044448092477661638)｜《Creating a Second Brain with Claude Code》｜来源条目：[摘要：Creating a Second Brain with Claude Code](summaries/摘要：Creating a Second Brain with Claude Code.md)

- [原文链接](https://mp.weixin.qq.com/s/2k5S5UlZKqACLr8g1Mb2eQ)｜《真香！这可能是openclaw抓取任何网页的终极解决方案了》｜源文章：真香！这可能是openclaw抓取任何网页的终极解决方案了

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493215&idx=1&sn=7cc67138b3f4025466cb3a64a55c8109&chksm=c0ccfbe465f303ae41c71f66e977f5051c02fda3d0eb7a62327f390e017b04181fb0fcbff59e#rd)｜《Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了"持久大脑"，持续的高质量上下文，这事靠谱了》｜来源条目：[摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了"持久大脑"，持续的高质量上下文，这事靠谱了](summaries/摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了持久大脑，持续的高质量上下文，这事靠谱了.md)

- [摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了"持久大脑"，持续的高质量上下文，这事靠谱了](summaries/摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了持久大脑，持续的高质量上下文，这事靠谱了.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493215&idx=1&sn=7cc67138b3f4025466cb3a64a55c8109&chksm=c0ccfbe465f303ae41c71f66e977f5051c02fda3d0eb7a62327f390e017b04181fb0fcbff59e#rd)）

## 关联概念

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

- [Tool Calling 2.0](concepts/Tool Calling 2.0.md)

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

- [爆炸半径分析](concepts/爆炸半径分析.md)

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
