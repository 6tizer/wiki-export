---
title: Hermes Agent
type: entity
tags:
- Agent 框架
status: 已审核
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/e47e7d37ec9f452a80c270954a83ee35
notion_id: e47e7d37-ec9f-452a-80c2-70954a83ee35
---

## 定义

Hermes Agent 是一个具备三层记忆系统、技能自迭代和内置安全机制的自进化AI助手，定位为OpenClaw的实用互补工具，支持导入OpenClaw配置快速迁移。

## 核心要点

- **三层记忆系统**：工作记忆（当前任务）+ 情节记忆（历史经验）+ 语义记忆（领域知识）

- **技能自迭代**：Agent能自动记录解决方案并在后续任务中复用，实现持续自我优化

- **安全机制**：内置操作权限管理，防止Agent越界操作

- **与OpenClaw互补**：Hermes更适合需要自主学习的长期任务；OpenClaw更适合高控制场景

- **快速迁移**：支持导入OpenClaw的配置和设置

## 对比 OpenClaw

| 维度 | Hermes | OpenClaw |

| --- | --- | --- |

| 设计哲学 | 自动化+自主学习 | 透明度+高控制 |

| 技能系统 | 自动归纳经验 | 手动编写Skill |

| 适用场景 | 自主长期任务 | 高控制开发场景 |

## 项目数据

- GitHub Stars：20,700+

- 消息平台适配：18+（Telegram、Discord、Slack、WhatsApp、Signal、微信企业版等）

- MCP 协议原生支持：可接入任何 MCP 工具服务器

- 多 LLM Provider 支持：OpenRouter、OpenAI、Anthropic、本地模型一键切换

## hermes-rs：Rust 重写版

hermes-rs 是对 hermes-agent Python 版的 Rust 重写，将 50,000 行压缩到 5,000 行，13 个 crate 模块化设计。

GitHub: [https://github.com/coder-brzhang/hermes-rs](https://github.com/coder-brzhang/hermes-rs)

## 来源引用

- [摘要：【万字】CC vs OpenClaw vs Hermes：一文深入拆解三大 Agent 框架](summaries/摘要：【万字】CC vs OpenClaw vs Hermes：一文深入拆解三大 Agent 框架.md)（[原文](https://mp.weixin.qq.com/s?__biz=MjM5NjE3NjYzMw%3D%3D&mid=2247496422&idx=1&sn=811535695480b3dedead76bdd49ebfc0&chksm=a707de0ce8531ae0d9d8a14dd5c1029fc10a9cf68cd3421d8de580646f70da173af4f671ec62#rd)）

- [摘要：Hermes Agent 生态要炸了，这波进化速度把我整不会了！](summaries/摘要：Hermes Agent 生态要炸了，这波进化速度把我整不会了！.md)（[原文](https://x.com/NFTCPS/status/2046076635200553224)）

- [摘要：TOP FIVE GITHUB REPOSITORIES THIS WEEK](summaries/摘要：TOP FIVE GITHUB REPOSITORIES THIS WEEK.md)（[原文](https://x.com/RoundtableSpace/status/2045906520672461309)）

- [摘要：GBrain v0.13 dropped](summaries/摘要：GBrain v0.13 dropped.md)（[原文](https://x.com/garrytan/status/2046002383021555986)）

- [摘要：本周增长最快的 GitHub 仓库：](summaries/摘要：本周增长最快的 GitHub 仓库：.md)（[原文](https://x.com/pritipatelfgoo/status/2045105855662809267)）

- [摘要：Introducing expanded coverage for image generation models in Hermes Agent and Nous Portal Tool Gateway!](summaries/摘要：Introducing expanded coverage for image generation models in Hermes Agent and Nous Portal Tool Gateway!.md)（[原文](https://x.com/NousResearch/status/2045004711699640463)）

- [摘要：Hermes Agent 上手指南：安装后必试的十件事与八大亮点全解析](summaries/摘要：Hermes Agent 上手指南：安装后必试的十件事与八大亮点全解析.md)（[原文](https://x.com/LufzzLiz/status/2042237123865297267)）

- [摘要：兄弟们，昨天配了一个新的bot，在我的失误下，把两个机器人部署到同一个目录下面，成功把旧bot搞炸了](summaries/摘要：兄弟们，昨天配了一个新的bot，在我的失误下，把两个机器人部署到同一个目录下面，成功把旧bot搞炸了.md)（[原文](https://x.com/AnchorNode/status=2044675901775126986)）

- [摘要：Browser Use × Hermes Agent：每个开源 Agent 现在都有了免费的云端浏览器](summaries/摘要：Browser Use × Hermes Agent：每个开源 Agent 现在都有了免费的云端浏览器.md)（[原文](https://x.com/YuLin807/status/2042198758260158535)）

- [摘要：Hermes Agent实测，龙虾新对手是进化爱马仕](summaries/摘要：Hermes Agent实测，龙虾新对手是进化爱马仕.md)（卡尔的AI沃茨，微信，2026-04-08）

- [摘要：？？不是，咋又来了一个 Hermes？](summaries/摘要：？？不是，咋又来了一个 Hermes？.md)（cxuanAI，微信，2026-04-09）

- 摘要：10,000+ markdown files（@AYi_AInotes，2026-04-10）— GBrain 作为 OpenClaw/Hermes Agent 的官方记忆后端开源

- 《如何使用Hermes Agent稳定爬取公众号文章》——Draco正在VibeCoding（微信，2026-04-11）：介绍了通过 Browser Use / Camoufox 封装微信公众号爬取 skill 的实战流程

- [摘要：Obsidian + Claude Code：用 AI 大神 Karpathy 的方法搭一个真正可用的第二大脑（全教程）](summaries/摘要：Obsidian + Claude Code：用 AI 大神 Karpathy 的方法搭一个真正可用的第二大脑（全教程）.md)（[原文](https://x.com/lxfater/status/2042848343949480173)）

- [摘要：Hermes WebUI：给 Hermes Agent 装上浏览器界面，CLI 党也能优雅用 AI](summaries/摘要：Hermes WebUI：给 Hermes Agent 装上浏览器界面，CLI 党也能优雅用 AI.md)（[原文](https://x.com/TheTuringPost/status/2040936147720048909)，来源条目）

- [摘要：Hermes WebUI：给 Hermes Agent 装上浏览器界面，CLI 党也能优雅用 AI](summaries/摘要：Hermes WebUI：给 Hermes Agent 装上浏览器界面，CLI 党也能优雅用 AI.md)（[原文](https://x.com/TheTuringPost/status/2040936147720048909)，源文章）

- [摘要：用 50 行 Python 跑通 Google A2A 协议：Hermes + OpenClaw 的多 Agent 互联实践](summaries/摘要：用 50 行 Python 跑通 Google A2A 协议：Hermes + OpenClaw 的多 Agent 互联实践.md)（[原文](https://x.com/YuLin807/status/2041667865477312551)，源文章）

- [摘要：同步阻塞 vs 异步编排：Hermes Delegate 与 OpenClaw 多 Agent 机制深度实战对比](summaries/摘要：同步阻塞 vs 异步编排：Hermes Delegate 与 OpenClaw 多 Agent 机制深度实战对比.md)（[原文](https://x.com/servasyy_ai/status/2042951017462169812)，来源条目）

- [摘要：Evolutionary self-improvement for Hermes Agent](summaries/摘要：Evolutionary self-improvement for Hermes Agent.md)（[原文](https://x.com/KKaWSB/status/2043119101028274268)，来源条目）

- [原文链接](https://x.com/SHL0MS/status/2043415274196435325)｜《SHL0MS | HERMES AGENT》｜来源条目：[摘要：SHL0MS | HERMES AGENT](summaries/摘要：SHL0MS  HERMES AGENT.md)

- [摘要：MiniMax M2.7 × Hermes Agent：开启自我进化的 Agent 工作流](summaries/摘要：MiniMax M2.7 × Hermes Agent：开启自我进化的 Agent 工作流.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzE5MTA3NzcxMQ%3D%3D&mid=2247488335&idx=1&sn=ece0fb7411d313acd1c583c84b748538&chksm=971ff5041a501710ae6c94e032c8f8d009fe38dd0edd9fbf16d3d392baedc9c670020c3bf213#rd)，来源条目）

- [原文链接](https://x.com/claudeai/status/2042308622181339453)｜《Claude 推出 Advisor Strategy》｜源文章：Claude Advisor Strategy：用 Sonnet 的钱，买 Opus 的脑子

- [摘要：3 Things I learnt after 3 weeks of using Hermes as a personal analyst](summaries/摘要：3 Things I learnt after 3 weeks of using Hermes as a personal analyst.md)（[原文](https://x.com/0xJeff/status/2043656911044870203)，来源条目）

- [摘要：斯坦福报告：美国AI投资为中国23倍，但模型差距消失；Q1豆包海外版下载7200万次；OpenAI指控Anthropic：300亿收入80亿造假 | 极客早知道](summaries/摘要：斯坦福报告：美国AI投资为中国23倍，但模型差距消失；Q1豆包海外版下载7200万次；OpenAI指控Anthropic：300亿收入80亿造假  极客早知道.md)（[原文](https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ%3D%3D&mid=2653103929&idx=1&sn=2e50fcd0464ff901c9ed770fc5dc01ce&chksm=7fa47587eb83e5092d967cd46f7886f4d5697b473655d34cf8d8dffbdf101f3cd662464fd2bd#rd)，来源条目）

- [摘要：用Hermes写的Hermes报告](summaries/摘要：用Hermes写的Hermes报告.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkyMDU4ODUwMw%3D%3D&mid=2247491544&idx=1&sn=74e54eb8e10fc81c93dae3e3d94bdf39&chksm=c0a9321173cd0bd2645a10b315050a4e45203835a1003f4b9f723b22140091f833bc5113a12f#rd)，来源条目）

- [摘要：不想碰命令行？Hermes 现在有图形界面了](summaries/摘要：不想碰命令行？Hermes 现在有图形界面了.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzk0NzQzOTczOA%3D%3D&mid=2247524083&idx=1&sn=91e2da0ea49f7a6dfe39ed118b3ccef1&chksm=c2b08eb2250002d244c3bc0c693ac6604e07ae4021320792b3d71baa679ed5d172196478ad6e#rd)，来源条目）

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzE5ODM0MDIyNg%3D%3D&mid=2247484011&idx=1&sn=588c8c9f5f8a8e56cb1d32c5ba91947a&chksm=976d338b09e0fcd9565bdfc1728262bd18a93f1408aecb26a19ba94a31968423d172955f1a51#rd)｜《Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比》｜来源条目：[摘要：Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比](summaries/摘要：Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比.md)

- [摘要：Hermes Agent 从入门到精通：25 个致命坑避坑实战指南](summaries/摘要：Hermes Agent 从入门到精通：25 个致命坑避坑实战指南.md)（[原文](https://x.com/BTCqzy1/status/2043210007358148893)，来源条目）

- [摘要：多Agent团队协作才是Hermes Agent的正确打开方式。](summaries/摘要：多Agent团队协作才是Hermes Agent的正确打开方式。.md)（[原文](https://x.com/Saccc_c/status/2044018336673964207)，来源条目）

- [摘要：Hermes Agent 从中级到高级进阶指南](summaries/摘要：Hermes Agent 从中级到高级进阶指南.md)（[原文](https://x.com/BTCqzy1/status/2044259795499450414)，来源条目）

- [摘要：Hermes Agent抄袭中国团队代码实锤！被锤后回应：你删号](summaries/摘要：Hermes Agent抄袭中国团队代码实锤！被锤后回应：你删号.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652692364&idx=1&sn=806ef08f63d5bf567d421f8808528c22&chksm=f047438bdb7b8b7734f13ec8b0c731b8c3a0085d501b9d6454c92b66b5d973bec5e7bce653ea#rd)，来源条目）

- [摘要：抽丝剥茧：深度解析 Hermes Agent 万字系统提示词（System Prompt）构成](summaries/摘要：抽丝剥茧：深度解析 Hermes Agent 万字系统提示词（System Prompt）构成.md)（[原文](https://x.com/LufzzLiz/status/2044258384556556743)，来源条目）

- [摘要：How Skills Work in Hermes Agent](summaries/摘要：How Skills Work in Hermes Agent.md)（[原文](https://x.com/NeoAIForecast/status/2044252861710905685)，来源条目）

- [原文链接](https://x.com/Teknium/status/2044329280201732217)｜《⚠️ Pre-beta — GUI not yet wired to core functions.》｜来源条目：摘要：⚠️ Pre-beta — GUI not yet wired to core functions.

- [摘要：The Ultimate Hermes Guide - from one agent to a 4-profile team that still feels coherent on day 30](summaries/摘要：The Ultimate Hermes Guide - from one agent to a 4-profile team that still feels coherent on day 30.md)（[原文](https://x.com/nyk_builderz/status/2044472463279710344)，来源条目）

- [摘要：Hermes Agent新手教程：从入门到精通，附带变现方式](summaries/摘要：Hermes Agent新手教程：从入门到精通，附带变现方式.md)（[原文](https://x.com/jiroucaigou/status/2044249069699428665)，来源条目）

- [摘要：OpenClaw 与 Hermes Agent 官方核心文档架构对比](summaries/摘要：OpenClaw 与 Hermes Agent 官方核心文档架构对比.md)（源文章页面）

- [摘要：Hermes 核心文档架构详尽分析与优化方案指南](summaries/摘要：Hermes 核心文档架构详尽分析与优化方案指南.md)（源文章）

- [摘要：Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮](summaries/摘要：Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIwMzY3Njc2MA%3D%3D&mid=2247484484&idx=1&sn=b877810761905accec8c61a88f1d20f3&chksm=97732bf3c04982b7874037c0a69fa13851f4885059370a3951a7a9094c6b6aba2a24fd85addc#rd)，来源条目）

- [摘要：2026年的开源社区，已经不是人在玩AI了，已经进化到 AI在玩AI，玩得比人类还好很多😆😆😆](summaries/摘要：2026年的开源社区，已经不是人在玩AI了，已经进化到 AI在玩AI，玩得比人类还好很多😆😆😆.md)（[原文](https://x.com/AYi_AInotes/status/2044964220005965927)，来源条目）

- [摘要：妈耶 HermesAgent直播回应抄没抄国内开发者](summaries/摘要：妈耶 HermesAgent直播回应抄没抄国内开发者.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg3MTk3NzYzNw%3D%3D&mid=2247506451&idx=1&sn=aec841a1c8c8ec2a99d64536babf7eae&chksm=cf1f5a4baf411e277ea71f2add117a204ea05d54a3884c6c63f8d79ec931d7d3a48694ae7f43#rd)，来源条目）

- [摘要：Hermes+AutoCLI+Obsidian： 打造自动入库、自动整理、自动微信汇报的知识系统](summaries/摘要：Hermes+AutoCLI+Obsidian： 打造自动入库、自动整理、自动微信汇报的知识系统.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI1MjkyNjI4NQ%3D%3D&mid=2247486639&idx=1&sn=afab9bd6fc7a268a719127ebbf1c368a&chksm=e8fcaa80f3faf33cce6201ed6bc26ddccfa5d6d6fc0c8dc4f51adf0fe53479ebd7ed270f0d14#rd)，来源条目）

- [摘要：我把Hermes官方UI卸载了，换成了这个（强烈推荐）](summaries/摘要：我把Hermes官方UI卸载了，换成了这个（强烈推荐）.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI2NjY5MjQzNQ%3D%3D&mid=2247484066&idx=1&sn=ce0a80a4e845c299dfcd7657277dfcab&chksm=eb567d729812b0d01454660a9b5ca7be3bd1ae5455eaf0ea2cba904bfa35775ad0e17f1bd1d6#rd)）

- [摘要：🚀 限时白嫖！3分钟搞定 小米 MiMo V2 Pro 接入 Hermes Agent「完整教程」](summaries/摘要：🚀 限时白嫖！3分钟搞定 小米 MiMo V2 Pro 接入 Hermes Agent「完整教程」.md)（[原文](https://x.com/Lonely__MH/status/2043311492037280078)）

- [摘要：Enable Tool Gateway](summaries/摘要：Enable Tool Gateway.md)（[原文](https://x.com/NousResearch/status/2044878344592699744)）

- [摘要：上次在 Hermes 里小米模型免费用，登录他们后台一看，这不是模型中转贩子吗？仔细一瞧居然有自研模型，再仔细研究一下，发现这家公司真不简单！](summaries/摘要：上次在 Hermes 里小米模型免费用，登录他们后台一看，这不是模型中转贩子吗？仔细一瞧居然有自研模型，再仔细研究一下，发现这家公司真不简单！.md)（[原文](https://x.com/laogui/status/2044930449538191713)）

- [摘要：Hermes Agent Creative Hackathon 正式启动](summaries/摘要：Hermes Agent Creative Hackathon 正式启动.md)（[原文](https://x.com/NousResearch/status/2045225469088326039)）

- [摘要：The Ultimate Guide to Running a Headless Mac mini for AI agents](summaries/摘要：The Ultimate Guide to Running a Headless Mac mini for AI agents.md)（[原文](https://x.com/mronge/status/2045234739679011144)）

- [摘要：AI researchers and engineers](summaries/摘要：AI researchers and engineers.md)（[原文](https://x.com/ollama/status/2045282803387158873)）

- [摘要：Hermes 多 Agent 深水区：三个高级实战技巧](summaries/摘要：Hermes 多 Agent 深水区：三个高级实战技巧.md)（[原文](https://x.com/BTCqzy1/status/2045720855137903046)）

- [摘要：Ollama 一键启动 Hermes Agent：免费、本地、会自我进化的 AI 私人助手](summaries/摘要：Ollama 一键启动 Hermes Agent：免费、本地、会自我进化的 AI 私人助手.md)（[原文](https://x.com/Saboo_Shubham_/status/2045692123887050816)）

- [摘要：Hermes Agent 高阶工具全配置：从身份记忆到感知表达，一文打通](summaries/摘要：Hermes Agent 高阶工具全配置：从身份记忆到感知表达，一文打通.md)（[原文](https://x.com/ResearchWang/status/2045812932538438001)）

- [摘要：Interesting insights, especially this: Hermes starts off as any other agent does, inefficient and often not sure how to complete a task that is training didnt have priors for. However, solve it once a](summaries/摘要：Interesting insights, especially this- Hermes starts off as any other agent does, inefficient and often not sure how to complete a task that is training didnt have priors for. However, solve it once a.md)（[原文](https://x.com/Teknium/status/2046001396819067008)）

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzk0ODM5NTEyNA%3D%3D&mid=2247505880&idx=1&sn=f1a5297d812535a2bffac2d7e0d7a9b0&chksm=c290cdf6c57d4eebecc0e36e7eba979efdecf65bf353528554e2a3908ab30c9f60c80f772947#rd)｜《[hermes101.dev](http://hermes101.dev/) 上线了！5 分钟装完、7 天入门、OpenClaw 老用户无痛迁移》｜来源条目：[摘要：hermes101.dev 上线了！5 分钟装完、7 天入门、OpenClaw 老用户无痛迁移](summaries/摘要：hermes101.dev 上线了！5 分钟装完、7 天入门、OpenClaw 老用户无痛迁移.md)

## 关联概念

- [agentskills.io](concepts/agentskills.io.md)

- [CaMeL 信任边界](concepts/CaMeL 信任边界.md)

- [Hermes Alpha](entities/Hermes Alpha.md)

- [Skill Factory](entities/Skill Factory.md)

- [Maestro](entities/Maestro.md)

- [Icarus Plugin](entities/Icarus Plugin.md)

- [andrej-karpathy-skills](entities/andrej-karpathy-skills.md)

- [GenericAgent](entities/GenericAgent.md)

- [Hermes Messaging Gateway](concepts/Hermes Messaging Gateway.md)

- [OpenClaw 迁移](concepts/OpenClaw 迁移.md)

- [Multica](entities/Multica.md)

- [claude-mem](entities/claude-mem.md)

- [CLAUDE.md](concepts/CLAUDE.md.md)

- [Nous Tool Gateway](entities/Nous Tool Gateway.md)

- [OpenCLI](entities/OpenCLI.md)

- [AutoCLI.ai](entities/AutoCLI.ai.md)

- [LLM 知识编译](concepts/LLM 知识编译.md)

- [ClawBot](entities/ClawBot.md)

- [多 Agent 协作工作流](concepts/多 Agent 协作工作流.md)

- [SOUL.md](concepts/SOUL.md.md)

- [AGENTS.md](concepts/AGENTS.md.md)

- [Obsidian](entities/Obsidian.md)

- [Claude Code](entities/Claude Code.md)

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [OpenClaw](entities/OpenClaw.md)

- [hermes101.dev](entities/hermes101.dev.md)

- [文件即大脑](concepts/文件即大脑.md)

- [Hermes WebUI](entities/Hermes WebUI.md)

- [Gateway](concepts/Gateway.md)

- [delegate_task](concepts/delegate_task.md)

- [Subagents 并行](concepts/Subagents 并行.md)

- [Stateless Ephemeral Unit](concepts/Stateless Ephemeral Unit.md)

- [LLM-Driven Replan](concepts/LLM-Driven Replan.md)

- [Subdirectory Hints](concepts/Subdirectory Hints.md)

- [Steer 机制](concepts/Steer 机制.md)

- [异步事件驱动编排](concepts/异步事件驱动编排.md)

- [Hermes Agent Self-Evolution](entities/Hermes Agent Self-Evolution.md)

- [GEPA](concepts/GEPA.md)

- [GEP 协议](concepts/GEP 协议.md)

- [DSPy](entities/DSPy.md)

- [技能自我进化](concepts/技能自我进化.md)

- [System Prompt 工程](concepts/System Prompt 工程.md)

- [Autoreason](concepts/Autoreason.md)

- [Advisor Strategy](concepts/Advisor Strategy.md)

- [Advisor Tool](concepts/Advisor Tool.md)

- [Ratchet-Driven Development](concepts/Ratchet-Driven Development.md)

- [持久化跨会话记忆](concepts/持久化跨会话记忆.md)

- [双记忆文件架构](concepts/双记忆文件架构.md)

- [Hindsight](entities/Hindsight.md)

- [Browser Use](entities/Browser Use.md)

- [OpenRouter](entities/OpenRouter.md)

- [GLM-5.1](entities/GLM-5.1.md)

- [MiniMax M2.7](entities/MiniMax M2.7.md)

- [LLM 长期记忆](concepts/LLM 长期记忆.md)

- [自我进化 Skills 系统](concepts/自我进化 Skills 系统.md)

- [AI 研究 AI](concepts/AI 研究 AI.md)

- [MCP 协议](concepts/MCP 协议.md)

- [Honcho](entities/Honcho.md)

- [ClawShell](entities/ClawShell.md)

- [WSL2](entities/WSL2.md)

- [Ollama](entities/Ollama.md)

- [llm-wiki-compiler](entities/llm-wiki-compiler.md)

- [Context Bleed](concepts/Context Bleed.md)

- Prompt Injection

- [Agent-curated memory](concepts/Agent-curated memory.md)

- [Frozen Snapshot](concepts/Frozen Snapshot.md)

- [Agent-Managed Skills](concepts/Agent-Managed Skills.md)

- [EvoMap](entities/EvoMap.md)

- [Evolver](entities/Evolver.md)

- [AI洗代码](concepts/AI洗代码.md)

- [ModelBox](entities/ModelBox.md)

- [程序性记忆](concepts/程序性记忆.md)

- [Browser Connect](concepts/Browser Connect.md)

- [TinyAgentOS](entities/TinyAgentOS.md)

- [taOSmd](entities/taOSmd.md)

- [Memory KPI](concepts/Memory KPI.md)

- [Policy Gate](concepts/Policy Gate.md)

- [team-agents.md](concepts/team-agents.md.md)

- [Agent Skills](concepts/Agent Skills.md)

- [记忆分层架构](concepts/记忆分层架构.md)

- [多智能体编排](concepts/多智能体编排.md)

- [调用链验证](concepts/调用链验证.md)

- [Token 污染](concepts/Token 污染.md)

- [Polling 抢消息](concepts/Polling 抢消息.md)

- [USER.md](concepts/USER.md.md)

- [文件即大脑](concepts/文件即大脑.md)

- [Gemma 4](entities/Gemma 4.md)

- [Abliteration](concepts/Abliteration.md)

- [Refusal Direction](concepts/Refusal Direction.md)

- [过度对齐](concepts/过度对齐.md)

- [Nous Research](entities/Nous Research.md)

- [Nous Portal](entities/Nous Portal.md)

- [Crawl4AI](entities/Crawl4AI.md)

- CamoFox

- [agency-agents-zh](entities/agency-agents-zh.md)

- [Nous Tool Gateway](entities/Nous Tool Gateway.md)
